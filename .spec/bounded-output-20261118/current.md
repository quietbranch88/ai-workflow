# Bounded tool output with preserved evidence

## Goal

As the workflow owner, reduce unnecessary tool-result expansion while preserving
mandatory instructions, authorization, privacy and complete verification evidence.

## Acceptance criteria

- [x] AC-1: Query guidance covers scoped lists/history, browser state, tool discovery and complete mandatory reads.
  - Observable: exact targets and bounded discovery are preferred; pagination, stale-state and restoration limits remain explicit.
  - Environment: canonical context guidance, source review.
  - Verify: independent review of context-management.md and referenced contracts.
- [x] AC-2: Large verification output has a traceable compact receipt without weakening tests.
  - Observable: revision, environment, command, counts, assertions, missing boundaries and redacted artifact reference remain visible; unavailable evidence is labeled.
  - Environment: canonical verification document and Claude builder mirror.
  - Verify: repository contract tests, package checks and independent review.
## Authorized delivery after local acceptance

Push reviewed commits, create a PR and read back its final-head CI. Track actual
results in the audit/handoff; local acceptance does not imply remote completion.
No merge or installation is included.

## Non-goals

No runtime tool changes, global configuration/memory edits, private transcript
publication, token savings claim, automatic compaction, merge or installation.
