# Pack dry-run DRY-012 (expired library — Broads SQ)

**Date:** 2026-11-13  
**pack_id:** DRY-012  
**mode:** `dry_run`  
**as_of:** `2026-11-13`  
**Fixture:** [`../testdata/redacted-sq-v1/`](../testdata/redacted-sq-v1/) — Broads OEM Assemblies Ltd  
**Library:** [`../testdata/synthetic-evidence-library-v1-expired/`](../testdata/synthetic-evidence-library-v1-expired/) (base v1 unchanged)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · Approver: [`approver-review-training.md`](approver-review-training.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-004.md`](pack-dry-run-dry-004.md) (same fixture, valid-date partial library) · [`pack-dry-run-dry-005.md`](pack-dry-run-dry-005.md) (EXPIRED on Harbour Wind PQQ)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

**Thesis (Lead — EXPIRED on multi-customer SQ):** Same expired EL schedule (`ins_el`) that blocks Harbour Wind PQQ (DRY-005) also blocks **Broads SQ** export — no silent renew; buyer/SQ MISSING deltas remain.

## Method

1. Opened Broads SQ questionnaire + evidence checklist (`redacted-sq-v1`).  
2. Timer start: `2026-11-13T15:20:00Z`.  
3. Expired-library rule: for each of Q1–Q18, look up matching `doc_key` in [`../testdata/synthetic-evidence-library-v1-expired/approved-answers.csv`](../testdata/synthetic-evidence-library-v1-expired/approved-answers.csv).  
4. If `approval_status=approved` **and** `expiry_or_review_date` ≥ as_of **and** `applies_to` includes `both` or `sq` → status **draft** citing `evidence_label`.  
5. If `approval_status=approved` **and** `expiry_or_review_date` &lt; as_of → status **EXPIRED** (cite label; **not** export-ready; do not silent-fill a fresh cert).  
6. If `not_held` or buyer-specific → **MISSING** (no invented Broads answers).  
7. First complete draft = all 18 rows reviewed with library cite, EXPIRED, or MISSING.  
8. Approver gate: export blocked — Q7 **EXPIRED** + 6 Broads/SQ MISSING; one rework loop confirming intentional expired-library (not silent renew).  
9. No waiver (`export_approved=no` — gate demo; library ≠ export approval).  
10. Timer stop: `2026-11-13T15:20:40Z` → **1** minute (agent checklist confirmation).

## Outcome (Q1–Q18)

| Q | Topic | Status | Library / gap |
|---|-------|--------|---------------|
| 1 | Legal name / CH number | draft | `identity_ch` → SYNTH-CH-LETTERHEAD-v1 |
| 2 | Addresses | draft | `identity_address` → SYNTH-ADDRESS-LETTERHEAD-v1 |
| 3 | FTE / founded | draft | `identity_fte` → SYNTH-HR-FTE-v1 |
| 4 | ISO 9001 | draft | `hseq_iso9001` → SYNTH-ISO9001-v1 |
| 5 | ISO 14001 / 45001 | draft | `hseq_iso14001_45001` → SYNTH-ISO-NOTHELD-v1 |
| 6 | HSEQ lead | draft | `hseq_lead` → SYNTH-HSEQ-CV-v1 |
| 7 | EL insurance | **EXPIRED** | `ins_el` → SYNTH-EL-SCHED-v1 (expiry 2025-12-31 &lt; as_of) |
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

## Contrast

| Check | DRY-004 (valid partial) | DRY-005 (PQQ expired) | DRY-012 (this) |
|-------|-------------------------|------------------------|----------------|
| Fixture | Broads SQ | Harbour Wind PQQ | **Broads SQ** |
| Q EL / ins_el | draft | **EXPIRED** (Q9) | **EXPIRED** (Q7) |
| MISSING | 6/18 | 1 + draft-only | **6/18** (same Broads deltas) |
| Export | blocked | blocked | **blocked** |

**Unique proof:** EXPIRED EL gate holds on the **second-buyer** SQ fixture — multi-customer, no silent renew.

## Approver / export

| # | Result |
|---|--------|
| 1 | Export **blocked** — EXPIRED Q7; MISSING Q9–Q12, Q17–Q18 |
| 2 | Rework loop: confirmed expired-library intentional; no silent renew |
| Export | **Not approved** (`export_approved=no`) |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| pack_id | DRY-012 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-sq-v1+synthetic-evidence-library-v1-expired |
| received_at | 2026-11-13T15:20:00Z |
| completed_at | 2026-11-13T15:20:40Z |
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 6 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes`: Broads SQ + expired library; Q7 EL EXPIRED; 6 MISSING Broads deltas; Block export; see pack-dry-run-dry-012.md.
