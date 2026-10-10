# Rubric: case S172 (School fees payment date)

- **Stress category:** Larger context
- **Catalogue item:** I169
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Explain from the records: the payment executed at 23:05 UTC on 31 March, which is 00:05 on 1 April UK time (BST since 30 March), exactly as scheduled. The export shows UTC dates. H&V can't speak for how the school will treat it.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Saying it went a day early.
- Promising the school will accept it.

## Why this case is tricky

Time-zone reasoning around the clocks change.
