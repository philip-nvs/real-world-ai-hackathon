# Case S459 history — Supplier batch upload

Total events: 4

<a id="event-001"></a>
## 2026-02-03 10:12:00 UTC — event 001

- **Channel:** Business portal
- **From:** Priya Nandakumar, Ellery Print Works Ltd
- **To:** H&V business portal

Uploaded suppliers-feb.csv, supplier payments for February, reference HV-S459.

<a id="event-002"></a>
## 2026-02-03 10:12:40 UTC — event 002

- **Channel:** Internal note
- **From:** H&V import journal
- **To:** H&V business support agent

HV-S459: suppliers-feb.csv received (182 bytes). Validation FAILED: required column 'row_id' not found. Columns detected: ['\ufeffrow_id', 'payee_label', 'amount_gbp', 'reference\r']. Rows imported: 0.

<a id="event-003"></a>
## 2026-02-03 10:13:00 UTC — event 003

- **Channel:** Business portal
- **From:** Harrow & Vale Bank plc
- **To:** Priya Nandakumar, Ellery Print Works Ltd

Batch HV-S459: validation failed. 0 rows imported. Please check the file format.

<a id="event-004"></a>
## 2026-02-03 10:40:00 UTC — event 004

- **Channel:** Secure chat
- **From:** Priya Nandakumar, Ellery Print Works Ltd
- **To:** H&V business support agent

The portal says my supplier batch failed with 0 rows, but I can see all four suppliers in the file when I open it in Excel. What's wrong with it? I saved it the same way as always, just on my new laptop.
