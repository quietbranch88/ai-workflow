# Tasks

- [x] task-1: Point the README model sentence at deterministic tools for Verify.
  - Files: README.md
  - Verify: `git diff 6dd7c30 -- README.md`
  - Evidence: recorded in audit.md.
- [x] task-2: Correct the portfolio anti-drift sentence and the verify-done evidence rule, including the plugin mirrors.
  - Files: prompts/portfolio-scan.md, prompts/verify-done.md, claude-code/plugin/skills/portfolio-scan/SKILL.md, claude-code/plugin/skills/verify-done/SKILL.md
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_evidence_skill_mirrors_match_canonical_content -v`
  - Evidence: recorded in audit.md.
- [x] task-3: Correct the Go timeout and Celery retry sentences in the pitfall guides and their plugin skills.
  - Files: pitfalls/go.md, pitfalls/python.md, claude-code/plugin/skills/go-pitfalls/SKILL.md, claude-code/plugin/skills/python-pitfalls/SKILL.md
  - Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests.test_python_pitfalls_do_not_name_a_missing_dependency_skill -v`
  - Evidence: recorded in audit.md.
- [x] task-4: Keep an open item visible when a comment is removed from between fence markers, and record the merged Markdown count.
  - Files: scripts/validate_workflow_docs.py, tests/test_workflow_enforcement.py, .spec/review-fixes-20261031/audit.md
  - Verify: `python3 -m unittest tests.test_workflow_enforcement.WorkflowDocumentValidatorTests.test_ship_sees_boxes_hidden_by_comment_fences_or_mismatched_closers -v`
  - Evidence: recorded in audit.md.

## Acceptance

- [x] The acceptance criteria name the original goal and the comparison that ran.
- [x] Documentation edits use claim review. No runtime test was invented for them.
- [x] No new dependency or secret-bearing file.
- [x] Machine installation stays separate from this record.
