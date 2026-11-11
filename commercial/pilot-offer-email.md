# Discovery → paid pilot offer email (stub)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Status:** Draft customer copy. **Advice required.** Not legal advice; **not** a substitute for a solicitor-cleared MSA/DPA.  
**Offer facts:** [`pilot-offer-sheet.md`](pilot-offer-sheet.md) · Kickoff: [`../operations/pilot-kickoff-checklist.md`](../operations/pilot-kickoff-checklist.md) · Fee log: [`../operations/pilot-fee-waiver-log.md`](../operations/pilot-fee-waiver-log.md)  
**Bridge checklist (discovery/observation → offer):** [`../research/discovery-pilot-offer-bridge.md`](../research/discovery-pilot-offer-bridge.md)  
**Solicitor pack (separate):** [`../security-and-legal/solicitor-send-checklist.md`](../security-and-legal/solicitor-send-checklist.md)  
**Product name:** Supplier Desk

**Solicitor gate:** Do **not** attach uncleared MSA/DPA stubs as customer contracts. Do **not** accept confidential packs until cleared terms are signed, fee/waiver is logged, and Path B-0 kickoff is complete. Do not invent offer/send Actuals in git.

## When to send

| Moment | Use |
|--------|-----|
| After discovery interview (pain confirmed) | **Primary** — Script A |
| Clear “want a pilot” reply after research call booked/done | Script A |
| They ask for pilot **before** research call | Hold Script A; use [`reply-booking-scripts.md`](reply-booking-scripts.md) two-track reply first |
| Cold Email 1 / Week packs | **Do not** send this — discovery first |
| Legal not cleared yet | Script B (deferral) — keep relationship; no packs |

---

## A — Paid pilot offer (post-discovery)

**Subject:** Supplier Desk — paid pilot outline for {{Company}}

```text
Hi {{Name}},

Thanks again for the discovery chat on how {{Company}} handles inbound customer qualification packs.

If useful, here is a concise paid pilot outline for Supplier Desk (founder-operated concierge — not a SaaS hard-sell):

• Duration: 4 weeks  
• Volume: up to 3 inbound PQQ/SQ / document-request packs  
• Fee: {{fee_ex_vat}} ex VAT (band £250–£750; mid anchor £500)  
• Delivery: evidence match + MISSING where unsupported + human Approver before export  
• Excluded: portal auto-submit; inventing certificates; bid-win or qualification guarantees  

Next steps (in order):
1. Solicitor-cleared pilot terms + DPA (I will not take confidential packs on uncleared stubs)  
2. Fee received or explicit waiver logged  
3. Path B-0 kickoff (Approver, encrypted path, baseline minutes)  
4. First pack within week 1 of the pilot window  

Happy to answer questions or adjust timing. No pressure either way — a clear no is useful data too.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour)
```

Default `{{fee_ex_vat}}` to **£500** unless a different band figure was agreed privately (do not invent discounts in git).

---

## B — Soft deferral (legal not ready)

**Subject:** Supplier Desk — holding the pilot outline

```text
Hi {{Name}},

Following our discovery chat, I’d like to offer {{Company}} a paid Supplier Desk pilot once solicitor-cleared terms are ready. I will not ask for confidential packs under uncleared stubs.

I’ll send the full outline (4 weeks / up to 3 packs / fee band) as soon as those documents clear. Until then, happy to stay in touch on research-only questions.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour)
```

---

## After send

1. CRM stage/notes → [`crm-stage-scripts.md`](crm-stage-scripts.md): Script A → keep **Discovery** + `pilot_offer_sent`; stage **Pilot** only after written interest **and** kickoff preconditions in motion.  
2. Do not mark scorecard Paid pilots Actual until a real Path B pilot starts.  
3. On acceptance path: solicitor-cleared MSA/DPA → [`../operations/pilot-fee-waiver-log.md`](../operations/pilot-fee-waiver-log.md) → [`../operations/pilot-kickoff-checklist.md`](../operations/pilot-kickoff-checklist.md).  
4. Dry-runs (DRY-00x) are not paid pilots.

## Stop rules

- No uncleared MSA/DPA stubs as customer contracts.  
- No win-rate or qualification claims.  
- No inventing offers, fees, or CRM Pilot Actuals in git.  
- No confidential pack intake before kickoff preconditions.  
- No SaaS hard-sell on the discovery→offer path.
