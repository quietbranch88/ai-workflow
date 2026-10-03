# Workflow readability audit

## Scope and baseline

2026-10-04: main `442a7f9737d6fba9396be1a857bf2a4f525e7e97`, isolated clean branch.
Documentation review only; source traces do not establish measured usability.

## Findings carried forward

All four were confirmed/open against the baseline. Fixes below await validation.

- **WF-D01 / medium / confirmed / open**: `workflow.md:104-105` promised no
  synthetic history for trivial docs, while `scripts/validate_workflow_docs.py:208-236`
  and `.github/workflows/validate.yml` require records for every non-living path in
  tracked Ship mode. A README typo triggers the mismatch. Counterevidence: the
  strict rule was already documented elsewhere. Resolution: remove the exemption
  promise and state the precise limitation in workflow, template and README;
  preserve existing checks. Source inspection, not a new runtime reproduction.
- **WF-D02 / medium / confirmed / open**: `README.md:24-58` omitted target-project
  navigation and mandatory template setup; `templates/AGENTS.md.template:8,91-93`
  retains placeholders. New adopters could follow all steps with incomplete rules.
  Counterevidence: the template says to set one project type. Resolution: explicit
  configuration step and separation of optional local checks from this repo's CI.
- **WF-D03 / low / confirmed / open**: `workflow.md:64-65` and template `:50`
  sent all implementation-only decisions to ADRs, conflicting with architecture-only
  guidance. Routine choices could create needless documents. Counterevidence:
  template task-file guidance already limits ADRs to architecture. Resolution:
  task/handoff for ordinary choices, ADR for architecture tradeoffs; remove the
  contradictory commit-to-PR-to-ADR sequence. This is wording ambiguity, not
  observed excessive documentation by users.
- **WF-D04 / low / confirmed / open**: `README.md:195-201` contained an incomplete
  sentence and no destination for further reading. Resolution: verified article
  links and a Zoe Builds homepage link replace the fragment.

## Supporting evidence

- GitHub profile's blog field points to https://zoe-builds.com.
- Read both language versions of the original article (published 2026-07-08):
  https://zoe-builds.com/en/articles/my-ai-workflow/ and
  https://zoe-builds.com/articles/my-ai-workflow/.
- Read the later decision case (published 2026-09-28):
  https://zoe-builds.com/en/articles/kafka-ai-human-decisions/.
- About jargon is an editorial concern, not a measured comprehension defect.
- CI's pinned project-type claim is narrowed to changing the AGENTS marker alone;
  the same PR can change workflow/validator source, which still requires review.

## Verification and delivery

Validation and independent review pending. No runtime behavior change; no artificial
mutation or service E2E is required. Blog contents and local installations unchanged.
