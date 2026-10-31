# Audit

## Intake

Clean `main` at `ad76dde`. No open issues or pull requests. Local
`python3 -m unittest discover -s tests -v` on that base: 71 tests, 68 passed,
3 skipped because `pwsh` and `pre-commit` are not on PATH.

## Findings fixed here

- Packaged grill-me skip list allowed a simple request, a clear spec, or an
  instruction to proceed to waive clarification. `prompts/grill-me.md` already
  required a remaining consequential unknown, including for product and
  authorization decisions. The skill now carries that guard and names
  `prompts/grill-me.md` as its canonical source.
- `prompts/portfolio-scan.md` called `mine` the short form of a different
  `gh repo list` command. The prompt now keeps only its own command.
- `pitfalls/python.md` named a `verify-deps` skill that is not in this
  repository. The line now matches the packaged checklist: "New deps verified".

Checked todo text for PR #18 (`2838a8f`, merged 2026-07-15) and PR #24
(`b2e5d66`, merged 2026-10-04). Both commits are ancestors of `main`. Machine
installation, new language pitfalls, and local-install comparison stay open.

## Left unchanged

Portfolio-scan and build-system-map skills remain paraphrases of their canonical
prompts, including the system-map privacy paragraph that exists only in the
skill. The `mine` alias is unchanged. This record does not install or merge.

## Verification

Revision `0cdb659` contains the wording, contract tests, and living records.

- `python3 -m unittest discover -s tests -q`: 74 tests, OK, 3 skipped
  (`pwsh` task-bootstrap tests and the pre-commit hook test). No red run was
  executed; the new tests forbid the previous sentences directly.
- `git diff --check`: pass.
- `python3 scripts/validate_workflow_docs.py --mode ship --project-type personal`
  on the changed files: pass, 0 warnings.
- Claude CLI is not installed here, so `claude plugin validate --strict` did not
  run. Hosted pull-request validation remains the check for that gate.
- No UI, dependency manifest, or secret-bearing file changed.
