# ADR-001 Parity Report — Directly-Authored vs Compiled Executive System

Date: 2026-07-26
Owner: founder
Related: [ADR-001](ADR-001-adopt-compiler-supersede-b3.md)

Compares:
- **OLD** (non-canonical, directly authored): `generated/001 Executive System/` — 54 files, restored from `scripts/install_package_2_1.py`.
- **NEW** (canonical, compiled): `generated/sessionvue-os/02 Business Systems/001 Executive System/` — 66 files, compiled from `inputs/sessionvue/systems/executive.system.json`.

> **Approval status note:** No content in the OLD tree was ever founder-approved. Its objects were `status: review` / `proposed`, awaiting the founder approval that was never given (we pivoted to the compiler first). So, by the letter of the directive, there is **no approved-only content** to migrate. What follows lists *substantive validated* content as migration candidates for a founder decision.

## Category-level parity

| Concept | OLD | NEW (compiled) | Assessment |
|---|---|---|---|
| Purpose | `01 Purpose/` | `input.purpose` + `01 Charter/PURPOSE` | ✅ covered |
| Scope / out-of-scope | `02 Scope/` | `input.out_of_scope` (5) + `Charter/NON RESPONSIBILITIES` | ✅ covered |
| Authority / policies | `03 Policies/` (2) | `input.authority` (5) + `01 Charter` + `05 Founder Approval` | ✅ covered |
| Control Center | 1 file | 13 dashboard files | ✅ richer in NEW |
| Integrations | `Integration Map` | `input.connected_systems` (9) + `07 Cross-System Governance` | ✅ covered |
| Knowledge | `Knowledge Map` | `input.knowledge_sources` (8) + `14 Knowledge/KNOWLEDGE MAP` | ✅ covered |
| Improvements | 2 files | `16 Improvements/` | ✅ covered |
| Archive | README | `17 Archive/README` | ✅ covered |
| Decisions | `DEC-EXE-003` + registry | `04 Decision Management` + `15 Decisions` | ⚠️ old decisions obsolete/superseded |
| **Workflows** | **8 WF-EXE objects** | **none** (no workflow slot in compiler) | ⛔ structural gap |
| **Templates** | **6 templates** | **none** (no template slot in compiler) | ⛔ structural gap |
| **Jobs** | 12 | 10 | ⚠️ 5 old concepts absent |
| **Metrics** | 8 | 6 | ⚠️ 5 old concepts absent |
| **Automations** | 6 | 5 | ⚠️ 4 old concepts absent |

## Migration candidates (substantive concepts present only in OLD)

### Jobs — 5 candidates
- Review Strategic Initiative
- Record Founder Decision
- Resolve Cross-System Conflict
- Prepare Quarterly Plan
- Propagate Executive Decision

### Metrics — 5 candidates
- Decision Propagation Completeness
- Project Approval Turnaround
- Company Health Review Completion
- Risk Review Completion
- Mission Alignment Pass Rate

### Automations — 4 candidates
- Approval Aging Alert (NEW has "Founder Approval Queue Digest" — related but a digest, not an aging alert)
- Cross-System Blocker Alert
- Decision Propagation Check
- Quarterly Planning Prompt

### Workflows — 8, structural gap
The compiler input schema has **no `workflows` array** and the compiler emits no workflow objects. The 8 OLD workflows (Strategic Initiative Intake, Company Priority Review, Founder Decision Flow, Weekly Executive Review, Quarterly Planning, Cross-System Conflict Resolution, Risk Review, Package Approval) map conceptually onto NEW governance folders (`02 Strategic Planning`, `04 Decision Management`, `05 Founder Approval`, `07 Cross-System Governance`, `08 Risk Management`, `09 Executive Reviews`) and onto Jobs. Preserving them as discrete Workflow objects would require **extending the compiler + input schema**.

### Templates — 6, structural gap
OLD per-system templates (Executive Decision Brief, Weekly Executive Review, Quarterly Plan, Company Health Review, Risk Assessment, Project Approval). No template slot in the compiler input. Under the compiler model these would become either repo-level `/templates`, Knowledge objects, or Job outputs — a design decision.

## Explicitly NOT migrated (obsolete / superseded)
- `JOB-EXE-001 Review Executive System Package` — meta job about the retired package.
- `WF-EXE-008 Package Approval` — about approving the retired package.
- `DEC-EXE-001 B3 skip` — **superseded by ADR-001**.
- `DEC-EXE-002 Build one Business System at a time` — historical.
- `DEC-EXE-003 Executive System Package Approval` — about the retired package.

## Recommendation
1. **Migrate the trivially-addable set** (schema already supports name-lists): the 5 jobs, 5 metrics, 4 automations above → append to `executive.system.json` arrays → recompile. Low risk, no schema change.
2. **Workflows & templates**: decide deliberately — (a) extend the compiler to support `workflows`/`templates`, (b) accept the governance-folder mapping and drop discrete workflow/template objects, or (c) relocate templates to repo-level `/templates`.
3. Obsolete/superseded items: do not migrate; record the supersession via ADR-001 and the compiled Decision Registry.

No canonical input has been edited yet. Migration awaits founder confirmation of the set.
