# Pilot repeat-usage tracker (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** each live pack close (especially pack 2/3) or Friday rollup  
**Scorecard:** [`../research/validation-scorecard.md`](../research/validation-scorecard.md) Repeat usage (≥2 packs / continuing customer / 60d)  
**Week-8 gate:** [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md)  
**Companions:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) · [`pilot-repeat-pack-playbook.md`](pilot-repeat-pack-playbook.md) · [`pilot-continuation-log.md`](pilot-continuation-log.md) · [`path-b-first-live-pack-intake.md`](path-b-first-live-pack-intake.md) · [`../research/scorecard-actuals-hygiene.md`](../research/scorecard-actuals-hygiene.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** live packs.  
**Do not** invent pack counts, dates, or scorecard Actuals in git. Prefer anonymised IDs; keep sensitive detail on the local encrypted path.

## Goal

Track whether a **continuing** customer completed ≥**2** live packs within **60 days** of their first live pack — honest input for scorecard Repeat usage / Week-8 — without treating dry-run sequences as proof.

## Rules

1. Count only metrics rows with `mode=live` for that customer (pack_ids `P01`/`P02`/`P03` or equivalent).  
2. **Window start** = date of first live pack `received_at` (or kickoff start if first pack same day — note which). Pass = ≥2 live packs with `completed_at` (or export decision date) within **60 days** of window start.  
3. Dry-runs (DRY-00x), including DRY-008 dual-buyer, are **not** repeat usage — never copy them here as GO evidence.  
4. Continuation `yes` alone is **not** repeat usage until a second **live** pack is logged.  
5. Scorecard Repeat usage Actual updates **only** from real pass rows (leave Actual `—` until then).  
6. At Week-8: copy pass/fail into the gate checklist Repeat usage field.

## Log (blank until real)

| Customer (or anonymised) | CRM id | Window start | Pack ids + dates (live) | Pack count | Pass (≥2 in 60d)? (Y/N/blank) | Logged by | Notes |
|--------------------------|--------|--------------|-------------------------|------------|-------------------------------|-----------|-------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Customers with ≥1 live pack | 0 |
| Customers with ≥2 live packs in 60d (pass) | 0 |
| Customers still short of 2 packs | 0 |

## Founder checklist

- [ ] After each live pack: ensure metrics CSV row exists (`mode=live`)  
- [ ] Update or add tracker row with pack_id + date  
- [ ] Recompute pack count and 60d pass  
- [ ] Update scorecard Repeat usage Actual only from real passes  
- [ ] At Week-8: paste outcome into [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md)  
- [ ] Do **not** invent a second pack to pass the gate  

## Stop rules

- Never invent live packs or pack dates.  
- Never treat DRY sequences as Repeat usage proof.  
- Continuation yes ≠ second pack.  
- Never commit confidential pack content with this log.
