# Workflow readability audit

## Scope and baseline

2026-10-04: main `442a7f9737d6fba9396be1a857bf2a4f525e7e97`, isolated clean branch.
Documentation review only; source traces do not establish measured usability.

## Findings carried forward

All four were confirmed/open against the baseline. The resolutions below are
confirmed/fixed at `facd078ea264bd65b3cf97878613fbc091e2fd5c`, supported by the
source checks, independent review and executed verification recorded below.

- **WF-D01 / medium / confirmed / fixed**: `workflow.md:104-105` promised no
  synthetic history for trivial docs, while `scripts/validate_workflow_docs.py:208-236`
  and `.github/workflows/validate.yml` require records for every non-living path in
  tracked Ship mode. A README typo triggers the mismatch. Counterevidence: the
  strict rule was already documented elsewhere. Resolution: remove the exemption
  promise and state the precise limitation in workflow, template and README;
  preserve existing checks. Source inspection, not a new runtime reproduction.
- **WF-D02 / medium / confirmed / fixed**: `README.md:24-58` omitted target-project
  navigation and mandatory template setup; `templates/AGENTS.md.template:8,91-93`
  retains placeholders. New adopters could follow all steps with incomplete rules.
  Counterevidence: the template says to set one project type. Resolution: explicit
  configuration step and separation of optional local checks from this repo's CI.
- **WF-D03 / low / confirmed / fixed**: `workflow.md:64-65` and template `:50`
  sent all implementation-only decisions to ADRs, conflicting with architecture-only
  guidance. Routine choices could create needless documents. Counterevidence:
  template task-file guidance already limits ADRs to architecture. Resolution:
  task/handoff for ordinary choices, ADR for architecture tradeoffs; remove the
  contradictory commit-to-PR-to-ADR sequence. This is wording ambiguity, not
  observed excessive documentation by users.
- **WF-D04 / low / confirmed / fixed**: `README.md:195-201` contained an incomplete
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

Executed on 2026-10-04 against the product-document tree at `facd078`:

- `python -m unittest discover -s tests -v`: 62 passed in 22.811 seconds.
- `claude plugin validate --strict .` and
  `claude plugin validate --strict ./claude-code/plugin`: both passed.
- `git diff --check`: passed. Both manifests parse; adapter version is 0.6.1.
- Relative Markdown destination check: all 34 destinations in the changed
  README/workflow/template exist. GitHub Markdown API returned rendered HTML
  containing the diagram block, setup step and linked articles.
- `python scripts/check_close_the_loop.py`: initially rejected missing task-N
  identifiers in the new record; corrected in `e4e831c`, then passed with 0 warnings.
- Independent initial review of `442a7f9..facd078`: no new actionable findings,
  WF-D01 through WF-D04 confirmed fixed; reviewer independently ran 19 docs
  contract tests, diff whitespace check, JSON and normalized mirror checks.
- Chrome on the actual GitHub README at branch
  `improve-workflow-readability-20261004` (HEAD `e4e831c`, README last changed at
  `facd078`): navigated to the operating-loop anchor; observed all six rendered
  Mermaid nodes and the two return paths, inspected top and bottom visually.
  Expanded the optional CI disclosure and verified the strict policy text appears.
  Clicked the original English article link and confirmed its destination URL,
  title and body. No mocked boundary. This is desktop documentation rendering
  and navigation evidence, not user comprehension or mobile-layout testing.
- GitHub About description updated and read back exactly as the plugin description:
  "Practical prompts, templates, and checks for planning, testing, and reviewing
  work with AI coding agents."

No executable code, dependency or CI logic change; no artificial mutation or service
E2E is required. Blog contents and local installations unchanged. The branch is
published; PR/hosted checks are recorded in the delivery response. This follow-up
is not merged, and prior approval for PR #20 does not authorize its merge.

## First-reader follow-up: FR-01 (2026-10-04)

