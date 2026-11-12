# Scorecard Actuals update hygiene checklist

**Epic:** [#1](https://github.com/thesnjk/BidHarbour/issues/1)  
**Use on:** Friday ritual / after each completed interview, observation, or live pilot close  
**Scorecard:** [`validation-scorecard.md`](validation-scorecard.md)  
**Companions:** [`interview-synthesis.md`](interview-synthesis.md) · [`observation-session-log.md`](observation-session-log.md) · [`../operations/pilot-continuation-log.md`](../operations/pilot-continuation-log.md) · [`../operations/pilot-support-burden-log.md`](../operations/pilot-support-burden-log.md) · [`../operations/minutes-saved-contrast-rollup.md`](../operations/minutes-saved-contrast-rollup.md) · [`week4-gate-checklist.md`](week4-gate-checklist.md) · [`week8-gate-checklist.md`](week8-gate-checklist.md)  
**Lead gap:** validation proof path — one map from source artefacts → Actuals without inventing

**Evidence label:** Checklist template only. Do **not** invent Actuals, INT/OBS/pack IDs, or Pass marks in git. Leave scorecard numbers at current zeros / `—` until real evidence exists.

## Goal

Update [`validation-scorecard.md`](validation-scorecard.md) honestly: each Actual moves only from an allowed source tally, with Evidence IDs pasted — never from CRM sends, dry-runs, or invented completions.

## Per-criterion map

| Criterion | Allowed source (recompute first) | Never count |
|-----------|----------------------------------|-------------|
| Interview pain convergence | [`interview-synthesis.md`](interview-synthesis.md) same_pain tally (lead niche) | Email sends, replies, booked-but-not-held slots |
| Workflow evidence | Distinct firms with completed `OBS-*` / interview-equivalent INT ([`observation-session-log.md`](observation-session-log.md)) | Send logs; synthetic dry-runs |
| Paid pilots | Live packs completed (kickoff + Path B; metrics `mode=live`) | DRY-00x; unsigned MSA stubs |
| Continuations | Written `yes` rows in [`../operations/pilot-continuation-log.md`](../operations/pilot-continuation-log.md) | Verbal interest; pending D |
| Time/value | Live minutes contrast [`../operations/minutes-saved-contrast-rollup.md`](../operations/minutes-saved-contrast-rollup.md) (+ baseline) | DRY wall-clock; invented £ |
| Repeat usage | Live packs ≥2 / continuing customer / 60d (real CRM + metrics) | Dry-run pack sequences |
| Support effort | Monthly rows in [`../operations/pilot-support-burden-log.md`](../operations/pilot-support-burden-log.md) | DRY `support_minutes=0` |
| Contribution margin | Real fee/cost notes (founder private) after customer #6 | Hypotheses only |
| Repeatable acquisition | ≥1 qualified discovery/week with completed booking → held interview path | Cold sends alone |

## Founder steps (each update)

1. **Complete source** — recording sheet / OBS log / live metrics / continuation reply / support month — before touching scorecard.  
2. **Recompute tally** on the source artefact (synthesis Friday ritual, support-burden month, etc.).  
3. **Update Actual** only if the number changed from real completions.  
4. **Paste Evidence IDs** (INT-* / OBS-* / pack_id / log row date) into the scorecard Evidence column.  
5. **Pass?** — mark only when threshold is honestly met; else leave blank / fail.  
6. **Gates** — Week-4 / Week-8 checklists copy from scorecard; do not invent rows to pass.  
7. **Never** bump Actuals from CRM send counts, LinkedIn clicks, or DRY reports alone.

## Ritual log (blank until real)

| Date | Criterion updated | New Actual | Evidence IDs | Updated by | Notes |
|------|-------------------|------------|--------------|------------|-------|
| | | | | | |

## Stop rules

- No invented interviews, observations, pilots, continuations, or minutes.  
- Send / reply alone ≠ interview Actual.  
- DRY-00x ≠ GO / Time/value / Support Actual.  
- Leave Actual at `0` / `—` until real evidence exists.  
- Do not claim scorecard GO for SaaS from templates alone.
