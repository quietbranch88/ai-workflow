# Workflow readability and consistency

## Goal

Make the public entry point usable without prior workflow vocabulary, resolve
the four confirmed design-review findings, and link the owner's relevant writing.

## Acceptance criteria

- [x] Observable: the README explains the artifacts, includes a six-stage diagram
  with repair loops, and lists the target directory and template configuration.
  - Environment: repository Markdown and GitHub rendering.
  - Verify: rendered README inspection, links and independent document review.
- [x] Observable: workflow, project template and packaged mirror agree that tracked
  Ship validation has no trivial-document exemption; routine decisions use task
  records and ADRs are reserved for architecture tradeoffs.
  - Environment: unchanged validator and updated guidance.
  - Verify: source trace, existing repository contract tests and mirror comparison.
- [x] Observable: the About text and plugin descriptions use plain language, and
  the README links verified original and later Kafka articles on Zoe Builds.
  - Environment: repository metadata and public article pages.
  - Verify: JSON parsing, article reads, Markdown rendering and About readback.

## Non-goals

- Change validator behavior, weaken CI, or claim a new lightweight automated exemption.
- Edit blog articles, local installations, unrelated rules, or published history.
- Treat preparation, PR publication and merge as the same state.

## First-reader follow-up acceptance (2026-10-04)

- [ ] Observable: cross-repo tasks can start without a system map; an existing
  map is read and its affected entries are maintained, with privacy preserved.
  - Environment: canonical workflow, context guide and packaged mirror.
  - Verify: inspect both missing-map and existing-map instructions; mirror contract tests.
- [ ] Observable: the original article has explicit English and Chinese link labels.
  - Environment: README rendered by GitHub.
  - Verify: inspect generated link text and destinations; Chrome navigation check.
