# Acceptance warnings and operation resumption

## Goal

Fix the reproduced empty-acceptance warning gap and preserve enough operation
state to reconcile interrupted external writes in the existing handoff.

## Acceptance criteria

- [x] Observable: Missing, empty or whitespace-only field lines and labels mentioned only in prose produce a warning; populated field lines do not. WIP and Ship still exit successfully for quality warnings.
  - Environment: CLI validator against temporary synthetic document fixtures.
  - Verify: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_workflow_enforcement.py -q`; record original fail-to-pass evidence in audit.md.
- [x] Observable: Resume guidance records pending operation identity, authorization reference, attempt/returned ID, known state and next readback; unknown outcomes cannot be blindly replayed.
  - Environment: Canonical context guide and handoff template.
  - Verify: Directly review success-with-lost-response, definite rejection, unavailable readback and running-worker scenarios against the documented contract.
- [x] Observable: Existing contracts and mirrored canonical content remain consistent.
  - Environment: Isolated source checkout; no installed-rule changes.
  - Verify: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`; changed-file Ship validation, local link validation and `git diff --check`.

## Non-goals

No Jira integration, agent-behavior evaluation, new journal framework, new approval
ceremony or unrelated audit fixes. Source publication follows the owner's existing
authorization; machine installation has a separate local delivery receipt.
