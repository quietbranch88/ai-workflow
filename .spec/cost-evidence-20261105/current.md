# Agent cost evidence

## Goal

Make cost-improvement claims measurable without weakening task correctness.
Zoe approved the narrowed proposal following independent review on 2026-11-05.

## Scope

Add cost accounting and paired A/B guidance inside the existing agent-evaluation
contract, synchronize its builder mirror, and update the plugin source version.
No pilot execution, usage-log collection, installation or automatic intervention.
Publication and integration remain separate delivery actions.

## Acceptance criteria

- [x] Observable: cost claims distinguish bills, estimates and proxies, account
  for cache writes and all attempts, and disclose missing usage without zero-fill.
  - Environment: local feature branch.
  - Verify: direct clause review against COST-R1-02 in audit.md.
- [x] Observable: comparisons pair the same tasks/revisions and preserve quality,
  controlled conditions, repeated trials and uncertainty before expansion.
  - Environment: local documentation.
  - Verify: direct clause review against COST-R1-01 and existing evaluation rules.
- [x] Observable: the builder embeds the complete updated canonical contract;
  ordinary work does not acquire background monitoring or intervention.
  - Environment: local packaged source.
  - Verify: existing adapter-consistency tests and strict plugin validation.
