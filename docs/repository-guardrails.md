# Repository guardrails

Prompt instructions, local hooks, and a green check after a direct push do not
protect the default branch. For repositories where an unreviewed change can
deploy, publish, mutate shared infrastructure, or bypass required evidence, use
server-side branch protection or an equivalent ruleset.

## Recommended default

- **Require a pull request** before merging into the protected branch.
- Require the repository's relevant **required status checks** and bind the rule
  to the observed check name, not an assumed label.
- Apply the rule to **administrators** and leave no routine bypass actor.
- Disable **force pushes** and branch **deletion**.
- For a solo repository, use **zero approving reviews** unless an independent
  reviewer is actually available. The pull request still preserves the diff,
  hosted checks, and merge receipt without creating an impossible approval gate.

Local pre-push checks remain useful as fast feedback, but they are not an
authorization or enforcement boundary. A protected branch also does not prove
the change is correct, deployed, or observed in production.

## Applying a rule

Changing repository rules is an infrastructure or permission mutation and needs
explicit human authorization for the named repository and branch. Before the
write, read the current default branch, existing rules, and the exact status-check
context from GitHub. Preserve unrelated rules.

After the write, perform authoritative API readback and record:

- repository, branch, and timestamp;
- pull-request requirement and required checks;
- administrator enforcement and bypass allowances;
- force-push and deletion settings;
- the pull request and hosted check used to verify the path.

Do not use a destructive direct-push experiment on a protected production branch
merely to prove rejection. Prefer configuration readback plus a normal pull
request; run a negative push test only in a disposable repository or when the
owner explicitly approves that exact probe.
