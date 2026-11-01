"""Regression oracles for the November workflow audit findings."""

import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_workflow_enforcement import (
    CLOSE_LOOP, ROOT, VALIDATOR, VALID_CURRENT, create_docs, run_bootstrap, run_validator, write,
)


class GitSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory(prefix="workflow-snapshot-")
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name)
        self.git("init", "-b", "main")
        self.git("config", "core.quotePath", "true")

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.root), *args],
            capture_output=True, text=True, check=True,
        ).stdout.strip()

    def commit(self, message):
        self.git("add", ".")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.com",
                 "commit", "-m", message)
        return self.git("rev-parse", "HEAD")

    def prepare_range(self, ticket="fixture", invalid=False):
        create_docs(self.root, ticket=ticket, complete=True)
        base = self.commit("baseline")
        write(self.root / "app.py", "print('changed')\n")
        for relative in (f".spec/{ticket}/current.md", f".spec/{ticket}/tasks.md",
                         "devlog.md", "todo.md"):
            path = self.root / relative
            path.write_text(path.read_text() + "\nChange recorded.\n", encoding="utf-8")
        if invalid:
            path = self.root / ".spec" / ticket / "current.md"
            path.write_text(path.read_text() + "\n<TBD>\n", encoding="utf-8")
        return base, self.commit("outgoing change")

    def ship(self, base, head):
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(self.root),
             "--mode", "ship", "--base", base, "--head", head],
            capture_output=True, text=True, timeout=20,
        )

    def hook(self, base, head):
        env = dict(os.environ, PRE_COMMIT_FROM_REF=base, PRE_COMMIT_TO_REF=head)
        env.pop("CLOSE_THE_LOOP", None)
        return subprocess.run(
            [sys.executable, str(CLOSE_LOOP)], cwd=self.root, env=env,
            capture_output=True, text=True, timeout=20,
        )

    def test_uncommitted_correction_cannot_validate_invalid_outgoing_revision(self):
        base, head = self.prepare_range(invalid=True)
        write(self.root / ".spec/fixture/current.md", VALID_CURRENT.replace("[ ]", "[x]"))
        for check in (self.ship, self.hook):
            with self.subTest(adapter=check.__name__):
                result = check(base, head)
                self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
                self.assertIn("placeholder", result.stdout + result.stderr)

    def test_dirty_placeholder_does_not_reject_a_valid_outgoing_revision(self):
        base, head = self.prepare_range()
        write(self.root / ".spec/fixture/current.md", "<TBD>\n")
        for check in (self.ship, self.hook):
            with self.subTest(adapter=check.__name__):
                result = check(base, head)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        explicit = run_validator(self.root, "ship", [
            ".spec/fixture/current.md", ".spec/fixture/tasks.md",
        ])
        self.assertNotEqual(0, explicit.returncode)
        self.assertIn("placeholder", explicit.stdout + explicit.stderr)

    def test_working_project_marker_cannot_weaken_outgoing_personal_policy(self):
        create_docs(self.root, complete=True)
        base = self.commit("baseline")
        write(self.root / "app.py", "print('changed')\n")
        for relative in (".spec/fixture/current.md", ".spec/fixture/tasks.md"):
            path = self.root / relative
            path.write_text(path.read_text() + "\nUpdated.\n", encoding="utf-8")
        head = self.commit("missing personal project records")
        write(self.root / "AGENTS.md", "Project type: team\n")
        result = self.ship(base, head)
        self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("devlog.md", result.stdout + result.stderr)

    def test_outgoing_records_are_checked_when_working_spec_directory_is_absent(self):
        base, head = self.prepare_range(invalid=True)
        (self.root / ".spec").rename(self.root / "working-records")
        for check in (self.ship, self.hook):
            with self.subTest(adapter=check.__name__):
                result = check(base, head)
                self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
                self.assertIn("placeholder", result.stdout + result.stderr)

    def test_unicode_ticket_passes_range_and_hook(self):
        base, head = self.prepare_range(ticket='測試 "quoted"')
        for check in (self.ship, self.hook):
            with self.subTest(adapter=check.__name__):
                result = check(base, head)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)


class MarkdownAndPlannerTests(unittest.TestCase):
    def test_ship_rejects_unfinished_items_for_each_markdown_list_marker(self):
        for marker in ("-", "*", "+", "1.", "2)"):
            with self.subTest(marker=marker), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                create_docs(root, complete=True)
                path = root / ".spec/fixture/tasks.md"
                path.write_text(path.read_text() + f"\n{marker} [ ] Pending real check\n",
                                encoding="utf-8")
                ship = run_validator(root, "ship", [".spec/fixture/tasks.md"])
                self.assertNotEqual(0, ship.returncode, ship.stdout + ship.stderr)
                self.assertIn("unchecked", ship.stdout + ship.stderr)
                wip = run_validator(root, "wip", [".spec/fixture/tasks.md"])
                self.assertEqual(0, wip.returncode, wip.stdout + wip.stderr)

    def test_fenced_asterisk_example_passes_but_hidden_unfinished_item_fails(self):
        for body, allowed in (
            ("~~~markdown\n* [ ] Example only\n~~~\n", True),
            ("~~~markdown\n<!-- * [ ] Example only -->\n~~~\n", True),
            ("~~~markdown\n<!--\n+ [ ] Example only\n-->\n~~~\n", True),
            ("~~~markdown\n<!-- * [ ] Example only\n~~~\n-->\n", True),
            ("~~~markdown\n<!-- Example\n~~~\n* [ ] Pending real check\n-->\n", False),
            ("<!-- * [ ] Pending real check -->\n", False),
            ("<!--\n+ [ ] Pending real check\n-->\n", False),
        ):
            with self.subTest(body=body), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                create_docs(root, complete=True)
                path = root / ".spec/fixture/tasks.md"
                path.write_text(path.read_text() + "\n" + body, encoding="utf-8")
                result = run_validator(root, "ship", [".spec/fixture/tasks.md"])
                self.assertEqual(allowed, result.returncode == 0, result.stdout + result.stderr)

    def test_packaged_planner_records_pass_wip(self):
        planner = (ROOT / "claude-code/plugin/agents/planner.md").read_text(encoding="utf-8")
        fence = chr(96) * 3
        blocks = re.findall(fence + r"markdown\n(.*?)" + fence, planner, re.DOTALL)
        self.assertEqual(2, len(blocks), "planner must show current and tasks examples")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for kind, block in zip(("current", "tasks"), blocks):
                completed = re.sub(r"<[^>\n]+>", "fixture evidence", block)
                completed = re.sub(r"(?m)^\.\.\.$", "Independent follow-up check.", completed)
                write(root / ".spec/fixture" / f"{kind}.md", completed)
            result = run_validator(root, "wip", [
                ".spec/fixture/current.md", ".spec/fixture/tasks.md",
            ])
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertIn("0 warning(s)", result.stdout)


