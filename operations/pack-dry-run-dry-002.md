# Pack dry-run DRY-002 (empty library — SQ)

**Date:** 2026-11-10  
**pack_id:** DRY-002  
**mode:** `dry_run`  
**Fixture:** [`../testdata/redacted-sq-v1/`](../testdata/redacted-sq-v1/)  
**Buyer (fictional):** Broads OEM Assemblies Ltd  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-001.md`](pack-dry-run-dry-001.md) (PQQ / Harbour Wind)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

**Multi-customer note:** Empty library means overlap rows (identity/ISO/insurance) and Broads-specific rows (OTD, CAPA, quality-plan ack, conflicts) are all MISSING — Broads conflicts are **not** interchangeable with Harbour Wind PQQ answers even if a library existed.

## Method

1. Opened SQ questionnaire + evidence checklist (no evidence folder).  
2. Timer start: `2026-11-10T21:56:00Z`.  
3. Empty-library rule: for each of Q1–Q18, attach **no** fictional source; leave status **MISSING**.  
4. First complete draft = all 18 rows reviewed and flagged MISSING.  
5. Approver gate: export blocked — required fields MISSING; one rework loop confirming intentional empty library.  
6. No waiver (`export_approved=no` — gate demo).  
7. Timer stop: `2026-11-10T21:56:08Z` → **1** minute (agent checklist confirmation; founder-paced Path A may take longer — re-time when training).

## Outcome (Q1–Q18)

| Q | Topic | Status | Expected evidence (gap) |
|---|-------|--------|-------------------------|
| 1 | Legal name / CH number | MISSING | Companies House extract or letterhead |
| 2 | Addresses | MISSING | Letterhead / lease / CH filing |
| 3 | FTE / founded | MISSING | Internal HR note or accounts |
| 4 | ISO 9001 | MISSING | Certificate PDF (number, scope, expiry) |
| 5 | ISO 14001 / 45001 | MISSING | Certificate PDF or “not held” |
| 6 | HSEQ lead | MISSING | CV / role description |
| 7 | EL insurance | MISSING | Broker schedule |
| 8 | PL insurance | MISSING | Broker schedule |
| 9 | On-time delivery KPI | MISSING | ERP/export report or customer scorecard (Broads-specific) |
| 10 | Open NCR / CAPA count | MISSING | Quality log extract (Broads-specific) |
| 11 | CAPA sample | MISSING | Redacted CAPA record |
| 12 | Site-visit readiness | MISSING | Calendar / access note |
| 13 | Capacity envelope | MISSING | Shop specs / photos |
| 14 | Subcontractor control | MISSING | AVL + control procedure |
| 15 | Modern slavery | MISSING | Statement URL or threshold note |
| 16 | Cyber Essentials | MISSING | Certificate or “not held” |
| 17 | Broads quality plan ack | MISSING | Signed buyer-specific acknowledgement |
| 18 | Conflicts vs Broads OEM | MISSING | Declaration form (not Harbour Wind) |

## Approver gate

| Pass | Result |
|------|--------|
| 1 | Export **blocked** — 18/18 required items MISSING |
| Rework loop | Confirmed empty-library dry-run intentional; no invented answers |
| Export | **Not approved** (no waiver) |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 18 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |
