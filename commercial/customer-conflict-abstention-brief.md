# Customer CONFLICT / abstention brief (blank)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use after / with:** Gap queue ([`../operations/missing-queue-email.md`](../operations/missing-queue-email.md)) when any required row is **CONFLICT** — Path B step 4  
**Lead gap:** CONFLICT + no newest-wins vs tender-AI silent merge / autofill  
**Companions:** [`customer-missing-abstention-brief.md`](customer-missing-abstention-brief.md) · [`customer-expired-abstention-brief.md`](customer-expired-abstention-brief.md) · [`competitive-objection-sheet.md`](competitive-objection-sheet.md) (Tender-AI) · [`../operations/approver-review-training.md`](../operations/approver-review-training.md) · [`../operations/concierge-pilot-runbook.md`](../operations/concierge-pilot-runbook.md) · fixture rehearsal [`../operations/pack-dry-run-dry-006.md`](../operations/pack-dry-run-dry-006.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until filled from a **real** pack’s CONFLICT list.  
**Do not** invent which source is “correct,” merge prose, or pick a schedule in git. Prefer anonymised pack labels; keep customer detail local.

## Goal

One short customer-facing brief: when two (or more) in-date approved evidence sources disagree, the row stays **CONFLICT** — we cite **both** labels and **do not** newest-wins / silent-pick; you (or your named Approver) choose the canonical evidence or retire a duplicate before export.

## Pack header (blank until real)

| Field | Value |
|-------|-------|
| pack_id | |
| Buyer / pack label | |
| CONFLICT count | |
| Conflict list | *(each row: requirement + both `evidence_label`s — or “see gap-queue email dated ___”)* |
| Reply SLA | 3 business days *(or local note)* |
| Named Approver | |
| Sent date | |
| Logged by | |

## Copy-ready brief

**Subject:** Supplier Desk — why some items stay CONFLICT (pack {{pack_id}})

```text
Hi {{Name}},

Alongside the gap list for {{buyer_or_pack_label}} (pack {{pack_id}}), a short note on how Supplier Desk treats conflicting evidence:

1. We matched your library and found more than one in-date approved source for the same requirement. Those rows stay **CONFLICT** — we list both evidence labels and will not invent which one is right.
2. That is deliberate. Draft tools often collapse duplicates or “newest wins” into one answer. Our job is inbound customer packs with an honest dual cite until you tell us the canonical document (or retire the duplicate).
3. Reply with which label to use, or send a clarifying document via the agreed encrypted path; we rematch and continue toward Approver review.
4. Export still needs your named Approver ({{Approver}}) to Approve — we do not portal auto-submit while CONFLICT remains open (unless you record an explicit waiver).

Reply SLA remains **{{SLA}}** business days on the gap queue. Questions welcome.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

## Founder checklist

- [ ] Gap / MISSING queue sent or ready ([`../operations/missing-queue-email.md`](../operations/missing-queue-email.md))  
- [ ] Header filled locally from real CONFLICT rows only — **both** labels listed  
- [ ] Brief sent (or attached to queue email) — **no invented pick**  
- [ ] No win-rate / qualification guarantees in the copy  
- [ ] No confidential pack text staged for git  

## Stop rules

- Never invent which conflicting schedule or document is “correct.”  
- Never silent-pick the newer file (no newest-wins).  
- Never claim verified tender-AI conflict behaviour beyond positioning.  
- Never treat DRY-006 / fixture CONFLICT as live customer Actuals.  
- Never replace the gap-queue email — this brief accompanies it.  
- Live packs: solicitor-cleared MSA/DPA first.
