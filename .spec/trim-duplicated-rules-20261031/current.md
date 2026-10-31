# Point duplicated rules at the canonical copy

## Goal

Remove accidental full restatements. Keep one canonical copy and turn the other
into a short pointer. Keep required mirrors.

## Acceptance criteria

- [x] Observable: `prompts/code-review.md` and `prompts/review-checklist.md` keep the fill-in fields, output skeleton, and mode names, and an initial review still omits the authoring transcript and the author's defense. Repeated mode, partial-review, stop, and convergence prose points at `docs/review.md`.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_active_agent_and_prompt_docs_use_ticket_scoped_specs tests.test_docs_contracts.AdapterConsistencyContractTests.test_standalone_agents_include_required_contracts_in_the_package -v`
- [x] Observable: the packaged grill-me skill contains the canonical dimension list and the one-question rule from `prompts/grill-me.md`, the skip guard still matches, and the old Process and Question categories headings are gone. Plugin version is 0.6.11.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_grill_me_skip_rule_matches_the_canonical_guard -v`
- [x] Observable: the 280-line cap on `workflow.md` remains only in the core-workflow contract test. The named public and recipe restatements are short pointers, and `workflow.md` stays at most 280 lines.
  - Environment: this repository, local Python 3.
  - Verify: `python3 -m unittest tests.test_docs_contracts.CanonicalWorkflowContractTests.test_core_workflow_stays_a_map_instead_of_a_monolithic_manual tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_names_the_original_goal_and_the_comparison tests.test_docs_contracts.PublicReadmeContractTests -v`

## Non-goals

- Delete required mirrors: the six-stage skill, the verify-done skill, the builder and reviewer embeddings, or the Python and Go pitfall skills. Leave portfolio-scan and build-system-map as paraphrases.
- Merge the user-visible-check rules with the original-goal evidence rule.
- Merge migration authorization in `workflow.md` with migration classification in `docs/verification.md`.
- Delete historical devlog entries or old `.spec` tickets.
- Change the ship validator, add a Playwright mandate, a mutation score, or a speed claim.
- Install this revision on a machine, or authorize a merge.
