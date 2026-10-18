# Audit

## Intake

Fetched and pulled main; no upstream drift. Clean feature branch at d6f1e10.
Read global policy, workflow/context management, repository guidance, distribution,
review contracts and prior delivery records. Article: https://claude.dev/blog/solving-code-review-at-anthropic/
This is design input, not proof of local agent performance. Existing independent
review and finding disposition are retained. Baseline: 64 passed, one hook test
skipped because pre-commit was not on PATH; final tooling-enabled run is below.

## Pilot dataset correction

Initial case-02 reviewer identified a valid fixture bug: contract allows whitespace
but the clean fixture prefix accepted only ASCII space/tab, rejecting U+00A0.
Classify as a confirmed dataset defect, not a model false positive. Stop scoring,
correct the clean reference to accept line-local whitespace and add a U+00A0
assertion. Preserve the initial report. Re-export and rerun the affected case with
fresh context; other packet bytes are unchanged and their reports remain applicable
with explicit carry-forward provenance. No hidden oracle was weakened.

The second fresh case-02 pass found another valid reference mismatch: the contract
requires whitespace after an optional dash, while the minimized pattern allowed
zero. Correct the pattern without weakening the contract, add positive/negative
prefix tests, preserve that report and re-export before the final bounded pass.
Both are dataset defects, not false-positive reviewer findings or performance gains.

## Reviewed payload and findings

Review base: `d6f1e10e3071338bd28298e38b3e0fcfc90b48c3`. The final 19 functional,
prompt, fixture and adapter files have ordered filename/NUL/raw-content/NUL SHA-256
`9340f175ef62da69494ac8b95463625267421dc4893c32bc308825d4a0e3d74a`.
Living records are excluded from that reviewed payload digest.

- D1: P2, confirmed/fixed, initial exported case-02 candidate line 7. U+00A0
  before Observable caused a false warning despite the fixed whitespace contract.
  Source trace plus unchanged-contract reference assertion confirms the correction.
- D2: P2, confirmed/fixed, second case-02 candidate line 7. `-Observable: ready`
  was accepted despite the contract requiring whitespace after a dash. Positive
  and negative prefix assertions confirm the final corrected behavior.
- R1: P3, confirmed/fixed, initial builder adapter line 176. Following the copied
  `../evals/reviewer/README.md` link resolved inside `plugin/evals`, which does not
  exist. The canonical source link itself resolved correctly; the mirror location
  was the counterexample. Replace the link in both sources with the explicit
  workflow-source path. Independent final source read and 19 mirror tests verify
  the correction in the payload hash above.

Fresh independent patch review found no remaining actionable defects. It executed
six eval tests, 19 contract tests and an independent two-trial hand-calculated
scoring check. Its source review confirmed acceptance-warning historical revisions;
installer historical reproduction was covered by the earlier independent oracle
research, not rerun by this reviewer. Patch review is separate from pilot scoring.

## Executed verification

- `python3 -m unittest discover -s tests -v`: all 71 tests pass, zero skips, using
  existing pre-commit tooling through an absolute PATH. An intermediate run with
  relative PATH failed when the existing hook test changed directories; that was
  an invocation/environment error, retained separately, not a candidate-code fix.
- `python3 -m unittest discover -s tests -p test_docs_contracts.py -v`: all 19
  pass after the final link-only correction. No executable behavior changed after
  the full suite run.
- Controlled mutation in a disposable copy changed detected-defect counting from
  unique matched defects to all finding IDs. The unchanged mixed-outcome assertion
  failed with incorrect counts. Restore the original implementation: the same
  targeted test and CLI check pass. No mutation is in the deliverable.
- `python3 scripts/check_close_the_loop.py` and `git diff --check`: pass.
- Changed-file `validate_workflow_docs.py --mode ship --spec-policy tracked
  --project-type personal`: pass with zero warnings. Both superseded case-02
  exports were executed against the unchanged contract examples: each reproduced
  its defect; the final exported reference passed both expectations.
- Claude CLI 2.1.210: `plugin validate --strict .` and
  `plugin validate --strict claude-code/plugin` both pass. Packaging validation is
  not an installed-session or agent-behavior test.
- Bandit on the new scorer: no findings or scan errors. Changed-file detect-secrets
  scan with network verification disabled: no findings. New code uses only Python
  standard library; no dependency manifest/lock or external runtime dependencies
  are added, so there is no new dependency set to advisory-scan.

Local logs, raw reports, original task prompts, packet hashes, corrected packet
versions, adjudicated JSON and actual CLI score are retained in the task's separate
`reviewer-pilot-20261019` evidence directory, outside this published source tree.

## Convergence tabletop (source checks, not runtime enforcement)

| Scenario | Required result checked against the contract |
| --- | --- |
| Initial review clean and all applicable gates resolved | Stop after round 1; no forced extra finding or round |
| Three completed passes still have unresolved finding IDs | Record IDs, repeated classes, evidence and cause; reassess approach/oracle/scope before dispatch |
| New commit after round 2 | Next substantive completed follow-up is round 3; counter does not reset |
| Transport retry or incomplete worker | Record failure separately; do not count another completed pass |
| Several reviewers in one pass | One round, not one round per worker |
| Three further unresolved rounds after reassessment | Reassess again; preserve findings and gates |
| Material architecture/risk/approval choice | Existing user decision boundary applies |
| Optional nit or serious newly revealed caller risk | Nits do not force loops; evidence-backed serious risk can expand follow-up scope |

## Pilot results and limitations

Final dataset digest:
`074b4c752ffb401d7eee2bd8cb24ddd2d1f453508bb1cb57bccb70023299ac6f`.
The coordinator executed the actual export/report/adjudication/score path locally:
four final case instances, one completed source-review pass each, two known defect
classes detected, zero misses, zero unsupported findings, zero of two clean cases
with false alarms, two duplicate matches and zero infrastructure failures. Each
duplicate is another manifestation of an already detected historical defect class.

There were six review dispatches in total, including two invalid clean-reference
versions before correction. They are preserved and excluded with reasons, not
counted as false positives or silently omitted successful trials. Case-01 and -03
reports came from the initial export, case-04 from the second; both files for each
were byte/hash-checked against the final dataset before carrying reports forward.
Case-02 final is a new fresh-context review of the corrected third export.

Reviewers did not inherit parent history and each reported reads limited to the
required global policy and one packet. Shared filesystem permissions were not
technically restricted to those files. Model/configuration IDs, token use,
per-run elapsed time, CPU/RAM guarantees and explicit kill limits were not exposed
or captured and are recorded as unknown. Responses were bounded by one source pass
and a requested 220-word limit. Maximum harness capacity was four active agents
including the coordinator; exact overlap was not measured. No independent human
adjudication or repeated stochastic trials occurred. The small, adapted dataset
does not establish stable model quality, baseline improvement or real-PR accuracy.

## Delivery state

Implemented, reviewed and locally verified on the feature branch. This update has
not been merged, pushed or installed. Existing installed main and current sessions
are unchanged. No PR/tracker/message surface was created; only local records were
reconciled. Source completion does not imply automatic execution of the checkpoint.
