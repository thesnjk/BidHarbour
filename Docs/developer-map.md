# BidHarbour developer map

Thin always-on index. Pull one file at a time.  
**Map as-of:** 2026-11-17 · Desk research as-of: **9 November 2025**.

## Strategic posture

**INVESTIGATE FURTHER** — validate Norfolk supplier PQQ/SQ pack assembly before production SaaS.

**Direction (charter):** [`project-charter.md`](project-charter.md)  
Recommendation owner: `strategy/executive-decision.md`  
Opportunity portfolio: `strategy/opportunity-portfolio.md`  
Full plan: `strategy/business-plan.md`  
Live scorecard: `research/validation-scorecard.md` (threshold twin only: `strategy/decision-scorecard.md` — do not invent Actuals)

## Folder map

| Path | Purpose | Key deliverables |
|------|---------|------------------|
| `strategy/` | Decision, brand, market, roadmap | `executive-decision.md`, `opportunity-portfolio.md`, `business-plan.md`, canvases |
| `research/` | Discovery, competitors, assumptions | interview templates, `competitors.md`, scorecard |
| `product/` | MVP + **post-GO** engineering backlog | `mvp-spec.md`, `backlog.md` (not the agent Continue queue) |
| `design/` | UX / IA | `ux-ia.md` |
| `engineering/` | Post-GO code (empty until GO) | apps/, packages/ later |
| `security-and-legal/` | Controls and stubs | `security-privacy-legal.md`, DPA stub, privacy issue-spotter, transfers annex |
| `commercial/` | GTM | outreach, first actions, CRM, NAAME/Hethel/GY peer-intro pack |
| `finance/` | Model and pricing | `model-24mo.xlsx`, `pricing.md` |
| `operations/` | Run model | KPIs, RACI, runbooks |
| `Docs/` | Committed thin docs | this file, [`project-charter.md`](project-charter.md), [`project-writeup.md`](project-writeup.md), architecture, legal-data-policy, master prompt |
| `testdata/` | Redacted synthetic fixtures only | `redacted-pqq-v1/`, `redacted-sq-v1/`, `synthetic-evidence-library-v1/` |
| `.firecrawl/` | Local research dumps | **gitignored** |

## Agent standing orders

Tracked: [`bidharbour-master-prompt.md`](bidharbour-master-prompt.md) (attach at chat start) — sections **A–Q**; **authoritative pre-GO agent backlog** = §N table in that file.  
**Dual backlog:** Continue queue = master-prompt §N; post-GO MoSCoW only = [`../product/backlog.md`](../product/backlog.md) (never the Continue queue).  
Direction: [`project-charter.md`](project-charter.md).  
OS regression: [`agent-os-regression-checklist.md`](agent-os-regression-checklist.md).  
Living narrative: [`project-writeup.md`](project-writeup.md) (chapters fill via self-service backlog).  
Evidence labels required on material claims.  
Human approval before any submission statement.  
No customer confidential files in git.

## Decision gates

1. Week 4 interview gate — pain convergence ≥6/10 in lead niche  
2. Pilot gate — 3 paid pilots, ≥2 continuations  
3. Build gate — scorecard GO before auth/database MVP  
4. Expand gate — Norfolk repeatability before East of England

## Default stack (post-GO only)

- Pilot: Airtable/Notion + scripts  
- MVP: Next.js + API + Postgres + object storage + worker  
- Auth: managed (Clerk/Auth0)  
- Billing: Stripe  
- AI: provider with DPA / zero-retention preference
