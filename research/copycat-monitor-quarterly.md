# Copycat quarterly monitor (Complys / tender-AI)

**Epic:** [#1](https://github.com/thesnjk/BidHarbour/issues/1)  
**Cadence:** Quarterly (public pages only)  
**Lead gap:** Complys or tender-AI adding a “customer pack importer” that blurs Supplier Desk’s inbound-pack + MISSING + Approver job ([`competitors.md`](competitors.md) §4)  
**Companions:** [`competitors.md`](competitors.md) · [`../commercial/competitive-objection-sheet.md`](../commercial/competitive-objection-sheet.md)  
**Baseline honesty pass:** 2026-11-10 (pricing notes; see competitors.md)

**Evidence label:** Checklist + blank pass log until a **real** quarterly pass is filled. Do **not** invent “they shipped pack importer,” feature parity, or scorecard Actuals. Pre-GO — **not** a full Firecrawl competitive sweep.

## Scope

| Vendor | Why watch | Primary public pages (verify live each pass) |
|--------|-----------|-----------------------------------------------|
| **Complys** | Most likely adjacent copycat (vault / RAMS → pack importer) | Pricing + product/features marketing |
| **Velstrian** | Tender-AI draft risk expanding to inbound packs | Pricing + product claims |
| **KimonBids** | Same tender-AI adjacency | Pricing + product claims |
| Constructionline *(optional glance)* | Scheme profile adjacency only — not core copycat | Memberships / pricing |

## Public-page checklist (per vendor)

Fill **Y / N / blank** only from pages you opened this pass. Record URL + date. No ToS-forbidden scrape; prefer manual browse or allowed fetch → notes in `.firecrawl/` (gitignored) if used.

| Signal | Complys | Velstrian | KimonBids | Notes / URL / date |
|--------|---------|-----------|-----------|--------------------|
| Pricing changed vs last pass | | | | |
| Claims **inbound** customer / OEM **PQQ / SQ / questionnaire pack** assembly | | | | |
| Claims **pack importer** / questionnaire upload → checklist | | | | |
| Claims **evidence library** match to pack requirements | | | | |
| Claims **MISSING / abstain** when evidence absent | | | | |
| Claims **named Approver / human sign-off before export** | | | | |
| AI drafting expanded (RAMS / tender / answers) | | | | |
| Buyer-of-job shift toward **supplier-side multi-customer inbound packs** | | | | |

## Copycat signal vs still adjacent

| Observation | Threatens Supplier Desk Lead? | Action |
|-------------|-------------------------------|--------|
| Vault / RAMS / contractor oversight unchanged | No — still adjacent | Keep objection sheet Complys row; no feature-parity claims |
| Public tender find + AI draft unchanged | No — wrong fight by design | Keep tender-AI objection; no win-rate contrast |
| New “upload customer questionnaire → filled answers” without abstain/Approver | **Yes — monitor closely** | Update competitors.md + objection talk track; do **not** invent parity |
| Explicit multi-customer evidence graph + MISSING + human export gate at SME price | **Yes — Lead compression** | Re-rank backlog; honesty-pass pricing/features; founder review |
| Price-only change, same job | Weak | Note in competitors.md delta only |

## Pass log (blank until real)

| Pass date | Reviewer | Sources touched | Delta vs 2026-11-10 (or prior pass) | Action |
|-----------|----------|-----------------|-------------------------------------|--------|
| | | | | update competitors.md / objection sheet / none |

## How to run (agent or founder)

1. Open this file; start a new pass-log row (date + reviewer).  
2. Browse public pages for Complys, Velstrian, KimonBids (optional Constructionline glance).  
3. Tick checklist from what you **saw** — leave blank if not checked.  
4. Classify any new claims via the signal table.  
5. If material delta: patch [`competitors.md`](competitors.md) dated observation + [`../commercial/competitive-objection-sheet.md`](../commercial/competitive-objection-sheet.md) talk track in a normal PR.  
6. Do **not** run a full Firecrawl sweep pre-GO unless posture moves post-GO (master prompt competitive research section).

## Stop rules

- No invented competitor features, prices, or “we still lead” proof.  
- No full Firecrawl competitive scrape pre-GO.  
- If a source ToS forbids automated access, skip and note the gate.  
- Dump notes stay in `.firecrawl/` — do not commit secrets or huge dumps.  
- Objection handling stays job-to-be-done contrast — never “we beat X by £Y.”
