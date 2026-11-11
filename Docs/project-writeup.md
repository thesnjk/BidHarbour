# BidHarbour — living project writeup

**As of:** 11 November 2026  
**Product:** BidHarbour / first product **Supplier Desk**  
**Posture:** **INVESTIGATE FURTHER** — validate Norfolk SME PQQ/SQ pack assembly via concierge pilots **before** production SaaS. Scorecard Actuals remain blank until founder interviews and paid pilots land real evidence.

This file is the single scrollable narrative for the project. Chapters fill iteratively from existing repo sources only. It does **not** invent interviews, sends, quotes, partnerships, or scorecard Actuals.

---

## Evidence rules

Label material claims as **Verified fact**, **Reasoned inference**, **Working assumption**, **Proposed experiment**, or **Unresolved question** (standing orders in [`bidharbour-master-prompt.md`](bidharbour-master-prompt.md); fuller rules in [`../strategy/business-plan.md`](../strategy/business-plan.md)).

- AI may extract, match, and draft. **Only authorised humans approve statements and submissions.**
- Where evidence is missing, mark **MISSING** — never invent certifications, policies, insurance, financials, or contractual commitments.
- Distinguish shipped artefacts in git from founder-only field work (sends, interviews, solicitor clearance, IPO spend).

---

## Contents

| Ch | Title | Status |
|----|--------|--------|
| 0 | How to read this | **Filled** — 11 Nov 2026 |
| 1 | Executive summary & decision posture | **Filled** — 11 Nov 2026 |
| 2 | Market, ICP, Norfolk AME wedge | *(pending — backlog #65)* |
| 3 | Problem workflow & product promise | *(pending — backlog #65)* |
| 4 | Competition & differentiation | *(pending — backlog #66)* |
| 5 | Validation scorecard & gates | *(pending — backlog #66)* |
| 6 | Pilot operating system (Path A / B-0 / B) | *(pending — backlog #67)* |
| 7 | Pack dry-runs DRY-001–006 | *(pending — backlog #67)* |
| 8 | CRM & outreach (A01–A50 + waves) | *(pending — backlog #68)* |
| 9 | Security, legal, data | *(pending — backlog #68)* |
| 10 | Brand, finance, risks, roadmap | *(pending — backlog #68)* |
| 11 | Post-GO MVP & engineering (deferred) | Stub only until scorecard **GO** — see Ch 0 |
| 12 | Artefact index & changelog | Living — updated each writeup PR |

---

## Chapter 0 — How to read this

**Last updated:** 11 November 2026

### Navigational spine

| Start | Path | Role |
|-------|------|------|
| Front door | [`../README.md`](../README.md) | Product one-liner + posture |
| Thin index | [`developer-map.md`](developer-map.md) | Folder map + decision gates |
| Living narrative | **this file** | Cumulative project writeup |
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

### Post-GO pointer (Ch 11 deferred)

Production SaaS, auth/database scaffold, and engineering MVP implementation stay **out of scope** until validation scorecard **GO**. Intent docs only: [`../product/mvp-spec.md`](../product/mvp-spec.md), [`architecture.md`](architecture.md), [`../product/backlog.md`](../product/backlog.md).

### Lead surfaces this writeup consolidates

Hypothesis Lead vs SharePoint / inbound-pack scatter (see [`../research/competitors.md`](../research/competitors.md); no invented proof): inbound pack → structured checklist; evidence match + **MISSING** abstain; human Approver before export; multi-customer packs for one SME; Norfolk pilot price band £250–£750 ex VAT.

---

## Chapter 1 — Executive summary & decision posture

**Last updated:** 11 November 2026  
**Primary sources:** [`../strategy/executive-decision.md`](../strategy/executive-decision.md) (as-of 9 Nov 2025), [`../research/validation-scorecard.md`](../research/validation-scorecard.md), [`../README.md`](../README.md). Synthesis only — no new claims.

### Product thesis

BidHarbour’s first product, **Supplier Desk**, helps small UK suppliers turn each incoming customer questionnaire or document pack into a reviewer-approved response pack backed by their own evidence library. AI may extract, match, and draft; **only authorised humans approve** statements and submissions. Where evidence is unavailable, mark **MISSING** — never invent compliance answers. (See also “what this product is not” in Chapter 0 / README.)

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

Agent/docs track has seeded ops, CRM, and dry-run artefacts in git. Founder still owns sends, interviews, solicitor-cleared MSA/DPA, and scorecard Actuals. See Chapter 0 table.

---

## Chapters 2–12 (bodies pending)

Bodies for Ch 2–10 land in backlog rows **65–68**. Until then, use the spine links in Chapter 0 and the Monday checklist for artefact discovery.

---

## Changelog

| Date | Change |
|------|--------|
| 11 Nov 2026 | Seeded living writeup: evidence rules, TOC, Chapter 0 navigational spine; chapters 1–10 queued as backlog #64–#68. |
| 11 Nov 2026 | Filled Chapter 1 — executive summary & decision posture (synthesis from executive-decision + scorecard; Actuals unchanged). |
