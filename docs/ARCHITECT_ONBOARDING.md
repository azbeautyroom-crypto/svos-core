# SVOS Architect Onboarding Guide

Status: reference (non-governing)
Authority: none — this guide introduces no authority and governs nothing.

> This is a **map, not law**. It helps a new architect navigate the existing governing hierarchy.
> It creates no new philosophy and restates no governing document; where a rule matters, it
> **points to** the authoritative file. If this guide ever disagrees with a governing document,
> the governing document wins. Every claim is labeled **[FACT]** (implemented and committed),
> **[RECOMMENDATION]** (proposed, not approved), or **[FOUNDER DECISION]** (recorded in an ADR or
> founder directive) — per the discipline the ADRs already follow.

## 1. Purpose of the guide
Help a brand-new architect **think correctly within SVOS** — find the governing documents, read them
in the right order, follow the decision and repository workflows, and tell canonical truth from
recommendation — **without creating any new architectural authority.**

## 2. Intended audience
An architect (human or AI) joining SVOS who will propose or implement changes. It assumes no prior
SVOS knowledge and no authority beyond what the founder grants (see the Constitution, Article II).

## 3. Required reading order
Read top-down; each layer governs the ones below it.
1. **`docs/SVOS_CONSTITUTION.md`** — the 12 Articles. Read first; it is the lens for everything.
2. **`inputs/sessionvue/company-brain/Company/Operating System Protocol.md`** — the Operating Doctrine (how the company and its agents operate).
3. **`contracts/EXECUTION_CONTRACT.md`** (`CONTRACT-001`) — the mandatory execution anatomy for governed objects.
4. **`spec/`** — the Specification Layer: `OS_SPECIFICATION.md`, `ARCHITECTURE.md`, `OBJECT_MODEL.md`, `NAMING.md`, `RELATIONSHIPS.md`, `VERSIONING.md`, `SOURCE_OF_TRUTH.md`.
5. **ADRs, in order:** `docs/adr/ADR-001` (compiler adopted) → `ADR-002` (folder object model) → `ADR-003` (Constitution adopted) → `ADR-004` (Executable Object Definition Model). ADRs are the amendment ledger — read them to understand *why* things are the way they are.
6. **Current state:** `docs/ARCHITECTURE.md`, `docs/PACKAGE_STATUS.md`, `docs/ROADMAP.md`.
7. **A live example:** one system input (`inputs/sessionvue/systems/operations.system.json`) and its `docs/adr/ADR-001-parity-report.md`-style provenance (`inputs/sessionvue/SOURCE_MAPPING.md`).

## 4. Governing hierarchy diagram
**[FACT]** Recorded in `docs/SVOS_CONSTITUTION.md` (Art. III) and `docs/adr/ADR-003`:
```
Founder                         (sole source of authority; may delegate — Art. II/IV)
  ↓
SVOS Constitution               docs/SVOS_CONSTITUTION.md      (WHY)
  ↓
Operating Doctrine              company-brain/…/Operating System Protocol.md   (HOW)
  ↓
Specification Layer             spec/*  +  contracts/EXECUTION_CONTRACT.md      (WHAT; compiler-enforced)
  ↓
Business Systems                inputs/sessionvue/systems/*.system.json         (canonical owners)
  ↓
Executable Objects              Jobs / Metrics / Automations (ADR-004 EODM)
  ↓
Execution                       inside or outside SVOS (Art. IX)
  ↓
Operating State                 generated/sessionvue-os/  (reproducible, disposable — Art. VI)

ADRs (docs/adr/) = the amendment ledger across every layer, not a rank.
The compiler (scripts/compile_sessionvue.py) mechanically enforces the Specification Layer.
```

## 5. Core architectural principles (by reference)
Do not memorize restatements — read the source. Each principle lives in one Article of
`docs/SVOS_CONSTITUTION.md`:
- Tenant-agnostic; SessionVue is the first instance → Art. I
- Authority originates with the Founder; delegation is bounded/recorded → Art. II
- Governing hierarchy; one Constitution, one Doctrine → Art. III
- Change only by founder-approved ADR; history preserved → Art. IV
- Canonical input is truth; absent = `NOT IN SOURCE`, never inferred → Art. V
- Generated output is reproducible, disposable operating state → Art. VI
- One owner, one source of truth, no duplication → Art. VII
- Business System = canonical owner of a bounded domain (not a department) → Art. VIII
- Execution may be inside or outside SVOS; validated result returns → Art. IX
- Improvement is deliberate and recorded → Art. X
- The Governance Test (every change improves Governance/Knowledge/Ownership/Execution/Improvement + mission) → Art. XI
- The AI workforce never expands its own authority → Art. XII

Execution-object structure lives in `contracts/EXECUTION_CONTRACT.md`; object types/ownership in
`spec/OBJECT_MODEL.md`; the compiler-as-mechanism in `compiler/COMPILER_CONTRACT.md`.

