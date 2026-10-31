# Review Checklist

Select initial, follow-up, or claim-check mode using [`code-review.md`](code-review.md).
An initial review omits the authoring transcript and the author's defense.
Mode scope, partial-review labeling, stop conditions, and the three-round
checkpoint are in [docs/review.md](../docs/review.md).

## 1. Spec conformance (highest)

- [ ] Implements every required case in the task's `.spec/<ticket>/current.md` (or the repository's established spec path)?
- [ ] Stays inside scope (no scope creep)?
- [ ] Respects stated invariants?
- [ ] If deviates from spec, is the deviation documented?

## 2. Correctness

- [ ] nil / empty handling on all inputs
- [ ] Error paths covered
- [ ] Off-by-one, boundary conditions
- [ ] Type assertions / conversions that could panic

## 3. Concurrency (if applicable)

- [ ] Goroutine ownership clear (who cancels, who waits)
- [ ] Shared state protected
- [ ] Context propagated
- [ ] `-race` clean

## 4. Security

- [ ] Input validation at trust boundaries
- [ ] No SQL / command injection vectors
- [ ] No secrets in logs / error returns
- [ ] Auth checks on protected paths

## 5. Maintainability

- [ ] Names match spec vocabulary
- [ ] Abstractions justify their responsibility, dependency boundary or test seam; a single implementation is not itself a defect
- [ ] No hallucinated APIs (verify external calls exist)
- [ ] Comments explain WHY where non-obvious

## Output format

```
## Review

### MUST FIX (blocking)
- [file:line] <issue>

### SHOULD FIX
- ...

### CONSIDER
- ...

### Spec conformance: PASS / PARTIAL / FAIL

### Review coverage
- Artifact/revision: ...
- Round / convergence reassessment: ...
- Categories reviewed: ...
- Not reviewed / blockers: ...
```

Use the finding evidence and validity/disposition fields in [docs/review.md](../docs/review.md) within the output above. Stopping and partial coverage follow that contract.
