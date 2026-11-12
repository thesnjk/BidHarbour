# Pack dry-run DRY-008 (dual-buyer pilot-window)

**Date:** 2026-11-11  
**pack_id:** DRY-008  
**mode:** `dry_run`  
**as_of:** `2026-11-11`  
**Pilot window (synthetic):** Pack 1 → Pack 2 in one 4-week-style window (training only)  
**Pack 1:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) — Harbour Wind (shared library **only**)  
**Pack 2:** [`../testdata/redacted-sq-v1/`](../testdata/redacted-sq-v1/) — Broads OEM Assemblies Ltd (shared + FO7 scoped)  
**Shared library:** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/) (**unchanged** across window)  
**Customer-scoped store:** [`../testdata/synthetic-customer-scoped-answers-v1/`](../testdata/synthetic-customer-scoped-answers-v1/) (`customer_id=broads-oem`) — Pack 2 only  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · Intake: [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md) · Approver: [`approver-review-training.md`](approver-review-training.md) · Closeout B intent: [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md)  
**Live Path B companion (packs 2–3):** [`pilot-repeat-pack-playbook.md`](pilot-repeat-pack-playbook.md) — dry-run ≠ live Actuals  
**Live dual-buyer window checklist:** [`pilot-dual-buyer-live-window-checklist.md`](pilot-dual-buyer-live-window-checklist.md) — training ≠ live proof  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md) (Harbour Wind partial) · [`pack-dry-run-dry-007.md`](pack-dry-run-dry-007.md) (FO7 Broads + Harbour Wind control)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

**Thesis (Lead vs Constructionline):** Same SME completes **two different buyer packs** in one pilot window; shared library stays clean; Broads-scoped answers never leak into Harbour Wind; both packs stay Approver-gated (`export_approved=no`).

## Method

1. Frame synthetic window: Pack 1 Harbour Wind PQQ, then Pack 2 Broads SQ (order matches backlog **#78**).  
2. Timer start: `2026-11-11T20:42:00Z`.  
3. **Pack 1 — Harbour Wind PQQ:** match against **shared library only** (ignore Broads-scoped CSV). Reuse DRY-003 outcomes: **2/22 MISSING** (Q3 group structure; Q22 `decl_conflicts_buyer`); Q15 draft-only case study. Confirm **zero** `SYNTH-BROADS-*` cites.  
4. Approver gate Pack 1: export **blocked**; one rework loop; no waiver.  
5. **In-window handoff (closeout B intent):** Pack 1 closed as blocked/training; shared `approved-answers.csv` **unchanged**; no silent merge of buyer-specific answers into shared. *(Not a live pilot Actual.)*  
6. **Pack 2 — Broads SQ:** match shared first, then `customer_id=broads-oem` scoped rows only. Reuse DRY-007 outcomes: **3/18 MISSING** (`sq_capa_open`, `sq_capa_sample`, `decl_conflicts_buyer`); **3** customer-scoped cites (OTD, site-visit, QP-ack).  
7. **FO7 check:** Pack 1 cites contain no Broads-scoped labels; Pack 2 may cite `SYNTH-BROADS-*` only for Broads.  
8. Approver gate Pack 2: export **blocked** on residual MISSING; one rework loop; no waiver.  
9. Timer stop: `2026-11-11T20:42:45Z` → **1** minute (agent checklist confirmation of dual-buyer sequence).

## Outcome — Pack 1 Harbour Wind (shared only)

| Check | Result |
|-------|--------|
| MISSING at first draft | **2/22** (Q3, Q22) — per DRY-003 |
| Broads-scoped labels cited? | **No** |
| Shared library pollution? | **None** |
| Export | **blocked** (`export_approved=no`) |

## Outcome — Pack 2 Broads (shared + FO7 scoped)

| Check | Result |
|-------|--------|
| MISSING at first draft | **3/18** (CAPA ×2 + buyer conflicts) — per DRY-007 |
| Customer-scoped cites | **3** (OTD, site-visit, QP-ack) |
| Shared `sq_*` still `not_held`? | **Yes** |
| Export | **blocked** (`export_approved=no`) |

## Approver / export (window)

| Pack | Result |
|------|--------|
| 1 Harbour Wind | Blocked — residual MISSING + draft-only case study; no waiver |
| 2 Broads | Blocked — residual MISSING; promotion ≠ export approval |
| Window | Both packs gated; dual-buyer isolation held |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| pack_id | DRY-008 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-pqq-v1→redacted-sq-v1+synthetic-evidence-library-v1+synthetic-customer-scoped-answers-v1 |
| received_at | 2026-11-11T20:42:00Z |
| completed_at | 2026-11-11T20:42:45Z |
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 3 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes`: dual-buyer window Pack1 Harbour Wind (2 MISSING, no Broads-scoped cites) → Pack2 Broads (3 MISSING, FO7 scoped); both export blocked; shared untouched.

## FO7 — pack-order allowed / forbidden

| Step | Allowed | Forbidden |
|------|---------|-----------|
| Pack 1 (Harbour Wind) | Shared library cites only | Cite `SYNTH-BROADS-*` or any `customer_id=broads-oem` row |
| After Pack 1 | Closeout B intent; keep shared clean | Silent copy Broads answers into shared |
| Pack 2 (Broads) | Shared + Broads-scoped rows | Cite another buyer’s scoped store |
| Either pack export | Approver clear hard gaps or waiver | Newest-wins / invent to clear MISSING |