@unittest.skipUnless(shutil.which("pwsh"), "PowerShell 7 required")
class BootstrapBranchTests(unittest.TestCase):
    def test_actual_remote_default_is_rejected_with_missing_or_stale_cache(self):
        for stale_cache in (False, True):
            for worktree in (False, True):
                with self.subTest(stale_cache=stale_cache, worktree=worktree), \
                        tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    repo, remote = root / "repo", root / "remote.git"

                    def git(*args):
                        return subprocess.run(["git", "-C", str(repo), *args],
                                              capture_output=True, text=True, check=True)

                    subprocess.run(["git", "init", "-b", "trunk", str(repo)],
                                   check=True, capture_output=True)
                    subprocess.run(["git", "init", "--bare", "-b", "trunk", str(remote)],
                                   check=True, capture_output=True)
                    write(repo / "README.md", "# Fixture\n")
                    git("add", ".")
                    git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.com",
                        "commit", "-m", "baseline")
                    git("remote", "add", "origin", str(remote))
                    git("push", "origin", "trunk")
                    git("switch", "-c", "main")
                    if stale_cache:
                        git("update-ref", "refs/remotes/origin/outdated", "HEAD")
                        git("symbolic-ref", "refs/remotes/origin/HEAD",
                            "refs/remotes/origin/outdated")
                    advertised = git("ls-remote", "--symref", "origin", "HEAD").stdout
                    self.assertIn("ref: refs/heads/trunk", advertised)
                    answers = [
                        "6", "", "", "", "", "", "1" if worktree else "2", "", "none", "", "",
                        "Fixture task", "Keep tasks isolated", "none", "No shared branch writes",
                        "Maintainers", "Task records", "none", "",
                    ]
                    result = run_bootstrap(repo, "trunk", answers)
                    self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
                    self.assertIn("shared", (result.stdout + result.stderr).lower())
                    self.assertFalse((repo / ".spec").exists())
                    self.assertEqual([], list(root.glob("repo-*")))
                    self.assertEqual("main", git("branch", "--show-current").stdout.strip())
                    if not stale_cache and not worktree:
                        git("remote", "set-url", "origin", str(root / "missing.git"))
                        unavailable = run_bootstrap(repo, "feature/task", answers)
                        self.assertNotEqual(0, unavailable.returncode)
                        self.assertIn("Cannot verify origin", unavailable.stderr)
                        self.assertFalse((repo / ".spec").exists())
                        self.assertEqual("main", git("branch", "--show-current").stdout.strip())
                        git("remote", "set-url", "origin", str(remote))
                    legitimate = run_bootstrap(repo, "feature/task", answers)
                    self.assertEqual(0, legitimate.returncode,
                                     legitimate.stdout + legitimate.stderr)
                    destination = root / "repo-feature-task" if worktree else repo
                    self.assertTrue((destination / ".spec/feature/task/current.md").is_file())

    def test_shared_and_actual_default_branches_are_not_ticket_destinations(self):
        for branch, worktree in (("main", False), ("master", False), ("dev", False),
                                 ("trunk", False), ("main", True), ("trunk", True)):
            with self.subTest(branch=branch, worktree=worktree), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                repo = root / "repo"
                repo.mkdir()
                subprocess.run(["git", "init", "-b", branch], cwd=repo, check=True,
                               capture_output=True)
                write(repo / "README.md", "# Fixture\n")
                subprocess.run(["git", "add", "."], cwd=repo, check=True, capture_output=True)
                subprocess.run([
                    "git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.com",
                    "commit", "-m", "baseline",
                ], cwd=repo, check=True, capture_output=True)
                if branch == "trunk":
                    subprocess.run(["git", "update-ref", "refs/remotes/origin/trunk", "HEAD"],
                                   cwd=repo, check=True, capture_output=True)
                    subprocess.run(["git", "symbolic-ref", "refs/remotes/origin/HEAD",
                                    "refs/remotes/origin/trunk"],
                                   cwd=repo, check=True, capture_output=True)
                answers = [
                    "6", "", "", "", "", "", "1" if worktree else "2", "", "none", "", "",
                    "Fixture task", "Keep tasks isolated", "none", "No shared branch writes",
                    "Maintainers", "Task records", "none", "",
                ]
                result = run_bootstrap(repo, branch, answers)
                self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
                self.assertIn("shared", (result.stdout + result.stderr).lower())
                self.assertFalse((repo / ".spec").exists(), "rejection must precede writes")
                self.assertEqual([], list(root.glob("repo-*")), "rejection must precede worktree creation")


if __name__ == "__main__":
    unittest.main()
