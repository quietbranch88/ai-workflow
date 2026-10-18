# Context routing audit

## Source and scope

- Baseline: main dda8272, synchronized with git pull --ff-only on 2026-10-18.
- User requested agent review and modifications, with a pull before changes.
- Only generic shareable workflow guidance is recorded in this repository.
- Two principles informed the change: task-relevant context and evidence-backed
  lessons. External articles are background, not authority over project rules.

## Baseline

- python3 -m unittest discover -s tests: 63 tests run, OK, 1 skipped.
- Independent reviewer confirmed minimum-question Define and scoped review already
  exist. These contracts were reused rather than duplicated or weakened.

## Candidate verification

- Fresh independent review of the public patch and task records found no
  actionable issue; mandatory instructions and existing approval gates remain.
- python3 -m unittest discover -s tests -v: 63 tests run in 14.806 seconds,
  OK with 1 skipped. The hook-installation test requires unavailable pre-commit;
  Git is present. This skip also existed in the baseline.
- git diff --check: passed.
- python3 scripts/check_close_the_loop.py: passed; on an uncommitted candidate it
  compares committed refs, so explicit changed-file Ship validation is also used.
- Relative Markdown link and anchor checks on changed guidance: passed.
- Ship document validation with every changed path explicitly supplied: passed,
  0 warnings. The first run caught missing task-N prefixes in the task record;
  those identifiers were corrected and the same check passed.
- The 280-line workflow, canonical review contracts, plugin mirrors and manifest
  were unchanged; existing adapter consistency tests passed. Claude CLI is not
  installed, so strict external plugin validation was not run.
- No runtime behavior changed; artificial fail-to-pass or mutation evidence is
  not applicable. No new behavior tests were added for the wording changes.

## Scenario walkthroughs

- Clear ticket: required sources and existing decisions are read first; no
  consequential gap means work proceeds without a forced confirmation.
- Missing required contract: dependent action waits; optional missing indexes do
  not prevent direct source inspection.
- Changed base or environment: refresh affected facts and expand review where
  required, without treating old evidence as current.
- One-off suggestion: retained in the task; no quota promotes it to policy.
- Reproducible mechanical failure: propose an executable check and evidence;
  existing capture authorization is still needed before saving guidance.
- Private incident: detailed source stays private; public guidance requires a
  shareable reproduction.
- Resumption: snapshot exposes revision, evidence, blockers, next action and
  recheck trigger; source is checked before relying on a material summary.

These are source-based scenario checks, not measured agent-behavior trials.

## Delivery

Prepared locally. Not pushed, merged or installed. Installed global files and new
session loading are outside the verified boundary.
