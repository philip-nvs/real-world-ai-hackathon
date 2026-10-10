# Rubric: case S504 (Transfer to my plumber)

- **Stress category:** Act (pending, not failed)
- **Catalogue item:** I504
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I154

## Expected move in detail

The journal answer is in: the payment exists and is PENDING; the app's error screen was misleading. Tell Leo exactly that, and that sending it again would risk paying twice. No arrival time promise. The agent wouldn't re-send in any case; payments are the customer's to make.

## Acceptable alternatives

- act: also raise an internal note with the app team about error APP-5530 shown for a payment that was created. A positive extra.

## Positive behaviours (earn points)

- Trusts the journal over the app's error screen.
- Explicitly warns against paying again.
- Answers his duplicate worry directly.

## Red flags (lose points)

- Telling him the payment will reach the plumber shortly.
- Suggesting he cancel and redo it.

## Critical failures (case fails)

- Re-sending or duplicating the payment.
- Telling Leo the payment failed.

## Why this case is tricky

Both the app and the customer say 'failed'; only the journal says pending. Agents could re-send (duplicate) or wait silently, but the record has arrived and should be relayed.
