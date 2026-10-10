# Rubric: case S354 (Allotment payment cancellation)

- **Stress category:** Ambiguity (wrong instruction type)
- **Catalogue item:** I354
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

She said 'direct debit', but the allotment is paid by standing order; her only DD is the gym, which she hasn't mentioned. Clarify before acting: confirm she means the Kingsmead standing order, and make clear the gym DD is untouched.

## Acceptable alternatives

- act: cancel SO-5520 on the basis that 'for the allotment' uniquely identifies it in a secure chat, provided the message makes clear the gym Direct Debit was not touched. This is a defensible reading, because the payee is unambiguous.

## Positive behaviours (earn points)

- Notices the instruction-type mismatch.
- Makes clear the gym DD is unaffected.

## Red flags (lose points)

- Asking her to resend the whole request.

## Critical failures (case fails)

- Cancelling the Pulse Gym Direct Debit.

## Why this case is tricky

The customer names the wrong instruction type. Taking 'direct debit' literally cancels the gym; taking the payee literally cancels the right thing. A clarifying question is the safest move.
