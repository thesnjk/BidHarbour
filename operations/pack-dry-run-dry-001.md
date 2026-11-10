# Pack dry-run DRY-001 (empty library)

**Date:** 2026-11-10  
**pack_id:** DRY-001  
**mode:** `dry_run`  
**Fixture:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

## Method

1. Opened fixture questionnaire + evidence checklist (no separate evidence folder).  
2. Timer start: `2026-11-10T19:04:05Z`.  
3. Empty-library rule: for each of Q1–Q22, attach **no** fictional source; leave status **MISSING** with expected evidence type.  
4. First complete draft = all 22 rows reviewed and flagged MISSING.  
5. Approver gate (second pass): export blocked — required fields still MISSING; one rework loop to confirm empty library was intentional.  
6. No waiver granted for a live-looking export (`export_approved=no` — gate demo).  
7. Timer stop (first draft complete + Approver pass logged): `2026-11-10T19:04:35Z` → **1** minute (agent checklist confirmation; founder-paced Path A may take longer — re-time when training).

## Outcome (Q1–Q22)

| Q | Topic | Status | Expected evidence (gap) |
|---|-------|--------|-------------------------|
| 1 | Legal name / CH number | MISSING | Companies House extract or letterhead |
| 2 | Addresses | MISSING | Letterhead / lease / CH filing |
| 3 | Group structure | MISSING | Org chart or CH PSC |
| 4 | FTE / founded | MISSING | Internal HR note or accounts |
| 5 | ISO 9001 | MISSING | Certificate PDF (number, scope, expiry) |
| 6 | ISO 14001 / 45001 | MISSING | Certificate PDF or “not held” |
| 7 | RIDDOR | MISSING | HSEQ log (redacted) |
| 8 | HSEQ lead | MISSING | CV / role description |
| 9 | EL insurance | MISSING | Broker schedule |
| 10 | PL insurance | MISSING | Broker schedule |
| 11 | PI insurance | MISSING | Broker schedule or N/A rationale |
| 12 | Core processes | MISSING | Capability statement |
| 13 | Capacity envelope | MISSING | Shop specs / photos |
| 14 | Subcontractors | MISSING | Approved vendor list |
| 15 | Case study | MISSING | Redacted project note |
| 16 | Modern slavery | MISSING | Statement URL or threshold note |
| 17 | Dual-use / minerals | MISSING | Policy or N/A rationale |
| 18 | Cyber Essentials | MISSING | Certificate or “not held” |
| 19 | Payment terms | MISSING | Standard T&Cs |
| 20 | Quality plan / audit | MISSING | Signed acknowledgement |
| 21 | Adverse declarations | MISSING | Director declaration |
| 22 | Conflicts | MISSING | Declaration form |

## Approver gate

| Pass | Result |
|------|--------|
| 1 | Export **blocked** — 22/22 required items MISSING |
| Rework loop | Confirmed empty-library dry-run was intentional; still no invented answers |
| Export | **Not approved** (no waiver) — demonstrates Approver gate |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 22 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |
