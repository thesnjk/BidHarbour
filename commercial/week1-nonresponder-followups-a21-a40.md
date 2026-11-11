# Week-1 non-responder follow-ups (A21–A40)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Companions:** [`week1-nonresponder-followups.md`](week1-nonresponder-followups.md) (A01–A20) · [`week1-nonresponder-followups-a41-a50.md`](week1-nonresponder-followups-a41-a50.md) (A41–A50)  
**Use after:** Email 1 sent (same send discipline as [`week1-send-runbook.md`](week1-send-runbook.md) / outreach pack; contact pages from hints below)  
**Contact hints:** [`a21-a30-contact-hints.md`](a21-a30-contact-hints.md) · [`a31-a40-contact-hints.md`](a31-a40-contact-hints.md)  
**Responders:** use [`reply-booking-scripts.md`](reply-booking-scripts.md) instead  
**Product name:** Supplier Desk  
**Rule:** research framing; no win-rate claims; do **not** invent personal emails or log fictitious sends

## When to use

| Condition | Action |
|-----------|--------|
| `outreach_status=sent`, no reply, not bounced | Run Day 3 → 7 → 14 sequence |
| Hard bounce / wrong entity | **Do not** run this sequence → [`bounce-ooo-triage.md`](bounce-ooo-triage.md) |
| They replied (any tone) | Stop this sequence; use reply scripts |
| `declined` / `Disqualified` / anti-persona skip | Do not follow up |
| Size / network / control caution (below) | Prefer skip or soft Day 3 only — do not burn Day 7/14 as lead ICP |

Calendar holds: **Day 3, Day 7, Day 14** from `sent_date`.

Applies to CRM **A21–A40** only after first touches are actually sent (never invent `sent` rows).

## Skip / caution band (do not treat as lead ICP wins)

| IDs | Caution |
|-----|---------|
| A21, A22, A24 | **SIZE-CHECK** / large-group — quality or network only unless SME unit confirmed |
| A25, A26 | **Not a customer** — Hethel / NAAME intro routes only |
| A30 | **Sector caution** (boatbuilding) — discovery only if multi-customer quals likely |
| A31–A35 | **Construction control** — contrast niche; follow up only after fab/marine density |
| A35, A39 | Verify live inbox on site before any further send |
| A40 | Size-check before counting as ICP win |

Lead priority for follow-ups when sent: **A23, A27, A28, A29, A36, A38** (then cautious others).

## Day 3 — short bump

**Channel:** email reply-all thread **or** LinkedIn note (if you have a real connection path — do not invent emails).

**Email subject:** Re: {{original subject}}

```text
Hi {{Name}},

Quick bump on my note about how Norfolk / East Anglia suppliers handle customer qualification packs (PQQ/SQ).

Would 25 minutes on your *last* pack help my Supplier Desk research? Happy to work around a quiet slot this week.

{{Founder}}
```

**LinkedIn note (≤300 chars):**

```text
Hi {{Name}} — emailed about how Norfolk suppliers handle customer qualification packs. Would 25 minutes on your last pack help my research? Happy to share anonymised patterns back.
```

**Log:** send-log `notes` += `fu_d3={{date}}`; CRM notes same.

## Day 7 — artefact ask

**Subject:** One detail on customer questionnaires

```text
Hi {{Name}},

Following up once more. When we speak, could we look at the *structure* of the last questionnaire you completed (redacted is fine)? I’m mapping where time actually goes for Supplier Desk research — not selling software on that call.

If packs aren’t a pain for you, a one-line “not an issue” is still useful data.

{{Founder}}
```

**Log:** `fu_d7={{date}}`.

## Day 14 — breakup

**Subject:** Closing the loop — qualification packs

```text
Hi {{Name}},

Closing the loop on my Supplier Desk research ask. If customer qualification packs aren’t a pain right now, that’s useful data too.

Happy to reconnect in ~6 months, or if a colleague at a similar fab/marine firm might spare 25 minutes, a name/intro would be appreciated.

Thanks either way,  
{{Founder}}
```

**Log:** `fu_d14={{date}}`; CRM may stay `Contacted` with note `sequence_complete_no_reply`.

## After any touch

1. Update [`week1-send-log.csv`](week1-send-log.csv) `notes` (and `reply_date` / `booked_slot` only if they actually reply).  
2. CRM: keep `outreach_status=sent` until reply; then `replied` / `booked` / `declined`.  
3. Never invent scorecard Actuals from silence.

## Stop rules

- Bounce / wrong entity → fix once or `Disqualified`; stop sequence.  
- Explicit no → reply script “not interested”; stop.  
- Soft no (“busy”) → one courtesy, then Day 14 breakup only.  
- Do not attach or request live confidential packs until solicitor-cleared MSA/DPA.  
- Do not invent personal emails; published general inboxes / LinkedIn only.
