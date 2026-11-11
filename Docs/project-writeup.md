# BidHarbour — professional project writeup

**As of:** 11 November 2026  
**Product:** BidHarbour / first product **Supplier Desk**  
**Document standard:** NEA-grade comprehensive professional project documentation (Analysis → Design → Implementation → Testing → Evaluation → Operator guide → Bibliography → Appendices), filled iteratively from existing repo sources.  
**Posture:** **INVESTIGATE FURTHER** — validate Norfolk SME PQQ/SQ pack assembly via concierge pilots **before** production SaaS. Scorecard Actuals remain blank until founder interviews and paid pilots land real evidence.

This file is the single scrollable project narrative. It does **not** invent interviews, client quotes, sends, partnerships, or scorecard Actuals. Where live client evaluation is absent, that gap is stated explicitly and provisional evidence is limited to desk research and Path A synthetic dry-runs.

---

## Evidence rules

Label material claims as **Verified fact**, **Reasoned inference**, **Working assumption**, **Proposed experiment**, or **Unresolved question** (standing orders in [`bidharbour-master-prompt.md`](bidharbour-master-prompt.md); fuller rules in [`../strategy/business-plan.md`](../strategy/business-plan.md)).

- AI may extract, match, and draft. **Only authorised humans approve statements and submissions.**
- Where evidence is missing, mark **MISSING** — never invent certifications, policies, insurance, financials, or contractual commitments.
- Distinguish shipped artefacts in git from founder-only field work (sends, interviews, solicitor clearance, IPO spend).

---

## Contents

