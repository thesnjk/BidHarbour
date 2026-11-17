# Pack dry-run DRY-013 (stacked gates — EXPIRED + CONFLICT + unsigned Approver)

**Date:** 2026-11-17  
**pack_id:** DRY-013  
**mode:** `dry_run`  
**as_of:** `2026-11-17`  
**Fixture:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) — Harbour Wind PQQ  
**Library:** [`../testdata/synthetic-evidence-library-v1-stacked/`](../testdata/synthetic-evidence-library-v1-stacked/) (base v1 unchanged)  
**Manifest:** [`export-manifest-dry-013-filled.md`](export-manifest-dry-013-filled.md)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · Approver: [`approver-review-training.md`](approver-review-training.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-005.md`](pack-dry-run-dry-005.md) (EXPIRED) · [`pack-dry-run-dry-006.md`](pack-dry-run-dry-006.md) (CONFLICT) · [`pack-dry-run-dry-009.md`](pack-dry-run-dry-009.md) (Block export)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

**Thesis (Lead — composite Approver export gate):** One PQQ pack simultaneously surfaces **EXPIRED** (EL) + **CONFLICT** (PL dual labels) + **MISSING** (buyer conflicts) + draft-only case study; Approver ticks **Block export** and leaves **Approve export** unticked — no silent renew, no newest-wins, no unsigned unlock.

## Method

1. Opened Harbour Wind PQQ questionnaire + evidence checklist.  
2. Timer start: `2026-11-17T13:40:00Z`.  
3. Stacked-library rule: for each of Q1–Q22, look up matching `doc_key` in [`../testdata/synthetic-evidence-library-v1-stacked/approved-answers.csv`](../testdata/synthetic-evidence-library-v1-stacked/approved-answers.csv).  
4. Drop `not_held` / no key → **MISSING**.  
5. For `approved` with `expiry_or_review_date` &lt; as_of → **EXPIRED** (cite label; do not silent-fill a fresh cert).  
6. For remaining in-date `approved` rows: if **&gt;1** row for the same `doc_key` and (`evidence_label` differs **or** `answer_summary` materially differs) → **CONFLICT** — cite **both** labels; **no** newest-wins / silent pick.  
7. Single in-date `approved` → **draft** (Approver-gated).  
8. `approval_status=draft` → **draft** (case study).  
9. First complete draft = all 22 rows reviewed with library cite, EXPIRED, CONFLICT, or MISSING.  
10. Filled Approver manifest ([`export-manifest-dry-013-filled.md`](export-manifest-dry-013-filled.md)): **Block export** ticked; **Approve export** unticked (unsigned).  
11. Rework loop: confirmed stacked library intentional — no silent renew of EL; no pick of PL v2-RNW.  
12. No waiver (`export_approved=no`).  
13. Timer stop: `2026-11-17T13:40:40Z` → **1** minute (agent checklist confirmation; founder-paced Path A may take longer — re-time when training).

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
| 22 | Conflicts | MISSING | `decl_conflicts_buyer` = `not_held` — buyer-named |

## Contrast

| Check | DRY-005 | DRY-006 | DRY-009 | DRY-013 (this) |
|-------|---------|---------|---------|----------------|
| EXPIRED | Q9 | 0 | 0 | **Q9** |
| CONFLICT | 0 | Q10 | 0 | **Q10** |
| MISSING | Q22 | Q22 | Q3+Q22* | **Q22** |
| Filled manifest / Block | — | — | yes | **yes** (unsigned Approve) |
| Export | blocked | blocked | blocked | **blocked** |

\*DRY-009 used an older stub gap on Q3; current v1 has `identity_group`.

**Unique proof:** Multiple simultaneous hard library gates **plus** unsigned Approver Block on one pack.

## Approver / export

| # | Result |
|---|--------|
| 1 | Export **blocked** — EXPIRED Q9; CONFLICT Q10 (both PL labels); MISSING Q22; Q15 draft-only |
| 2 | Manifest: **Block export** ticked; **Approve export** unticked |
| 3 | Rework loop: stacked library intentional; no silent renew / newest-wins |
| Export | **Not approved** (`export_approved=no`) |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| pack_id | DRY-013 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-pqq-v1+synthetic-evidence-library-v1-stacked |
| received_at | 2026-11-17T13:40:00Z |
| completed_at | 2026-11-17T13:40:40Z |
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 1 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes`: stacked library; Q9 EL EXPIRED + Q10 PL CONFLICT (both labels) + Block export unsigned Approver; see pack-dry-run-dry-013.md / export-manifest-dry-013-filled.md.
