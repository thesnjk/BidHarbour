# Observation / screenshare consent email stub

**Epic:** [#1](https://github.com/thesnjk/BidHarbour/issues/1)  
**Use when:** booking a later observation or screenshare after the kit “If later” step  
**Kit:** [`observation-kit-naame-hethel.md`](observation-kit-naame-hethel.md) · Checklist: [`observation-checklist.md`](observation-checklist.md) · Log: [`observation-session-log.md`](observation-session-log.md)  
**Product name:** Supplier Desk  

**Status:** Copy-ready research note — **not** legal advice; **not** a DPA. Verbal consent at the event is also fine; send this the same day when the slot is deferred.

**Rule:** Do not invent consent Actuals. Add an `OBS-*` row only after a completed observation.

---

**Subject:** Supplier Desk research — observation consent ({{slot}})

```text
Hi {{Name}},

Thanks for considering a short workflow observation for my Supplier Desk research (CRM {{crm_id}} if useful).

Proposed slot: {{slot}} (screenshare or on-site walkthrough of your last customer qualification / assurance pack). Redacted materials are fine.

Please reply with one of:
1. **Yes** — happy to proceed on that slot
2. **Reschedule** — suggest another time
3. **Decline** — no problem

If we proceed, we agree:
- Notes only; no photos of certificates or documents with personal data
- You may stop or redact anything at any time
- This is research on how packs get done — not a software demo or sales pitch on the call
- No win-rate or qualification claims; I will not commit your pack files to any public repo

Thanks,
{{Founder}}
Supplier Desk (research) · Norfolk
```

## After send

- [ ] Calendar invite matches `{{slot}}`  
- [ ] On the day: run [`observation-checklist.md`](observation-checklist.md)  
- [ ] After completion: `OBS-YYYYMMDD-##` in [`observation-session-log.md`](observation-session-log.md)  
- [ ] Negatives → [`negative-findings.md`](negative-findings.md) same day  

## Stop rules

- Do not invent OBS rows, consent replies, or scorecard Actuals.  
- Do not commit live customer packs or PII.  
- Do not pitch production SaaS or win rates during observation.
