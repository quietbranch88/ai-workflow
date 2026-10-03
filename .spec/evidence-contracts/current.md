# Evidence contracts and private task records

## Goal

Bring the portable workflow, templates and optional adapter up to the accepted
evidence and review contracts without publishing private rules or weakening the
existing tracked-document checks.

## Acceptance criteria

- [x] Observable: review guidance distinguishes initial, follow-up and claim checks;
  findings retain evidence, counterevidence, validity and disposition.
  - Environment: canonical Markdown and packaged Claude adapter.
  - Verify: direct claim review and adapter contract tests.
- [x] Observable: verification guidance requires independent oracles, applicable
  defect-detection evidence and real boundaries; TDD remains optional unless required.
  - Environment: workflow, templates, global example and adapter.
  - Verify: direct review against this contract; repository tests and strict plugin validation.
- [x] Observable: explicit local-only policy validates a named local ticket without
  requiring its files in the Git diff; missing or incomplete evidence still fails.
  Tracked policy remains the default. Private files in the index or outgoing commits fail.
  - Environment: disposable Git fixtures through validator and pre-push entrypoints.
  - Verify: new failing-baseline tests, unchanged-test pass after implementation,
    and the complete unittest suite.
- [x] Observable: architecture guidance preserves existing structures and makes
  only necessary boundary repairs; metadata accurately describes the workflow.
  - Environment: public docs, manifests and GitHub About description.
  - Verify: diff review, JSON parse, Markdown link check and remote readback.

## Non-goals

- Copy private/company configuration into this repository or update local installations.
- Change hosted CI policy, repository permissions, production systems or published history.
- Merge the pull request without the owner's explicit approval.
