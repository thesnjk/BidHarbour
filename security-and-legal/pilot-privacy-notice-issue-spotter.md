# Pilot privacy notice — issue-spotter draft

**Epic:** [#5](https://github.com/thesnjk/BidHarbour/issues/5)  
**Status:** Draft issue-spotter for solicitor. **Not legal advice.**  
**Do not send to customers until counsel clears** a privacy notice (or confirms none is required at Path A pilot stage).  
**Aligns with:** [`../Docs/legal-data-policy.md`](../Docs/legal-data-policy.md) · [`dpa-stub.md`](dpa-stub.md) · [`tos-privacy-stubs.md`](tos-privacy-stubs.md) · [`subprocessors-and-data-flow.md`](subprocessors-and-data-flow.md) · [`international-transfers-decision-tree-annex-stub.md`](international-transfers-decision-tree-annex-stub.md)  
**Product name:** Supplier Desk (BidHarbour)

**Rule:** Expands the heading list in [`tos-privacy-stubs.md`](tos-privacy-stubs.md) for **Path A concierge pilots**. Does **not** invent a live notice, clearance, or customer send.

---

## 1. Audiences and roles *(Reasoned inference — confirm with counsel)*

| Audience / data | Typical role | Notes for notice / DPA |
|-----------------|--------------|------------------------|
| Customer organisation uploading PQQ/SQ packs | **Controller** | Packs may contain personal data (names, HR/training, contacts) |
| BidHarbour operator processing those packs | **Processor** | Concierge Path A: founder laptop + named-access encrypted path |
| BidHarbour CRM / billing / outreach contacts | BidHarbour as **Controller** | Separate from pack processing; public company contacts only in git CRM |
| Named Approver at customer | Customer personnel | Approval gate — not BidHarbour inventing facts |

Solicitor ask-back (also in [`solicitor-send-checklist.md`](solicitor-send-checklist.md)): **is a privacy notice needed at pilot stage?** for (a) pack processing and/or (b) BidHarbour’s own CRM.

---

## 2. What Path A pilot processing covers

| Activity | Personal data risk | Control posture (design) |
|----------|--------------------|--------------------------|
| Intake of customer packs | High if packs include individuals | Encrypted path; named-access register; no live packs in git |
| Checklist extract / match / MISSING flags | Medium | Human process; AI assist only if contracted |
| Approver review + export manifest | Medium | Named Approver; export blocked on hard gaps |
| Email / scheduling with customer | Medium | Prefer links over attaching full packs |
| Optional LLM / OCR | High if used | Minimise; **no-train** / ZDR preferred; record model/version |
| Retention then deletion/return | Medium | Ops schedule → [`../operations/pilot-data-retention-schedule.md`](../operations/pilot-data-retention-schedule.md) |
| DSR assist | Medium | [`pilot-dsr-handling.md`](pilot-dsr-handling.md) |

Path B SaaS (tenant app, MFA, RLS) is **out of scope** for this pilot-focused spotter — design intent only until scorecard GO.

---

## 3. Issue-spotter sections (placeholders for counsel)

Replace `{{…}}` when drafting the cleared notice. Do not fill with invented legal conclusions.

### Who we are

- Legal entity name: `{{BidHarbour legal name}}`  
- Contact: `{{privacy contact email / address}}`  
- Product: Supplier Desk (concierge pilot)

### What data we process

- Pack contents as supplied by customer (may include personal data — **Advice required** for categories list)  
- Account / contact details for pilot coordination  
- Approver identity and approval timestamps (manifest)  
- Optional: model/version logs if LLM assist used

### Purposes and lawful bases

| Purpose | Lawful basis placeholder | Notes |
|---------|--------------------------|-------|
| Prepare evidence-backed PQQ/SQ response packs | `{{counsel: contract / legitimate interests / …}}` | Processor acts on customer instructions |
| Security, audit, breach handling | `{{…}}` | Align incident runbook |
| CRM / outreach (BidHarbour controller) | `{{…}}` | Separate notice/path if required |

### Processors / subprocessors

Working inventory → [`subprocessors-and-data-flow.md`](subprocessors-and-data-flow.md).  
**Hosting region alone does not establish UK GDPR compliance.**

### International transfers

If any subprocessor processes outside UK/EEA → decision tree annex  
→ [`international-transfers-decision-tree-annex-stub.md`](international-transfers-decision-tree-annex-stub.md).  
Stub ≠ approved transfer mechanism.

### Retention

Default pilot clock + asset classes → [`../operations/pilot-data-retention-schedule.md`](../operations/pilot-data-retention-schedule.md). Solicitor annex prevails when cleared.

### Rights / complaints

- Individual rights intake (via controller / processor assist) → [`pilot-dsr-handling.md`](pilot-dsr-handling.md)  
- UK complaints: Information Commissioner’s Office (ICO) — `{{counsel confirm wording}}`

### Product principles to reflect in notice language *(not a compliance claim)*

1. AI may assist extraction, retrieval, drafting.  
2. **Only authorised humans** approve statements and submissions.  
3. Unsupported facts → **MISSING** — never invent certifications, insurance, financials, or contractual commitments.  
4. **No training** of foundation models on customer pack content without written agreement.

---

## 4. Founder / solicitor checkboxes

- [ ] Counsel confirms: privacy notice **required** / **not required** / **deferred** at Path A pilot stage  
- [ ] If required: cleared notice version stored outside git (or vault); date logged privately  
- [ ] Controller vs processor mapping confirmed in DPA  
- [ ] Subprocessor list reviewed against live pilot tooling  
- [ ] Transfers annex completed for any non-UK/EEA processing  
- [ ] CRM / outreach notice path decided (separate from pack processing)  
- [ ] **Do not** send this stub or uncleared copy to customers  

---

## 5. Related solicitor pack

Attach with [`solicitor-send-checklist.md`](solicitor-send-checklist.md) and [`solicitor-cover-email.md`](solicitor-cover-email.md).  
Cleared solicitor drafts prevail over this issue-spotter.
