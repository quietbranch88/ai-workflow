# User-visible checks

## Goal

Turn the browser-first, case-first end-to-end discussion into this workflow's
existing verification contract. The oracle is the visible result in the acceptance
or QA case. The real browser comes before a repeatable UI check. The project keeps
its own test runner.

## Acceptance criteria

- [x] Observable: `docs/verification.md` has a User-visible checks section that
  takes assertions from the acceptance or QA case, requires a real-browser pass
  before the repeatable check, and keeps that check in the project's existing UI
  test runner. The section does not name Playwright.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_user_visible_checks_use_the_acceptance_case_and_existing_runner tests.test_docs_contracts.AdapterConsistencyContractTests.test_standalone_agents_include_required_contracts_in_the_package tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_skill_mirrors_match_canonical_content -v`
- [x] Observable: the packaged builder contains the same section, verify-done and
  its skill tell UI work to exercise the visible result first, and the plugin
  version is 0.6.8.
  - Environment: `claude-code/plugin/` and `prompts/verify-done.md`.
  - Verify: the same unittest command, plus JSON parse of `plugin.json`.
- [x] Observable: `GOTCHAS.md` points at that order, and `workflow.md` stays within
  280 lines.
  - Environment: this repository.
  - Verify: `python3 -m unittest tests.test_docs_contracts.CanonicalWorkflowContractTests.test_core_workflow_stays_a_map_instead_of_a_monolithic_manual tests.test_docs_contracts.AdapterConsistencyContractTests.test_user_visible_checks_use_the_acceptance_case_and_existing_runner -v`

## Non-goals

- Require Playwright, Jest, Vitest, analytics, or another external test product.
- Treat a prompt keyword as a verification method.
- Claim a speed or cost improvement.
- Install this revision on a machine, or treat the pull request as a merge.
