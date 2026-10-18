# Reviewer pilot: known defects and clean controls

This opt-in pilot contains four minimized module-review packets from two real
regressions. It is not a full PR benchmark or a production merge gate. The
reference tests prove each packet's expected behavior; they do not measure a
reviewer's ability. The scoring script performs arithmetic on independently
adjudicated reports, not semantic grading or model inference.

## Run

1. Freeze the source revision and dataset digest before dispatch:

   ```sh
   python3 scripts/reviewer_eval.py export /absolute/new/path/review-packets
   ```

   Export contains only each case's `CONTRACT.md` and `candidate.py`. Give a
   fresh reviewer one packet per trial; never include `oracle.json`, this guide,
   tests, prior reports or another paired case. Preserve the raw report, prompt,
   configuration and timing. The exporter is not a sandbox: use actual isolated
   permissions where available, otherwise disclose the behavioral access limit.
2. Ask for concrete actionable contract violations (trigger, line and effect), or
   no findings. Do not force findings or tell the reviewer which cases are clean.
   Keep the oracle and grading outside its writable scope. All graded behavior is
   stated in the packet contract. No network, real-home writes or package install
   is needed. Candidate callbacks can be inspected without execution.
3. An adjudicator compares **every actionable finding** with the contract and
   reference evidence. Assign the corresponding defect ID only when the finding
   demonstrates it; use `null` for an unsupported finding, with a reason. Similar
   wording or a matching line alone is not enough. If a new valid defect appears,
   stop scoring, correct/version the oracle and revalidate rather than calling it
   a false positive. Record optional nits separately from actionable findings.
4. Score the record:

   ```sh
   python3 scripts/reviewer_eval.py score /absolute/path/adjudicated-run.json
   ```

The tool never dispatches models, retries jobs, changes permissions or approves
code. Use a bounded case/trial/token/time budget selected for the experiment.
A timeout has an explicit infrastructure-error entry, not an empty clean review.
For comparisons use repeated clean trials and record model/configuration, harness,
prompt, tool access, budgets, CPU/RAM/kill limits, concurrency, network/caches and
service versions. State unavailable measurements explicitly. A tiny one-pass
pilot, especially with only behavioral isolation, cannot establish model quality,
improvement over a baseline or generalization to real repositories.

## Record format

Top-level fields:

- `schema_version`: 1; `kind`: `model-review` or `synthetic` (never conflate them).
- `dataset_digest`: value returned by export, covering the oracle and packet files.
- `metadata`: nonempty strings for `model`, `model_configuration`, `harness`,
  `prompt_revision`, `tools_permissions`, `budgets`, `environment`, `adjudicator`.
- `trials`: positive integer. `results` contains exactly one entry for every
  case/trial pair, including failures. No selective omission of failed cases.

Completed result example (schema illustration, not an executed review):

```json
{
  "case_id": "case-01", "trial": 1, "status": "completed", "rounds": 1,
  "raw_report": "Preserve the original reviewer response here.",
  "findings": [{"id": "F1", "defect_id": "mode-dispatch",
                "reason": "Adjudicator cites trigger, contract and source evidence."}]
}
```

A completed clean report has `findings: []`. An infrastructure failure uses
`status: "infrastructure_error"`, an `error` string, the completed round count
(possibly zero), and `findings: []`; retain any partial raw report separately.
Rounds mean completed substantive passes, including the initial pass; parallel
reviewers in the same pass count once. New commits do not reset the count.

Metrics are reported with counts/denominators: recall on completed known-defect
cases; missed defects; unassessed defects from infrastructure errors; unsupported
finding count; clean-case false-alarm rate; duplicate matches; completed/failed
case count; mean/max rounds for completed cases. Repeated findings of one defect
receive one detection credit, not extra recall. Undefined ratios are null, never
100%. No score or round threshold implies permission to merge. The CLI exits 0
for a valid record even when it reports misses or false alarms; exit 2 means an
invalid input or an operational error.

## Frozen oracle and provenance (do not provide to reviewers)

These are compact reproductions with synthetic callbacks/text, not verbatim source
archives, full-system simulations or undisclosed production data. Defect classes
and expectations were selected from the historical contracts before fixture code.
The reference tests are `tests/test_reviewer_eval.py`.

| Packet | Expected finding | Independent historical source |
| --- | --- | --- |
| case-01 | `mode-dispatch`: non-install modes fall through to writes; check and unknown modes are instances of one missing dispatch guard | `zoe-agent-notes` f6a71333b0633f763375e965ca6baf2b3df98ba1, `sync.sh:10,22-28`; recorded isolated check/instal reproduction wrote five synthetic files without backup |
| case-03 | None; check has no side effects, unknown modes reject, install backs up before writing | `zoe-agent-notes` df1a6b6ef4d1dbeed1ad5a0d5d1b28255fcd6b4e, `mac/install_rules.py:142-148,173-175` and `tests/test_mac_installer.py:62-74` |
| case-04 | `empty-acceptance`: substring presence accepts blank labels or prose instead of required populated field lines | `ai-workflow` 709e2d941971e8c6197e83333e7443c26093e45e, `scripts/validate_workflow_docs.py:169-179`; independent `README.md:168-170` and `templates/spec.md:16-21` quality-warning contract |
| case-02 | None; empty/prose-only fields warn while valid fields pass; quality warnings do not fail delivery | `ai-workflow` b55fe9d3bfa7be982d9b77041a72918e2e660992, `scripts/validate_workflow_docs.py:169-185`; unchanged historical assertions had nine relevant red failures then 20 passes |

The minimized contract deliberately excludes legacy collect behavior, full
Markdown parsing and unrelated installer/security behavior. Do not generalize
these packets' clean labels beyond their stated contract. Keep all actual runs
and raw reports outside the published source; publish only redacted, authorized
results with their limits. Developer guidance on review convergence lives in
[the existing review contract](../../docs/review.md).

Design input: [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/).
This pilot does not reproduce that team's proprietary evaluations or measurements.
