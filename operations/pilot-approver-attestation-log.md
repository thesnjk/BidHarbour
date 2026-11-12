# Pilot Approver attestation log (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** Path B Approver gate — Approve or Block on a **live** pack  
**Lead gap:** human approval before export (vs autonomous bid tools)  
**Sign on:** [`export-manifest-template.md`](export-manifest-template.md)  
**Train first:** [`approver-review-training.md`](approver-review-training.md)  
**Training (not Actuals):** [`pack-dry-run-dry-009.md`](pack-dry-run-dry-009.md) · [`pack-dry-run-dry-010.md`](pack-dry-run-dry-010.md)  
**Metrics:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) (`export_approved`)  
**Runbook:** [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) Path B steps 5–6  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** live packs.  
**Do not** invent Approver names, Approve/Block decisions, or scorecard Actuals in git. Prefer anonymised IDs; keep filled manifests on the local encrypted path.

## Goal

Record that a **named** Approver decided Approve or Block for each live pack — so export never proceeds without attestation, and metrics `export_approved` matches the manifest declaration.

## Rules

1. Log only `mode=live` packs (`P01`/`P02`/`P03`). DRY-009/010 rehearse gates — they are **not** live attestation proof.  
2. Named Approver required (same person as manifest header).  
3. **Approve export** tick ↔ metrics CSV `export_approved=yes` after delivery.  
4. **Block export** (or operator waiver without Approve — DRY-010 discipline) ↔ `export_approved=no`.  
5. Portal auto-submit stays **no**.  
6. Never export without a logged Approve for that pack_id.

## Log (blank until real)

| pack_id | CRM id / anonymised | Named Approver | Decision (Approve / Block) | Blockers summary (if Block) | export_approved (Y/N) | Manifest path (local) | Date | Logged by | Notes |
|---------|---------------------|----------------|----------------------------|-----------------------------|-----------------------|-----------------------|------|-----------|-------|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

## Founder checklist

- [ ] Manifest completed locally ([`export-manifest-template.md`](export-manifest-template.md))  
- [ ] Named Approver ticked Approve **or** Block with blockers noted  
- [ ] Attestation row filled above (anonymised OK in git)  
- [ ] Metrics CSV `export_approved` matches decision  
- [ ] On Approve: deliver formats; portal auto-submit still **no**  
- [ ] On Block: no customer-facing “approved pack”; chase MISSING / rework  
- [ ] No live manifest / Approver PII staged for git  

## Stop rules

- Never invent Approver names or export decisions.  
- Never treat DRY-009/010 outcomes as live attestation.  
- Never set `export_approved=yes` without Approve tick + named Approver.  
- Operator row waiver alone ≠ Approve (DRY-010).  
- Never commit live manifests or customer evidence paths to git.
