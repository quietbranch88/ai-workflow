# Review Checklist

Select initial, follow-up, or claim-check mode using `code-review.md`. For an initial review, cover every applicable category in priority order, even after finding a blocker. For follow-ups, cover the changed behavior and open findings, expanding to related paths when new evidence or risk warrants it; do not automatically repeat the full initial review.
If access, time, or another blocker prevents completing the review, report the
reviewed artifact/revision, covered categories, and unreviewed scope explicitly;
do not label a partial review complete or approved.

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
- Categories reviewed: ...
- Not reviewed / blockers: ...
```

Use the finding evidence and validity/disposition fields in [docs/review.md](../docs/review.md) within the output above. Optional suggestions are non-blocking. Record the reviewed base/target, mode, prior finding outcomes, and any expanded scope. Missing execution evidence remains unverified. Finish when blockers and applicable gates are addressed and delivery claims agree; do not require zero nits.
