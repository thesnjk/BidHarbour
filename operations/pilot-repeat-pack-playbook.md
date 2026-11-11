# Pilot pack 2/3 in-window playbook (Path B repeat)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** Path B step 8 (script **A**) when the pilot window is still open and packs completed &lt; 3  
**Runbook:** [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) Path B  
**Closeout:** [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md) (A → B → C)  
**Fee / waiver (pack 1 gate):** [`pilot-fee-waiver-log.md`](pilot-fee-waiver-log.md)  
**Metrics:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) (`P02` / `P03`)  
**Kickoff (once only):** [`pilot-kickoff-checklist.md`](pilot-kickoff-checklist.md)  
**Design / offer:** [`../research/pilot-design.md`](../research/pilot-design.md) · [`../commercial/pilot-offer-sheet.md`](../commercial/pilot-offer-sheet.md) — 4 weeks · max **3** packs  
**Training (not Actuals):** [`pack-dry-run-dry-008.md`](pack-dry-run-dry-008.md) dual-buyer / FO7 handoff  
**Product name:** Supplier Desk

**Rule:** Research / pilot framing. No win-rate claims. Do **not** invent fee, metrics, or continuation Actuals. DRY-008 rehearses FO7 isolation — it does **not** fill live `P02`/`P03` rows. Do **not** re-run full Path B-0 kickoff for packs 2–3.

## Goal

Raise **second-pack velocity** inside the paid window (multi-customer repeat after Pack 1) without a second fee or legal re-kickoff.

## When to use

| Situation | Action |
|-----------|--------|
| Pack N exported; customer sends next questionnaire | Intake as `P02`/`P03` — Path B steps 1–8; script **B** optional |
| Pack N closed; capacity remains; nothing inbound | Send script **B** (nudge) — see [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md) §B |
| Packs completed = 3 **or** window ending | Skip further B; move to script **C** → [`pilot-results-review-agenda.md`](pilot-results-review-agenda.md) |
| Fee still `pending` for pack 1 | **Block** — resolve [`pilot-fee-waiver-log.md`](pilot-fee-waiver-log.md) before any live intake |
| Window closed / continuation only | Do not open new pack_ids; use C → D → E |

## Preconditions (pack 2/3 — not full Path B-0)

- [ ] Path B-0 kickoff already completed for this customer  
- [ ] Pack 1 fee `received` **or** `waived` (fee log)  
- [ ] MSA/DPA still in force; named Approver available  
- [ ] `packs_completed` &lt; 3; pilot window still open  
- [ ] Encrypted intake path + named-access register still valid  
- [ ] **No second fee** for in-window packs 2–3 unless solicitor-cleared offer/MSA says otherwise  

## Sequence

1. **Close pack N** — Path B steps 6–8; send script **A** (pack delivered).  
2. **Decide next** — inbound pack → step 4; capacity + quiet → send script **B**; window end → script **C**.  
3. **Script B** (if used) — set `{{next_pack_id}}` (`P02`/`P03`), `{{packs_remaining}}` = 3 − packs_completed.  
4. **Intake pack N+1** — new `pack_id`; update local intake CSV; evidence folder for this buyer only.  
5. **Match** — shared library first; customer-scoped store **only** for matching `customer_id` (FO7). Rehearsal: DRY-008 allowed/forbidden table.  
6. **MISSING → Approver → export** — Path B steps 4–6; never invent; never export without Approver.  
7. **Metrics** — one CSV row for this pack (`mode=live` when real); do not treat DRY-008 as live.  
8. **Loop** — if packs &lt; 3 and window open, return to step 1; else script **C**.

```text
Pack N closed (A)
    ├─ inbound next pack ──────────────► Path B 1–8 (P02/P03)
    ├─ capacity + quiet ─► send B ─────► wait / intake
    └─ window end / 3 packs ───────────► C (results review)
```

## Library / FO7 handoff (between packs)

| Allowed | Forbidden |
|---------|-----------|
| Cite shared approved answers for the new pack | Silent copy of buyer-specific answers into shared library |
| Cite that buyer’s customer-scoped store only | Cite another buyer’s scoped answers (FO7 failure) |
| Promote buyer-specific answers to scoped store after Approver | Newest-wins merge without review |
| Keep shared CSV clean across the window | Invent evidence to clear MISSING |

Training characterisation: [`pack-dry-run-dry-008.md`](pack-dry-run-dry-008.md).

## Founder checklist

- [ ] Confirm window dates + packs remaining (private notes OK)  
- [ ] Script A sent for pack N  
- [ ] Script B sent **or** inbound pack received **or** skipped to C  
- [ ] New pack_id logged (`P02` / `P03`)  
- [ ] Metrics row filled after Approver decision (real pilots only)  
- [ ] FO7 check: no cross-buyer scoped cites  
- [ ] Fee log still shows pack-1 gate satisfied — no invented second fee row  

## Stop rules

- Never process pack 2/3 on uncleared MSA/DPA or pending pack-1 fee.  
- Never invent MISSING fills, certifications, or win rates.  
- Never commit live customer packs to git.  
- Never count DRY-008 / other dry-runs as scorecard Actuals.  
- Never open pack 4 inside the pilot window (max 3).  
- Never re-run full kickoff solely for packs 2–3 unless legal terms changed.
