# Prompt: Verify done

Before claiming completion, walk every acceptance criterion against evidence from
this session and the named revision. Follow [verification contracts](../docs/verification.md)
and [review/delivery reconciliation](../docs/review.md).

Report:

```text
Revision / environment / observed path / time window:
Verified: criterion -> command, discovered test/assertion, result and artifact
Source-inspected only: criterion -> file:line and limits
Unverified: criterion -> missing evidence, blocked hop and next action
Delivery: implemented / verified / merged / deployed (state each separately)
```

- Use independent acceptance oracles and required fail-to-pass or controlled-mutation
  evidence; never infer these from coverage or a green suite. TDD is optional unless required.
- Tests pass only when actually run after the relevant edit. Confirm discovery and
  assertions. Record relevant scans and absent tools separately from failures.
- Kafka / DB-transaction / auth work requires real integration evidence. Cross-service
  and device paths require the affected real chain; UI needs the interaction result.
  Mocked browser APIs prove frontend flow only. Missing required gates stay unverified.
- For irreversible behavior, require safe E2E before merge or the owner's explicit
  acceptance of the named gap; neither authorizes a production mutation.
- Check the actual diff when an agent claims edits. Partial completion is valid;
  do not silently drop criteria. Source inspection is not runtime proof.
- Reconcile authorized audit/tasks/changelog/PR/tracker records and read back remote
  changes. Retain dated corrections and blocked next actions; this grants no authority
  to publish, message, merge or deploy.
