# Opportunity portfolio (pre-GO)

**As-of:** 2026-11-17  
**Rule:** One active opportunity at a time. Scores are **judgement** from desk research — not validated WTP. Do **not** invent interviews, prices beyond dated cites, or scorecard Actuals.  
**Primary sources:** [`executive-decision.md`](executive-decision.md) · [`norfolk-market-map.md`](norfolk-market-map.md) (**15-row industry screen** lives there) · [`../research/competitors.md`](../research/competitors.md) · [`../research/customer-discovery-programme.md`](../research/customer-discovery-programme.md) · [`../Docs/project-charter.md`](../Docs/project-charter.md)

**This file:** thin scored portfolio index (primary / backup / exclusions). Do **not** duplicate the Norfolk industry screen — refresh attractiveness there, then sync selection below.

## Scoring dimensions (1–5)

Customer value · Willingness to pay · Technical reuse · MVP effort (5=easier) · Support burden (5=low) · Regulatory risk (5=low) · Competitive pressure (5=low pressure) · Distribution advantage · Solo-founder fit.

## Candidates (12)

| # | Opportunity | Verdict | CV | WTP | Reuse | MVP | Support | Reg | Comp | Dist | Solo | Notes / evidence label |
|---|-------------|---------|----|-----|-------|-----|---------|-----|------|------|------|------------------------|
| 1 | **Supplier Desk — inbound multi-customer PQQ/SQ packs** | **PRIMARY** | 5 | 3 | 5 | 3 | 3 | 3 | 3 | 4 | 4 | Norfolk AME/marine; Approver + abstention wedge. *Working assumption on hours/WTP.* |
| 2 | RFQ quoting / estimating for fab SMEs | **BACKUP** | 4 | 3 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | ManufactIQ/FabPulse Lead. Secondary **only if PQQ fails**. *Verified adjacency pricing (2025).* |
| 3 | Constructionline-style scheme membership | Exclude as core | 3 | 4 | 1 | 1 | 3 | 3 | 2 | 2 | 2 | Different job (single profile). *Verified product purpose.* Matrix: [`../commercial/constructionline-vs-multi-buyer-pack-matrix.md`](../commercial/constructionline-vs-multi-buyer-pack-matrix.md). |
| 4 | Public tender discovery + AI draft (Velstrian/KimonBids axis) | Exclude v1 | 3 | 4 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | Wrong fight; hallucination risk. *Verified pricing band Nov 2025 / 2026-11-10.* One-pager: [`../commercial/tender-ai-wrong-fight-one-pager.md`](../commercial/tender-ai-wrong-fight-one-pager.md). |
| 5 | Buyer-side QA vault (Evidash axis) | Exclude | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | Wrong side of market; £649+/mo. *Verified Evidash pricing.* One-pager: [`../commercial/evidash-buyer-vs-supplier-desk-one-pager.md`](../commercial/evidash-buyer-vs-supplier-desk-one-pager.md). |
| 6 | Contractor RAMS / compliance vault (Complys axis) | Exclude as core | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 2 | Adjacent; copycat watch. Matrix: [`../commercial/complys-vault-vs-inbound-pack-matrix.md`](../commercial/complys-vault-vs-inbound-pack-matrix.md). |
| 7 | SharePoint + Copilot “do nothing new” | Status quo rival | 2 | 5 | 5 | 5 | 1 | 4 | 1 | 5 | 5 | £0 SaaS; high labour. Must beat on minutes. *Reasoned inference.* Matrix: [`../commercial/sharepoint-vs-inbound-checklist-matrix.md`](../commercial/sharepoint-vs-inbound-checklist-matrix.md). |
| 8 | Certificate expiry tracker only | Exclude | 2 | 2 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | Subset of job; not pack assembly. |
| 9 | Supplier directory / marketplace | Exclude | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | Not the wedge; high support. |
| 10 | Holiday-property exception / changeover ops | **REJECT** | 2 | 3 | 1 | 2 | 2 | 4 | 1 | 1 | 2 | Weak Norfolk entry; Turno adjacency. *Executive-decision reject.* |
| 11 | Autonomous compliance / auto-submit to portals | Exclude | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | Violates human-approval non-negotiable. |
| 12 | East Anglia widen (same Supplier Desk job) | Later geography | 4 | 3 | 5 | 4 | 3 | 3 | 3 | 3 | 3 | Only after Norfolk frequency proof. *Assumption.* |

## Selection

| Role | Choice |
|------|--------|
| **Primary** | #1 Supplier Desk inbound PQQ/SQ packs |
| **Backup** | #2 RFQ hybrid — only if scorecard shows PQQ validation fail |
| **Do not develop in parallel** | #3–#11 as core products; #12 only as geographic widen post-proof |

## Refresh ritual

On backlog **re-rank** slices: skim [`../research/competitors.md`](../research/competitors.md) Lead/Gap; update scores only with **dated** observations; never invent WTP or Actuals. Scan-artefact paths for exclusion / status-quo rivals live on candidates **#3–#7** (Constructionline, tender-AI, Evidash, Complys, SharePoint). Agent row for ritual hygiene may exist in the master-prompt self-service backlog.
