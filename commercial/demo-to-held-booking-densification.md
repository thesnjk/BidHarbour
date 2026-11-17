# Discovery demo → held booking densification (blank Actuals)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use when:** a fixture **discovery demo** just finished ([`concierge-discovery-demo-runbook.md`](concierge-discovery-demo-runbook.md)) and the next step is not yet a **held** qualified discovery and/or booking-commitment path  
**Lead gap:** Repeatable acquisition densification — demo minutes → booked/held next step (fixture demo alone ≠ held interview or Paid pilots)  
**Companions:** [`concierge-discovery-demo-runbook.md`](concierge-discovery-demo-runbook.md) · [`held-discovery-pilot-booking-commitment.md`](held-discovery-pilot-booking-commitment.md) · [`reply-booking-scripts.md`](reply-booking-scripts.md) · [`discovery-noshow-rebook-checklist.md`](discovery-noshow-rebook-checklist.md) · [`../research/qualified-discovery-week-tracker.md`](../research/qualified-discovery-week-tracker.md) · [`../research/discovery-pilot-offer-bridge.md`](../research/discovery-pilot-offer-bridge.md) · [`crm-stage-scripts.md`](crm-stage-scripts.md) · [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md) · [`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** demos and real held/booking events.  
**Do not** invent demos, held interviews, offers, kickoffs, or scorecard Actuals in git. Prefer anonymised CRM ids.

## Goal

Same-day densification after a fixture discovery demo: log the demo, book or confirm a **held** discovery slot (or mark already Held if the call counted), then hand off to booking commitment — without treating the demo as proof or inventing Actuals.

## Preconditions

| Check | Rule |
|-------|------|
| Demo done | Fixture runbook completed (or aborted honestly) — not a SaaS tour |
| Lead ICP | AME / marine / fab — not anti-persona / reserve as a win |
| Not cold-only | Demo was booked research or clear pack-assembly pain — see demo runbook “When not to demo” |
| Legal | Script A / live packs only if [`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md) PASS |

## Sequence

1. **Log demo** — CRM stay `Discovery`; optional `notes=fixture_demo` ([`crm-stage-scripts.md`](crm-stage-scripts.md)). Do **not** credit scorecard Actuals from the fixture.  
2. **Next slot** — Same-day: book or confirm a discovery/interview follow-up via [`reply-booking-scripts.md`](reply-booking-scripts.md) (“yes / times”). Grid slot Open→Booked. If they already completed a **held** qualified discovery in this call, mark grid `Held` and skip to step 4.  
3. **If they flake** — Use [`discovery-noshow-rebook-checklist.md`](discovery-noshow-rebook-checklist.md) (one rebook; densify warm/referral — no new cold scrape).  
4. **On Held** — Run [`held-discovery-pilot-booking-commitment.md`](held-discovery-pilot-booking-commitment.md) (week tracker row → bridge → Script A/B → written interest / kickoff). Do not jump to `Pilot` on verbal interest alone.  
5. **Week honesty** — Update [`../research/qualified-discovery-week-tracker.md`](../research/qualified-discovery-week-tracker.md) only for **held** qualified discoveries. Demo-only weeks stay at 0 held. Soft decline → [`referral-ask-script.md`](referral-ask-script.md).

## Log (blank until real)

| CRM id | Demo date | Fixture demo done? (Y/N) | Follow-up booked? (Y/N/blank) | Grid Held? (Y/N/blank) | Commitment checklist run? (Y/N/blank) | Logged by | Notes |
|--------|-----------|--------------------------|------------------------------|------------------------|---------------------------------------|-----------|-------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Demo → follow-up booked | 0 |
| Demo → Held | 0 |
| Demo → commitment checklist run | 0 |

## Founder checklist

- [ ] Demo logged (`fixture_demo` note optional); CRM still Discovery until Held/Pilot rules say otherwise  
- [ ] Same-day follow-up booked **or** already Held marked honestly  
- [ ] Flake path → noshow densify (not new cold scrape)  
- [ ] On Held → booking commitment checklist (not skipped)  
- [ ] Week tracker / Repeatable acquisition only after Held  
- [ ] Script A only on legal PASS; else Script B hold  
- [ ] No invented Actuals; no win-rate / SaaS hard-sell  

## Stop rules

- Never invent demos, held interviews, offers, or kickoffs.  
- Fixture demo ≠ held interview ≠ Paid pilots Actual.  
- Never mark CRM `Pilot` on demo interest alone.  
- Never send Script A on uncleared MSA/DPA.  
- Never scrape a new cold 50-list to densify after a demo.  
- Soft decline → one referral ask; do not harass.  
- Do not replace the demo runbook or the booking-commitment checklist — compose with them.
