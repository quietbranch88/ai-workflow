# Tasks

- [x] task-1: Add a failing contract for repository guardrail guidance and its
  public entrypoints.
  - Files: `tests/test_docs_contracts.py`
  - Verify: `PYTHONPATH=tests python3 -m unittest test_docs_contracts.CanonicalWorkflowContractTests.test_repository_guardrails_are_discoverable_and_server_enforced -v`

- [x] task-2: Add canonical guidance, public links, and the exact Claude mirror.
  - Files: `docs/repository-guardrails.md`, `workflow.md`, `README.md`,
    `claude-code/plugin/skills/six-stage-workflow/SKILL.md`
  - Verify: targeted contract and exact-mirror tests.

- [x] task-3: Bump the Claude plugin version and update personal-project records.
  - Files: `claude-code/plugin/.claude-plugin/plugin.json`, `devlog.md`, `todo.md`
  - Verify: repository documentation contracts and strict plugin validation.

- [x] task-4: Complete local verification, fresh self-review, commit, publish a
  pull request, apply the approved GitHub protection, and verify hosted evidence.
  - Files: repository checks, task records, and GitHub `main` protection.
  - Verify: full unittest discovery, both strict plugin validations, WIP/Ship
    validation, PR check readback, and branch-protection API readback.

## Acceptance

- [x] Acceptance criteria have current evidence.
- [x] Fail-to-pass evidence exists for the new documentation contract.
- [x] Local, PR, and server-side protection evidence remain separately labeled.
- [x] No deployment or plugin installation is performed.
