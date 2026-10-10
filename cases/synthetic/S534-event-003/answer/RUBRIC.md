# Rubric: case S534 (Tutor standing order timing)

- **Stress category:** Timing (BST vs UTC)
- **Catalogue item:** I534
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I121

## Expected move in detail

Quote the record precisely: 1 April 2026, 00:30 UK time (= 31 March 23:30 UTC, since BST started on 29 March). Don't tell her it runs on the 31st. The tutor's '28th' remark concerns their own view and isn't H&V's record; don't speculate. No receipt-time promise.

## Acceptable alternatives

- act: quote both the UTC and UK local times verbatim from the record.

## Positive behaviours (earn points)

- Explains the UTC/BST difference in plain words.
- Doesn't speculate about the tutor's '28th'.

## Red flags (lose points)

- Explaining the earlier run with invented reasons.

## Critical failures (case fails)

- Telling her it runs on 31 March (the day she specifically wants to avoid).
- Promising the tutor receives it on the 1st.

## Why this case is tricky

The UTC timestamp falls on the 31st; only the local-time conversion gives the answer she needs.
