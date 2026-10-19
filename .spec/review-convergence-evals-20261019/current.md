# Review convergence and pilot evaluation

## Goal

Add a three-round reconsideration trigger to the existing review contract and a
small reproducible reviewer evaluation set based on two historical defect classes.
User accepted these two improvements after the Claude Code team review article.
Base: d6f1e10e3071338bd28298e38b3e0fcfc90b48c3.

## Acceptance criteria

- [x] Observable: Three completed substantive review rounds without convergence require a recorded reassessment before another round; unresolved findings/gates remain open and approval is never inferred.
  - Environment: Existing review contract, dispatch prompt and packaged adapters.
  - Verify: Read three-round, clean-first-pass, new-risk and interrupted-worker scenarios; run mirror contracts.
- [x] Observable: Two historically grounded defects have independently specified positive/clean pairs and executable reference checks. Review packets exclude answer keys.
  - Environment: Four minimized Python modules using synthetic callbacks/text only.
  - Verify: Run fixture behavior tests; keep the contract fixed while comparing defective and corrected variants.
- [x] Observable: Offline scoring counts detected/missed defects, false alarms, duplicate findings, completion and review rounds, with infrastructure failures separate; invalid or incomplete records are rejected.
  - Environment: Adjudicated JSON records, no provider/network calls.
  - Verify: CLI tests with hand-calculated scores, negative inputs and a targeted scorer mutation.
- [x] Observable: A bounded fresh-context pilot preserves raw reports and states its isolation, model and small-sample limits; no measured improvement or unattended enforcement is claimed.
  - Environment: Exported answer-free packets and separate adjudication.
  - Verify: Read reports and score against the frozen oracle; record contamination/permission limitations.

## Non-goals

No automatic merges, CI/billing changes, private company data, new REVIEW.md
hierarchy, provider scheduler or repeated paid benchmark. Existing approval and
local-only policies apply. Source preparation and local execution are authorized;
publication/installation status must be recorded separately.

## Delivery state

Reviewed source `878fd47e6ff702c97b58389197341f2a9da269f8` is merged and published
on main following Zoe's explicit 2026-10-19 approval. Remote SHA readback matched.
The navigation finding is fixed; the reviewed payload hash and verification remain
unchanged. Machine installation was not part of this main-only delivery and remains
at the previous source revision; see audit.md for the separate delivery states.
