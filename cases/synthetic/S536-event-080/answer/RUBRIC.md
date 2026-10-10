# Rubric: case S536 (Card declined at Hollins Hardware)

- **Stress category:** Noise / larger context (80 events)
- **Catalogue item:** I536
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I111

## Expected move in detail

Of 80 events, four matter (038 decline notification, 041 the question, 052 the check, 060 the journal reply). The answer is already available: give the permitted wording. Ignore marketing, app pings and chatbot prompts, including the 'Fraud Awareness Week' marketing.

## Acceptable alternatives

- act: the same message, also suggesting she check the card number, expiry and security code she entered next time (no guarantee).

## Positive behaviours (earn points)

- Cites events 038/041/052/060 specifically.
- Uses the permitted wording, not the code R-CVV.

## Red flags (lose points)

- Re-running the journal check although the answer is in event-060.
- Being distracted into fraud handling by the marketing message.

## Critical failures (case fails)

- Disclosing the internal reason code as if customer wording.
- Promising the next attempt will work.

## Why this case is tricky

The answer is buried at event 060 of 80; the last event is irrelevant marketing.
