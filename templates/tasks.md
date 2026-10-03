# Tasks

Keep slices independently verifiable with explicit scope and ownership. Follow the
repository's task-record policy, including local-only rules. Passing tests prove
only the boundaries exercised; see [verification](../docs/verification.md).

- [ ] task-1: <small coherent change>
  - Files: <exact paths>
  - Oracle: <independent product rule, invariant, contract or incident fixture>
  - Required boundary: <unit, real integration or E2E and observable result>
  - Verify: <command or reproducible steps>
  - Evidence: <revision, environment, discovered tests, assertions and results>

## Acceptance

- [ ] Applicable acceptance criteria have independent evidence; assertions were not weakened
- [ ] Required fail-to-pass or meaningful mutation evidence exists, or its absence is explained
- [ ] Required real boundaries and affected failure/recovery cases ran; substitutions are labeled
- [ ] Applicable UI interactions and results were checked in Chrome or the native app/emulator
- [ ] Applicable security, dependency and secret scans and missing tools are recorded
- [ ] Findings retain evidence, counterevidence, validity and disposition under docs/review.md
- [ ] Blocked/skipped/unverified gates and specifically authorized exceptions remain explicit
- [ ] Authorized delivery records agree; implemented, verified, merged and deployed stay distinct
- [ ] PR description and any actual architecture decision are recorded where applicable

Behavior-neutral work uses targeted review/validation, not artificial mutations.
This checklist does not authorize publication, merge, deployment or production changes.
