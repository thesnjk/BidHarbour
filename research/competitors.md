# 8. Competitors and substitutes

**Pricing / feature observations dated:** 10 November 2026 (honesty pass) unless noted.  
**Prior pass:** 9 November 2025.  
**Refresh method:** public pricing pages via WebSearch/WebFetch 2026-11-10 → local notes [`.firecrawl/2026-11-10-competitor-pricing.md`](../.firecrawl/2026-11-10-competitor-pricing.md) (gitignored).  
“Not found in documentation” ≠ “does not exist.”

## Direct and adjacent matrix

| Product | Target buyer | Core workflow | Pricing (public) | Onboarding | AI | Security notes (public) | Weakness vs BidHarbour job | Switching |
|---------|--------------|---------------|------------------|------------|----|-------------------------|----------------------------|-----------|
| Constructionline | Suppliers / buyers construction | Prequal membership profile | Bronze from **£399/yr** lowest turnover band + year-1 joining fee (often **£99**); Silver/Gold/Platinum higher by band; excl VAT (**Verified fact** — Constructionline memberships page + public selector cites 2026-11-10) | Form + assessment | Limited / not pack AI | Scheme platform | One profile ≠ multi-customer inbound pack assembly | Annual membership lock-in |
| Complys | Main contractors / suppliers | Compliance vault, contractor PQ, RAMS | Free Sharer; Share **£15/mo**; Pro **£30/mo**; Growth **£49**; Growth Plus **£99**; Diamond **£199** (**Verified fact** — complys.co.uk/pricing 2026-11-10) | Self-serve | AI RAMS / tender writing on higher tiers | UK-focused claims on site | Oriented to contractor oversight / RAMS, not OEM inbound packs with Approver export gate | Low–medium |
| Evidash | Buyer QA (food / vendor docs) | Vendor doc coverage + validation | Coverage Core **$649/mo** or **£499/mo** (USD pricing page vs About GBP cite); Validation Core same; both modules stack (**Verified fact** — evidash.com/pricing + /about 2026-11-10) | Sales / self | Extraction + human review | AWS, encrypted claims | Buyer-side; price far above Norfolk SME supplier willingness | Medium |
| Velstrian | SME bidders | Tender find + AI draft | Starter **£49**; Pro **£149**; Portfolio **£549**/mo (**Verified fact** — velstrian.com/pricing 2026-11-10) | Self-serve | Bid drafting credits | Not fully audited here | Public/private tender drafting; not multi-customer evidence graph + MISSING abstention | Low |
| KimonBids | SME public sector | Tender portals + AI drafts | Free; Pro **£79**; Growth **£179**; Scale **£399**/mo (**Verified fact** — kimonbids.com/pricing 2026-11-10) | Self-serve | Bid drafts capped | UK GDPR claims on site | Same as Velstrian — tender-win focus | Low |
| TenderNation | SME bidders | Discovery + AI | £49–£149/mo *(prior pass 2025-11-09; not re-verified 2026-11-10)* | Self-serve | AI actions | Not fully audited here | Same | Low |
| M365 / SharePoint | All | Storage + collab | M365 licence | Familiar | Copilot optional (separate) | Org tenant | No requirement checklist / approval export gate | High familiarity inertia |
| Manual + consultant | All | Bespoke packs | £400–£800/day typical *(Reasoned inference — market rates)* | Human | None | N/A | Expensive; not scalable | Relationship-based |
| QMS platforms | Quality-led firms | Controlled docs | Varies | Heavy | Varies | Often strong | Overkill / not inbound pack UX | High |

## BidHarbour surface matrix (vs job-to-be-done)

Job: inbound customer-specific PQQ/SQ pack → checklist → evidence match → **MISSING**/conflict → human Approver → export.

| Surface | BidHarbour posture | Lead / Parity / Gap | Evidence |
|---------|-------------------|---------------------|----------|
| Inbound pack → structured checklist | Concierge + fixture (`testdata/redacted-pqq-v1/`) | **Lead** (hypothesis) vs SharePoint; **Gap** vs SaaS until GO | Fixture + pilot runbook shipped; no paid interview proof yet |
| Evidence match + abstain (MISSING) | Standing product principle | **Lead** vs tender-AI that invents prose; **Parity** with Evidash buyer validation (wrong side of market) | Master prompt / legal-data-policy |
| Human approval before export | Non-negotiable gate | **Lead** vs autonomous bid tools | Pilot runbook Approver path |
| Multi-customer packs (same SME, different buyers) | Core thesis | **Lead** vs Constructionline single profile | Business plan / executive decision |
| Norfolk SME price point | Pilot £250–£750 ex VAT / pack window | **Lead** vs Evidash $649+/mo buyer tools; **Parity** band with Complys/Velstrian monthly SaaS *if* validated | pilot-offer-sheet; scorecard Actual still 0 |
| Public tender discovery | Out of scope | **Gap** by design (Velstrian/KimonBids Lead there) | competitors.md this file |
| RFQ estimating | Out of scope / fallback only | **Gap** by design (ManufactIQ/FabPulse) | Fallback A below |

**Competitive rationale (one line):** Interviews and concierge pilots remain the only way to prove the inbound-pack + Approver differentiation; brochure SaaS would compete on the wrong axis (tender drafting or buyer vaults).

## Fallback A — RFQ tools

| Product | Notes | Price checked |
|---------|-------|---------------|
| ManufactIQ | Enquiry→quote→invoice for UK manufacturers | From £99/mo *(prior pass)* |
| FabPulse | Fab quoting from drawings/email | £49–£199/mo *(prior pass)* |
| KanchanFlow | RFQ-to-order job shops | Tiered (GBP pages) *(prior pass)* |

**Implication:** BidHarbour should **not** compete on estimating. Only adjacent if RFQs embed heavy compliance questionnaires.

## Fallback B — Holiday ops

| Product | Notes | Price |
|---------|-------|-------|
| Turno | Cleaning turnover coordination | ~$10/property/mo for multi-property non-marketplace *(prior pass)* |
| Changeover Master | UK holiday-let changeover ops *(existence known; deep feature audit not completed)* | Not fully verified |

**Verdict:** Reject as Norfolk entry for BidHarbour.

## Conclusions

1. **Underserved job (hypothesis):** inbound, customer-specific qualification pack with approved evidence graph + human approval export at SME price.  
2. **Differentiation valuable enough to buy?** Unproven — must show time saved vs SharePoint in paid pilots (scorecard Actual still 0).  
3. **Service vs SaaS:** Concierge + light software first; pure SaaS only after retention / GO.  
4. **Most likely copycat:** Complys or a tender-AI vendor adding “customer pack importer.” Monitor quarterly. Copycat-awareness talk track (queued, not a tender scrape): backlog **#81** → `commercial/competitive-objection-sheet.md` (Constructionline / SharePoint / tender-AI / Complys — abstain + Approver; no win-rate).  
 
5. **2026-11-10 delta:** Velstrian mid-tier clarified as Pro **£149** (not a flat £49–£549 smear); Evidash dual USD/GBP Core cites documented; Complys/KimonBids tiers unchanged vs prior pass.

## Gaps in this research

Full Constructionline official PDF price grid not scraped (selector-based); TenderNation / ManufactIQ / FabPulse not re-fetched this pass; My Supplier List deep review not completed — remain **Unresolved**.
