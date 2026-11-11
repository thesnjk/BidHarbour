# CRM stage transition scripts + notes conventions

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**CRM:** [`crm-accounts.csv`](crm-accounts.csv) · [`crm-readme.md`](crm-readme.md)  
**Offer path:** [`pilot-offer-email.md`](pilot-offer-email.md) · Fee: [`../operations/pilot-fee-waiver-log.md`](../operations/pilot-fee-waiver-log.md) · Continuation: [`../operations/pilot-continuation-log.md`](../operations/pilot-continuation-log.md)  
**Product name:** Supplier Desk

**Rule:** Update `stage` / `outreach_status` / `notes` the **same day** as the trigger. Do **not** invent transitions or scorecard Actuals. Never put confidential pack contents in `notes`.

## Stages (when to advance)

| Stage | Enter when | Typical `outreach_status` | Required `notes` tags (as applicable) |
|-------|------------|---------------------------|----------------------------------------|
| Identified | Seeded / referral created | `not_started` / `queued` | optional `referral_from={{id}}` |
| Contacted | Email 1 or LinkedIn first touch sent | `sent` | — |
| Discovery | Reply booked **or** interview completed | `booked` / `replied` | optional `int={{INT-ID}}` |
| Discovery (offer out) | Post-interview pilot outline sent | keep Discovery | `pilot_offer_sent` |
| Pilot | Written interest **and** kickoff preconditions in motion | — | `pilot_offer_accepted`; then fee/MSA tags below |
| Active | Written continuation **yes** + cleared continuation terms in force | — | `continuation_yes` · `msa_cleared` |
| Churned | Soft stop / continuation **no** / window ended without Active | — | `continuation_no` or `stopped` |
| Disqualified | Hard bounce exhausted, wrong entity, anti-persona, size fail | `declined` / skipped | `hard_bounce` / `wrong_entity` / `anti_persona` / `size_check` |

Reserve / construction-control / non-ICP rows may move stages for honesty — **do not** count them as lead ICP wins.

## Transition playbook

### A — Booked discovery call

1. `stage=Discovery` · `outreach_status=booked`  
2. Set send-log `reply_date` / `booked_slot`; add grid slot.  
3. `notes`: `int_pending` until INT-ID exists.

### B — Interview done

1. Keep `Discovery`.  
2. `notes`: `int={{INT-ID}}` (and time-study if used).  
3. If pain fits ICP and they are open to a pilot → send [`pilot-offer-email.md`](pilot-offer-email.md) Script A → add `pilot_offer_sent`.  
4. If legal not ready → Script B deferral; keep Discovery + `pilot_offer_held_legal`.

### C — Written interest in paid pilot

1. Move to `Pilot` only when kickoff is **in motion** (MSA/DPA path, fee discussion, or kickoff booked) — not on “sounds interesting” alone.  
2. `notes`: `pilot_offer_accepted` · `fee_pending` until logged.  
3. On fee: update [`../operations/pilot-fee-waiver-log.md`](../operations/pilot-fee-waiver-log.md) **and** CRM `fee_received` or `fee_waived`.  
4. On cleared MSA/DPA: add `msa_cleared` (date in private notes OK).

### D — Continuation yes/no

1. Log written decision in [`../operations/pilot-continuation-log.md`](../operations/pilot-continuation-log.md).  
2. `yes` → `notes=continuation_yes`; stage **Active** only after cleared continuation terms (else stay Pilot + `continuation_yes` · `msa_pending`).  
3. `no` → `notes=continuation_no`; stage **Churned**; run close-out E.

### E — Decline / disqualify

1. Soft decline → `outreach_status=declined`; leave Contacted or Discovery + note; optional referral ask.  
2. Hard bounce / wrong entity / anti-persona → `Disqualified` + triage tags from [`bounce-ooo-triage.md`](bounce-ooo-triage.md).

## `notes` tag vocabulary

| Tag | Meaning |
|-----|---------|
| `pilot_offer_sent` | Offer email Script A sent |
| `pilot_offer_held_legal` | Deferral Script B — waiting on solicitor |
| `pilot_offer_accepted` | Written interest; kickoff path started |
| `fee_pending` / `fee_received` / `fee_waived` | Align with fee log |
| `msa_cleared` / `msa_pending` | Cleared terms status |
| `continuation_yes` / `continuation_no` | Align with continuation log |
| `int={{INT-ID}}` | Completed interview id |
| `referral_from={{id}}` | Warm intro source |

Combine tags with spaces (e.g. `pilot_offer_sent fee_pending`). No pack file paths or cert contents.

## Same-day checklist

- [ ] Stage matches the latest real trigger  
- [ ] Tags match fee / continuation / offer artefacts (never invent)  
- [ ] Lead ICP vs reserve labelled in notes if relevant  
- [ ] Scorecard Actuals unchanged unless a real interview/pilot/continuation landed  

## Stop rules

- Do not invent CRM stages, fees, continuations, or INT-IDs.  
- Do not put confidential customer packs in git or CRM `notes`.  
- Do not count reserve / non-ICP / control-niche as lead wins.  
- Do not move to Pilot on uncleared MSA/DPA stubs alone.  
- No SaaS hard-sell encoded as stage pressure.
