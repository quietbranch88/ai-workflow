# Verification contracts

Apply the gates the change actually affects. Documentation and behavior-neutral
edits use claim review and relevant validators; do not invent runtime tests.

## Before implementation

State an observable acceptance contract independent of the proposed code structure.
Include compatibility, failure behavior and the requirement source: a product rule,
existing invariant, versioned contract or incident fixture. AI may propose fixtures
and counterexamples, but its implementation is not the test oracle.

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

## Evidence record

Record revision, environment/service versions, exact commands or reproducible steps,
discovered tests, assertions, results, skipped cases and redacted artifacts. Separate
source inspection, executed tests, deployed observations and causal conclusions.
Evidence for one handler or time window does not establish a total system outcome.
Reconcile completion claims with [review and delivery records](review.md).
