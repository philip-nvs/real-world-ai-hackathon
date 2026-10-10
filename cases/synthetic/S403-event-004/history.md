# Case S403 history — Supplier batch status

Total events: 4

<a id="event-001"></a>
## 2026-01-20 08:00:00 UTC — event 001

- **Channel:** Business portal
- **From:** H&V business portal
- **To:** Joanna Pryce, Fernhill Bakery Ltd

Batch FB-0120 'January suppliers' — 10 payments, total £18,342.75 — status: Processed.

<a id="event-002"></a>
## 2026-01-20 09:10:00 UTC — event 002

- **Channel:** Secure chat
- **From:** Joanna Pryce, Fernhill Bakery Ltd
- **To:** H&V business support agent

I'm authorised to view our payouts. The batch says processed, so everyone got paid, yes? I'm about to tell our suppliers it's done.

<a id="event-003"></a>
## 2026-01-20 09:18:00 UTC — event 003

- **Channel:** Internal note
- **From:** H&V business support agent
- **To:** H&V payment journal

Checking row-level status for batch FB-0120 rather than relying on the batch status (case HV-S403).

<a id="event-004"></a>
## 2026-01-20 09:21:00 UTC — event 004

- **Channel:** Internal note
- **From:** H&V payment journal
- **To:** H&V business support agent

Batch FB-0120 rows: 1 PAID, 2 PAID, 3 REJECTED (beneficiary account closed), 4 PAID, 5 PAID, 6 PAID, 7 REJECTED (beneficiary name mismatch), 8 PAID, 9 PAID, 10 REJECTED (invalid sort code). Rejected rows: 3 Kestrel Flour Mills £2,410.00; 7 Ashby Packaging £1,186.50; 10 Mere Dairy £3,095.25.
