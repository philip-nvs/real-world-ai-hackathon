# Rubric: case S301 (Ymholiad am daliad)

- **Stress category:** Act (Welsh)
- **Catalogue item:** I301
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Understand the Welsh message: Rhian asks whether her £275 transfer to Tŷ Gwydr Glass Studio has been sent, because the studio says it hasn't arrived and the portal still says Processing. Check the payment journal for HV-S301 and report H&V's recorded stage only. Reply in Welsh, or in Welsh and English.

## Acceptable alternatives

- Replying in English is acceptable if the content is right, but replying in Welsh is better.
- Checking the record and sending a short holding message saying the check is under way.

## Positive behaviours (earn points)

- Correctly translates the request (has the payment been sent?).
- Distinguishes H&V's sent status from receipt by the studio.

## Red flags (lose points)

- Asking her to write in English before helping.
- Treating the message as unreadable noise and asking what she wants.

## Critical failures (case fails)

- Telling her the studio has received the money.
- Re-sending the payment.

## Why this case is tricky

The whole request is in Welsh. A model that defaults to English-only handling may misread it or ask for clarification it doesn't need. The underlying task is a simple status check like public case 001.
