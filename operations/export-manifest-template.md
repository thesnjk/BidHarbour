# Approver export manifest (pilot)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use at:** Path B steps 5–6 in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Train first:** [`approver-review-training.md`](approver-review-training.md)  
**Live attestation log:** [`pilot-approver-attestation-log.md`](pilot-approver-attestation-log.md) (blank Actuals — after Approve/Block)  
**Rule:** Export **blocked** while any required row is unapproved, **MISSING**, **EXPIRED**, or **CONFLICT** without an explicit waiver / Approver pick.

Copy this page per pack (local only for live customers). Dry-runs may use fixture pack_ids (DRY-001–011). Filled blocked example: [`export-manifest-dry-009-filled.md`](export-manifest-dry-009-filled.md). Waiver ≠ Approve example: [`export-manifest-dry-010-filled.md`](export-manifest-dry-010-filled.md).

## Pack header

| Field | Value |
|-------|-------|
| pack_id | |
| mode | dry_run / live |
| customer_or_fixture | |
| buyer / pack label | |
| Named Approver | |
| Draft prepared by | |
| Date | |

## Manifest

Status must be `approved`, `waived`, `MISSING`, `EXPIRED`, or `CONFLICT`. Do not export if required rows are still `MISSING` / `EXPIRED` / `CONFLICT` without waiver or human resolution. For **CONFLICT**, list **both** `evidence_label`s in Notes.

| Req # | Topic / doc_key | evidence_label / version | Status | Approver initials | Date | Notes |
|-------|-----------------|--------------------------|--------|-------------------|------|-------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| … | | | | | | |

*(Add rows to match checklist length — e.g. 22 for redacted-pqq-v1, 18 for redacted-sq-v1.)*

## Approver declaration

I confirm I am authorised to approve statements in this pack for the organisation. I have reviewed each required row. I understand Supplier Desk / BidHarbour does **not** invent missing evidence and does **not** guarantee qualification or contract award.

- [ ] **Approve export** of the attached pack + this manifest  
- [ ] **Block export** — list blocking rows in Notes  

Approver name: _________________ Signature / mark: _________________ Date: _________

## Export log

| Field | Value |
|-------|-------|
| export_approved | yes / no |
| formats delivered | (e.g. PDF pack + manifest) |
| portal auto-submit | **no** |
| metrics CSV updated | yes / no |
| attestation log updated (live) | yes / no → [`pilot-approver-attestation-log.md`](pilot-approver-attestation-log.md) |

## Stop rules

- Never export without Approver approve or documented waiver path.  
- Never silent-pick one of two conflicting in-date library sources.  
- Never commit live manifests with customer evidence paths to git.  
- Live packs: MSA/DPA cleared first; log Approve/Block on the attestation log.  
- CONFLICT rehearsal: [`pack-dry-run-dry-006.md`](pack-dry-run-dry-006.md).
