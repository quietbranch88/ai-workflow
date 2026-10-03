# Review modes and finding decisions

Use fresh context with a bounded target, acceptance source, patch base, prior
reviewed revision/report and known finding decisions. Prior agent agreement is not
independent evidence. Report no finding when the evidence supports none.

- **Initial:** inspect the intended patch, relevant callers/writers and every
  applicable risk category, even after finding a blocker.
- **Follow-up:** start at the last reviewed revision; verify open findings and the
  fixes' affected paths. Reopen earlier decisions only with new evidence. Explain
  expansion for new risks, shared-contract changes or changed base/history.
- **Claim check:** review changed statements against their evidence and related
  delivery records. Do not rerun unrelated runtime suites for wording changes.
  Build/release/schema-generation changes retain their relevant verification gates.

## Finding contract

For each actionable finding record stable task-local ID, severity and impact,
reviewed revision, file/line or precise artifact location, trigger/preconditions,
affected path, expected versus actual behavior, requirement source and checked
evidence. Label source traces, executed reproductions and missing boundaries
honestly. Keep hypothetical concerns separate from confirmed defects.

Check relevant callers, writers and guards for counterevidence before adopting a
finding. Compilation, startup or environment failure does not prove a false
positive. A proposed test is not an executed test; do not run unsafe reproductions.

Track two independent fields:

- **Validity:** `pending`, `confirmed`, `false-positive`.
- **Disposition:** `open`, `fixed`, `deferred`, `risk-accepted`, `dismissed`.

A dismissal needs counterevidence and a reason. Deferral needs a reason and next
step; it is not risk acceptance. A fix needs its revision and required verification;
missing verification keeps it open. Risk acceptance needs the named risk, owner,
dated explicit decision, scope and review conditions; silence or generic approval
is insufficient. Preserve rejected findings and status-change reasons in the
existing audit; cite new evidence when reopening one.

## Coverage and stopping

Report artifact/revision, reviewed categories and unreviewed scope/blockers. Do not
label a partial review complete. The coordinator validates evidence, applies fixes
and requests only the appropriate follow-up scope. Finish when blockers and
applicable gates are addressed and material claims agree; optional nits do not
require repeated full reviews. Existing approval requirements still apply.

## Close the delivery loop

Before substantial work closes, reconcile audit, tasks, changelog, PR description
and tracker acceptance/status where applicable. Keep implemented, verified, merged
and deployed separate. Check current remote content before alleging a mismatch.
Update only authorized surfaces and read them back; record exact outstanding
corrections and next actions when access or authorization is absent. Retain a dated
correction for previously shared inaccurate claims with links to superseded evidence;
do not rewrite merged history. This step grants no messaging, merge or deploy authority.
