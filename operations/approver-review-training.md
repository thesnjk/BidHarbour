# Approver review training (one-pager)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use before:** Path B Approver gate — [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) step 5  
**Sign on:** [`export-manifest-template.md`](export-manifest-template.md)  
**Product name:** Supplier Desk

**Role:** You are the **named Approver** with authority to approve statements for the organisation. Concierge / AI may **draft** only — you sign every export (or explicitly block).

**Rule:** Do **not** invent certifications, insurance, financials, or capabilities. Export stays **blocked** while any required row is unapproved, **MISSING**, **EXPIRED**, or **CONFLICT** without an explicit waiver / human pick.

## Before sign-off checklist

Walk the pack checklist + manifest row by row:

- [ ] Every required row is `approved`, `waived` (with note), or still `MISSING` / **EXPIRED** / **CONFLICT** with export **blocked**  
- [ ] Each cited `evidence_label` / version matches the document you reviewed (or synthetic label on dry-run)  
- [ ] Expiry / review dates checked where required; expired → **EXPIRED** block (or renew)  
- [ ] Two in-date library matches that disagree → **CONFLICT**; list both labels; pick or retire one before approve  
- [ ] No silent-fill of gaps; MISSING queue sent if customer still owes evidence  
- [ ] Buyer-specific rows (conflicts, Broads QP ack, etc.) are **not** copied from another buyer’s pack  
- [ ] Portal auto-submit remains **no** — customer uploads via their channel  
- [ ] You are named on the manifest header and authorised for this org  

## Using the export manifest

1. Fill pack header (`pack_id`, mode, buyer, your name).  
2. Complete the manifest table (status + initials + date).  
3. Tick **Approve export** only if every required row is approved or explicitly waived.  
4. Tick **Block export** if anything required is still MISSING, EXPIRED, CONFLICT, or wrong — list blocking rows in Notes (both labels for CONFLICT).  
5. After approve: founder delivers formats + updates metrics CSV (`export_approved=yes`).  
6. Live packs: log Approve/Block on [`pilot-approver-attestation-log.md`](pilot-approver-attestation-log.md) (blank Actuals in git until real).

## Waive vs block

| Situation | Action |
|-----------|--------|
| Evidence on file, accurate, in date | **Approve** row |
| Customer confirmed not held / N/A with rationale | May **waive** (record rationale) |
| Still MISSING after SLA; no waiver | **Block** export |
| Past expiry / review date | **Block** (EXPIRED) until renew or waive |
| Two in-date approved sources disagree | **Block** (CONFLICT) until you pick/retire one |
| Draft-only library cite (e.g. case study `draft`) | Rework or block until you accept |

Target: ≤**1** major rework loop after your first review ([`../research/pilot-design.md`](../research/pilot-design.md)).

## Practice (dry-run)

Rehearse on fixture packs (DRY-001–011) with [`../testdata/`](../testdata/) — synthetic only. **EXPIRED:** [`pack-dry-run-dry-005.md`](pack-dry-run-dry-005.md). **CONFLICT:** [`pack-dry-run-dry-006.md`](pack-dry-run-dry-006.md). **Filled manifest + Block export:** [`pack-dry-run-dry-009.md`](pack-dry-run-dry-009.md) · [`export-manifest-dry-009-filled.md`](export-manifest-dry-009-filled.md). **Waiver ≠ Approve export:** [`pack-dry-run-dry-010.md`](pack-dry-run-dry-010.md) · [`export-manifest-dry-010-filled.md`](export-manifest-dry-010-filled.md). Dry-runs do **not** count as scorecard GO evidence or live attestation rows.

## Stop rules

- Live packs: solicitor-cleared MSA/DPA first.  
- No win-rate or qualification guarantees in comments or customer emails.  
- Do not commit live manifests or customer evidence paths to git.  
- Library match ≠ your approval.
