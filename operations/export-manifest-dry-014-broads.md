# Approver export manifest — DRY-014 Broads FO7 scoped-export (synthetic)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**pack_id:** DRY-014 (Pack 2 — Broads)  
**Method note:** [`pack-dry-run-dry-014.md`](pack-dry-run-dry-014.md)  
**Template:** [`export-manifest-template.md`](export-manifest-template.md)  
**Match prior:** [`pack-dry-run-dry-007.md`](pack-dry-run-dry-007.md) · dual-buyer: [`pack-dry-run-dry-008.md`](pack-dry-run-dry-008.md)  
**Scoped store:** [`../testdata/synthetic-customer-scoped-answers-v1/`](../testdata/synthetic-customer-scoped-answers-v1/)

**Evidence label:** Synthetic process training — **not** a live Approver Actual. Do **not** increment validation scorecard from this alone. `export_approved=no`.

## Pack header

| Field | Value |
|-------|-------|
| pack_id | DRY-014 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-sq-v1 + synthetic-evidence-library-v1 + synthetic-customer-scoped-answers-v1 |
| buyer / pack label | Broads OEM Assemblies Ltd (fixture SQ) |
| Named Approver | DR (synthetic dry-run role) |
| Draft prepared by | Path A operator (dry-run) |
| Date | 2026-11-17 |

## FO7 scoped cites (export story)

These three rows appear on the Broads export story only (`scope=customer`, `customer_id=broads-oem`). They must **not** appear on Harbour Wind.

| Req # | Topic / doc_key | evidence_label | Status | Scope note | Approver initials |
|-------|-----------------|----------------|--------|------------|-------------------|
| 9 | On-time delivery KPI / `sq_otd_kpi` | SYNTH-BROADS-OTD-v1 | approved (scoped) | FO7 — Broads only; **not** in shared library | DR |
| 12 | Site-visit readiness / `sq_site_visit` | SYNTH-BROADS-SITE-v1 | approved (scoped) | FO7 — Broads only | DR |
| 17 | Broads quality plan ack / `sq_broads_qp_ack` | SYNTH-BROADS-QP-ACK-v1 | approved (scoped) | FO7 — Broads only | DR |

## Residual blockers (export blocked)

| Req # | Topic / doc_key | Status | Notes |
|-------|-----------------|--------|-------|
| 10 | Open NCR / CAPA / `sq_capa_open` | MISSING | Not promoted; shared `not_held` |
| 11 | CAPA sample / `sq_capa_sample` | MISSING | Not promoted |
| 18 | Conflicts vs Broads OEM / `decl_conflicts_buyer` | MISSING | Not promoted |

Shared-library cites for other Broads SQ rows follow DRY-004/007 pattern (unchanged). Full 18-row twin not duplicated here — this companion proves **scoped cites on the correct buyer’s export story**.

## Approver declaration

| Field | Value |
|-------|-------|
| Decision | **Block export** |
| Blockers | Q10, Q11, Q18 MISSING |
| Waiver | none |
| FO7 check | Scoped cites present for Broads; confirm Harbour Wind control has zero `SYNTH-BROADS-*` |
| Shared pollution | none — `sq_otd_kpi` / `sq_site_visit` / `sq_broads_qp_ack` still `not_held` in shared CSV |
| export_approved | **no** |

## Stop rules

- Scoped cite on Broads ≠ licence to export while MISSING remain.  
- Do not copy these labels into a Harbour Wind (or other-buyer) manifest.  
- Do not merge FO7 rows into shared `approved-answers.csv` from this dry-run.
