# Verification contracts

Apply the gates the change actually affects. Documentation and behavior-neutral
edits use claim review and relevant validators; do not invent runtime tests.

## Before implementation

State an observable acceptance contract independent of the proposed code structure.
Include compatibility, failure behavior and the requirement source: a product rule,
existing invariant, versioned contract or incident fixture. AI may propose fixtures
and counterexamples, but its implementation is not the test oracle.

Each criterion states one decidable behavior: the input, the observer-visible
result, and one behavior that must not change. A filled label is not that
contract. "Tests pass", "inspect the diff", or "the report exists" can be true
while the original goal is unmet.

Map the actual entrypoint through services, storage, queues and devices to the
observable result. Name the boundaries the acceptance test must exercise. Backend
paths do not need an artificial browser step. Record missing environments separately
from code defects.

## Defect detection and scans

- TDD is optional unless the user or repository requires it. Never claim a red/green
  sequence that did not run. Review expected values independently when the same
  agent writes both production code and tests; do not weaken assertions or mock the
  boundary whose behavior needs proof.
- For bugs and regressions, show a failing baseline, historical defective revision
  or safe controlled mutation. For other behavior changes, use a meaningful mutation
  unless existing fail-to-pass evidence detects the same defect.
- Mutate only the production behavior under test in an isolated copy; keep tests
  and expectations unchanged. Confirm failure is the relevant assertion, not build
  or startup failure. Restore the behavior and rerun successfully. Never mutate
  deployed data or leave the mutation in the deliverable. Record why any required
  evidence was impractical or unsafe instead of implying it exists.
- Run repository-available static security, dependency advisory and secret scans
  for executable code, dependencies, build/release or secrets-sensitive changes.
  Record absent tools and skipped gates; a scan does not prove business logic.
- Before installing or rewriting a lockfile, record each direct dependency's
  name, registry, and version, and install from the existing lock unless the
  task is to add or upgrade it. An advisory scan does not prove the package is
  the intended project. Leave install scripts off unless that package needs
  them, and run the install without secrets.

## Real boundaries and results

- Cross-service/device workflows, identity propagation and critical journeys require
  a targeted run through the affected real chain in a safe test environment before
  calling the workflow verified. Assert the user outcome and relevant durable state
  or downstream delivery, including affected retry, duplicate or recovery cases.
- Web UI changes require relevant UI tests and Chrome automation through the actual
  interaction and expected result; inspect layout and relevant states too. Native UI
  uses the app/emulator. Missing targets leave visual/flow verification incomplete.
- Browser tests with mocked APIs prove frontend flow only; database tests prove that
  integration only. HTTP success, navigation and screenshots alone do not prove an
  end-to-end outcome. Declare substituted boundaries. Use actual application
  migrations/configuration in isolated database verification.
- For irreversible behavior (deletion, wipe, unenrollment, factory reset, payment),
  require successful safe E2E before merge or an explicit recorded owner decision
  accepting the named gap. Record revision/path, missing evidence and possible
  triggers. Generic merge approval is insufficient. A waiver remains unverified
  and does not authorize production mutation.
- If a producer, consumer, credential, device or environment is unavailable, name
  the blocked hop. Do not downgrade the gate or call the full path verified.

A shared or deployed database migration is classified before it is run. Additive
expansion that stays compatible with the deployed app needs a dry run on a
disposable restored or sanitized snapshot, and a recorded reverse or roll-forward
with its loss window. A destructive contraction needs proof the old shape is
unused, a rehearsed restore, and a separate human approval of that step. The
agent may draft the migration and the dry-run report. Production credentials
stay with the owner.

## User-visible checks

A UI or end-to-end check proves a result a person or client can observe. Take the
assertions from the acceptance contract or an existing product or QA case: the flow,
the page or client, and what is visible on success, while waiting, and on failure.
Reading the implementation and restating its branches checks the code structure.

An API check through the real client belongs when that response is the contract.
A result the user sees still needs the UI path.

For a web UI change, exercise the affected path in the real browser before encoding
it as a repeatable check. Record the entry, the actions, the visible result, and
any blocker the source does not show, such as an obscured control or a delayed load.
The walk narrative is a claim. The recorded visible result is the evidence. A
screenshot or log may carry that result; pair it with the asserted outcome and any
required durable state or downstream effect.

After each action, record the new visible state. Stop when it is not the case's
result; later actions in that walk do not count. Reaching the same screen by
another path is not that flow. Find the control by its accessible name, label, or
visible text, and act only once it is visible and operable. While walking, also
notice a focus trap, scrolling behind an overlay, a control that moves before the
action, and a narrow viewport.

