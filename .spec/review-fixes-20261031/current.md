# Review fixes 2026-10-31

## Goal

The working tree, not commit `ecef65d`, is what a later agent follows.
`ecef65d` is merged PR #30 at plugin 0.6.11. This change keeps the private
system map local, separates Ship mode from the WIP pre-push hook, and reverts
a failing shape check instead of relaxing it.

## Acceptance criteria

- [x] Observable: `docs/verification.md` tells the reader to revert growth instead of raising a ceiling, the builder copy matches that section, and the plugin version is at least 0.6.12.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_shape_check_failure_does_not_raise_the_ceiling -v`
- [x] Observable: Ship mode still fails when an open checklist item sits after an unclosed fence, after a mismatched fence closer, or inside an HTML comment, including a fence wrapped in that comment. A closed fence example and a branch-name comment still pass.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_workflow_enforcement.WorkflowDocumentValidatorTests.test_ship_sees_boxes_hidden_by_comment_fences_or_mismatched_closers tests.test_workflow_enforcement.WorkflowDocumentValidatorTests.test_ship_ignores_checkbox_examples_inside_fenced_code tests.test_workflow_enforcement.WorkflowDocumentValidatorTests.test_ship_allows_branch_metadata_html_comment -v`
- [x] Observable: private system-map instructions do not say to commit that file, and an unfinished-marker scan matches a whole word, so `tbdata` stays allowed.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_system_map_validator.SystemMapValidatorTests.test_tbd_matches_a_word_and_allows_tbdata tests.test_docs_contracts.CanonicalWorkflowContractTests -v`

## Non-goals

Product-specific provider, screen, and deployment settings stay in the project
that owns them. Timed-out unit tests on this machine are not treated as logic
defects. Machine installation of plugin 0.6.12 stays separate.
