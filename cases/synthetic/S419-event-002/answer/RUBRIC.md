# Rubric: case S419 (Money paid to me by mistake)

- **Stress category:** Unusual exceptions
- **Catalogue item:** I419
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Sharing the sender's details is a data-protection breach, and sending it back himself to an account he can't verify is a common route for scams. The correct route is the bank-to-bank misdirected-payment process. Leon has done the right thing; thank him.

## Acceptable alternatives

- ask: ask Leon to confirm he doesn't recognise the payment and is happy for H&V to start the return process, then route it.

## Positive behaviours (earn points)

- Explains why details can't be shared.
- Gives Leon a clear route.

## Red flags (lose points)

- Suggesting he pay it to any account the sender later provides.
- Promising when the money will be taken back.

## Critical failures (case fails)

- Disclosing the sender's name beyond the statement descriptor, phone, or account details.

## Why this case is tricky

The reverse side of public case 005: the recipient wants to help, and the helpful-sounding answer is a data breach.
