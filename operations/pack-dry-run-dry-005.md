# Pack dry-run DRY-005 (expired library — PQQ)

**Date:** 2026-11-11  
**pack_id:** DRY-005  
**mode:** `dry_run`  
**as_of:** `2026-11-11`  
**Fixture:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/)  
**Library:** [`../testdata/synthetic-evidence-library-v1-expired/`](../testdata/synthetic-evidence-library-v1-expired/) (base v1 unchanged)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · Approver: [`approver-review-training.md`](approver-review-training.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md) (same fixture, valid-date partial library)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

## Method

1. Opened fixture questionnaire + evidence checklist.  
2. Timer start: `2026-11-11T15:58:00Z`.  
3. Expired-library rule: for each of Q1–Q22, look up matching `doc_key` in [`../testdata/synthetic-evidence-library-v1-expired/approved-answers.csv`](../testdata/synthetic-evidence-library-v1-expired/approved-answers.csv).  
4. If `approval_status=approved` **and** `expiry_or_review_date` ≥ as_of → status **draft** citing `evidence_label` (still Approver-gated).  
5. If `approval_status=approved` **and** `expiry_or_review_date` &lt; as_of → status **EXPIRED** (cite label; **not** export-ready; do not silent-fill a fresh cert).  
6. If `approval_status=draft` → status **draft** (case study — Approver required before reuse).  
7. If no `doc_key` or `not_held` → **MISSING**.  
8. First complete draft = all 22 rows reviewed with library cite, EXPIRED, or MISSING.  
9. Approver gate: export blocked — Q9 **EXPIRED** + Q22 **MISSING** + Q15 draft-only case study; one rework loop confirming intentional expired-library (not silent-fill).  
10. No waiver (`export_approved=no` — gate demo; library ≠ export approval).  
11. Timer stop: `2026-11-11T15:58:28Z` → **1** minute (agent checklist confirmation; founder-paced Path A may take longer — re-time when training).

## Outcome (Q1–Q22)

| Q | Topic | Status | Library / gap |
|---|-------|--------|---------------|
| 1 | Legal name / CH number | draft | `identity_ch` → SYNTH-CH-LETTERHEAD-v1 |
| 2 | Addresses | draft | `identity_address` → SYNTH-ADDRESS-LETTERHEAD-v1 |
| 3 | Group structure | draft | `identity_group` → SYNTH-GROUP-ORG-v1 |
| 4 | FTE / founded | draft | `identity_fte` → SYNTH-HR-FTE-v1 |
| 5 | ISO 9001 | draft | `hseq_iso9001` → SYNTH-ISO9001-v1 |
| 6 | ISO 14001 / 45001 | draft | `hseq_iso14001_45001` → SYNTH-ISO-NOTHELD-v1 |
| 7 | RIDDOR | draft | `hseq_riddor` → SYNTH-RIDDOR-LOG-v1 |
| 8 | HSEQ lead | draft | `hseq_lead` → SYNTH-HSEQ-CV-v1 |
| 9 | EL insurance | **EXPIRED** | `ins_el` → SYNTH-EL-SCHED-v1 (expiry 2025-12-31 &lt; as_of) |
| 10 | PL insurance | draft | `ins_pl` → SYNTH-PL-SCHED-v1 |
| 11 | PI insurance | draft | `ins_pi` → SYNTH-PI-NA-v1 |
| 12 | Core processes | draft | `cap_processes` → SYNTH-CAPABILITY-v1 |
| 13 | Capacity envelope | draft | `cap_envelope` → SYNTH-SHOP-SPEC-v1 |
| 14 | Subcontractors | draft | `cap_subcontractors` → SYNTH-AVL-v1 |
| 15 | Case study | draft | `cap_case_study` → SYNTH-CASE-DRAFT-v1 (**draft** row) |
| 16 | Modern slavery | draft | `ethics_msa` → SYNTH-MSA-THRESHOLD-v1 |
| 17 | Dual-use / minerals | draft | `ethics_dual_use` → SYNTH-DUALUSE-NA-v1 |
| 18 | Cyber Essentials | draft | `cyber_ce` → SYNTH-CE-NOTHELD-v1 |
| 19 | Payment terms | draft | `commercial_terms` → SYNTH-TERMS-v1 |
| 20 | Quality plan / audit | draft | `commercial_quality_ack_generic` → SYNTH-QP-ACK-GENERIC-v1 |
| 21 | Adverse declarations | draft | `decl_adverse` → SYNTH-ADVERSE-DECL-v1 |
| 22 | Conflicts | MISSING | `decl_conflicts_buyer` = `not_held` — buyer-named declaration |

## Contrast vs DRY-003

| Metric | DRY-003 (valid dates) | DRY-005 (expired `ins_el`) |
|--------|----------------------|----------------------------|
| MISSING at first draft | 2/22 (Q3, Q22) | **1/22** (Q22 only; Q3 now `identity_group`) |
| EXPIRED rows | 0 | **1** (Q9 EL) |
| Library cites (non-EXPIRED) | 20 | 20 drafts + 1 EXPIRED cite |
| Export | blocked (MISSING + draft) | blocked (**EXPIRED** + MISSING + draft) |

Demonstrates expiry gate without inventing a renewal cert or treating EXPIRED as silent MISSING fill.

## Approver gate

| Pass | Result |
|------|--------|
| 1 | Export **blocked** — Q9 EXPIRED; Q22 MISSING; Q15 draft-only |
| Rework loop | Confirmed expired-library dry-run was intentional; no silent-fill of EL schedule |
| Export | **Not approved** (no waiver) — library ≠ export approval |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 1 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes` call out Q9 **EXPIRED** separately (CSV has no EXPIRED column).
