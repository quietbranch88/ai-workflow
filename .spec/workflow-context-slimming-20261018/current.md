# Proportional workers and compact handoffs

## Goal

Align the parallel audit recipe with existing proportional controls, preserve worker
recovery state, and remove duplicated handoff state without weakening evidence gates.
Base: `a1444616b04a909ba5205b21f6d681e7341b7a87`.

## Acceptance criteria

- [x] Observable: Worker count respects independent scopes, capacity, aggregate budget and explicit user model/count choices; actual API scheduling replaces message-batching and speed guarantees.
  - Environment: Documentation in the source checkout.
  - Verify: Read the two-scope/two-slot and one-slot examples and compare with workflow.md; inspect permission and resource-ownership statements.
- [x] Observable: Success, failure, live timeout and unknown interruption retain ID/scope/status, partial evidence and bounded recovery without duplicate live work.
  - Environment: Documentation tabletop, not an agent-runtime experiment.
  - Verify: Trace each scenario through prompts/parallel-audit.md and context-management.md; record results in audit.md.
- [x] Observable: Handoff keeps its resume snapshot and pending operations while pointing to current/tasks/audit and settled decisions, including counterevidence.
  - Environment: Template and required workflow read order.
  - Verify: Compare template sections against the base revision; inspect required-record preservation and link targets.
- [x] Observable: Mirrors, plugin version and living records agree and repository checks pass.
  - Environment: Local source checkout, plugin 0.6.5.
  - Verify: Run git diff --check, python3 scripts/check_close_the_loop.py, the repository unittest suite and changed-file Ship validation.

## Non-goals

No new agent router, runtime mechanism, benchmark, test framework, installation,
commit, publication or merge in this builder step. No private audit paths or company
material in published records. No measured performance or token reduction claim.

## Delivery state

Reviewed source 8cc6234 is published and installed, with separate remote/local SHA
readback recorded in audit.md. These are source-file observations; running-session
reload and runtime/agent-quality claims remain outside the verification evidence.
