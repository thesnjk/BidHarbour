# Minutes-saved contrast rollup (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Lead gap:** minutes saved vs SharePoint / ad-hoc folder labour on inbound packs ([`../research/competitors.md`](../research/competitors.md))  
**Scorecard:** Time/value row in [`../research/validation-scorecard.md`](../research/validation-scorecard.md)  
**Product name:** Supplier Desk

**Evidence label:** Template / rollup home only until filled from **real** interview + kickoff baseline + **live** pilot metrics.  
**Do not** invent minutes, £ values, firm names, or scorecard Actuals in git.

## Purpose

Single place to compute **Time/value** contrast across:

1. Pre-pilot current-state (interview SharePoint / inbound-pack time-study)  
2. Path B-0 kickoff baseline (last comparable pack)  
3. Live pilot pack metrics (`minutes_to_first_draft`, support/rework)

## Rules

1. Never invent minute estimates or timesheets in the repo.  
2. **DRY-00x** rows in [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) are **not** customer contrast — ignore `mode=dry_run` for this rollup.  
3. Use only `mode` indicating a **live** / customer pilot pack when computing pass/fail.  
4. Do **not** write a scorecard Time/value Actual until at least one real live contrast row exists (prefer median across continuing pilots for the programme gate).  
5. Prefer anonymised CRM ids here; keep filled worksheets on the local encrypted path.

## Input sources

| Stage | Artefact | What to pull |
|-------|----------|--------------|
| Pre-pilot | [`../research/interview-sharepoint-time-study.md`](../research/interview-sharepoint-time-study.md) | Last inbound pack total admin minutes / tools (INT-ID) |
| Kickoff baseline | [`baseline-minutes-worksheet.md`](baseline-minutes-worksheet.md) | Total admin minutes (or agreed time-to-first-draft) for last comparable pack |
| Live pilot | [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) | `minutes_to_first_draft`, `support_minutes`, `rework_loops`; `export_approved`; live mode only |
| Design thresholds | [`../research/pilot-design.md`](../research/pilot-design.md) | ≥40% reduction **or** ≥90 min saved; £ value alternative on scorecard |

## Thresholds (pass definitions)

| Gate | Pass if (with real numbers only) |
|------|----------------------------------|
| Scorecard Time/value | Median ≥**90 min** saved **or** customer-stated ≥**£150**/pack value |
| Product promise (pilot-design) | ≥**40%** reduction vs baseline **or** ≥90 min saved |
| Programme | Prefer ≥3 live contrast rows before treating median as stable |

## How to compute (leave cells blank until real)

| Quantity | Formula |
|----------|---------|
| Minutes saved | `baseline_total − (minutes_to_first_draft + support_minutes)` *(adjust if kickoff agreed a different definition — document in Notes)* |
| % reduction | `minutes_saved / baseline_total × 100` |
| Pass (minutes) | `minutes_saved ≥ 90` **or** `% reduction ≥ 40` |
| Pass (£) | Stated pack value ≥ 150 **ex VAT** (only if customer volunteered) |

Optional: if interview time-study exists for the same CRM id and no kickoff baseline yet, note it under Pre-pilot minutes — **do not** treat interview alone as pilot pass.

## Rollup table (blank until real)

| CRM id | INT-ID (opt.) | Pack id (live) | Baseline total min | Pilot first-draft min | Support min | Minutes saved | % reduction | £ value (if stated) | Pass? | Evidence paths |
|--------|---------------|----------------|--------------------|-----------------------|-------------|---------------|-------------|---------------------|-------|----------------|
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |

**Median minutes saved (live rows only):** _(blank)_  
**Scorecard Time/value Actual update:** only after real median / £ evidence — link this file + baseline + CSV row ids in the Evidence IDs cell.

## Operator checklist

- [ ] Interview time-study filled only from real INT-ID (if used)  
- [ ] Kickoff baseline filled from real Path B-0 workshop  
- [ ] Live metrics row(s) exist with non-dry_run mode  
- [ ] Contrast computed with formulas above; no DRY minutes mixed in  
- [ ] Scorecard Actual left blank until evidence exists; then cite this rollup  

## Related

- Kickoff: [`pilot-kickoff-checklist.md`](pilot-kickoff-checklist.md) §2 Baseline workshop  
- Path B logging: [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
- Continuation (separate gate): [`pilot-continuation-log.md`](pilot-continuation-log.md)  
