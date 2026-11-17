# Path A clock → minutes-saved leave-behind bridge (blank Actuals)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use when:** a Path A / Path B pack clock has been logged and the customer leave-behind is not yet filled after results review  
**Lead gap:** minutes saved vs SharePoint / folder labour — live clock → rollup → leave-behind (DRY wall-clock ≠ customer proof)  
**Companions:** [`../operations/path-a-pilot-pack-clock-time-log.md`](../operations/path-a-pilot-pack-clock-time-log.md) · [`../operations/minutes-saved-contrast-rollup.md`](../operations/minutes-saved-contrast-rollup.md) · [`../operations/baseline-minutes-worksheet.md`](../operations/baseline-minutes-worksheet.md) · [`minutes-saved-leave-behind.md`](minutes-saved-leave-behind.md) · [`../operations/pilot-results-review-agenda.md`](../operations/pilot-results-review-agenda.md) · [`../research/scorecard-actuals-hygiene.md`](../research/scorecard-actuals-hygiene.md) · [`competitive-objection-sheet.md`](competitive-objection-sheet.md) (SharePoint) · [`sharepoint-vs-inbound-checklist-matrix.md`](sharepoint-vs-inbound-checklist-matrix.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** live clocks and reviews.  
**Do not** invent minutes, £ values, baselines, or scorecard Actuals in git. Prefer anonymised pack IDs; keep customer detail on the local encrypted path.

## Goal

Bridge Path A / live pack clock discipline into an honest customer leave-behind: log clock → contrast vs baseline → results review → leave-behind — without treating DRY / training wall-clock as minutes saved.

## Preconditions

| Check | Rule |
|-------|------|
| Clock logged | Row on [`../operations/path-a-pilot-pack-clock-time-log.md`](../operations/path-a-pilot-pack-clock-time-log.md); CSV `minutes_to_first_draft` matches |
| Proof path | Only `mode=live` feeds rollup / leave-behind / Time/value |
| Training | `mode=dry_run` / Path A re-time = method only — stop before leave-behind |
| Baseline | Kickoff baseline on [`../operations/baseline-minutes-worksheet.md`](../operations/baseline-minutes-worksheet.md) (or honest gap noted) |
| Review | Results review held or scheduled ([`../operations/pilot-results-review-agenda.md`](../operations/pilot-results-review-agenda.md)) |

## Sequence

1. **Clock** — Complete phased log for the pack; total matches metrics CSV. Document mode (`dry_run` / `live`).  
2. **Gate mode** — If `dry_run`: stop. Do **not** fill leave-behind or bump scorecard Time/value. Founder may re-time Path A for training only.  
3. **Live only — rollup** — Compute contrast on [`../operations/minutes-saved-contrast-rollup.md`](../operations/minutes-saved-contrast-rollup.md) using baseline + live clock (no invented £).  
4. **Results review** — Present contrast on the agenda; no win-rate / qualification claims.  
5. **Leave-behind** — Fill [`minutes-saved-leave-behind.md`](minutes-saved-leave-behind.md) on a **local** copy from the live rollup; do not stage customer minutes in git.  
6. **Scorecard** — Update Time/value Actual only via [`../research/scorecard-actuals-hygiene.md`](../research/scorecard-actuals-hygiene.md) after real live contrast — never from DRY.

## Log (blank until real)

| pack_id | mode | Clock logged? (Y/N) | Rollup done? (Y/N/blank) | Results review? (Y/N/blank) | Leave-behind filled locally? (Y/N/blank) | Scorecard synced? (Y/N/blank) | Logged by | Notes |
|---------|------|---------------------|--------------------------|----------------------------|------------------------------------------|-------------------------------|-----------|-------|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Live packs bridged to rollup | 0 |
| Leave-behinds filled (local) | 0 |
| Scorecard Time/value syncs | 0 |

## Founder checklist

- [ ] Clock row + CSV total aligned  
- [ ] Mode gated — dry_run stopped before leave-behind  
- [ ] Live: baseline + rollup completed (no invent)  
- [ ] Results review used live contrast only  
- [ ] Leave-behind filled locally from rollup  
- [ ] Scorecard Time/value only after hygiene + real live data  
- [ ] No win-rate / DRY-as-proof claims  

## Stop rules

- Never invent minutes, baselines, or £ saved.  
- Never use DRY-00x / Path A training wall-clock as customer leave-behind or scorecard Actuals.  
- Never stage confidential customer leave-behind numbers in git.  
- Never claim SharePoint “replaced” or qualification wins.  
- Do not replace the clock log, rollup, or leave-behind — compose with them.  
- Live packs: solicitor-cleared MSA/DPA first.
