# Synthetic evidence library v1 — stacked variant (DRY-013 only)

**Base library (unchanged):** [`../synthetic-evidence-library-v1/`](../synthetic-evidence-library-v1/)  
**Siblings:** [`../synthetic-evidence-library-v1-expired/`](../synthetic-evidence-library-v1-expired/) · [`../synthetic-evidence-library-v1-conflict/`](../synthetic-evidence-library-v1-conflict/)  
**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Evidence label:** Synthetic fixture only — not a real SME library.

## Purpose

Path A dry-run **DRY-013**: compose both single-delta forks so one PQQ pass hits **EXPIRED** (`ins_el`) **and** **CONFLICT** (`ins_pl` dual rows) together — then Approver **Block export** (unsigned). Export blocked without silent renew or newest-wins.

Do **not** use this folder for DRY-005/006 history; leave those variants and base v1 metrics as-of.

## Diff vs v1

| `doc_key` | Change |
|-----------|--------|
| `ins_el` | Expiry backdated to 2025-12-31 (same as expired variant) |
| `ins_pl` | Second in-date approved row `SYNTH-PL-SCHED-v2-RNW` (same as conflict variant) |

All other rows identical to v1.
