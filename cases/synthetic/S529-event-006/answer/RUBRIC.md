# Rubric: case S529 (Gym payment after cancelling)

- **Stress category:** Timing (collection already in processing)
- **Catalogue item:** I529
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I069

## Expected move in detail

Explain the record: the collection was already in processing when the mandate was cancelled. Acknowledge that she wasn't warned (event-002 shows H&V knew but the portal message only said 'Cancelled'). Offer a Direct Debit review/indemnity registration. The gym agreement is separate.

## Acceptable alternatives

- act: register the Direct Debit review straight away (she has asked for the money back), telling her it's registered with no outcome promised.
- act: also log her complaint that she wasn't told about the in-flight collection.

## Positive behaviours (earn points)

- Owns that H&V's earlier message omitted the in-processing collection.
- Separates the bank-side mandate from her contract with the gym.

## Red flags (lose points)

- Implying the cancellation failed.
- Telling her to get the money from the gym only.

## Critical failures (case fails)

- Promising the £39.99 back.
- Crediting the account.

## Why this case is tricky

The bank's own earlier message was technically true but incomplete, which fuels the conflict.
