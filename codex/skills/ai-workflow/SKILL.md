---
name: ai-workflow
description: Apply the shared AI Workflow to substantial implementation, multi-file fixes, or high-risk behavior changes, with task records and verification evidence. Also use when the user explicitly requests AI Workflow; keep simple questions and routine checks proportional.
---

# AI Workflow

Use the installed shared Markdown as the canonical process. This is a thin
Codex entrypoint, with no separate copy of the workflow rules.

Follow applicable global, workspace and repository instructions and read their
required references first. Do not assume Claude's imports supplied that context.

Locate the shared workflow checkout using the project instructions; the default
is `~/.ai-workflow`. Use the actual checkout path for every reference below. If
the required checkout is unavailable, resolve its location before dependent work.
Read `workflow.md` and `context-management.md` from that checkout.

Resume the existing ticket and its settled decisions before planning. Let the
canonical workflow determine whether the full Define-to-Ship loop is needed;
keep the user's accepted scope and existing work intact.

Read additional guidance from the checkout only when the task needs it:

- Requirement gaps: `prompts/grill-me.md`.
- Verification contracts: `docs/verification.md`.
- Review and finding disposition: `docs/review.md`.
- Private task records: `docs/local-spec-policy.md`.

Check the repository's task-record policy before writing or staging records.
Preserve local-only records and follow the existing project test commands.
Use the canonical prompts and templates on demand rather than copying them
into project rules or treating Claude slash commands as Codex commands.

Close the loop with evidence for the actual revision and environment. Keep
implemented, verified, merged and deployed states distinct. This skill grants
no additional authorization for external writes, merges, deployment or agents.
