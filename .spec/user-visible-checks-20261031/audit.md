# Audit

## What changed

`docs/verification.md` now states the user-visible order: take assertions from the
acceptance or QA case, exercise the path in the real browser, then keep it in the
project's existing UI test runner. A green suite without that result stays
unproven. A check that passes and fails with no product change stays unverified.
Observed usage may suggest a case and does not replace the acceptance contract.

The packaged builder embeds the same section. `prompts/verify-done.md` and its
skill say to exercise the visible result before relying on the repeatable check.
`GOTCHAS.md` points at the order. Plugin version is 0.6.8. `workflow.md` was not
expanded.

No Playwright, Jest, Vitest, analytics product, or prompt-keyword method is
required. No speed or cost claim is made.

## Verification

- Targeted contract tests for the new section, builder embedding, verify-done
  mirror, and the 280-line cap: pass.
- `python3 -m unittest discover -s tests -q`: 75 tests, OK, 3 skipped because
  `pwsh` and `pre-commit` are not on PATH.
- `git diff --check`: pass.
- Ship-mode validation of the changed files: pass, 0 warnings.
- Claude CLI is not installed here, so strict plugin validation did not run.
  Hosted pull-request validation covers that gate.
- No UI, dependency manifest, or secret-bearing file changed. No red/green
  mutation was run; the contract tests read the documents directly.
