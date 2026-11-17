# BidHarbour — project charter

**As-of:** 2026-11-17  
**Authority:** This file is the source of truth for **current direction**. Operating rules live in local-only `bidharbour-master-prompt.md` (not committed). Continue queue: [`agent-backlog.md`](agent-backlog.md). Do not invent interviews, pilots, or scorecard Actuals here.

| Field | Content |
|-------|---------|
| **Project name** | BidHarbour — first product **Supplier Desk** |
| **One-line description** | Helps small UK suppliers turn each incoming customer questionnaire or document pack into a reviewer-approved response pack backed by their own evidence library. |
| **Strategic posture** | **INVESTIGATE FURTHER** — validate Norfolk SME PQQ/SQ pack assembly via concierge pilots **before** material production SaaS spend. *(Desk research as-of 9 Nov 2025; Actuals still 0.)* |
| **Primary customer** | Owner-managed subcontract engineering / fabrication / marine-offshore services firm in **Norfolk** (Norwich, Great Yarmouth, King’s Lynn corridors), ~5–75 employees, selling to multiple OEMs/tier-1s/asset operators with **different** qualification templates. |
| **Primary problem** | Each new/renewed customer sends a PQQ/SQ/assurance pack; staff re-hunt certificates, policies, insurance, H&S answers across email/SharePoint — **2–8+ hours per pack** with expiry/conflict risk. *(Working assumption — must be measured in pilots.)* |
| **Primary workflow** | Inbound pack → structured checklist → evidence match → MISSING / EXPIRED / CONFLICT / customer-specific gaps → named human Approver → export + audit trail. |
| **Promised outcome** | ≥40% reduction in admin minutes to first complete human-approved draft, with 100% requirements mapped to evidence or explicit gaps. *(Proposed experiment.)* |
| **Revenue model** | Paid concierge pilot (**£250–£750** ex VAT) → setup/import → subscription band (**£99–£249**/mo hypotheses). Hybrid managed-service + software OK if onboarding stays bounded. *(Proposed experiment — not validated prices.)* |
| **Initial geography** | Norfolk / East Anglia AME + marine/offshore supply chain. |
| **Active opportunity** | **Supplier Desk** — inbound multi-customer PQQ/SQ pack assembly with abstention + Approver export. |
| **Backup opportunity** | RFQ admin / quoting hybrid — **secondary only if PQQ validation fails** (FabPulse/ManufactIQ already own estimating). |
| **Explicit exclusions** | Holiday-property ops; public tender discovery/writing as v1; buyer-side portals; inventing compliance answers; win-rate / qualification guarantees; uncleared MSA/DPA live packs. |
| **Founder constraints** | Founder-led outreach and scorecard Actuals; solicitor clearance for MSA/DPA; IPO/domain brand risk (`bidharbour.com` occupied — Verified fact Nov 2025); capacity scenarios in [`../strategy/founder-scenarios.md`](../strategy/founder-scenarios.md). |
| **GO / NARROW / PIVOT / STOP** | Current: **INVESTIGATE FURTHER / NARROW** (Norfolk AME/marine PQQ). Production SaaS = **NO-GO until scorecard**. Live sheet: [`../research/validation-scorecard.md`](../research/validation-scorecard.md). Threshold twin (do not invent Actuals): [`../strategy/decision-scorecard.md`](../strategy/decision-scorecard.md). |
| **Next decision gate** | Week-4 interview gate (≥6/10 same pain) via [`../research/week4-gate-checklist.md`](../research/week4-gate-checklist.md); Week-8 pilot gate via [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md). |

## Dual-backlog contract

| Queue | Role | Path |
|-------|------|------|
| **Continue / self-service** | Authoritative pre-GO agent work | [`agent-backlog.md`](agent-backlog.md) |
| **Post-GO engineering** | MoSCoW after scorecard **GO** only | [`../product/backlog.md`](../product/backlog.md) |
| **Operating rules** | Local-only standing orders | `bidharbour-master-prompt.md` (not in git) |

Do **not** treat `product/backlog.md` as the Continue queue. Do **not** migrate self-service row numbers into it. Do **not** commit the master prompt.

## Evidence & human approval (one-liners)

- **Evidence:** label material claims Verified fact / Reasoned inference / Working assumption / Proposed experiment / Unresolved question — see local master prompt §C; never invent interviews or scorecard Actuals ([`../research/validation-scorecard.md`](../research/validation-scorecard.md)).
- **Human approval:** AI may extract/match/draft; only authorised humans approve statements and submissions — see [`legal-data-policy.md`](legal-data-policy.md).

## Agent vs founder ownership

| Work | Owner |
|------|--------|
| Self-service agent backlog (fixtures, runbooks, DRY, blank templates) | **Agent** — [`agent-backlog.md`](agent-backlog.md) |
| Post-GO engineering MoSCoW | **Agent after GO** — [`../product/backlog.md`](../product/backlog.md) |
| Outreach sends, interview Actuals, scorecard numbers | **Founder** |
| Solicitor MSA/DPA clearance, live customer packs | **Founder** (+ counsel) |
| Brand IPO / domain / Companies House | **Founder** |

## First five post-upgrade Continues (after this OS ship)

Execute on subsequent Continues — not invent Actuals:

1. Row **118** — Evidash buyer vs Supplier Desk one-pager  
2. Row **119** — re-rank; append Lead-closing rows  
3. Next unfinished self-service rows after that re-rank  
4. Keep founder outreach / scorecard Actuals founder-owned  
5. Charter hygiene only if posture/scorecard actually moves

## Pointers (do not duplicate)

| Topic | Path |
|-------|------|
| Executive decision / thesis | [`../strategy/executive-decision.md`](../strategy/executive-decision.md) |
| Business plan index | [`../strategy/business-plan.md`](../strategy/business-plan.md) |
| Opportunity portfolio | [`../strategy/opportunity-portfolio.md`](../strategy/opportunity-portfolio.md) |
| Risk + pre-mortem | [`../strategy/risk-register.md`](../strategy/risk-register.md) |
| Pilot standard | [`../research/pilot-design.md`](../research/pilot-design.md) · [`../operations/concierge-pilot-runbook.md`](../operations/concierge-pilot-runbook.md) |
| Discovery programme | [`../research/customer-discovery-programme.md`](../research/customer-discovery-programme.md) |
| Legal / data | [`legal-data-policy.md`](legal-data-policy.md) |
| Developer map | [`developer-map.md`](developer-map.md) |
| Living narrative | [`project-writeup.md`](project-writeup.md) |

## Non-negotiable product principles (summary)

- AI may extract / match / draft; **only authorised humans approve** submissions.  
- Unsupported facts → **MISSING**; past expiry → **EXPIRED**; dual in-date disagree → **CONFLICT** — never silent invent, renew, or newest-wins.  
- Never commit live customer packs, secrets, or certificates — redacted `testdata/` only.
