# Devlog

## 2026-10-19 - review convergence and a bounded reviewer pilot

- Add a three-round reassessment checkpoint without automatic approval or waived gates; retain scoped follow-ups and evidence-based finding disposition.
- Add four minimized historical-defect/clean packets, reference checks and an offline export/adjudicated-scoring CLI. Metrics distinguish misses, false alarms, duplicates and infrastructure failures.
- Synchronize packaged review/verification contracts and plugin 0.6.6.
- Verify all 71 repository tests without skips, scorer mutation detection, strict plugin packaging and a fresh independent review. Four final pilot cases found both known defect classes with no clean-case false alarms; two reference-fixture defects were corrected and retained separately.
- Validation and delivery state: see `.spec/review-convergence-evals-20261019/audit.md`; preparation is separate from publication and installation. No general reviewer-quality improvement is claimed.

## 2026-10-18 - proportional workers and compact handoffs

- **What**: Replace fixed audit fan-out and speed promises with bounded dispatch,
  explicit permissions and recoverable worker state. Keep handoff snapshot and
  pending operations while linking canonical scope, evidence and decisions.
- **Alignment**: Clarify glossary isolation and clarification-skip conditions;
  synchronize canonical workflow mirror and plugin 0.6.5.
- **Evidence**: `.spec/workflow-context-slimming-20261018/audit.md`; documentation
  checks only, with no measured speed or token savings.
- **Review**: Fresh independent Astra review found no actionable defects; all
  65 tests passed without skips and both strict plugin validations passed.
- **Delivery**: Reviewed source `8cc6234` published to GitHub main and read back;
  actual local checkout fast-forwarded and verified separately. Local settings
  and private overlays were preserved. This records source-file installation,
  not a running-session reload or agent-performance improvement.

## 2026-10-18 - acceptance warnings and interrupted operations

- **What**: Warn on missing or empty acceptance field lines, including labels only
  mentioned in prose; preserve warning-only WIP/Ship behavior. Add minimal pending
  operation state and reconciliation guidance to the existing resume handoff.
- **Evidence**: `.spec/workflow-hardening-20261018/audit.md` records original
  baseline and regression fail-to-pass evidence; full checks recorded there.
- **Review**: Fresh independent review found no actionable defects; all 65 tests
  and both strict plugin validations passed. Static/secret scan scope is in the audit.
- **Distribution**: Workflow mirror and plugin 0.6.4 published in `b55fe9d`;
  GitHub main readback verified. Machine installation has its own receipt.

## 2026-10-18 - context-routing source published

- **Delivery**: Zoe authorized publication after a fresh GPT-6 Astra review.
  Source commit `4bbe318` is on GitHub main, confirmed with `git ls-remote`.
- **Review and checks**: No confirmed or deferred findings across the seven
  changed files. The repository suite ran 63 tests, with 62 passing and the
  existing pre-commit-dependent test skipped. Ship validation passed without
  warnings; close-loop and whitespace checks passed.
- **Boundary**: Source publication supersedes the earlier prepared-only state.
  Local installation and loading in another agent session were not performed.
- **Evidence**: `.spec/context-routing-20261018/audit.md`, publication follow-up.

## 2026-10-18 - task context and evidence handoffs

- **What**: Add phase-specific context routing, evidence-based lesson capture and
  a compact resume snapshot to the handoff template. Reuse existing clarification
  and review contracts; mandatory instructions and authorization gates still apply.
- **Why**: Indexes identify documents but do not say when context needs refreshing
  or which facts a resumed task must verify again.
- **Evidence**: `.spec/context-routing-20261018/audit.md`. Prepared locally;
  publication and installation are separate, unperformed actions.

## 2026-10-15 - routing gate for the full loop

- **What**: Add a "When to use the full loop" section to `workflow.md` and the
  Claude mirror: substantial multi-file, cross-repository, or high-risk work uses
  all six stages; questions, read-only audits, routine test runs, and small fixes
  skip it; an audit that confirms a high-risk defect to fix enters at Define.
  Trimmed three restated lines to stay within the 280-line contract. Plugin 0.6.3.
- **Why**: The boundary lived only in tool adapters and personal rules, so an
  audit that turned into an auth fix had no canonical instruction to switch loops.
- **Evidence**: `.spec/routing-gate-20261015/audit.md`. Prepared on a branch;
  merge remains Zoe's explicit decision.

## 2026-10-04 - concise first-reader README

- **What**: Place the background story first, as Zoe requested, followed by three
  setup steps and a concrete synthetic-data task example. Fold optional tooling and model guidance,
  and keep required setup, privacy, verification and approval boundaries visible.
- **Evidence**: `.spec/workflow-readability/audit.md`, concise onboarding follow-up.
- **Dated correction**: PR #23 merged as `e996b12`; the earlier preparation state
  below is superseded. This README revision is a separate, unmerged change.

## 2026-10-04 - personal-project approval clarification

- **What**: Correct the template's claim that destructive-operation approval is
  the only safeguard personal projects need. Both project types retain the
  canonical workflow approval gates; unused local constraints may be removed.
- **Evidence**: `.spec/workflow-readability/audit.md`, WD-01 follow-up.
- **Dated correction**: PR #22 is merged as `9034daa`; its earlier preparation
  status below is superseded. This wording follow-up is a separate local change.

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
