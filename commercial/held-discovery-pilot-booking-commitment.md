# Held discovery → paid pilot booking commitment (blank Actuals)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use when:** interview grid Status is **`Held`** and the session was a **qualified** lead-ICP discovery (same rules as the week tracker)  
**Lead gap:** pilot conversion — held qualified discovery → written interest + kickoff booked (vs SharePoint status quo / tender-AI wrong-axis; scorecard Paid pilots still empty)  
**Companions:** [`../research/qualified-discovery-week-tracker.md`](../research/qualified-discovery-week-tracker.md) · [`../research/discovery-pilot-offer-bridge.md`](../research/discovery-pilot-offer-bridge.md) · [`crm-stage-scripts.md`](crm-stage-scripts.md) · [`pilot-offer-email.md`](pilot-offer-email.md) · [`pilot-offer-sheet.md`](pilot-offer-sheet.md) · [`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md) · [`../operations/pilot-kickoff-checklist.md`](../operations/pilot-kickoff-checklist.md) · [`../operations/pilot-fee-waiver-log.md`](../operations/pilot-fee-waiver-log.md) · [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md) · [`../research/interview-synthesis.md`](../research/interview-synthesis.md) · soft decline → [`referral-ask-script.md`](referral-ask-script.md)  
**Pre-held only:** discovery slot booking → [`reply-booking-scripts.md`](reply-booking-scripts.md) (not this checklist)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** held discoveries and real offer/kickoff events.  
**Do not** invent INT/OBS ids, offers sent, fees, kickoff dates, CRM `Pilot` stage, or scorecard Paid pilots in git. Prefer anonymised CRM ids.

## Goal

Same-day densification after a **held** discovery: log the held, run the bridge, send Script A or B per legal gate, capture **written** interest and/or **book the kickoff slot** — without treating “sounds interesting” as Pilot or inventing Actuals.

## Preconditions

| Check | Rule |
|-------|------|
| Held + qualified | Grid `Held`; lead ICP (AME / marine / fab) — not anti-persona / reserve as a win |
| Synthesis | Capture notes → [`../research/interview-synthesis.md`](../research/interview-synthesis.md); follow bridge, do not invent pain |
| Legal gate | [`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md) **PASS** for Script A; else Script B + `pilot_offer_held_legal` |
| Not cold | Never send Script A from Week packs alone ([`../research/discovery-pilot-offer-bridge.md`](../research/discovery-pilot-offer-bridge.md) hard stop) |

## Sequence (compose with bridge — do not duplicate it)

1. **Held logged** — Confirm grid `Held`; row on [`../research/qualified-discovery-week-tracker.md`](../research/qualified-discovery-week-tracker.md); CRM `notes` `int={{INT-ID}}` ([`crm-stage-scripts.md`](crm-stage-scripts.md) Transition B).  
2. **Bridge** — Run [`../research/discovery-pilot-offer-bridge.md`](../research/discovery-pilot-offer-bridge.md) capture → synthesis → offer decision (pain fit / ICP).  
3. **Gate** — Confirm legal readiness. PASS → Script A ([`pilot-offer-email.md`](pilot-offer-email.md) + [`pilot-offer-sheet.md`](pilot-offer-sheet.md)); FAIL/pending → Script B; tag `pilot_offer_sent` or `pilot_offer_held_legal`.  
4. **Commitment** — On **written** interest: tag `pilot_offer_accepted`; book kickoff call; move to `Pilot` only when kickoff is **in motion** (Transition C). Verbal “sounds interesting” alone → stay Discovery.  
5. **Hand-off** — Kickoff execution → [`../operations/pilot-kickoff-checklist.md`](../operations/pilot-kickoff-checklist.md); fee → [`../operations/pilot-fee-waiver-log.md`](../operations/pilot-fee-waiver-log.md). Soft decline → [`referral-ask-script.md`](referral-ask-script.md).  
6. **Scorecard** — Offer send ≠ Paid pilots Actual. Paid pilots only after real Path B kickoff + live pack path.

## Commitment log (blank until real)

| CRM id | INT id | Offer script (A/B/—) | Gate PASS? | Offer sent date | Written interest (Y/N/blank) | Kickoff booked (Y/N/blank) | Fee status | Logged by | Notes |
|--------|--------|----------------------|------------|-----------------|------------------------------|----------------------------|------------|-----------|-------|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Held → offer sent | 0 |
| Held → written interest | 0 |
| Held → kickoff booked | 0 |

## Founder checklist

- [ ] Grid `Held` + week tracker row (qualified only)  
- [ ] `int=` + synthesis / bridge invoked  
- [ ] Legal gate checked — Script A only on PASS  
- [ ] CRM tags (`pilot_offer_sent` / `pilot_offer_held_legal` / `pilot_offer_accepted`) honest  
- [ ] Written interest before `Pilot` stage; kickoff slot booked when committed  
- [ ] Kickoff hand-off to checklist — this file does not replace it  
- [ ] Soft decline → one referral ask  
- [ ] No invented Actuals; no win-rate claims  

## Stop rules

- Never invent held interviews, offers, fees, or kickoffs.  
- Never send Script A on uncleared MSA/DPA.  
- Never mark CRM `Pilot` on verbal interest alone.  
- Offer send ≠ scorecard Paid pilots / interview Actual.  
- Never hard-sell SaaS or claim win-rate / qualification guarantees.  
- Soft decline → referral ask; do not harass.  
- Do not replace [`../research/discovery-pilot-offer-bridge.md`](../research/discovery-pilot-offer-bridge.md) — compose with it.
