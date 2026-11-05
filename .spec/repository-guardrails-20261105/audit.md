# Audit

## Sources and decisions

- Zoe approved adding the previously proposed repository guardrail on 2026-11-05.
- GitHub documents that a protected branch can require a pull request with zero
  approving reviews, required status checks, and administrator enforcement.
- CabLate's article motivated the operational pattern; GitHub documentation and
  API readback are the authoritative configuration sources.

## Verification

- The initial targeted contract errored because
  `docs/repository-guardrails.md` did not exist. The same contract then passed
  with the new policy and entrypoints.
- `python3 -m unittest discover -s tests -v`: 98 tests passed in 29.992 seconds.
- `claude plugin validate --strict .`: passed.
- `claude plugin validate --strict claude-code/plugin`: passed.
- WIP workflow-document validation passed with zero warnings.
- Exact canonical/Claude mirror, 280-line workflow ceiling, and targeted
  repository-guardrail contracts passed.
- `git diff --check`: passed.
- Fresh author self-review found no actionable documentation or configuration
  mismatch. This was not an independent second review.
- The first feature-branch push was blocked before network dispatch because the
  installed pre-commit hook resolved `.git/ai-workflow/pre-commit.yaml` relative
  to a linked worktree, where `.git` is a file. The expected WIP validator and
  range diff check were rerun manually and passed. The next attempt uses the
  hook's documented one-shot `PRE_COMMIT_ALLOW_NO_CONFIG=1` fallback; this is an
  environment workaround, not evidence that the hook executed.

## GitHub configuration readback

- Repository / branch: `quietbranch88/ai-workflow`, `main`.
- Read back on 2026-11-05 through GitHub's branch-protection API.
- Pull request requirement: enabled with zero approving reviews.
- Required status check: strict `Workflow contracts`, bound to GitHub Actions
  app id `15368`.
- Administrator enforcement: enabled; restrictions/bypass actors: none.
- Force pushes and deletion: disabled.
- Hosted pull-request evidence is pending the feature-branch publication.

## Hosted pull-request evidence

- PR #37 launched `Workflow contracts` on source `0513ba4`, proving that the
  required check is attached to the pull-request path.
- The first hosted run failed only at the Ship record gate: one unchecked item
  in `current.md` and three in `tasks.md`. Repository tests had passed before
  that step. This final record update resolves those known items; the next run's
  conclusion is a GitHub delivery receipt, not preclaimed local evidence.

## Delivery state

- Prepared and locally verified in an isolated feature worktree.
- The approved `main` protection setting is applied and read back, and PR #37 is
  published. Merge, deployment, and plugin installation are not yet claimed.
