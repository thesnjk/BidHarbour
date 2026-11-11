# Synthetic evidence library v1 — conflict variant (DRY-006 only)

**Base library (unchanged):** [`../synthetic-evidence-library-v1/`](../synthetic-evidence-library-v1/)  
**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Evidence label:** Synthetic fixture only — not a real SME library.

## Purpose

Path A dry-run **DRY-006**: same answers as v1 except **two** in-date `approved` rows for `ins_pl` with differing limits/labels → status **CONFLICT** on match; export blocked without silent pick of either schedule.

Do **not** use this folder for DRY-003/004/005 history; leave base v1 metrics as-of.

## Diff vs v1

| `doc_key` | Change |
|-----------|--------|
| `ins_pl` | Second row added: `SYNTH-PL-SCHED-v2-RNW` (£10m / SYNTH-PL-002-RNW / expiry 2027-06-30) alongside v1’s £5m `SYNTH-PL-SCHED-v1` |

All other rows identical to v1 (one row per key).
