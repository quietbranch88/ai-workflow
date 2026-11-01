# Publish the native Codex workflow entrypoint

## Goal

Make the locally configured Codex workflow reproducible from the shared repository,
without publishing personal paths, global policies or installation receipts.

## Acceptance criteria

- [x] Observable: A portable native ai-workflow skill routes to the existing canonical workflow and relevant guidance without introducing a second rule set.
  - Environment: Repository skill package and local Codex app-server.
  - Verify: Run the bundled skill validator; temporarily install the exact package in the actual user skill root, run native skills/list and restore the prior bytes; inspect instructions against canonical guidance.
- [x] Observable: Codex setup documents installation, invocation, canonical checkout location and preservation of existing local overrides.
  - Environment: codex/README.md and the packaged metadata.
  - Verify: Review changed links, instructions and the package's two files.
- [x] Observable: The shareable patch passes repository checks and contains no machine-specific paths or private installation records.
  - Environment: Local isolated checkout and the existing GitHub repository.
  - Verify: Run repository tests, both strict plugin validations, WIP and Ship; inspect the staged diff and changed links.

## Scope

Add a thin Codex adapter and setup guidance, update the release version and living
records. No executable runtime, dependency, global policy or hook changes. Remote
publication was authorized by the user's sync request. The user subsequently
authorized integration into main on 2026-11-01.

## Delivery state

Implementation `d8bf259` was published to `codex/codex-skill-sync-20261101` and
confirmed by exact remote SHA readback. [PR #35](https://github.com/quietbranch88/ai-workflow/pull/35)
is the authoritative record for subsequent integration and hosted-check state.
External receipts retain exact operation identities and readback evidence.
Local installation and model-based compliance evaluation remain separate.
