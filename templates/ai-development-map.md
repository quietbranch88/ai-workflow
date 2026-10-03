# <ticket> AI development map

This file is the handoff entry point for Codex, Claude, and helper agents working on the same ticket.

## Authoritative sources

Read these in order before changing code:

1. `<master spec path>`
2. `<repo task list path>`
3. `<repo audit path>`
4. `<deferred or sub-task path if any>`

## Current scope

Summarize the current parent-ticket or task scope:

1. 
2. 
3. 

## Implementation files

### Production

- 

### Tests

- 

### Call sites or integration points

- 

## Verification checkpoints

1. Record the independently checkable acceptance contract and its source.
2. Map required boundaries and existing tests; name missing coverage/environments.
3. Record the chosen workflow. TDD is optional unless required; do not invent red/green evidence.
4. Record required fail-to-pass or controlled-mutation outcomes without changing the oracle.
5. Record revision, environment, discovered tests/assertions and relevant real integration/E2E results.
6. Label mocked boundaries, scan results, missing tools and blocked/unverified gates.

Use [docs/verification.md](../docs/verification.md) and repository-specific contracts.
Behavior-neutral edits use targeted review instead of artificial failing tests.

## Verification commands

```text
ruff check ...
pytest <narrow target>
pytest <broader target>
```

## Known blockers

- 

## Pitfall capture

- ask_to_capture_as_pitfall:
- pitfall_status:
- pitfall_target:
- pitfall_note:

## Out of scope

- 

## Git hygiene

Do not stage:

- local worktrees
- cache files
- unrelated untracked files

## Handoff notes

- 

## Human and AI roles

Record human decisions and the AI's implementation, investigation, documentation or
verification role separately from earlier human work. Keep implemented, verified,
merged and deployed states separate; follow the repository's publication policy.
