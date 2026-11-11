# 10. Pilot design and value measurement

**As-of:** 9 November 2025  
Concierge pilot operable **before** full development.

## Fixed scope

| Item | Spec |
|------|------|
| Duration | 4 weeks |
| Packs | Max **3** inbound PQQ/SQ / document request packs |
| Allowed types | PDF, Word, Excel questionnaires + supporting PDFs |
| Excluded | Full public tenders; engineering estimates; portal auto-submit; custom macros |
| Delivery | Founder-operated concierge using library + checklist + human approve |
| Fee | **£250–£750 ex VAT** *(Proposed experiment)* — suggest £500 mid |

## Dry-run fixture (before real packs)

Use synthetic kit [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) to rehearse checklist → MISSING → Approver → export. **No** live customer documents until MSA/DPA cleared.

**Runbook:** [`../operations/concierge-pilot-runbook.md`](../operations/concierge-pilot-runbook.md) · **Metrics stub:** [`../operations/pilot-metrics-stub.csv`](../operations/pilot-metrics-stub.csv)

## Baseline measurements (week 0)

- Minutes for last comparable pack (participant estimate + any timesheets)  
- Tools used  
- Missing/expired incidents in last 3 packs (recall)  

## Success criteria (pilot)

| Metric | Target |
|--------|--------|
| Admin minutes per request | ≥40% reduction **or** ≥90 min saved |
| Time to first complete draft | Recorded; improve vs baseline |
| Missing-field frequency | All fields mapped to evidence or MISSING |
| Rework loops | ≤1 major rework after approver review |
| Human review effort | Measured; not unbounded |
| Support effort | Founder time logged |
| Repeat usage | Customer requests ≥2nd pack in window if available |
| Willingness to continue | Written yes/no to paid continuation |

**Do not claim** increased bid-win rates.

## Manual work (founder)

- Checklist curation  
- Library tagging  
- Match review  
- Export formatting within agreed templates  
- Training approver on review checklist → [`../operations/approver-review-training.md`](../operations/approver-review-training.md)  

## Customer responsibilities

- Provide evidence folder promptly  
- Name an Approver with authority  
- Respond to MISSING queue within 3 business days  
- Not use outputs without Approver sign-off  

## Data-handling rules

- DPA + pilot MSA in force before real packs  
- Encrypted transfer; access limited to named founder accounts  
- Delete or return within 30 days of pilot end unless subscription continues  
- No model training on customer content  

## Fees, refund, cancellation *(for legal review — Advice required)*

Draft commercial intent only:

- Fee due before pack 1 processing  
- If BidHarbour misses agreed turnaround on 2+ packs due to its fault → refund unused portion  
- Customer may cancel for convenience within 5 days unused → full refund; after work starts → fee non-refundable except fault clause  
- **Solicitor must review before use.**

## After the pilot

1. Results review meeting with metrics  
2. Offer setup + subscription **or** stop  
3. Capture testimonial only with written permission  
4. Update scorecard  

**Scripts:** [`../operations/pilot-closeout-scripts.md`](../operations/pilot-closeout-scripts.md) (post-export A–F).
