# Audit and verification

Base: 3c507efaa86a33ec9091fd6ecac9a4c40e8a8f05. Initial source audit round 1 already
identified A03-F1/F2/F3, A04-F1, A05-F1 and A06-F1. All six are confirmed/open.
User authorized fixing all six and a fresh review. This record preserves those IDs.

## Patch boundary

Coordinator independently inspected validators, hook callers, planner templates,
bootstrap and tests. Fresh security investigator /root/fix_security_boundary traced
tip/history/advertised-object checks through the shared Git subprocess boundary.
The privacy contract is actual outgoing objects, not replacement trees. All tests
use synthetic isolated repositories; no real private data is transferred.

## Workspace

The desktop create_worktree tool rejected the source repository because it is
outside this chat's registered workspace. Used an independent local clone and
codex/workflow-six-audit-fixes branch instead; the installed checkout remains clean.

## Evidence

Baseline: 81 tests in 60.629s, pass with one missing-pre-commit skip. Added regression
oracles failed against unchanged source: nine tests produced 20 relevant assertion
failures; four replacement-object privacy tests all failed with the expected false
acceptance/rejection. Those failures establish detection for all six finding IDs.

After implementation, the nine focused regression tests passed (10.541s), and all
20 local-only tests passed (13.860s). Assertions cover actual CLI decisions, native
push rejection and unchanged remote refs, plus successful clean-object transfer.
Commit and tree replacements and a hidden private ancestor are exercised; legacy
grafts/shallow-history policy is not expanded or claimed by this fix.

The first complete candidate suite ran 94 tests in 371.134s: two existing bootstrap
tests timed out at 30s; one pre-commit test was skipped. A diagnostic rerun of one
unchanged test passed in 23.213s, which is unstable evidence, not a resolved failure.
The clipboard is not part of those branch/scaffold assertions. Their test fixture
now disables desktop clipboard delivery, matching the new isolated bootstrap
fixtures, while retaining all branch/worktree/file-content assertions and the same
timeout. The two isolated positive controls passed in 35.886s. This does not prove
clipboard delivery caused the timeouts, or verify actual desktop clipboard behavior.
The complete changed-fixture suite subsequently passed: 94 tests in 178.111s,
93 passed and one pre-commit-runner test skipped because the tool is absent.
This is evidence for the declared isolated bootstrap boundary; actual desktop
clipboard delivery stays unverified. No runtime source changed between the two
complete suites; the fixture's substituted clipboard boundary is explicit.

Environment: macOS arm64, Python 3.15.0, Git 2.54.0 (Apple Git-157), PowerShell 7.6.3.
The 3.10 check is syntax parsing, not a Python 3.10 runtime result. Hosted CI has
not run against this local candidate.

All changed Python files parse with Python 3.10 syntax; both manifests parse.
No third-party dependency was added or upgraded. bandit, pip-audit, gitleaks,
detect-secrets, ruff, mypy, pre-commit and Claude CLI are unavailable on this path.
No repository-configured static-security/advisory/secret scanner exists to run;
manual diff review is not described as an automated scan. Claude strict package
validation and pre-commit runner integration remain unverified for this candidate.

Fresh reviewer /root/review_six_fixes is reviewing immutable candidate patch SHA256
35c31189246853cc06e7952b39696482c935441d98fa8f1c822448905e56ddc9, against base
3c507efaa86a33ec9091fd6ecac9a4c40e8a8f05. This is review round 2 including the
original source audit, and the single requested candidate-review cycle. Its packet
excludes author defenses, prior verdicts and the investigator's report. Read-only
is a prompt constraint, not enforced filesystem isolation. No source edits will
occur during that pass. No merge or installation completion is claimed.

## Candidate-review findings and correction

The single fresh review completed. It supported A03-F1, A03-F2, A04-F1 and A05-F1
for the named cases and found two concrete remaining gaps:

- A03-F3-R1, confirmed/open P2 at candidate validate_workflow_docs.py:126/161:
  HTML comments inside closed code fences were globally reintroduced as unfinished
  items. Independent coordinator CLI controls produced two relevant failures.
- A06-F1 remained confirmed/open P2 at candidate start-task.ps1:260-277/319-332:
  missing or stale cached origin/HEAD could hide the actual remote default branch.
  Coordinator fixtures starting on main and targeting advertised default trunk
  produced four relevant failures covering branch/worktree and missing/stale cache.

Coordinator corrected both within the same review cycle. Comment evidence is now
associated with its source line and discarded with closed fenced examples; comments
are literal inside real fences, while unfinished comments outside fences or after
unclosed fences still fail. Both bootstrap paths use one shared-branch resolver.
When origin exists, its advertised symbolic HEAD is authoritative, avoiding stale
cache; an unavailable/ambiguous origin fails before writes. No-origin repositories
keep local behavior. This intentionally means offline configured-origin bootstrap
needs restored remote visibility; cached metadata alone cannot safely establish an
actual default. No origin configuration or cached refs are changed by bootstrap.

The first correction-focused run passed all ten tests in 22.865s. Additional
legitimate feature and unreadable-origin controls are included in final validation.
Reviewer did not rereview the corrected tree; coordinator owns disposition and
post-review verification. No extra automatic review cycle is claimed.

## Final disposition and evidence

Final substantive patch SHA256:
87f51f489b6826e531ffda881134085c956759d68482c5ba3c04e0b71e3b217d.
This identifies source/tests/package/docs independently of these living records.

| ID | Validity | Disposition | Final checked evidence |
| --- | --- | --- | --- |
| A03-F1 | confirmed | fixed | GitSnapshotTests: dirty correction/placeholder, absent working directory and project-marker controls |
| A03-F2 | confirmed | fixed | Actual Ship/WIP Unicode and quoted filename round trips |
| A03-F3 | confirmed | fixed | Dash, asterisk, plus and ordered unfinished tasks reject Ship and remain valid WIP |
| A03-F3-R1 | confirmed | fixed | Closed fenced HTML-comment examples pass; outside/unclosed hidden unfinished tasks fail |
| A04-F1 | confirmed | fixed | Real native push rejects original private tip/tree/ancestor objects; refs unchanged; clean raw history succeeds |
| A05-F1 | confirmed | fixed | Filled packaged planner examples pass real WIP parsing with zero warnings |
| A06-F1 | confirmed | fixed | Shared/cached/uncached/stale-default branch/worktree destinations reject before writes; ordinary feature controls pass; unavailable origin leaves main untouched |

Final command: `python3 -B -m unittest discover -s tests -v`.
Result: 95 discovered, 94 passed, one unavailable-pre-commit skip, 69.222s.
No runtime code changed after this run. README received a factual failure-behavior
note; its headings/public structure were preserved and the statement was checked
against the shared resolver and unavailable-origin control. `git diff --check` and
Python 3.10 syntax parsing passed. WIP/Ship working-file and final commit gates are
run as the final delivery check; the external validation receipt records their
actual result at the local commit.

Retained red-state, failed/diagnostic, successful suite and immutable patch artifacts
are in the standalone codex-security artifact collection for this target; no logs
or local inventories are committed. Earlier failed runs are preserved rather than
superseded as if they had passed. This record does not establish desktop clipboard
reliability, a real plugin installation, hosted CI for this commit, or actual agent
adherence. Unavailable tools and substituted clipboard boundary remain explicit.

Delivery: implemented and locally verified in an isolated feature branch; not
merged, externally pushed, deployed or copied over the active workflow installation.
