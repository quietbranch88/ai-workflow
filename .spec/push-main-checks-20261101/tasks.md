# Tasks

- [x] task-1: Run the existing checks on a push to main, using that push as the Ship range.
  - Files: .github/workflows/validate.yml, tests/test_ci_workflow_contract.py
  - Oracle: the workflow names both events, and the Ship base and head change with the event.
  - Required boundary: the contract test reads the workflow file.
  - Verify: `python3 -m unittest tests.test_ci_workflow_contract -v`
  - Evidence: local run recorded in audit.md.
- [x] task-2: Tell the README reader about the push, without growing workflow.md.
  - Files: README.md, .spec/push-main-checks-20261101/, devlog.md, todo.md
  - Oracle: workflow.md stays at most 280 lines.
  - Required boundary: the existing line-cap test.
  - Verify: `python3 -m unittest tests.test_docs_contracts.CanonicalWorkflowContractTests.test_core_workflow_stays_a_map_instead_of_a_monolithic_manual -v`
  - Evidence: recorded in audit.md.

## Acceptance

- [x] The criteria have contract-test evidence. The tests read the workflow file and the line count.
- [x] No red/green sequence was run. This is a workflow-file contract.
- [x] No service or UI path changed.
- [x] No new dependency or secret-bearing file.
- [x] Preparation, verification, merge, and the user's computer stay separate.
