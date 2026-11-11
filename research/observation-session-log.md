# Observation session log (blank Actuals)

**Purpose:** One row per **completed** workflow observation — feeds scorecard **Workflow evidence** (≥3 businesses).  
**Epic:** [#1](https://github.com/thesnjk/BidHarbour/issues/1)  
**Kit:** [`observation-kit-naame-hethel.md`](observation-kit-naame-hethel.md)  
**During:** [`observation-checklist.md`](observation-checklist.md)  
**Scorecard:** [`validation-scorecard.md`](validation-scorecard.md) → *Workflow evidence*  
**Booking index:** [`interview-grid-8wk.md`](interview-grid-8wk.md)  
**Rollup:** [`interview-synthesis.md`](interview-synthesis.md) Workflow evidence table

**Evidence label:** Template only until rows are filled from **real** observations.  
**Do not** invent OBS IDs, firms, minutes, or scorecard Actuals. Event attendance alone is not evidence.

## Rules

1. Add a row only after an observation is finished (on-site or screenshare) with consent + redaction noted.  
2. IDs: `OBS-YYYYMMDD-##` (local sequence that day).  
3. Distinct businesses only count toward ≥3 — one firm, one OBS for the scorecard tally (repeat packs on same firm stay logged but do not inflate the count).  
4. Private detailed notes stay off-git; this log holds non-sensitive fields only.  
5. Update scorecard Actual from the **tally below**, not from CRM sends or booked slots.

## Completed observations (blank until real)

| OBS-ID | Date | Venue (NAAME/Hethel/GY/other) | Niche | CRM id | Pack type (PQQ/SQ/other) | Minutes | Consent+redaction (Y/N) | Evidence note |
|--------|------|-------------------------------|-------|--------|--------------------------|---------|-------------------------|---------------|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*(Add rows as needed. Target ≥3 distinct businesses in lead niche.)*

## Tally → scorecard

| Metric | How to compute | Current (keep blank/zero until data) |
|--------|----------------|--------------------------------------|
| Completed observations (n) | Count non-empty OBS-ID rows | 0 |
| Distinct businesses | Count unique CRM id / anonymised firm | 0 |
| Workflow evidence | Distinct businesses vs threshold ≥3 | 0 |

**Scorecard field:** Workflow evidence → paste Evidence IDs (`OBS-*`) when Actual moves.

## After each real OBS

1. Fill checklist notes privately; confirm total minutes with participant.  
2. Add row above; mark grid booking if used.  
3. Tick matching row in [`interview-synthesis.md`](interview-synthesis.md) Workflow evidence (use OBS-ID in the INT-ID column or note OBS-*).  
4. Negatives → [`negative-findings.md`](negative-findings.md) same day.  
5. Update [`validation-scorecard.md`](validation-scorecard.md) Actual **only** if distinct-business count changed.

## Stop rules

- Do not invent observation results or scorecard Actuals.  
- Do not commit live customer packs, certificates, or PII.  
- Do not pitch win rates or production SaaS during observation.  
- Do not claim NAAME/Hethel partnership.
