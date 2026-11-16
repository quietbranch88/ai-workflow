# Tasks

Verification map: required

- [x] task-1: Correct indented IDs and directly adjacent generic/HTML evidence.
  - Acceptance: AC-1, AC-2
  - Files: scripts/validate_workflow_docs.py; tests/test_verification_map.py
  - Oracle: independent findings IR-01/IR-02 and current.md; existing list grammar and content compatibility.
  - Required boundary: real CLI with temporary synthetic records.
  - Verify: python3 -m unittest discover -s tests -p test_verification_map.py
  - Detection: fail-to-pass: unchanged new tests failed 8 assertions on merged main; preserve the tests while fixing behavior.
  - Evidence: audit.md records 8 baseline assertion failures, final pass, 21 independent probes and source hash.
- [x] task-2: Prepare security receipts, final checks and the authorized follow-up PR.
  - Acceptance: AC-3
  - Files: task records; devlog.md; todo.md; authorized GitHub branch and PR.
  - Oracle: explicit user authorization to review/scan, fix and open PR; no main merge.
  - Required boundary: final local revision, scanners, GitHub readback and hosted CI.
  - Verify: repository suite, WIP/Ship/package checks, scan commands and PR receipts.
  - Detection: not-applicable: delivery metadata uses source/readback checks; executable defects are covered by task-1.
  - Evidence: audit.md records 113 passing tests, independent review, scoped security results and prepared delivery.

## Acceptance

- [x] Findings have concrete repros, fixes and independent follow-up review.
- [x] Known filler rejection, legacy/WIP and local-only safeguards still pass.
- [x] Security results name the tested immutable target and limitations.
- [x] Prepared delivery remains separate from confirmed branch/PR receipts; no merge or activation is implied.
