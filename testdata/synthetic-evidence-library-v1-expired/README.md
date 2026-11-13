# Synthetic evidence library v1 — expired variant (DRY-005 / DRY-012)

**Base library (unchanged):** [`../synthetic-evidence-library-v1/`](../synthetic-evidence-library-v1/)  
**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Evidence label:** Synthetic fixture only — not a real SME library.

## Purpose

Path A dry-runs **DRY-005** (Harbour Wind PQQ) and **DRY-012** (Broads SQ): same answers as v1 except `ins_el` `expiry_or_review_date` = **2025-12-31** (past as-of **2026-11-11** / **2026-11-13**) → status **EXPIRED** on match; export blocked without silent fill.

Do **not** use this folder for DRY-003/004 history; leave base v1 metrics as-of.

## Diff vs v1

| `doc_key` | Change |
|-----------|--------|
| `ins_el` | Expiry backdated to 2025-12-31; answer text notes EXPIRED vs DRY-005 as-of |

All other rows identical to v1.
