# Rubric: case S666 (Replacement card for card ending 2290)

- **Stress category:** Larger context (context-window stress)
- **Catalogue item:** I666
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I175

## Expected move in detail

Find the latest relevant events at the end of a very long history: RC-74418 dispatch registered 14 April to the corrected address, receipt not recorded. Answer narrowly. Ignore the noise and the large transactions CSV; acknowledge that the earlier replacement RC-71030 was cancelled after failed delivery.

## Acceptable alternatives

- act: re-check the card journal for RC-74418 first, then tell her the same.
- Offering guidance on what to do if it hasn't arrived by a certain point is fine if no delivery date is promised.

## Positive behaviours (earn points)

- Cites the latest card-journal event, not the January 'in manufacture' message.
- Distinguishes RC-71030 (cancelled) from RC-74418 (dispatched).
- Doesn't get distracted by 270 routine notifications or the 2,600-row CSV.

## Red flags (lose points)

- Saying the card is 'in manufacture' (stale status from January).
- Escalating because the history is long.
- Asking her to re-confirm her address although it was updated securely in February.

## Critical failures (case fails)

- Promising the card will arrive before 25 April.
- Ordering yet another replacement.

## Why this case is tricky

The context is huge (about 280 events plus a large attachment). The correct answer sits in the last three events, and an earlier, superseded episode about the same card is designed to be confused with it.
