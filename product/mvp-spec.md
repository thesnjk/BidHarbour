# 11. Product strategy and MVP

**As-of:** 9 November 2025  
**Build only after validation scorecard GO.**

## Product vision

A practical, trustworthy supplier-side desk that turns each customer qualification request into a complete, evidence-backed, human-approved response pack.

## Core use case

Organisation receives a customer PQQ/SQ pack → uploads → checklist → matches approved library → resolves gaps → authorised approver signs off → exports pack with audit trail.

## Must-have capabilities (MoSCoW)

| Priority | Capability |
|----------|------------|
| **Must** | Organisation workspace; user roles; approved evidence library; approved reusable answers; document ownership + review/expiry dates; incoming request upload; requirement checklist; evidence matching; missing-information queue; human review and approval; exportable pack; activity history; customer data export and deletion |
| **Should** | Email ingest; expiry dashboard; bulk import; basic notifications |
| **Could** | OCR-heavy tables; customer-specific answer overrides UI; API |
| **Not now** | Buyer portal; auto-submit to customer systems; certification issuance; engineering estimating; public tender discovery; autonomous compliance answers |

## Explicit exclusions

No invented certifications/policies/insurance/financials; no bid-win guarantees; no generic DMS repositioning; no supplier directory.

## User stories and acceptance criteria (Must)

1. **As** an admin, **I can** create an organisation workspace and invite users with roles (Admin, Editor, Approver, Viewer)  
   **AC:** Role enforced on approve/export; MFA available.

2. **As** an editor, **I can** upload documents into the evidence library with owner and review/expiry date  
   **AC:** Version retained; expired items flagged in match.

3. **As** an editor, **I can** store approved reusable answers linked to evidence  
   **AC:** Answer cannot be marked approved without Approver role; source DocumentVersion required or explicit “policy text owned by org” flag.

4. **As** an editor, **I can** upload an incoming customer request pack and get an editable requirement checklist  
   **AC:** User can add/edit/delete requirements; uncertain extractions marked Uncertain.

5. **As** an editor, **I can** see matches and a missing/expired/conflict queue  
   **AC:** Every match shows provenance link; conflicts listed explicitly.

6. **As** an approver, **I can** approve or reject sections before export  
   **AC:** Export blocked while required items unapproved or missing (unless explicit waiver recorded).

7. **As** an admin, **I can** export a pack and view activity history  
   **AC:** Export includes manifest of evidence versions; AuditEvent written.

8. **As** an admin, **I can** export and delete organisation data  
   **AC:** Deletion completes per DPA timeline; confirmed in UI.

## Dependencies

Auth provider; object storage; OCR/LLM under DPA; Stripe (billing); legal stubs approved for production language.

## Release criteria

- Two pilot customers complete one real pack on software  
- Zero cross-tenant access in security smoke tests  
- Export gate tests pass  
- Support runbook published  
- Privacy notice + DPA in force

## What stays manual initially

Complex table extraction cleanup; customer-specific Word formatting; first library taxonomy design; edge-case conflict resolution.
