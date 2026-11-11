# Approver export manifest (pilot)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use at:** Path B steps 5–6 in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Train first:** [`approver-review-training.md`](approver-review-training.md)  
**Rule:** Export **blocked** while any required row is unapproved or MISSING without an explicit waiver.

Copy this page per pack (local only for live customers). Dry-runs may use fixture pack_ids (DRY-001 / DRY-002).

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

Status must be `approved`, `waived`, or `MISSING`. Do not export if required rows are still `MISSING` without waiver.

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

## Stop rules

- Never export without Approver approve or documented waiver path.  
- Never commit live manifests with customer evidence paths to git.  
- Live packs: MSA/DPA cleared first.
