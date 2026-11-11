# Pilot data retention / deletion schedule

**Epic:** [#5](https://github.com/thesnjk/BidHarbour/issues/5)  
**Status:** Draft operational schedule for founder-run Supplier Desk pilots. **Advice required.** Not legal advice; **not** a substitute for a solicitor-cleared DPA/MSA.  
**Aligns with:** script **E** in [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md) · [`../research/pilot-design.md`](../research/pilot-design.md) data-handling · [`../security-and-legal/dpa-stub.md`](../security-and-legal/dpa-stub.md)  
**Product name:** Supplier Desk

**Rule:** Do not invent deletion/return Actuals in git. Live packs require cleared MSA/DPA. Customer evidence stays on local / encrypted paths — **never** committed.

## Clock

| Event | Timing |
|-------|--------|
| Pilot end | `pilot_end_date` (window closed or written stop / no continuation) |
| Delete or return deadline | **T+30 calendar days** after `pilot_end_date` |
| Continuation | Cleared paid subscription / MSA extension **suspends** the 30-day clock until that term ends; then this schedule applies again |

## Asset classes

| Asset | Location | At close-out (no continuation) |
|-------|----------|--------------------------------|
| Evidence folders / pack uploads | Local encrypted path | Return **or** secure delete per customer choice |
| Filled intake CSV copies | Local only (not git) | Return **or** secure delete |
| Draft checklists / match notes | Local | Return **or** secure delete |
| Export packs + Approver-signed manifests | Local / encrypted path | Return **or** secure delete |
| MISSING / close-out email copies | Named founder mailbox / local notes | Secure delete or redact after deadline unless needed for dispute (**Advice required**) |
| Metrics CSV process rows | Local metrics stub copy | Keep **aggregate** minutes / MISSING counts / rework loops **without** customer documents or identifiers beyond opaque `pack_id` if required for scorecard |
| Synthetic / fixture dry-runs (DRY-00x) | `testdata/` | Unchanged — not customer data |

## Customer choice (script E)

1. Prefer **return** via the agreed encrypted path, **or**  
2. Prefer **secure delete** — founder confirms in writing when complete  

If no reply by `reply_by`, founder follows the preference stated at kickoff / DPA; default operational intent is **secure delete** of customer materials by T+30 (**Advice required** if DPA says otherwise).

## Founder checklist

- [ ] Send script **E** with `pilot_end_date` and `reply_by`  
- [ ] Log return vs delete preference (local activity note — not git)  
- [ ] Execute return or secure delete by T+30  
- [ ] Wipe / revoke named founder account access to that customer’s materials  
- [ ] Write completion note: date, method (return/delete), accounts covered  
- [ ] Confirm no customer content used for model training  

## Stop rules

- No uncleared DPA/MSA stubs as customer contracts.  
- No model training on customer content.  
- No committing live customer files or filled intake CSVs.  
- No inventing “deletion complete” Actuals in the repo.  
- Dry-run fixtures alone are not scorecard GO evidence.
