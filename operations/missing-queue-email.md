# MISSING-queue customer email (pilot)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use at:** Path B step 4 in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**SLA:** customer reply ≤ **3 business days** ([`../research/pilot-design.md`](../research/pilot-design.md))  
**Abstention brief (why gaps stay MISSING):** [`../commercial/customer-missing-abstention-brief.md`](../commercial/customer-missing-abstention-brief.md)  
**Product name:** Supplier Desk

**Rule:** List gaps only. Do **not** invent certifications, insurance, or capabilities. Live packs require solicitor-cleared MSA/DPA.

## When to send

After first-draft match: every requirement still `not_received` / expired without waiver → one MISSING queue email (or encrypted share + email pointer).

## Copy-ready email

**Subject:** Supplier Desk pilot — information still needed for pack {{pack_id}}

```text
Hi {{Name}},

We’re assembling your response pack for {{buyer_or_pack_label}} under the Supplier Desk concierge pilot (pack {{pack_id}}).

The items below are marked **MISSING** — we will not invent answers. If you can supply evidence (or confirm not held / N/A with a short rationale) within **3 business days**, we can continue toward Approver review and export.

| # | Topic / doc_key | What we need |
|---|-----------------|--------------|
| 1 | {{topic_or_doc_key}} | {{expected_evidence_type}} |
| 2 | | |
| 3 | | |

Please reply with files via the agreed encrypted path (or say if an item is not held / N/A).

We will not export required statements without your named Approver’s sign-off.

Thanks,  
{{Founder}}  
Supplier Desk (BidHarbour pilot)
```

## After send

1. Log send time in pack notes / metrics `notes`.  
2. Optionally send / attach [`../commercial/customer-missing-abstention-brief.md`](../commercial/customer-missing-abstention-brief.md) (why we abstain vs autofill).  
3. On receipt: update local intake CSV (`received` / `waived`); rematch checklist.  
4. Still-MISSING after SLA: Approver may **waive** (recorded) or block export — never silent-fill.

## Stop rules

- No live packs on uncleared MSA/DPA stubs.  
- No win-rate or qualification guarantees in the email.  
- Do not commit customer evidence to git.