## 6. Standard architectural decision process
**[FACT]** The pattern every recent change followed (see any ADR + `docs/CHANGE_CONTROL.md`, `docs/ADR_TEMPLATE.md`):
1. **Assess against the Constitution** and the Governance Test (Art. XI). If it improves none, challenge it.
2. **Design read-only**, repository as sole source of truth; classify each element FACT / RECOMMENDATION / FOUNDER DECISION.
3. **Adversarially review** — try to disprove it; recommend the smallest viable change; prevent scope creep (see how ADR-004 deferred Operating State to a future ADR).
4. **Author an ADR** (`docs/adr/ADR-00N-…`) with explicit non-goals; **founder approves** (nothing is authority until the founder decides).
5. **Implement in gated milestones**, each preserving a working repository and **byte-identical golden parity** for unchanged systems.
6. **Stop for founder approval before commit/push.**

## 7. Repository workflow
**[FACT]**
- Author only **canonical input** under `inputs/sessionvue/` (systems, `company-brain/`, projects, jobs, `SOURCE_MAPPING.md`).
- Compile with `scripts/compile_sessionvue.py` → `generated/sessionvue-os/` (**git-ignored, disposable — never edit or commit it**).
- Validate with `scripts/validate_generated.py`; run `tests/test_compile_smoke.py` (includes **golden regression** in `tests/goldens/`).
- A system changes output only when its input changes; its golden is re-emitted **only** on a founder-approved change.
- Executable objects may be a name **or** a definition object (ADR-004 / EODM), backward-compatible.
- Commit and push only when the founder directs; keep changes scoped; verify `origin/main` sync.

## 8. How to distinguish canonical truth from recommendation
- **[FACT]** = present and committed in the repository. Verify by reading the file, not memory.
- **[RECOMMENDATION]** = proposed in a design/review session; carries no authority until approved.
- **[FOUNDER DECISION]** = recorded in an ADR (`Status: accepted`, `Founder Decision: ACCEPTED`) or a founder directive.
- A fact absent from canonical source is **`NOT IN SOURCE`** — never inferred (Art. V). Provenance for authored inputs lives in `inputs/sessionvue/SOURCE_MAPPING.md`. External-but-canonical references are marked `referenced-external`.

## 9. Common anti-patterns (avoid)
- **[FACT]** Editing `generated/sessionvue-os/` — it is disposable output (Art. VI). Fix the input and recompile.
- Duplicating canonical truth into a system — reference it (Art. VII). Definitions **reference** Company Brain, never copy it.
- Putting a procedure into Knowledge — forbidden (`contracts/EXECUTION_CONTRACT.md`: "Knowledge must never silently contain a procedure that should be a Job").
- Inventing a missing fact — use `NOT IN SOURCE` (Art. V).
- Creating a Business System by org-chart analogy — a system exists only for a bounded ownership need (Art. VIII).
- Bundling scope — defer what isn't needed yet (ADR-004 deferred Operating State/Evidence to ADR-005).
- Changing a golden baseline without a founder-approved input change (breaks the regression guarantee).
- An agent expanding its own authority — prohibited (Art. XII).

## 10. Expectations for an SVOS architect
- Reference, don't restate; evidence-only; repository is the sole source of truth.
- Challenge before adopting; recommend the **smallest** viable change; state non-goals.
- Preserve byte-identical parity for unchanged systems; keep the compiler deterministic.
- Label everything FACT / RECOMMENDATION / FOUNDER DECISION; never blur them (Art. IV governance discipline).
- Build on genuine need; stop for founder approval before committing.
- Leave SVOS governed, documented, and reproducible (Art. XII).

## 11. Reference map to the governing documents
| Layer | Document | Role |
|---|---|---|
| Constitution | `docs/SVOS_CONSTITUTION.md` | Highest governing philosophy (12 Articles) |
| Operating Doctrine | `inputs/sessionvue/company-brain/Company/Operating System Protocol.md` | How the company and agents operate |
| Execution Contract | `contracts/EXECUTION_CONTRACT.md` (`CONTRACT-001`) | Mandatory execution anatomy for governed objects |
| Specification | `spec/OS_SPECIFICATION.md`, `spec/ARCHITECTURE.md`, `spec/OBJECT_MODEL.md`, `spec/NAMING.md`, `spec/RELATIONSHIPS.md`, `spec/VERSIONING.md`, `spec/SOURCE_OF_TRUTH.md` | Structure: layers, objects, naming, versioning, source-of-truth |
| Decisions (ledger) | `docs/adr/ADR-001…ADR-004` (+ `ADR-001-parity-report.md`) | Why the architecture is as it is; the amendment ledger |
| Change control | `docs/CHANGE_CONTROL.md`, `docs/ADR_TEMPLATE.md`, `docs/RELEASE_PROCESS.md` | How governing documents change |
| Compiler | `compiler/COMPILER_CONTRACT.md`, `compiler/EXECUTION_CONTRACT_BINDING.md`, `compiler/contracts/sessionvue.compile.json`, `scripts/compile_sessionvue.py` | The deterministic mechanism |
| Validation & tests | `validation/*`, `scripts/validate_generated.py`, `tests/test_compile_smoke.py`, `tests/goldens/` | Enforcement + regression |
| Company Brain | `inputs/sessionvue/company-brain/` | Canonical company truth (referenced, not copied) |
| Business Systems | `inputs/sessionvue/systems/*.system.json` | Canonical owners (Executive BS-001, Operations BS-002, Marketing BS-003) |
| Provenance | `inputs/sessionvue/SOURCE_MAPPING.md` | Where authored inputs came from |
| Current state | `docs/ARCHITECTURE.md`, `docs/PACKAGE_STATUS.md`, `docs/ROADMAP.md` | What exists today |
