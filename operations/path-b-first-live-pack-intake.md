# Path B first live pack intake worksheet (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** Path B-0 kickoff exit ([`pilot-kickoff-checklist.md`](pilot-kickoff-checklist.md) §4)  
**Use at:** runbook Path B step 1 ([`concierge-pilot-runbook.md`](concierge-pilot-runbook.md))  
**Lead gap:** inbound pack → structured checklist vs SharePoint / folder scatter  
**Companions:** [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md) · [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) · [`pre-pilot-legal-readiness-gate.md`](pre-pilot-legal-readiness-gate.md) · [`../security-and-legal/pilot-named-access-register.md`](../security-and-legal/pilot-named-access-register.md) · [`missing-queue-email.md`](missing-queue-email.md) · [`pilot-repeat-pack-playbook.md`](pilot-repeat-pack-playbook.md) (packs 2–3)  
**Product name:** Supplier Desk

**Evidence label:** Template only until a **real** live pack arrives. Do **not** invent pack_ids, minutes, or scorecard Actuals in git. Never commit customer evidence, filled intake CSVs, or confidential pack text.

## Goal

Turn kickoff exit into a logged **P01** intake: encrypted receive → local evidence CSV → metrics row (`mode=live`) → checklist extract handoff — without treating dry-runs as live proof.

## Preconditions (all required)

- [ ] Legal readiness gate **PASS** → [`pre-pilot-legal-readiness-gate.md`](pre-pilot-legal-readiness-gate.md)  
- [ ] Kickoff §4 exit complete → [`pilot-kickoff-checklist.md`](pilot-kickoff-checklist.md)  
- [ ] Named Approver + encrypted path on file  
- [ ] Baseline worksheet started (kickoff) → [`baseline-minutes-worksheet.md`](baseline-minutes-worksheet.md)  
- [ ] This worksheet kept **local / encrypted** when filled with customer identifiers  

## Pack header (blank until real)

| Field | Value |
|-------|-------|
| pack_id | P01 *(or next live id — never DRY-00x)* |
| mode | `live` |
| CRM id / anonymised customer | |
| Buyer / pack label | |
| received_at (ISO) | |
| Channel | encrypted path / other *(local note)* |
| Named Approver | |
| Operator | |

## Intake steps (Path B step 1)

1. **Receive** — Confirm pack + evidence folder arrived via agreed encrypted path (not full packs in open email if avoidable).  
2. **Local evidence CSV** — Copy [`pilot-evidence-library-intake.csv`](pilot-evidence-library-intake.csv) outside git; mark `received` / `expired` / `waived` per [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md).  
3. **Metrics row** — Start a **local** row in metrics CSV: `pack_id`, `mode=live`, `customer_or_fixture`, `received_at` (leave minutes/missing blank until first draft). Do **not** invent values.  
4. **Checklist extract** — Build per-pack requirement list (same shape as fixture); hand off to Path B step 2.  
5. **FO7** — Buyer-specific / scoped answers stay scoped; do **not** merge into shared library without Approver + `applies_to` change (see DRY-007 / [`pilot-repeat-pack-playbook.md`](pilot-repeat-pack-playbook.md)).  
6. **Continue** — Path B steps 2–8 (match → MISSING queue → Approver → export → log → closeout **A**).

## Founder / operator checklist

- [ ] Preconditions ticked honestly  
- [ ] Pack header filled locally (no git commit of customer IDs if sensitive)  
- [ ] Local evidence CSV updated  
- [ ] Metrics live row started (blank outcome fields OK)  
- [ ] Checklist extract started → Path B step 2  
- [ ] No confidential files staged for git  

## Stop rules

- No live pack on uncleared MSA/DPA or incomplete kickoff.  
- No inventing certifications, insurance, financials, or capabilities.  
- No committing customer packs, filled intake CSVs, or secret paths to git.  
- DRY-00x rehearsal ≠ live **P01** / scorecard GO evidence.  
- No portal auto-submit; Approver still signs every export.
