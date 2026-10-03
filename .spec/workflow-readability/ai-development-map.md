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

Zoe requested correction of FR-01 after a fresh reader simulation. The main agent
also makes the discussed original-article language labels explicit. Review checks
the missing-map and existing-map paths without changing map-generation code.
