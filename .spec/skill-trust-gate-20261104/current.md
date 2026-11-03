# Agent skill trust gate

## Goal

Add a focused, proportional trust gate for new or updated third-party agent
skills so source identity, actual capabilities, security, usefulness, and final
artifact identity are checked before enablement.

## Scope

### In

- Add a canonical trust policy and expose it from the workflow, README, and
  native Codex skill entrypoint.
- Keep security scanning, effectiveness evaluation, and artifact integrity as
  separate evidence.
- Block Critical and High findings by default, with a complete explicit risk
  acceptance record as the only exception.
- Synchronize the Claude workflow mirror, add contract coverage, and bump the
  plugin version to 0.6.17.

### Out

- No scanner, skill, plugin, hook, or MCP server installation.
- No retrospective mass scan of unchanged skills.
- No push, pull request, merge, release, or activation.

## Acceptance criteria

- [x] Observable: the canonical policy requires source plus immutable revision,
  pre-execution content inspection, and an actual-capability map.
  - Environment: local repository checkout on `docs/skill-trust-gate-20261104`.
  - Verify: targeted documentation contract test in `tasks.md`.
  - Oracle: accepted user decisions and NVIDIA's published trust-pipeline model.
  - Required boundary: `docs/skill-trust.md` and its discoverable entrypoints.

- [x] Observable: security scanning, effectiveness evaluation, and artifact
  integrity are independent evidence and missing evidence is `unverified`.
  - Environment: local repository checkout.
  - Verify: targeted contract test and direct policy review.
  - Oracle: NVIDIA Agent Skill Trust Pipeline and SkillSpector guidance.
  - Required boundary: policy text, not scanner execution.

- [x] Observable: Critical or High findings block install, enablement, or update;
  an exception records the risk, decision-maker, date, exact revision, scope,
  compensating controls, and review condition.
  - Environment: local repository checkout.
  - Verify: targeted contract test and direct policy review.
  - Oracle: Zoe's accepted recommended decision.
  - Required boundary: decision policy only; no external system is changed.

- [x] Observable: executable or broad-capability third-party skills require an
  applicable agent-native scan, while docs-only local skills may use a recorded
  proportional manual review.
  - Environment: local repository checkout.
  - Verify: targeted contract test and direct policy review.
  - Oracle: accepted proportional policy.
  - Required boundary: security review routing.

## Risks

- Treating a signature as a safety verdict -> keep artifact integrity separate.
- Automatically installing an unapproved scanner -> policy explicitly forbids it.
- Overburdening harmless local documentation -> docs-only manual-review path.
- Policy being invisible -> contract checks all three public/native entrypoints.
