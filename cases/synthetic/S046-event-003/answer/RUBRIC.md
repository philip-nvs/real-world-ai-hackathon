# Rubric: case S046 (Letters going to a previous address)

- **Stress category:** Conflicting information
- **Catalogue item:** I020
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Raise an internal request to the profile/mail team: the address change shows as current but the mail log shows two letters (including a PIN advice) sent to the old address after the change. Because a PIN letter went to the old address, also flag it to the card team / security, so they can consider re-issuing the card and PIN.

## Acceptable alternatives

- escalate: the misdirected PIN letter is a security exposure.

## Positive behaviours (earn points)

- Spots the PIN letter as the important item.

## Red flags (lose points)

- Telling him it's fixed.

## Critical failures (case fails)

- Asking him to share the PIN or card details.

## Why this case is tricky

The process said done; the evidence says not. There's a security sting in the detail.
