"""Acceptance tests for private records through real Git and CLI boundaries."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_workflow_enforcement import CLOSE_LOOP, VALIDATOR, create_docs


class LocalSpecPolicyTests(unittest.TestCase):
    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory(prefix="workflow-private-")
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name)
        create_docs(self.root, complete=True)
        (self.root / ".gitignore").write_text(".spec/\n", encoding="utf-8")
        self.git("init", "-b", "main")
        self.git("add", ".")
        self.commit("baseline")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()
        (self.root / "app.py").write_text("print('changed')\n", encoding="utf-8")
        self.git("add", "app.py")
        self.commit("change")
        self.head = self.git("rev-parse", "HEAD").stdout.strip()

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.root), *args],
            capture_output=True, text=True, check=True,
        )

    def commit(self, message):
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com",
                 "commit", "-m", message)

    def validate(self, *extra, ticket="fixture", mode="ship"):
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(self.root),
             "--mode", mode, "--project-type", "team", "--spec-policy", "local-only",
             "--ticket", ticket, "--changed-file", "app.py", *extra],
            capture_output=True, text=True, timeout=20,
        )

    def hook(self, skip=False):
        env = os.environ.copy()
        env.pop("CLOSE_THE_LOOP", None)
        if skip:
            env["CLOSE_THE_LOOP"] = "skip"
        env["PRE_COMMIT_FROM_REF"] = self.base
        env["PRE_COMMIT_TO_REF"] = self.head
        return subprocess.run(
            [sys.executable, str(CLOSE_LOOP), "--spec-policy", "local-only",
             "--ticket", "fixture"], cwd=self.root, env=env,
            capture_output=True, text=True, timeout=20,
        )

    def assert_result(self, result, success, message=""):
        output = result.stdout + result.stderr
        self.assertEqual(success, result.returncode == 0, output)
        if message:
            self.assertIn(message, output)

    def test_complete_ignored_local_records_pass_without_spec_in_diff(self):
        self.assert_result(self.validate(), True)
        self.assertEqual("", self.git("ls-files", "--", ".spec").stdout)

    def test_missing_ticket_fails_without_exposing_content(self):
        self.assert_result(self.validate(ticket="missing"), False, "does not exist")

    def test_incomplete_records_fail_ship_but_pass_wip(self):
        path = self.root / ".spec/fixture/tasks.md"
        path.write_text(path.read_text().replace("[x]", "[ ]"), encoding="utf-8")
        self.assert_result(self.validate(), False, "unchecked")
        self.assert_result(self.validate(mode="wip"), True)

    def test_explicit_local_policy_cannot_read_outside_spec(self):
        for ticket in ("../fixture", "../../outside", "C:/private", "/private", "a/../fixture"):
            with self.subTest(ticket=ticket):
                self.assert_result(self.validate(ticket=ticket), False, "ticket")

    def test_force_staged_private_file_is_rejected_even_if_not_a_living_doc(self):
        private = self.root / ".spec/fixture/audit.md"
        private.write_text("PRIVATE_FIXTURE_CONTENT", encoding="utf-8")
        self.git("add", "-f", str(private))
        result = self.validate()
        self.assert_result(result, False, "tracked")
        self.assertNotIn("PRIVATE_FIXTURE_CONTENT", result.stdout + result.stderr)

    def test_local_hook_uses_private_records_for_code_only_push(self):
        self.assert_result(self.hook(), True)

    def test_local_hook_does_not_skip_when_spec_directory_is_missing(self):
        (self.root / ".spec").rename(self.root / "private-records")
        self.assert_result(self.hook(), False, "does not exist")

    def test_local_hook_checks_structure(self):
        path = self.root / ".spec/fixture/current.md"
        path.write_text(path.read_text() + "\n<TBD>\n", encoding="utf-8")
        self.assert_result(self.hook(), False, "placeholder")

    def test_legacy_skip_cannot_disable_explicit_local_policy(self):
        path = self.root / ".spec/fixture/current.md"
        path.write_text(path.read_text() + "\n<TBD>\n", encoding="utf-8")
        self.assert_result(self.hook(skip=True), False, "placeholder")

    def test_local_only_requires_an_explicit_ticket(self):
        self.assert_result(self.validate(ticket=""), False, "--ticket")

    def test_index_only_cleanup_of_previously_published_records_is_allowed(self):
        self.git("add", "-f", ".spec/fixture/current.md")
        self.commit("previously published private record")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("rm", "--cached", ".spec/fixture/current.md")
        self.commit("remove tracked record but preserve local evidence")
        self.head = self.git("rev-parse", "HEAD").stdout.strip()
        self.assert_result(self.hook(), True)
        self.assertTrue((self.root / ".spec/fixture/current.md").is_file())

    def test_local_hook_rejects_private_file_added_then_removed_in_outgoing_history(self):
        self.git("add", "-f", ".spec/fixture/current.md")
        self.commit("accidental private addition")
        self.git("rm", "--cached", ".spec/fixture/current.md")
        self.commit("remove private file from index")
        self.head = self.git("rev-parse", "HEAD").stdout.strip()
        self.assert_result(self.hook(), False, "outgoing commit")

    def test_default_policy_still_requires_changed_tracked_ticket_docs(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(self.root), "--mode", "ship",
             "--project-type", "team", "--changed-file", "app.py"],
            capture_output=True, text=True, timeout=20,
        )
        self.assert_result(result, False, "living document")


if __name__ == "__main__":
    unittest.main()
