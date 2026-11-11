# Post–first-50 referral / rebook wave

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**When:** after Week-5 send log for A41–A50 is filled (or Week-5 in flight with parallel referral work)  
**Prior wave:** [`week5-send-runbook.md`](week5-send-runbook.md)  
**Scripts:** [`referral-ask-script.md`](referral-ask-script.md) · [`crm-stage-scripts.md`](crm-stage-scripts.md) · [`bounce-ooo-triage.md`](bounce-ooo-triage.md) · [`reply-booking-scripts.md`](reply-booking-scripts.md)  
**Grid:** [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md)  
**Product name:** Supplier Desk

**Rule:** Keep research framing. No win-rate claims. Do **not** invent named intros, personal emails, or send Actuals. Prefer Norfolk **AME / marine** lead ICP. Do **not** scrape a new cold 50-list in this wave. Parallel network path (events + LinkedIn warm intros, also not a new cold-50): [`naame-hethel-gy-network-peer-intro-pack.md`](naame-hethel-gy-network-peer-intro-pack.md).

## Goal

Keep the discovery pipeline warm after A01–A50 exhaust via (A) warm referral intros and (B) selective soft-recycle of quiet lead ICP accounts — without paid ads or SaaS hard-sell.

## Priority order

1. **Queued referral intros** (new CRM rows with `referral_from=`)  
2. **Lead ICP soft recycles** (AME / marine `sent`, no reply, not bounced)  
3. **Network-only** (e.g. A50-style intros) — do not count as lead wins  

## Preconditions

- [ ] Week-5 log rows mostly filled (`sent` / honest `skipped` / `bounced`) — or document parallel start  
- [ ] Bounce / OOO triage done on hard bounces before any recycle  
- [ ] Day 14 breakup completed (or account never entered follow-ups) before Track B recycle  
- [ ] Signature ready; LinkedIn preferred for named people  

---

## Track A — Warm intros

| Step | Action |
|------|--------|
| 1 | After each completed interview, soft decline, or clean pilot close: run [`referral-ask-script.md`](referral-ask-script.md) |
| 2 | On name/intro: new CRM row → `Identified` · `queued` · `notes=referral_from={{id}}` ([`crm-stage-scripts.md`](crm-stage-scripts.md)) |
| 3 | Warm-intro outbound (consent for name-use); published inbox or LinkedIn only |
| 4 | On book → Discovery; add slot on interview grid |
| 5 | Prefer AME / marine peers with multi-customer packs; skip counting non-ICP as lead wins |

**Same-day target:** process every new intro the day it arrives; do not invent intros to fill quota.

---

## Track B — Selective non-responder recycle

**Eligible:** `outreach_status` was `sent`; no reply; **not** hard bounce / Disqualified / anti-persona / size_check skip; Day 14 breakup sent **≥2 weeks** ago (or equivalent cool-down).

**Ineligible:** hard bounce; wrong entity; declined; reserve/non-ICP counted as lead; A50 as customer; construction-control contrast rows as lead wins.

### Rebook email (one touch)

**Subject:** Norfolk supplier packs — still useful to talk?

```text
Hi {{Name}},

I reached out a few weeks ago about how {{Company}} handles inbound customer qualification packs.
If timing is better now, would you spare 25 minutes on the **last** pack you completed?

Research only (Supplier Desk) — not a software demo on that call. Happy to share anonymised patterns back.

{{Founder}}
```

| Step | Action |
|------|--------|
| 1 | Pull candidates from Week-1–5 send logs (lead AME/marine first) |
| 2 | Confirm eligibility; triage bounce history |
| 3 | Send **one** rebook email or LinkedIn note — log on the same week’s send log `notes` (e.g. `recycle_rebook={{date}}`) or CRM notes |
| 4 | If still no reply: stop this wave for that id (no endless chase) |
| 5 | On reply → [`reply-booking-scripts.md`](reply-booking-scripts.md) → grid slot |

**Same-day target:** up to **5** lead ICP recycles per sitting; quality over volume.

---

## Logging

| Outcome | Where |
|---------|--------|
| New referral row | `crm-accounts.csv` (or private extension) + `referral_from=` |
| Warm outbound sent | CRM `outreach_status=sent` · stage Contacted |
| Recycle touch | Send-log or CRM `notes=recycle_rebook={{date}}` |
| Booked | Grid slot + `outreach_status=booked` · Discovery |

Do not invent rows. Do not commit confidential pack content.

## Acceptance (founder)

| Metric | Target |
|--------|--------|
| Referral asks made (post-interview / decline / pilot) | Ongoing — every eligible conversation |
| New referral CRM rows queued/sent | ≥1 when intros exist (never invent) |
| Lead ICP recycles attempted | ≤5/sitting; only eligible |
| Scorecard | Actuals from completed interviews only |

## Stop rules

- Do not invent personal emails, named intros, or send Actuals.  
- Do not run Day 3/7/14 again on hard bounces — [`bounce-ooo-triage.md`](bounce-ooo-triage.md).  
- Do not count reserve / aerospace / simulator / calibration-intro as lead ICP wins.  
- Do not start a new cold 50-account scrape in this slice.  
- Do not pitch SaaS hard-sell on rebook or referral calls.  
- Do not start production auth/database code (pre-GO).
