# Tasks

- [x] task-1: Synchronize portable evidence, review and architecture contracts and adapters.
  - Files: workflow, docs, prompts, templates, Claude adapter and manifests.
  - Verify: claim review, repository contracts, strict plugin validation.
- [x] task-2: Support explicitly selected local-only records in validator and pre-push caller.
  - Files: scripts/validate_workflow_docs.py, scripts/check_close_the_loop.py, tests/test_local_spec_policy.py.
  - Oracle: acceptance contract in current.md; local records must stay private while remaining structurally checked.
  - Verify: failing baseline, passing regression tests and real disposable Git integration.
- [x] task-3: Reconcile public docs, metadata and delivery evidence.
  - Files: README.md, devlog.md, todo.md and task records.
  - Verify: review and remote description readback; report hosted PR checks separately after publication.

## Acceptance

- [x] All acceptance criteria have evidence or explicitly recorded outstanding delivery state.
- [x] Review findings and verification blockers are recorded separately.
- [x] Applicable tests and available scans are recorded; no merge or deployment is implied.
