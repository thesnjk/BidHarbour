# Pack dry-run DRY-007 (customer-scoped promotion — FO7)

**Date:** 2026-11-11  
**pack_id:** DRY-007  
**mode:** `dry_run`  
**as_of:** `2026-11-11`  
**Pack A (re-match):** [`../testdata/redacted-sq-v1/`](../testdata/redacted-sq-v1/) — Broads OEM Assemblies Ltd  
**Pack B (control):** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) — Harbour Wind (shared library only)  
**Shared library:** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/) (**unchanged**)  
**Customer-scoped store:** [`../testdata/synthetic-customer-scoped-answers-v1/`](../testdata/synthetic-customer-scoped-answers-v1/) (`customer_id=broads-oem`)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · Intake: [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md) · Approver: [`approver-review-training.md`](approver-review-training.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-004.md`](pack-dry-run-dry-004.md) (Broads partial — 6 MISSING) · [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md) (Harbour Wind partial)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

**FO7 thesis:** Buyer-specific answers promoted after Pack 1 live in a **customer-scoped** store; the shared library stays clean so multi-customer packs do not silently inherit another buyer’s answers (Lead vs Constructionline-style single profile).

## Method

1. Treat DRY-004 Broads MISSING set as Pack-1 outcomes: `sq_otd_kpi`, `sq_capa_open`, `sq_capa_sample`, `sq_site_visit`, `sq_broads_qp_ack`, `decl_conflicts_buyer`.  
2. Approver promotes **three** Broads-only answers into [`../testdata/synthetic-customer-scoped-answers-v1/customer-scoped-answers.csv`](../testdata/synthetic-customer-scoped-answers-v1/customer-scoped-answers.csv): `sq_otd_kpi`, `sq_site_visit`, `sq_broads_qp_ack` (`scope=customer`, `customer_id=broads-oem`).  
3. Confirm shared [`approved-answers.csv`](../testdata/synthetic-evidence-library-v1/approved-answers.csv) still has those `doc_key`s as `not_held` — **no pollution**.  
4. Timer start: `2026-11-11T20:18:00Z`.  
5. **Re-match Broads SQ (Q1–Q18):** shared library first (`both`/`sq` approved); then customer-scoped rows **only if** `customer_id=broads-oem`; else MISSING.  
6. **Control — Harbour Wind PQQ:** match against **shared library only** (ignore Broads-scoped CSV). Confirm no Broads-scoped `evidence_label` appears. Residual gaps per DRY-003 remain (export still not a pass demo).  
7. Approver gate on Broads re-match: export blocked — residual MISSING (`sq_capa_open`, `sq_capa_sample`, `decl_conflicts_buyer`); one rework loop confirming intentional non-promotion of CAPA/conflicts.  
8. No waiver (`export_approved=no`).  
9. Timer stop: `2026-11-11T20:18:28Z` → **1** minute (agent checklist confirmation).

## Outcome — Broads SQ re-match (vs DRY-004)

| Q | Topic | DRY-004 | DRY-007 | Cite |
|---|--------|---------|---------|------|
| 9 | On-time delivery KPI | MISSING | **draft (customer-scoped)** | SYNTH-BROADS-OTD-v1 |
| 10 | Open NCR / CAPA count | MISSING | MISSING | still `not_held` shared; not promoted |
| 11 | CAPA sample | MISSING | MISSING | not promoted |
| 12 | Site-visit readiness | MISSING | **draft (customer-scoped)** | SYNTH-BROADS-SITE-v1 |
| 17 | Broads quality plan ack | MISSING | **draft (customer-scoped)** | SYNTH-BROADS-QP-ACK-v1 |
| 18 | Conflicts vs Broads OEM | MISSING | MISSING | not promoted |

Shared-row cites (Q1–Q8, Q13–Q16) unchanged from DRY-004 pattern (reusable library).

| Metric | DRY-004 | DRY-007 Broads |
|--------|---------|----------------|
| MISSING at first draft | 6/18 | **3/18** (Q10, Q11, Q18) |
| Customer-scoped cites | 0 | **3** |
| Shared library pollution | — | **None** (`sq_*` still `not_held` in shared CSV) |
| Export | blocked | blocked (residual MISSING; no waiver) |

## Outcome — Harbour Wind PQQ control (shared library only)

| Check | Result |
|-------|--------|
| Broads-scoped labels cited? | **No** |
| Shared library rows used? | Yes — same partial-library pattern as DRY-003 |
| Would citing SYNTH-BROADS-* be a FO7 failure? | **Yes** — forbidden |

## Approver / export

| # | Result |
|---|--------|
| 1 | Broads export **blocked** — 3/18 MISSING remain (CAPA ×2 + buyer conflicts) |
| 2 | Rework loop: confirmed only OTD / site-visit / QP-ack promoted to customer scope; CAPA + conflicts intentionally left MISSING |
| Export | **Not approved** (no waiver) — library promotion ≠ export approval |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| pack_id | DRY-007 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-sq-v1 + synthetic-customer-scoped-answers-v1 |
| received_at | 2026-11-11T20:18:00Z |
| completed_at | 2026-11-11T20:18:28Z |
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 3 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes` call out FO7 customer-scoped promotion; Harbour Wind control must not cite Broads-scoped rows.

## FO7 method note

| Step | Allowed | Forbidden |
|------|---------|-----------|
| After Pack 1 Approver | Promote buyer-specific answers → customer-scoped store | Silent copy into shared `approved-answers.csv` |
| Next Broads pack | Cite `customer_id=broads-oem` scoped rows | — |
| Other buyer pack | Shared library (+ that buyer’s own scope only) | Cite another buyer’s scoped answers |
| Promote to shared | Separate Approver + change `applies_to` / remove buyer wording | Newest-wins merge without review |
