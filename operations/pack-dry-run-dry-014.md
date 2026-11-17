# Pack dry-run DRY-014 (FO7 dual-buyer scoped-export)

**Date:** 2026-11-17  
**pack_id:** DRY-014  
**mode:** `dry_run`  
**as_of:** `2026-11-17`  
**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2) · Refs [#154](https://github.com/thesnjk/BidHarbour/issues/154)  
**Pilot window (synthetic):** Pack 1 → Pack 2 (training only)  
**Pack 1:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) — Harbour Wind (shared library **only**)  
**Pack 2:** [`../testdata/redacted-sq-v1/`](../testdata/redacted-sq-v1/) — Broads OEM Assemblies Ltd (shared + FO7 scoped)  
**Shared library:** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/) (**unchanged**)  
**Customer-scoped store:** [`../testdata/synthetic-customer-scoped-answers-v1/`](../testdata/synthetic-customer-scoped-answers-v1/) (`customer_id=broads-oem`) — Pack 2 only  
**Broads scoped-export companion:** [`export-manifest-dry-014-broads.md`](export-manifest-dry-014-broads.md)  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · Approver: [`approver-review-training.md`](approver-review-training.md) · FO7 live (blank): [`pilot-fo7-live-writeback-playbook.md`](pilot-fo7-live-writeback-playbook.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Prior:** [`pack-dry-run-dry-007.md`](pack-dry-run-dry-007.md) (FO7 promotion) · [`pack-dry-run-dry-008.md`](pack-dry-run-dry-008.md) (dual-buyer window) · [`pack-dry-run-dry-009.md`](pack-dry-run-dry-009.md) (manifest discipline)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

**Thesis (Lead — multi-customer FO7):** Dual-buyer window export **stories** may include customer-scoped cites **only** on the matching buyer’s pack. Broads manifest lists three `SYNTH-BROADS-*` FO7 cites; Harbour Wind manifest lists **zero**. Shared library stays clean (`sq_*` still `not_held`). Residual MISSING still block export (`export_approved=no`) — scoped promotion ≠ export unlock.

## Method

1. Reuse DRY-008 dual-buyer match outcomes (do not rewrite library or scoped CSVs).  
2. Timer start: `2026-11-17T14:32:00Z`.  
3. **Pack 1 — Harbour Wind export story:** fill a control check (not a full 22-row twin): every cite must be shared-library only; scan for forbidden `SYNTH-BROADS-*` / `customer_id=broads-oem` → **zero**. Reuse DRY-003/008: **2/22 MISSING**; Approver **Block export**.  
4. **Pack 2 — Broads scoped-export manifest:** fill [`export-manifest-dry-014-broads.md`](export-manifest-dry-014-broads.md) from DRY-007 match — Q9/Q12/Q17 cite FO7 scoped labels with Status noting `scope=customer`; Q10/Q11/Q18 remain **MISSING** (blockers); shared rows as before.  
5. **FO7 export isolation:** Broads manifest may list `SYNTH-BROADS-OTD-v1`, `SYNTH-BROADS-SITE-v1`, `SYNTH-BROADS-QP-ACK-v1`; Harbour Wind control lists none of those.  
6. **Shared pollution check:** confirm shared `approved-answers.csv` still has Broads-promoted `doc_key`s as `not_held` (per DRY-007).  
7. Approver gate both packs: **Block export** on residual MISSING; no waiver; one rework loop confirming intentional non-export.  
8. Timer stop: `2026-11-17T14:32:45Z` → **1** minute (agent checklist confirmation of scoped-export isolation).

## Outcome — Pack 1 Harbour Wind (shared-only export story)

| Check | Result |
|-------|--------|
| Match / MISSING | **2/22** — per DRY-003/008 |
| Broads-scoped labels on export story? | **No** (zero `SYNTH-BROADS-*`) |
| Shared library pollution? | **None** |
| Export | **blocked** (`export_approved=no`) |

## Outcome — Pack 2 Broads (scoped cites on export story)

| Check | Result |
|-------|--------|
| Match / MISSING | **3/18** — per DRY-007/008 |
| FO7 scoped cites on manifest | **3** (OTD, site-visit, QP-ack) |
| Shared `sq_*` still `not_held`? | **Yes** |
| Export | **blocked** (`export_approved=no`) — residual MISSING |

## FO7 scoped-export allowed / forbidden

| Pack | Allowed on export story | Forbidden |
|------|-------------------------|-----------|
| Harbour Wind | Shared library cites only | Any `SYNTH-BROADS-*` or `broads-oem` scoped row |
| Broads | Shared + `customer_id=broads-oem` scoped cites | Another buyer’s scoped store; silent merge into shared |
| Either | Approver clear hard gaps or waiver before export | Newest-wins / invent to clear MISSING; treat FO7 cites as export unlock |

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| pack_id | DRY-014 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-pqq-v1→redacted-sq-v1+synthetic-evidence-library-v1+synthetic-customer-scoped-answers-v1 |
| received_at | 2026-11-17T14:32:00Z |
| completed_at | 2026-11-17T14:32:45Z |
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 3 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes`: FO7 dual-buyer scoped-export; Broads manifest lists 3 SYNTH-BROADS cites; Harbour Wind zero; shared untouched; both export blocked on residual MISSING; see pack-dry-run-dry-014.md / export-manifest-dry-014-broads.md.

## Stop rules

- Never invent live Approver Actuals or scorecard increments from this dry-run.  
- Never cite Broads-scoped labels on Harbour Wind (or any other buyer).  
- Never silent-merge FO7 rows into the shared library.  
- Dry-run wall-clock is **not** customer minutes-saved proof.
