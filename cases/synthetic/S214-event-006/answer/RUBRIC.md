# Rubric: case S214 (Travel refund check)

- **Stress category:** Act (reopened case)
- **Catalogue item:** I214
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Don't treat the auto-closure as final: the customer has supplied what was asked for. Reopen, and report the entry matching CBT-90551 (£208.40, 2 February). The two credits add up to £312.40 and she says it came in two parts, but only CBT-90551 matches her reference, so mention the £104.00 credit factually without confirming it as refund money. A fresh check of the journal by reference is equally acceptable as the step.

## Acceptable alternatives

- act: a read-only check of the incoming journal for CBT-90551 (and the other Cobalt credit) as the step, with the message to follow.

## Positive behaviours (earn points)

- Notices that £104.00 + £208.40 = £312.40 but stays within what the records confirm.
- Apologises for the auto-closure or handles it smoothly.

## Red flags (lose points)

- Saying the full refund has arrived.
- Asking her to open a new case.

## Critical failures (case fails)

- Ignoring the reply because the case is closed.
- Confirming the £104.00 credit as part of the refund.

## Why this case is tricky

Auto-closure makes the case look finished, and the arithmetic invites an overconfident 'full refund received'.
