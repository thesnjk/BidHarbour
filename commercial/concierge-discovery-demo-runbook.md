# Concierge discovery demo runbook (15 min)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Goal:** Show inbound pack → checklist → **MISSING** → Approver **block** on a synthetic PQQ — **no SaaS**, no live customer packs.  
**Product name:** Supplier Desk  
**Use with:** [`go-to-market.md`](go-to-market.md) · [`discovery-one-pager.md`](discovery-one-pager.md) · [`competitive-objection-sheet.md`](competitive-objection-sheet.md) · [`../research/discovery-pilot-offer-bridge.md`](../research/discovery-pilot-offer-bridge.md) · [`pilot-offer-sheet.md`](pilot-offer-sheet.md) · [`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md)  
**Ops depth:** Path A [`../operations/concierge-pilot-runbook.md`](../operations/concierge-pilot-runbook.md) · empty-library story [`../operations/pack-dry-run-dry-001.md`](../operations/pack-dry-run-dry-001.md) · Approver [`../operations/approver-review-training.md`](../operations/approver-review-training.md) · manifest [`../operations/export-manifest-template.md`](../operations/export-manifest-template.md)

**Rule:** Research / discovery framing. Fixture-only. Do **not** invent scorecard Actuals, win rates, or certifications. DRY-001 is training — not customer minutes-saved proof. Filled-manifest / partial-library demo depth is backlog **#85** (DRY-009) — **not** this runbook.

## Lead gap

**Inbound pack → checklist vs SharePoint** folder scatter — show the method so discovery converts toward a bounded pilot.

## Preconditions (before the call)

- [ ] Discovery booked **or** clear pack-assembly pain already confirmed  
- [ ] Local copies ready: [`../testdata/redacted-pqq-v1/questionnaire.md`](../testdata/redacted-pqq-v1/questionnaire.md) + working copy of [`../testdata/redacted-pqq-v1/evidence-checklist.md`](../testdata/redacted-pqq-v1/evidence-checklist.md)  
- [ ] **No** live customer confidential packs on screen  
- [ ] Approver role available (second person or founder role-play)  
- [ ] Consent / research framing ready ([`reply-booking-scripts.md`](reply-booking-scripts.md))

## When **not** to demo

| Situation | Do instead |
|-----------|------------|
| Cold Week-1–5 outreach | Book research call — no fixture demo |
| They ask “demo the product” before pain | Two-track reply: research first ([`reply-booking-scripts.md`](reply-booking-scripts.md) § demo immediately) |
| They want to upload real packs now | Legal gate + kickoff — not this runbook |

---

## Demo clock (15 min — aligns GTM)

| Min | Segment | Do |
|-----|---------|-----|
| 0–3 | Their pack types | Ask last inbound PQQ/SQ / who owns it / where files live (SharePoint?). Mirror to Harbour Wind–style PQQ fixture. |
| 3–10 | Method | Open questionnaire + checklist; empty-library rule: mark requirements **MISSING** (no invented certs). Point at DRY-001 outcome: **22/22 MISSING**, export blocked. |
| 10–13 | Approver + security | Approver training bullets; open [`export-manifest-template.md`](../operations/export-manifest-template.md) shape; **Block export** while hard gaps open (`export_approved=no`). |
| 13–15 | Pilot terms | Cap: 4 weeks · ≤3 packs · £250–£750 ex VAT → [`pilot-offer-sheet.md`](pilot-offer-sheet.md). Script A only if legal gate PASS; else Script B hold. |

## Founder step table

| Step | Action | Fixture / artefact |
|------|--------|-------------------|
| 1 | State job: inbound pack → checklist → match → MISSING → Approver → export | [`discovery-one-pager.md`](discovery-one-pager.md) |
| 2 | Open redacted PQQ questionnaire | `testdata/redacted-pqq-v1/questionnaire.md` |
| 3 | Work checklist rows as **MISSING** (empty library) | Working copy of `evidence-checklist.md` |
| 4 | Say: “Library = approved evidence when we have it; today empty → honest gaps” | DRY-001 method |
| 5 | Approver pass: refuse export until gaps cleared or waived | [`approver-review-training.md`](../operations/approver-review-training.md) |
| 6 | Show manifest columns (blocked, not filled live approval) | [`export-manifest-template.md`](../operations/export-manifest-template.md) |
| 7 | Close with pilot outline or legal-hold | Offer sheet + legal gate |

## Talk tracks (~20s)

**SharePoint:** “SharePoint stores files. This walk-through is the missing checklist and Approver gate — we measure your last pack’s minutes separately; we don’t invent savings from this fixture.”

**AI risk:** “AI may draft later. Today we abstain: unsupported facts stay **MISSING**. Only a named Approver exports.”

**Constructionline:** “Membership profiles help schemes. This is the next OEM questionnaire in the inbox — different job.”

More rows: [`competitive-objection-sheet.md`](competitive-objection-sheet.md).

---

## After demo

1. Keep CRM **Discovery**; optional `notes=fixture_demo` ([`crm-stage-scripts.md`](crm-stage-scripts.md)).  
2. If pain fits → [`../research/discovery-pilot-offer-bridge.md`](../research/discovery-pilot-offer-bridge.md) → Script A/B per [`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md).  
3. Do **not** update [`../research/validation-scorecard.md`](../research/validation-scorecard.md) Actuals from the fixture demo.  
4. Book observation / interview follow-up if useful ([`../research/observation-kit-naame-hethel.md`](../research/observation-kit-naame-hethel.md)).

## Stop rules

- No SaaS UI tour or vapour feature walkthrough.  
- No live customer packs or uncleared MSA/DPA.  
- No win-rate / qualification claims.  
- No scorecard Actuals from DRY-001.  
- No filled export-manifest dry-run (that is **#85** / DRY-009).  
- No portal auto-submit claims.
