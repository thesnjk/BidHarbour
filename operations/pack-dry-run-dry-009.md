# Pack dry-run DRY-009 (filled export manifest + Approver discipline)

**Date:** 2026-11-11  
**pack_id:** DRY-009  
**mode:** `dry_run`  
**as_of:** `2026-11-11`  
**Fixture:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) — Harbour Wind PQQ  
**Library:** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/) (unchanged)  
**Filled manifest:** [`export-manifest-dry-009-filled.md`](export-manifest-dry-009-filled.md)  
**Template:** [`export-manifest-template.md`](export-manifest-template.md)  
**Approver:** [`approver-review-training.md`](approver-review-training.md)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior match:** [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md) (partial library — 2/22 MISSING + Q15 draft-only)

**Evidence label:** Synthetic process training — **not** a live Approver Actual. Do **not** increment validation scorecard Actuals from this run alone.

**Thesis (Lead vs tender-AI autonomy):** A **complete** export manifest does **not** unlock export while hard gaps remain — human Approver discipline blocks (`export_approved=no`).

## Method

1. Reuse DRY-003 match outcomes on `redacted-pqq-v1` + `synthetic-evidence-library-v1` (do not rewrite library CSV).  
2. Timer start: `2026-11-11T22:40:00Z`.  
3. Translate checklist → filled manifest ([`export-manifest-dry-009-filled.md`](export-manifest-dry-009-filled.md)): all 22 rows; approved-library cites get Status `approved` + initials `DR`; Q3/Q22 → `MISSING`; Q15 → label present but Approver **withholds** initials (library draft-only).  
4. Approver walk per [`approver-review-training.md`](approver-review-training.md): row-by-row; no silent-fill of MISSING; draft-only ≠ export-ready.  
5. Tick **Block export**; list blockers in declaration Notes (Q3, Q15, Q22). No waiver.  
6. Export log: `export_approved=no`; formats none; portal auto-submit no.  
7. Timer stop: `2026-11-11T22:40:40Z` → **1** minute (agent checklist confirmation of manifest discipline).

## Outcome vs DRY-003

| Check | DRY-003 | DRY-009 |
|-------|---------|---------|
| Match / MISSING | 2/22 MISSING; Q15 draft-only | **Same** (reused) |
| Manifest rows filled | No | **Yes — 22/22** |
| Approver declaration | Summarised block | **Block export** on filled form |
| Export | blocked | **blocked** (`export_approved=no`) |

**Unique proof:** full manifest ≠ Approve export.

## Approver / export

| # | Result |
|---|--------|
| 1 | Export **blocked** — MISSING Q3/Q22 + draft-only Q15 |
| 2 | Rework loop: confirmed no silent-fill; library ≠ export approval |
| Export | **Not approved** (no waiver) |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| pack_id | DRY-009 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-pqq-v1 |
| received_at | 2026-11-11T22:40:00Z |
| completed_at | 2026-11-11T22:40:40Z |
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 2 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes`: partial-library + filled export manifest Approver block; see pack-dry-run-dry-009.md / export-manifest-dry-009-filled.md.
