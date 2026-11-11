# Baseline minutes capture worksheet (Path B-0)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use at:** Path B-0 kickoff — [`pilot-kickoff-checklist.md`](pilot-kickoff-checklist.md) §2 Baseline workshop  
**Pre-kickoff (optional):** interview capture [`../research/interview-sharepoint-time-study.md`](../research/interview-sharepoint-time-study.md) for the same firm — carry forward minutes/tools when available (never invent)  
**Contrast later with:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) · Rollup home: [`minutes-saved-contrast-rollup.md`](minutes-saved-contrast-rollup.md) · Design targets: [`../research/pilot-design.md`](../research/pilot-design.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until filled from a **real** kickoff.  
**Do not** invent minute estimates, timesheets, or customer names in git. Prefer anonymised IDs here; keep filled worksheets on the local encrypted path only.

## Rules

1. Capture baseline for the **last comparable** inbound PQQ/SQ / document-request pack **before** Path B pack 1.  
2. Participant estimate is OK; attach timesheet numbers only when the customer volunteers them.  
3. Dry-runs DRY-001–004 are **not** customer baseline — do not copy their minute columns into this sheet as Actuals.  
4. Live fills stay local; do **not** commit filled worksheets or banking/identity PII to git.  
5. Success contrast later: ≥40% reduction **or** ≥90 min saved vs this baseline (pilot-design) — compute only with real pilot metrics in [`minutes-saved-contrast-rollup.md`](minutes-saved-contrast-rollup.md).

## Header (blank until real)

| Field | Value |
|-------|-------|
| Customer (or anonymised) | {{Company}} |
| CRM id | |
| Kickoff date | |
| Comparable pack label (buyer / year / type) | {{pack_label}} |
| Captured by | {{Founder}} |
| Source | estimate / timesheet / both |

## Last comparable pack — minutes

| Measure | Minutes (blank) | Notes |
|---------|-----------------|-------|
| Total admin minutes (end-to-end assembly) | | Estimate + timesheet if any |
| Time to first complete draft | | Before Approver / portal upload |
| Approver / peer review minutes | | |
| Rework after review (if recalled) | | |
| Support / chasing evidence (if recalled) | | |

## Roles and tools

| Field | Blank |
|-------|-------|
| Roles involved (titles only) | |
| Primary tools (email / SharePoint / shared drive / other) | |
| Portal upload required? (yes/no/unknown) | |

## Missing / expired recall (last ~3 packs)

| Incident type | Count recalled (blank) | Notes |
|---------------|------------------------|-------|
| Missing evidence / cert | | |
| Expired document | | |
| Conflicting answers across buyers | | |
| Other friction | | |

## Contrast ritual (after live packs — do not pre-fill)

For each live `pack_id` row in [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv):

1. Take baseline **Total admin minutes** (or time-to-first-draft if that is the agreed contrast).  
2. Take pilot `minutes_to_first_draft` + `support_minutes` (and note `rework_loops`).  
3. Absolute minutes saved ≈ `baseline_total − (minutes_to_first_draft + support_minutes)` *(adjust if kickoff agreed a different definition)*.  
4. % reduction ≈ `minutes_saved / baseline_total × 100`.  
5. Pass bar: ≥40% reduction **or** ≥90 min saved — present in results review via [`pilot-results-review-agenda.md`](pilot-results-review-agenda.md) only when numbers are real.  
6. Present at close-out script **C** with [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md); no win-rate claims.

| Live pack_id | Baseline minutes used | Pilot minutes used | Minutes saved | % reduction | Pass? |
|--------------|----------------------|--------------------|---------------|-------------|-------|
| | | | | | |
| | | | | | |
| | | | | | |

## Founder checklist

- [ ] Complete this sheet (or local private copy) at/before kickoff Baseline workshop  
- [ ] Tick kickoff exit “Baseline notes captured”  
- [ ] Leave metrics CSV live rows blank until real packs  
- [ ] At results review, fill contrast table from real CSV + this baseline only  

## Stop rules

- No invented baselines, timesheets, or contrast Actuals in the repo.  
- No win-rate or qualification claims tied to minutes saved.  
- No uncleared MSA/DPA stubs as customer contracts.  
- Dry-run CSV rows ≠ customer baseline proof for GO.
