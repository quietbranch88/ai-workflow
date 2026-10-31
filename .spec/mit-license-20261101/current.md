# MIT license 2026-11-01

## Goal

Make the public AI Workflow repository explicitly reusable under the MIT
License instead of leaving its reuse terms unspecified.

## Acceptance criteria

- [x] Observable: the repository root contains the standard MIT License text
  and identifies `quietbranch88` as the 2026 copyright holder.
  - Environment: this repository on the documentation-only feature branch.
  - Verify: `python3 -c "from pathlib import Path; text=Path('LICENSE').read_text(); assert text.startswith('MIT License'); assert 'Copyright (c) 2026 quietbranch88' in text"`
- [x] Observable: task records and project living documents identify the
  license decision and contain no unfinished checklist item for this task.
  - Environment: this repository with `origin/main` as the comparison base.
  - Verify: `python3 scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base origin/main --head HEAD`

## Non-goals

No workflow rule, tool adapter, dependency, runtime, installation, deployment,
or historical release changes in this task.
