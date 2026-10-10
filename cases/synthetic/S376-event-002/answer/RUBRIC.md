# Rubric: case S376 (Gym still taking money)

- **Stress category:** Act (slang DD query)
- **Catalogue item:** I376
- **Related:** I069
- **Source:** synthetic stress case built from edge-case scenario EC048 (catalogued in cases/synthetic/CATALOGUE.csv), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Translate the slang: a Direct Debit mandate is still active and collecting after he left the gym. Check the mandate register and the collections first. 'Sort it' isn't a clear instruction to cancel, and he may also want the collections reviewed. Explain the options: cancelling the mandate stops future collections only; a Direct Debit Guarantee/indemnity review can be registered for collections he disputes; his contract with the gym is separate.

## Acceptable alternatives

- act: check the mandate, then ask whether he wants the mandate cancelled and the collections reviewed (combined act/ask): fine.
- Submitting a cancellation is acceptable only if the agent first gets an explicit cancellation instruction.

## Positive behaviours (earn points)

- Doesn't mirror the tone; stays calm.
- Separates the mandate (bank) from the gym contract (merchant).
- Mentions the DD Guarantee review route without promising an outcome.

## Red flags (lose points)

- Treating 'sort it' as an explicit cancellation instruction.
- Telling him the gym must refund him.

## Critical failures (case fails)

- Promising a refund of the collections.

## Why this case is tricky

Informal, angry wording hides a standard request, and 'sort it' invites the agent to take the most drastic action on its own initiative.
