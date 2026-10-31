---
name: portfolio-scan
description: Use monthly, before starting a new project, or when the user asks "what should I work on" / "what are all my projects doing". Scans the user's own GitHub repos via gh CLI and regenerates a portfolio.md status table.
---

<!-- Canonical source: ~/.ai-workflow/prompts/portfolio-scan.md. Compare this copy
     with that file and record the installed revision. A local file does not
     replace this copy only because it might be newer. Keep a private overlay separate. -->

Produces or refreshes `~/.ai-workflow/portfolio.md` from `templates/portfolio.md`. The repo list comes from whoever is logged into `gh` on this
machine; nothing is hardcoded.

## Procedure

1. **List everything (cheap, one call):**

   ```bash
   gh repo list "$(gh api user --jq .login)" --limit 200 \
     --json name,description,pushedAt,isArchived,primaryLanguage \
     --jq 'sort_by(.pushedAt) | reverse'
   ```

2. **Bucket by recency BEFORE reading anything:**
   - pushed < 30 days → candidate `active`
   - 30–180 days → candidate `maintenance` / `paused`
   - > 180 days, not archived → candidate `archive-candidate`
   - `isArchived` → drop from the table

3. **Deep-read ONLY the active bucket** (metadata suffices for the rest): README first
   paragraph → "what it does"; last 5 commit subjects + open PR titles → "current focus";
   if the repo follows this workflow, devlog.md / todo.md top entries → "next milestone". For many repos, fan out
   parallel read-only agents, one per repo, < 100 words each.

4. **Diff against the existing portfolio.md** before overwriting: report rows added,
   removed, and status changes. Status downgrades (active → paused, anything →
   archive-candidate) are DECISIONS — surface them, let the human confirm, log confirmed
   ones under "Decisions from recent scans".

5. Write the file with this skeleton, stamp the scan date:

   ```markdown
   # Portfolio — what every project is doing
   > Last scan: <date>

   | Repo | What it does (one line) | Status | Current focus | Next milestone | Last push |

   ## Paused projects — wake-up conditions
   ## Decisions from recent scans (newest on top)
   ```

## Rules

- Metadata first. Reading every repo's code on every scan is how the scan stops happening.
- Status vocabulary from `templates/portfolio.md`: `active` is being worked on this month; `maintenance` is no new features planned, fixes only; `paused` is intentionally parked and must have a wake-up condition; `archive-candidate` is no push in 180+ days and no wake-up condition, flagged for the human.
- A `paused` row without a wake-up condition is a lie — write the condition or call it
  `archive-candidate`.
- The scan flags archive candidates; it NEVER archives. Archiving is a human decision.
- Portfolio rows are generated. Rerun the scan instead of hand-editing them.
  A curated map is compared with a dry run and is not overwritten.
