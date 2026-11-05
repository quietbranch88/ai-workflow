# Repository guardrails

## Goal

Document and apply a server-side default-branch guardrail for the AI Workflow
repository so direct pushes cannot bypass pull-request evidence and hosted checks.

## Scope

### In

- Add concise canonical guidance for server-side default-branch protection.
- Require a pull request and the existing `Workflow contracts` status check on
  `quietbranch88/ai-workflow` `main`, including for administrators.
- Block force pushes and deletion while requiring zero approving reviews for this
  solo repository.
- Add contract coverage, synchronize the Claude workflow mirror, and bump the
  plugin version to 0.6.18.

### Out

- No required reviewer or CODEOWNERS policy.
- No deployment, plugin installation, or unrelated repository setting change.
- No claim that local hooks or prompt instructions enforce a GitHub branch.

## Acceptance criteria

- [x] Observable: the public guidance distinguishes local guidance from
  server-side enforcement and recommends pull requests plus required checks for
  protected default branches.
  - Environment: feature worktree for `quietbranch88/ai-workflow`.
  - Verify: targeted documentation contract test.
  - Oracle: GitHub protected-branch documentation and the accepted CabLate pattern.
  - Required boundary: `docs/repository-guardrails.md`, `workflow.md`, and `README.md`.

- [x] Observable: solo-maintainer guidance does not create an impossible review
  gate and preserves a separate approval boundary for repository-setting changes.
  - Environment: local documentation plus GitHub repository settings.
  - Verify: targeted contract test and direct source review.
  - Oracle: GitHub permits zero required approvals while still requiring a PR.
  - Required boundary: policy text and branch-protection configuration.

- [x] Observable: `main` rejects direct pushes, force pushes, and deletion and
  requires the `Workflow contracts` check on pull requests, with admin enforcement.
  - Environment: GitHub repository `quietbranch88/ai-workflow`.
  - Verify: authoritative branch-protection API readback and an enforced PR check;
    the final green result remains a delivery receipt on the pull request.
  - Oracle: GitHub branch protection response for `main`.
  - Required boundary: repository branch settings; no deployment boundary.

## Risks

- A wrong check name could block all merges -> bind the rule to the observed
  GitHub check name and read the configuration back.
- A mandatory approval could deadlock a solo repository -> require a PR with
  zero approving reviews.
- Documentation could imply local enforcement -> explicitly separate prompt,
  hook, and server-side guarantees.
