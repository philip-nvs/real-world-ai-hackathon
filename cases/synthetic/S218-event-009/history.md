# Case S218 history — Return request for a payment to the wrong payee

Total events: 9

<a id="event-001"></a>
## 2026-02-18 10:00:00 UTC — event 001

- **Channel:** Verified call
- **From:** Tamsin Hale
- **To:** H&V service agent

Checks done. I sent £520 to the wrong saved payee yesterday, Hart Electrical instead of Hart Plumbing. Please ask for it back.

<a id="event-002"></a>
## 2026-02-18 10:10:00 UTC — event 002

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V payment team

Please register a return request for Tamsin Hale's £520.00 transfer PAY-80311 to Hart Electrical, payee selected in error (verified call, event 001). Case HV-S218.

<a id="event-003"></a>
## 2026-02-18 10:10:40 UTC — event 003

- **Channel:** Internal note
- **From:** H&V payment team system
- **To:** H&V service agent

Timeout: no response received (request ID RQ-1188).

<a id="event-004"></a>
## 2026-02-18 10:12:00 UTC — event 004

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V payment team

Retrying the return request registration for PAY-80311.

<a id="event-005"></a>
## 2026-02-18 10:12:20 UTC — event 005

- **Channel:** Internal note
- **From:** H&V payment team
- **To:** H&V service agent

Return request registered: HV-S218-2 for PAY-80311.

<a id="event-006"></a>
## 2026-02-18 10:13:00 UTC — event 006

- **Channel:** Internal note
- **From:** H&V payment team
- **To:** H&V service agent

Return request registered: HV-S218 for PAY-80311 (request RQ-1188, delayed confirmation).

<a id="event-007"></a>
## 2026-02-18 10:30:00 UTC — event 007

- **Channel:** Secure portal
- **From:** H&V payment team
- **To:** Tamsin Hale

Return request registered: HV-S218.

<a id="event-008"></a>
## 2026-02-18 10:31:00 UTC — event 008

- **Channel:** Secure portal
- **From:** H&V payment team
- **To:** Tamsin Hale

Return request registered: HV-S218-2.

<a id="event-009"></a>
## 2026-02-18 11:00:00 UTC — event 009

- **Channel:** Secure chat
- **From:** Tamsin Hale
- **To:** H&V service agent

Why have I got two return requests? Have you now asked for £1,040 back? I only sent £520 once.
