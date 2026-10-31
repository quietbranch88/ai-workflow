# Align drifted instructions

## Goal

Make the packaged clarification skill, the portfolio scan command, and the Python
dependency checklist agree with the instructions they claim to follow. Record two
todo items whose described pull requests are already on main.

## Acceptance criteria

- [x] Observable: the packaged grill-me skill skips clarification only when no
  consequential unknown remains, and a reproduction or planner checklist does not
  resolve a missing product or authorization decision. Plugin version is 0.6.7.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_grill_me_skip_rule_matches_the_canonical_guard -v`
- [x] Observable: `prompts/portfolio-scan.md` keeps the `--limit 200` command with
  `isArchived`, and does not call `mine` a short form of that command.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_portfolio_scan_keeps_its_own_repository_command -v`
- [x] Observable: `pitfalls/python.md` and the packaged Python pitfalls skill both
  say to verify new dependencies, and neither names `verify-deps`.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_python_pitfalls_do_not_name_a_missing_dependency_skill -v`
- [x] Observable: `todo.md` records workflow-enforcement PR #18 and the story-first
  README PR #24 as merged, and leaves machine installation, new language pitfalls,
  and local-install comparison open.
  - Environment: this repository.
  - Verify: read `todo.md` against `git merge-base --is-ancestor` for `2838a8f` and `b2e5d66`.

## Non-goals

- Rewrite the portfolio-scan or system-map skills into byte-identical mirrors.
- Change the `mine` alias in `shell/aliases.sh`.
- Install this revision on a local machine, merge it, or treat preparation as publication.