A repair may change how a control is found or how long the runner waits. It may
not replace the acceptance result with the behavior just observed. A generated
check that fails on the current tree is inspected as a possible product failure.
Do not drop or rewrite it to make the suite green, and do not count an assertion
that accepts the error just seen. Review matches each assertion to the acceptance
case and the observed result. Expected values copied from the implementation, or
checks that only assert no error or that a page opened, do not prove the result.
On a failed or blocked walk, keep the last visible state from the failing attempt.
That record explains the failure and leaves the run unverified.

Keep the confirmed path in the project's existing UI test runner so later
verification does not depend on an agent repeating the walk. A green suite that
does not assert this visible result, or that has no fail-to-pass or mutation
evidence for it, leaves the path unproven; use the defect-detection rules above.
A check that passes and fails with no product change is unstable evidence: record
the flake and leave that run unverified. A later attempt that passes after a
failure on the same code is still unstable evidence. A retry is not a pass.
Quarantine removes a known flake from the blocking gate only. Record an owner and
a reason, keep the check visible, and leave every path it covers unverified until
the check is stable and back on the gate. A missing browser or device leaves the
flow unverified.

When an agent drives the browser, confirm the origin, data store, providers, and
credentials are the isolated test target, and start a clean browser rather than a
person's profile or ambient session. Each attempt creates its own synthetic
records, changes only those records, and deletes those exact ids if the walk stops
early. A shared account is for sign-in only. A missing target or seed leaves the
browser path unverified.

Keep a browser check for a critical journey whose failure a unit, service, or
contract test cannot observe. One such journey needs one browser check. Cases
those lower layers can already fail stay there.

Observed usage may suggest a case. The acceptance contract remains the requirement
source.

## Domain-specific checks

Select from the affected contract, not a universal checklist:

- **Database/search:** version-matched real engine, actual migrations, ordering,
  duplicates/skips, transaction rollback and physical index/migration postconditions.
- **Auth/user data:** real authorization path, allowed and cross-tenant/role denied
  access, expiry/revocation, trusted identity and pooled/cache cleanup; retention,
  disclosure, third-party sharing and deletion. An empty UI does not prove denial.
- **Payments:** sandbox amount/currency invariants, idempotency, authenticated replay,
  ledger reconciliation and relevant failure, refund and retry paths.
- **External APIs/cloud:** versioned contracts and real boundary evidence where
  access permits; timestamped logs/config/resource state and affected recovery.
  A snapshot does not establish durable recovery or customer impact.
- **Performance:** workload/data shape, environment, warm-up, repetitions, statistic
  and before/after revision. Measure the complete claimed boundary, including lazy
  evaluation and serialization. Separate fixture queries, assert correct results
  across sizes and detect the relevant regression. Query counts alone do not prove
  throughput, end-to-end latency, production percentiles or cost savings.

## Messaging and caches

Before materially changing Kafka/Redis behavior, read the existing contract and
record only affected decisions. Use an ADR for real tradeoffs. Resolve consequential
product ambiguity with the owner; do not infer durability from defaults.

Define success through the final side effect, source of truth and owners; allowed
loss, duplication, delay, ordering, staleness and recovery window. Record actual
broker/client versions, topology and effective settings without credentials.

- **Kafka:** event identity/dedup key, schema compatibility, partition/ordering
  scope, retention and sensitive data; success/ack timing, retry limits, offset
  commits, poison-message and recovery ownership. Specify DB/publication consistency
  and side-effect/progress recovery from partial failure. Choose replication,
  minimum ISR, leader election, retention and backpressure for the stated contract.
  Producer idempotence does not make the whole business operation exactly-once.
  Trace event IDs through real producer, consumer and durable effects; exercise
  broker/consumer failure and replay where required, only in an isolated environment.
- **Redis:** distinguish cache, session, lock, dedup and queue roles. Specify tenant
  keys, TTL/invalidation, eviction, persistence, read routing, topology, timeouts,
  retries and outage behavior. Use the actual application client/configuration.
  Cache tests populate/update/delete via the application and check allowed staleness,
  expiry, stale refills, eviction and bounded source fallback load. Sessions require
  expiry/revocation, isolation and fail-closed authorization. Locks require competing
  clients, lease expiry, delayed workers, owner-checked release and fencing or an
  equivalent stale-write guard when required. Queue/Stream/PubSub tests verify the
  mechanism's delivery, ack and recovery contract and final effects; PubSub does
  not replay missed messages. Exercise matching failover/persistence topology when
  required. SET NX or WAIT alone proves neither safe effects nor zero loss.

