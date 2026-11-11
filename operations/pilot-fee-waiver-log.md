# Pilot fee / waiver log (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use at:** Path B-0 kickoff — [`pilot-kickoff-checklist.md`](pilot-kickoff-checklist.md)  
**Offer:** [`../commercial/pilot-offer-sheet.md`](../commercial/pilot-offer-sheet.md) · Design fees: [`../research/pilot-design.md`](../research/pilot-design.md)  
**Refund / cancel emails:** [`pilot-refund-cancellation-email.md`](pilot-refund-cancellation-email.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** pilots.  
**Do not** invent fee receipts, bank references, waivers, or customer names in git. Prefer anonymised IDs here; keep invoice/PDF copies on the local encrypted path only.

## Rules

1. Fee is due **before pack 1 processing** (pilot-design commercial intent — **Advice required** until solicitor-cleared MSA).  
2. Status must be `received` **or** `waived` before live Path B intake; `pending` blocks pack 1.  
3. A waiver requires an **explicit** reason (e.g. discovery-for-credit, founder courtesy) and who authorised it.  
4. Cleared MSA/DPA are still required for live packs — fee/waiver does not replace legal clearance.  
5. Band reference: £250–£750 ex VAT (mid anchor £500) per offer sheet — record the agreed figure privately if needed; this log may use band only.  
6. **Packs 2–3 in-window:** no second fee by default (same pilot window / max 3 packs) unless solicitor-cleared offer or MSA says otherwise — see [`pilot-repeat-pack-playbook.md`](pilot-repeat-pack-playbook.md).

## Log (blank until real)

| Customer (or anonymised) | CRM id | Pilot window (start–end) | Fee agreed (ex VAT) | Status (`received` / `waived` / `pending`) | Date | Method / waiver reason | Logged by | Notes |
|--------------------------|--------|--------------------------|---------------------|--------------------------------------------|------|------------------------|-----------|-------|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Rows with status `received` | 0 |
| Rows with status `waived` | 0 |
| Rows still `pending` | 0 |

## Founder checklist

- [ ] Agree fee (or waiver) at/before kickoff  
- [ ] Add row above (or local private copy if banking detail is sensitive)  
- [ ] CRM `notes`: `fee_received` or `fee_waived` (or `fee_pending`) → [`../commercial/crm-stage-scripts.md`](../commercial/crm-stage-scripts.md)  
- [ ] Tick kickoff precondition “Fee received or explicit waiver logged”  
- [ ] Do not start pack 1 while status is `pending`  

## Stop rules

- No invented payments, receipts, or waivers in the repo.  
- No uncleared MSA/DPA stubs as customer contracts.  
- No win-rate or qualification claims tied to fee collection.  
- Dry-runs (DRY-00x) do not require fee rows.
