# AI Workflow Repository Rules

**Project type: personal**

This repository is the tool-agnostic source of truth for the repository owner's AI-development
workflow. It contains documentation, reusable prompts, templates, scripts, and
thin Codex and Claude Code adapters; it is not an application runtime.

## Canonical sources

- Follow `docs/rule-distribution.md` when synchronizing shared rules, local installations, or plugin adapters. Preserve private overlays separately and record the installed source revision.

- Process changes belong in `workflow.md`.
- Principle changes belong in `PHILOSOPHY.md`.
- Reusable technical traps belong in `pitfalls/`.
- `README.md`, `GOTCHAS.md`, and `GLOSSARY.md` are public entry points. Keep
  them concise and link to canonical details instead of duplicating them.
- Files under `claude-code/plugin/skills/` that declare a `Canonical source`
  are mirrors. When the canonical source changes, update the mirror and plugin
  version in the same change.

## Workflow

For non-trivial work, keep acceptance, audit, and handoff state in
`.spec/<ticket>/`. Personal-project living documents, including `devlog.md`
and `todo.md`, follow [Close the loop](workflow.md#close-the-loop-before-opening-a-pr).

## Verification

Follow [Close the loop](workflow.md#close-the-loop-before-opening-a-pr). Run:

- `git diff --check`
- `python scripts/check_close_the_loop.py` for the WIP pre-push guard. It does
  not run Ship mode.
- Ship mode, before a pull request:
  `python scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base "$BASE_SHA" --head "$HEAD_SHA"`
- Validate changed Markdown links and render the README through GitHub's
  Markdown API before changing its public structure.

Do not commit credentials, local repository inventories, private project data,
or generated personal maps.
