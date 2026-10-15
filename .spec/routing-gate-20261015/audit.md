# Audit

Branch `routing-gate-20261015` from main `b2e5d66`, isolated worktree.
Documentation and adapter metadata only; no validator or script behavior changed.

## Background

Two stale local copies of this repository were compared with main on
2026-10-15. Everything in them was already on main except a routing gate; that
is the only content carried here. Installation state is kept in local records.

## Verification (2026-10-15, before commit)

- `python -m pytest -q tests` → 63 passed, 23 subtests (one mirror-equality
  failure during work, fixed by applying the same trims to the mirror).
- `git diff --check` → clean. `workflow.md` → 280 lines (cap 280).
- `plugin.json` parses; version 0.6.3.
- `python scripts/validate_workflow_docs.py --root . --mode wip --project-type personal --changed-file …` over all changed files → pass, 0 warnings.
- Relative links in changed Markdown → 0 broken.
- Not run: GitHub Markdown render (README unchanged); hosted CI (runs on push).

## Review (fresh context, initial mode, 2026-10-15)

No blocker or major. Reviewer confirmed the three trims lose no rule that is
not stated elsewhere (PHILOSOPHY cross-reference was itself inaccurate; the
escalation rule survives in the model-routing section; the install path remains
in README). Pytest 63 passed, `git diff --check` clean, mirror equal, 280/280.

| ID | Sev | Finding | Validity / disposition |
| --- | --- | --- | --- |
| F1 | minor | "small fixes skip it" vs the high-risk list: precedence unstated | confirmed / fixed — "risk wins over size" |
| F2 | minor | "skip it" readable as skipping record checks that Ship still requires | confirmed / fixed — "skip the stages, not the record checks" |
| F3 | minor | Machine-local installation state in public todo.md and this audit | confirmed / fixed — removed; kept in local records |
| F4 | minor | Ship validator failed on one unchecked task item | confirmed / fixed — review recorded, item checked |
| F5 | info | Model name in ai-development-map unverifiable by reviewer | confirmed correct by the session; no change |
| nit | — | "Keep this file focused on the execution loop" editor hint dropped; plugin mirror's `templates/` is unresolvable inside the plugin (pre-existing) | dismissed — editor hint, not a rule; pre-existing |

Post-fix verification (2026-10-15): pytest 63 passed / 23 subtests;
`git diff --check` clean; `workflow.md` 280/280; mirror equality test passed;
`validate_workflow_docs.py --mode ship --project-type personal` over the changed
files → pass, 0 warnings; privacy grep over changed files → no machine paths or
company identifiers. The same Ship validation is rerun against the commit range
after commit; hosted CI runs on push. Merge remains the owner's decision.
