# Pilot continuation yes/no capture log (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** close-out script **D** — [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md)  
**Scorecard:** [`../research/validation-scorecard.md`](../research/validation-scorecard.md) Continuations (≥2) · Week-8 gate: [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md)  
**Design:** [`../research/pilot-design.md`](../research/pilot-design.md) · Offer: [`../commercial/pilot-offer-sheet.md`](../commercial/pilot-offer-sheet.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** written yes/no replies.  
**Do not** invent continuation decisions, customer names, or scorecard Actuals in git. Prefer anonymised IDs here; keep full emails on the local encrypted path only.

## Rules

1. Fill a row only after a **real** written yes/no to close-out **D** (email or signed note after results review).  
2. Status must be `yes`, `no`, or `pending` (awaiting reply after **D** sent).  
3. Dry-runs (DRY-00x) are **not** continuations — never copy them into this log.  
4. A `yes` does **not** authorise further confidential packs until solicitor-cleared continuation MSA/DPA.  
5. Scorecard Continuations Actual increments only from real `yes` rows (never invent; leave Actual at 0 until then).  
6. On `no` (or timeout → treat as stop): run close-out **E** per [`pilot-data-retention-schedule.md`](pilot-data-retention-schedule.md).

## Log (blank until real)

| Customer (or anonymised) | CRM id | Pilot window (start–end) | Results-review date | Decision (`yes` / `no` / `pending`) | Decision date | Channel (`email` / `call`) | Logged by | Notes |
|--------------------------|--------|--------------------------|---------------------|--------------------------------------|---------------|----------------------------|-----------|-------|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Rows with decision `yes` | 0 |
| Rows with decision `no` | 0 |
| Rows still `pending` | 0 |

## Founder checklist

- [ ] Send close-out **D** after results review  
- [ ] On reply: add row above (or local private copy if identity is sensitive)  
- [ ] If `yes`: arrange commercial outline + legal review before any further packs  
- [ ] If `no` / stop: run **E**; optional **G** referral ask (clean no only)  
- [ ] Update scorecard Continuations Actual only from real `yes` count  
- [ ] At Week-8 gate: copy tally into [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md)  

## Stop rules

- No invented yes/no or scorecard Continuations Actuals in the repo.  
- No uncleared MSA/DPA stubs as continuation contracts.  
- No win-rate or qualification claims tied to continuation.  
- Dry-run metrics ≠ continuation proof for GO.
