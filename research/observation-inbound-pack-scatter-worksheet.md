# Observation inbound-pack scatter worksheet (blank Actuals)

**Epic:** [#1](https://github.com/thesnjk/BidHarbour/issues/1)  
**Use during:** live workflow observation (on-site or screenshare) — while walking the **last / in-progress inbound** customer PQQ/SQ pack  
**Companions:** [`observation-kit-naame-hethel.md`](observation-kit-naame-hethel.md) · [`observation-checklist.md`](observation-checklist.md) · [`observation-session-log.md`](observation-session-log.md) · [`observation-consent-email.md`](observation-consent-email.md)  
**Interview twin (minutes rollup):** [`interview-sharepoint-time-study.md`](interview-sharepoint-time-study.md)  
**Later contrast:** Path B [`../operations/baseline-minutes-worksheet.md`](../operations/baseline-minutes-worksheet.md) · rollup [`../operations/minutes-saved-contrast-rollup.md`](../operations/minutes-saved-contrast-rollup.md)  
**Scorecard:** [`validation-scorecard.md`](validation-scorecard.md) → *Workflow evidence* (OBS tally) + pre-pilot Time/value notes only  
**Lead gap:** inbound pack → **structured checklist** vs SharePoint / email / folder **scatter** ([`competitors.md`](competitors.md))

**Evidence label:** Template only until filled from a **real** completed observation.  
**Do not** invent OBS/INT IDs, hunt minutes, firm names, or scorecard Actuals in git. Prefer anonymised IDs; keep filled sheets local / encrypted. Dry-run (DRY-00x) wall-clock is **not** observation scatter evidence.

## Goal

Capture **where** each requirement’s evidence was hunted across tools/people — the scatter that structured checklist + MISSING/EXPIRED/CONFLICT + Approver export is meant to beat. This sheet is observation-scoped; use the time-study for interview minute totals.

## Rules

1. Fill only during/after a real observation with consent + redaction noted; log `OBS-YYYYMMDD-##` on [`observation-session-log.md`](observation-session-log.md).  
2. One inbound pack per sheet (same SME, one buyer template). Multi-buyer → separate sheets.  
3. Participant estimate for “minutes to find” is OK; stopwatch preferred when watching.  
4. Outcome values only: `found` / `MISSING` / `EXPIRED` / `CONFLICT` / `unknown` — never invent a cert, date, or answer.  
5. Do **not** move scorecard Actuals from this template alone; Workflow evidence moves from session-log tally after real OBS rows.

## Header (blank until real)

| Field | Value |
|-------|-------|
| OBS-ID | OBS-YYYYMMDD-## |
| INT-ID (if also interviewed) | INT-YYYYMMDD-## or blank |
| CRM id | |
| Niche | AME / marine / other |
| Firm (anonymised OK) | |
| Pack type | PQQ / SQ / other |
| Observation date | |
| Venue | NAAME / Hethel / GY / screenshare / other |
| Consent + redaction | Y / N |
| Captured by | {{Founder}} |

## Scatter map (blank rows)

Map each requirement / evidence chase observed. Leave cells blank until real. Add rows as needed.

| # | Requirement / evidence sought (short) | Where hunted (SharePoint path / email / drive / scheme / person) | Minutes to find | Outcome (found / MISSING / EXPIRED / CONFLICT / unknown) | Notes |
|---|----------------------------------------|------------------------------------------------------------------|-----------------|----------------------------------------------------------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |

## Scatter summary (blank until real)

| Metric | Value (blank) | Notes |
|--------|---------------|-------|
| Distinct hunt locations (n) | | Count unique tools/paths/people above |
| Rows with outcome ≠ found | | Gap / expiry / conflict / unknown count |
| Approx total hunt minutes | | Sum of minutes column; do not invent |
| Structured checklist used? | Y / N / blank | Did they start from a requirement list mapped to evidence? |

## Checklist Lead contrast (observation-scoped)

Tick only what was **observed** on this pack (blank = not seen / not discussed):

- [ ] No requirement checklist mapped to evidence (ad-hoc hunt)  
- [ ] Gaps filled from memory or left silent (no explicit **MISSING**)  
- [ ] Expired / near-expiry doc reused without **EXPIRED** flag  
- [ ] Dual in-date disagree resolved as newest-wins (no **CONFLICT**)  
- [ ] No named human Approver / export manifest before submit  
- [ ] Multi-customer templates / evidence mixed in one library  
- [ ] Other: _________________

Hypothesis Lead vs SharePoint scatter: structured checklist + abstain + Approver export. **Unproven** until real OBS + pilot contrast.

## Contrast hooks (do not pre-fill)

| Later artefact | How this sheet helps |
|----------------|----------------------|
| [`observation-session-log.md`](observation-session-log.md) | OBS-ID + minutes; Workflow evidence tally |
| [`interview-sharepoint-time-study.md`](interview-sharepoint-time-study.md) | Same firm interview: carry hunt friction into Tools / “did not do well” |
| Path B baseline / minutes rollup | Starting map of scatter locations if firm pilots |
| Scorecard Workflow / Time/value | Evidence IDs = OBS-* (+ INT-* if any); Actuals stay 0/`—` until founder completes real sessions / pilots |

## Founder checklist

- [ ] Run with [`observation-checklist.md`](observation-checklist.md); expand “Where evidence lived” into scatter rows above  
- [ ] Add OBS row to [`observation-session-log.md`](observation-session-log.md) same day  
- [ ] If interview same firm: copy coarse totals into [`interview-sharepoint-time-study.md`](interview-sharepoint-time-study.md)  
- [ ] Negatives → [`negative-findings.md`](negative-findings.md)  
- [ ] Do not invent minutes or commit filled PII / live packs to git  

## Stop rules

- No invented observation results or scorecard Actuals.  
- No win-rate or qualification claims.  
- DRY-00x metrics ≠ observation scatter proof.  
- Event attendance / booked slot alone is not evidence.  
- Do not process uncleared MSA/DPA live packs into the repo.
