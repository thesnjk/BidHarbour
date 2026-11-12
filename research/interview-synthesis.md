# Interview synthesis (cross-interview rollup)

**Purpose:** Roll up completed interviews for Week-4 **pain convergence** and workflow evidence — feeds [`validation-scorecard.md`](validation-scorecard.md).  
**Per-interview capture:** [`recording-template.md`](recording-template.md) (`INT-YYYYMMDD-##`)  
**Guide:** [`interview-guide.md`](interview-guide.md)  
**Disconfirming:** [`negative-findings.md`](negative-findings.md)  
**Next (pilot conversion):** [`discovery-pilot-offer-bridge.md`](discovery-pilot-offer-bridge.md)

**Evidence label:** Template only until rows are filled from **completed** interviews.  
**Do not** invent quotes, INT IDs, or scorecard Actuals. Send/reply alone is not evidence.

## Rules

1. Add a row only after an interview (or observation coded as interview-equivalent) is finished and a recording sheet exists.  
2. `same_pain` = Y only if the **last pack** pain matches the ICP job (inbound customer-specific PQQ/SQ assembly / evidence chase) — not generic “busy.”  
3. Update scorecard Actuals from the **tally below**, not from CRM send counts.  
4. Anti-persona or “not a problem” → still log here + append [`negative-findings.md`](negative-findings.md).

## Completed interviews (blank until real)

| INT-ID | Niche | CRM id | same_pain (Y/N) | hours_last_pack | WTP pilot (Y/Soft/N) | anti_persona (Y/N) | Evidence note |
|--------|-------|--------|-----------------|-----------------|----------------------|--------------------|---------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

*(Add rows as needed. Target ≥10 coded in lead niche for convergence.)*

## Convergence tally → scorecard

| Metric | How to compute | Current (keep blank/zero until data) |
|--------|----------------|--------------------------------------|
| Completed interviews (n) | Count non-empty INT-ID rows | 0 |
| same_pain = Y | Count Y in same_pain | 0 |
| Pain convergence | `same_pain_Y / max(n,1)` as x/10 style vs threshold ≥6/10 **in lead niche** | 0/10 |
| Lead niche focus | Filter table to AME or marine; recompute | — |

**Scorecard field:** Interview pain convergence → paste Evidence IDs (INT-*) into scorecard when Actual moves.

## Workflow evidence (≥3 businesses)

Scorecard: Workflow evidence ≥3 businesses. Source of truth for observation rows → [`observation-session-log.md`](observation-session-log.md). Tick only with distinct firms + `OBS-*` (or interview-equivalent INT-IDs):

| # | Firm (or anonymised) | OBS-ID / INT-ID | Pack type seen (PQQ/SQ/other) | Done? |
|---|----------------------|-----------------|-------------------------------|-------|
| 1 | | | | [ ] |
| 2 | | | | [ ] |
| 3 | | | | [ ] |

## Friday ritual

1. Pull new INT sheets into the table above.  
2. Recompute tally.  
3. Update [`validation-scorecard.md`](validation-scorecard.md) Actuals **only if** numbers changed from real completions — follow [`scorecard-actuals-hygiene.md`](scorecard-actuals-hygiene.md).  
4. Log negatives the same day.  
5. Attach any new [`interview-sharepoint-time-study.md`](interview-sharepoint-time-study.md) sheets to Evidence note (INT-ID) — minutes vs SharePoint; do not invent; Time/value Actual stays blank until pilots.  
6. At Week 4: run [`week4-gate-checklist.md`](week4-gate-checklist.md) from this tally — do not invent rows to pass.  
7. At Week 8: run [`week8-gate-checklist.md`](week8-gate-checklist.md) from scorecard + live pilot metrics — dry-runs alone are not GO evidence.
