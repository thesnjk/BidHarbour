#!/usr/bin/env python3
"""Generate BidHarbour finance and research workbooks. Run from repo root."""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
THIN = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)
HEADER_FILL = PatternFill("solid", fgColor="1F4E79")
HEADER_FONT = Font(color="FFFFFF", bold=True)
WARN_FILL = PatternFill("solid", fgColor="FFF2CC")
MONEY = "£#,##0.00"
PCT = "0.0%"


def style_header(ws, row, cols):
    for c in range(1, cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.border = THIN


def build_financial_model():
    wb = Workbook()
    ws = wb.active
    ws.title = "Assumptions"
    ws["A1"] = "BidHarbour 24-month financial model"
    ws["A2"] = (
        "All figures EX VAT unless noted. Hypotheses — not promises. As-of 2025-11-09"
    )
    ws["A1"].font = Font(bold=True, size=14)
    ws.merge_cells("A2:F2")
    ws["A4"] = "VAT treatment"
    ws["B4"] = "Modelled ex VAT; account for VAT separately"
    ws["A5"] = "Currency"
    ws["B5"] = "GBP"

    headers = ["Parameter", "Downside", "Base", "Upside", "Unit", "Notes"]
    for i, h in enumerate(headers, 1):
        ws.cell(row=7, column=i, value=h)
    style_header(ws, 7, 6)

    assumptions = [
        ("Starting_cash", 15000, 40000, 75000, "GBP", "Solo / FT / team scenarios"),
        ("Founder_draw_monthly", 0, 2000, 4000, "GBP/mo", "Draw != profit"),
        ("Pilot_fee_avg", 350, 500, 650, "GBP", "Ex VAT"),
        ("Setup_fee_avg", 300, 600, 900, "GBP", "Ex VAT non-recurring"),
        ("Sub_price_monthly", 99, 149, 249, "GBP/mo", "Per organisation"),
        ("Monthly_churn", 0.08, 0.05, 0.025, "pct", "Unvalidated"),
        ("New_subs_per_mo_m1_3", 0, 0, 0, "count", "Validation — pilots only"),
        ("New_subs_per_mo_m4_6", 0.3, 0.8, 1.2, "count", "Post early MVP"),
        ("New_subs_per_mo_m7_12", 0.5, 1.2, 2.0, "count", ""),
        ("New_subs_per_mo_m13_24", 0.4, 1.0, 1.8, "count", "East Anglia if expand"),
        ("Pilots_per_mo_m1_3", 0.5, 1.0, 1.5, "count", ""),
        ("Pilots_per_mo_m4_12", 0.2, 0.4, 0.6, "count", "Tapers as productized"),
        ("Setup_attach_rate", 0.5, 0.8, 1.0, "pct", "Share of new subs paying setup"),
        ("Hosting_base", 50, 80, 120, "GBP/mo", ""),
        ("Hosting_per_customer", 3, 5, 8, "GBP/mo", ""),
        ("AI_OCR_base", 20, 50, 80, "GBP/mo", ""),
        ("AI_OCR_per_customer", 4, 8, 15, "GBP/mo", "Volume sensitive"),
        ("Tools_software", 50, 100, 150, "GBP/mo", ""),
        ("Legal_insurance_alloc", 100, 150, 250, "GBP/mo", "Amortised"),
        ("Travel_sales", 50, 150, 300, "GBP/mo", ""),
        ("Contractor_costs", 0, 0, 500, "GBP/mo", "Upside may use help"),
        ("Payment_fee_rate", 0.029, 0.029, 0.029, "pct", "Card approx"),
        ("Bad_debt_rate", 0.02, 0.01, 0.005, "pct", "From m6"),
        ("Support_hours_per_cust", 1.0, 0.75, 0.5, "hours/mo", ""),
        ("Support_cost_per_hour", 0, 25, 35, "GBP", "0 if founder unpaid opportunity"),
        ("CAC_cash_per_cust", 200, 400, 600, "GBP", "Travel/tools; excludes founder time"),
    ]

    for r, row in enumerate(assumptions, 8):
        for c, val in enumerate(row, 1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.border = THIN
            if c in (2, 3, 4) and row[4] == "pct":
                cell.number_format = PCT
            elif c in (2, 3, 4) and row[4] in ("GBP", "GBP/mo"):
                cell.number_format = MONEY

    ws["A40"] = "Monthly sheet uses INDEX(..., scenario column) driven by Monthly!B1"
    ws["A41"] = "Contribution = Revenue - COGS(hosting+AI+fees+bad debt) - support cash"
    ws["A42"] = "Do not trust LTV/CAC until 6+ months retention data"
    ws["A43"] = "Grant funding not assumed"
    for col in range(1, 7):
        ws.column_dimensions[get_column_letter(col)].width = 22

    wsM = wb.create_sheet("Monthly")
    wsM["A1"] = "Active scenario"
    wsM["B1"] = "Base"
    wsM["B1"].fill = WARN_FILL
    wsM["C1"] = "Type exactly: Downside | Base | Upside"
    wsM["A2"] = "VAT"
    wsM["B2"] = "All amounts EX VAT"
    wsM["A3"] = "Scenario column index"
    wsM["B3"] = '=IF(B1="Downside",2,IF(B1="Base",3,IF(B1="Upside",4,3)))'

    wsM["A5"] = "Resolved parameters"
    wsM["A5"].font = Font(bold=True)
    wsM["A6"] = "Sub_price"
    wsM["B6"] = "=INDEX(Assumptions!$B$12:$D$12,1,$B$3)"
    wsM["B6"].number_format = MONEY
    wsM["A7"] = "Churn"
    wsM["B7"] = "=INDEX(Assumptions!$B$13:$D$13,1,$B$3)"
    wsM["B7"].number_format = PCT
    wsM["A8"] = "Founder_draw"
    wsM["B8"] = "=INDEX(Assumptions!$B$9:$D$9,1,$B$3)"
    wsM["B8"].number_format = MONEY
    wsM["A9"] = "Starting_cash"
    wsM["B9"] = "=INDEX(Assumptions!$B$8:$D$8,1,$B$3)"
    wsM["B9"].number_format = MONEY

    metrics = [
        "Month",
        "New_pilots",
        "Pilot_revenue",
        "New_subs",
        "Churned_subs",
        "Paying_customers_EOM",
        "MRR",
        "Setup_revenue",
        "Gross_revenue",
        "Hosting",
        "AI_OCR",
        "Payment_fees",
        "Bad_debt",
        "COGS_total",
        "Support_cash",
        "Contribution",
        "Founder_draw",
        "Tools",
        "Legal_ins",
        "Travel",
        "Contractors",
        "CAC_spend",
        "OpEx_total",
        "Operating_profit",
        "Cash_EOM",
        "New_subs_assumption",
    ]
    for c, m in enumerate(metrics, 1):
        wsM.cell(row=12, column=c, value=m)
    style_header(wsM, 12, len(metrics))

    for m in range(1, 25):
        r = 12 + m
        wsM.cell(row=r, column=1, value=m)

        if m <= 3:
            wsM.cell(row=r, column=2, value="=INDEX(Assumptions!$B$18:$D$18,1,$B$3)")
            wsM.cell(row=r, column=26, value="=INDEX(Assumptions!$B$14:$D$14,1,$B$3)")
        else:
            wsM.cell(row=r, column=2, value="=INDEX(Assumptions!$B$19:$D$19,1,$B$3)")
            if m <= 6:
                wsM.cell(row=r, column=26, value="=INDEX(Assumptions!$B$15:$D$15,1,$B$3)")
            elif m <= 12:
                wsM.cell(row=r, column=26, value="=INDEX(Assumptions!$B$16:$D$16,1,$B$3)")
            else:
                wsM.cell(row=r, column=26, value="=INDEX(Assumptions!$B$17:$D$17,1,$B$3)")

        wsM.cell(row=r, column=3, value=f"=B{r}*INDEX(Assumptions!$B$10:$D$10,1,$B$3)")
        wsM.cell(row=r, column=3).number_format = MONEY
        wsM.cell(row=r, column=4, value=f"=Z{r}")

        if m == 1:
            wsM.cell(row=r, column=5, value=0)
            wsM.cell(row=r, column=6, value=f"=D{r}")
        else:
            wsM.cell(row=r, column=5, value=f"=F{r-1}*$B$7")
            wsM.cell(row=r, column=6, value=f"=F{r-1}-E{r}+D{r}")

        wsM.cell(row=r, column=7, value=f"=F{r}*$B$6")
        wsM.cell(row=r, column=7).number_format = MONEY
        wsM.cell(
            row=r,
            column=8,
            value=(
                f"=D{r}*INDEX(Assumptions!$B$20:$D$20,1,$B$3)"
                f"*INDEX(Assumptions!$B$11:$D$11,1,$B$3)"
            ),
        )
        wsM.cell(row=r, column=8).number_format = MONEY
        wsM.cell(row=r, column=9, value=f"=C{r}+G{r}+H{r}")
        wsM.cell(row=r, column=9).number_format = MONEY
        wsM.cell(
            row=r,
            column=10,
            value=(
                f"=INDEX(Assumptions!$B$21:$D$21,1,$B$3)"
                f"+F{r}*INDEX(Assumptions!$B$22:$D$22,1,$B$3)"
            ),
        )
        wsM.cell(row=r, column=10).number_format = MONEY
        wsM.cell(
            row=r,
            column=11,
            value=(
                f"=INDEX(Assumptions!$B$23:$D$23,1,$B$3)"
                f"+F{r}*INDEX(Assumptions!$B$24:$D$24,1,$B$3)"
            ),
        )
        wsM.cell(row=r, column=11).number_format = MONEY
        wsM.cell(
            row=r,
            column=12,
            value=f"=I{r}*INDEX(Assumptions!$B$29:$D$29,1,$B$3)",
        )
        wsM.cell(row=r, column=12).number_format = MONEY
        if m >= 6:
            wsM.cell(
                row=r,
                column=13,
                value=f"=I{r}*INDEX(Assumptions!$B$30:$D$30,1,$B$3)",
            )
        else:
            wsM.cell(row=r, column=13, value=0)
        wsM.cell(row=r, column=13).number_format = MONEY
        wsM.cell(row=r, column=14, value=f"=J{r}+K{r}+L{r}+M{r}")
        wsM.cell(row=r, column=14).number_format = MONEY
        wsM.cell(
            row=r,
            column=15,
            value=(
                f"=F{r}*INDEX(Assumptions!$B$31:$D$31,1,$B$3)"
                f"*INDEX(Assumptions!$B$32:$D$32,1,$B$3)"
            ),
        )
        wsM.cell(row=r, column=15).number_format = MONEY
        wsM.cell(row=r, column=16, value=f"=I{r}-N{r}-O{r}")
        wsM.cell(row=r, column=16).number_format = MONEY
        wsM.cell(row=r, column=17, value="=$B$8")
        wsM.cell(row=r, column=17).number_format = MONEY
        wsM.cell(row=r, column=18, value="=INDEX(Assumptions!$B$25:$D$25,1,$B$3)")
        wsM.cell(row=r, column=19, value="=INDEX(Assumptions!$B$26:$D$26,1,$B$3)")
        wsM.cell(row=r, column=20, value="=INDEX(Assumptions!$B$27:$D$27,1,$B$3)")
        wsM.cell(row=r, column=21, value="=INDEX(Assumptions!$B$28:$D$28,1,$B$3)")
        for c in range(18, 22):
            wsM.cell(row=r, column=c).number_format = MONEY
        wsM.cell(
            row=r,
            column=22,
            value=f"=D{r}*INDEX(Assumptions!$B$33:$D$33,1,$B$3)",
        )
        wsM.cell(row=r, column=22).number_format = MONEY
        wsM.cell(row=r, column=23, value=f"=Q{r}+R{r}+S{r}+T{r}+U{r}+V{r}")
        wsM.cell(row=r, column=23).number_format = MONEY
        wsM.cell(row=r, column=24, value=f"=P{r}-W{r}")
        wsM.cell(row=r, column=24).number_format = MONEY
        if m == 1:
            wsM.cell(row=r, column=25, value=f"=$B$9+I{r}-N{r}-W{r}")
        else:
            wsM.cell(row=r, column=25, value=f"=Y{r-1}+I{r}-N{r}-W{r}")
        wsM.cell(row=r, column=25).number_format = MONEY

    for col in range(1, 27):
        wsM.column_dimensions[get_column_letter(col)].width = 14
    wsM.column_dimensions["A"].width = 18

    wsS = wb.create_sheet("Summary", 0)
    wsS["A1"] = "BidHarbour — 24-month summary (ex VAT)"
    wsS["A1"].font = Font(bold=True, size=14)
    wsS["A2"] = (
        "Change scenario on Monthly!B1 (Downside | Base | Upside). "
        "Conditional scenarios — not promises."
    )
    rows = [
        ("A4", "Active scenario", "B4", "=Monthly!B1", None),
        ("A5", "Starting cash", "B5", "=Monthly!B9", MONEY),
        ("A6", "Month 12 MRR", "B6", "=Monthly!G24", MONEY),
        ("A7", "Month 24 MRR", "B7", "=Monthly!G36", MONEY),
        ("A8", "Month 12 paying customers", "B8", "=Monthly!F24", None),
        ("A9", "Month 24 paying customers", "B9", "=Monthly!F36", None),
        ("A10", "Month 24 cash", "B10", "=Monthly!Y36", MONEY),
        ("A11", "Cumulative gross revenue Y1 (m1-12)", "B11", "=SUM(Monthly!I13:I24)", MONEY),
        ("A12", "Cumulative gross revenue Y2 (m13-24)", "B12", "=SUM(Monthly!I25:I36)", MONEY),
        (
            "A13",
            "Cumulative pilot+setup Y1 (non-recurring)",
            "B13",
            "=SUM(Monthly!C13:C24)+SUM(Monthly!H13:H24)",
            MONEY,
        ),
        ("A14", "Min cash over 24m", "B14", "=MIN(Monthly!Y13:Y36)", MONEY),
    ]
    for a, al, b, bf, fmt in rows:
        wsS[a] = al
        wsS[b] = bf
        if fmt:
            wsS[b].number_format = fmt

    wsS["A16"] = "Break-even customers (approx static)"
    wsS["A17"] = "Fixed monthly (draw+tools+legal+travel+contractors+hosting base+AI base)"
    wsS["B17"] = (
        "=Monthly!B8"
        "+INDEX(Assumptions!B25:D25,1,Monthly!B3)"
        "+INDEX(Assumptions!B26:D26,1,Monthly!B3)"
        "+INDEX(Assumptions!B27:D27,1,Monthly!B3)"
        "+INDEX(Assumptions!B28:D28,1,Monthly!B3)"
        "+INDEX(Assumptions!B21:D21,1,Monthly!B3)"
        "+INDEX(Assumptions!B23:D23,1,Monthly!B3)"
    )
    wsS["B17"].number_format = MONEY
    wsS["A18"] = (
        "Contribution per customer approx "
        "(price - hosting/cust - AI/cust - payfee*price - support)"
    )
    wsS["B18"] = (
        "=Monthly!B6"
        "-INDEX(Assumptions!B22:D22,1,Monthly!B3)"
        "-INDEX(Assumptions!B24:D24,1,Monthly!B3)"
        "-(Monthly!B6*INDEX(Assumptions!B29:D29,1,Monthly!B3))"
        "-(INDEX(Assumptions!B31:D31,1,Monthly!B3)*INDEX(Assumptions!B32:D32,1,Monthly!B3))"
    )
    wsS["B18"].number_format = MONEY
    wsS["A19"] = "Break-even customers (if B18>0)"
    wsS["B19"] = (
        '=IF(B18<=0,"n/a — negative unit contribution",ROUNDUP(B17/B18,0))'
    )
    wsS["A21"] = "Sensitivities: toggle Monthly!B1; edit Assumptions price/churn/AI/support rows."
    wsS["A22"] = "See finance/model-assumptions.md. LTV/CAC omitted until retention exists."
    wsS.column_dimensions["A"].width = 70
    wsS.column_dimensions["B"].width = 18

    wsN = wb.create_sheet("Notes")
    wsN["A1"] = "Notes"
    notes = [
        "1. Distinguishes pilot/setup (non-recurring) from MRR.",
        "2. Founder draw is cash cost.",
        "3. LTV/CAC intentionally omitted as reliable metrics.",
        "4. No grants assumed.",
        "5. Paying_customers may be fractional due to churn formula — interpret as average.",
        "6. Validation months intentionally low new subs.",
    ]
    for i, n in enumerate(notes, 2):
        wsN.cell(row=i, column=1, value=n)

    out = ROOT / "finance" / "model-24mo.xlsx"
    wb.save(out)
    print("Wrote", out)


def build_competitor_matrix():
    wb = Workbook()
    wc = wb.active
    wc.title = "Competitors"
    headers = [
        "Product",
        "Target buyer",
        "Core workflow",
        "Pricing",
        "Price date",
        "Onboarding",
        "Integrations",
        "AI functionality",
        "Security (public)",
        "Weakness vs BidHarbour job",
        "Switching implications",
        "Evidence notes",
    ]
    for i, h in enumerate(headers, 1):
        wc.cell(row=1, column=i, value=h)
    style_header(wc, 1, len(headers))

    rows = [
        [
            "Constructionline",
            "Suppliers/buyers construction",
            "Prequal membership profile",
            "From ~GBP399/yr + join fee; 3rd party Mar2025 Bronze319-Platinum2549+99",
            "2025-11-09",
            "Form + assessment",
            "Buyer network",
            "Limited / not pack AI",
            "Scheme platform",
            "One profile != multi-customer pack assembly",
            "Annual membership",
            "Verified public FAQs + 3rd party",
        ],
        [
            "Complys",
            "Main contractors / suppliers",
            "Compliance vault, contractor PQ, RAMS",
            "From ~GBP30/mo; free tier",
            "2025-11-09",
            "Self-serve",
            "Not fully documented here",
            "AI RAMS/checks claimed",
            "UK-focused claims",
            "Not inbound OEM pack assembly",
            "Low-medium",
            "complys.co.uk",
        ],
        [
            "Evidash",
            "Buyer QA food",
            "Vendor doc coverage + validation",
            "GBP649/mo per module (also USD tiers)",
            "2025-11-09",
            "Sales/self",
            "Not fully documented",
            "Extraction + HITL",
            "AWS encrypted claims",
            "Buyer-side; price high for Norfolk SME supplier",
            "Medium",
            "evidash.com",
        ],
        [
            "Velstrian",
            "SME bidders",
            "Tender find + AI draft",
            "GBP49-549/mo",
            "2025-11-09",
            "Self-serve",
            "Higher tiers",
            "Bid drafting credits",
            "Not fully audited",
            "Public tender focus",
            "Low",
            "velstrian.com/pricing",
        ],
        [
            "KimonBids",
            "SME public sector",
            "Tender portals + AI",
            "GBP79-399/mo",
            "2025-11-09",
            "Self-serve",
            "Not fully documented",
            "Bid drafts capped",
            "Not fully audited",
            "Public tender focus",
            "Low",
            "kimonbids.com/pricing",
        ],
        [
            "TenderNation",
            "SME bidders",
            "Discovery + AI",
            "GBP49-149/mo",
            "2025-11-09",
            "Self-serve",
            "Business tier APIs claimed",
            "AI actions",
            "Not fully audited",
            "Public tender focus",
            "Low",
            "tendernation.io",
        ],
        [
            "M365/SharePoint",
            "All",
            "Storage + collab",
            "M365 licence",
            "2025-11-09",
            "Familiar",
            "Office suite",
            "Copilot optional",
            "Org tenant",
            "No checklist/match/approve export gate",
            "High inertia",
            "Reasoned inference",
        ],
        [
            "Manual + consultant",
            "All",
            "Bespoke packs",
            "GBP400-800/day typical",
            "2025-11-09",
            "Human",
            "N/A",
            "None",
            "N/A",
            "Expensive; not scalable",
            "Relationship",
            "Market inference",
        ],
        [
            "ManufactIQ",
            "UK manufacturers",
            "Enquiry to quote to invoice",
            "From GBP99/mo",
            "2025-11-09",
            "Self-serve after demo",
            "Not fully documented",
            "Assistive features claimed",
            "Not fully audited",
            "Estimating CRM — not PQQ pack",
            "Medium",
            "Fallback A",
        ],
        [
            "FabPulse",
            "UK fab shops",
            "Quoting from drawings/email",
            "GBP49-199/mo",
            "2025-11-09",
            "Self-serve",
            "Not fully documented",
            "AI reading tiers",
            "Not fully audited",
            "Quoting not compliance packs",
            "Medium",
            "Fallback A",
        ],
        [
            "Turno",
            "STR hosts",
            "Cleaning turnover",
            "~USD10/property/mo multi",
            "2025-11-09",
            "Self-serve",
            "PMS integrations",
            "Limited for exceptions",
            "Not fully audited",
            "Wrong problem domain",
            "High for hosts",
            "Fallback B reject",
        ],
        [
            "My Supplier List",
            "Unresolved deep review",
            "Supplier list / engagement",
            "Not found in this build",
            "2025-11-09",
            "Not found",
            "Not found",
            "Not found",
            "Not found",
            "Deep review incomplete",
            "-",
            "NOT FOUND != does not exist",
        ],
        [
            "Changeover Master",
            "Holiday lets",
            "Changeover ops",
            "Not fully verified this session",
            "2025-11-09",
            "Not fully verified",
            "Not fully verified",
            "Not fully verified",
            "Not fully verified",
            "Fallback B — rejected for entry",
            "-",
            "Incomplete",
        ],
    ]
    for r, row in enumerate(rows, 2):
        for c, v in enumerate(row, 1):
            cell = wc.cell(row=r, column=c, value=v)
            cell.border = THIN
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    for col in range(1, 13):
        wc.column_dimensions[get_column_letter(col)].width = 18
    out = ROOT / "research" / "competitor-matrix.xlsx"
    wb.save(out)
    print("Wrote", out)


def build_validation_scorecard():
    wb = Workbook()
    ws = wb.active
    ws.title = "Scorecard"
    ws["A1"] = (
        "BidHarbour validation scorecard — management rules, not industry benchmarks"
    )
    ws["A1"].font = Font(bold=True)
    ws["A2"] = "As-of 2025-11-09 — update Actual weekly"

    headers = [
        "Criterion",
        "Threshold",
        "Actual",
        "Pass (Y/N)",
        "Evidence IDs",
        "Notes",
    ]
    for i, h in enumerate(headers, 1):
        ws.cell(row=4, column=i, value=h)
    style_header(ws, 4, 6)

    criteria = [
        ("Interview pain convergence", ">=6/10 same problem in niche", "0/10", "", "", ""),
        (
            "Existing-alternative inadequacy",
            "Majority cannot name tool that completes inbound multi-customer packs",
            "",
            "",
            "",
            "",
        ),
        ("Workflow evidence", ">=3 businesses", "0", "", "", ""),
        ("Paid pilots", "3", "0", "", "", ""),
        ("Continuation", ">=2 pay after pilot", "0", "", "", ""),
        (
            "Time/value delivered",
            ">=90 min saved median OR >=GBP150/pack value",
            "",
            "",
            "",
            "",
        ),
        (
            "Repeat usage",
            ">=2 packs per continuing customer in 60 days",
            "",
            "",
            "",
            "",
        ),
        ("Support effort", "<45 min/customer/mo", "", "", "", ""),
        ("Contribution margin", "Positive by customer #6", "", "", "", ""),
        ("Repeatable acquisition", ">=1 qualified discovery/week", "", "", "", ""),
    ]
    for r, row in enumerate(criteria, 5):
        for c, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=c, value=v)
            cell.border = THIN

    ws["A16"] = "Week 4 gate outcome"
    ws["C16"] = "GO / NARROW / PIVOT / STOP"
    ws["A17"] = "Week 8 gate outcome"
    ws["C17"] = "GO / NARROW / PIVOT / STOP"
    ws["A19"] = "Current recommendation"
    ws["B19"] = "INVESTIGATE FURTHER / NARROW — no production SaaS yet"
    ws["B19"].fill = WARN_FILL

    ws["A21"] = "Interview log (counts toward scorecard)"
    h4 = [
        "ID",
        "Date",
        "Niche",
        "Same pain Y/N",
        "Packs/year",
        "Hours last pack",
        "WTP",
        "Negative finding",
    ]
    for i, h in enumerate(h4, 1):
        ws.cell(row=22, column=i, value=h)
    style_header(ws, 22, 8)
    for r in range(23, 53):
        for c in range(1, 9):
            ws.cell(row=r, column=c).border = THIN

    for col in range(1, 9):
        ws.column_dimensions[get_column_letter(col)].width = 22

    ws2 = wb.create_sheet("PilotMetrics")
    ph = [
        "Pilot ID",
        "Customer (code)",
        "Fee ex VAT",
        "Baseline minutes",
        "Pilot minutes",
        "Minutes saved",
        "Missing fields",
        "Rework loops",
        "Reviewer minutes",
        "Support minutes",
        "Continue Y/N",
    ]
    for i, h in enumerate(ph, 1):
        ws2.cell(row=1, column=i, value=h)
    style_header(ws2, 1, len(ph))
    for r in range(2, 6):
        for c in range(1, len(ph) + 1):
            ws2.cell(row=r, column=c).border = THIN
        ws2.cell(row=r, column=6, value=f'=IF(OR(D{r}="",E{r}=""),"",D{r}-E{r})')

    out = ROOT / "research" / "validation-scorecard.xlsx"
    wb.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    build_financial_model()
    build_competitor_matrix()
    build_validation_scorecard()
    print("Done")
