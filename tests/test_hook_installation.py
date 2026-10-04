"""Exercise the distributed hook template through the actual pre-commit runner."""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from test_workflow_enforcement import create_docs


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("pre-commit") and shutil.which("git"), "pre-commit and git required")
class HookInstallationTests(unittest.TestCase):
    def test_template_launches_from_spaced_home_and_preserves_guard_results(self):
        with tempfile.TemporaryDirectory(prefix="workflow hook install ") as directory:
            root = Path(directory)
            fixture = root / "project"
            fixture.mkdir()
            profile = root / "user home"
            installed = profile / ".ai-workflow" / "scripts"
            installed.mkdir(parents=True)
            for name in ("check_close_the_loop.py", "validate_workflow_docs.py"):
                shutil.copy2(ROOT / "scripts" / name, installed / name)

            # Only the child process gets a disposable home; real user settings stay intact.
            env = dict(os.environ)
            env.update(HOME=str(profile), USERPROFILE=str(profile), PRE_COMMIT_HOME=str(root / "cache"))
            env.pop("CLOSE_THE_LOOP", None)
            env.pop("WORKFLOW_SPEC_POLICY", None)
            env.pop("WORKFLOW_TICKET", None)

            def git(*args):
                return subprocess.run(
                    ["git", "-C", str(fixture), *args], check=True,
                    capture_output=True, text=True, env=env,
                ).stdout.strip()

            git("init", "-b", "main")
            create_docs(fixture)
            template = (ROOT / "templates/pre-commit.template.yaml").read_text(encoding="utf-8")
            # Do not install unrelated third-party hooks; use the distributed local block unchanged.
            (fixture / ".pre-commit-config.yaml").write_text(
                template.split("  # ---- Universal ----", 1)[0], encoding="utf-8",
            )
            git("add", ".")
            git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.com", "commit", "-m", "baseline")
            base = git("rev-parse", "HEAD")
            (fixture / "app.py").write_text("print('changed')\n", encoding="utf-8")
            git("add", "app.py")
            git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.com", "commit", "-m", "code only")

            def run_hook():
                return subprocess.run(
                    ["pre-commit", "run", "close-the-loop", "--hook-stage", "pre-push",
                     "--from-ref", base, "--to-ref", "HEAD"],
                    cwd=fixture, env=env, capture_output=True, text=True, timeout=40,
                )

            blocked = run_hook()
            output = blocked.stdout + blocked.stderr
            self.assertNotEqual(0, blocked.returncode, output)
            self.assertIn("this push changes code but no living-tier doc", output)
            self.assertNotIn("can't open file", output)

            tasks = fixture / ".spec" / "fixture" / "tasks.md"
            tasks.write_text(tasks.read_text(encoding="utf-8") + "\nDraft verification in progress.\n", encoding="utf-8")
            git("add", str(tasks))
            git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.com", "commit", "-m", "record draft")
            allowed = run_hook()
            self.assertEqual(0, allowed.returncode, allowed.stdout + allowed.stderr)


if __name__ == "__main__":
    unittest.main()
