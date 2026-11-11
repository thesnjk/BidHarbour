# Referral ask script (post-interview / post-pilot)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Product name:** Supplier Desk  
**Use with:** [`reply-booking-scripts.md`](reply-booking-scripts.md) · [`../operations/pilot-closeout-scripts.md`](../operations/pilot-closeout-scripts.md) · [`go-to-market.md`](go-to-market.md) · [`crm-readme.md`](crm-readme.md) · post–first-50 wave: [`post-first50-referral-wave.md`](post-first50-referral-wave.md) · network venues: [`naame-hethel-gy-network-peer-intro-pack.md`](naame-hethel-gy-network-peer-intro-pack.md)

**Rule:** Keep Supplier Desk research / pilot framing. No win-rate or qualification claims. Do **not** invent named intros, personal emails, or CRM Actuals. Prefer Norfolk **AME / marine** peers who run multi-customer inbound PQQ/SQ packs.

## When to ask

| Moment | Trigger | Ask |
|--------|---------|-----|
| **Post-interview** | End of discovery call (consent already covered) | Up to **2** peer intros |
| **Soft decline** | “Not interested / no time” on outreach reply | **1** intro, no pitch |
| **Post-pilot** | After pack delivered (**A**) or after written continuation **yes** / clean **no** (**D**) | Up to **2** peer intros |
| **Do not ask** | Mid refund/cancel friction; hard bounce; uncleared MSA dispute; testimonial-only thread without rapport | — |

Testimonial ask stays separate → close-out **F**. Referral ask is close-out **G** (this file).

---

## Post-interview (spoken, ~30s)

```text
Before we wrap — do you know one or two peers at similar Norfolk fab or marine firms
who also wrestle with customer questionnaires / qualification packs?

If you’re willing to intro {{Founder}} by email (or share a name + company),
that would help the research. OK to mention you suggested it?
```

If they give a name only (no intro email): thank them; add CRM row; reach via public contact page / general inbox — do not invent a personal address.

---

## Soft-decline email (expand reply-booking)

**Subject:** Re: {{original}}

```text
Thanks for the straight answer — helpful.

If a colleague at a similar Norfolk fab/marine firm might spare 25 minutes on how
they handle customer questionnaires, a name or short intro would be gold.
Either way, appreciate it.

{{Founder}}
```

*(CRM: `outreach_status=declined` or leave Contacted + note; negative-findings if “not a problem for us”.)*

---

## Post-pilot email

**Subject:** Supplier Desk — peer intros?

```text
Hi {{Name}},

Thanks again for the Supplier Desk pilot work with {{Company}}.

If two peers at similar Norfolk AME / marine firms also assemble inbound PQQ/SQ packs
for multiple customers, would you be open to a short email intro? Happy for you to
decline — no pressure, and I will not claim win or qualification outcomes.

OK to use your name when I reach out?

Thanks,
{{Founder}}
Supplier Desk (BidHarbour pilot)
```

**Timing:** after successful pack delivery, or after continuation **yes** / clean **no**. Skip during refund/cancel paths ([`../operations/pilot-refund-cancellation-email.md`](../operations/pilot-refund-cancellation-email.md)).

---

## They refer someone — confirm + CRM

```text
Thanks — I’ll reach out to {{Referral}} at {{ReferralCompany}} and mention you suggested it.
OK to use your name? (Reply yes / no is enough.)
```

**CRM hygiene (same day):**

1. Add new row (beyond A01–A50 if needed, or note on existing id) — stage **Identified**, `outreach_status=queued`.  
2. `source` / notes: `Referral from {{Company}} ({{id if known}})`; evidence = founder-confirmed intro, not invented.  
3. Prefer lead **AME / marine**; do **not** count construction-control / reserve-only / non-ICP as lead wins.  
4. Queue warm-intro outbound below; do not invent personal emails — use public inbox or LinkedIn for named people.

---

## Warm-intro outbound (to the referred contact)

**Subject:** {{ReferrerName}} suggested I contact you — Supplier Desk research

```text
Hi {{Referral}},

{{ReferrerName}} at {{Company}} suggested I get in touch (name used with their OK).

I’m doing short customer-discovery research for Supplier Desk — supplier-side assembly
of inbound qualification packs (PQQ/SQ), not a product demo and not a bid-win pitch.

Would you have 25–30 minutes for a call on the **last** customer questionnaire your
team completed? Happy to work around production.

{{Founder}}
```

If name-use was **no**, omit the referrer sentence and use a neutral “a Norfolk peer suggested…” only if that peer agreed to anonymous mention; otherwise treat as cold discovery using the standard Week packs.

After they say yes → [`reply-booking-scripts.md`](reply-booking-scripts.md) booking block.

---

## After send / after call

1. Log ask date + outcome (intro given / declined / deferred) in interview or pilot notes — never invent.  
2. On intro: create CRM row before sending warm outbound.  
3. Book slots on [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md); scorecard Actuals only after completed interviews.  
4. Annual-plan “free pack credit” for referral cohorts stays a **hypothesis** in [`go-to-market.md`](go-to-market.md) — do not promise in email until solicitor-cleared terms exist.

## Stop rules

- Do not invent named intros, personal emails, or filled CRM Actuals.  
- Do not hard-sell SaaS on referral or discovery calls.  
- Do not claim win rates or guaranteed qualification.  
- Do not count scaffolding / construction-control / reserve network rows as lead ICP wins.  
- Do not ask for referrals during active refund/cancel friction.  
- Do not process referred customers’ confidential packs until solicitor-cleared MSA/DPA.
