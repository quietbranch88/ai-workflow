# Tasks

- [x] task-1: Add a failing contract for the trust gate and its entrypoints.
  - Files: `tests/test_docs_contracts.py`
  - Verify: `PYTHONPATH=tests python3 -m unittest test_docs_contracts.CanonicalWorkflowContractTests.test_third_party_skill_trust_gate_is_discoverable_and_blocks_high_findings -v`
  - Evidence: the pre-change run errored because `docs/skill-trust.md` did not exist.

- [x] task-2: Write the canonical policy and expose it from shared entrypoints.
  - Files: `docs/skill-trust.md`, `workflow.md`, `README.md`, `codex/skills/ai-workflow/SKILL.md`
  - Verify: targeted contract test and direct diff review.

- [x] task-3: Synchronize the Claude mirror and bump plugin version.
  - Files: `claude-code/plugin/skills/six-stage-workflow/SKILL.md`, `claude-code/plugin/.claude-plugin/plugin.json`
  - Verify: exact mirror contract and strict plugin validators.

- [x] task-4: Complete full verification, fresh self-review, commit, and Ship-mode
  validation of the complete local branch range.
  - Files: repository checks and task records.
  - Verify: full unittest discovery, strict plugin validation, WIP/Ship record
    validation, source-link check, and `git diff --check`.
  - Evidence: 97 tests and both strict plugin validations passed; final Ship-mode
    evidence is recorded in `audit.md` after committing the complete local range.

## Acceptance

- [x] Applicable acceptance criteria have current local evidence.
- [x] Fail-to-pass evidence exists for the new policy contract.
- [x] No scanner, third-party skill, plugin, or external integration was installed.
- [x] Canonical/mirror checks, full tests, and Ship validation pass.
- [x] Push, merge, publication, release, and activation remain unperformed.
