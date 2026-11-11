# Synthetic customer-scoped answers v1 (Broads OEM)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**customer_id:** `broads-oem` (fictional buyer — Broads OEM Assemblies Ltd)  
**Org (fictional supplier):** East Anglia Precision Fabrication Ltd  
**Dry-run:** [`../../operations/pack-dry-run-dry-007.md`](../../operations/pack-dry-run-dry-007.md)  
**Shared library (unchanged):** [`../synthetic-evidence-library-v1/`](../synthetic-evidence-library-v1/)

## Purpose

Demonstrate **FO7**: after Pack 1, Approver may promote buyer-specific answers into a **customer-scoped** store without copying them into the shared / reusable library.

## Rules

1. Fixture only — not a live customer promotion.  
2. Rows here apply **only** when matching packs for `customer_id=broads-oem`.  
3. Harbour Wind / other buyers must **not** cite these rows.  
4. Do **not** merge into [`../synthetic-evidence-library-v1/approved-answers.csv`](../synthetic-evidence-library-v1/approved-answers.csv) without a second Approver decision and explicit `applies_to` change (out of scope for DRY-007).  
5. Do **not** increment validation scorecard Actuals from this fixture alone.

## Files

| File | Role |
|------|------|
| [`customer-scoped-answers.csv`](customer-scoped-answers.csv) | Broads-only promoted answers (`scope=customer`) |
