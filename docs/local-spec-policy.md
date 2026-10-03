# Local-only task records

The default `tracked` policy keeps shareable living documents in the change.
Repositories that prohibit publishing `.spec/` must explicitly select `local-only`.
This policy is independent of `personal` versus `team`; never infer it from missing
files or relax an existing repository rule. This repository retains tracked policy.

## Configure locally

1. Record the policy in the repository's rules and exclude `.spec/` using the
   repository's approved ignore mechanism. Continue maintaining task records.
2. If files were tracked, inspect the exact paths and remove only their index
   entries while preserving local files. Do not rewrite published history without
   separate authorization; removing files now does not erase prior publication.
3. Use a **native Git pre-push hook** receiving the full stdin ref list, as shown
   below. Do not use the pre-commit adapter for local-only privacy: it exposes only
   one ref pair and can miss another branch in the same push. Set `WORKFLOW_TICKET`
   to the task's relative slug, or pass `--ticket topic/name`. The hook checks WIP structure.
4. Before delivery, run Ship validation locally, using the actual code comparison:

```sh
python /path/to/ai-workflow/scripts/validate_workflow_docs.py --root . \
  --spec-policy local-only --ticket topic/name --mode ship \
  --base origin/main --head HEAD
```

Select the repository's actual integration ref. A local-only ticket must have
`current.md` and `tasks.md`; they need not appear in the Git diff. WIP allows open
checkboxes, Ship does not. Both reject malformed records and placeholders. An
explicit safe slug is required; paths escaping the repository are rejected.

For an otherwise empty `.git/hooks/pre-push` (make it executable on Unix):

```sh
#!/bin/sh
exec python /absolute/path/to/ai-workflow/scripts/check_close_the_loop.py \
  --spec-policy local-only --native-pre-push "$@"
```

Git supplies the remote name/URL as arguments and every ref update on stdin.
Preserve existing hooks: if a pre-push hook already exists, deliberately compose
the checks while buffering/replaying the same stdin to each. Do not overwrite it
or consume stdin before another check needs it. The tracked policy can continue
using pre-commit; local-only mode refuses that incomplete adapter.

The local validator rejects `.spec` files in the index. The pre-push caller also
checks every ref update and its outgoing commits for `.spec` files, including a file
added and later removed within the push. New refs use freshly advertised remote
tips rather than cached origin refs; unknown remote objects cause conservative
history checking. It fails on malformed input or unreadable history/remotes. The legacy
`CLOSE_THE_LOOP=skip` escape hatch does not disable local-only checks. Git hooks
can still be bypassed; these are local safeguards, not server-side enforcement.

## Evidence and CI boundary

Local-only validation checks named local records, not whether they were updated for
the current patch or whether their claims are true. Review binds evidence to the
revision. In this mode the validator does not require publishing `devlog.md` or
`todo.md`; maintain authorized project records according to repository policy.

Do not upload private records as CI artifacts, PR attachments or plugin content.
A clean hosted checkout lacks local evidence and cannot claim to validate it.
Keep repository tests/security checks in CI; any hosted adaptation needs its own
approved public evidence contract. This change does not modify hosted CI policy or
authorize changing a team's pipeline. Do not pass local-only merely to bypass a
tracked-document requirement.
