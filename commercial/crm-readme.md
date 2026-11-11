# CRM — first 50 named accounts

**File:** [`crm-accounts.csv`](crm-accounts.csv)  
**As-of seed:** 9 November 2025  
**Stages:** Identified → Contacted → Discovery → Pilot → Active → Churned / Disqualified

## Columns

| Column | Meaning |
|--------|---------|
| id | Stable row id (A01–A50) |
| company | Legal/trading name |
| town | Norfolk / East Anglia operating base |
| niche | `AME` / `marine` / `construction` |
| inferred_buyer_title | Starting guess — verify before send |
| website | Public homepage if known |
| contact_page | Public contact/about URL (A01–A50 enriched) |
| contact_hint | Published general inbox/phone/caution — never invent personal emails |
| linkedin_search_hint | Query string for LinkedIn |
| source | Where the name was found |
| evidence_label | `Verified fact` (public listing) or `to fill` |
| stage | CRM stage |
| outreach_status | `not_started` / `queued` / `sent` / `replied` / `booked` / `declined` |
| notes | Free text — no confidential customer packs |

## How seeded rows were chosen

Public websites, ORE Catapult F4OR listings, and prior BidHarbour desk research (EEEZ/Norfolk AME). **No implied partnership or endorsement.** Seeded rows are starting points for founder verification (size, fit, contactability).

**First-50 complete** (A01–A50 enriched with public contact hints as of 11 November 2026). Verify size/fit before send; some rows are reserve / referral / sector-caution by design.

## Founder workflow

1. Verify each seeded company (employees 5–75; multi-customer PQQs likely).  
2. Contact hints: [`a01-a10-contact-hints.md`](a01-a10-contact-hints.md) · [`a11-a20-contact-hints.md`](a11-a20-contact-hints.md) · [`a21-a30-contact-hints.md`](a21-a30-contact-hints.md) · [`a31-a40-contact-hints.md`](a31-a40-contact-hints.md) · [`a41-a50-contact-hints.md`](a41-a50-contact-hints.md).  
3. Send waves: Week-1 [`week1-send-runbook.md`](week1-send-runbook.md) (A01–A10) → Week-2 [`week2-send-runbook.md`](week2-send-runbook.md) (A11–A20) → Week-3 [`week3-send-runbook.md`](week3-send-runbook.md) (A21–A30) → Week-4 [`week4-send-runbook.md`](week4-send-runbook.md) (A31–A40).  
4. First-50 complete — verify before send; prioritise lead ICP over construction-control / leisure / large-group / non-customer rows.  
5. Send discovery emails as **Supplier Desk**; update `stage` / `outreach_status` the same day.  
6. Do **not** invent personal emails; published `sales@` / `enquiries@` from company sites are OK as first reach. Keep extra PII in a private CRM copy if needed.
