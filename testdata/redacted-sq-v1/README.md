# Redacted SQ fixture v1 (synthetic)

**Purpose:** Second buyer pack for multi-customer dry-runs — same fictional SME, different SQ.  
**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2) concierge pilots.  
**Evidence label:** Synthetic fixture — **not** a real buyer questionnaire.

## Multi-customer thesis

| Pack | Buyer (fictional) | Type |
|------|-------------------|------|
| [`../redacted-pqq-v1/`](../redacted-pqq-v1/) | Harbour Wind Operations Ltd | Initial PQQ |
| **This fixture** | Broads OEM Assemblies Ltd | Annual SQ / approved-supplier review |

**Supplier under review (both packs):** East Anglia Precision Fabrication Ltd  

Overlap (reusable library): identity, ISO, insurance, modern slavery.  
Deltas: Broads-specific KPIs, site visit, quality plan acknowledgement, CAPA, conflicts vs Broads OEM (not Harbour Wind).

## Contents

| File | Role |
|------|------|
| [`questionnaire.md`](questionnaire.md) | Synthetic Broads OEM SQ questions |
| [`evidence-checklist.md`](evidence-checklist.md) | Map each question → evidence type, draft status, or **MISSING** |

## How to use (founder dry-run)

1. Time yourself against an empty or partial evidence library shared with PQQ v1.  
2. Cite a source **or** mark **MISSING** — never invent certifications/insurance.  
3. Approver gate before any export.  
4. Optional: log a separate metrics row (e.g. DRY-002) in `operations/pilot-metrics-stub.csv` — not required for this fixture PR.

## Rules

- Do **not** replace this with live customer packs until solicitor-cleared MSA/DPA.  
- Do **not** commit real certificates, policies, or financials into git.  
- Safe to share internally as process training only.
