# Audit

## What changed

`.github/workflows/validate.yml` runs on a pull request and on a push to `main`.
A push compares `github.event.before` with `github.sha`. A pull request still
compares the pull-request base and head. `README.md` says so. `workflow.md`
stays at 280 lines.

## Original goal and what was compared

The goal was to make a push to the default branch run the same checks as a
pull request.

What this run exercised:

- `python3 -m unittest discover -s tests -q`: 81 tests, OK, 3 skipped because
  `pwsh` and `pre-commit` are not on PATH. `tests.test_ci_workflow_contract`
  reads the workflow file.
- `git diff --check`: pass.
- `workflow.md` line count: 280.
- Ship-mode validation of `3055057` against `origin/main`: pass, 0 warnings.
  `check_close_the_loop.py` on that range: pass.

That comparison checks the workflow text. It does not push to `main`, and it
does not prove GitHub has already run the new job.

## This environment's install

The previous install was plugin 0.6.11 at `ecef65d`. It was compared with
`origin/main` `1e150ec`. Every differing file matched the old snapshot, so
there was no private overlay. The install root `/home/ubuntu/.ai-workflow` now
matches that revision, plugin 0.6.12, 148 copied paths, no removals. The
content hash recomputed from the installed bytes is
`464ecdf3f89061b9817942d57b78f7c9f405a069079a244eb6328cc329505ab7`.
The receipt is `/home/ubuntu/.local/share/ai-workflow/install-receipt.json`.

Claude CLI 2.1.210 is installed for this user. Strict validation passed for
the marketplace root and `claude-code/plugin`. `ai-workflow@quietbranch88`
version 0.6.12 is enabled at user scope, from the local install path.

## Not claimed

- The user's computer was not updated. The open install todos stay open for
  that computer.
- Empty acceptance fields still warn. A filled label is still not a check that
  the original goal was met.
- Branch protection was not changed. Until this workflow is on `main`, a
  required check cannot be added for it.
- This record does not authorize a merge.
