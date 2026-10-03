# Tasks

- [ ] task-1: Synchronize portable evidence, review and architecture contracts and adapters.
  - Files: workflow, docs, prompts, templates, Claude adapter and manifests.
  - Verify: claim review, repository contracts, strict plugin validation.
- [ ] task-2: Support explicitly selected local-only records in validator and pre-push caller.
  - Files: scripts/validate_workflow_docs.py, scripts/check_close_the_loop.py, tests/test_local_spec_policy.py.
  - Oracle: acceptance contract in current.md; local records must stay private while remaining structurally checked.
  - Verify: failing baseline, passing regression tests and real disposable Git integration.
- [ ] task-3: Reconcile public docs, metadata and delivery evidence.
  - Files: README.md, devlog.md, todo.md and task records.
  - Verify: review, remote description readback, PR checks.

## Acceptance

- [ ] All acceptance criteria have evidence or explicitly recorded outstanding delivery state.
- [ ] Review findings and verification blockers are recorded separately.
- [ ] Applicable tests and available scans are recorded; no merge or deployment is implied.
