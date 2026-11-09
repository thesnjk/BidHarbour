# 19. Operating model

**As-of:** 9 November 2025

## Founder responsibilities

Sales outreach, discovery, pilot delivery, product decisions, security hygiene, scorecard updates.

## Outsource

- Bookkeeping / VAT returns  
- Solicitor review of MSA/DPA/ToS  
- Penetration test before scale (post 15+ customers)  
- Occasional contractor for UI polish post-GO  

## Customer onboarding checklist

1. Signed pilot/sub + DPA  
2. MFA enabled for all users  
3. Approver named  
4. Library import session  
5. First pack walkthrough  
6. Success metrics baseline recorded  
7. Support channel explained  

## Support

- Channels: email (primary); optional scheduled call  
- Hours: Mon–Fri 09:00–17:00 UK  
- Escalation: security/privacy → founder same day; billing → 2 business days  

## Billing and collections

Stripe invoices; failed payment retry 3×; pause processing if 14 days overdue *(policy draft)*.

## Internal procedures to document

- Pilot runbook  
- Incident ownership (`operations/incident-runbook.md`)  
- Release process (post-GO)  
- Product feedback log → backlog  
- Customer offboarding / deletion  
- Business continuity: password manager, repo access, billing admin backup  

## Lean RACI

| Activity | Founder | Contractor | Customer | Solicitor |
|----------|---------|------------|----------|-----------|
| Outreach | R/A | C | I | — |
| Pilot delivery | R/A | C | C | — |
| DPA/MSA | C | — | C | R/A review |
| Product build (post-GO) | R/A | R | I | — |
| Incident response | R/A | C | I | C |
| Bookkeeping | A | R | — | — |

R=Responsible A=Accountable C=Consulted I=Informed

## First hiring trigger

**&gt;15 active subscriptions** AND support **&gt;20 hours/month** sustained for 2 months → part-time customer success — based on workload/economics, not ambition.
