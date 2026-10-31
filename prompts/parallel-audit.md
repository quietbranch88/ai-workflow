# Parallel Audit Pattern

Use for independently useful read-only audit scopes when delegation is authorized.
A single bounded scope usually stays local; sequential dependencies stay sequential.
For implementation use isolated builders under [workflow.md](../workflow.md#parallel-agents).

## Dispatch

1. Identify independent scopes and choose the worker count from their value,
   available worker slots, and the aggregate time/token budget. Respect explicit
   user model/count choices; if capacity is lower, schedule bounded waves. Report
   unavailable requested models or infeasible budgets rather than silently changing
   the request. Do not add redundant scopes merely to fill slots.
2. Record each worker's scope, assigned role/model, deadline or stop condition,
   retry limit, and owner in the existing task record. Use capability roles such
   as read-only explorer or reviewer, mapped to the actual tool API.
3. Dispatch using that API's scheduling semantics without awaiting each worker's
   completion before launching independent work. Calls in separate messages can
   overlap when dispatch is asynchronous; putting calls in one message alone
   does not guarantee concurrency. Respect runtime limits and tool restrictions.
4. Give each worker a self-contained question, acceptance source, fixed revision
   or artifact, allowed reads/commands, evidence format and a short report limit
   (usually 200 words). Record the returned worker ID immediately.
5. Continue independent work, then spot-check load-bearing claims and synthesize
   evidence and missing coverage into the existing audit. Do not repeat the whole
   delegated search or treat agent agreement as independent proof.

A requested read-only role is an instruction, not enforced filesystem or tool
isolation. Record actual permissions; use enforced restrictions when available.
Do not call a shared writable checkout sandboxed merely because the prompt says
“do not edit.” Name owners for any mutable test resources, accounts, ports or
artifact paths; isolate them or serialize contested use. A read-only audit must
not acquire mutation authority through this resource checklist.

## Bounded lifecycle

Keep worker ID, scope, owner, last observed status and evidence in the existing
task/handoff record. Track queued, running, completed, failed, cancelled or unknown
as observed; a deadline is not proof that a worker stopped.

- On success, preserve the report and evidence before releasing owned resources.
- On explicit failure, preserve partial results and identify uncovered scope.
  Retry only within the assigned budget, after confirming the worker stopped and
  reconciling its resource ownership; otherwise report partial coverage.
- On timeout or interruption, inspect status using the known ID before cancellation
  or replacement. If still running, choose a bounded wait or authorized cancellation.
  Verify cancellation/stoppage before replacing the same scope or releasing resources.
- If status cannot be established, retain `unknown` with the next readback step;
  do not launch a duplicate or claim complete coverage. Preserve useful workers,
  partial evidence and owned resources for resumption instead of blind cleanup.

Follow [operation resumption](../context-management.md#resume-pending-operations)
for pending operations. The coordinator owns reconciliation and may finish with an
honest partial report when the budget expires; it need not wait forever for all workers.
For builder work, one integration owner checks the assembled revision before
claiming combined behavior verified; individually passing reports are insufficient.
A conflict-free merge stays untrusted until those checks pass on the assembled
tree, including a shared contract one side changed and behavior both sides implemented.

## Template prompt

```text
Role / question: read-only explorer or reviewer; one bounded question.
Context: repository, purpose, acceptance source, base/target revision.
Scope / owner: allowed files and commands; resource ownership if relevant.
Permissions: requested read-only; actual enforced restrictions or their absence.
Budget: deadline/stop condition, retry limit; coordinator tracks aggregate budget.
Checks: specific independent checks and counterevidence to inspect.
Return under 200 words: findings with file:line and checked evidence, counterevidence,
coverage, blockers and unverified boundaries. Preserve partial results on failure.
Do not edit files or execute mutating commands.
```

## Example

An audit with two independent scopes (API validation and UI error handling) and
two available worker slots can dispatch one bounded worker per scope. With only
one available slot, use sequential waves or keep the work local unless delegation
was requested. The coordinator records both IDs and reconciles any failed or
unknown scope before replacement, then reports combined coverage and its limits.

There is no promised speed or token saving. Any performance claim needs a
comparable serial baseline, end-to-end elapsed time, total tokens and quality
outcomes; scheduling overhead and synthesis can outweigh parallel execution.
