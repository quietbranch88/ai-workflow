# Context loading and compaction

## Goal

Make context reduction portable and verifiable while retaining mandatory safety,
authorization and verification requirements. The owner approved synchronizing
these general practices into AI Workflow on 2026-11-12.

## Scope

Update canonical context guidance, its workflow entry route, the declared Claude
workflow mirror and plugin source version. Keep machine paths, company rules,
personal memory and private benchmark artifacts outside this repository. No
runtime implementation, automatic memory migration, permission change or blanket
savings claim. Feature-branch delivery does not authorize merge or installation.

## Acceptance criteria

- [x] Observable: mandatory core gates and explicit document/task/read-time routes
  coexist with on-demand detail; missing required context prevents dependent work.
  - Environment: canonical documentation and workflow mirror.
  - Verify: clause review and existing adapter-consistency tests.
- [x] Observable: bounded tool output preserves necessary evidence; external memory
  writes and compacted state retain authorization and source-readback boundaries.
  - Environment: documentation tabletop.
  - Verify: trace truncated output, a triggered contract, and an unknown remote write.
- [x] Observable: fresh-session claims name the tested surface and distinguish
  source preservation, traces, byte estimates, token usage, caches and billing.
  - Environment: documentation tabletop.
  - Verify: trace a translation, a verification task and a single-pair CLI result.
- [x] Observable: mirrors, package version and living records agree and checks pass.
  - Environment: local checkout and feature-branch commit range.
  - Verify: repository tests, strict package validators, diff/link checks, WIP guard
    and Ship validation before publication.
