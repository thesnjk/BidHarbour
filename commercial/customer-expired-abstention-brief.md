# Customer EXPIRED / abstention brief (blank)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use after / with:** Gap queue ([`../operations/missing-queue-email.md`](../operations/missing-queue-email.md)) when any required row is **EXPIRED** — Path B step 4  
**Lead gap:** EXPIRED vs silent renew / autofill (no invented dates)  
**Companions:** [`customer-missing-abstention-brief.md`](customer-missing-abstention-brief.md) · [`customer-conflict-abstention-brief.md`](customer-conflict-abstention-brief.md) · [`competitive-objection-sheet.md`](competitive-objection-sheet.md) (Tender-AI) · [`../operations/approver-review-training.md`](../operations/approver-review-training.md) · [`../operations/concierge-pilot-runbook.md`](../operations/concierge-pilot-runbook.md) · fixture rehearsal [`../operations/pack-dry-run-dry-005.md`](../operations/pack-dry-run-dry-005.md) · [`../operations/pack-dry-run-dry-012.md`](../operations/pack-dry-run-dry-012.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until filled from a **real** pack’s EXPIRED list.  
**Do not** invent renewal dates, backdated schedules, or “current” expiry in git. Prefer anonymised pack labels; keep customer detail local.

## Goal

One short customer-facing brief: when approved evidence is past its review/expiry date, the row stays **EXPIRED** — we cite the existing `evidence_label` and **do not** silent-renew or roll dates forward; you send a renewed document (or your named Approver records a waiver) before export.

## Pack header (blank until real)

| Field | Value |
|-------|-------|
| pack_id | |
| Buyer / pack label | |
| EXPIRED count | |
| Expired list | *(each row: requirement + `evidence_label` — dates local only, or “see gap-queue email dated ___”)* |
| Reply SLA | 3 business days *(or local note)* |
| Named Approver | |
| Sent date | |
| Logged by | |

## Copy-ready brief

**Subject:** Supplier Desk — why some items stay EXPIRED (pack {{pack_id}})

```text
Hi {{Name}},

Alongside the gap list for {{buyer_or_pack_label}} (pack {{pack_id}}), a short note on how Supplier Desk treats expired evidence:

1. We matched your library and found approved evidence past its review or expiry date. Those rows stay **EXPIRED** — we cite the existing evidence label and will not invent a fresh certificate or roll the date forward.
2. That is deliberate. Draft tools often imply coverage is current by silent renew or autofill. Our job is inbound customer packs with honest expiry until you supply a renewed document.
3. Send the renewed evidence via the agreed encrypted path (or confirm not held / N/A with a short rationale); we rematch and continue toward Approver review.
4. Export still needs your named Approver ({{Approver}}) to Approve — we do not portal auto-submit while EXPIRED remains open (unless you record an explicit waiver).

Reply SLA remains **{{SLA}}** business days on the gap queue. Questions welcome.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

## Founder checklist

- [ ] Gap / MISSING queue sent or ready ([`../operations/missing-queue-email.md`](../operations/missing-queue-email.md))  
- [ ] Header filled locally from real EXPIRED rows only — **no invented dates**  
- [ ] Brief sent (or attached to queue email) — **no silent renew**  
- [ ] No win-rate / qualification guarantees in the copy  
- [ ] No confidential pack text staged for git  

## Stop rules

- Never invent or backdate expiry / renewal dates.  
- Never silent-renew expired certificates or treat EXPIRED as in-date.  
- Never claim verified tender-AI renew behaviour beyond positioning.  
- Never treat DRY-005 / DRY-012 fixture dates as live customer Actuals.  
- Never replace the gap-queue email — this brief accompanies it.  
- Live packs: solicitor-cleared MSA/DPA first.
