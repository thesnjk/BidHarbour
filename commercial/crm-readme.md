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
2. Fill blanks from NAAME lists, Hethel tenants, LinkedIn Norfolk fab/marine searches.  
3. Queue **10** discovery emails (use **Supplier Desk** product name — see brand checklist).  
4. Update `stage` / `outreach_status` the same day.  
5. Do **not** commit personal emails, phone numbers, or customer pack files into git — keep PII in a private CRM copy if needed.
