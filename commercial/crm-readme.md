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
| contact_page | Public contact/about URL (A01–A20 enriched) |
| contact_hint | Published general inbox/phone/caution — never invent personal emails |
| linkedin_search_hint | Query string for LinkedIn |
| source | Where the name was found |
| evidence_label | `Verified fact` (public listing) or `to fill` |
| stage | CRM stage |
| outreach_status | `not_started` / `queued` / `sent` / `replied` / `booked` / `declined` |
| notes | Free text — no confidential customer packs |

## How seeded rows were chosen

Public websites, ORE Catapult F4OR listings, and prior BidHarbour desk research (EEEZ/Norfolk AME). **No implied partnership or endorsement.** Seeded rows are starting points for founder verification (size, fit, contactability).

Blank `to fill` rows pad to **50** for the Days 1–14 target list.

## Founder workflow

1. Verify each seeded company (employees 5–75; multi-customer PQQs likely).  
2. For A01–A10: use [`a01-a10-contact-hints.md`](a01-a10-contact-hints.md); for A11–A20: [`a11-a20-contact-hints.md`](a11-a20-contact-hints.md) + [`week1-send-runbook.md`](week1-send-runbook.md).  
3. Fill blanks A21–A50 from NAAME lists, Hethel tenants, LinkedIn Norfolk fab/marine searches.  
4. Send discovery emails as **Supplier Desk**; update `stage` / `outreach_status` the same day.  
5. Do **not** invent personal emails; published `sales@` / `enquiries@` from company sites are OK as first reach. Keep extra PII in a private CRM copy if needed.
