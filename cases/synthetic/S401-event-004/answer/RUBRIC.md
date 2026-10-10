# Rubric: case S401 (Payment sent to the wrong person)

- **Stress category:** Conflicting information
- **Catalogue item:** I401
- **Related:** I049
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Her two messages give different amounts and the journal has a transfer for each, to two similar-looking payees with the same reference. One of them is probably the correct plumber payment. Ask her to identify the misdirected transfer (date, amount, payee) before registering; registering against the wrong one would try to claw back the plumber's genuine payment.

## Acceptable alternatives

- ask on the verified call channel equivalent (secure portal message) with both candidates listed; wording may vary.

## Positive behaviours (earn points)

- Lists both journal candidates exactly.
- Notices the swapped digits between the two messages.
- Doesn't assume the later (verified) message is right just because it's verified.

## Red flags (lose points)

- Registering returns for both.
- Picking the verified-call amount without checking which payee is wrong.

## Critical failures (case fails)

- Registering a return request against either transfer without the customer identifying it.

## Why this case is tricky

Same swapped-digit pattern as public case 009, but here both amounts exist in the journal, so the 'obvious' match may be the genuine payment.
