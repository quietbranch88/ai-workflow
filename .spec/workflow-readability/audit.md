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

### Final follow-up verification and dispositions

Product target `01c8d3b9fa00f2d743377d7a7ead37dad8f82731`, base `da4014b`:

- Full local suite: 63 tests passed in 30.116 seconds; new real pre-commit test ran,
  not skipped. Both strict Claude package surfaces passed; Ruff and diff check passed.
  Close-loop WIP check passed with zero warnings. Final Ship check follows record closure.
- Independent reviewer found no new actionable issues. Independently ran the new
  hook test (1 passed), docs contracts (19 passed), close-loop and whitespace checks.
  Checked existing guards, runpy argument/exit handling and sibling imports.
- **FR-01: confirmed / fixed at 01c8d3b**. Existing/missing map instructions now agree;
  source review plus mirror tests establish the correction. No human usability claim.
- **DL-01: confirmed / fixed at 01c8d3b**. Actual template invocation reaches the
  guard with a spaced home path; denial and permitted draft paths both pass their
  assertions. Historical-template fail-to-pass evidence recorded above.
- **DL-SCAN-01 remains false-positive / dismissed** with the recorded trusted-PATH
  and test-only argument-array counterevidence. Do not report Bandit as clean.
- 35 relative Markdown destinations verified. GitHub Markdown API rendered README.
  Chrome opened the published branch at `01c8d3b`; observed the new Codex setup and
  prerequisites, English-only story link, and preserved rendered Mermaid nodes.
  Clicked the story link and confirmed English destination, title and body. One
  immediate heading query timed out during navigation; the subsequent page state
  confirmed success. No mock, no blog mutation, no Codex model session.
- Limitations: Bash aliases, optional Codex launcher and Linux hook execution were
  not run. The new test skips without pre-commit/Git; CI does not explicitly install
  pre-commit, so hosted success alone cannot establish this integration path.
- Branch published; this follow-up is not merged. PR and hosted check results are
  recorded in the PR and delivery response. No local installation was changed.

### Codex directory entry and merge authorization (2026-10-04)

Zoe noted that the Claude-only directory naming implied exclusive support, then
explicitly requested MERGE. Add `codex/README.md` and visible root links while
retaining the shared canonical files; do not rename or break the Claude package.

At `7c1da5a`, 19 docs contract tests passed, 38 README/workflow/template relative
destinations and all 7 Codex-guide destinations resolved. Both README documents
rendered through GitHub's Markdown API; whitespace check passed. Focused independent
claim-check of `acb99a6..7c1da5a` found no actionable issue and independently verified
guide links, target-project setup and local/cloud file-access wording against the
official AGENTS guide. No executable change after the reviewed/tested hook fix.

The owner authorized PR #22's merge including this directory follow-up. Final-head
hosted checks, remote merge SHA and post-merge directory state are verified and
reported in the PR/delivery response after this preparation record is committed.
This record does not assert that the merge has already happened.

### WD-01: personal-project approval wording (2026-10-04)

Remote PR #22 was read back as MERGED at `9034daa6d4f3d7d50459eb73f5e88e1c8110cbba`
on 2026-10-04. This supersedes its preparation status above; it does not authorize
merging this later follow-up.

- **WD-01 / medium / confirmed / fixed locally**: fresh source review against
  `9034daa` found `templates/AGENTS.md.template:105-106` telling personal-project
  adopters that destructive-operation approval is the only required backstop.
  Expected: both project types retain all `workflow.md:253-262` approval gates.
  Trigger: copying the template and removing its Out of bounds section for a
  personal project. Impact: readers may infer merge/deploy/publication approval
  no longer applies. Counterevidence: the template already references workflow.md;
  full readers can discover the correct gates. No unauthorized action was observed.
- Fix: allow removing unused local constraints while explicitly preserving
  workflow approval gates for both project types. Fix revision: the commit
  containing this dated entry on `fix-personal-approval-guidance-20261004`.
- Source check: the conflicting phrase had one occurrence, in this template.
  Canonical workflow and its packaged mirror retain their existing approval gates;
  this template has no declared packaged mirror. No plugin version change needed.
- `python -m unittest discover -s tests -p test_docs_contracts.py -v`: 19 passed
  in 4.935 seconds on Windows. `git diff --check`: passed. Direct review of the
  replacement against canonical Approval gates confirms the wording correction;
  the existing tests establish surrounding contract consistency only.
