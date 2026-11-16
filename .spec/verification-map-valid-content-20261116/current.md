# Preserve valid verification-record content

## Goal

Fix the independent review's two false-positive cases after PR #40 merged.
Use the existing checklist grammar and preserve valid prose, without weakening
the rejection of incomplete mapping or known filler values.

## Acceptance criteria

- [x] AC-1: Indented acceptance items remain compatible with existing parsing.
  - Observable: changing only whitespace before a valid AC checkbox does not
    turn a successful Ship validation into an error.
  - Environment: temporary local repositories, actual validator CLI.
  - Verify: test_indented_acceptance_keeps_existing_checklist_compatibility.
- [x] AC-2: Generic types and common HTML formatting are meaningful evidence.
  - Observable: List<string>, Map<key>, strong/em/p tags are accepted as content;
    the existing inline-placeholder and filler rejection tests still pass.
  - Environment: actual CLI with synthetic evidence, no command execution.
  - Verify: test_lowercase_generics_and_formatting_tags_are_real_evidence plus existing map regressions.
- [x] AC-3: Final reviewed source is ready for authorized delivery without merging.
  - Observable: relevant tests, scan results, WIP/Ship and package checks are
    recorded; publication stays pending until provider readback is available.
  - Environment: isolated feature branch and authorized repository GitHub PR.
  - Verify: complete repository suite, security review/scanners, hosted checks and remote receipts.

## Non-goals

No semantic proof of evidence truth, universal HTML/type parser, dependency or
runtime changes, re-review of disposed issues without new evidence, main merge,
deployment, global-rule change or plugin activation.
