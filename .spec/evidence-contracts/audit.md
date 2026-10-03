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

### Limits

- Tests invoke the actual Python CLI against synthetic local Git repositories, not
  a live remote push. They prove local checks, not server-side enforcement.
- Markdown rules are intent. No agent-quality benchmark or production E2E is claimed.
- The installed local workflow remains unchanged. No private/company overlays copied.