Design-approved, implemented, integration/E2E-verified and deployed are distinct.
Missing topology is a blocker, not permission to test destructively in production.

## Agent evaluation is separate from patch verification

Record model/configuration, harness, tools/permissions, task set, retry/token/time
budget, CPU/RAM guarantees, kill limits, timeout, concurrency, network, caches and
service versions. Start trials clean and isolated. Prove task solvability with a
reference path; expose every graded condition and include positive and negative
cases. Prefer deterministic outcome/durable-state graders; calibrate model judges
against humans. Grade exact tool sequences only when required by the contract.
Keep evaluation data independent, preserve trajectories for sampled review and
account for access to tests, graders, fixtures or history. For probabilistic claims,
use repeated trials and report sample size, pass rate, variance and failure classes;
separate infrastructure failures from assertions. Coverage/mutation scores and one
synthetic session do not establish agent quality, reliability or adoption.

For a bounded reviewer-specific pilot, see `evals/reviewer/README.md` in the workflow
source. Its adjudicated metrics do not replace patch acceptance or human authorization.

### Cost comparisons

Distinguish billed currency, price-based estimates, and token proxies; a token
reduction alone does not establish a lower bill or subscription charge. Record
the billed model, usage source, price source/date and currency. Where charged,
include uncached input, cache reads, cache writes and output, including cache
rebuilding after tool/configuration changes. Count optimizer/judge calls, retries,
failures and unfinished attempts in both arms. Report usage coverage and unknown
prices or missing usage explicitly, never as zero or silently excluded savings.
Report human setup, review and recovery time separately.

Pair A/B trials on the same task and starting revision with fixed model,
configuration and budgets except the tested change; interleave the trial order.
Apply the isolation and repeated-trial rules above, controlling cache conditions
and keeping learned history separate from held-out evaluation tasks. Predeclare
the cost metric, quality checks, acceptable regression margin and trial budget.
Report paired differences and uncertainty, including failures. A small pilot
(such as ten tasks) establishes feasibility only; if the evidence cannot support
both savings and the quality criterion, report `inconclusive` before expansion.

Use existing authorized usage records and task notes for a bounded pilot. This
contract does not require new transcript collection, background model judges,
automatic tool pruning or loop intervention.

## Shape checks and ceilings

A project's shape or size check fails because the change grew the structure:
another path, a longer capped file, or a higher limit. Revert the step that
grew it. Do not raise the ceiling, add a public URL, a fake-success route, or
a release-check file so the command passes. Lower the ceiling in the same pull
request only after an extra path was actually removed. Raising a ceiling stops
for the owner's decision.

The live instruction is the current section the project names. Dated sections
are history. One pull request removes one extra path. For that removal, write a
failing test, then one named small refactoring that makes it pass. Visible
behavior stays until the last step deletes the path. If that step is red,
revert only that step. A closed switch stays off the production path. Do not
change production configuration or split a module this task did not name. Put
the code and one status line in the current section in the same pull request.
A personal project also includes `devlog.md` and `todo.md`. A team project
follows its own convention for those two files.

## Acceptance-to-evidence links

Use the existing `current.md` and `tasks.md`, not a second evidence document.
Give acceptance checklist items stable `AC-1:` IDs. New task templates declare
`Verification map: required`; each mapped task has `Acceptance: AC-1` (or a
comma-separated list), `Oracle`, `Required boundary`, `Verify`, `Detection` and
`Evidence` fields. Setup tasks need no artificial acceptance link.

Use `Detection: mutation: <evidence reference>` or `fail-to-pass: <reference>`;
for behavior-neutral work use `not-applicable: <reason>`. Reuse valid detection
evidence for the same requirement and tested revision/boundary. Prioritize critical
failure paths and settings; no global mutation or verification-token percentage
is required. A planned WIP record may say evidence is not run yet; keep it open.
The validator does not detect a checked task whose evidence was never run;
reviewers check that.
Its filler check catches common template placeholders (empty, `TODO`, `N/A`,
`<lowercase slot>`); it is a heuristic, so reviewers still read every value.

The existing document validator checks declared/covered IDs and populated fields
when the marker or an Acceptance field is present. Legacy tickets remain valid
without opting in. It reads the target Git revision in range mode and never runs
recorded commands. It cannot establish evidence truth, independence or product
correctness; reviewers inspect the referenced results and product CI runs the
checks. Passing this structural gate is not a product-verification claim.

