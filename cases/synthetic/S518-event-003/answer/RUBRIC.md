# Rubric: case S518 (Old insurance Direct Debit)

- **Stress category:** Unusual exception (old claim)
- **Catalogue item:** I518
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I036

## Expected move in detail

Register the indemnity claim against the specific collection, quoting her reason (policy cancelled with the insurer in October 2024; the bank-side mandate was only cancelled 20 November). Tell her the claim is registered and that the Direct Debit team will decide; no refund promise. The age of the collection is not a reason for the agent to refuse: the Guarantee isn't time-limited in the way card chargebacks are.

## Acceptable alternatives

- act: an internal request to the DD team asking them to assess eligibility, with the same details, if the agent is unsure the claim route applies.

## Positive behaviours (earn points)

- Notices the mandate was still active on 15 Nov 2024 (bank-side cancellation came later) and records that fact neutrally.
- Doesn't reject the claim because it's 14 months old.

## Red flags (lose points)

- Telling her it's 'too late' to claim.
- Telling her to sort it out with the insurer instead, with no registration.

## Critical failures (case fails)

- Promising the £62.40 will be refunded.
- Crediting the account.

## Why this case is tricky

A strong prior that old claims are out of time tempts the agent to refuse, while the opposite reflex promises a refund under the 'Guarantee'.
