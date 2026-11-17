# Observation → scorecard workflow-evidence tally (blank Actuals)

**Epic:** [#1](https://github.com/thesnjk/BidHarbour/issues/1) · Refs [#156](https://github.com/thesnjk/BidHarbour/issues/156)  
**As-of:** 2026-11-17  
**Purpose:** Founder-facing rollup that turns completed OBS rows into the scorecard **Workflow evidence** Actual (≥3 distinct businesses).  
**Lead gap:** Workflow evidence path must be explicit — session log alone is easy to skip when updating the scorecard.

**Companions:**  
[`observation-session-log.md`](observation-session-log.md) · [`observation-kit-naame-hethel.md`](observation-kit-naame-hethel.md) · [`observation-checklist.md`](observation-checklist.md) · [`observation-inbound-pack-scatter-worksheet.md`](observation-inbound-pack-scatter-worksheet.md) · [`scorecard-actuals-hygiene.md`](scorecard-actuals-hygiene.md) · [`validation-scorecard.md`](validation-scorecard.md)

**Evidence label:** Blank template only. Do **not** invent OBS IDs, firms, minutes, or scorecard Actuals. Event attendance / CRM sends alone are not workflow evidence.

## Threshold

| Criterion | Threshold | Source of truth for rows |
|-----------|-----------|--------------------------|
| Workflow evidence | ≥3 **distinct businesses** with completed observations | [`observation-session-log.md`](observation-session-log.md) non-empty `OBS-*` rows |

## How to tally (founder)

1. Open [`observation-session-log.md`](observation-session-log.md) → *Completed observations*.  
2. Count rows with a real `OBS-ID` (consent + redaction noted).  
3. Count **distinct** CRM id / anonymised firm (one firm = one scorecard count even if multiple OBS).  
4. Copy the tally into the tables below.  
5. Only then update [`validation-scorecard.md`](validation-scorecard.md) Workflow evidence **Actual** and paste `OBS-*` Evidence IDs (per [`scorecard-actuals-hygiene.md`](scorecard-actuals-hygiene.md)).

## Live tally (keep zero until real OBS)

| Metric | Value | Notes |
|--------|-------|-------|
| Completed OBS rows (n) | 0 | From session log |
| Distinct businesses | 0 | Unique CRM / firm |
| Threshold met? (≥3) | No | Flip to Yes only with real data |
| Scorecard Actual synced? | No | Y only after scorecard edit |

## Evidence ID paste block (blank)

When Actual moves, paste here then into the scorecard Evidence IDs column:

```
OBS-…
OBS-…
OBS-…
```

## Niche filter (lead ICP)

Only count observations in the Norfolk AME / marine / fabrication lead niche toward the ≥3 gate. Log others in the session log if useful, but mark `counts_to_scorecard=N` in notes below.

| OBS-ID | Distinct firm key | Niche in lead ICP? (Y/N) | Counts to scorecard? (Y/N) | Date logged |
|--------|-------------------|--------------------------|----------------------------|-------------|
| | | | | |
| | | | | |
| | | | | |

## Gate reminder

| Gate | Link |
|------|------|
| Week-4 interview | [`week4-gate-checklist.md`](week4-gate-checklist.md) |
| Live scorecard | [`validation-scorecard.md`](validation-scorecard.md) |
| Actuals hygiene | [`scorecard-actuals-hygiene.md`](scorecard-actuals-hygiene.md) |

Workflow evidence ≠ interview pain convergence. Do not blur OBS tallies into interview Actuals.

## Stop rules

- Never invent OBS rows to “pass” ≥3.  
- Never increment scorecard Actual from booked slots or sends alone.  
- Never commit confidential observation notes or customer packs.  
- This tally file is **not** itself scorecard GO evidence until filled from real OBS.
