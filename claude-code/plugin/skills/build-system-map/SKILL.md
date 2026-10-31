---
name: build-system-map
description: Use when the user wants a cross-repo system map, or when agents keep re-exploring the same repos every session. Scans locally cloned repos in parallel and builds/refreshes a system-map.md recording structure — entry points, public surfaces, integration edges.
---

<!-- Canonical source: ~/.ai-workflow/prompts/system-map-scan.md. Compare this copy
     with that file and record the installed revision. A local file does not
     replace this copy only because it might be newer. Keep a private overlay separate. -->

The point: pay the cross-repo exploration cost ONCE. Afterwards agents read the map and
verify only what their ticket touches — they do not re-explore N repos every session.

The map records STRUCTURE (what talks to what, where things live), never status, progress,
code, or secrets. It describes the user's own locally cloned repos — ask which repo paths
to scan if not obvious.

## Build procedure (one time, and again after a large architectural change)

1. In ONE message, spawn one read-only Explore agent per repo. Each prompt is
   self-contained, asks for exactly the fields below, under 200 words:

   ```
   Explore <path-to-repo>. Report, under 200 words:
   1. One-line purpose (from README + main entry point)
   2. Stack: language, framework, datastore
   3. Entry points: services/jobs/handlers with file paths
   4. Public surface: REST routes / events published / packages exported — where defined
   5. What it consumes: outbound HTTP clients, topics subscribed, shared libs imported
   6. Whether .spec/, devlog.md, todo.md exist
   7. One or two gotchas a new agent must know before editing
   ```

2. Write `~/.ai-workflow/system-map.md` from `templates/system-map.md`. That path is the only copy. Day-to-day, patch the local file; do not rescan. Repeat this full scan only after a large architectural change. Do not commit the file. Validate with `python scripts/validate_system_map.py --map ~/.ai-workflow/system-map.md`.

3. Integration edges: record an edge ONLY after seeing BOTH sides (the caller's client
   code AND the callee's handler/contract). One-sided claims go to `## Unconfirmed`.

4. Keep each repo section under ~15 lines. This is an orientation cache, not documentation.

## Consume rule (what kills re-querying)

Cross-repo task → read the map FIRST, before any Explore fan-out. Spot-verify only the
entry points and edges the ticket touches: paths still exist, signatures still match.
Do NOT re-explore repos the ticket doesn't touch.

## Patch rule (keeps the cache honest)

If a change adds/removes/renames anything the map records — an entry point, endpoint,
event, integration edge, shared lib — patch the local map. Do not commit the private
map. Note the repair in the repository devlog. Map contradicts reality → the map is
stale: fix the local copy, never silently work around it.

## Privacy

The finished map is an architecture diagram of the user's systems. Keep it on
local disk. Do not commit it, including to a private repository.
