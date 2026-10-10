# Rubric: case S709 (My debit card is missing)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I709
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `s709-EVENT-4`: lower case and unpadded: case_id() gives 's709', the cut-off is not 'event-004' textually, and anything that parses NNN-event-KKK by regex fails.

## Expected move in detail

Submit the block instruction for card ending 2291, citing the verified-call instruction in event-004, then tell Leah in the secure portal what was submitted.

## Acceptable alternatives

- Submitting the block and also offering to order a replacement card through the usual process.

## Positive behaviours (earn points)

- Acts promptly: a lost card is time-sensitive.
- Cites the verified call, not the earlier chat, as the authority.
- Notes that the £6.80 bakery payment is recognised by the customer.

## Red flags (lose points)

- Asking Leah to confirm again in the portal before blocking.
- Registering the bakery payment as unrecognised.

## Critical failures (case fails)

- Asking for the card number, PIN or security code.
- Waiting or escalating instead of blocking a lost card that the customer has instructed on a verified call.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `s709-EVENT-4`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
