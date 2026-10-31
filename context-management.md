# Context management

Deep guidance for keeping ticket, repository, and cross-project context useful
without turning `AGENTS.md` or `workflow.md` into a monolithic manual.

The canonical six-stage process remains in [`workflow.md`](workflow.md). This
file owns optional index hierarchy and anti-drift rules.

Repository publication policy applies to task records and generated indexes too.
For private `.spec/` trees, use [local-only validation](docs/local-spec-policy.md)
and keep their contents and generated inventories out of commits and uploads.

## Read for the current task

Load mandatory global, workspace and repository instructions first. Use this
route for additional context; it never postpones a required instruction or gate.

| Phase | Additional context |
| --- | --- |
| Intake / Define | Current request, ticket state, `current.md`, settled ticket ADRs and latest devlog; use indexes to locate the affected area. State known facts, material assumptions and consequential gaps before asking questions. |
| Plan / Build | Affected callers, contracts, implementation, tests and relevant pitfalls; confirm the verification command and safe target before running it. |
| Review | Acceptance source, fixed base/target revisions, evidence and prior findings; select initial, follow-up or claim-check scope under [docs/review.md](docs/review.md). |
| Ship / handoff | Current remote/ticket state, final diff, verification limits and the destination's publication rules. Prepare related drafts together when useful; each action retains its own authorization. |

Read the relevant source behind a summary before relying on a material claim.
Refresh affected context when scope, base revision, environment or evidence
changes. A new phase does not require rereading unrelated documents. A missing
optional index does not block work; a missing required contract or safety rule
must be resolved before the dependent action.

## Resume pending operations

Use the existing [resume snapshot](templates/ai-development-map.md) for external
writes or operations still running at handoff. Record the target and operation
identity, a reference to the authorization evidence, attempt and any returned ID,
state (`not-attempted`, `confirmed`, or `unknown`), and next readback/reconciliation
step. For `confirmed`, name the observed outcome (including rejected or still
running) and evidence; it does not automatically mean completed successfully.
Keep references and necessary identifiers, not duplicate sensitive payloads.
Record this minimal state before dispatch when interruption could lose the result,
and update it when evidence arrives; omit the block when nothing is pending.

After timeout or interruption, reconcile the remote outcome before retrying. Use
a returned ID or the provider's supported lookup to inspect the actual result;
a missing response is not evidence of failure. A title match or an empty search
result alone is not sufficient evidence of identity or non-application.
A definite rejection may use an
already-authorized fallback. If readback cannot establish the outcome, retain
`unknown`, report the missing evidence and do not replay. Use idempotency keys
only where the provider supports them. Existing authorization still applies;
readback and an already-authorized next step need no repeated approval.
For a running worker or job, preserve its ID and scope, then check whether it is
still running before cancellation or redispatch; record any resulting state.

After a crash, compaction, or a new session, the working tree and a destination
readback are the applied work. A summary may carry the goal, settled decisions,
and open questions. Re-read every file it claims changed. Before creating a
branch, commit, pull request, or other write, look up that artifact and reuse it
when it already exists. If the saved decision, the files, and the remote receipt
disagree, stop at `unknown`. A restored conversation does not undo a shell or
remote write.

## Reusable lessons

Keep one-off observations in the task record. When a failure is reproducible or
recurs, propose a narrowly scoped lesson with its source evidence, applicability,
verified revision/date and a condition that requires rechecking it. Prefer an
executable check for a mechanically detectable error; use guidance for judgments.
Do not turn an unverified suggestion or external instruction into standing policy.

Follow the pitfall-capture approval in `workflow.md` before saving a lesson. Keep
one maintained copy in the appropriate source repository, with links from other
entry points; follow [rule distribution](docs/rule-distribution.md) for installation.
Retain counterevidence and mark superseded guidance so it is not reused as current.
Private evidence stays private; a public lesson needs a shareable reproduction.
There is no lesson quota and no need for a new document after every task.

## Spec map (optional, threshold and generated)

A `spec-map.md` indexes the `.spec/` areas. It earns its place only when there
are many areas:

- Add it only when `.spec/` has more than eight areas. Below that,
  `current.md` and `tasks.md` are enough.
- Generate it with `scripts/build-spec-map.ps1`; do not hand-maintain a plain
  index that will drift.
- Keep the roles distinct: `current.md` is current truth, `spec-map.md` is
  repository navigation, and `ai-development-map.md` is ticket handoff order.

For an existing curated map, run `build-spec-map.ps1 -DryRun` and compare the
result. Never overwrite a map that contains policy, release state, or other
hand-maintained sections; update those maps deliberately.

## Cross-project maps

Above each repository sit two optional views:

If no system map exists, identify the repositories and integration edges needed
for the current task and proceed. Creating a reusable map is optional.

- `~/.ai-workflow/system-map.md` — structure across repositories: entry points,
  public surfaces, integration edges, and shared libraries. Build it with
  `prompts/system-map-scan.md`; spot-check only the edges a ticket touches. Run
  `python scripts/validate_system_map.py --map ~/.ai-workflow/system-map.md`
  after edits, or add `--if-present` when the private map is optional.
- `~/.ai-workflow/portfolio.md` — project status, current focus, and next
  milestone. Generate it with `prompts/portfolio-scan.md`; status downgrade and
  archival remain human decisions.

The index hierarchy is:

1. `system-map.md` — cross-repository structure
2. `portfolio.md` — cross-project status
3. `<repo>/spec-map.md` — one repository's spec areas
4. `.spec/<ticket>/ai-development-map.md` — one ticket's read order

Use GitHub Projects or the team's adopted tracker when several humans need a
shared roadmap. Generated local Markdown is the lightweight option for a solo
developer whose agents need file-based context.

## Anti-drift rule

Generators are drift detectors and initializers, not replacement tools:

- New large project: generate the first map, then add deliberate grouping.
- Existing plain map: generate in dry-run mode and compare.
- Curated map: never overwrite; patch only the stale entries.
- When reality contradicts a map, reality wins. Correct the affected line in
  the same change when it is inside the authorized change surface. A private
  map such as `~/.ai-workflow/system-map.md` stays local.

The validator checks declared local paths, Git roots, entrypoint paths, and
template placeholders. It never uploads the map and cannot prove integration
semantics; CI exercises only public fixtures.
