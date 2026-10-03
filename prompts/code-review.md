# Prompt: Code review

Use the installed reviewer role with the appropriate mode. Supply the concrete fields below; do not send unresolved placeholders. For a small change, user requirements can replace a spec document.

```text
Independently review this work. Treat my explanations and previous reviewer conclusions as claims to verify. Report no finding when evidence supports none.

Repository/worktree: <absolute path>
Target: <commit SHA or captured uncommitted patch identifier>
Mode: <initial | follow-up | claim check>
Acceptance source: <resolved spec path or explicit requirements>
Initial patch base: <SHA>
Previously reviewed revision/report: <SHA and report path, or none>
Open findings: <IDs, claims, fixes and evidence pointers, or none>
Dismissed/deferred/risk-accepted findings: <record links and reasons, or none>
Changed boundaries and available test environment: <facts and limitations>
Requested next step: <e.g. prepare PR; no authority to publish or merge>

Initial mode: review the full intended patch and relevant callers/writers against the acceptance criteria.
Follow-up mode: start from the previous reviewed revision to the target, verify open findings and inspect the fixes' impact. Reopen earlier decisions only with new evidence. If the base/history changed, examine that delta and state additional coverage needed.
Claim-check mode: check the changed statements and evidence, including related delivery records. Do not infer runtime behavior from source alone. Build/release/schema-generation changes retain their applicable verification gates.

Expand the review when the delta reveals a new material risk or changes a shared contract, authorization, transaction or service boundary. Explain the reason and affected paths; do not silently re-audit everything or ignore a serious issue outside the list.

Return review coverage, evidence-backed findings, dispositions for requested finding IDs, and a recommendation with unresolved gates. Follow docs/review.md in the workflow source, plus applicable repository rules. Distinguish blocking defects from optional improvements. Do not edit the deliverable or remote records.
```

After review, the coordinator checks the evidence before adopting recommendations, applies authorized fixes, updates their existing records, and dispatches only the appropriate follow-up scope. Stop once blockers and applicable gates are addressed and claims agree; optional style suggestions alone do not require another round. Track additional review rounds only when they resolve a named uncertainty or inspect a new change.
