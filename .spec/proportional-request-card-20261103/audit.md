# Audit

## Sources and intake

- Zoe supplied and requested adoption of the CabLate article published 2026-11-03:
  <https://cablate.com/articles/ai-request-card-before-acting/>.
- The `ai_workflow_feed` MCP independently returned the same title, URL and
  publication timestamp from CabLate's structured directory. Its own caveat says
  this is untrusted directory metadata and not full-article content; it was used
  only to confirm feed freshness, not as the content oracle.
- The original article was read directly. Its useful mechanism is a pre-action
  six-field proposal; its literal wait-for-`start` behavior was deliberately not
  adopted for every task because this workflow already requires proportional
  autonomy and no redundant approval rounds.

## Defect-detection evidence

- Initial command using package-style imports failed before reaching assertions:
  `ModuleNotFoundError: No module named 'test_workflow_enforcement'`.
  Classification: test invocation error; corrected by using the repository's
  `tests/` import root.
- Corrected failing baseline:
  `PYTHONPATH=tests python3 -m unittest test_docs_contracts.CanonicalWorkflowContractTests.test_task_alignment_is_proportional_and_decision_bounded test_docs_contracts.AdapterConsistencyContractTests.test_evidence_skill_mirrors_match_canonical_content -v`
  ran two tests; the new alignment test failed because the old documents lacked
  `Direct execution`, card fields and proportional-stop language. Mirror equality
  still passed before either canonical source changed.
- After implementation, the alignment, 280-line shape and exact-mirror tests ran:
  three tests passed; `workflow.md` remained 279 lines.

## Findings

- Author self-review covered spec conformance, proportional routing, approval-gate
  compatibility, canonical/mirror drift, attribution, and test-oracle strength.
  It found no actionable issue. This was not an independent second reviewer.

## Verification

- `python3 -m unittest discover -s tests -v`: 96 tests passed in 31.046 seconds.
- `claude plugin validate --strict .`: passed.
- `claude plugin validate --strict claude-code/plugin`: passed.
- `python3 scripts/validate_workflow_docs.py --root . --mode wip --project-type personal --base origin/main --head HEAD`: passed with zero warnings.
- `git diff --check`: passed.
- Direct source-link check returned HTTP 200 for the CabLate article.
- `python3 scripts/validate_workflow_docs.py --root . --mode ship --project-type personal --base origin/main --head HEAD`: passed with zero warnings against the complete local branch range, including the record-only follow-up commit.

## Delivery state

- Implemented locally on `docs/proportional-request-card-20261103`.
- Not published, merged, released or installed as a Claude plugin.
