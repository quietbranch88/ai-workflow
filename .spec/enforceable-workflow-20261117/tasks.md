# Tasks

Verification map: required

- [x] task-1: Implement proportional practices and synchronize declared mirrors.
  - Acceptance: AC-1, AC-2
  - Oracle: User-approved five practices; existing authorization and verification contracts.
  - Required boundary: Canonical Markdown to packaged Claude mirrors, no runtime behavior change.
  - Verify: python3 -m unittest discover -s tests -v; claude plugin validate --strict claude-code/plugin
  - Detection: not-applicable: Documentation-only guidance and plugin version metadata; existing contract tests check mirror parity.
  - Evidence: 75b169a, macOS local; 113 tests passed in 32.723s; strict package validation passed.
- [x] task-2: Complete ten scoped independent reviews and reconcile evidence.
  - Acceptance: AC-1, AC-2
  - Oracle: Task acceptance and docs/review.md evidence contract.
  - Required boundary: Immutable patch and relevant canonical routes, read-only agent review.
  - Verify: Ten worker reports; local links, diff, WIP and Ship checks.
  - Detection: not-applicable: Claim review of documentation; no formal model or product runtime introduced.
  - Evidence: Ten fresh scoped reviews completed on 75b169a with no actionable findings; audit records checks and limits.

## Acceptance

- [x] Reconcile local evidence and delivery state.
