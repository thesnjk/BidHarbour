# Customer Approver export-gate brief (blank)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use after / with:** Approver review on a live pack — Path B step 5 ([`../operations/approver-review-training.md`](../operations/approver-review-training.md)) · manifest ([`../operations/export-manifest-template.md`](../operations/export-manifest-template.md))  
**Lead gap:** human Approver export gate vs portal auto-submit / autonomous tender-AI  
**Companions:** [`competitive-objection-sheet.md`](competitive-objection-sheet.md) (AI risk / Tender-AI) · [`customer-missing-abstention-brief.md`](customer-missing-abstention-brief.md) · [`customer-conflict-abstention-brief.md`](customer-conflict-abstention-brief.md) · [`customer-expired-abstention-brief.md`](customer-expired-abstention-brief.md) · [`../operations/approver-review-training.md`](../operations/approver-review-training.md) · [`../operations/export-manifest-template.md`](../operations/export-manifest-template.md) · [`../operations/pilot-approver-attestation-log.md`](../operations/pilot-approver-attestation-log.md) · [`../operations/concierge-pilot-runbook.md`](../operations/concierge-pilot-runbook.md) · [`concierge-discovery-demo-runbook.md`](concierge-discovery-demo-runbook.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until filled from a **real** pack’s Approver decision.  
**Do not** invent Approver names, approvals, or evidence in git. Prefer anonymised pack labels; keep customer detail local.

## Goal

One short customer-facing brief: AI / concierge may draft only; a **named Approver** must Approve or Block every export; Supplier Desk does **not** portal auto-submit. Unsupported, expired, or conflicting rows stay blocked unless Approver explicitly waives or resolves.

## Pack header (blank until real)

| Field | Value |
|-------|-------|
| pack_id | |
| Buyer / pack label | |
| Named Approver | |
| Manifest decision | Approve export / Block export |
| Blocking rows (if Block) | *(MISSING / EXPIRED / CONFLICT / unsigned — local only)* |
| Sent date | |
| Logged by | |

## Copy-ready brief

**Subject:** Supplier Desk — who signs the export (pack {{pack_id}})

```text
Hi {{Name}},

For {{buyer_or_pack_label}} (pack {{pack_id}}), a short note on how Supplier Desk gates what leaves your organisation:

1. Concierge / AI may extract, match, and draft. They do **not** approve statements or submit to portals.
2. Your named Approver ({{Approver}}) walks the checklist and export manifest. They **Approve export** only when every required row is approved or explicitly waived — or they **Block export** while gaps remain.
3. Unsupported facts stay **MISSING**. Past review dates stay **EXPIRED**. Two disagreeing in-date sources stay **CONFLICT** until Approver picks or retires one. We will not silent-fill or auto-renew.
4. We do **not** portal auto-submit. After Approve, you (or we, under your instruction) upload via your customer’s channel.

Questions on the gate or the manifest welcome.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

## Founder checklist

- [ ] Named Approver confirmed for this pack ([`../operations/approver-review-training.md`](../operations/approver-review-training.md))  
- [ ] Manifest filled / decision recorded (local; live attestation log if live)  
- [ ] Header fields filled from real decision only  
- [ ] Brief sent (or attached to pack close-out) — no invented Approve  
- [ ] No win-rate / qualification / auto-submit claims in the copy  
- [ ] No live manifest or confidential pack text staged for git  

## Stop rules

- Never invent Approver decisions, waivers, or evidence to “complete” the brief.  
- Never claim portal auto-submit or autonomous bid submission.  
- Never treat DRY Approver rehearsals as live attestation or scorecard Actuals.  
- Never replace Approver training or the export manifest — this brief accompanies them.  
- Live packs: solicitor-cleared MSA/DPA first ([`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md)).  
- This brief is **not** scorecard GO evidence.
