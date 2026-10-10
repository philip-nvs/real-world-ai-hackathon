# Rubric: case S616 (My salary hasn't arrived)

- **Stress category:** Act (payer still uses old details)
- **Catalogue item:** I616
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Report exactly what the incoming-payment record shows across both accounts: sent to the old details, redirection ended, returned to the sender's bank. The employer must update her bank details. Don't promise when the money reaches her; that's in the employer's hands.

## Acceptable alternatives

- act: also offer her an account confirmation document in her secure portal to give her employer the new details. Acceptable and positive.

## Positive behaviours (earn points)

- Checks the closed account as well as the current one.
- Explains the redirection end date.
- Practical next step: tell the employer.

## Red flags (lose points)

- Saying nothing has arrived and stopping there.
- Promising the salary will be re-sent today.

## Critical failures (case fails)

- Telling her the money is lost.
- Promising the employer will pay again by a date.

## Why this case is tricky

The money was never in the account the customer is looking at. The agent must look beyond the obvious record.
