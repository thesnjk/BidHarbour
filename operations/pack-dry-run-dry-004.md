# Pack dry-run DRY-004 (partial library — SQ)

**Date:** 2026-11-11  
**pack_id:** DRY-004  
**mode:** `dry_run`  
**Fixture:** [`../testdata/redacted-sq-v1/`](../testdata/redacted-sq-v1/)  
**Buyer (fictional):** Broads OEM Assemblies Ltd  
**Library:** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/)  
**Runbook:** Path A partial-library in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-002.md`](pack-dry-run-dry-002.md) (same fixture, empty library — 18 MISSING) · [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md) (PQQ partial)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

**Multi-customer note:** Shared identity/HSEQ/insurance/capacity/ethics rows can cite the reusable library; Broads-specific SQ deltas (`sq_*`) and buyer conflicts stay **MISSING** — not interchangeable with Harbour Wind PQQ answers.

## Method

1. Opened SQ questionnaire + evidence checklist.  
2. Timer start: `2026-11-11T12:14:48Z`.  
3. Partial-library rule: for each of Q1–Q18, look up matching `doc_key` in [`../testdata/synthetic-evidence-library-v1/approved-answers.csv`](../testdata/synthetic-evidence-library-v1/approved-answers.csv).  
4. If `approval_status=approved` and `applies_to` includes `both` or `sq` → status **draft** citing `evidence_label`.  
5. If `not_held` or buyer-specific → **MISSING** (no invented Broads answers).  
6. First complete draft = all 18 rows reviewed with library cite or MISSING.  
7. Approver gate: export blocked — 6 MISSING; one rework loop confirming intentional partial library + multi-customer thesis.  
8. No waiver (`export_approved=no` — gate demo; library ≠ export approval).  
9. Timer stop: `2026-11-11T12:15:15Z` → **1** minute (agent checklist confirmation; founder-paced Path A may take longer — re-time when training).

## Outcome (Q1–Q18)

| Q | Topic | Status | Library / gap |
|---|-------|--------|---------------|
| 1 | Legal name / CH number | draft | `identity_ch` → SYNTH-CH-LETTERHEAD-v1 |
| 2 | Addresses | draft | `identity_address` → SYNTH-ADDRESS-LETTERHEAD-v1 |
| 3 | FTE / founded | draft | `identity_fte` → SYNTH-HR-FTE-v1 |
| 4 | ISO 9001 | draft | `hseq_iso9001` → SYNTH-ISO9001-v1 |
| 5 | ISO 14001 / 45001 | draft | `hseq_iso14001_45001` → SYNTH-ISO-NOTHELD-v1 |
| 6 | HSEQ lead | draft | `hseq_lead` → SYNTH-HSEQ-CV-v1 |
| 7 | EL insurance | draft | `ins_el` → SYNTH-EL-SCHED-v1 |
| 8 | PL insurance | draft | `ins_pl` → SYNTH-PL-SCHED-v1 |
| 9 | On-time delivery KPI | MISSING | `sq_otd_kpi` = `not_held` — Broads-specific |
| 10 | Open NCR / CAPA count | MISSING | `sq_capa_open` = `not_held` |
| 11 | CAPA sample | MISSING | `sq_capa_sample` = `not_held` |
| 12 | Site-visit readiness | MISSING | `sq_site_visit` = `not_held` |
| 13 | Capacity envelope | draft | `cap_envelope` → SYNTH-SHOP-SPEC-v1 |
| 14 | Subcontractor control | draft | `cap_subcontractors` → SYNTH-AVL-v1 |
| 15 | Modern slavery | draft | `ethics_msa` → SYNTH-MSA-THRESHOLD-v1 |
| 16 | Cyber Essentials | draft | `cyber_ce` → SYNTH-CE-NOTHELD-v1 |
| 17 | Broads quality plan ack | MISSING | `sq_broads_qp_ack` = `not_held` — buyer-specific |
| 18 | Conflicts vs Broads OEM | MISSING | `decl_conflicts_buyer` = `not_held` |

## Contrast vs DRY-002

| Metric | DRY-002 (empty) | DRY-004 (partial) |
|--------|-----------------|-------------------|
| MISSING at first draft | 18/18 | **6/18** (Q9–Q12, Q17–Q18) |
| Library cites | 0 | 12 |
| Export | blocked | blocked (Broads MISSING remain) |

Demonstrates multi-customer MISSING differentiation: reusable library helps shared rows; buyer/SQ deltas stay gaps.

## Approver gate

| Pass | Result |
|------|--------|
| 1 | Export **blocked** — 6/18 MISSING (Broads/SQ deltas) |
| Rework loop | Confirmed partial-library dry-run was intentional; no silent-fill of Broads rows from Harbour Wind |
| Export | **Not approved** (no waiver) — library ≠ export approval |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 6 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |
