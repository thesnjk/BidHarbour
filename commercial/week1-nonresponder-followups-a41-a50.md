# Week-1 non-responder follow-ups (A41–A50)

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Companions:** [`week1-nonresponder-followups.md`](week1-nonresponder-followups.md) (A01–A20) · [`week1-nonresponder-followups-a21-a40.md`](week1-nonresponder-followups-a21-a40.md) (A21–A40)  
**Use after:** Email 1 sent (same send discipline as [`week1-send-runbook.md`](week1-send-runbook.md) / outreach pack; contact pages from hints below)  
**Contact hints:** [`a41-a50-contact-hints.md`](a41-a50-contact-hints.md)  
**Responders:** use [`reply-booking-scripts.md`](reply-booking-scripts.md) instead  
**Product name:** Supplier Desk  
**Rule:** research framing; no win-rate claims; do **not** invent personal emails or log fictitious sends

## When to use

| Condition | Action |
|-----------|--------|
| `outreach_status=sent`, no reply, not bounced | Run Day 3 → 7 → 14 sequence |
| They replied (any tone) | Stop this sequence; use reply scripts |
| `declined` / `Disqualified` / anti-persona skip | Do not follow up |
| Size / reserve / sector caution (below) | Prefer skip or soft Day 3 only — do not burn Day 7/14 as lead ICP |

Calendar holds: **Day 3, Day 7, Day 14** from `sent_date`.

Applies to CRM **A41–A50** only after first touches are actually sent (never invent `sent` rows). Completes first-50 follow-up coverage.

## Skip / caution band (do not treat as lead ICP wins)

| IDs | Caution |
|-----|---------|
| A41, A45 | **Sector caution** (boatbuilding / Broads leisure) — discovery only if multi-customer quals likely |
| A42, A43 | Lead marine priority when sent — confirm multi-customer quals before counting as ICP win |
| A44, A46 | **SIZE-CHECK** — multi-site / group scale; reserve or network only unless SME unit confirmed |
| A47–A49 | **Reserve / non-ICP** (electric drives, aerospace, simulators) — soft touch only; do not count as fab/marine wins |
| A49 | Verify live inbox / prefer form or LinkedIn before further send |
| A50 | **Not a customer** — Norfolk Calibration / Hethel co-location intro only (same honesty as A25/A26) |

Lead priority for follow-ups when sent: **A42, A43**, then size-check **A44**, sector-check **A41/A45**. Reserve/referral: network via **A50**, then **A47** — skip counting **A46/A48/A49** as lead wins.

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
