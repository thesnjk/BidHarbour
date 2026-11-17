# Continuation log → scorecard Continuations tally (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**As-of:** 2026-11-17  
**Purpose:** Founder-facing rollup that turns written continuation `yes` rows into the scorecard **Continuations** Actual (≥2).  
**Lead gap:** Continuations path must be explicit — the log alone is easy to skip when updating the scorecard / Week-8 gate.

**Companions:**  
[`pilot-continuation-log.md`](pilot-continuation-log.md) · [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md) · [`../research/scorecard-actuals-hygiene.md`](../research/scorecard-actuals-hygiene.md) · [`../research/validation-scorecard.md`](../research/validation-scorecard.md) · [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md) · [`../commercial/crm-stage-scripts.md`](../commercial/crm-stage-scripts.md)

**Evidence label:** Blank template only. Do **not** invent yes/no decisions, customer names, or scorecard Actuals. Verbal interest / pending D / DRY-00x are not continuations.

## Threshold

| Criterion | Threshold | Source of truth for rows |
|-----------|-----------|--------------------------|
| Continuations | ≥2 written **`yes`** after close-out **D** | [`pilot-continuation-log.md`](pilot-continuation-log.md) |

## How to tally (founder)

1. Open [`pilot-continuation-log.md`](pilot-continuation-log.md) → *Log*.  
2. Count rows with Decision = **`yes`** only (written email or signed note).  
3. Exclude `pending`, `no`, verbal interest, and any DRY/training rows.  
4. Copy into the live tally below.  
5. Only then update [`../research/validation-scorecard.md`](../research/validation-scorecard.md) Continuations **Actual** and paste evidence (CRM id / decision date / pack window) per [`../research/scorecard-actuals-hygiene.md`](../research/scorecard-actuals-hygiene.md).  
6. At Week 8: copy this tally into [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md) Continuations line — do not invent rows to pass.

## Live tally (keep zero until real yes)

| Metric | Value | Notes |
|--------|-------|-------|
| Written `yes` (n) | 0 | From continuation log |
| Written `no` | 0 | Context only — not scorecard |
| `pending` | 0 | Not counted |
| Threshold met? (≥2 yes) | No | Flip to Yes only with real data |
| Scorecard Actual synced? | No | Y only after scorecard edit |

## Evidence paste block (blank)

When Actual moves, paste here then into the scorecard Evidence IDs column:

```
continuation_yes · CRM-… · decision_date=…
continuation_yes · CRM-… · decision_date=…
```

## Yes filter (scorecard-eligible)

| CRM id (anonymised OK) | Decision date | Channel | Counts to scorecard? (Y/N) | MSA/DPA note before further packs | Logged by |
|------------------------|---------------|---------|----------------------------|-----------------------------------|-----------|
| | | | | | |
| | | | | | |
| | | | | | |

## Gate reminder

| Gate | Link |
|------|------|
| Week-8 | [`../research/week8-gate-checklist.md`](../research/week8-gate-checklist.md) |
| Live scorecard | [`../research/validation-scorecard.md`](../research/validation-scorecard.md) |
| Actuals hygiene | [`../research/scorecard-actuals-hygiene.md`](../research/scorecard-actuals-hygiene.md) |
| Source log | [`pilot-continuation-log.md`](pilot-continuation-log.md) |

Continuations ≠ Repeat usage. Do not blur `yes` into packs-per-60d ([`pilot-repeat-usage-tracker.md`](pilot-repeat-usage-tracker.md)).

## Stop rules

- Never invent `yes` rows to “pass” ≥2.  
- Never increment scorecard Actual from verbal interest, pending D, or DRY-00x.  
- A `yes` does not authorise further confidential packs until solicitor-cleared continuation MSA/DPA.  
- Never commit confidential continuation emails or customer identities.  
- No win-rate or qualification claims tied to continuation.  
- Week-8 pass ≠ production SaaS.
