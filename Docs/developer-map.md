# BidHarbour developer map

Thin always-on index. Pull one file at a time. Research as-of: **9 November 2025**.

## Strategic posture

**INVESTIGATE FURTHER** — validate Norfolk supplier PQQ/SQ pack assembly before production SaaS.

Recommendation owner: `strategy/executive-decision.md`  
Full plan: `strategy/business-plan.md`  
Scorecard: `research/validation-scorecard.md`

## Folder map

| Path | Purpose | Key deliverables |
|------|---------|------------------|
| `strategy/` | Decision, brand, market, roadmap | `executive-decision.md`, `business-plan.md`, canvases |
| `research/` | Discovery, competitors, assumptions | interview templates, matrices, scorecard |
| `product/` | MVP and backlog | `mvp-spec.md`, `backlog.md` |
| `design/` | UX / IA | `ux-ia.md` |
| `engineering/` | Post-GO code (empty until GO) | apps/, packages/ later |
| `security-and-legal/` | Controls and stubs | `security-privacy-legal.md`, DPA stub |
| `commercial/` | GTM | outreach, first actions, CRM |
| `finance/` | Model and pricing | `model-24mo.xlsx`, `pricing.md` |
| `operations/` | Run model | KPIs, RACI, runbooks |
| `Docs/` | Committed thin docs | this file, architecture, legal-data-policy, master prompt |
| `.firecrawl/` | Local research dumps | **gitignored** |

## Agent standing orders

Tracked: [`bidharbour-master-prompt.md`](bidharbour-master-prompt.md) (attach at chat start).  
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
