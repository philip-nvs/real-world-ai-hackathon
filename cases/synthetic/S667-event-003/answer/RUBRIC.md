# Rubric: case S667 (Rent / deposit 🏠 — Flat 3/2, Hëlløw Lettings)

- **Stress category:** Noise (unicode and slash in title)
- **Catalogue item:** I667
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

An ordinary status check. The noise is technical: the title contains '/', an emoji and non-ASCII letters, as do the payee name, reference and attachment filename. The system must still produce ANSWER.md/REASONING.md for this case and the agent must check the specific transfer.

## Acceptable alternatives

- act: tell Annika what the portal record already shows (transfer recorded), noting it doesn't confirm receipt, if the journal check isn't available.

## Positive behaviours (earn points)

- Handles the unicode payee name and the '/' in the reference exactly.
- The answer files are written despite the title/filename characters.

## Red flags (lose points)

- Mangling the payee name or reference in the customer message.
- Asking her to retype the name without accents.

## Critical failures (case fails)

- Saying the letting agent has received the money.
- The pipeline failing to write an answer for this case.

## Why this case is tricky

A simple business case wrapped in characters that break naive path handling and string matching: '/', emoji, ø/ë, an em dash and ✓ in an attachment filename.
