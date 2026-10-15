# Tasks

- [x] task-1: Add the routing section to the canonical workflow and trim restated lines to keep the cap.
  - Files: workflow.md
  - Oracle: acceptance contract in current.md; the 280-line test contract.
  - Verify: `python -m pytest -q tests`; `git diff --check`.
- [x] task-2: Mirror the section in the Claude adapter and bump the plugin version.
  - Files: claude-code/plugin/skills/six-stage-workflow/SKILL.md, claude-code/plugin/.claude-plugin/plugin.json
  - Verify: diff review; JSON parse.
- [x] task-3: Record delivery state.
  - Files: devlog.md, todo.md, .spec/routing-gate-20261015/
  - Verify: `python scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base origin/main --head HEAD`.

## Acceptance

- [x] All acceptance criteria have evidence or explicitly recorded outstanding delivery state.
- [x] Fresh review findings are recorded with dispositions.
- [x] No merge, push, or installation is implied by this record.
