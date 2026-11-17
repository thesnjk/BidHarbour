# Path A pilot per-pack clock-time log (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** each Path A pack (DRY training / founder re-time) **or** Path B live pack close  
**Lead gap:** minutes saved vs SharePoint / ad-hoc folders — unproven until **live** contrast  
**Scorecard:** [`../research/validation-scorecard.md`](../research/validation-scorecard.md) Time/value (via rollup only)  
**Companions:** [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) (Path A 1–6 · Metrics ritual) · [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) · [`baseline-minutes-worksheet.md`](baseline-minutes-worksheet.md) · [`minutes-saved-contrast-rollup.md`](minutes-saved-contrast-rollup.md) · [`../research/interview-sharepoint-time-study.md`](../research/interview-sharepoint-time-study.md) · [`../research/scorecard-actuals-hygiene.md`](../research/scorecard-actuals-hygiene.md) · [`../commercial/minutes-saved-leave-behind.md`](../commercial/minutes-saved-leave-behind.md) · live clock → leave-behind → [`../commercial/path-a-clock-to-leavebehind-bridge.md`](../commercial/path-a-clock-to-leavebehind-bridge.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** timers.  
**Do not** invent clocks, baselines, interview minutes, or scorecard Actuals in git. Prefer anonymised pack IDs; keep customer detail on the local encrypted path.

## Goal

One phased per-pack clock ledger so founder re-timing and live packs produce honest `minutes_to_first_draft` (and notes) — feeding metrics CSV always, and Time/value **only** when `mode=live` via the contrast rollup.

## Rules

1. Start/stop wall-clock for each phase below; total to first draft must match the metrics CSV row for that `pack_id`.  
2. `mode=dry_run` (Path A / DRY-00x) = **training / method only** — never copy into scorecard Time/value or treat as customer minutes saved.  
3. `mode=live` (Path B) may feed [`minutes-saved-contrast-rollup.md`](minutes-saved-contrast-rollup.md) with kickoff baseline — still never invent.  
4. Support chase minutes stay in `support_minutes` / [`pilot-support-burden-log.md`](pilot-support-burden-log.md) — not in draft wall-clock.  
5. Agent-paced DRY stubs (~1 min) are construct-invalid for GO; founder-paced Path A re-time when training.

## Phase definitions (Path A steps 1–6)

| Phase | Maps to | Start | Stop |
|-------|---------|-------|------|
| P1 Open pack | Path A §1–2 | Questionnaire + checklist open | Working copy ready |
| P2 Extract / map | Path A §3 (checklist rows) | First requirement | Last requirement mapped or MISSING |
| P3 First draft complete | Path A §3 end | — | All rows draft / MISSING / EXPIRED / CONFLICT reviewed |
| P4 Approver | Path A §4 | Hand-off to Approver | Approver decision recorded |
| P5 Export decision | Path A §5–6 | Export attempt / block | Manifest decision + timer stop → CSV |

**`minutes_to_first_draft`** = wall-clock from P1 start through P3 stop (exclude Approver wait unless you agree otherwise in Notes — document once and stay consistent).

## Per-pack log (blank until real)

| pack_id | mode (`dry_run` / `live`) | Fixture or customer (anonymised) | P1 start (ISO) | P3 stop (ISO) | minutes_to_first_draft | P4–P5 min (opt.) | Metrics CSV row | Method note / DRY link | Baseline / INT-ID (live only) | Logged by | Notes |
|---------|---------------------------|----------------------------------|----------------|---------------|------------------------|------------------|-----------------|------------------------|-------------------------------|-----------|-------|
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Packs logged (any mode) | 0 |
| Founder-paced Path A re-times | 0 |
| Live packs with complete P1–P3 | 0 |
| Live packs forwarded to contrast rollup | 0 |

## Founder checklist

- [ ] Timer used for each phase; total matches CSV `minutes_to_first_draft`  
- [ ] `mode` set correctly (`dry_run` vs `live`)  
- [ ] DRY rows: method note or `pack-dry-run-dry-*.md` link only — **not** scorecard  
- [ ] Live rows: kickoff [`baseline-minutes-worksheet.md`](baseline-minutes-worksheet.md) ready before contrast  
- [ ] Live contrast: [`minutes-saved-contrast-rollup.md`](minutes-saved-contrast-rollup.md) — ignore DRY  
- [ ] Scorecard Time/value Actual only via rollup + hygiene map  
- [ ] No invented clocks; no confidential pack content in git  

## Stop rules

- Never invent clock times, baselines, or £ values.  
- Never treat DRY wall-clock as customer minutes saved or GO Time/value.  
- Never mix Support effort into draft wall-clock.  
- Never commit live customer pack content with this log.  
- This log is measurement discipline — not win-rate or qualification proof.
