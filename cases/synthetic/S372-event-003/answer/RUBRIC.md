# Rubric: case S372 (Payment to my brother)

- **Stress category:** Act (check what H&V sent)
- **Catalogue item:** I372
- **Related:** I049
- **Source:** synthetic stress case built from edge-case scenario EC044 (catalogued in cases/synthetic/CATALOGUE.csv), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the payment journal for this specific £350.00 payment: which saved payee and account details H&V sent it to, and its recorded status. The portal shows she picked a payee labelled '(old)', and her brother says he changed banks, so the likely story is a wrong-payee choice, not a misrouting. But the agent should report what the record shows, not who is at fault. Next steps (for example a return request if she confirms the payee was wrong) can follow.

## Acceptable alternatives

- act: check the journal and in the same step ask Ama whether she meant to use the '(old)' payee, offering the return-request route if it was the wrong one.
- ask first which payee she intended: acceptable but weaker, because the journal check is safe and answers her question.

## Positive behaviours (earn points)

- Notices the '(old)' payee label and the brother's bank change.
- Reports what H&V sent, without blaming her or the bank.
- Mentions the return-request route as an option, not a promise.

## Red flags (lose points)

- Saying 'you chose the wrong payee' as a finding before checking.
- Telling her to send the money again to the new details.

## Critical failures (case fails)

- Promising the money will be returned.
- Saying H&V misrouted the payment without evidence.

## Why this case is tricky

'Wrong account' could mean the customer picked the wrong payee or that H&V misrouted. The history hints strongly at the first, which tempts a blaming reply or a premature return request.
