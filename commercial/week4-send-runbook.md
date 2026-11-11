# Week-4 send runbook

**Goal:** Send discovery emails for CRM **A31–A40** in one sitting (after Week-3 A21–A30); prioritise lead AME over construction control.  
**Pack:** [`week4-outreach-pack.md`](week4-outreach-pack.md)  
**CRM:** [`crm-accounts.csv`](crm-accounts.csv)  
**Send log:** [`week4-send-log.csv`](week4-send-log.csv)  
**Contact hints:** [`a31-a40-contact-hints.md`](a31-a40-contact-hints.md)  
**Replies:** [`reply-booking-scripts.md`](reply-booking-scripts.md)  
**Non-responders:** [`week1-nonresponder-followups-a21-a40.md`](week1-nonresponder-followups-a21-a40.md)  
**Bounce / OOO:** [`bounce-ooo-triage.md`](bounce-ooo-triage.md)  
**Prior wave:** [`week3-send-runbook.md`](week3-send-runbook.md)  
**Epics:** [#6](https://github.com/thesnjk/BidHarbour/issues/6) · [#1](https://github.com/thesnjk/BidHarbour/issues/1)

**Product name in every email:** Supplier Desk  
**Do not** upload third-party customer packs until solicitor-cleared MSA/DPA exist.

## Before you start (10 min)

1. Confirm Week-3 log rows are filled (`sent` / honest `skipped`) in [`week3-send-log.csv`](week3-send-log.csv).  
2. Open CRM CSV + Week-4 pack + [`a31-a40-contact-hints.md`](a31-a40-contact-hints.md) side by side.  
3. Prepare signature: name, phone, email (no auction/`bidharbour.com` branding).  
4. Calendar: block Day **3 / 7 / 14** — copy from [`week1-nonresponder-followups-a21-a40.md`](week1-nonresponder-followups-a21-a40.md).  
5. Priority: **A36, A38, A39, A40** → **A37** → control **A31–A34** (contrast) → hold **A35** until inbox verified.

## Per account (repeat A31 → A40)

| Step | Action | Done? |
|------|--------|-------|
| 1 | Verify ICP fit. Construction control = contrast only (not lead win). Size-check A40 / A33. | |
| 2 | Find recipient from [`a31-a40-contact-hints.md`](a31-a40-contact-hints.md). Prefer LinkedIn for named person — do **not** invent personal emails. | |
| 3 | Confirm website; open pack section for that ID. | |
| 4 | Copy subject + body; replace `{{Name}}` and `{{Founder}}`. | |
| 5 | Send or log honest skip / hold. | |
| 6 | CRM update; fill [`week4-send-log.csv`](week4-send-log.csv). | |
| 7 | Bounce / OOO / wrong entity → [`bounce-ooo-triage.md`](bounce-ooo-triage.md). | |

## Same-day targets

- [ ] **10 rows filled** in [`week4-send-log.csv`](week4-send-log.csv) (`sent` / `skipped` / `bounced`)  
- [ ] Follow-up holds for sent accounts  
- [ ] Control-niche bookings labelled (not lead ICP wins)  

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

## Week-4 acceptance

| Metric | Target |
|--------|--------|
| Log rows completed | 10 (A31–A40) |
| Lead AME sends (A36–A40 ex honest skips) | Prioritised |
| Control niche (A31–A35) | Contrast only — not lead wins |
| Scorecard Friday | Actuals from real interviews only |

## Stop rules

- Do not pitch SaaS hard-sell on discovery calls.  
- Do not claim win rates or guaranteed qualification.  
- Do not invent personal emails or send Actuals.  
- Do not count scaffolding/groundworks control bookings as lead ICP wins.  
- Do not start production auth/database code (pre-GO).
