# Review follow-ups 2026-11-01

## Goal

The post-merge review of `6dd7c30` no longer sends a later agent to the wrong
check, and Ship mode still sees an open item when a comment sits between fence
markers.

## Acceptance criteria

- [x] Observable: `README.md` sends Verify to deterministic tools, and a faster model only searches or classifies exact tool output.
  - Environment: this repository at the follow-up working tree.
  - Verify: `git diff 6dd7c30 -- README.md`
- [x] Observable: portfolio scan does not call the spec-map rule "regenerate, don't hand-edit", and verify-done does not require a new runtime test for a documentation edit.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_skill_mirrors_match_canonical_content tests.test_docs_contracts.AdapterConsistencyContractTests.test_portfolio_scan_keeps_its_own_repository_command -v`
- [x] Observable: Ship mode fails when ``<!-- x -->` or `<!-- x -->``` ` is used to hide `- [ ]` or an unfinished marker. A closed fence example still passes. Plugin version is 0.6.13.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_workflow_enforcement.WorkflowDocumentValidatorTests.test_ship_sees_boxes_hidden_by_comment_fences_or_mismatched_closers tests.test_workflow_enforcement.WorkflowDocumentValidatorTests.test_ship_ignores_checkbox_examples_inside_fenced_code tests.test_workflow_enforcement.WorkflowDocumentValidatorTests.test_ship_allows_branch_metadata_html_comment -v`

## Non-goals

The four local timeout tests stay as they are. Machine installation of plugin
0.6.13 stays separate. Historical devlog entries stay.
