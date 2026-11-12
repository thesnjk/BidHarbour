# Warm-intro CRM intake checklist (blank Actuals)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use when:** a peer intro is **confirmed** (post referral ask **G** / soft-decline intro / network peer)  
**Lead gap:** referral density — turn intros into CRM hygiene without inventing contacts  
**Companions:** [`referral-ask-script.md`](referral-ask-script.md) · [`pilot-referral-evidence-packet.md`](pilot-referral-evidence-packet.md) · [`crm-stage-scripts.md`](crm-stage-scripts.md) · [`crm-readme.md`](crm-readme.md) · [`reply-booking-scripts.md`](reply-booking-scripts.md) · [`post-first50-referral-wave.md`](post-first50-referral-wave.md) · [`naame-hethel-gy-network-peer-intro-pack.md`](naame-hethel-gy-network-peer-intro-pack.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until a **real** intro lands. Do **not** invent named people, personal emails, or CRM Actuals in git. Prefer anonymised labels; keep contact details on the local encrypted path.

## Goal

Same-day path from confirmed intro → CRM **Identified** → warm outbound **Contacted** → Discovery booking — without inventing addresses or counting non-ICP as lead wins.

## Intake steps

1. **Confirm intro** — Referrer gave a name/company (and optionally an intro email). Log date privately.  
2. **Name-use** — Ask/confirm OK to use referrer’s name ([`referral-ask-script.md`](referral-ask-script.md) confirm block). Record Y/N.  
3. **ICP filter** — Prefer Norfolk **AME / marine** multi-customer inbound packs. Construction-control / reserve / anti-persona → create row for honesty but **do not** count as lead ICP win (stage Disqualified / note `anti_persona` if clear).  
4. **CRM row** — Add row (beyond A01–A50 if needed): `stage=Identified`, `outreach_status=queued`, `notes` include `referral_from={{referrer_id}}` ([`crm-stage-scripts.md`](crm-stage-scripts.md)).  
5. **Channel (no invent)** — Public company inbox, published contact page, or LinkedIn for named people. **Never** invent a personal email.  
6. **Warm outbound** — Send referral-ask warm-intro template; set `stage=Contacted`, `outreach_status=sent` same day.  
7. **On reply** — Book via [`reply-booking-scripts.md`](reply-booking-scripts.md) → `Discovery` / `booked`; grid slot on interview grid. Scorecard Actuals only after completed interview.

## Checklist (blank until real)

- [ ] Intro confirmed (not invented)  
- [ ] Name-use Y/N recorded  
- [ ] ICP filter applied (lead vs honesty-only)  
- [ ] CRM row created: Identified / queued + `referral_from=`  
- [ ] Outreach channel is public / LinkedIn / general — not invented  
- [ ] Warm outbound sent; Contacted / sent  
- [ ] Reply → Discovery booking (or declined / deferred logged honestly)  

## Log (blank until real)

| Referrer CRM id | Referral firm / person (anonymised OK) | Name-use (Y/N) | New CRM id | Channel | Sent date | Outcome (`sent` / `booked` / `declined` / `deferred` / blank) | Notes |
|-----------------|----------------------------------------|----------------|------------|---------|-----------|----------------------------------------------------------------|-------|
| | | | | | | | |
| | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Intros logged | 0 |
| Warm outbound sent | 0 |
| Discovery booked from warm intro | 0 |

## Stop rules

- No invented personal emails, named intros, or CRM Actuals.  
- Non-ICP rows are not lead wins.  
- No SaaS hard-sell on warm intro or discovery.  
- No win-rate / qualification claims.  
- Scorecard Actuals only after completed interviews — send alone is not evidence.
