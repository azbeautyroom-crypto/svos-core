---
title: Canonical SessionVue Inputs — Source Mapping Manifest
object_type: knowledge
status: review
owner: founder
updated: 2026-07-27
version: 1.1.0
contract: CONTRACT-001
source_of_truth: true
generated: false
---

# Package I1 — Canonical SessionVue Inputs — Source Mapping Manifest

Date: 2026-07-26 · Owner: founder · Source vault: `~/Downloads/SessionVue-OS` (read-only; not modified)
Canonical source of truth: `10 Company/Facts.md` (owner: founder; uses the NOT IN SOURCE convention)

## Product knowledge architecture (LOCKED 2026-07-27)

| Object | Path | Role | `source_of_truth` |
|---|---|---|---|
| **Product Brain** | `company-brain/Products/Product Brain.md` → compiles to `04 Knowledge/Products/Product Brain.md` | Founder product **specification** (intent). Owns product truth. | `true` |
| **Product Implementation Audit** | `company-brain/Products/Product Implementation Audit.md` → compiles to `04 Knowledge/Products/Product Implementation Audit.md` | Living **engineering reference** (code reality + gaps vs Brain). Not a second Product Brain. | `false` |

Rules: link; never merge. When code and Brain disagree, update the Audit; change Product Brain only by founder ruling. Marketing consumes Product Brain for product truth, not the Audit. See Founder Directives: Product Brain / Implementation Audit split.

| Input file | Source file | Source authority | Transformation performed | Unresolved gaps |
|---|---|---|---|---|
| company-brain/Company/Mission.md | `10 Company/Facts.md` §1 (→ `10 Company/Mission/README`) | Canonical, founder, **LOCKED** | Transcribed locked mission ("Content first, software second") verbatim; added Knowledge frontmatter + sections | none |
| company-brain/Company/Vision.md | Founder-approved canonical statement, 2026-07-25 | Canonical, founder | Transcribed founder-approved vision verbatim | none |
| company-brain/Company/Company Identity.md | `10 Company/Facts.md` §1–2 | Canonical, founder | Transcribed identity + positioning facts (founder, target, voice, promise pillars) | none |
| company-brain/Company/Business Model.md | `10 Company/Facts.md` §1,§3,§6,§8 | Canonical, founder, **LOCKED** | Transcribed model ("Independent-first…") + tier/launch summary | **Salon tier pricing NOT IN SOURCE** |
| company-brain/Company/Founder Directives.md | `10 Company/Facts.md` §7,§10 | Canonical, founder, **LOCKED** | Transcribed the 8 locked directives table | none |
| company-brain/Memberships/Membership Brain.md | `10 Company/Facts.md` §3 | Canonical, founder | Transcribed tier structure, tier language (approved/forbidden), pricing display | **Salon tier NOT IN SOURCE** |
| company-brain/Products/Product Brain.md | Founder product architecture rulings 2026-07-27; prior `Facts.md` §3–§6 | Canonical, founder, **LOCKED** intent | Founder specification: Session principle, dual discovery, categories, platform, tier pointer; intent-only (no implementation state) | **Laser / Body sculpting / Dental specialty lists NOT IN SOURCE** |
| company-brain/Products/Product Implementation Audit.md | Product Audit v1 against `/Users/angelplatt/AZBeautyRoom`; intent pointers to Product Brain | Engineering reference (not product truth) | Living audit: Current Implementation · Founder Intent · Gap · Evidence per lifecycle | Gaps recorded inside Audit; closing them is not authorized by recording |
| company-brain/Integrations/Integration Brain.md | `10 Company/Facts.md` §5,§8, Critical Gaps | Canonical, founder | Transcribed Supabase facts + Shelby partnership status | **Sending domain + external integrations beyond verified sources NOT IN SOURCE** |
| company-brain/Company/Operating System Protocol.md | `SessionVue-OS/00 Executive/Operating-System-Protocol.md` | Canonical, founder, verified | Transcribed core principles, canonical Workflow, ownership map, response standard; added frontmatter | none |
| company-brain/Company/Approval Rules.md | `contracts/EXECUTION_CONTRACT.md` (CONTRACT-001) + `10 Company/Facts.md` §10 | Canonical, founder | Assembled approval requirements + locked directives | **Numeric approval thresholds NOT IN SOURCE** |
| projects/Landing Page (Waitlist Website).md | `SessionVue-OS/02 Projects/SessionVue/Website/Landing Page (waitlist website).md` | Canonical, founder (`type: project`) | Transcribed objective, verbatim status/next-action, deliverables, open items; vault cross-refs rendered as plain paths | Completion condition + metrics `NOT IN SOURCE` |
| projects/Pre-Launch Go-to-Market.md | `SessionVue-OS/02 Projects/SessionVue/60 Marketing/Pre-Launch Go-to-Market.md` | Canonical, founder (`type: project`) | Transcribed verbatim goal/status/next-action, funnel, consolidated automations, boundaries | Completion condition + per-platform metric split `NOT IN SOURCE` |
| jobs/README.md | none — vault `80 Operations/Jobs` confirmed **empty** 2026-07-26 | — | Placeholder stub w/ frontmatter | **Global jobs NOT IN SOURCE (no approved source exists yet)** |

## Rules honored
- Wrote only to `inputs/sessionvue/{company-brain,projects,jobs}` (plus this manifest at `inputs/sessionvue/SOURCE_MAPPING.md`, per founder instruction; not copied to generated output).
- No content sourced from `generated/sessionvue-os/`.
- Vault not modified (read-only).
- Approved wording preserved (locked statements transcribed verbatim).
- Genuine gaps marked `NOT IN SOURCE`, not invented.
- Frontmatter (incl. `contract: CONTRACT-001`, `generated: false`) on every authored/copied file.

## Retained NOT IN SOURCE gaps (founder-confirmed 2026-07-26)
- Salon pricing and positioning
- Laser specialty list
- Body sculpting specialty list
- Dental specialty list
- Sending domain
- External integrations beyond verified sources

## Projects & global Jobs (2026-07-26)
- **Projects**: authored from the two founder-approved active projects named in the vault's `02 Projects.md` (Landing Page / waitlist and Pre-Launch Go-to-Market). Additional vault Systems (001 Waitlist, 002 Content Engine, 003 Content Distribution) are **not** yet authored as Project inputs — available if the founder wants them added.
- **Global Jobs**: remain `NOT IN SOURCE` — the vault global-jobs folder is confirmed empty; no approved global Job exists yet.

## Reference conventions (founder ruling 2026-07-26)
- **`referenced-external`** knowledge sources point outside the generated OS knowledge tree (e.g. `contracts/EXECUTION_CONTRACT.md` in the repo, `HQ/Active Priorities.md` in the vault). By ruling, they are **not** mirrored or resolved into OS wikilinks — they are canonical where they live and referenced by path. Non-resolving inside the OS is by design, not a gap.
- **Project Registry** is now generated by the compiler at `06 Registry/Project Registry.md` from the copied Project inputs (deterministic `PRJ-NNN` IDs; title/status/owner from each project's own frontmatter). No facts inferred.

## Scope note
Global `jobs/` input remains incomplete (`NOT IN SOURCE`). The Projects input now covers the two approved active projects but is not necessarily the complete project portfolio.
