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