- `python scripts/check_close_the_loop.py`: exit 0 for the local state.
- No executable, dependency, public README structure or rendered UI changes.
  No new runtime install, model session, usability study or service E2E was run.
  This is a local documentation correction; publication and merge remain separate.

### WD-01 delivery authorization (2026-10-04)

Zoe explicitly requested merge after local fix commit `97b40e4`. This supersedes
the earlier pending-authorization state for this follow-up. The close-loop check
was rerun and passed with zero warnings; PR creation, hosted validation and merge
will be read back and recorded in the PR delivery record.

- Fresh independent claim-check of `9034daa..97b40e4`: no actionable findings;
  WD-01 confirmed fixed. Reviewer independently passed 19 docs tests, diff check
  and close-loop validation. Later authorization-only notes were checked by the
  main agent against Zoe's explicit merge request.
- Pre-PR full suite: `python -m unittest discover -s tests -v`, 63 passed in
  28.891 seconds, including the real pre-commit hook test, on Windows.

### Concise onboarding follow-up (2026-10-04)

Baseline: merged main `e996b120d824ca750882c4254865a85cf9e0af2a` (PR #23).
Zoe requested the proposed shorter first-reader README. This is editorial work,
not a new assertion that the earlier README failed a measured usability test.

- README now leads with purpose, three setup steps, a synthetic CSV bug example
  and the unchanged Mermaid flow. Advanced tool prerequisites, CI and model
  routing are folded; the blog story is last. The stage table has two columns.
- Retained the existing-rule preservation guard, required template configuration,
  private-record policy, local/cloud file-access caveat, verification gaps and
  separate merge/deployment authorization. Core contracts, scripts, manifests
  and tests are unchanged. The example is illustrative, not an executed CSV fix.
- Updated the Codex guide's prerequisites link from Quick start to Optional setup.
  Source search found no in-repository links to the removed section anchors.
- `python -m unittest discover -s tests -p test_docs_contracts.py -v`: 19 passed
  in 3.346 seconds. `git diff --check`: passed.
- A temporary local verifier checked 32 relative destinations and heading anchors,
  compared the unchanged Mermaid source with main, and rendered both edited
  README files through GitHub's Markdown API. Whitespace-token counts for the
  root Markdown file: 1,623 before, 1,142 after (30% fewer, rounded); this is a
  length measurement, not evidence of improved comprehension.
- Chrome preview at `http://127.0.0.1:8769/`, rendered from this commit's document
  content with local styling: inspected the three steps and example; expanded
  copy commands and observed both guarded commands; collapsed them; expanded
  optional CI and observed prerequisites and strict Ship text; collapsed it.
  The accessibility tree contained all six Mermaid stages and both repair paths;
  the screenshot showed the example and upper flow. This establishes local
  document/disclosure behavior, not production GitHub styling or a model session.
- Subsequent browser inspection lost its connection. Rebinding and opening a
  fresh tab did not recover it. Full-page visual inspection and clicking through
  the Codex guide's updated anchor were not completed; source link validation
  passed. No mobile or human usability test was run.
- Local-only delivery for this follow-up; no new PR, push or merge. Earlier merge
  authorization applied to PR #23, not this newly requested README revision.

### Final ordering and merge authorization (2026-10-04)

Zoe subsequently requested moving The longer story to the front and merging.
The story now follows the short introduction and precedes Quick start; the
shorter setup, task example and optional sections remain. This supersedes the
story-last and unapproved-merge statements above. Validation and independent
review will be recorded below; remote delivery will be read back in the PR.

- Final document target `1a7cccd`: 63 tests passed in 29.633 seconds; Ship passed
  with zero warnings; diff check passed; 32 relative links/anchors validated and
  both README files rendered with GitHub's Markdown API.
- Fresh independent review of `e996b12..1a7cccd`: no actionable findings. Checked
  ordering, onboarding, canonical policy and actual CI/bootstrap behavior.
  The original blog article was rechecked; the second article was inaccessible
  to the reviewer's web tool, so its unchanged-meaning summary was compared with
  the baseline rather than newly verified against the external article.
- Chrome connection recovered. On the final local preview, the top screenshot
  shows the story immediately after the intro. Clicked Codex and then Optional
  setup; observed the guide and return URL `index.html#optional-setup` with the
  expected section. This closes the prior local navigation gap, not a human
  usability or live GitHub styling claim. Source diagram remains unchanged.
