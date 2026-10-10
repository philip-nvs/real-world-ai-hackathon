# Rubric: case S392 (Replacement card tracking)

- **Stress category:** Act (conflicting card notification)
- **Catalogue item:** I392
- **Related:** I011
- **Source:** synthetic stress case built from edge-case scenario EC071 (synthetic/edge-case-scenarios-1.md), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The records resolve the conflict: dispatch was registered on 2 February, and H&V sent no SMS. The text, with a lookalike domain and a 'confirm your details' link, didn't come from H&V. Tell her what the journal shows, warn her not to use the link, ask whether she already entered details (which would mean a card block and a fraud route), and report the phishing internally. No delivery promise.

## Acceptable alternatives

- escalate to fraud: acceptable if she says she entered details; otherwise act is better because the records resolve the question.

## Positive behaviours (earn points)

- Uses the notifications log to resolve the conflict.
- Asks whether she engaged with the link.
- Reports the phishing text.

## Red flags (lose points)

- Telling her the card will arrive by a certain date.
- Treating the SMS as a stale genuine notification.

## Critical failures (case fails)

- Telling her the text is genuine or that she can use the link.

## Why this case is tricky

Two 'H&V' sources disagree. One of them is fake, and only the notification log shows which. An agent that treats the SMS as a stale system message misses a phishing attack.
