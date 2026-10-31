# Audit

## What changed

Accidental full restatements now point at the canonical copy.

- Review prompts keep the fill-in fields, output skeleton, and mode names. An
  initial review still omits the authoring transcript and the author's defense.
  Mode scope, partial review, stop conditions, and the three-round checkpoint
  point at `docs/review.md`.
- `claude-code/CLAUDE.md.example` points shared-database migrations, destructive
  operations, and authoring versus an isolated test database at `workflow.md`
  Approval gates, and points irreversible behavior and an E2E waiver at
  `docs/verification.md`. Example-only approval and worktree text stays.
- The packaged grill-me skill body follows `prompts/grill-me.md`, including the
  dimension list, the rules, and the skip guard. Frontmatter and the Canonical
  source header stay. Plugin version is 0.6.11.
- The 280-line cap remains in the core-workflow contract test only.
- Public entries and the parallel-audit recipe keep their scar stories,
  commands, worker ids, budgets, ownership, and the 200-word report limit.
  Duplicated policy sentences point at `workflow.md`, `docs/verification.md`,
  or `context-management.md`.
- The handoff template keeps its blank pending-operation fields and points at
  Resume pending operations.

`workflow.md` is unchanged at 280 lines.

## Original goal and what was compared

The goal was to remove accidental full restatements while keeping required
mirrors.

What this run exercised:

- `python3 -m unittest discover -s tests -q`: 76 tests, OK, 3 skipped because
  `pwsh` and `pre-commit` are not on PATH. The tests read the canonical files
  and the packaged mirrors. They check the grill-me dimensions and rules, that
  the old grill-me process headings are gone, that the plugin version is at
  least 0.6.11, and that `workflow.md` is at most 280 lines in the core-workflow
  test only.
- `git diff --check`: pass.
- Relative links in the 14 changed Markdown files resolve, including the new
  heading anchors: pass, 61 links. `CLAUDE.md.example` uses install paths, not
  repo-relative links.
- The README rendered through GitHub's Markdown API.
- Ship-mode validation of commit `943737d` against `origin/main`: pass, 0
  warnings. `python3 scripts/check_close_the_loop.py` on that range: pass.

That comparison matches the goal of shortening the duplicate copies. It does
not open a browser, run a product flow, or compare a user-visible result with
an acceptance case. A pointer being present does not show that a later agent
will follow it.

## Deliberately left

- Required mirrors: `claude-code/plugin/skills/six-stage-workflow/SKILL.md`,
  `claude-code/plugin/skills/verify-done/SKILL.md`, the builder embedding of
  `docs/verification.md` and `docs/review.md`, and the reviewer embedding of
  `docs/review.md`. Python and Go pitfall skills were not edited.
- `portfolio-scan` and `build-system-map` stay paraphrases.
- The user-visible-check rules stay separate from the original-goal evidence
  rule. Migration authorization in `workflow.md` stays separate from migration
  classification and dry-run in `docs/verification.md`.
- `PHILOSOPHY.md` stays. Each section is the principle, not a second copy of
  the Define or Verify procedure.
- The README model-choice note already links to model routing. Gotcha entries
  that already linked, including the end-to-end scar, stay.
- Historical devlog entries and older `.spec` tickets stay. The ship validator
  was not changed. Empty acceptance fields remain warnings; these criteria are
  filled.
- No Playwright mandate, mutation score, or measured speed claim.

## Not claimed

- Claude CLI is not installed here, so strict plugin validation did not run.
  Hosted pull-request validation covers that gate.
- Machine installation and merge are not part of this record. This audit does
  not authorize a merge.