| Part | Title | Status |
|------|--------|--------|
| 0 | How to read / evidence rules | **Filled** — 11 Nov 2026 |
| 1 | Executive summary & decision posture | **Filled** — 11 Nov 2026 |
| 2 | Analysis | **Filled** — 11 Nov 2026 |
| 3 | Design | *(pending — backlog #66)* |
| 4 | Implementation (shipped artefacts & fixtures) | *(pending — backlog #67)* |
| 5 | Testing (incl. DRY-001–006 formal evidence) | *(pending — backlog #67)* |
| 6 | Evaluation | *(pending — backlog #68)* |
| 7 | Operator / user guide | *(pending — backlog #68)* |
| 8 | Bibliography | *(pending — backlog #69)* |
| 9 | Appendices | *(pending — backlog #69)* |

---

## Part 0 — How to read this

**Last updated:** 11 November 2026

### Navigational spine

| Start | Path | Role |
|-------|------|------|
| Front door | [`../README.md`](../README.md) | Product one-liner + posture |
| Thin index | [`developer-map.md`](developer-map.md) | Folder map + decision gates |
| Living narrative | **this file** | Cumulative professional project writeup |
| Standing orders | [`bidharbour-master-prompt.md`](bidharbour-master-prompt.md) | Agent backlog + non-negotiables |
| Decision owner | [`../strategy/executive-decision.md`](../strategy/executive-decision.md) | INVESTIGATE FURTHER rationale |
| Business plan index | [`../strategy/business-plan.md`](../strategy/business-plan.md) | Sectional strategy outline |
| Validation truth | [`../research/validation-scorecard.md`](../research/validation-scorecard.md) | Criteria + Actuals (still blank pre-founder) |
| Monday ledger | [`../operations/monday-checklist.md`](../operations/monday-checklist.md) | Shipped artefact checklist |

### Shipped in git vs founder-only Actuals

| In git (agent / docs track) | Founder-only (do not invent) |
|-----------------------------|------------------------------|
| Runbooks, CRM packs A01–A50, Week 1–5 outreach, bounce triage, referral / rebook wave | Real outreach sends and reply logs |
| Path B kickoff / fee-waiver / retention / DSR / Approver / close-out artefacts | Live MSA/DPA with customers; solicitor clearance |
| DRY-001–006 pack dry-runs on redacted / synthetic fixtures | Paid pilot packs; minutes-saved Actuals |
| Interview / observation / time-study **templates** (blank Actuals) | Completed interviews; scorecard Actuals |
| Brand clearance checklists and decision memos | IPO / domain spend; HarbourResponse reserve actions |

### What this product is not

Not a generic file store; certificate-expiry tracker alone; supplier directory; buyer-side procurement portal; automated certification service; autonomous estimator; AI allowed to invent compliance answers; or a guarantee of qualification / contract awards. See README and executive decision.

### Post-GO pointer (deferred)

Production SaaS, auth/database scaffold, and engineering MVP implementation stay **out of scope** until validation scorecard **GO**. Intent docs only: [`../product/mvp-spec.md`](../product/mvp-spec.md), [`architecture.md`](architecture.md), [`../product/backlog.md`](../product/backlog.md). Design of the post-GO system is documented later in Part 3; it is **not** claimed as implemented.

### Lead surfaces this writeup consolidates

Hypothesis Lead vs SharePoint / inbound-pack scatter (see [`../research/competitors.md`](../research/competitors.md); no invented proof): inbound pack → structured checklist; evidence match + **MISSING** abstain; human Approver before export; multi-customer packs for one SME; Norfolk pilot price band £250–£750 ex VAT.

---

## Part 1 — Executive summary & decision posture

**Last updated:** 11 November 2026  
**Primary sources:** [`../strategy/executive-decision.md`](../strategy/executive-decision.md) (as-of 9 Nov 2025), [`../research/validation-scorecard.md`](../research/validation-scorecard.md), [`../README.md`](../README.md). Synthesis only — no new claims.

### Product thesis

BidHarbour’s first product, **Supplier Desk**, helps small UK suppliers turn each incoming customer questionnaire or document pack into a reviewer-approved response pack backed by their own evidence library. AI may extract, match, and draft; **only authorised humans approve** statements and submissions. Where evidence is unavailable, mark **MISSING** — never invent compliance answers. (See also “what this product is not” in Part 0 / README.)

### Exact proposed first customer (ICP)

Owner-managed **subcontract engineering, fabrication, or marine/offshore services firm** in **Norfolk** (Norwich, Great Yarmouth, King’s Lynn corridors), **5–75 employees**, selling to **multiple OEMs, tier-1s, or asset operators** that each send **different** qualification templates — not only public-sector tenders.  
*(From executive decision; firm-level demand unverified until interviews.)*

### Recurring problem & promised outcome

| Element | Statement | Label |
|---------|-----------|--------|
| Problem | Each new or renewed customer sends a PQQ/SQ/assurance pack; staff re-hunt certificates, policies, insurance, H&S answers, and case studies across email, SharePoint, and desktops — **2–8+ hours per pack**, with expiry/conflict risk. | Working assumption — must be measured in pilots |
| Promise | **≥40% reduction in admin minutes** from pack receipt to first complete human-approved draft, with **100% requirements mapped** to evidence or explicit missing flags. | Proposed experiment threshold |

### Decision posture

| Decision | Status |
|----------|--------|
| 8-week customer discovery + concierge pilots | **GO** |
| Production SaaS development | **NO-GO until scorecard** |
| Overall | **INVESTIGATE FURTHER** |

Live scorecard Actuals (interviews, observations, paid pilots, continuations) are still **0 / blank** until founder field work lands — see [`../research/validation-scorecard.md`](../research/validation-scorecard.md). Do not treat shipped runbooks as validation proof.

### Proof bar before significant SaaS spend

From the executive decision (thresholds mirrored on the scorecard):

- ≥6/10 interviews report the same recurring pain in **one** niche  
- ≥3 workflow observations with real redacted packs  
- **3 paid pilots**; **≥2** convert to paid continuation  
- Median **≥90 min saved** per pack vs baseline *(or customer-stated equivalent value ≥£150/pack)*

### Revenue model (hypothesis only)

Paid concierge pilot (**£250–£750** ex VAT) → setup/import → subscription band (**£99–£249**/mo). Hybrid managed-service + software acceptable if onboarding stays bounded. *(Proposed experiment — not validated prices.)*

### Fallback stance (do not silent-pivot)

Keep BidHarbour PQQ/SQ response assembly as primary. RFQ quoting is secondary **only if** PQQ validation fails. Holiday-property ops rejected for Norfolk entry. Narrowest entry: private inbound supply-chain packs for Norfolk AME + marine/offshore fabricators — exclude public tender writing as v1.

### Shipped vs founder Actuals

Agent/docs track has seeded ops, CRM, and dry-run artefacts in git. Founder still owns sends, interviews, solicitor-cleared MSA/DPA, and scorecard Actuals. See Part 0 table.

---

## Part 2 — Analysis

**Last updated:** 11 November 2026  
**Purpose:** Define the problem, intended users, desk research base, alternatives, objectives, models, constraints, and assumptions with professional NEA-grade rigour — **without fabricating clients or interview Actuals**.

### 2.1 Problem statement

Small UK suppliers that sell to multiple private customers repeatedly receive **customer-specific** Pre-Qualification Questionnaires (PQQs), Supplier Questionnaires (SQs), and assurance packs. Each pack asks for overlapping but non-identical certificates, policies, insurance schedules, H&S statements, capability claims, and case studies. Staff typically assemble responses by searching email, SharePoint, desktop folders, and prior Word exports. That process is slow, error-prone, and creates liability when expired or conflicting documents are submitted.

**Precise problem (working assumption until measured):** for Norfolk engineering / fabrication / marine SMEs in the ICP, assembling one inbound pack consumes **2–8+ hours** of admin time, with common failures of missed requirements, expired evidence, conflicting answers across packs, and rubber-stamp review without provenance.

**Job to be done:** turn each incoming customer pack into a **complete, evidence-backed, human-approved** response pack — mapping every requirement to approved evidence or an explicit **MISSING** / **EXPIRED** / **CONFLICT** flag — then export with an audit trail.

**Why this is a software-and-process problem (reasoned inference):** the failure modes are checklist completeness, evidence provenance, expiry/conflict detection, and gated human approval — not estimating skill or public-tender discovery. Substitutes (SharePoint alone, one-profile schemes, tender-AI drafting) do not close that loop for multi-customer private packs.

Primary sources: [`../strategy/executive-decision.md`](../strategy/executive-decision.md), [`../strategy/workflow-map.md`](../strategy/workflow-map.md).

### 2.2 Background

#### 2.2.1 Geographic and sector context

| Fact | Source path | Label |
|------|-------------|--------|
| Norfolk active enterprises stock ~33,130 (2023) | [`../strategy/norfolk-market-map.md`](../strategy/norfolk-market-map.md) citing Norfolk’s Story / ONS | Verified fact (as recorded in repo) |
| 99.7% of Norfolk enterprises &lt;250 employees; 88.3% &lt;10 | Norfolk market map | Verified fact (as recorded) |
| Advanced manufacturing & engineering: 2,150 businesses; 47,582 jobs; £2bn GVA (17%) | Norfolk Business Board via market map | Verified fact (as recorded) |
| NAAME: ~5,900 manufacturing businesses Norfolk & Suffolk; ~84,500 employed | naame.co.uk About via market map | Verified fact (as recorded) |

**Limitation:** sector brochure counts may mix enterprises and sites; firm-level questionnaire frequency remains **low confidence** until interviews ([`../strategy/market-size.md`](../strategy/market-size.md)).

#### 2.2.2 Why Norfolk AME / marine is the leading niche

The market map ranks **offshore energy & marine** and **manufacturing & engineering** as Lead attractiveness because they combine verified local density, multi-customer private qualification friction, accessible networks (NAAME, Hethel, EEEZ), and willingness-to-pay analogies in adjacent compliance/tender spend. Tourism/holiday accommodation is explicitly **Avoid** for Norfolk entry; buyer-side food QA and heavy regulated care are out of scope for v1.

#### 2.2.3 Reachable demand (low-confidence sketch)

Bottom-up Norfolk sketch ([`../strategy/market-size.md`](../strategy/market-size.md)): ~2,150 AME → assumed eligible multi-customer fraction → SAM ~430 enterprises → Y1 founder-reachable SOM ~13–22. ACV hypotheses £1.8k–£3.0k. **Conditional scenarios only** — not forecasts.

### 2.3 Intended users / stakeholders

**No live named clients are claimed in this document.** The following describes **intended** users derived from segmentation and the executive decision.

#### 2.3.1 Ideal customer profile (ICP)

| Dimension | Range | Label |
|-----------|-------|--------|
| Activity | CNC / fabrication / maintenance / marine services / small assemblies | Working assumption |
| Employees | 5–75 FTE | Working assumption |
| Turnover | £1m–£25m | Working assumption |
| Incoming packs | 6–30+ / year | Working assumption |
| Distinct customer templates | 3–15 | Working assumption |
| Current software | Microsoft 365 or Google Workspace; maybe light QMS | Working assumption |
| Admin resources | 0.5–1.5 FTE office/quality hybrid | Working assumption |
| Purchasing authority | MD can approve £99–£249/mo without board | Working assumption |

Source: [`../strategy/customer-segmentation.md`](../strategy/customer-segmentation.md).

#### 2.3.2 Buying / operating roles

| Role | Typical title | Job in the workflow |
|------|---------------|---------------------|
| Economic buyer | MD / Ops Director | Approves spend; cares about risk and time |
| Daily user | Quality / admin coordinator | Runs packs |
| Approver | MD or designated competent person | Signs off statements before export |
| Gatekeeper | IT / sometimes customer procurement | MFA, DPA, upload permission |
| Beneficiary | Estimators / engineers | Less document chase |

#### 2.3.3 Anti-personas (do not target)

- Sole traders with &lt;2 questionnaires/year  
- Firms only bidding public sector with a working tender subscription and no private packs  
- Enterprises needing full procurement suite / custom SSO in week one  
- Buyers seeking a supplier directory or accreditation scheme  
- Holiday-let operators (rejected fallback)

### 2.4 Research into the problem

#### 2.4.1 Desk research completed (in repo)

| Theme | Artefact | What it establishes | What it does **not** establish |
|-------|----------|---------------------|--------------------------------|
| Decision posture | [`../strategy/executive-decision.md`](../strategy/executive-decision.md) | INVESTIGATE FURTHER; GO discovery / NO-GO SaaS | Firm-level pain prevalence |
| Market / ICP | norfolk-market-map, customer-segmentation, market-size | Density + ICP hypothesis | Pack frequency Actuals |
| Workflow | [`../strategy/workflow-map.md`](../strategy/workflow-map.md) | Current→future steps; time assumptions | Measured minutes |
| Competition | [`../research/competitors.md`](../research/competitors.md) | Public pricing + Lead/Gap matrix (dated) | Whether buyers will pay BidHarbour |
| Validation design | [`../research/validation-scorecard.md`](../research/validation-scorecard.md), Week 4/8 gates, interview grid | Thresholds and instruments | Any completed interview Actuals (still 0) |
| Path A dry-runs | `operations/pack-dry-run-dry-001.md` … `dry-006.md` + `testdata/` | Fixture-based export-gate behaviour | Live customer pack behaviour |

#### 2.4.2 Planned primary research instruments (blank Actuals)

These instruments exist so founder fieldwork can be recorded honestly. **None are filled with invented respondents.**

| Instrument | Path | Status |
|------------|------|--------|
| Live validation scorecard | [`../research/validation-scorecard.md`](../research/validation-scorecard.md) | Actuals 0 / blank |
| 8-week interview grid | [`../research/interview-grid-8wk.md`](../research/interview-grid-8wk.md) | Template |
| Interview recording / synthesis | `research/recording-template.md`, `interview-synthesis.md` | Templates |
| Observation kit / session log | `research/observation-kit-naame-hethel.md`, `observation-session-log.md` | Templates |
| SharePoint / inbound-pack time-study | [`../research/interview-sharepoint-time-study.md`](../research/interview-sharepoint-time-study.md) | Blank Actuals |
| CRM first-50 + Week 1–5 outreach | `commercial/` | Packs/runbooks shipped; sends founder-only |

#### 2.4.3 Research honesty statement

Unlike a completed client-interview NEA Analysis section, BidHarbour **does not yet have** completed primary interviews or paid pilot Actuals. Analysis therefore rests on desk research + designed experiments. Claiming otherwise would violate evidence rules.

### 2.5 Alternative solutions

Job under comparison: **inbound customer-specific PQQ/SQ pack → checklist → evidence match → MISSING/conflict → human Approver → export**.

#### 2.5.1 Commercial and default substitutes

| Alternative | Why insufficient for this job | Evidence label |
|-------------|-------------------------------|----------------|
| Constructionline / CHAS-like schemes | One shared prequal profile; does not assemble **customer-specific** multi-template responses | Verified fact (product purpose + public pricing recorded in competitors.md) |
| Velstrian / KimonBids / TenderNation | Optimised for **tender discovery + AI drafting**; weak fit for private supply-chain packs; hallucination risk without strict evidence linking | Verified fact (published pricing recorded Nov 2025 / Nov 2026) |
| Evidash | **Buyer-side** vendor doc control; wrong persona; price far above Norfolk SME supplier band | Verified fact (public pricing recorded) |
| Complys | Contractor compliance toward main contractors / RAMS; not OEM inbound pack Approver export | Verified fact (public pricing recorded) |
| SharePoint + spreadsheets | Default £0 substitute; high labour; no checklist/match/approve/export gate | Reasoned inference |
| Manual consultant | £400–£800/day typical; not scalable for recurring packs | Reasoned inference (market rates) |
| QMS platforms | Controlled docs but overkill / wrong UX for inbound pack cycles | Reasoned inference |

Full matrix: [`../research/competitors.md`](../research/competitors.md).

#### 2.5.2 BidHarbour surface Lead / Gap (hypothesis)

| Surface | Posture | Lead / Parity / Gap |
|---------|---------|---------------------|
| Inbound pack → structured checklist | Concierge + fixtures | Lead (hypothesis) vs SharePoint; Gap vs SaaS until GO |
| Evidence match + MISSING abstain | Product principle | Lead vs tender-AI inventing prose |
| Human approval before export | Non-negotiable | Lead vs autonomous bid tools |
| Multi-customer packs | Core thesis | Lead vs single-profile schemes |
| Norfolk SME price | Pilot £250–£750 ex VAT | Lead vs buyer tools; Parity with mid SaaS *if* validated |
| Public tender discovery / RFQ estimating | Out of scope | Gap by design |

#### 2.5.3 Analysis conclusion on alternatives

Adjacent products prove willingness to pay for **some** compliance or tender-response work, but none clearly own the **supplier-side inbound multi-customer pack + evidence graph + Approver export** job at SME price. Differentiation remains a **hypothesis** until pilots measure time saved vs SharePoint.

### 2.6 Objectives

Objectives below adapt Must-have MVP capabilities ([`../product/mvp-spec.md`](../product/mvp-spec.md)) and validation thresholds into Functional (FO) and Non-Functional (NFO) objectives suitable for traceability. Pre-GO, FOs are satisfied by the **concierge operating system + fixtures** where noted; production SaaS realisation is deferred until scorecard GO.

#### 2.6.1 Functional objectives (FO)

| ID | Objective | Pre-GO realisation | Post-GO SaaS |
|----|-----------|--------------------|--------------|
| FO1 | Ingest an inbound customer pack and produce an editable requirement checklist | Path A/B runbooks + redacted fixtures | Request upload + parser |
| FO2 | Maintain an approved evidence library with ownership and review/expiry dates | Synthetic libraries + intake worksheets | Document / DocumentVersion |
| FO3 | Store approved reusable answers linked to evidence | Answer-bank pattern in pilots | ApprovedAnswer + EvidenceLink |
| FO4 | Match requirements to library; flag MISSING / EXPIRED / CONFLICT / CUSTOMER_SPECIFIC | DRY-001–006 method notes | Matcher worker |
| FO5 | Route drafts to a named human Approver; block export until gates pass | Approver training + export manifest | Approval records + hard gates |
| FO6 | Export a complete pack with evidence-version manifest and audit trail | Export manifest template | Export + AuditEvent |
| FO7 | Support multi-customer packs without polluting shared library without promotion | Pilot thesis + architecture rule | Customer + Request isolation |
| FO8 | Capture baseline and post-pack minutes for value proof | Baseline worksheet + metrics stub | In-product metrics later |
| FO9 | Honour retention, deletion, and DSR obligations for pilot data | Retention / DSR one-pagers | Productised DSR flows |
| FO10 | Abstain rather than invent compliance facts | Standing product principle | LLM abstain + provenance |

#### 2.6.2 Non-functional objectives (NFO)

| ID | Objective | Notes |
|----|-----------|--------|
| NFO1 | Trust / confidentiality | DPA/MSA solicitor path before real packs; UK GDPR awareness ([`legal-data-policy.md`](legal-data-policy.md)) |
| NFO2 | Auditability | Every match and export must show provenance |
| NFO3 | Maintainability of ops | Runbooks and monday checklist keep concierge repeatable |
| NFO4 | Cost control pre-GO | No always-on SaaS infra; Path A low-code/manual ([`architecture.md`](architecture.md)) |
| NFO5 | Honesty of validation | Scorecard Actuals never invented; blank until evidence |
| NFO6 | Usability for SME admins | Concierge + clear Approver path; SaaS UX deferred |
| NFO7 | Extensibility | Architecture entities allow post-GO SaaS without changing job-to-be-done |

#### 2.6.3 Justification and prioritisation

| Priority band | Objectives | Why first |
|---------------|------------|-----------|
| P0 | FO4, FO5, FO10, NFO1, NFO5 | Safety and trust: abstain, Approver, no fake Actuals, legal path |
| P1 | FO1–FO3, FO6–FO7 | Core pack assembly loop and multi-customer thesis |
| P2 | FO8–FO9, NFO2–NFO4, NFO6–NFO7 | Proof, compliance ops, economics, future SaaS |

Public tender discovery and RFQ estimating are **explicitly excluded** from v1 objectives (workflow-map scope control).

#### 2.6.4 Measurable success criteria

| Criterion | Threshold | Actual (as of writeup) | Pass? |
|-----------|-----------|------------------------|-------|
| Interview pain convergence | ≥6/10 same problem in niche | 0/10 | — |
| Workflow observations | ≥3 businesses | 0 | — |
| Paid pilots | 3 | 0 | — |
| Continuations | ≥2 | 0 | — |
| Time/value | ≥90 min saved median or ≥£150/pack value | — | — |
| Admin minutes reduction (product promise) | ≥40% vs baseline | — | — |
| Requirements mapped | 100% to evidence or explicit missing flags | Fixture dry-runs only | Provisional on Path A |
| Export gate | Block on MISSING/EXPIRED/CONFLICT without waiver | Demonstrated on DRY-001–006 fixtures | Provisional |

Source of live Actuals table: [`../research/validation-scorecard.md`](../research/validation-scorecard.md).

#### 2.6.5 Objective validation criteria

| Objective set | How validated | When |
|---------------|---------------|------|
| FO1–FO6 (process) | Path A dry-runs on redacted/synthetic fixtures; Path B live packs after MSA/DPA | Dry-runs done in git; live pending |
| FO8 / time promise | Time-study + baseline worksheet + pilot metrics | Founder / pilot |
| FO9 / NFO1 | Solicitor-cleared stubs + retention/DSR drills | Before real packs |
| Market FOs / WTP | Interviews + paid pilots + continuations | Scorecard Week 4 / Week 8 gates |
| Post-GO SaaS FOs | Release criteria in mvp-spec (two real packs on software, export gate tests, zero cross-tenant) | After GO only |

### 2.7 Modelling the problem

#### 2.7.0 Problem decomposition

| Sub-problem | Description | Maps to |
|-------------|-------------|---------|
| D1 Intake | Receive and version the customer pack | FO1 |
| D2 Understand | Extract / curate requirement checklist | FO1 |
| D3 Library | Maintain approved evidence and answers | FO2–FO3 |
| D4 Match | Link requirements to library; classify gaps | FO4, FO10 |
| D5 Approve | Human review per section | FO5 |
| D6 Export | Pack + manifest + audit | FO6 |
| D7 Multi-buyer | Isolate customer-specific vs shared library | FO7 |
| D8 Measure | Baseline vs actual minutes | FO8 |

#### 2.7.1 Current-state → future-state workflow

From [`../strategy/workflow-map.md`](../strategy/workflow-map.md) (times are working assumptions):

| Step | Current failure | Proposed intervention | Human approval |
|------|-----------------|----------------------|----------------|
| Receive | Wrong version filed | Versioned request upload | User confirms customer |
| Understand asks | Missed tables/clauses | Assisted checklist + human edit | User |
| Gather evidence | Expired/wrong file | Evidence library + expiry | User |
| Draft answers | Stale/unsupported claims | ApprovedAnswer match; abstain if none | Approver |
| Internal review | Rubber-stamp | Structured approval per section | **Approver** |
| Submit | Wrong attachment | Export pack + audit | Approver sign-off |
| Archive | Lost provenance | Request + export history | — |

**Time totals:** 3–8+ hours typical *(working assumption — measure in pilots).*

#### 2.7.2 Level-0 data flow (conceptual)

```mermaid
flowchart LR
  CustomerPack[CustomerPack] --> Intake[IntakeChecklist]
  Intake --> Matcher[MatchEngine]
  Library[EvidenceLibrary] --> Matcher
  Answers[ApprovedAnswers] --> Matcher
  Matcher --> GapQueue[GapQueue]
  GapQueue --> Approver[HumanApprover]
  Matcher --> Approver
  Approver --> ExportPack[ExportAndAudit]
  ExportPack --> CustomerOut[CustomerSubmission]
```

Sequence view (from workflow-map):

```mermaid
sequenceDiagram
  participant Customer
  participant User as AdminUser
  participant Desk as SupplierDesk
  participant Lib as EvidenceLibrary
  participant Approver
  Customer->>User: Sends PQQ pack
  User->>Desk: Upload pack
  Desk->>Desk: Extract requirements checklist
  Desk->>Lib: Match approved answers and evidence
  Desk->>User: Missing expired conflict queue
  User->>Approver: Review draft
  Approver->>Desk: Approve or reject per section
  Desk->>User: Export pack and audit trail
```

#### 2.7.3 Conceptual entity model

Core entities from [`architecture.md`](architecture.md) / mvp-spec (design intent; not claimed as implemented SaaS tables):

| Entity | Responsibility |
|--------|----------------|
| Organisation | Tenant boundary |
| User / Role | Admin, Editor, Approver, Viewer |
| Customer | Buyer whose template differs |
| Request | One inbound pack instance |
| Requirement | Checklist item from the pack |
| Document / DocumentVersion | Evidence with expiry/review |
| ApprovedAnswer | Reusable statement linked to evidence |
| EvidenceLink | Requirement ↔ answer/document |
| Approval | Per-section human decision |
| Export / AuditEvent | Gated output + provenance |

**Rule:** shared company evidence lives under Organisation; customer-specific submissions live under Customer + Request and must not pollute the shared library without explicit promotion + approval.

#### 2.7.4 Modelling summary

The problem decomposes cleanly into intake → match → abstain/gap → approve → export, with multi-customer isolation as a first-class concern. This model justifies both the **concierge Path A/B** operating system now and the **lean SaaS** path after GO, without requiring tender-discovery or estimating subsystems.

### 2.8 Requirement derivation process

| Input | Derived requirement class |
|-------|---------------------------|
| Desk research: SharePoint labour + multi-template pain (hypothesis) | FO1–FO4, FO7 |
| Product principle: never invent compliance | FO10, NFO5 |
| Liability / trust | FO5–FO6, NFO1–NFO2 |
| Norfolk SME economics | Pilot fee band; NFO4; subscription hypotheses in Part 1 |
| Legal-data policy | FO9; pre-pilot MSA/DPA artefacts |
| Competitive Lead surfaces | Emphasise Approver export + MISSING abstain over AI bid prose |
| Validation scorecard | Measurable success criteria §2.6.4 |

Derivation is **traceable and revisable**: if interviews falsify pack frequency or WTP, objectives and ICP narrow or STOP per executive decision — they do not silent-pivot to holiday ops.

### 2.9 Constraints

| Constraint | Detail | Label / source |
|------------|--------|----------------|
| Pre-GO no production SaaS | No auth/database scaffold until scorecard GO | Standing orders / architecture Path A |
| No invented Actuals | Interviews, sends, pilot metrics not fabricated | Evidence rules |
| No real customer packs in git | Redacted/synthetic fixtures only under `testdata/` | Legal / git rules |
| Legal before live packs | MSA/DPA solicitor review required | [`legal-data-policy.md`](legal-data-policy.md) |
| AI training | No training on customer documents without written DPA + product design | Legal-data policy |
| Brand | `bidharbour.com` occupied by unrelated EU auction entity — clear or rename before brand investment | Executive decision *(verified fact as recorded)* |
| Founder capacity | Execution branches part-time / full-time / two-person | `strategy/founder-scenarios.md` |
| Scope exclusions | No public tender v1; no RFQ estimating unless PQQ fails; no holiday ops | Workflow-map / executive decision |
| Region ≠ compliance | Hosting region alone does not establish UK GDPR compliance | Legal-data policy |

### 2.10 Assumptions

| ID | Assumption | Label |
|----|------------|--------|
| A1 | Target firms spend 2–8+ hours per inbound pack today | Working assumption |
| A2 | ≥6 packs/year is common enough in ICP to justify tooling | Working assumption |
| A3 | MD can approve £99–£249/mo without board for fitting ICP | Working assumption |
| A4 | Pilot fee £250–£750 ex VAT is acceptable for a measured pack window | Proposed experiment |
| A5 | Multi-customer private packs are the painful job (not Constructionline alone) | Reasoned inference / hypothesis |
| A6 | Concierge Path A can prove the loop before SaaS | Proposed experiment |
| A7 | Human Approver will be accepted as necessary (not a sales blocker) | Working assumption |
| A8 | Norfolk AME/marine density yields reachable SOM via founder-led sales | Working assumption (market-size) |
| A9 | RFQ and holiday fallbacks remain secondary/rejected unless PQQ validation fails | Decision constraint |
| A10 | DRY fixture behaviour is useful provisional evidence but **not** a substitute for live pilots | Methodological assumption |

---

## Parts 3–9 (bodies pending)

| Part | Backlog | Scope |
|------|---------|--------|
| 3 Design | #66 | Goals, architecture intent, data/class design, match/MISSING algorithm, IA, data dictionary, objective traceability |
| 4–5 Implementation + Testing | #67 | Shipped artefacts/fixtures mapping; test strategy; DRY-001–006 as formal evidence |
| 6–7 Evaluation + Operator guide | #68 | FO/NFO evaluation (honest no live clients); operator/user guide |
| 8–9 Bibliography + Appendices | #69 | Sources list; artefact index; dry-run pointers; blank discovery template index |

---

## Changelog

| Date | Change |
|------|--------|
| 11 Nov 2026 | Seeded living writeup: evidence rules, TOC, Chapter 0 navigational spine; chapters 1–10 queued as backlog #64–#68. |
| 11 Nov 2026 | Filled Chapter 1 — executive summary & decision posture (synthesis from executive-decision + scorecard; Actuals unchanged). |
| 11 Nov 2026 | Reframed document to NEA-grade Parts 0–9; filled Part 2 Analysis in full (no invented clients); re-queued Design→Appendices as backlog #66–#69. |
