# Bounded tool output with preserved evidence

## Goal

As the workflow owner, reduce unnecessary tool-result expansion while preserving
mandatory instructions, authorization, privacy and complete verification evidence.

## Acceptance criteria

- [ ] AC-1: Query guidance covers scoped lists/history, browser state, tool discovery and complete mandatory reads.
  - Observable: exact targets and bounded discovery are preferred; pagination, stale-state and restoration limits remain explicit.
  - Environment: canonical context guidance, source review.
  - Verify: independent review of context-management.md and referenced contracts.
- [ ] AC-2: Large verification output has a traceable compact receipt without weakening tests.
  - Observable: revision, environment, command, counts, assertions, missing boundaries and redacted artifact reference remain visible; unavailable evidence is labeled.
  - Environment: canonical verification document and Claude builder mirror.
  - Verify: repository contract tests, package checks and independent review.
- [ ] AC-3: Reviewed changes are pushed as a PR with final-head CI observed.
  - Observable: remote branch/head and PR readback match final local revision; CI result reported without claiming merge or installation.
  - Environment: authorized GitHub repository and local feature worktree.
  - Verify: remote head, PR and final-head Actions readback.

## Non-goals

No runtime tool changes, global configuration/memory edits, private transcript
publication, token savings claim, automatic compaction, merge or installation.
