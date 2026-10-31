# Audit

## What changed

Reviewed copies now follow the canonical rule, and Ship mode still sees an open
item that a fence or an HTML comment would otherwise hide.

- A failing shape or size check is reverted. The ceiling is not raised, and a
  public URL or release-check file is not added to make the check pass.
- The private system map stays on the local machine. The pre-push hook is WIP
  only. Ship mode is `scripts/validate_workflow_docs.py --mode ship`.
- Plugin mirrors for the workflow, builder, pitfalls, grill-me, system map, and
  portfolio scan match the canonical text. Plugin version is 0.6.12.
- `TBD` in a system map is a whole word. A closed fence still hides an example
  checkbox. An unclosed fence, a mismatched closer, or a checkbox inside a
  comment does not.

`workflow.md` stays at 280 lines.

## Original goal and what was compared

The goal was to make the working tree, not `ecef65d`, the text a later agent
follows. `ecef65d` is merged PR #30 at plugin 0.6.11.

What this run exercised:

- Unit tests except four known local timeouts: 77 tests, 0 failures, 1 skipped
  because `pre-commit` is not on PATH. The run included
  `AdapterConsistencyContractTests` and `CanonicalWorkflowContractTests`.
- `git diff --check`: pass.
- Relative links in the 25 changed Markdown files: 40 links, 3 template
  placeholders only (`templates/devlog.md`).
- Ship-mode validation against `origin/main` is recorded with the commit SHA.

That comparison checks the copies and the validator. It does not install the
plugin on this machine or prove a later agent will follow the text.

## Deliberately left

- Four unit tests that time out on this machine: the two `pwsh` task-bootstrap
  tests and the two local-only hook tests. Isolated reruns previously returned
  the expected result. CI still runs the full suite.
- Historical devlog entries. Product-specific provider and screen rules stay in
  the project that owns them.
- Machine installation of 0.6.12 is not part of this record.

## Not claimed

- Claude CLI strict plugin validation did not run here. Hosted pull-request
  validation covers that gate.
