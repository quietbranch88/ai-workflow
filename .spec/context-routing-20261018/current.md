# Task context and evidence handoffs

## Goal

Make task context selection, resumption and lesson capture explicit while using
the existing clarification, review and authorization contracts.

## Scope

Update context-management.md and the handoff template. Canonical workflow,
review contracts, plugin mirrors and runtime behavior stay outside this change.

## Acceptance criteria

- [x] Observable: Phase routing loads mandatory instructions before optional context and refreshes material sources when facts change.
  - Environment: Maintained source tree.
  - Verify: Compare context-management.md against workflow.md and docs/review.md; walk clear-ticket and missing-required-source scenarios.
- [x] Observable: A resumed task names revision, verification evidence, blockers, next action and mutable facts needing recheck.
  - Environment: Handoff template.
  - Verify: Inspect templates/ai-development-map.md against a changed-remote-head scenario.
- [x] Observable: Lesson promotion requires concrete evidence and existing capture authorization, preserves counterevidence and private-source boundaries.
  - Environment: Maintained documentation.
  - Verify: Walk a one-off suggestion, a reproducible mechanical failure and a private incident scenario.
- [x] Observable: Existing repository and adapter contracts remain valid.
  - Environment: Local Python test environment.
  - Verify: python3 -m unittest discover -s tests -v; git diff --check; living-doc validation in Ship mode.

## Non-goals

No new runtime, plugin installation, deployment or claim that another agent
session loaded the changed files. Source publication was separately authorized
after fresh review and is recorded in audit.md. Documentation review does not
establish measured time/token savings or agent reliability improvement.
