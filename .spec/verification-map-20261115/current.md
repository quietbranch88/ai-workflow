# Acceptance-to-evidence mapping

## Goal

Connect important acceptance criteria to existing task checks and defect-detection
evidence without adding another record format or treating prose as proof.

## Scope

Extend the existing document validator, spec/task templates and verification
contract. Pilot the mapping on this validator change. Preserve legacy tickets,
WIP work, immutable Git-range reads, local-only records and existing authorization.
No product runtime changes, fixed verification-token quota, new telemetry,
blanket API bans, formal-method installation, push, merge or global-rule changes.

## Acceptance criteria

- [x] AC-1: Mapped tasks cannot claim a structurally complete link with missing fields.
  - Observable: missing/duplicate/unknown criterion IDs, uncovered criteria, empty
    evidence and absent or malformed detection records fail the validator.
  - Environment: isolated temporary repositories, public validator CLI.
  - Verify: `python3 -m unittest discover -s tests -p test_verification_map.py`.
- [x] AC-2: Draft and legacy records retain their existing behavior.
  - Observable: legacy tasks pass; mapped open tasks allow planned evidence in
    WIP, while Ship rejects unchecked work under its existing rule.
  - Environment: the same CLI fixtures and existing enforcement regressions.
  - Verify: mapped fixture tests plus `test_workflow_enforcement.py`.
- [x] AC-3: Validation reads target-commit bytes and never runs recorded commands.
  - Observable: a fixed Git-range check ignores a repaired working copy; a
    sentinel command inside Verify cannot create its marker during validation.
  - Environment: isolated local Git fixture with synthetic text only.
  - Verify: fixed-revision and command-sentinel regression tests.
- [x] AC-4: Canonical guidance, mirrors and recorded delivery state agree.
  - Observable: documentation describes the structural limit, evidence reuse,
    risk-based mutations and optional formal methods without a 70% quota;
    package/CI-equivalent checks pass, with no claim of publication/activation.
  - Environment: isolated source checkout, tracked outgoing range.
  - Verify: repository suite, package validators, scans, diff and Ship checks.

## Non-goals

The validator cannot prove commands ran, an oracle is independent, a mutation
was meaningful, a claim is true, or integration/E2E passed. Those require actual
execution and review. No historical ticket migration or fresh product pilot.
