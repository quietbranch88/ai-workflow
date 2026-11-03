---
name: grill-me
description: Clarify consequential unresolved requirements after checking existing context; ask only necessary questions and continue independent work.
---

<!-- Canonical source: prompts/grill-me.md in the maintained ai-workflow repository.
     Record the installed source revision; preserve private overlays separately. -->

# Grill Me — interactive requirement clarification

Inspired by Matt Pocock's pattern. Resolve consequential unknowns using existing context first, then ask only what remains necessary.

## How to use

Read the request, prior decisions, repository contracts, and relevant task docs before asking. Use safe read-only inspection to resolve what the available evidence can answer. Use the dimensions below to identify consequential gaps, not as a mandatory questionnaire. Continue independent work while waiting and defer only work that depends on a required answer.

## Proportional response

- **Direct execution** — when the request is clear, bounded, and reversible, and its target and verification are known. State material routine assumptions and proceed without a card.
- **Compact alignment card** — when plausible interpretations would materially change the outcome, scope, risk, authorization, or acceptance, or when the user asks for plan-first work. Do not trigger it merely because a chat or follow-up is new.

Keep the card to one screen and propose specifics instead of returning open-ended homework:

- **Goal** — who needs what outcome or decision.
- **Done / evidence** — observable result and how it will be checked.
- **Scope / non-goals** — included boundaries and deliberate exclusions.
- **Approach** — the smallest useful method, including a relevant borrowed practice when it adds value.
- **Agent assumptions** — reversible choices the agent proposes to make.
- **User decisions** — at most two consequential unresolved choices, each with a recommendation; write `None` when there are none.

Stop only when a decision can change the result, authorization, or data-loss boundary, or when the user explicitly requested plan-first work. Otherwise state assumptions and proceed; there is no mandatory confirmation round or required literal `start`.

### Dimensions to consider (skip irrelevant or already resolved items)

1. **Scope boundary**
   - What is in scope vs. out of scope?
   - What's the smallest version that delivers value?

2. **Inputs & validation**
   - What inputs are accepted? Format, size, character set?
   - Empty input behavior?
   - Oversized input behavior?
   - Malformed input behavior?

3. **Outputs & failure modes**
   - Success response shape?
   - Error response shape? Which error codes?
   - What does the caller see when downstream fails?

4. **State & persistence**
   - Stateless or stateful?
   - If stateful: where, retention policy, consistency requirements?

5. **Concurrency**
   - Is this called concurrently? From how many sources?
   - Idempotent on retry?
   - Rate limit considerations?

6. **Auth & authorization**
   - Who can call this? How are they authenticated?
   - Are there permission checks beyond authentication?

7. **Observability**
   - What should be logged? At what level?
   - What metrics should this emit?
   - What alerts should fire on failure?

8. **Downstream dependencies**
   - What external services / DBs does this hit?
   - What are their SLAs and failure modes?
   - Circuit breaker / retry strategy?

## Rules

- Ask at most two unresolved questions total in a card and no more than ONE question per dimension — don't sprawl
- Phrase as "Do you want X or Y?" when possible, not open-ended
- For routine implementation choices, use existing contracts and state any material assumption. Do not guess consequential product, authorization, or data-loss decisions.
- Summarize resolved decisions when useful; do not repeat an approval already given.
- If no consequential unknown remains, proceed. There is no question quota or mandatory interview phase.

## When NOT to grill

Skip clarification in these cases only if no consequential unknown remains. A
reproduction or planner checklist does not resolve missing product or authorization
decisions by itself.

- Trivial requests ("rename this variable")
- Bug fixes with a clear reproduction. The reproduction is not the acceptance contract; name the original goal. "Tests pass" can be true while that goal is unmet.
- Tasks already broken down by a planner
