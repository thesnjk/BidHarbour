# 1. Executive decision

**As-of:** 9 November 2025  
**Recommendation:** **INVESTIGATE FURTHER** — GO to 8-week validation; **NO-GO** to production SaaS until scorecard thresholds pass.

---

## One-sentence business description

BidHarbour Supplier Desk helps small UK suppliers turn each incoming customer questionnaire or document pack into a reviewer-approved response pack backed by their own evidence library.

## Exact proposed first customer

Owner-managed **subcontract engineering, fabrication, or marine/offshore services firm** in **Norfolk (Norwich, Great Yarmouth, King’s Lynn corridors)**, **5–75 employees**, selling to **multiple OEMs, tier-1s, or asset operators** that each send **different** qualification templates (not only public-sector tenders).

## Exact recurring problem

Each new or renewed customer sends a PQQ/SQ/assurance pack; staff re-hunt certificates, policies, insurance schedules, H&S answers, and case studies across email, SharePoint, and desktops — **2–8+ hours per pack** with expiry/conflict risk.  
*(Working assumption — must be measured in pilots.)*

## Measurable promised outcome

**≥40% reduction in admin minutes** from pack receipt to **first complete human-approved draft**, with **100% requirements mapped** to evidence or explicit “missing” flags.  
*(Proposed experiment threshold.)*

## Why a buyer would pay rather than use existing tools

| Alternative | Why insufficient for this job | Evidence label |
|-------------|-------------------------------|----------------|
| Constructionline / CHAS | One shared prequal profile; does not assemble **customer-specific** multi-template responses | Verified fact (product purpose + pricing from public Constructionline materials, Nov 2025) |
| Velstrian / KimonBids / TenderNation | Optimised for **public tender discovery + AI drafting**; weak fit for private supply-chain packs; higher hallucination risk without strict evidence linking | Verified fact (published pricing ~£49–£179/mo, Nov 2025) |
| Evidash | **Buyer-side** food QA document control; wrong persona and price band (£649/mo+) | Verified fact (evidash.com pricing, Nov 2025) |
| Complys | Contractor compliance **to main contractors**; not inbound customer pack assembly | Verified fact (complys.co.uk, Nov 2025) |
| SharePoint + spreadsheets | Default substitute; £0 SaaS but high labour and no checklist/match/approve loop | Reasoned inference |

## Proposed revenue model

Paid concierge pilot (£250–£750) → setup/import (£300–£1,000) → subscription (£99–£249/mo band). Hybrid managed-service + software acceptable if onboarding stays bounded.  
*(Proposed experiment — not validated prices.)* All figures **ex VAT** unless stated.

## Most important evidence supporting the concept

1. Norfolk advanced manufacturing & engineering: **2,150 businesses, 47,582 jobs, £2bn GVA (17%)** — Norfolk Business Board sector update. *(Verified fact.)*  
2. East of England offshore supply-chain density (Great Yarmouth / Lowestoft) — EEEZ matrix and operator programmes. *(Verified fact: cluster exists; firm-level pain unverified.)*  
3. Adjacent products prove willingness to pay for “response assembly” in tenders (Velstrian £49+, KimonBids £79+). *(Verified fact: published pricing.)*

## Strongest evidence against

1. Crowded adjacency at lower (Complys) and higher (Evidash) price points.  
2. Unverified frequency and willingness-to-pay among Norfolk SMEs; demand may be seasonal/low volume.  
3. Confidentiality may block cloud upload without strong trust.  
4. `bidharbour.com` occupied by Portuguese online auctioneer BID HARBOUR, LDA. *(Verified fact, Nov 2025.)*

## Three largest uncertainties

1. Real **requests/month** and **admin hours** per firm in the target niche.  
2. Whether users will **upload customer packs** to a third-party SaaS.  
3. **Retention** after the initial library build (“one-time setup” trap).

## Go / investigate further / no-go

| Decision | Status |
|----------|--------|
| 8-week customer discovery + concierge pilots | **GO** |
| Production SaaS development | **NO-GO until scorecard** |
| Overall | **INVESTIGATE FURTHER** |

## What must be proven before significant development expenditure

- ≥6/10 interviews report the same recurring pain in **one** niche.  
- ≥3 workflow observations with real redacted packs.  
- **3 paid pilots**; **≥2** convert to paid continuation.  
- Median **≥90 min saved** per pack vs baseline *(or customer-stated equivalent value ≥£150/pack)*.

See `research/validation-scorecard.md`.

---

## One-page summary (cofounder / adviser)

**BidHarbour Supplier Desk** — from customer request to submission-ready.

**Who:** Norfolk engineering / fabrication / marine suppliers (5–75 people) juggling different customer qualification packs.

**Job:** Turn each incoming PQQ/SQ into a complete, evidence-backed pack with a named human approver — no invented compliance.

**Why now / why here:** Dense AME and offshore supply chain; multi-customer admin pain; adjacent tender tools prove spend but miss private inbound packs.

**Model:** Paid pilot → setup → £99–£249/mo subscription (hypotheses).

**Ask of the next 8 weeks:** Prove frequency, time saved, willingness to pay, and retention intent with 30 interviews and 3 paid pilots — **before** building SaaS.

**Fallback stance:** Keep BidHarbour PQQ workflow as primary; RFQ quoting is secondary only if validation fails; holiday-property ops rejected for Norfolk entry.

**Brand caution:** Preliminary desk research found `bidharbour.com` used by an EU auction platform — clear or rename before brand investment. Not professional legal clearance.

**Founder capacity unknown:** Execution plans branch for part-time solo / full-time technical / two-person team (`strategy/founder-scenarios.md`).

---

## Fallback comparison (do not silent-pivot)

| Option | Verdict |
|--------|---------|
| **A. RFQ admin for small manufacturers** | **Secondary.** FabPulse / ManufactIQ / KanchanFlow (£49–£99/mo, 2025) already own pricing/estimating RFQ→quote. Overlap only if RFQs include heavy compliance gates. |
| **B. Holiday-property exception coordinator** | **Reject for Norfolk entry.** Turno dominates turnover coordination; weak fit vs supplier-desk hypothesis. |

**Narrowest profitable entry:** Single workflow — **Supplier Qualification Questionnaire (PQQ/SQ/assurance) response assembly** for Norfolk AME + marine/offshore fabricators. Exclude public tender writing as v1.
