# AI development map

## Human intent

On 2026-10-04 Zoe requested correction of the workflow design/readability review
and allowed links to her blog articles. Prior merge approval applied to PR #20.

## AI roles

- Main agent: inspect current sources, verify blog destinations, edit documentation
  and metadata, run checks and reconcile delivery evidence.
- Independent reviewer: inspect the final patch and prior finding dispositions.

## Boundaries

This is documentation and plugin metadata work. No validator logic or tests change.
The Kafka incident is the author's published account, not an incident reproduced
in this task. No agent performance or human usability improvement is measured.

## First-reader follow-up (2026-10-04)

Zoe requested correction of FR-01 after a fresh reader simulation, then specified
English-only article links and asked whether the downloadable code works with
Codex. The main agent checked a fresh remote clone, real hook invocation and
official AGENTS guidance. Review covers missing/existing maps and the hook launch
fix; no model-performance or automatic profile installation is claimed.

Zoe then identified the Claude-only directory naming as misleading and explicitly
authorized merge of the current work. Add a Codex guide pointing to shared sources,
validate it, and merge PR #22 only after checks pass at the final head.
