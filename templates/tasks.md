# Tasks

Verification map: required

Map acceptance IDs from `current.md` to checks and evidence in these existing task
fields; see [verification](../docs/verification.md#acceptance-to-evidence-links).
Repository publication policy still applies, including local-only records.

- [ ] task-1: <small coherent change>
  - Acceptance: AC-1
  - Files: <exact paths>
  - Oracle: <independent product rule, invariant, contract or incident fixture>
  - Required boundary: <unit, real integration or E2E and observable result>
  - Verify: <command or reproducible steps>
  - Detection: <mutation or fail-to-pass>: <relevant failure and restored pass reference>
  - Evidence: <revision, environment, discovered tests, assertions and results>

For behavior-neutral work, use `Detection: not-applicable: <reason>`. Reuse an
existing failure for the same requirement/revision/boundary instead of repeating it.

## Acceptance

- [ ] Mapped results were reviewed; structural validation is not proof of correctness
- [ ] Assertions were not weakened to make checks pass
- [ ] Required real boundaries and affected failure/recovery cases ran; substitutions are labeled
- [ ] Applicable UI interactions and results were checked in Chrome or the native app/emulator
- [ ] Applicable security, dependency and secret scans and missing tools are recorded
- [ ] Findings retain evidence, counterevidence, validity and disposition under docs/review.md
- [ ] Blocked/skipped/unverified gates and specifically authorized exceptions remain explicit
- [ ] Authorized delivery records agree; implemented, verified, merged and deployed stay distinct
- [ ] PR description and any actual architecture decision are recorded where applicable

This checklist does not authorize publication, merge, deployment or production changes.
