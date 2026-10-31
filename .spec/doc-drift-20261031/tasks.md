# Tasks

- [x] task-1: Apply the canonical grill-me skip guard to the packaged skill and bump the plugin.
  - Files: claude-code/plugin/skills/grill-me/SKILL.md, claude-code/plugin/.claude-plugin/plugin.json, tests/test_docs_contracts.py
  - Oracle: prompts/grill-me.md skip section; docs/rule-distribution.md version rule.
  - Required boundary: contract test reading the skill and plugin manifest.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_grill_me_skip_rule_matches_the_canonical_guard -v`
  - Evidence: local run passed. Plugin version reads 0.6.7. Skill no longer treats an instruction to proceed as a waiver.
- [x] task-2: Keep the portfolio scan command independent of the mine alias.
  - Files: prompts/portfolio-scan.md, tests/test_docs_contracts.py
  - Oracle: the scan needs isArchived and a 200-repository limit; mine uses a different limit and field list.
  - Required boundary: contract test reading the prompt.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_portfolio_scan_keeps_its_own_repository_command -v`
  - Evidence: local run passed. The prompt keeps the full gh command and does not mention the alias.
- [x] task-3: Remove the missing dependency-skill name from the Python checklist.
  - Files: pitfalls/python.md, tests/test_docs_contracts.py
  - Oracle: this repository has no verify-deps skill. The packaged checklist already omitted that name.
  - Required boundary: contract test reading both checklist copies.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_python_pitfalls_do_not_name_a_missing_dependency_skill -v`
  - Evidence: local run passed. Both copies say "New deps verified".
- [x] task-4: Record the alignment and check the two already-merged todo items.
  - Files: .spec/doc-drift-20261031/, devlog.md, todo.md
  - Oracle: PR #18 merge 2838a8f and PR #24 merge b2e5d66 are ancestors of main.
  - Required boundary: living-document ship check for this personal project.
  - Verify: `python3 scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base origin/main --head HEAD`
  - Evidence: `0cdb659` holds the wording and contract tests. The ship check for the branch range is in audit.md.

## Acceptance

- [x] The four acceptance criteria have contract-test or ancestry evidence. Assertions forbid the previous sentences; they were not weakened to match leftover wording.
- [x] No red/green sequence was run. These are documentation contracts, so the detection is the new assertions against the old sentences, not a production mutation.
- [x] No service, UI, or recovery path changed. The exercised boundary is the repository Markdown and plugin manifest read by the contract tests.
- [x] No new dependency or secret-bearing file. Static scan tools beyond `git diff --check` and the repository tests were not required for this wording change; their absence is this note.
- [x] Preparation, verification, merge, and machine installation stay separate. This record does not authorize merge or installation.
