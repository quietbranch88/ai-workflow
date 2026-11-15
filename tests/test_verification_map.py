import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_workflow_enforcement import create_docs, run_validator, write, VALID_CURRENT, VALID_TASKS


CURRENT = VALID_CURRENT.replace('- [ ] Observable:', '- [ ] AC-1: Report contract\n  - Observable:')
TASKS = VALID_TASKS.replace('# Tasks', '# Tasks\n\nVerification map: required').replace(
    '  - Files: `report.py`',
    '  - Acceptance: AC-1\n'
    '  - Files: `report.py`\n'
    '  - Oracle: current.md AC-1 and the report schema contract\n'
    '  - Required boundary: report CLI against synthetic fixtures\n'
    '  - Detection: mutation: wrong report result fails unchanged assertions\n'
    '  - Evidence: audit.md records revision, environment, assertion and result',
)


class VerificationMapTests(unittest.TestCase):
    def fixture(self, root, current=CURRENT, tasks=TASKS, complete=True):
        create_docs(root, complete=complete)
        for name, value in [('current', current), ('tasks', tasks)]:
            write(root / '.spec/fixture' / (name + '.md'),
                  value.replace('- [ ]', '- [x]') if complete else value)

    def run_check(self, root, mode='ship'):
        return run_validator(root, mode, ['.spec/fixture/current.md', '.spec/fixture/tasks.md'])

    def test_complete_mapping_and_detection_alternatives_pass(self):
        for detection in ['mutation: relevant assertion failed and restored pass',
                          'fail-to-pass: same defect caught by baseline',
                          'not-applicable: behavior-neutral record correction']:
            with self.subTest(detection=detection), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                tasks = TASKS.replace('mutation: wrong report result fails unchanged assertions', detection)
                self.fixture(root, tasks=tasks)
                result = self.run_check(root)
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertIn('pass with 0 warning(s)', result.stdout)

    def test_missing_or_placeholder_evidence_fields_fail(self):
        for field in ['Oracle', 'Required boundary', 'Verify', 'Detection', 'Evidence']:
            for value in ['', '<pending>']:
                with self.subTest(field=field, value=value), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    tasks = '\n'.join('  - ' + field + ': ' + value if line.strip().startswith('- ' + field + ':') else line
                                      for line in TASKS.splitlines())
                    self.fixture(root, tasks=tasks)
                    result = self.run_check(root)
                    self.assertNotEqual(0, result.returncode, result.stdout)
                    self.assertIn(field, result.stderr)

    def test_filler_values_count_as_placeholders(self):
        for field in ['Oracle', 'Required boundary', 'Verify', 'Detection', 'Evidence']:
            for value in ['TODO', '...', 'N/A', '-', 'see <later> x']:
                with self.subTest(field=field, value=value), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    tasks = '\n'.join('  - ' + field + ': ' + value if line.strip().startswith('- ' + field + ':') else line
                                      for line in TASKS.splitlines())
                    self.fixture(root, tasks=tasks)
                    result = self.run_check(root)
                    self.assertNotEqual(0, result.returncode, result.stdout)
                    self.assertIn(field, result.stderr)

    def test_detection_explanation_cannot_be_filler(self):
        for invalid in ['mutation: TODO', 'mutation: ...', 'fail-to-pass: N/A']:
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.fixture(root, tasks=TASKS.replace(
                    'mutation: wrong report result fails unchanged assertions', invalid))
                result = self.run_check(root)
                self.assertNotEqual(0, result.returncode, result.stdout)
                self.assertIn('Detection', result.stderr)

    def test_other_list_markers_still_opt_in_and_are_checked(self):
        starred = '\n'.join(line.replace('  - ', '  * ', 1) if line.startswith('  - ') else line
                            for line in TASKS.splitlines())
        cases = {
            'starred fields, no marker': starred.replace('Verification map: required', ''),
            'starred fields, listed marker': starred.replace('Verification map: required',
                                                             '- Verification map: required'),
        }
        for name, tasks in cases.items():
            with self.subTest(case=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.fixture(root, tasks=tasks)
                self.assertEqual(0, self.run_check(root).returncode, 'complete starred record should pass')
            with self.subTest(case=name + ', empty Oracle'), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                broken = tasks.replace('  * Oracle: current.md AC-1 and the report schema contract', '  * Oracle:')
                self.fixture(root, tasks=broken)
                result = self.run_check(root)
                self.assertNotEqual(0, result.returncode, result.stdout)
                self.assertIn('Oracle', result.stderr)

    def test_missing_duplicate_unknown_or_uncovered_criterion_fails(self):
        cases = [
            (CURRENT.replace('AC-1:', 'No ID:'), TASKS),
            (CURRENT, TASKS.replace('Acceptance: AC-1', 'Acceptance: AC-9')),
            (CURRENT.replace('## Non-goals', '- [ ] AC-2: another requirement\n\n## Non-goals'), TASKS),
            (CURRENT.replace('## Non-goals', '- [ ] AC-1: duplicated requirement\n\n## Non-goals'), TASKS),
            (CURRENT, TASKS.replace('Acceptance: AC-1', 'Acceptance: AC-1, AC-1')),
            (CURRENT, TASKS.replace('Acceptance: AC-1', 'Acceptance: AC-1 garbage')),
            (CURRENT, TASKS.replace('Acceptance: AC-1', 'Acceptance:')),
            (CURRENT, TASKS.replace('  - Acceptance: AC-1\n', '')),
        ]
        for index, (current, tasks) in enumerate(cases):
            with self.subTest(case=index), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.fixture(root, current=current, tasks=tasks)
                self.assertNotEqual(0, self.run_check(root).returncode)

    def test_detection_requires_known_method_and_explanation(self):
        for invalid in ['mutation', 'mutation:', 'not-applicable:', 'unknown: passed',
                        'mutation: <evidence>', 'not-applicable: <reason>']:
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.fixture(root, tasks=TASKS.replace(
                    'mutation: wrong report result fails unchanged assertions', invalid))
                result = self.run_check(root)
                self.assertNotEqual(0, result.returncode)
                self.assertIn('Detection', result.stderr)

    def test_wip_accepts_planned_evidence_and_ship_rejects_open_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root, complete=False, tasks=TASKS.replace(
                'audit.md records revision, environment, assertion and result',
                'Not run; planned command above, pending environment'))
            self.assertEqual(0, self.run_check(root, 'wip').returncode)
            self.assertNotEqual(0, self.run_check(root, 'ship').returncode)

    def test_legacy_ticket_remains_compatible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            create_docs(root, complete=True)
            self.assertEqual(0, self.run_check(root).returncode)

    def test_recorded_commands_are_never_executed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            marker = root / 'must-not-exist'
            tasks = TASKS.replace('`python verify_report.py`', f'`touch {marker}`')
            self.fixture(root, tasks=tasks)
            self.assertEqual(0, self.run_check(root).returncode)
            self.assertFalse(marker.exists())

    def test_local_only_mapping_is_checked_without_tracking_private_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(['git', '-C', str(root), 'init', '-q'], check=True)
            self.fixture(root, tasks=TASKS.replace(
                'Evidence: audit.md records revision, environment, assertion and result', 'Evidence:'))
            from test_workflow_enforcement import VALIDATOR
            result = subprocess.run([sys.executable, str(VALIDATOR), '--root', str(root),
                                     '--spec-policy', 'local-only', '--ticket', 'fixture',
                                     '--changed-file', '.spec/fixture/tasks.md', '--mode', 'ship'],
                                    capture_output=True, text=True, timeout=20)
            self.assertNotEqual(0, result.returncode)
            self.assertIn('Evidence', result.stderr)
            tracked = subprocess.run(['git', '-C', str(root), 'ls-files', '.spec'],
                                     capture_output=True, text=True, check=True)
            self.assertEqual('', tracked.stdout)

    def test_fixed_revision_cannot_be_repaired_by_working_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.run(['git', '-C', str(root), *args], check=True,
                                      capture_output=True, text=True).stdout.strip()
            git('init', '-q')
            self.fixture(root)
            git('add', '.')
            git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'baseline')
            base = git('rev-parse', 'HEAD')
            self.fixture(root, tasks=TASKS.replace('  - Evidence: audit.md records revision, environment, assertion and result',
                                                 '  - Evidence:'))
            git('add', '.')
            git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'incomplete evidence')
            head = git('rev-parse', 'HEAD')
            self.fixture(root)
            from test_workflow_enforcement import VALIDATOR
            result = subprocess.run([sys.executable, str(VALIDATOR), '--root', str(root),
                                     '--mode', 'ship', '--base', base, '--head', head],
                                    capture_output=True, text=True, timeout=20)
            self.assertNotEqual(0, result.returncode, result.stdout)
            self.assertIn('Evidence', result.stderr)
