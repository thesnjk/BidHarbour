# Week-5 send runbook

**Goal:** Send discovery emails for CRM **A41–A50** in one sitting (after Week-4 A31–A40); prioritise marine fills over reserve/non-ICP. Completes first-50 wave.  
**Pack:** [`week5-outreach-pack.md`](week5-outreach-pack.md)  
**CRM:** [`crm-accounts.csv`](crm-accounts.csv)  
**Send log:** [`week5-send-log.csv`](week5-send-log.csv)  
**Contact hints:** [`a41-a50-contact-hints.md`](a41-a50-contact-hints.md)  
**Replies:** [`reply-booking-scripts.md`](reply-booking-scripts.md)  
**Non-responders:** [`week1-nonresponder-followups-a41-a50.md`](week1-nonresponder-followups-a41-a50.md)  
**Bounce / OOO:** [`bounce-ooo-triage.md`](bounce-ooo-triage.md)  
**Prior wave:** [`week4-send-runbook.md`](week4-send-runbook.md)  
**Epics:** [#6](https://github.com/thesnjk/BidHarbour/issues/6) · [#1](https://github.com/thesnjk/BidHarbour/issues/1)

**Product name in every email:** Supplier Desk  
**Do not** upload third-party customer packs until solicitor-cleared MSA/DPA exist.

## Before you start (10 min)

1. Confirm Week-4 log rows are filled (`sent` / honest `skipped`) in [`week4-send-log.csv`](week4-send-log.csv).  
2. Open CRM CSV + Week-5 pack + [`a41-a50-contact-hints.md`](a41-a50-contact-hints.md) side by side.  
3. Prepare signature: name, phone, email (no auction/`bidharbour.com` branding).  
4. Calendar: block Day **3 / 7 / 14** — copy from [`week1-nonresponder-followups-a41-a50.md`](week1-nonresponder-followups-a41-a50.md).  
5. Priority: **A42, A43** → size-check **A44** → sector-check **A41/A45** → network **A50, A47** → soft/skip counting **A46/A48/A49**; confirm A49 inbox before send.

## Per account (repeat A41 → A50)

| Step | Action | Done? |
|------|--------|-------|
| 1 | Verify ICP fit. Marine fills first; reserve/non-ICP = network only (not lead wins). Size-check A44/A46. | |
| 2 | Find recipient from [`a41-a50-contact-hints.md`](a41-a50-contact-hints.md). Prefer LinkedIn for named person — do **not** invent personal emails. | |
| 3 | Confirm website; open pack section for that ID. | |
| 4 | Copy subject + body; replace `{{Name}}` and `{{Founder}}`. | |
| 5 | Send or log honest skip / hold. | |
| 6 | CRM update; fill [`week5-send-log.csv`](week5-send-log.csv). | |
| 7 | Bounce / OOO / wrong entity → [`bounce-ooo-triage.md`](bounce-ooo-triage.md). | |

## Same-day targets

- [ ] **10 rows filled** in [`week5-send-log.csv`](week5-send-log.csv) (`sent` / `skipped` / `bounced`)  
- [ ] Follow-up holds for sent accounts  
- [ ] Reserve / non-ICP bookings labelled (not lead ICP wins)  

### Send-log field values

| Field | Allowed values |
|-------|----------------|
| `channel` | `email` / `linkedin` |
| `recipient_type` | `named` / `role_only` / `general_inbox` / `skipped` |
| `outcome` | `sent` / `skipped` / `bounced` |
| `booked_slot` | `S01`… when booked |

## After replies

Use [`reply-booking-scripts.md`](reply-booking-scripts.md).  
Book → CRM `Discovery`; set `reply_date` + `booked_slot`; add slot in [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md).  
Scorecard Actuals only from completed interviews.  
Referral intros → [`referral-ask-script.md`](referral-ask-script.md).

## Week-5 acceptance

| Metric | Target |
|--------|--------|
| Log rows completed | 10 (A41–A50) |
| Lead marine sends (A42–A43; A44 if SME) | Prioritised |
| Reserve / non-ICP (A46–A50, soft A48/A49) | Network only — not lead wins |
| Scorecard Friday | Actuals from real interviews only |

## Stop rules

- Do not pitch SaaS hard-sell on discovery calls.  
- Do not claim win rates or guaranteed qualification.  
- Do not invent personal emails or send Actuals.  
- Do not count reserve / aerospace / simulator / calibration-intro bookings as lead ICP wins.  
- Do not treat A50 as a pilot customer.  
- Do not start production auth/database code (pre-GO).
