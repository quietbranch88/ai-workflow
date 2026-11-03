# Proportional request-card intake

## Goal

Adapt the CabLate pre-action request-card idea into this workflow so agents align
consequentially ambiguous work before editing without adding a confirmation round
to every clear, reversible task.

## Scope

### In

- Add proportional direct-execution versus compact-card routing to `workflow.md`.
- Align `prompts/grill-me.md`, required Claude skill mirrors, contract tests and
  the plugin version.
- Attribute the public source article and retain the existing authorization gates.

### Out

- No change to the read-only AI workflow feed MCP server or its source catalog.
- No automatic hook that blocks every new prompt.
- No merge, release, plugin installation or external publication in this task.

## Acceptance criteria

- [x] Observable: clear, bounded and reversible requests are explicitly routed to direct execution without a request card.
  - Environment: local repository checkout on branch `docs/proportional-request-card-20261103`.
  - Verify: `PYTHONPATH=tests python3 -m unittest test_docs_contracts.CanonicalWorkflowContractTests.test_task_alignment_is_proportional_and_decision_bounded -v`
  - Oracle: Zoe's request to optimize the workflow without adding unnecessary friction, plus the existing proportional-controls principle.
  - Required boundary: canonical workflow text through its contract test.

- [x] Observable: consequential ambiguity or plan-first work produces a one-screen six-field card with no more than two user decisions.
  - Environment: local repository checkout.
  - Verify: the targeted contract test above and direct diff review of `workflow.md` and `prompts/grill-me.md`.
  - Oracle: the user-supplied CabLate article, adapted to existing authorization and autonomy rules.
  - Required boundary: canonical workflow and reusable clarification prompt.

- [x] Observable: canonical content and Claude mirrors remain byte-equivalent after link normalization, and plugin version is at least 0.6.16.
  - Environment: local repository checkout.
  - Verify: `PYTHONPATH=tests python3 -m unittest test_docs_contracts.AdapterConsistencyContractTests.test_evidence_skill_mirrors_match_canonical_content -v`
  - Oracle: `AGENTS.md` canonical-source and mirror rule.
  - Required boundary: canonical Markdown, packaged skill mirror and plugin manifest.

## Non-goals

- Requiring the literal reply `start` before all work.
- Replacing explicit approval gates with the request card.
- Claiming that MCP directory metadata is the full article; the original article
  remains the content source.

## Risks

- Too many cards slow routine work -> direct-execution route and consequential-gap trigger.
- Agent assumptions hide decisions -> dedicated assumptions and user-decisions fields.
- Canonical and packaged text drift -> exact mirror contract test.

