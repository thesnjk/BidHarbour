# Pilot refund / cancellation email stubs

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Status:** Draft customer copy. **Advice required.** Not legal advice; **not** a substitute for a solicitor-cleared MSA. Aligns to fee intent in [`../research/pilot-design.md`](../research/pilot-design.md).  
**Related:** [`pilot-fee-waiver-log.md`](pilot-fee-waiver-log.md) · [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md) script **E** · [`../commercial/pilot-offer-sheet.md`](../commercial/pilot-offer-sheet.md) · [`../security-and-legal/pilot-msa-stub.md`](../security-and-legal/pilot-msa-stub.md)  
**Product name:** Supplier Desk

**Rule:** Do not invent refund Actuals or amounts in git. Do not send these under uncleared stubs. After any cancel path, run close-out **E** (data return/delete).

## Triggers (draft commercial intent)

| Case | Intent (pilot-design) | Script |
|------|----------------------|--------|
| **A** Customer cancels for convenience within **5 days**, packs unused | Full refund of fee paid | A below |
| **B** Customer cancels after work started | Fee non-refundable except fault clause | B below |
| **C** BidHarbour fault — missed agreed turnaround on **2+** packs | Refund unused portion | C below |

Amounts stay as `{{amount_ex_vat}}` — fill from private fee log / invoice only.

---

## A — Convenience cancel (≤5 days, unused)

**Subject:** Supplier Desk pilot — cancellation and refund

```text
Hi {{Name}},

We confirm cancellation of your Supplier Desk pilot as of {{pilot_end_date}}, within the unused convenience window.

Per draft pilot terms (solicitor-cleared MSA prevails), we will refund {{amount_ex_vat}} ex VAT to the original payment method. We will also run data return / secure delete (close-out) so materials are not retained beyond the agreed window.

No win-rate or qualification claims apply either way.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

Then: update [`pilot-fee-waiver-log.md`](pilot-fee-waiver-log.md) notes locally → send script **E**.

---

## B — Cancel after work started (non-refundable)

**Subject:** Supplier Desk pilot — cancellation confirmed

```text
Hi {{Name}},

We confirm cancellation of your Supplier Desk pilot as of {{pilot_end_date}}.

Because pack work had already started, the pilot fee is non-refundable under draft commercial intent (except where a fault clause applies — solicitor-cleared MSA prevails). We will still complete data return / secure delete per close-out.

If you believe a fault refund applies, reply with the packs and dates and we will review under cleared terms.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

Then: send script **E**.

---

## C — Fault / unused-portion refund

**Subject:** Supplier Desk pilot — unused-portion refund

```text
Hi {{Name}},

We missed agreed turnaround on two or more packs in your Supplier Desk pilot window. Under draft commercial intent (solicitor-cleared MSA prevails), we will refund the unused portion: {{amount_ex_vat}} ex VAT.

We are also closing the pilot as of {{pilot_end_date}} and will run data return / secure delete unless you prefer to continue under freshly cleared terms.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

Then: local fee-log note → script **E**.

## Stop rules

- No sending under uncleared MSA/DPA stubs.  
- No inventing payment/refund Actuals in the repo.  
- No win-rate or qualification claims.  
- Always follow with script **E** for data handling.
