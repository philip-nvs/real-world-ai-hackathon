# Rubric: case S110 (Glide Shoes refund)

- **Stress category:** Ambiguity
- **Catalogue item:** I097
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Ask Tom what happened: has Glide Shoes agreed a refund that hasn't arrived (H&V can check), or is there a problem with the order he wants to dispute (H&V can register a card dispute)? H&V doesn't refund merchant purchases itself.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Promising a refund.
- Opening a dispute by default.

## Why this case is tricky

Two possible intents with different processes.
