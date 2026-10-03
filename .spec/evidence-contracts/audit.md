# Evidence contract audit

## Baseline

- Reviewed source: 58fd6f89d973f52f6f21577ef2dff087239e3fac.
- `python -m unittest discover -s tests -v`: 44 tests passed on Windows before edits.
- Accepted requirements are recorded in current.md. This is a personal repository;
  its shareable task records remain tracked. Local-only support is opt-in for adopters.
- No external service/runtime path changes; real Git fixtures are the affected boundary.

## Verification and findings

### Executed locally, 2026-10-03

- New acceptance tests before implementation: 10 ran, 8 failed. Several validator
  failures were unsupported CLI arguments, not a meaningful behavioral red state;
  the hook's missing-record case did show the wrong successful return. Do not infer
  complete red/green evidence from that run.
- After implementation: 54 tests passed, including actual disposable Git repositories,
  private index rejection, add-then-remove outgoing history and structural validation.
- Controlled mutation in an isolated copy bypassed local-record validation while
  leaving the test unchanged. `test_incomplete_records_fail_ship_but_pass_wip` failed
  at its expected rejection assertion (actual: successful return). Restoring the
  production behavior made the same test pass. The deliverable was never mutated.
- Both `claude plugin validate --strict .` and `claude plugin validate --strict
  claude-code/plugin` passed with CLI 2.1.210. These validate packaging, not agent behavior.
- `ruff check scripts/validate_workflow_docs.py scripts/check_close_the_loop.py
  tests/test_local_spec_policy.py` passed. `git diff --check` passed.
- 39 changed-file relative Markdown links resolved. GitHub Markdown API rendered
  README successfully with expected sections and new contract links present.
- About description was updated and read back through GitHub CLI. This is metadata
  publication only; the feature branch is not merged or installed.

### Scanner disposition

`uv tool run bandit -q scripts/validate_workflow_docs.py scripts/check_close_the_loop.py`
reported 8 low-severity warnings (B404, B603, B607), zero medium/high; exit 1.
This is not reported as a clean scan.

- SCAN-01: B404/B603; validity false-positive, disposition dismissed for command
  injection. Locations: subprocess import/calls in both scripts. Counterevidence:
  calls use argument arrays without a shell; new commands/subcommands and pathspec
  are fixed, root is a distinct argument, ticket is not passed to Git. Existing
  refs come from the local hook context. No demonstrated injection path.
- SCAN-02: B607; validity false-positive, disposition dismissed as a new vulnerability
  in this patch. Calls intentionally use the developer-installed Git, as before;
  this local tool assumes a trusted executable PATH. No elevated or remote service
  execution is introduced. A hostile machine/PATH is outside this tool's boundary.
- Dependency inventory: changed Python tools use only the standard library;
  pyproject.toml declares no packages, and no dependencies were added/upgraded.
  No repository dependency-advisory configuration exists; no package advisory scan
  result is claimed. Secret scan and fresh review results are recorded below when run.

### Initial independent review: df79463

Base 58fd6f8; reviewer checked the complete diff and relevant callers/guards and
independently ran 58 tests. Two findings were adopted after source/caller checks:

- **EC-01, P1, confirmed / open pending follow-up.** At
  `scripts/check_close_the_loop.py:98-103` in df79463, local-only checked one
  PRE_COMMIT range while `docs/local-spec-policy.md:31-34` promised every outgoing
  commit. pre-commit 3.7.1 returns on the first eligible stdin ref. A clean first
  branch plus a second branch with added-then-removed `.spec` history could publish
  private records. Reviewer reproduced a successful two-ref push to a disposable
  local bare remote and read the private historical tree there. Single-ref tests
  were counterevidence only for single-ref scope. Required: inspect the whole native
  ref list and reject the push before any remote ref changes.
  Fix candidate: require native local-only hook input; inspect all ref updates and
  use fresh advertised remote tips for new refs; reject the incomplete pre-commit
  adapter. Positive and negative real-hook tests check durable remote refs.
  An isolated mutation that changed iteration to `updates[:1]` made
  `test_native_hook_rejects_private_history_in_second_ref` fail at the rejection
  assertion: both refs were actually pushed to the synthetic remote. Restoring the
  loop made the unchanged test pass. This independently confirms detection.
- **EC-02, P2, confirmed / open pending follow-up.** At packaged reviewer lines
  43-45 and builder line 15 in df79463, bare source-relative references required
  contracts outside marketplace source `claude-code/plugin`. Standalone packaged
  roles could not locate them. Source/manifest/inventory inspection confirmed the
  omission; no agent-runtime failure was claimed. The six-stage skill's links were
  counterevidence for coordinated use only. Fix candidate: embed canonical review
  and verification contracts in the relevant agents and assert content consistency.

### Updated verification after review fixes

- `python -m unittest discover -s tests -p test_local_spec_policy.py -v`: 16 passed.
  Includes an actual installed native hook and real pushes to local bare remotes,
  both clean multi-ref success and rejected second-ref private history. No live
  service, credentials, user data or production mutation was involved.
- Ruff and packaged-plugin strict validation passed after these fixes.
- The earlier 58-test run and single-ref evidence remain historical. Final complete
  suite, scanner and follow-up review results are recorded separately below.

### Limits

- Tests invoke the actual Python CLI/native hook and perform real Git pushes to
  synthetic local bare remotes, not a hosted remote. They prove local checks,
  not server-side enforcement. Earlier pre-commit-only scope was superseded by EC-01.
- Markdown rules are intent. No agent-quality benchmark or production E2E is claimed.
- The installed local workflow remains unchanged. No private/company overlays copied.

### Follow-up and final local verification: 4aa40a2

- Fresh follow-up reviewed df79463 -> 4aa40a2 against the same acceptance contract.
  No new blockers. EC-01 and EC-02 are now **confirmed / fixed**, fix revision
  4aa40a234b222d02a40d44d671dfa24d206763fd. The earlier open entries are retained
  as history; the reason for closure is inspected fixes plus the evidence below.
- Reviewer independently ran 16 local-policy tests and 19 documentation contracts;
  all passed, including positive/negative actual native-hook pushes and in-package
  contract consistency. `git diff --check` passed. No agent-quality evaluation claimed.
- Coordinator's final runtime/test revision: 4aa40a2. Complete suite: **62 tests
  passed** on Windows, Python 3.11.9, Git 2.49.0.windows.1. Both controlled mutations
  failed the intended assertions and passed after restoration in isolated copies.
- Ruff passed on changed scripts/tests; staged Gitleaks passed after the fixes.
  Final Bandit output still has the same eight low warnings and zero medium/high;
  SCAN-01/02 dispositions remain applicable. No security warning was suppressed.
- Packaged strict validation passed again after embedding the contracts; marketplace
  metadata is unchanged from its passing strict run. CLI version: 2.1.210.
- Final 39 relative Markdown links resolved; GitHub Markdown API rendering passed.
  Default tracked WIP check passed with zero warnings.
- Implemented and locally verified; not merged, deployed or installed. This source
  snapshot records pre-publication evidence. Hosted checks and PR publication are
  separate observations recorded in the PR, rather than inferred from local results.
