---
title: Canonical SessionVue Inputs — Source Mapping Manifest
object_type: knowledge
status: review
owner: founder
updated: 2026-07-26
version: 1.0.0
contract: CONTRACT-001
source_of_truth: true
generated: false
---

# Package I1 — Canonical SessionVue Inputs — Source Mapping Manifest

Date: 2026-07-26 · Owner: founder · Source vault: `~/Downloads/SessionVue-OS` (read-only; not modified)
Canonical source of truth: `10 Company/Facts.md` (owner: founder; uses the NOT IN SOURCE convention)

| Input file | Source file | Source authority | Transformation performed | Unresolved gaps |
|---|---|---|---|---|
| company-brain/Company/Mission.md | `10 Company/Facts.md` §1 (→ `10 Company/Mission/README`) | Canonical, founder, **LOCKED** | Transcribed locked mission ("Content first, software second") verbatim; added Knowledge frontmatter + sections | none |
| company-brain/Company/Vision.md | Founder-approved canonical statement, 2026-07-25 | Canonical, founder | Transcribed founder-approved vision verbatim | none |
| company-brain/Company/Company Identity.md | `10 Company/Facts.md` §1–2 | Canonical, founder | Transcribed identity + positioning facts (founder, target, voice, promise pillars) | none |
| company-brain/Company/Business Model.md | `10 Company/Facts.md` §1,§3,§6,§8 | Canonical, founder, **LOCKED** | Transcribed model ("Independent-first…") + tier/launch summary | **Salon tier pricing NOT IN SOURCE** |
| company-brain/Company/Founder Directives.md | `10 Company/Facts.md` §7,§10 | Canonical, founder, **LOCKED** | Transcribed the 8 locked directives table | none |
| company-brain/Memberships/Membership Brain.md | `10 Company/Facts.md` §3 | Canonical, founder | Transcribed tier structure, tier language (approved/forbidden), pricing display | **Salon tier NOT IN SOURCE** |
| company-brain/Products/Product Brain.md | `10 Company/Facts.md` §3,§4,§5,§6 | Canonical, founder | Transcribed 14 canonical categories, platform, tier pointer | **Laser / Body sculpting / Dental specialty lists NOT IN SOURCE** |
| company-brain/Integrations/Integration Brain.md | `10 Company/Facts.md` §5,§8, Critical Gaps | Canonical, founder | Transcribed Supabase facts + Shelby partnership status | **Sending domain + external integrations beyond verified sources NOT IN SOURCE** |
| projects/README.md | none (no approved SVOS-format Project input) | — | Placeholder stub w/ frontmatter | **Entire projects input NOT IN SOURCE (checkpoint stub only)** |
| jobs/README.md | none (no approved global Job input) | — | Placeholder stub w/ frontmatter | **Entire global jobs input NOT IN SOURCE (checkpoint stub only)** |

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

## Scope note
`projects/README.md` and `jobs/README.md` are accepted **only** for this Executive-system compile checkpoint. They do **not** make the full SessionVue OS inputs complete.
