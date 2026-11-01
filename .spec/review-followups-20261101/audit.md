# Audit

## What changed

The post-merge review gaps are closed in the working tree. Plugin version is 0.6.13.

- `README.md` sends Verify to deterministic tools. A faster model searches or
  classifies exact tool output.
- Portfolio scan no longer calls the spec-map rule "regenerate, don't hand-edit".
  A curated map is dry-run and compared, and is not overwritten. Portfolio rows
  stay generated.
- verify-done uses claim review for documentation and behavior-neutral edits.
  A bug can use a failing baseline, a historical defective revision, or a safe
  controlled mutation.
- `ReadHeaderTimeout` and `IdleTimeout` of 0 inherit `ReadTimeout`. A Celery
  task runs once unless retry or broker redelivery is configured. The plugin
  skills match those pitfall files.
- Ship mode still sees an open item when a comment sits between fence markers,
  including `<!-- x -->` before a fence marker. A closed fence example still
  does not count.
- The merged review audit now says the link check covered 25 Markdown files
  and the merged range has 26, because that audit file was added afterward.

`workflow.md` stays at 280 lines.

## Original goal and what was compared

The goal was to stop the `6dd7c30` review text from sending a later agent to
the wrong check, and to keep Ship mode from missing an item hidden by a
comment between fence markers.

What this run exercised:

- The nine ship and contract tests named in `tasks.md`: 9 tests, 0 failures.
- `python3 scripts/validate_workflow_docs.py --mode ship --project-type personal`
  on this working tree: pass, 0 warnings.
- `git diff --check`: pass. Work commit `aec6125`.
- The Python and Go pitfall skill bodies match `pitfalls/python.md` and
  `pitfalls/go.md`.

That comparison reads the documents and the validator. It does not install
plugin 0.6.13 or run the four local timeout tests.

## Deliberately left

- Four unit tests that time out on this machine.
- Historical devlog entries.
- Machine installation of 0.6.13.

## Not claimed

- The full unit suite and hosted Claude plugin validation did not run for this
  follow-up. The earlier merge's hosted check passed at `6dd7c30`.
