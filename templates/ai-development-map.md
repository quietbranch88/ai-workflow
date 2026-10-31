# <ticket> AI development map

This is the ticket handoff entry point, not a second spec or evidence log.
Keep the snapshot below current and link to canonical sections for details.
When copying this template, record the workflow source root (repository URL or
installed directory) and resolve its guidance links from that root, not from the
ticket directory. The relative links below work only in this source template.
Mandatory global, workspace and repository instructions still load first.

## Resume snapshot

Keep this block short and current; link to detailed records below.

- Repository / branch / revision:
- Current goal and next action:
- Last verified at / environment / evidence:
- Open findings, blockers and unverified boundaries:
- Recheck before relying on: <mutable fact, source and trigger; e.g. remote head before opening a PR>

### Pending operation (only when applicable)

Follow [Resume pending operations](../context-management.md#resume-pending-operations).
Repeat the fields below only for distinct pending operations.

- Target / operation identity / scope:
- Authorization evidence reference:
- Attempt / known returned ID:
- State: not-attempted | confirmed | unknown; observed outcome and evidence:
- Next readback / reconciliation step before retry or redispatch:

## Read order and canonical records

1. `current.md`: goal, scope/non-goals, acceptance criteria and required boundaries.
2. Every settled ticket ADR and latest project devlog, as required by the workflow.
3. `tasks.md`: next work, implementation/caller/test locations, verification commands,
   blockers and the task's implementation choices.
4. Relevant live findings and evidence in `audit.md`, plus linked prior decisions,
   rejected findings and counterevidence affecting this work. Follow those links
   before repeating or reopening a finding; do not erase historical evidence.
5. Relevant deferred/subtask records, only when the next action depends on them.

Replace these names with section links when needed. Keep required records; do not
copy their scope, command lists, blockers or results here. If a source changes,
refresh its pointer and the short snapshot. Preserve settled decisions and retain
reasons/evidence when updating state. Missing required context blocks dependent work.

## Task-specific pointers

- Acceptance / scope / non-goals: `current.md` section
- Implementation / callers / tests / next action: `tasks.md` section
- Verification evidence / unverified gates / blockers: `audit.md` and `tasks.md` sections
- Prior decisions / counterevidence: relevant ADR or `audit.md` finding IDs
- Pitfall capture: task-local note or evidence pointer; record whether capture was
  proposed/approved, status and destination under the existing approval rule.

Verification follows [docs/verification.md](../docs/verification.md) and repository
contracts: preserve independent oracles, applicable defect-detection evidence,
revision/environment, real boundaries, substitutions and missing gates in the audit.
Behavior-neutral changes use direct checks, without artificial failing tests.

## Human and AI roles

Record human decisions and the AI's implementation, investigation, documentation or
verification role separately from earlier human work. Link to decisions/evidence;
keep implemented, verified, merged and deployed states separate. Follow publication
policy and preserve unrelated work; never stage private inventories or local caches.
