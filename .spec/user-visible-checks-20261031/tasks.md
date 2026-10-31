# Tasks

- [x] task-1: Add the user-visible order to the verification contract and the packaged builder.
  - Files: docs/verification.md, claude-code/plugin/agents/builder.md
  - Oracle: acceptance or QA case names the visible result; the real browser precedes the repeatable check.
  - Required boundary: contract test that the canonical text is embedded in the builder.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_standalone_agents_include_required_contracts_in_the_package tests.test_docs_contracts.AdapterConsistencyContractTests.test_user_visible_checks_use_the_acceptance_case_and_existing_runner -v`
  - Evidence: local run recorded in audit.md.
- [x] task-2: Point verify-done, its skill, and GOTCHAS at the same order, and bump the plugin.
  - Files: prompts/verify-done.md, claude-code/plugin/skills/verify-done/SKILL.md, GOTCHAS.md, claude-code/plugin/.claude-plugin/plugin.json
  - Oracle: docs/rule-distribution.md requires the mirror and version to move with the canonical prompt.
  - Required boundary: existing skill-mirror equality test.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_skill_mirrors_match_canonical_content -v`
  - Evidence: local run recorded in audit.md. Plugin version reads 0.6.9.
- [x] task-3: Record the change without growing workflow.md.
  - Files: .spec/user-visible-checks-20261031/, devlog.md, todo.md, tests/test_docs_contracts.py
  - Oracle: workflow.md line cap remains 280.
  - Required boundary: ship-mode living-document check for this personal project.
  - Verify: `python3 scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base origin/main --head HEAD`
  - Evidence: recorded in audit.md after the branch range is checked.

## Acceptance

- [x] The acceptance criteria have contract-test evidence. Assertions were not weakened to allow a named test product.
- [x] No red/green sequence was run. This is a documentation contract; the new assertions forbid a tool mandate and require the order.
- [x] No service, UI, or recovery path changed. The exercised boundary is the Markdown contract read by the tests.
- [x] No new dependency or secret-bearing file. Claude plugin validation is left to hosted pull-request checks when the CLI is absent.
- [x] Preparation, verification, merge, and machine installation stay separate.
