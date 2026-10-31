# Review fixes 2026-10-31

## Goal

The working tree, not commit `ecef65d`, is what a later agent follows.
`ecef65d` is merged PR #30 at plugin 0.6.11. This change keeps the private
system map local, separates Ship mode from the WIP pre-push hook, and reverts
a failing shape check instead of relaxing it.

## Acceptance criteria

- Observable: `docs/verification.md` tells the reader to revert growth instead
  of raising a ceiling, and the private system-map instructions do not say to
  commit that file.
- Environment: this repository at the review-fixes working tree.
- Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests tests.test_docs_contracts.CanonicalWorkflowContractTests`

## Non-goals

Product-specific provider, screen, and deployment settings stay in the project
that owns them. Timed-out unit tests on this machine are not treated as logic
defects.
