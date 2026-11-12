# Pack dry-run DRY-010 (waiver discipline — waiver ≠ Approver Approve)

**Date:** 2026-11-12  
**pack_id:** DRY-010  
**mode:** `dry_run`  
**as_of:** `2026-11-12`  
**Fixture:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) — Harbour Wind PQQ  
**Library:** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/) (unchanged)  
**Filled manifest:** [`export-manifest-dry-010-filled.md`](export-manifest-dry-010-filled.md)  
**Template:** [`export-manifest-template.md`](export-manifest-template.md)  
**Approver:** [`approver-review-training.md`](approver-review-training.md)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior match:** [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md) (partial library — 2/22 MISSING + Q15 draft-only)  
**Contrast:** [`pack-dry-run-dry-009.md`](pack-dry-run-dry-009.md) (filled manifest; no waiver)

**Evidence label:** Synthetic process training — **not** a live Approver Actual. Do **not** increment validation scorecard Actuals from this run alone.

**Thesis (Lead vs Approver bypass):** A **recorded row waiver** does **not** unlock export without Approver ticking **Approve export** — waiver ≠ silent pass (`export_approved=no`).

## Method

1. Reuse DRY-003 match outcomes on `redacted-pqq-v1` + `synthetic-evidence-library-v1` (do not rewrite library CSV).  
2. Timer start: `2026-11-12T00:05:00Z`.  
3. Translate checklist → filled manifest ([`export-manifest-dry-010-filled.md`](export-manifest-dry-010-filled.md)): all 22 rows; approved-library cites get Status `approved` + initials `DR`; Q3 → Status `waived` with **operator-proposed** note (no Approver Approve); Q22 → `MISSING`; Q15 → label present, initials withheld (draft-only).  
4. Approver walk per [`approver-review-training.md`](approver-review-training.md): row waiver without Approve does not unlock; remaining MISSING / draft-only still block.  
5. Tick **Block export** (Approve unticked); blockers in Notes (Q3 operator-waiver without Approve, Q15, Q22).  
6. Export log: `export_approved=no`; formats none; portal auto-submit no.  
7. Timer stop: `2026-11-12T00:05:40Z` → **1** minute (agent checklist confirmation of waiver discipline).

## Outcome vs DRY-009

| Check | DRY-009 | DRY-010 |
|-------|---------|---------|
| Match / MISSING | 2/22 + Q15 draft-only | **Same** (reused) |
| Q3 status | MISSING | **waived** (operator-proposed) |
| Approver declaration | Block export | **Block export** (Approve unticked) |
| Export | blocked | **blocked** (`export_approved=no`) |

**Unique proof:** recorded waiver ≠ Approve export / Approver bypass.

## Approver / export

| # | Result |
|---|--------|
| 1 | Export **blocked** — operator Q3 waiver without Approve; MISSING Q22; draft-only Q15 |
| 2 | Rework loop: confirmed waiver row ≠ silent unlock |
| Export | **Not approved** |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| pack_id | DRY-010 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-pqq-v1 |
| received_at | 2026-11-12T00:05:00Z |
| completed_at | 2026-11-12T00:05:40Z |
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 2 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes`: partial-library + operator Q3 waiver without Approver Approve; Block export; see pack-dry-run-dry-010.md / export-manifest-dry-010-filled.md.
