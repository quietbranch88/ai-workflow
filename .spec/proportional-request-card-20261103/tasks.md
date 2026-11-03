# Tasks

- [x] task-1: Add a failing contract for proportional routing, six card fields and bounded decisions.
  - Files: `tests/test_docs_contracts.py`
  - Oracle: accepted task contract in `current.md`.
  - Required boundary: documentation contract test.
  - Verify: targeted unittest command in `current.md`.
  - Evidence: pre-change run failed on missing direct-execution/card text; corrected run passed.

- [x] task-2: Update the canonical workflow and clarification prompt.
  - Files: `workflow.md`, `prompts/grill-me.md`
  - Oracle: user request, original CabLate article and existing proportional workflow rules.
  - Required boundary: intake guidance through Define routing.
  - Verify: targeted contract test plus diff review.
  - Evidence: pending full-suite entry in `audit.md`.

- [x] task-3: Synchronize required Claude mirrors and bump plugin version.
  - Files: `claude-code/plugin/skills/six-stage-workflow/SKILL.md`, `claude-code/plugin/skills/grill-me/SKILL.md`, `claude-code/plugin/.claude-plugin/plugin.json`
  - Oracle: repository mirror contract.
  - Required boundary: packaged skill content.
  - Verify: exact mirror contract and strict package validation.
  - Evidence: pending full-suite entry in `audit.md`.

- [x] task-4: Complete full verification, fresh diff review and delivery reconciliation.
  - Files: repository checks and task records.
  - Oracle: `AGENTS.md` verification and close-the-loop rules.
  - Required boundary: complete local branch.
  - Verify: full unittest discovery, strict plugin validation, Ship validator and `git diff --check`.
  - Evidence: 96 tests, both strict plugin validations, WIP validation, link check and diff check passed; review found no actionable issue. Ship runs against the local commit range before handoff.

## Acceptance

- [x] Applicable acceptance criteria have independent evidence; assertions were not weakened.
- [x] Fail-to-pass evidence exists for the new documentation contract.
- [x] No runtime, UI, security-sensitive or external-write boundary changed.
- [x] Canonical/mirror checks and full tests pass; Ship validation is the immediate post-commit gate and reopens this item on failure.
- [x] Merge, publication and plugin installation remain separate and unperformed.

