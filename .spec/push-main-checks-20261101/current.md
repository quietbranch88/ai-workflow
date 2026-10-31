# Checks on a push to the default branch

## Goal

A push to the default branch runs the same repository checks as a pull request.
The comparison range is that push, not an empty pull-request SHA.

## Acceptance criteria

- [x] Observable: `.github/workflows/validate.yml` runs on `pull_request` and on a
  push to `main`. The Ship check uses `github.event.before` and `github.sha` for
  a push, and the pull-request base and head SHAs for a pull request.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_ci_workflow_contract -v`
- [x] Observable: `README.md` says that workflow runs for a pull request and for
  a push to the default branch. `workflow.md` stays within 280 lines.
  - Environment: this repository.
  - Verify: `python3 -m unittest tests.test_ci_workflow_contract tests.test_docs_contracts.CanonicalWorkflowContractTests.test_core_workflow_stays_a_map_instead_of_a_monolithic_manual -v`

## Non-goals

- Make an empty Observable, Environment, or Verify field fail Ship mode. That
  warning is the reviewed rule.
- Judge whether a filled label matches the original goal. The validator checks
  structure, not meaning.
- Update the user's computer. This environment can refresh only its own install.
- Require the new check in branch protection before this change is on the
  default branch. Merge stays a separate authorization.