## Enforceable safeguards

For a recurring or reproducible mistake, assess the smallest check that can reject
it: a type/API constraint, lint rule or regression test. Record the failure evidence,
requirement source, affected callers and chosen enforcement point in the existing
task audit. If it is a judgment rather than a mechanically detectable property,
retain concise guidance. This assessment does not require a new check per review.

Before adopting a check, run a representative valid case and a deliberately invalid
case. Keep the oracle unchanged and confirm the invalid case fails for the intended
reason; reuse equivalent fail-to-pass evidence. Record where the check actually runs
(local, CI or both), its coverage and exceptions. A local hook is not server
enforcement. Remove a redundant prose reminder only after its replacement is
verified, retaining requirement sources, rationale and authorization boundaries.

Constrain an API only when observed misuse or a concrete contract risk justifies it.
Inspect the actual client/version and callers before choosing a typed result,
existing adapter, narrow wrapper or lint restriction; do not add a wrapper by default.
State allowed callers, migration/compatibility behavior and justified exceptions.
Verify the real adapter boundary and relevant failures, and check bypasses at the
claimed enforcement point. A restriction requires project-scoped authorization;
this guidance neither bans APIs globally nor authorizes modifying shared CI.

For example, a Kafka interface can distinguish queued, broker-acknowledged,
rejected and unknown outcomes. Queue admission is not broker acknowledgement;
acknowledgement is not consumer completion. Timeout can mean an unknown outcome,
not confirmed rejection. Test the configured client's actual contract; do not
promise durability or exactly-once effects from an interface name or a unit test.

## Formal methods during Plan

Consider formal methods when a consequential property is hard to examine with
ordinary tests: concurrent transitions, retries and partial failure, or a precise
algorithmic invariant. Record the decision in the existing plan; simple bounded
error propagation needs no model. Use TLA+ for state-transition designs and Lean
for explicit propositions/proofs when appropriate expertise and tooling are available.
Neither tool is a universal requirement or a substitute for integration evidence.

Start from the User Story and acceptance invariants, then describe the smallest
relevant states/actions and environmental assumptions. For TLA+/TLC, record the
model/configuration revision, finite bounds, checked safety properties, and any
liveness/fairness assumptions. Distinguish exhaustive exploration within those
bounds from simulation or an incomplete run. A successful bounded check is not
an unbounded proof. For Lean, record the theorem, assumptions/axioms, tool version
and checked proof status; a proposed proof or a proof with unfilled obligations
is not a completed verification.

Inspect counterexamples against the product requirement before changing the model;
do not weaken an invariant or exclude a required failure simply to obtain a pass.
Map model actions/proof assumptions to implementation boundaries and turn applicable
counterexamples into regression cases. Apply defect-detection checks to important
implementation paths with unchanged test expectations. Record abstractions, omitted
failures and remaining real-boundary checks in the audit. A model/proof result does
not establish that production code implements it.

Kafka retry example (illustrative, not an executed model): distinguish broker
acceptance from delivery of its reply. Explore accept -> reply lost -> timeout ->
retry, with duplicate effects if the modeled consumer lacks deduplication. Require
an explicit business contract before adding deduplication; producer idempotence
alone does not prove exactly-once business effects.

## Verification effort and feedback

Allocate verification by affected risk, uncertainty and uncovered acceptance, not
a fixed percentage of tokens or a universal mutation score. Prioritize critical
failure paths and meaningful boundaries. Reuse passing evidence only when revision,
inputs and environment remain applicable; rerun affected checks after changes.

Use existing authorized task/usage records to identify repeated reads, redundant
checks and missing evidence. Record which acceptance criteria a check exercises,
what it detected and what remains unverified. Keep cached input, uncached input,
output and any included reasoning distinct; serialized image payload length is not
a text-token count. Include review agents and failed attempts when their usage is
available, and report missing coverage rather than estimating savings from file
size. Apply the cost-comparison contract before claiming improvement. This adds no
background collection, schedule, fixed quota or new transcript retention.

## Evidence record

Record revision, environment/service versions, exact commands or reproducible steps,
discovered tests, assertions, results, skipped cases and redacted artifacts. Separate
source inspection, executed tests, deployed observations and causal conclusions.
Evidence for one handler or time window does not establish a total system outcome.
Name the original goal and what this run actually exercised. State whether the
observed result matched that goal, and which part was not compared. A green
suite, a file that contains the required words, or a command that exited 0 does
not by itself establish the comparison.
Reconcile completion claims with [review and delivery records](review.md).
