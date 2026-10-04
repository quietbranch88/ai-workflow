# Devlog

## 2026-10-04 — first-reader onboarding follow-up

- **What**: Clarify how cross-repo work starts without an optional system map,
  preserve read/update duties for existing maps, and retain English-only article
  links. Document Codex setup and optional tool requirements. Fix the pre-push
  template's literal-home-path failure; synchronize the Claude mirror at 0.6.2.
- **Codex entry**: Add `codex/README.md` and visible root links so the directory
  listing no longer suggests Claude-only support; keep all process rules shared.
- **Evidence**: `.spec/workflow-readability/audit.md`, finding FR-01 and follow-up checks.
- **Dated correction**: The readability update below merged in PR #21 as `da4014b`.
  Its earlier unmerged status is superseded; this follow-up remains a separate change.

## 2026-10-04 — workflow readability and consistent adoption guidance

- **What**: Add a six-stage Mermaid loop, plain-language descriptions, complete
  template setup steps and links to the owner's original and later Kafka articles.
  Clarify tracked Ship requirements and reserve ADRs for architecture tradeoffs.
  Synchronize the Claude adapter at 0.6.1; validator behavior is unchanged.
- **Evidence**: `.spec/workflow-readability/audit.md` records findings and validation.
- **Dated correction**: PR #20 merged as `442a7f9` on 2026-10-03. The previous
  entry's feature-branch status is superseded for remote delivery; it remains no
  evidence of local installation. This follow-up is not yet merged.

## 2026-10-03 — evidence contracts and private task records

- **What**: Synchronize independent acceptance oracles, defect-detection and real-boundary
  verification, scoped review with finding decisions, and proportional architecture.
  Add opt-in local-only record validation and synchronize the Claude adapter at 0.6.0.
- **Why**: Portable templates still required test-first behavior and stopped review at
  the first blocker; tracked-document guards could not support private task records.
- **Evidence**: `.spec/evidence-contracts/audit.md`; real disposable Git fixtures,
  controlled mutation, repository contracts, strict plugin validation and Markdown render.
- **Delivery**: Repository About description updated and read back. Code/docs are on
  a feature branch; merge and local installation are separate, not completed states.
- **Dated correction**: The September 15 entry described preparation at that time.
  Remote main `58fd6f8` now contains those rule-distribution sources. Its publication
  is observed in the current tree; local installation is not established by that fact.

## 2026-09-15 — rule delivery preparation

Align rule distribution, clarification, debugging and private-map handling; retain the current plugin baseline and increment it to 0.5.1. Validation and scope: `.spec/rules-delivery-20260915/audit.md`. Prepared locally; no remote publication.

## 2026-07-15 — workflow-enforcement — make WIP flexible and Ship evidence enforceable

- **What**: Add WIP/Ship living-doc validation, warning-only acceptance-quality
  annotations, a private system-map validator, and read-only PR CI with pinned
  GitHub actions and Claude CLI. Align the canonical docs, optional Claude
  mirror, and the bilingual the portfolio site article.
- **Why**: The old close-loop guard proved only that a living file changed;
  hosted checks, local map claims, and falsifiable acceptance wording were not
  enforced or independently visible.
- **Spec/Plan**: `.spec/workflow-enforcement/current.md`
- **Evidence**: Full Python contracts, two strict Claude validations, local
  private-map validation, GitHub Markdown render, bilingual Node contracts,
  Astro check/build, and desktop/mobile browser QA.
- **Boundary**: GitHub-hosted status appears only after the PR opens; live site
  deployment and branch-protection changes remain outside this task.

## 2026-07-15 — readme-workflow-refresh — make adoption safer and the controls proportional

- **What**: Move a guarded, tool-agnostic Quick start to the top of README;
  align the canonical workflow and Claude mirror around risk-based isolation,
  review, model routing, and approval; harden local task/worktree and pre-push
  guards.
- **Why**: The public page was table-heavy, the generic path was secondary, and
  several written guarantees disagreed with what the local scripts enforced.
- **Spec/Plan**: `.spec/readme-workflow-refresh/current.md`
- **PR**: [#17](https://github.com/quietbranch88/ai-workflow/pull/17)
- **Evidence**: 15 contract/integration tests, PowerShell parse, JSON parse,
  relative-link validation, GitHub Markdown render, and `git diff --check` pass.
- **Notes**: Pilotfish influenced only the attributed, tool-agnostic role
  contract and fresh-verifier ideas. Official Claude Code CLI `2.1.210` strict
  validation passes for both the marketplace and packaged plugin.

## 2026-07-15 — readme-storytelling — make the workflow portable across agents and model tiers

- **What**: Make the canonical workflow usable by any coding agent, move
  Claude Code and Codex into optional adapter guidance, and replace brittle
  provider-version routing with capability- and risk-based routing.
- **Why**: The public README and repository metadata still implied that Claude
  was required, while hard-coded model names and prices had already drifted.
- **Spec/Plan**: `.spec/readme-storytelling/current.md`
- **Commit**: `2a181ae`
- **Continues**: README storytelling work in PR #15
- **Notes**: Strong and weaker models keep the same acceptance criteria and
  evidence gates; task size, autonomy, permissions, and escalation differ.
  At that commit, Claude plugin validation was blocked because the CLI was not
  installed; the later README/workflow refresh completed strict validation.

## 2026-07-15 — readme-storytelling — make the public entry point reflect the author's voice

- **What**: Reframe the README around the failure and evidence loop that
  created the workflow; add dedicated Gotchas and Glossary entry points.
- **Why**: The existing README is complete but reads like a directory manual,
  and the two concepts the author expected are missing as discoverable documents.
- **Spec/Plan**: `.spec/readme-storytelling/current.md`
- **Commits**: `e351bd6`, plus the close-the-loop follow-up in PR #15
- **Continues**: public-profile and repository-brand cleanup from 2026-07-13
- **Notes**: Canonical workflow and pitfall content remains in its existing
  files; the new public docs route to it instead of copying it wholesale. The
  repository About homepage was also updated to `the legacy personal site`.
