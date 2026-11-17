# Customer FO7 scoped-answer brief (blank)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use after / with:** Approver promotes buyer-specific answers on a live pack — Path B FO7 write-back ([`../operations/pilot-fo7-live-writeback-playbook.md`](../operations/pilot-fo7-live-writeback-playbook.md))  
**Lead gap:** multi-customer isolation vs Constructionline-style single profile / silent shared-library pollution  
**Companions:** [`competitive-objection-sheet.md`](competitive-objection-sheet.md) (Constructionline / multi-customer) · [`constructionline-vs-multi-buyer-pack-matrix.md`](constructionline-vs-multi-buyer-pack-matrix.md) · [`../operations/pilot-fo7-live-writeback-playbook.md`](../operations/pilot-fo7-live-writeback-playbook.md) · [`../operations/pilot-dual-buyer-live-window-checklist.md`](../operations/pilot-dual-buyer-live-window-checklist.md) · [`../operations/concierge-pilot-runbook.md`](../operations/concierge-pilot-runbook.md) · [`../operations/approver-review-training.md`](../operations/approver-review-training.md) · [`concierge-discovery-demo-runbook.md`](concierge-discovery-demo-runbook.md)  
**Training only (not live proof):** DRY-007 · DRY-008 · DRY-014 under `operations/`  
**Product name:** Supplier Desk

**Evidence label:** Template only until filled from a **real** pack’s scoped promotions.  
**Do not** invent doc_keys, buyer answers, or promotions in git. Prefer anonymised pack labels; keep live scoped CSVs on the local encrypted path.

## Goal

One short customer-facing brief: buyer-specific approved answers stay **scoped** to that customer; they do **not** silently enter the shared library or appear in another buyer’s pack. Named Approver still gates export.

## Pack header (blank until real)

| Field | Value |
|-------|-------|
| pack_id | |
| Buyer / pack label | |
| customer_id (anonymised OK) | |
| Scoped doc_keys (count / list) | *(local only — no confidential text in git)* |
| Shared library unchanged? | Y / N |
| Named Approver | |
| Sent date | |
| Logged by | |

## Copy-ready brief

**Subject:** Supplier Desk — buyer-specific answers stay scoped (pack {{pack_id}})

```text
Hi {{Name}},

For {{buyer_or_pack_label}} (pack {{pack_id}}), a short note on how Supplier Desk treats answers that apply only to this customer:

1. Some answers are **buyer-specific** (named sites, KPIs, or acknowledgements that only this customer asked for). Your named Approver ({{Approver}}) marks those as scoped to this customer.
2. Scoped answers live in a **customer-scoped** store for this buyer only. They do **not** get copied into the shared company library by default — so the next OEM’s pack cannot silently inherit them.
3. Shared-library answers stay company-wide only when Approver explicitly promotes them as shared-eligible. We never silent-merge buyer-specific text.
4. Export still needs Approver sign-off. We do not portal auto-submit.

If another buyer pack runs in the same pilot window, we match that pack against the shared library plus **that** buyer’s scoped store only — never this one’s.

Questions welcome.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

## Founder checklist

- [ ] Approver named scoped-only vs shared-eligible answers ([`../operations/pilot-fo7-live-writeback-playbook.md`](../operations/pilot-fo7-live-writeback-playbook.md))  
- [ ] Header fields filled locally from real promotions only  
- [ ] Brief sent (or attached to pack close-out) — no invented scoped rows  
- [ ] Shared library untouched unless Approver explicitly promoted shared rows  
- [ ] No win-rate / qualification guarantees in the copy  
- [ ] No live scoped CSV or confidential answer text staged for git  

## Stop rules

- Never invent scoped answers, doc_keys, or evidence to “demonstrate” FO7 in git.  
- Never silent-merge buyer-specific answers into the shared library.  
- Never cite another buyer’s scoped store (FO7 / I5 failure).  
- Never treat DRY-007/008/014 outcomes as live write-back proof or scorecard Actuals.  
- Live packs: solicitor-cleared MSA/DPA first ([`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md)).  
- This brief is **not** scorecard GO evidence.
