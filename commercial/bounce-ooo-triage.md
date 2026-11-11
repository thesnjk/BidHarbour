# Bounce / OOO / wrong-entity triage

**Epic:** [#6](https://github.com/thesnjk/BidHarbour/issues/6)  
**Use with:** [`week1-send-runbook.md`](week1-send-runbook.md) · [`week2-send-runbook.md`](week2-send-runbook.md) · [`week3-send-runbook.md`](week3-send-runbook.md)  
**Logs:** [`week1-send-log.csv`](week1-send-log.csv) · [`week2-send-log.csv`](week2-send-log.csv) · [`week3-send-log.csv`](week3-send-log.csv)  
**Replies (human):** [`reply-booking-scripts.md`](reply-booking-scripts.md)  
**Product name:** Supplier Desk

**Rule:** Do not invent personal emails or bounce Actuals. Prefer published general inboxes + LinkedIn for named people. Do **not** run Day 3/7/14 non-responder sequences on hard bounces.

## Decision table

| Signal | Send-log `outcome` | `skip_reason` (examples) | CRM | Next action |
|--------|--------------------|--------------------------|-----|-------------|
| Hard bounce (user unknown / mailbox gone) | `bounced` | `hard_bounce` | Fix once or `Disqualified` | One alternate **public** inbox or LinkedIn role-reach; else stop |
| Soft bounce / mailbox full / defer | `bounced` or leave `sent` + note | `soft_bounce` | Keep `Contacted` | Retry **once** after 24–48h; then treat as hard if fails |
| Auto OOO | keep `sent` | (notes: `ooo_until={{date}}`) | `Contacted` | Pause Day 3/7/14 until return; optional OOO ack below |
| Wrong person / left company | `skipped` or `sent` + note | `wrong_person` | Fix contact or `Disqualified` | Wrong-person script; one redirect ask |
| Wrong legal entity | `skipped` | `wrong_entity` | `Disqualified` or correct CRM row | Do not chase; correct seed |
| Anti-persona / size fail | `skipped` | `anti_persona` / `size_check` | `Disqualified` | Honest skip — not a “win” |
| ICP skip (pre-send) | `skipped` | `icp_skip` | `Disqualified` or leave Identified | Do not send Email 1 |

## Founder checklist (same day)

- [ ] Classify signal from table above  
- [ ] Update matching send-log row (`outcome`, `skip_reason`, `notes`)  
- [ ] Update CRM `outreach_status` / `stage`  
- [ ] Cancel or reschedule Day 3/7/14 holds if hard bounce / wrong entity  
- [ ] If retrying: only published contact-page inbox or LinkedIn — **no invented `{first.last}@`**

## Scripts

### OOO acknowledge (optional)

```text
Subject: Re: {{original}}

Thanks {{Name}} — noted you’re back {{return_date}}. I’ll follow up then about a short research chat on your last customer qualification pack (Supplier Desk discovery — not a sales demo).

{{Founder}}
```

### Wrong person — redirect ask

```text
Subject: Re: {{original}}

Sorry to bother you — looks like I reached the wrong desk.

Could you point me to whoever handles customer questionnaires / assurance packs (MD, Ops, or Quality)? Research call only (Supplier Desk); redacted packs fine.

Thanks,  
{{Founder}}
```

### Internal retry note (founder — do not invent addresses)

Before a second send: open the contact-hints file for that CRM band → use only a **different published** general inbox or LinkedIn InMail to a verified role. Log channel = `email` or `linkedin`. If none, set `Disqualified` + `hard_bounce`.

## Stop rules

- No Day 3/7/14 sequence after hard bounce until a successful re-send.  
- No inventing personal emails or logging fictitious sends.  
- No win-rate or qualification claims in recovery messages.  
- Large-group anti-persona skips are not booking wins.
