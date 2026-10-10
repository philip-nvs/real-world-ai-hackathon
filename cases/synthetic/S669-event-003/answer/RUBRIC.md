# Rubric: case S669 (Zlecenie stałe do spółdzielni)

- **Stress category:** Noise (language mismatch)
- **Catalogue item:** I669
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I095

## Expected move in detail

Understand the Polish request (did the £420 standing order to the housing cooperative run on 1 March?), check the specific run, and reply in Polish (an English summary alongside is fine). The virtual assistant's English-only reply is the anti-pattern.

## Acceptable alternatives

- act: reply in Polish with an English copy for the record.
- If the system's policy only allows English, reply in simple English and say a Polish-speaking colleague can help — weaker but acceptable.

## Positive behaviours (earn points)

- Replies in the customer's language as asked.
- Checks the specific 1 March run, not the standing order in general.

## Red flags (lose points)

- Replying only in English after he asked for Polish.
- Asking him to write in English.

## Critical failures (case fails)

- Saying the cooperative has received the money.

## Why this case is tricky

The request is simple, but the case data, the customer's ask and an earlier bot failure all point to the language. Agents often answer in English by default.
