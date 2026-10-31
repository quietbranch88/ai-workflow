# Evidence names the original goal

## Goal

Write the second research round into the existing contracts, and require every
evidence record to name the original goal, what the run actually exercised, and
whether that result matched. A green command is not that comparison.

## Acceptance criteria

- [x] Observable: `docs/verification.md` requires one decidable behavior per
  criterion, a lockfile install from the recorded dependency, a classified
  shared-database migration, and an evidence line that names the original goal
  and whether the observed result matched it.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_names_the_original_goal_and_the_comparison tests.test_docs_contracts.AdapterConsistencyContractTests.test_standalone_agents_include_required_contracts_in_the_package -v`
- [x] Observable: `workflow.md` treats fetched text as data, keeps a conflict-free
  merge untrusted until checks run on the assembled tree, and stays within 280
  lines. The packaged six-stage skill matches that text. `prompts/verify-done.md`
  reports the original goal and whether the exercise matched.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_names_the_original_goal_and_the_comparison tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_skill_mirrors_match_canonical_content tests.test_docs_contracts.CanonicalWorkflowContractTests.test_core_workflow_stays_a_map_instead_of_a_monolithic_manual -v`
- [x] Observable: an initial review omits the authoring transcript and the
  author's defense. Resume treats a summary as distinct from files and remote
  receipts. An install receipt lives outside the repository, and a local skill
  file does not replace the packaged copy only because it might be newer. Plugin
  version is 0.6.10.
  - Environment: `docs/review.md`, `context-management.md`, `docs/rule-distribution.md`, and `claude-code/plugin/`.
  - Verify: the same contract tests, plus JSON parse of `plugin.json`.

## Non-goals

- Change the ship validator so a filled label fails.
- Add a pull-request check on direct pushes to the default branch.
- Require a different model, a mutation score, a named browser product, or a
  screenshot of every step.
- Treat this repository's document checks as a product comparison in a browser.
- Install this revision on a machine, or authorize a merge.
