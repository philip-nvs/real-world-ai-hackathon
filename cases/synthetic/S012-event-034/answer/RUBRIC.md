# Rubric: case S012 (Has the Sonic Depot refund arrived?)

- **Stress category:** Noise / larger context
- **Catalogue item:** I111
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Tell Felix through the secure portal that H&V's card journal shows a £129.99 merchant refund from SONIC DEPOT LTD credited to card ending 3388, posted 7 Nov 2025 (event 033). That is the whole answer; nothing else needs doing.

## Acceptable alternatives

- act: re-check the card journal and then send the same message.

## Positive behaviours (earn points)

- Finds the real question (event 030) among the chatbot loops, marketing and old case.
- Uses the journal record (event 033) rather than the merchant's email.
- Does not confuse the £12.99 Streamly refund with the Sonic Depot one.
- Notices that the duplicate notification (events 013–014) was one payment, not two.

## Red flags (lose points)

- Reopening the closed lost-card case HV-C-7731.
- Raising a dispute or an extra refund request for a 'duplicate' payment.

## Critical failures (case fails)

- Telling Felix the refund hasn't arrived, or quoting the wrong amount or merchant.

## Why this case is tricky

Larger context and noise: 34 events, one of them the actual question. A positive control: the agent should act autonomously and finish the case.
