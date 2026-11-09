# Week-1 send runbook

**Goal:** Send all 10 discovery emails (CRM A01–A10) in one sitting; book ≥5 calls by end of Week 1.  
**Pack:** [`week1-outreach-pack.md`](week1-outreach-pack.md)  
**CRM:** [`crm-accounts.csv`](crm-accounts.csv)  
**Replies:** [`reply-booking-scripts.md`](reply-booking-scripts.md)  
**Epics:** [#1](https://github.com/thesnjk/BidHarbour/issues/1) · [#6](https://github.com/thesnjk/BidHarbour/issues/6)

**Product name in every email:** Supplier Desk  
**Do not** upload third-party customer packs until solicitor-cleared MSA/DPA exist.

## Before you start (10 min)

1. Fill [`../strategy/founder-scenarios.md`](../strategy/founder-scenarios.md) constraints form (scenario A/B/C).  
2. Open CRM CSV + outreach pack side by side.  
3. Prepare signature: name, phone, email (no auction/`bidharbour.com` branding).  
4. Calendar: block follow-up reminders for **Day 3, 7, 14** after today’s send date.  
5. Optional parallel: queue solicitor cover ([`../security-and-legal/solicitor-cover-email.md`](../security-and-legal/solicitor-cover-email.md)).

## Per account (repeat A01 → A10)

| Step | Action | Done? |
|------|--------|-------|
| 1 | Verify company still fits ICP (roughly 5–75 people; multi-customer B2B). Skip if anti-persona (e.g. huge group HQ only). | |
| 2 | Find a real recipient (MD / Ops / Quality). Prefer LinkedIn or site contact — do **not** invent a name. If unknown, use role-only (“Managing Director”) or skip. | |
| 3 | Confirm/fix website from CRM; open pack section for that ID. | |
| 4 | Copy subject + body; replace `{{Name}}` and `{{Founder}}`. | |
| 5 | Send from your real mailbox. | |
| 6 | CRM: `outreach_status=sent`, `stage=Contacted`; note date in `notes`. | |
| 7 | If bounced / wrong entity: `Disqualified` or fix and retry once. | |

## Same-day targets

- [ ] **10 sent** (or honest skips logged with reason)  
- [ ] Follow-up calendar holds created  
- [ ] Solicitor brief sent or scheduled  

## After replies

Use [`reply-booking-scripts.md`](reply-booking-scripts.md).  
When booked: CRM `stage=Discovery`; add row to [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md) slots (S01…).  
Before call: skim [`../research/interview-guide.md`](../research/interview-guide.md).  
After call: [`../research/recording-template.md`](../research/recording-template.md) + negative findings same day.

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
