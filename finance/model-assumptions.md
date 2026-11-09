# 17. Financial model — assumptions and formulas

**Companion file:** `finance/model-24mo.xlsx`  
**As-of:** 9 November 2025  
**VAT treatment:** Modelled figures are **ex VAT**. VAT on eligible sales/costs handled separately in accounting; do not mix gross/net in contribution.

## Scenarios

| | Downside | Base | Upside |
|--|----------|------|--------|
| Starting cash | £15,000 | £40,000 | £75,000 |
| Founder draw / mo | £0 | £2,000 | £4,000 (team) |
| Monthly churn | 8% | 5% | 2.5% |
| New subs / mo after m6 | 0.5 | 1.2 | 2.0 |
| Pilot fee avg | £350 | £500 | £650 |
| Sub price | £99 | £149 | £249 |
| Setup fee avg | £300 | £600 | £900 |

## Formulas (implemented in workbook)

- `MRR_t = PayingCustomers_t * Price`  
- `PayingCustomers_t = PayingCustomers_{t-1} * (1 - Churn) + NewSubs_t`  
- `SetupRevenue_t` and `PilotRevenue_t` tracked **separate** from recurring  
- `GrossRevenue_t = Pilot + Setup + MRR + Overage`  
- `COGS_t ≈ Hosting + AI/OCR + PaymentFees`  
- `Contribution_t = GrossRevenue_t - COGS_t - SupportLabourCash`  
- `OpEx_t = FounderDraw + Tools + LegalInsuranceAlloc + Travel + Contractors + Other`  
- `OperatingProfit_t = Contribution_t - (OpEx_t - SupportLabourCash already in contrib if cash)` — see sheet notes  
- `Cash_t = Cash_{t-1} + GrossRevenue_t - COGS_t - OpEx_t - PaymentFees`  
- Payment fees ≈ 2.9% * card revenue *(assumption)*  
- Bad debt ≈ 1% of invoice revenue after m6 *(assumption)*  

## Break-even customers (illustrative)

At £149/mo, £2,000 founder draw, £400 variable+tools:  
`Customers ≈ (FounderDraw + FixedOpEx - Setup/Pilot avg) / (Price - variable per cust)`  
Workbook computes sensitivity. Desk estimate **~25–40** orgs if draw minimal — **Reasoned inference**.

## Do not trust yet

LTV/CAC before 6+ months retention data.  
Grant funding **not** assumed.

## Distinctions

- Founder salary/draw ≠ profit ≠ available cash  
- Setup/pilot = non-recurring  
- Support labour included in economics
