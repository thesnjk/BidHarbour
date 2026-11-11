# Pack dry-run DRY-006 (conflict library — PQQ)

**Date:** 2026-11-11  
**pack_id:** DRY-006  
**mode:** `dry_run`  
**as_of:** `2026-11-11`  
**Fixture:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/)  
**Library:** [`../testdata/synthetic-evidence-library-v1-conflict/`](../testdata/synthetic-evidence-library-v1-conflict/) (base v1 unchanged)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · Approver: [`approver-review-training.md`](approver-review-training.md) · Manifest: [`export-manifest-template.md`](export-manifest-template.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-005.md`](pack-dry-run-dry-005.md) (EXPIRED) · [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md) (partial)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

## Method

1. Opened fixture questionnaire + evidence checklist.  
2. Timer start: `2026-11-11T19:05:00Z`.  
3. Conflict-library rule: for each of Q1–Q22, look up matching `doc_key` in [`../testdata/synthetic-evidence-library-v1-conflict/approved-answers.csv`](../testdata/synthetic-evidence-library-v1-conflict/approved-answers.csv).  
4. Drop `not_held` / no key → **MISSING**.  
5. For `approved` with `expiry_or_review_date` &lt; as_of → **EXPIRED**.  
6. For remaining in-date `approved` rows: if **&gt;1** row for the same `doc_key` and (`evidence_label` differs **or** `answer_summary` materially differs) → **CONFLICT** — cite **both** labels; **no** newest-wins / silent pick.  
7. Single in-date `approved` → **draft** (Approver-gated).  
8. `approval_status=draft` → **draft** (case study).  
9. First complete draft = all 22 rows reviewed with library cite, CONFLICT, EXPIRED, or MISSING.  
10. Approver gate: export blocked — Q10 **CONFLICT** + Q22 **MISSING** + Q15 draft-only; one rework loop confirming intentional conflict-library (not silent pick of v2-RNW).  
11. No waiver (`export_approved=no`).  
12. Timer stop: `2026-11-11T19:05:28Z` → **1** minute (agent checklist confirmation; founder-paced Path A may take longer — re-time when training).

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
| 9 | EL insurance | draft | `ins_el` → SYNTH-EL-SCHED-v1 |
| 10 | PL insurance | **CONFLICT** | `ins_pl` → SYNTH-PL-SCHED-v1 **and** SYNTH-PL-SCHED-v2-RNW (£5m vs £10m) |
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
| 22 | Conflicts | MISSING | `decl_conflicts_buyer` = `not_held` — buyer-named (not library CONFLICT) |

## Contrast vs DRY-003 / DRY-005

| Metric | DRY-003 (v1) | DRY-005 (expired) | DRY-006 (conflict) |
|--------|--------------|-------------------|---------------------|
| MISSING at first draft | 2/22 | 1/22 | **1/22** (Q22) |
| EXPIRED | 0 | 1 (Q9) | 0 |
| CONFLICT | 0 | 0 | **1** (Q10) |
| Export | blocked | blocked | blocked (**CONFLICT** + MISSING + draft) |

Demonstrates duplicate in-date library conflict without silent pick or inventing a “winning” schedule.

## Approver gate

| Pass | Result |
|------|--------|
| 1 | Export **blocked** — Q10 CONFLICT (both PL labels); Q22 MISSING; Q15 draft-only |
| Rework loop | Confirmed conflict-library intentional; listed both `evidence_label`s in Notes; no silent pick of v2-RNW |
| Export | **Not approved** (no waiver) — library ≠ export approval |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 1 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes` call out Q10 **CONFLICT** separately (CSV has no CONFLICT column).
