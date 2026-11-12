# Pilot support-burden log (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** each live pack metrics row (or weekly Friday rollup)  
**Scorecard:** [`../research/validation-scorecard.md`](../research/validation-scorecard.md) Support effort (&lt;45 min/customer/mo)  
**Week-8 gate:** [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md)  
**Source metrics:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) · ritual: [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Minutes contrast (separate):** [`minutes-saved-contrast-rollup.md`](minutes-saved-contrast-rollup.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** live pilot support minutes.  
**Do not** invent support minutes, customer names, or scorecard Actuals in git. Prefer anonymised IDs; keep sensitive detail on the local encrypted path.

## Goal

Monthly per-customer rollup of founder/operator **support minutes** so Support effort can be judged honestly against &lt;45 min/customer/mo — without treating dry-run CSV zeros as proof.

## Rules

1. Fill a row only from **live** metrics (`mode=live`) — sum `support_minutes` for that customer in the calendar month.  
2. Dry-runs (DRY-00x) are **not** Support-effort Actuals — never copy their `support_minutes` into this log as GO evidence.  
3. Include customer-facing chase (MISSING queue replies, Approver coaching, evidence chase) that you logged as support — not drafting wall-clock already in `minutes_to_first_draft`.  
4. Scorecard Support effort Actual updates **only** from real rows here (leave Actual blank/`—` until then).  
5. At Week-8: copy monthly totals into the gate checklist Support effort field.

## Log (blank until real)

| Customer (or anonymised) | CRM id | Month (YYYY-MM) | Pack ids (live) | support_minutes (sum) | Source (`metrics` / local notes) | Logged by | Notes |
|--------------------------|--------|-----------------|-----------------|------------------------|----------------------------------|-----------|-------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Customer-months logged | 0 |
| Customer-months under 45 min | 0 |
| Customer-months ≥45 min | 0 |

## Founder checklist

- [ ] After each live pack: ensure metrics CSV `support_minutes` is honest (or blank until known)  
- [ ] Weekly/Friday: roll live rows into a month row above (anonymised OK in git)  
- [ ] Compare month total to **&lt;45 min/customer/mo** threshold  
- [ ] Update scorecard Support effort Actual only from real tallies  
- [ ] At Week-8: paste outcome into [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md)  
- [ ] Do **not** invent minutes to pass the gate  

## Stop rules

- Never invent support minutes or scorecard Actuals.  
- Never treat DRY `support_minutes=0` as Support-effort proof.  
- Never commit confidential customer pack content with this log.  
- Support burden is operational load — not win-rate or qualification proof.
