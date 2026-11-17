# Interview pain-convergence → scorecard tally (blank Actuals)

**Epic:** [#1](https://github.com/thesnjk/BidHarbour/issues/1)  
**As-of:** 2026-11-17  
**Purpose:** Founder-facing rollup that turns completed interview synthesis rows into the scorecard **Interview pain convergence** Actual (≥6/10 same problem in lead niche).  
**Lead gap:** Pain-convergence path must be explicit — synthesis alone is easy to skip when updating the scorecard / Week-4 gate.

**Companions:**  
[`interview-synthesis.md`](interview-synthesis.md) · [`recording-template.md`](recording-template.md) · [`interview-grid-8wk.md`](interview-grid-8wk.md) · [`week4-gate-checklist.md`](week4-gate-checklist.md) · [`scorecard-actuals-hygiene.md`](scorecard-actuals-hygiene.md) · [`validation-scorecard.md`](validation-scorecard.md) · [`negative-findings.md`](negative-findings.md) · [`qualified-discovery-week-tracker.md`](qualified-discovery-week-tracker.md)

**Evidence label:** Blank template only. Do **not** invent INT IDs, quotes, same_pain flags, or scorecard Actuals. Booked slots / sends alone are not interview evidence.

## Threshold

| Criterion | Threshold | Source of truth for rows |
|-----------|-----------|--------------------------|
| Interview pain convergence | ≥6/10 **same_pain = Y** in lead niche (AME / marine / fab) | [`interview-synthesis.md`](interview-synthesis.md) completed INT rows |

## How to tally (founder)

1. Open [`interview-synthesis.md`](interview-synthesis.md) → *Completed interviews*.  
2. Filter to **lead niche** (AME or marine — fabrication OK if lead ICP; exclude anti-persona / reserve as wins).  
3. Count non-empty `INT-ID` rows in that filter (= n).  
4. Count `same_pain = Y` in that filter.  
5. Express as x/10 style: `same_pain_Y / max(n,1)` scaled to /10 (or use n as denominator when n≥10).  
6. Copy into the live tally below.  
7. Only then update [`validation-scorecard.md`](validation-scorecard.md) Interview pain convergence **Actual** and paste `INT-*` Evidence IDs (per [`scorecard-actuals-hygiene.md`](scorecard-actuals-hygiene.md)).  
8. At Week 4: copy this tally into [`week4-gate-checklist.md`](week4-gate-checklist.md) §2 — do not invent rows to pass.

## Live tally (keep zero until real INT)

| Metric | Value | Notes |
|--------|-------|-------|
| Lead niche | — | AME / marine / fab |
| Completed INT in lead niche (n) | 0 | From synthesis |
| same_pain = Y | 0 | Lead niche only |
| Pain convergence (x/10) | 0/10 | vs ≥6/10 |
| Threshold met? (≥6/10) | No | Flip to Yes only with real data |
| Scorecard Actual synced? | No | Y only after scorecard edit |

## Evidence ID paste block (blank)

When Actual moves, paste here then into the scorecard Evidence IDs column:

```
INT-…
INT-…
INT-…
```

## Niche filter (lead ICP)

Only count interviews in the Norfolk AME / marine / fabrication lead niche toward the ≥6/10 gate. Log others in synthesis if useful, but mark `counts_to_scorecard=N` below.

| INT-ID | Niche | same_pain (Y/N) | Counts to scorecard? (Y/N) | Date logged |
|--------|-------|-----------------|----------------------------|-------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## Gate reminder

| Gate | Link |
|------|------|
| Week-4 interview | [`week4-gate-checklist.md`](week4-gate-checklist.md) |
| Live scorecard | [`validation-scorecard.md`](validation-scorecard.md) |
| Actuals hygiene | [`scorecard-actuals-hygiene.md`](scorecard-actuals-hygiene.md) |
| Synthesis source | [`interview-synthesis.md`](interview-synthesis.md) |

Interview pain convergence ≠ workflow evidence. Do not blur INT tallies into OBS Actuals ([`observation-workflow-evidence-tally.md`](observation-workflow-evidence-tally.md)).

## Stop rules

- Never invent INT rows or same_pain flags to “pass” ≥6/10.  
- Never increment scorecard Actual from booked slots, sends, or fixture demos alone.  
- Held discovery only — booked ≠ held ([`qualified-discovery-week-tracker.md`](qualified-discovery-week-tracker.md)).  
- Never commit confidential interview notes or customer packs.  
- Anti-persona / “not a problem” → log + [`negative-findings.md`](negative-findings.md); do not count as same_pain = Y.  
- Week-4 pass ≠ production SaaS / inventing interviews.
