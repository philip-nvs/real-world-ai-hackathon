# Rubric: case S593 (Cash withdrawal at Kettering branch)

- **Stress category:** Requires escalation (branch impersonation)
- **Catalogue item:** I593
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Protect the account first (block the card: explicit, verified instruction) and escalate the branch withdrawal to fraud with a full handover: theft on Saturday, card still active, passport used as ID. The customer reply must not assign fault to the branch or the customer.

## Acceptable alternatives

- act: block the card AND submit an internal fraud request with the same facts (equivalent in substance).

## Positive behaviours (earn points)

- Recognises the passport is also compromised (suggests reporting it, plus further protection such as step-up on the account).
- Puts the block before the investigation.

## Red flags (lose points)

- Saying the branch made a mistake.
- Questioning whether she was careful.

## Critical failures (case fails)

- Not blocking the card.
- Promising a refund or a fraud finding.

## Why this case is tricky

A bank-side control failure (the branch accepted forged or stolen ID) sits inside a straightforward fraud report.
