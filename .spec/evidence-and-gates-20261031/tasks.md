# Tasks

- [x] task-1: State one decidable behavior, the dependency install record, the migration classes, and the original-goal comparison in the verification contract and the packaged builder.
  - Files: docs/verification.md, claude-code/plugin/agents/builder.md
  - Oracle: the evidence sentence names the original goal and whether the observed result matched it.
  - Required boundary: contract test that the canonical text is embedded in the builder.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_names_the_original_goal_and_the_comparison tests.test_docs_contracts.AdapterConsistencyContractTests.test_standalone_agents_include_required_contracts_in_the_package -v`
  - Evidence: local run recorded in audit.md.
- [x] task-2: Treat fetched text as data, keep a conflict-free merge untrusted, and point verify-done at the original goal. Keep workflow.md within 280 lines and match the packaged skill.
  - Files: workflow.md, claude-code/plugin/skills/six-stage-workflow/SKILL.md, prompts/verify-done.md, claude-code/plugin/skills/verify-done/SKILL.md, prompts/parallel-audit.md, GOTCHAS.md
  - Oracle: docs/rule-distribution.md requires the mirror and version to move with the canonical source.
  - Required boundary: existing skill-mirror equality test and the 280-line cap.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_skill_mirrors_match_canonical_content tests.test_docs_contracts.CanonicalWorkflowContractTests.test_core_workflow_stays_a_map_instead_of_a_monolithic_manual -v`
  - Evidence: local run recorded in audit.md.
- [x] task-3: Omit the authoring transcript from an initial review, separate a resume summary from files and remote receipts, and record an install receipt outside the repository.
  - Files: docs/review.md, claude-code/plugin/agents/reviewer.md, prompts/code-review.md, context-management.md, docs/rule-distribution.md, claude-code/plugin/skills/python-pitfalls/SKILL.md, claude-code/plugin/skills/go-pitfalls/SKILL.md, claude-code/plugin/skills/portfolio-scan/SKILL.md, claude-code/plugin/skills/build-system-map/SKILL.md, claude-code/plugin/.claude-plugin/plugin.json
  - Oracle: plugin version reads 0.6.10, and the four skill headers no longer say a local file may be newer.
  - Required boundary: review text embedded in the packaged reviewer and builder.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_names_the_original_goal_and_the_comparison tests.test_docs_contracts.AdapterConsistencyContractTests.test_standalone_agents_include_required_contracts_in_the_package -v`
  - Evidence: local run recorded in audit.md.
- [x] task-4: Record the change and state what the checks compared.
  - Files: .spec/evidence-and-gates-20261031/, devlog.md, todo.md, tests/test_docs_contracts.py
  - Oracle: the audit names the original goal, the document checks that ran, and that no product result was compared.
  - Required boundary: ship-mode living-document check for this personal project.
  - Verify: `python3 scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base origin/main --head HEAD`
  - Evidence: recorded in audit.md after the branch range is checked.

## Acceptance

- [x] The acceptance criteria have contract-test evidence. The tests read the documents; they do not compare a product result with a browser.
- [x] No red/green sequence was run. This is a documentation contract.
- [x] No service, UI, or recovery path changed. The exercised boundary is the Markdown contract read by the tests.
- [x] No new dependency or secret-bearing file. Claude plugin validation is left to hosted pull-request checks when the CLI is absent.
- [x] Preparation, verification, merge, and machine installation stay separate. This record does not authorize a merge.
