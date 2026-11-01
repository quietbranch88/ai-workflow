# Correct the six workflow audit defects

## Goal

Make the workflow's actual checks enforce the six existing contracts identified at
base 3c507efaa86a33ec9091fd6ecac9a4c40e8a8f05. User authorized fixes, tests and one
fresh review. No merge, publication, installation update or deployment is requested.

## Acceptance criteria

- [x] Observable: tracked checks accept/reject the declared outgoing revision even when working files differ; explicit working-file and local-only checks retain their semantics.
  - Environment: isolated real Git fixtures, WIP hook and Ship CLI.
  - Verify: run test_audit_regressions.GitSnapshotTests.
- [x] Observable: valid Unicode/quoted ticket paths pass through Git-range and WIP adapters without changing their filenames.
  - Environment: Git default path quoting enabled.
  - Verify: run GitSnapshotTests.test_unicode_ticket_passes_range_and_hook.
- [x] Observable: unfinished Markdown task-list items using supported bullet/ordered markers fail Ship; completed records, WIP drafts and fenced examples remain valid.
  - Environment: CLI fixtures.
  - Verify: run test_audit_regressions.MarkdownAndPlannerTests.
- [x] Observable: replacement objects cannot hide private tip or ancestor records from native pre-push; clean raw history still pushes successfully.
  - Environment: synthetic local Git and bare remote, actual native hook and remote ref readback.
  - Verify: run replacement tests in test_local_spec_policy.LocalSpecPolicyTests.
- [x] Observable: filled packaged planner examples pass the real WIP record parser.
  - Environment: packaged role Markdown and actual validator.
  - Verify: run MarkdownAndPlannerTests.test_packaged_planner_records_pass_wip.
- [x] Observable: bootstrap rejects main/master/dev and the actual default branch as ticket destinations before writing records; ordinary feature workflows retain their existing behavior. A configured origin must advertise a readable symbolic HEAD; unavailable/ambiguous defaults stop before writes, and stale/missing cache is not authoritative.
  - Environment: isolated repositories, PowerShell 7, clipboard disabled in wrapper.
  - Verify: run test_audit_regressions.BootstrapBranchTests and existing bootstrap smoke tests.

## Scope and invariants

Use existing CLI modes, repository templates and Git boundaries. Preserve private
local evidence, multiref/deletion behavior and existing fail-closed errors. Keep
changes limited to the six defects, their regression tests, plugin version and
required living records. Do not modify the active installed source checkout.
