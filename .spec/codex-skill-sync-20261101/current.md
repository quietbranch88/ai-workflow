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
publication is authorized by the user's sync request; main integration remains a
separate action under the existing approval policy.

## Delivery state

Prepared for the authorized `codex/codex-skill-sync-20261101` branch publication.
An external receipt records the exact outgoing SHA and subsequent remote readback;
this source record does not claim an unperformed main merge or hosted CI run.
