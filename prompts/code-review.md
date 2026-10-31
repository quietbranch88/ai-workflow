# Prompt: Code review

Use the installed reviewer role with the appropriate mode. Supply the concrete fields below; do not send unresolved placeholders. For a small change, user requirements can replace a spec document. Initial, follow-up, and claim-check scope, partial-review labeling, stop conditions, and the three-round convergence checkpoint are in [docs/review.md](../docs/review.md).

```text
Independently review this work. For an initial review, omit the authoring transcript and the author's defense. See docs/review.md. Previous conclusions are claims, not the verdict. Report no finding when evidence supports none.

Repository/worktree: <absolute path>
Target: <commit SHA or captured uncommitted patch identifier>
Mode: <initial | follow-up | claim check>
Completed substantive rounds for this change: <number; initial dispatch is 0>
Latest convergence reassessment and next-round budget: <record link or not yet required>
Acceptance source: <resolved spec path or explicit requirements>
Initial patch base: <SHA>
Previously reviewed revision/report: <SHA and report path, or none>
Open findings: <IDs, claims, fixes and evidence pointers, or none>
Dismissed/deferred/risk-accepted findings: <record links and reasons, or none>
Changed boundaries and available test environment: <facts and limitations>
Requested next step: <e.g. prepare PR; no authority to publish or merge>

Return review coverage, evidence-backed findings, dispositions for requested finding IDs, and a recommendation with unresolved gates. Distinguish blocking defects from optional improvements. Do not edit the deliverable or remote records.
```

The coordinator follows [docs/review.md](../docs/review.md) before adopting a recommendation or dispatching another round.
