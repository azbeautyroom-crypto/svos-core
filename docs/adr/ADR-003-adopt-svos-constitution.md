# ADR-003 — Adopt the SVOS Constitution

Status: accepted
Date: 2026-07-26
Owner: founder
Decision Type: architecture / governance
Related: ADR-001 (compiler adoption), ADR-002 (folder object model), CONTRACT-001
Marks: completion of SVOS Core v1

# Architectural evolution (summary)

1. **B1** established the SVOS Core specification (object model, layers, naming, versioning).
2. **ADR-001** adopted the compiler architecture: canonical inputs → compile → disposable generated output; superseded the B3-skip.
3. **ADR-002** generalized the compiler to a per-system folder object model; Executive (BS-001) and Operations (BS-002) were built and proven byte-identical / golden-locked.
4. A founder **North Star** directive, then two adversarial review passes, produced a governing philosophy that reconciles the repository's several partial/absent governing tiers into one.

# Why the Constitution is introduced

- The repository had **competing or absent** governing tiers: CONTRACT-001 deferred to an "Architecture Constitution" and an "AI Operating Manual" that did not exist; the LOCKED spec called Business Systems "departments" while the built systems behave as ownership boundaries; and no document was authoritative over the whole Operating System.
- The **SVOS Constitution** establishes the single, tenant-agnostic governing philosophy from which every lower layer derives. It defines immutable principles, not mechanics, and is intended to hold regardless of implementation, headcount, humans-vs-AI, or the number of companies operated on SVOS.
- The Constitution is adopted here and lives permanently at `docs/SVOS_CONSTITUTION.md`.

# Superseded terminology

- **"Business System = permanent operating department"** → Business System = **canonical owner of a bounded domain of responsibility** (ownership boundary). The pre-enumerated 12-department roster becomes **non-binding examples**.
- **"Architecture Constitution" / "root AI Operating Manual"** (referenced by CONTRACT-001) → resolve to **SVOS Constitution** and **Operating Doctrine**.
- **"SVOS runs the company"** (singular) → **tenant-agnostic**: SVOS runs an operating *instance*; SessionVue is the first instance.
- The spec clause **"Nothing below this specification may redefine architecture"** is reconciled: the **SVOS Constitution ranks above the specification**.

# Constitutional authority hierarchy (recorded)

```
Founder
  ↓
SVOS Constitution        (WHY — immutable principles)
  ↓
Operating Doctrine       (HOW — company & agent operating standard)
  ↓
Specification Layer      (WHAT — LOCKED specifications + Execution Contract; enforced by the compiler)
  ↓
Business Systems         (canonical owners of bounded domains)
  ↓
Executable Objects
  ↓
Execution
  ↓
Operating State          (reproducible; updated only by validated evidence)
```

- **Authority originates with the Founder**; documents and ADRs record authority, they do not create it. Delegation is intentional, bounded, revocable, and recorded.
- **ADRs are the amendment ledger** across the hierarchy, not a ranked layer.
- **The compiler** enforces the Specification Layer and preserves determinism; it does not define philosophy.

# Scheduled terminology reconciliation (implemented in this change; terminology only)

| Document | Change |
|---|---|
| `spec/OS_SPECIFICATION.md` | "permanent operating departments" → ownership-boundary framing; roster → examples; tenant-agnostic phrasing; reconcile the "nothing below" clause under the Constitution |
| `spec/OBJECT_MODEL.md` | "Permanent operating department." → ownership-boundary definition |
| `spec/ARCHITECTURE.md` | "permanent operating departments" → ownership boundaries |
| `contracts/EXECUTION_CONTRACT.md` | authority references → SVOS Constitution + Operating Doctrine |
| `docs/ARCHITECTURE.md`, `docs/ROADMAP.md`, `docs/PACKAGE_STATUS.md` | reference the SVOS Constitution as the highest governing tier |

# Not in scope (unchanged)

No new architecture is introduced. No change to compiler logic, canonical inputs (`inputs/sessionvue/`, incl. the Operating System Protocol), Business Systems, generated output, or tests. Executive and Operations already conform to the Constitution.

# Validation Required

- Reconciliation is terminology-only; generated output must remain **byte-identical** (golden regression), and validation + smoke must pass unchanged.

# Rollback

Governance/terminology only. Revert this change to restore prior wording; no generated-output or behavioral effect.

# Founder Decision

`ACCEPTED` — SVOS Core v1 complete. No further architectural work begins automatically; Marketing (BS-003) is the next capability and must begin as a separate founder-approved architecture session.
