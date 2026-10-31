# Tasks

- [x] task-1: Record that a failing shape or size check is reverted, and keep the private system map local.
  - Files: docs/verification.md, workflow.md, GOTCHAS.md, prompts/system-map-scan.md, templates/system-map.md, context-management.md
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_shape_check_failure_does_not_raise_the_ceiling -v`
  - Evidence: local run recorded in audit.md.
- [x] task-2: Align the plugin mirrors, pitfall notes, and prompt wording with the canonical text. Plugin 0.6.12.
  - Files: claude-code/plugin/, pitfalls/, prompts/grill-me.md, prompts/refactor.md
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests tests.test_docs_contracts.CanonicalWorkflowContractTests -v`
  - Evidence: local run recorded in audit.md.
- [x] task-3: Make Ship mode see an open item hidden by an unclosed fence, a mismatched closer, or an HTML comment.
  - Files: scripts/validate_workflow_docs.py, tests/test_workflow_enforcement.py
  - Verify: `python3 -m unittest tests.test_workflow_enforcement.WorkflowDocumentValidatorTests.test_ship_sees_boxes_hidden_by_comment_fences_or_mismatched_closers -v`
  - Evidence: local run recorded in audit.md.
- [x] task-4: Record the change and state what the checks compared.
  - Files: .spec/review-fixes-20261031/, devlog.md, todo.md
  - Verify: `python3 scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base origin/main --head HEAD`
  - Evidence: recorded in audit.md after the branch range is checked.

## Acceptance

- [x] The acceptance criteria have contract-test evidence. The tests read the documents and the validator.
- [x] No service, UI, or recovery path changed.
- [x] No new dependency or secret-bearing file. Claude plugin validation is left to hosted pull-request checks when the CLI is absent.
- [x] Machine installation stays separate from this record.
