# Tasks

Verification map: required

- [x] task-1: Add mapped task validation and public CLI regression fixtures.
  - Acceptance: AC-1, AC-2, AC-3
  - Files: scripts/validate_workflow_docs.py; tests/test_verification_map.py
  - Oracle: current.md AC-1 through AC-3, existing WIP/Ship and immutable-range contracts.
  - Required boundary: real validator CLI and disposable local Git fixtures.
  - Verify: python3 -m unittest discover -s tests -p test_verification_map.py
  - Detection: fail-to-pass: new regressions must reject incomplete mapped records
    against the original validator; a safe gate-removal mutation must also fail.
  - Evidence: audit.md records the failing baseline, 9 unchanged-test mutation assertions,
    restored pass, final 107-test suite and target-commit/privacy CLI fixtures.
- [x] task-2: Update canonical guidance, templates and declared mirrors; verify delivery.
  - Acceptance: AC-4
  - Files: docs/verification.md; templates/spec.md; templates/tasks.md; package metadata;
    declared builder mirror; devlog.md; todo.md
  - Oracle: current.md AC-4 and the existing canonical/mirror distribution contract.
  - Required boundary: repository tests, local package checks and tracked Ship validation.
  - Verify: python3 -m unittest discover -s tests; strict plugin checks; Ship validator
  - Detection: not-applicable: guidance and packaging identity use claim/mirror checks;
    executable gate behavior is covered by task-1.
  - Evidence: audit.md records the final 107-test suite, strict plugin checks,
    changed-document links and syntax checks; dedicated scanners are unavailable.

## Acceptance

- [x] All AC IDs map to checks, independent sources and scoped evidence.
- [x] Failing baseline or mutation and restoration are observed, not merely planned.
- [x] Existing modes, target-commit reads and private-record boundaries remain intact.
- [x] Local verification and publication/activation are reported separately.
