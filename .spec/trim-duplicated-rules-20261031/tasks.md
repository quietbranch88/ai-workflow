# Tasks

- [x] task-1: Point the review prompts at `docs/review.md` without dropping the initial-review isolation sentence, the fill-in fields, the output skeleton, or the mode names.
  - Files: prompts/code-review.md, prompts/review-checklist.md
  - Oracle: the prompts still name initial, follow-up, and claim-check, and still say an initial review omits the authoring transcript and the author's defense.
  - Required boundary: `docs/review.md` and the packaged reviewer stay the canonical copies.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_active_agent_and_prompt_docs_use_ticket_scoped_specs tests.test_docs_contracts.AdapterConsistencyContractTests.test_standalone_agents_include_required_contracts_in_the_package -v`
  - Evidence: local run recorded in audit.md.
- [x] task-2: Make the packaged grill-me skill follow `prompts/grill-me.md` and bump the plugin to 0.6.11.
  - Files: claude-code/plugin/skills/grill-me/SKILL.md, claude-code/plugin/.claude-plugin/plugin.json, tests/test_docs_contracts.py
  - Oracle: the skill contains the canonical dimension list and the one-question rule, and the old Process heading is gone.
  - Required boundary: YAML frontmatter and the Canonical source header stay. The test does not require a byte-identical file.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_grill_me_skip_rule_matches_the_canonical_guard -v`
  - Evidence: local run recorded in audit.md.
- [x] task-3: Replace the named public and recipe restatements with pointers, and keep the workflow line cap in the core-workflow test only.
  - Files: claude-code/CLAUDE.md.example, GOTCHAS.md, prompts/parallel-audit.md, templates/ai-development-map.md, README.md, GLOSSARY.md, AGENTS.md, tests/test_docs_contracts.py
  - Oracle: `workflow.md` is still at most 280 lines, and the evidence test no longer asserts that cap.
  - Required boundary: `git diff --check` and `python scripts/check_close_the_loop.py` remain required in AGENTS.md. PHILOSOPHY.md stays because its sections are the principles.
  - Verify: `python3 -m unittest tests.test_docs_contracts.CanonicalWorkflowContractTests.test_core_workflow_stays_a_map_instead_of_a_monolithic_manual tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_names_the_original_goal_and_the_comparison tests.test_docs_contracts.PublicReadmeContractTests -v`
  - Evidence: local run recorded in audit.md.
- [x] task-4: Record the change and state what the checks compared.
  - Files: .spec/trim-duplicated-rules-20261031/, devlog.md, todo.md
  - Oracle: the audit names the original goal, the document checks that ran, and that no browser result was compared.
  - Required boundary: ship-mode living-document check for this personal project. Machine installation and merge stay separate.
  - Verify: `python3 scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base origin/main --head HEAD`
  - Evidence: recorded in audit.md after the branch range is checked.

## Acceptance

- [x] The acceptance criteria have contract-test evidence. The tests read the documents; they do not compare a product result in a browser.
- [x] No red/green sequence was run. This is a documentation contract.
- [x] No service, UI, or recovery path changed. The exercised boundary is the Markdown contract read by the tests.
- [x] No new dependency or secret-bearing file. Claude plugin validation is left to hosted pull-request checks when the CLI is absent.
- [x] Preparation, verification, merge, and machine installation stay separate. This record does not authorize a merge.
