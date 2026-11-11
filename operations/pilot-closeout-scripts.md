# Pilot continuation / close-out scripts (post-export)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** Path B steps 6–8 in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) (export delivered + pack closed)  
**Design:** [`../research/pilot-design.md`](../research/pilot-design.md) · Offer: [`../commercial/pilot-offer-sheet.md`](../commercial/pilot-offer-sheet.md)  
**Product name:** Supplier Desk

**Rule:** No win-rate or qualification claims. Live packs require solicitor-cleared MSA/DPA. Dry-runs may rehearse with fixture `pack_id`s (DRY-00x) — do not treat as customer Actuals.

## When to use

| Script | Trigger |
|--------|---------|
| **A** Pack delivered | Export approved; formats + manifest sent |
| **B** Next pack in window | Customer has capacity for pack 2 or 3 inside 4-week pilot |
| **C** Results review invite | Pilot window ending or all packs done |
| **D** Willingness to continue | After results review — written yes/no |
| **E** Close-out / data return | Stop or no continuation; ≤30 days after pilot end |
| **F** Testimonial ask | Optional; only after written permission |
| **Refund / cancel** | Convenience / after-work / fault refund → [`pilot-refund-cancellation-email.md`](pilot-refund-cancellation-email.md) (then **E**) |

---

## A — Pack delivered

**Subject:** Supplier Desk pilot — pack {{pack_id}} delivered

```text
Hi {{Name}},

Pack {{pack_id}} for {{buyer_or_pack_label}} is delivered with the Approver-signed export manifest.

What we sent: {{formats}} (e.g. PDF pack + manifest). We do **not** auto-submit to buyer portals — please upload via your usual channel if required.

We will not claim win or qualification outcomes. Metrics for this pack are logged on our side for the pilot review.

If another inbound pack arrives in the pilot window, reply with the questionnaire + evidence folder and we will open the next pack_id.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

---

## B — Next pack in window

**Subject:** Supplier Desk pilot — ready for pack {{next_pack_id}}?

```text
Hi {{Name}},

We still have capacity for up to {{packs_remaining}} more pack(s) in your 4-week Supplier Desk pilot window (max 3 total).

If a new PQQ/SQ or document request arrives, send the questionnaire + evidence folder via the agreed encrypted path and name the Approver for that pack. We will not invent MISSING evidence and will not export without Approver sign-off.

No pressure if nothing is inbound — we can move to the results review instead.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

---

## C — Results review invite

**Subject:** Supplier Desk pilot — results review (30 min)

```text
Hi {{Name}},

Ready to close the Supplier Desk pilot loop with a short results review?

Proposed agenda (≈30 min):
1. Baseline vs pilot minutes / MISSING / rework for packs completed
2. What worked / what was manual friction
3. Next step: paid continuation (setup + subscription hypotheses) **or** stop cleanly

I will not present bid-win rates. Please suggest two slots this week, or pick one: {{slot_a}} / {{slot_b}}.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

---

## D — Willingness to continue

**Subject:** Supplier Desk — written yes/no on continuation

```text
Hi {{Name}},

Following our results review, please reply with a clear **yes** or **no** on paid continuation under Supplier Desk (setup + subscription bands on the offer sheet are hypotheses — solicitor-cleared terms required before any further confidential packs).

- **Yes** — I will send the current commercial outline and arrange legal review before kickoff.
- **No** — we will run close-out / data return (script E) and stop. If a fee refund/cancel path applies, use [`pilot-refund-cancellation-email.md`](pilot-refund-cancellation-email.md) before or with **E**.

Either answer is useful for our validation scorecard. No win-rate claims either way.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

---

## E — Close-out / data return

**Schedule:** execute per [`pilot-data-retention-schedule.md`](pilot-data-retention-schedule.md) (T+30 from `pilot_end_date`; return or secure delete).

**Subject:** Supplier Desk pilot — close-out and data return

```text
Hi {{Name}},

We are closing your Supplier Desk pilot as of {{pilot_end_date}}.

Per the pilot data-handling rules we will **delete or return** pilot materials within **30 days** of pilot end unless you continue under cleared subscription terms. Please confirm by {{reply_by}}:

1. Prefer **return** of files via the encrypted path, or
2. Prefer **secure delete** (we will confirm when complete)

Named founder accounts only will retain access until then. We will not train models on your content.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```


---

## F — Testimonial ask (optional)

**Subject:** Supplier Desk — permission to quote?

```text
Hi {{Name}},

If the pilot was useful, may we quote a short written testimonial (2–3 sentences) naming {{Company}} and Supplier Desk? Reply **yes** with the exact wording you approve, or **no** — no problem either way.

We will not invent quotes or claim bid-win outcomes.

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

---

## After send

1. Log which script (A–F) and date in pack / pilot notes.  
2. On **D**: record written yes/no for scorecard Actuals only when real (never invent).  
3. On **E**: diary the 30-day delete/return; confirm completion to customer.  
4. On **F**: store approved wording only; discard if declined.

## Stop rules

- No live packs on uncleared MSA/DPA stubs.  
- No win-rate or qualification guarantees.  
- No invented interview / scorecard Actuals.  
- Do not commit live customer files or filled manifests to git.  
- Dry-run rehearsal ≠ pilot success evidence for GO.
