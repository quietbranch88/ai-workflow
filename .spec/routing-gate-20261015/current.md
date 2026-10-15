# Routing gate for the six-stage loop

## Goal

State in the canonical workflow when the full Define → Ship loop applies and
when a task skips it, so adapters and agents stop inferring the boundary from
the stage list. Include the case where a read-only audit turns into a fix.

## Acceptance criteria

- [x] Observable: `workflow.md` has a "When to use the full loop" section before
  Stages that names the qualifying work (substantial multi-file, cross-repository,
  high-risk behavior), the work that skips it, and the audit-to-fix entry point.
  - Environment: canonical Markdown in this repository.
  - Verify: direct claim review of the section; `python -m pytest -q tests`.
- [x] Observable: the packaged Claude mirror carries the same section and the plugin
  version moves from 0.6.2 to 0.6.3.
  - Environment: `claude-code/plugin/`.
  - Verify: diff review of the mirror; JSON parse of `plugin.json`.
- [x] Observable: `workflow.md` stays within the 280-line contract with no rule lost;
  trimmed lines were restatements (PHILOSOPHY cross-reference, templates path,
  duplicate escalation sentence).
  - Environment: this repository.
  - Verify: `tests/test_docs_contracts.py` line cap; `git diff --check`.

## Non-goals

- Change the stages, approval gates, or any validator behavior.
- Update local installations or merge without the owner's explicit approval.
