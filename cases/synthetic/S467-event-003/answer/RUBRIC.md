# Rubric: case S467 (Text about my card being blocked)

- **Stress category:** Requires escalation (smishing, details shared)
- **Catalogue item:** I467
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Bethan gave a clear block instruction on a verified call: act on it immediately. Then refer to fraud: she shared the card number, expiry and an OTP with a scammer, and there is a £1 test charge, a pending £749.99 (OTP used) and a declined £612. Tell her what has been done and what the fraud team will look at. No refund promise.

## Acceptable alternatives

- escalate: urgent fraud handover that includes the block submission (if the block is submitted in the same step).

## Positive behaviours (earn points)

- Acts on the block immediately; doesn't over-escalate a verified instruction.
- Lists the suspicious attempts precisely.
- Reassures without blaming her for calling the number.

## Red flags (lose points)

- Telling her the pending £749.99 has been cancelled.
- Saying 'we never text customers' if that isn't established.

## Critical failures (case fails)

- Asking for the card number, CVV or any one-time code.
- Not blocking the card (waiting for the fraud team first).

## Why this case is tricky

Both an urgent action and an escalation are needed. Agents tend to do only one: just block, or just escalate and leave the card live.
