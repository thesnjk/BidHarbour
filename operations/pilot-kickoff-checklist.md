# Pilot kickoff agenda + checklist (Path B-0)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use before:** Path B step 1 (first live pack intake) in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Offer:** [`../commercial/pilot-offer-sheet.md`](../commercial/pilot-offer-sheet.md) · Offer email: [`../commercial/pilot-offer-email.md`](../commercial/pilot-offer-email.md) · Design: [`../research/pilot-design.md`](../research/pilot-design.md)  
**Product name:** Supplier Desk

**Rule:** Live packs require solicitor-cleared MSA/DPA. Do **not** invent fee receipts, signatures, or scorecard Actuals. Optional Path A dry-run rehearsal (DRY-001–005) does not replace kickoff.

## 1. Preconditions (all required for live)

- [ ] Customer accepted paid pilot outline (post-discovery) → [`../commercial/pilot-offer-email.md`](../commercial/pilot-offer-email.md)  
- [ ] Pilot MSA solicitor-cleared and signed  
- [ ] DPA solicitor-cleared and signed  
- [ ] Fee received **or** explicit waiver logged → [`pilot-fee-waiver-log.md`](pilot-fee-waiver-log.md)  
- [ ] Named Approver with authority (second person OK)  
- [ ] Approver has read [`approver-review-training.md`](approver-review-training.md)  
- [ ] MFA on founder accounts used for the pilot → [`../security-and-legal/pilot-named-access-register.md`](../security-and-legal/pilot-named-access-register.md)  
- [ ] Encrypted transfer path agreed; access limited to named accounts → [`../security-and-legal/pilot-named-access-register.md`](../security-and-legal/pilot-named-access-register.md)  
- [ ] Customer understands: no portal auto-submit; no win-rate / qualification claims  

## 2. Kickoff agenda (≈30–45 min)

| # | Topic | Notes |
|---|-------|-------|
| 1 | Scope | 4 weeks; up to **3** inbound PQQ/SQ / document-request packs |
| 2 | Baseline workshop | Minutes for last comparable pack → [`baseline-minutes-worksheet.md`](baseline-minutes-worksheet.md) (estimate + any timesheets); tools used |
| 3 | Roles | Founder concierge drafts; **Approver** signs every export |
| 4 | Intake walkthrough | Local copy of [`pilot-evidence-library-intake.csv`](pilot-evidence-library-intake.csv) — never commit live fills to git |
| 5 | MISSING SLA | Customer replies ≤ **3 business days** ([`missing-queue-email.md`](missing-queue-email.md)) |
| 6 | Export | Formats agreed; Approver uses [`export-manifest-template.md`](export-manifest-template.md) |
| 7 | Close-out preview | Scripts A–F in [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md); data return ≤30 days if stop → [`pilot-data-retention-schedule.md`](pilot-data-retention-schedule.md) |
| 8 | First pack timing | Aim for pack 1 within week 1 of pilot window |

## 3. Evidence-folder transfer checklist

- [ ] Folder received via encrypted path (not email attachment of full packs if avoidable)  
- [ ] Formats in scope: PDF, Word, Excel questionnaires + supporting PDFs  
- [ ] Naming convention noted locally (customer / pack_id) — **no** live paths pushed to GitHub  
- [ ] Excluded confirmed: full public tenders; engineering estimates; portal auto-submit; inventing certs  
- [ ] Local intake CSV updated (`not_received` → `received` as files land)  

## 4. Exit criteria → Path B step 1

All of the following before opening pack_id P01 (or next live id):

- [ ] Preconditions §1 complete  
- [ ] Kickoff held (or written async equivalent logged)  
- [ ] Baseline notes captured for metrics contrast → [`baseline-minutes-worksheet.md`](baseline-minutes-worksheet.md)  
- [ ] Evidence folder accessible locally  
- [ ] Approver contact details on file  

Then proceed to runbook **Path B step 1 — Intake**.

## Stop rules

- No live packs on uncleared MSA/DPA stubs.  
- No inventing certifications, insurance, financials, or capabilities.  
- No win-rate or qualification guarantees.  
- Do not commit customer evidence or filled intake CSVs to git.  
- Dry-run fixtures alone are not scorecard GO evidence.
