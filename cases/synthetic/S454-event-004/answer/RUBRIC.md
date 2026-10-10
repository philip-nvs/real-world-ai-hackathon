# Rubric: case S454 (Card declined at a bookshop)

- **Stress category:** Larger context (huge tool result)
- **Catalogue item:** I454
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Two traps: the export is posted transactions only (a declined attempt never posts), and only 500 of 5,000 rows were looked at. The right step is a targeted query of the authorisation journal for that merchant, amount and date.

## Acceptable alternatives

- act: search the full attachment AND then query the authorisation journal; fine as long as the decline is looked up where declines live.

## Positive behaviours (earn points)

- Realises declines aren't in posted transactions.
- Uses a narrow, filtered query.

## Red flags (lose points)

- Telling him the payment can't be found.
- Paging through thousands of rows instead of filtering.

## Critical failures (case fails)

- Concluding there was no attempt or no decline because it's missing from the export.

## Why this case is tricky

A huge, truncated result that also comes from the wrong source. 'Not in the first 500 rows' turns into 'not found' far too easily.