Prior review target: `da4014bc472e213b59f395ba440ddf32e485b89f` (merged PR #21).
This supersedes the previous section's unmerged delivery state for that PR only.

- **FR-01 / P2 medium / confirmed / open**: `workflow.md:74-77` told a first-time
  cross-repo user to read a missing `system-map.md` FIRST, while
  `context-management.md:29-37` declares the map optional. The Quick start promises
  an actionable entry after project configuration. Expected: a missing-map path
  that names the involved repositories and edges without requiring a global map.
  Actual: ambiguous prerequisite. Counterevidence: the context guide offers a map
  generator and single-repo work is unaffected. Evidence is source comparison and
  a fresh agent's reading simulation, not an executed human usability study.
- Proposed fix: state both existing-map and missing-map behavior in canonical
  workflow/context guide; make close-loop map updates conditional on existence;
  preserve bounded exploration and private-map restrictions. Synchronize the mirror.
- Related editorial correction: display the original article title separately
  from explicitly labeled English and Chinese links; destinations remain unchanged.
- No executable code, tests, dependency or CI changes. Validation/review pending.

### Scope correction and download verification (2026-10-04)

Zoe subsequently requested English-only links and asked whether the downloadable
code works with Codex. This supersedes the bilingual-label proposal above. The
real-hook defect below expands the patch to one executable template and one test;
the earlier documentation-only scope statement no longer describes the final patch.

- Fresh public clone of `main@da4014b`: 62 tests passed in 23.784 seconds, including
  real PowerShell task/bootstrap and disposable Git push tests. This establishes
  those exercised paths, not every optional helper or agent's future behavior.
- `pwsh -NoProfile -File scripts/build-spec-map.ps1 -SpecPath .spec -DryRun`:
  exit 0, six task areas listed, no map written. Status remains a heuristic as documented.
- Environment: Windows, Python 3.11.9, PowerShell 7.6.5, pre-commit 4.6.2.
- Official AGENTS guidance https://learn.chatgpt.com/docs/agent-configuration/agents-md
  confirms project-root instruction discovery. README now says to configure and
  open the target project, not just clone the shared library. No Codex model run
  or real `-LaunchCodex` session was executed. That optional switch needs user-defined
  profiles, which the repo does not install; this requirement is now documented.
- **DL-01 / P2 medium / confirmed / open pending final review**: distributed
  `templates/pre-commit.template.yaml:15` passes a literal `~` as a Python script
  argument. Trigger: copying/installing the advertised hook in a target repo.
  Expected: invoke the installed close-loop guard. Actual: pre-commit launches
  without a shell, so Python reports file-not-found under the target repo's `~`
  directory. Real pre-commit reproduction on downloaded main confirmed exit 2
  from Python, before the guard. Counterevidence: direct shell invocations and
  existing validator tests work; neither exercises this template entry.
- Fix: resolve Path.home inside Python and execute the installed script via runpy.
  A new integration test runs the actual template local block through pre-commit
  with a disposable home containing spaces, checks code-only rejection by the
  real guard and acceptance after adding valid draft records.
- Test development correction: the first draft expected the wrong rejection
  wording. After matching the existing guard diagnostic, the unchanged final test
  failed against the historical template in an isolated copy at the launch/guard
  assertion, then passed after restoring the fixed template. This is regression
  evidence for the launch defect; startup failure is the defect being tested.
- `ruff check scripts tests`: passed. Bandit 1.9.4 on the new test reported five
  LOW B404/B603/B607 warnings, zero medium/high; scan exit 1, not a clean scan.
  **DL-SCAN-01 / low / false-positive / dismissed** for introduced command injection:
  test-only subprocess import/calls at lines 5,37,57 use argument arrays without
  a shell and fixed tool names plus disposable paths/known Git refs. Trusted local
  PATH is required, as with the existing Git integration tests; no remote input
  or privilege elevation is introduced. No dependencies were added/upgraded;
  pyproject declares no dependency inventory, so no advisory result is claimed.
