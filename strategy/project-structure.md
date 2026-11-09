# 20. Project and repository structure

**As-of:** 9 November 2025

## Organisational tree (this repo)

| Path | Purpose | Owner role | Key deliverables | Definition of done |
|------|---------|------------|------------------|--------------------|
| `strategy/` | Decisions, brand, market, roadmap | Founder | business-plan, canvases, scorecard links | Decisions dated + labeled |
| `research/` | Discovery evidence | Founder / researcher | interviews, competitors, scorecard | Negative findings logged |
| `product/` | Specs, backlog | PM / founder | mvp-spec, backlog | MoSCoW + acceptance criteria |
| `design/` | UX / IA | Founder / designer | ux-ia, wireframes | Journeys + empty/error states |
| `engineering/` | Code (post-GO) | Technical founder | apps, packages | Tests for touched code |
| `security-and-legal/` | Controls, stubs | Founder + solicitor | DPA, ToS stubs | Marked Advice required where needed |
| `commercial/` | GTM | Founder commercial | scripts, CRM | Outreach sent + tracked |
| `finance/` | Model, pricing | Founder | xlsx + assumptions | Formulas auditable; VAT stated |
| `operations/` | Runbooks, KPIs | Founder | KPI, RACI, onboarding | Runbook used in a pilot |
| `Docs/` | Thin committed docs | Tech | developer-map, architecture | Linked from README |

## Proposed engineering monorepo (post-GO)

```
/apps/web
/apps/worker
/packages/domain
/packages/database
/packages/document-processing
/packages/ai
/packages/ui
/packages/config
/tests
/infra
/docs
```

Simpler alternative until scale: single `apps/web` full-stack app + one worker folder. Prefer simpler until multi-team.

## Dependencies

Research → Product → Design → Engineering.  
Security-and-legal gates pilots.  
Commercial feeds research.  
Finance consumes commercial + ops assumptions.

## Never in source control

Live customer files, secrets, credentials, unredacted packs, API keys. See `.gitignore` and `Docs/legal-data-policy.md`.
