# Pack dry-run DRY-003 (partial library — PQQ)

**Date:** 2026-11-11  
**pack_id:** DRY-003  
**mode:** `dry_run`  
**Fixture:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/)  
**Library:** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/)  
**Runbook:** Path A partial-library in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-001.md`](pack-dry-run-dry-001.md) (same fixture, empty library — 22 MISSING)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

## Method

1. Opened fixture questionnaire + evidence checklist.  
2. Timer start: `2026-11-11T11:55:51Z`.  
3. Partial-library rule: for each of Q1–Q22, look up matching `doc_key` in [`../testdata/synthetic-evidence-library-v1/approved-answers.csv`](../testdata/synthetic-evidence-library-v1/approved-answers.csv).  
4. If `approval_status=approved` → status **draft** citing `evidence_label` (still Approver-gated).  
5. If `approval_status=draft` → status **draft** (case study — Approver required before reuse).  
6. If no `doc_key` or `not_held` → **MISSING** (no invented certs beyond stub).  
7. First complete draft = all 22 rows reviewed with library cite or MISSING.  
8. Approver gate: export blocked — 2 MISSING + 1 draft-only case study; one rework loop confirming intentional partial library (not silent-fill).  
9. No waiver (`export_approved=no` — gate demo; library ≠ export approval).  
10. Timer stop: `2026-11-11T11:56:20Z` → **1** minute (agent checklist confirmation; founder-paced Path A may take longer — re-time when training).

## Outcome (Q1–Q22)

| Q | Topic | Status | Library / gap |
|---|-------|--------|---------------|
| 1 | Legal name / CH number | draft | `identity_ch` → SYNTH-CH-LETTERHEAD-v1 |
| 2 | Addresses | draft | `identity_address` → SYNTH-ADDRESS-LETTERHEAD-v1 |
| 3 | Group structure | MISSING | No `doc_key` in stub — org chart / CH PSC gap |
| 4 | FTE / founded | draft | `identity_fte` → SYNTH-HR-FTE-v1 |
| 5 | ISO 9001 | draft | `hseq_iso9001` → SYNTH-ISO9001-v1 |
| 6 | ISO 14001 / 45001 | draft | `hseq_iso14001_45001` → SYNTH-ISO-NOTHELD-v1 |
| 7 | RIDDOR | draft | `hseq_riddor` → SYNTH-RIDDOR-LOG-v1 |
| 8 | HSEQ lead | draft | `hseq_lead` → SYNTH-HSEQ-CV-v1 |
| 9 | EL insurance | draft | `ins_el` → SYNTH-EL-SCHED-v1 |
| 10 | PL insurance | draft | `ins_pl` → SYNTH-PL-SCHED-v1 |
| 11 | PI insurance | draft | `ins_pi` → SYNTH-PI-NA-v1 |
| 12 | Core processes | draft | `cap_processes` → SYNTH-CAPABILITY-v1 |
| 13 | Capacity envelope | draft | `cap_envelope` → SYNTH-SHOP-SPEC-v1 |
| 14 | Subcontractors | draft | `cap_subcontractors` → SYNTH-AVL-v1 |
| 15 | Case study | draft | `cap_case_study` → SYNTH-CASE-DRAFT-v1 (**draft** row — Approver before reuse) |
| 16 | Modern slavery | draft | `ethics_msa` → SYNTH-MSA-THRESHOLD-v1 |
| 17 | Dual-use / minerals | draft | `ethics_dual_use` → SYNTH-DUALUSE-NA-v1 |
| 18 | Cyber Essentials | draft | `cyber_ce` → SYNTH-CE-NOTHELD-v1 |
| 19 | Payment terms | draft | `commercial_terms` → SYNTH-TERMS-v1 |
| 20 | Quality plan / audit | draft | `commercial_quality_ack_generic` → SYNTH-QP-ACK-GENERIC-v1 |
| 21 | Adverse declarations | draft | `decl_adverse` → SYNTH-ADVERSE-DECL-v1 |
| 22 | Conflicts | MISSING | `decl_conflicts_buyer` = `not_held` — buyer-named declaration |

## Contrast vs DRY-001

| Metric | DRY-001 (empty) | DRY-003 (partial) |
|--------|-----------------|-------------------|
| MISSING at first draft | 22/22 | **2/22** (Q3, Q22) |
| Library cites | 0 | 20 (19 approved + 1 draft case study) |
| Export | blocked | blocked (MISSING + draft case study) |

Demonstrates measurable MISSING differentiation without inventing evidence beyond the synthetic stub.

## Approver gate

| Pass | Result |
|------|--------|
| 1 | Export **blocked** — 2/22 MISSING; Q15 still draft-only |
| Rework loop | Confirmed partial-library dry-run was intentional; no silent-fill of Q3/Q22 |
| Export | **Not approved** (no waiver) — library ≠ export approval |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 2 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |
