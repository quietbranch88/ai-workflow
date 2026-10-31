# Tasks

- [x] Align the reviewed contradictions and add the shape-ceiling rule.
  - Files: docs/verification.md, GOTCHAS.md, workflow.md, prompts, pitfalls, templates, plugin mirrors
  - Verify: AdapterConsistencyContractTests and CanonicalWorkflowContractTests

## Acceptance

- Observable: the contract test finds the shape-ceiling section and plugin 0.6.12.
- Environment: local checkout, Python 3.
- Verify: `python3 -m unittest tests.test_docs_contracts.AdapterConsistencyContractTests tests.test_docs_contracts.CanonicalWorkflowContractTests`
