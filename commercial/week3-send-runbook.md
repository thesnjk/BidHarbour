# Week-3 send runbook

**Goal:** Send discovery emails for CRM **A21–A30** in one sitting (after Week-2 A11–A20); book calls toward programme targets.  
**Pack:** [`week3-outreach-pack.md`](week3-outreach-pack.md)  
**CRM:** [`crm-accounts.csv`](crm-accounts.csv)  
**Send log:** [`week3-send-log.csv`](week3-send-log.csv)  
**Contact hints:** [`a21-a30-contact-hints.md`](a21-a30-contact-hints.md)  
**Replies:** [`reply-booking-scripts.md`](reply-booking-scripts.md)  
**Non-responders:** [`week1-nonresponder-followups-a21-a40.md`](week1-nonresponder-followups-a21-a40.md)  
**Prior wave:** [`week2-send-runbook.md`](week2-send-runbook.md)  
**Epics:** [#6](https://github.com/thesnjk/BidHarbour/issues/6) · [#1](https://github.com/thesnjk/BidHarbour/issues/1)

**Product name in every email:** Supplier Desk  
**Do not** upload third-party customer packs until solicitor-cleared MSA/DPA exist.

## Before you start (10 min)

1. Confirm Week-2 log rows are filled (`sent` / honest `skipped`) in [`week2-send-log.csv`](week2-send-log.csv).  
2. Open CRM CSV + Week-3 pack + [`a21-a30-contact-hints.md`](a21-a30-contact-hints.md) side by side.  
3. Prepare signature: name, phone, email (no auction/`bidharbour.com` branding).  
4. Calendar: block Day **3 / 7 / 14** follow-ups — copy from [`week1-nonresponder-followups-a21-a40.md`](week1-nonresponder-followups-a21-a40.md).  
5. Priority order: **A23, A27, A28, A29** → network **A25/A26** → caution/skip **A21/A22/A24** → sector-check **A30**.

## Per account (repeat A21 → A30)

| Step | Action | Done? |
|------|--------|-------|
| 1 | Verify company still fits ICP (roughly 5–75 people; multi-customer B2B). Skip if anti-persona / large group HQ only. | |
| 2 | Find a real recipient (MD / Ops / Quality). Start from [`a21-a30-contact-hints.md`](a21-a30-contact-hints.md). Prefer LinkedIn for a **named** person — do **not** invent personal emails. | |
| 3 | Confirm/fix website from CRM; open pack section for that ID. | |
| 4 | Copy subject + body; replace `{{Name}}` and `{{Founder}}`. | |
| 5 | Send from your real mailbox (or log honest skip / network-only). | |
| 6 | CRM: `outreach_status=sent`, `stage=Contacted`; fill [`week3-send-log.csv`](week3-send-log.csv). | |
| 7 | If bounced / OOO / wrong entity / ICP skip: triage via [`bounce-ooo-triage.md`](bounce-ooo-triage.md); set log `outcome` + `skip_reason`; CRM `Disqualified` or fix and retry once. | |

## Same-day targets

- [ ] **10 rows filled** in [`week3-send-log.csv`](week3-send-log.csv) (`sent` or honest `skipped` / `bounced`)  
- [ ] Follow-up calendar holds created for sent accounts  
- [ ] Negatives logged if entity/ICP fails  

### Send-log field values

| Field | Allowed values |
|-------|----------------|
| `channel` | `email` / `linkedin` |
| `recipient_type` | `named` / `role_only` / `general_inbox` / `skipped` |
| `outcome` | `sent` / `skipped` / `bounced` |
| `booked_slot` | `S01`… when booked (leave blank until then) |

## After replies

Use [`reply-booking-scripts.md`](reply-booking-scripts.md).  
When booked: CRM `stage=Discovery`; set `reply_date` + `booked_slot` on the Week-3 send-log row; add the slot in [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md).  
Before call: skim [`../research/interview-guide.md`](../research/interview-guide.md).  
After call: [`../research/recording-template.md`](../research/recording-template.md) + negative findings same day; update scorecard Actuals from completed interviews only.

## Week-3 acceptance

| Metric | Target |
|--------|--------|
| Log rows completed | 10 (A21–A30) |
| Emails sent (ex skips) | Honest count |
| Conversations booked (this wave) | Contribute to ≥5 programme bookings |
| Scorecard Friday | Actuals updated from real interviews only |

## Next wave

When Week-3 log rows are filled: run [`week4-send-runbook.md`](week4-send-runbook.md) (CRM A31–A40) with [`week4-outreach-pack.md`](week4-outreach-pack.md).

## Stop rules

- Do not pitch SaaS hard-sell on discovery calls.  
- Do not claim win rates or guaranteed qualification.  
- Do not invent personal emails or send Actuals.  
- Do not process real customer packs until legal drafts cleared.  
- Do not start production auth/database code (pre-GO).
