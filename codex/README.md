# Use AI Workflow with Codex

Codex uses the shared Markdown workflow in this repository. This directory is
its setup entry point; it does not contain a separate set of rules or an installer.

## Set up a project

1. Follow the root [Quick start](../README.md#quick-start) to clone the shared
   files and merge [the project-instruction template](../templates/AGENTS.md.template)
   into your target project's `AGENTS.md`. Preserve existing project rules.
2. Fill in the project type, task-record policy, project context and real test
   commands. The template still needs those project-specific values.
3. Open **the target project** in Codex. Start a new task after configuring its
   `AGENTS.md`, then send the instruction below with the work you want done.

```text
Read AGENTS.md and ~/.ai-workflow/workflow.md, then follow the six-stage
workflow for this task. Do not claim completion without verification evidence.
```

If you cloned to another location, use that actual path in the project instructions
and prompt. The shared files must be accessible in the environment where Codex runs;
a local clone is not automatically available in a separate cloud environment.

## What Codex reads

- Your project's `AGENTS.md`: project rules and commands.
- [`workflow.md`](../workflow.md): the shared Define-to-Ship process.
- [`prompts/`](../prompts): reusable task instructions; ask Codex to read the
  relevant file when needed.
- [`docs/`](../docs): verification and review details referenced by the workflow.
- [`templates/`](../templates): starting points for project and task records.

Codex discovers project `AGENTS.md` instructions as described in the
[official guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Other shared files are supplied by the project instructions or your task prompt;
cloning the repo alone does not register every prompt as a Codex skill.

## Optional helpers

See [Optional setup](../README.md#optional-setup) for Python, PowerShell and
hook prerequisites. The default task bootstrap prints a prompt that you can paste
into Codex. Its optional launcher needs your own named Codex profiles.

The `claude-code/` package and `/plugin marketplace` commands are the Claude
adapter. Codex uses the shared sources above without installing that adapter.
