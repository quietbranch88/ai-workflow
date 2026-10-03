# Evidence contracts AI development map

## Authoritative sources

- current.md: accepted outcome and exclusions.
- tasks.md: work and verification state.
- audit.md: executed evidence and finding decisions.
- docs/rule-distribution.md: portable sources and private overlays.

## Roles and decisions

- Owner requested synchronization of the reviewed gaps and repository description.
- Codex maps the public/local differences, authors the portable patch and tests,
  runs verification and prepares delivery. Human approval still owns merge.
- A fresh reviewer checks the final patch and independent acceptance contract.
- Existing local installation edits are preserved; this task does not install them.

## Verification boundary

The changed executable path is validator/pre-push -> actual disposable Git
repository -> local ticket structure and outgoing commit privacy checks.
Markdown defines intent; it cannot prove agent compliance or production behavior.
