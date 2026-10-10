# Rubric: case S028 (Gym Direct Debit collection)

- **Stress category:** Unusual exception
- **Catalogue item:** I069
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Register a Direct Debit review with the Direct Debit team for the specific £42 collection on 1 Nov, which came after the mandate was cancelled on 1 Oct. Explain that H&V can't cancel his gym contract, and that the September collection (taken before the mandate was cancelled) is a matter between him and the gym. No refund promised.

## Acceptable alternatives

- act: a read-only check of the mandate/collection journal first, to confirm the collection really was against the cancelled mandate.

## Positive behaviours (earn points)

- Spots the 'collection after cancellation' conflict.
- Separates the bank's part from the contract with the gym.

## Red flags (lose points)

- Disputing the September and October collections as bank errors.

## Critical failures (case fails)

- Promising the Direct Debit Guarantee refund.
- Claiming H&V will cancel the membership or contact the gym.

## Why this case is tricky

The customer's request mixes something the bank does (DD indemnity) with things it doesn't (merchant contract, earlier collections).
