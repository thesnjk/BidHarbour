# Week-1 send runbook

**Goal:** Send all 10 discovery emails (CRM A01–A10) in one sitting; book ≥5 calls by end of Week 1.  
**Pack:** [`week1-outreach-pack.md`](week1-outreach-pack.md)  
**CRM:** [`crm-accounts.csv`](crm-accounts.csv)  
**Send log:** [`week1-send-log.csv`](week1-send-log.csv)  
**Replies:** [`reply-booking-scripts.md`](reply-booking-scripts.md)  
**Non-responders:** [`week1-nonresponder-followups.md`](week1-nonresponder-followups.md) (A01–A20) · [`week1-nonresponder-followups-a21-a40.md`](week1-nonresponder-followups-a21-a40.md) (A21–A40) · [`week1-nonresponder-followups-a41-a50.md`](week1-nonresponder-followups-a41-a50.md) (A41–A50)  
**Epics:** [#1](https://github.com/thesnjk/BidHarbour/issues/1) · [#6](https://github.com/thesnjk/BidHarbour/issues/6)

**Product name in every email:** Supplier Desk  
**Do not** upload third-party customer packs until solicitor-cleared MSA/DPA exist.

## Before you start (10 min)

1. Fill [`../strategy/founder-scenarios.md`](../strategy/founder-scenarios.md) constraints form (scenario A/B/C).  
2. Open CRM CSV + outreach pack side by side.  
3. Prepare signature: name, phone, email (no auction/`bidharbour.com` branding).  
4. Calendar: block follow-up reminders for **Day 3, 7, 14** after today’s send date — copy from the matching band: [`week1-nonresponder-followups.md`](week1-nonresponder-followups.md) (A01–A20) · [`week1-nonresponder-followups-a21-a40.md`](week1-nonresponder-followups-a21-a40.md) · [`week1-nonresponder-followups-a41-a50.md`](week1-nonresponder-followups-a41-a50.md).  
5. Optional parallel: queue solicitor cover ([`../security-and-legal/solicitor-cover-email.md`](../security-and-legal/solicitor-cover-email.md)).

## Per account (repeat A01 → A10)

| Step | Action | Done? |
|------|--------|-------|
| 1 | Verify company still fits ICP (roughly 5–75 people; multi-customer B2B). Skip if anti-persona (e.g. huge group HQ only). | |
| 2 | Find a real recipient (MD / Ops / Quality). Start from [`a01-a10-contact-hints.md`](a01-a10-contact-hints.md) (public contact pages + general inboxes). Prefer LinkedIn for a **named** person — do **not** invent personal emails. If unknown, use role-only (“Managing Director”) or skip. | |
| 3 | Confirm/fix website from CRM; open pack section for that ID. | |
| 4 | Copy subject + body; replace `{{Name}}` and `{{Founder}}`. | |
| 5 | Send from your real mailbox. | |
| 6 | CRM: `outreach_status=sent`, `stage=Contacted`; note date in `notes`. Fill the matching row in [`week1-send-log.csv`](week1-send-log.csv) (`sent_date`, `channel`, `recipient_type`, `outcome`). | |
| 7 | If bounced / wrong entity / ICP skip: set log `outcome` + `skip_reason`; CRM `Disqualified` or fix and retry once. | |

## Same-day targets

- [ ] **10 rows filled** in [`week1-send-log.csv`](week1-send-log.csv) (`sent` or honest `skipped` / `bounced`)  
- [ ] Follow-up calendar holds created  
- [ ] Solicitor brief sent or scheduled  

### Send-log field values

| Field | Allowed values |
|-------|----------------|
| `channel` | `email` / `linkedin` |
| `recipient_type` | `named` / `role_only` / `general_inbox` / `skipped` |
| `outcome` | `sent` / `skipped` / `bounced` |
| `booked_slot` | `S01`… when booked (leave blank until then) |

## After replies

Use [`reply-booking-scripts.md`](reply-booking-scripts.md).  
When booked: CRM `stage=Discovery`; set `reply_date` + `booked_slot` on the send-log row; add the slot in [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md) (S01…).  
Before call: skim [`../research/interview-guide.md`](../research/interview-guide.md).  
After call: [`../research/recording-template.md`](../research/recording-template.md) + negative findings same day; update scorecard Actuals from completed interviews only.

## Week-1 acceptance

| Metric | Target |
|--------|--------|
| Emails sent | 10 (A01–A10) |
| Conversations booked | ≥5 |
| Interviews completed | ≥3 |
| Scorecard Friday | Actuals updated |

## Stop rules

- Do not pitch SaaS hard-sell on discovery calls.  
- Do not claim win rates or guaranteed qualification.  
- Do not process real customer packs until legal drafts cleared.  
- Do not start production auth/database code (pre-GO).
