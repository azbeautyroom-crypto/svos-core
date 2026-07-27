# SVOS Architecture (as committed)

This document describes the architecture as it exists in the repository today. It introduces
no new architecture; it records what has been approved and committed. Authoritative decisions
live in the ADRs under `docs/adr/`.

The highest governing document is the **[SVOS Constitution](SVOS_CONSTITUTION.md)** (adopted by
ADR-003). The governing hierarchy is: Founder → SVOS Constitution → Operating Doctrine →
Specification Layer (LOCKED specs + Execution Contract) → Business Systems → Executable Objects →
Execution → Operating State, with ADRs as the amendment ledger and the compiler enforcing the
Specification Layer.

## Compile pipeline

```text
inputs/sessionvue/  →  scripts/compile_sessionvue.py  →  generated/sessionvue-os/
   (canonical,              (the compiler)                 (reproducible,
    hand-authored)                                          disposable output)
```

- **`inputs/sessionvue/` is the single source of truth** (ADR-001). It contains:
  - `company-brain/` → copied to `04 Knowledge/`
  - `projects/` → copied to `03 Projects/`
  - `jobs/` → copied to `05 Jobs/` (currently a `NOT IN SOURCE` stub)
  - `systems/*.system.json` → compiled into Business Systems
  - `SOURCE_MAPPING.md` → provenance manifest (not copied to output)
- **`generated/sessionvue-os/` is disposable** (ADR-001): gitignored, never committed, and never edited
  manually. Defects are fixed in the input/compiler and recompiled.
- The compile contract is `compiler/contracts/sessionvue.compile.json`; the governing execution
  contract is `contracts/EXECUTION_CONTRACT.md` (`CONTRACT-001`).

## Business System model (ADR-002)

Each `*.system.json` declares its own anatomy through a single **folder object model**. Each folder:

```json
{ "id": "02 Intake", "index": 2, "title": "Intake", "role": "component", "purpose": "…" }
```

The compiler derives folder creation, artifact placement, the Control Center System Map, and all
system wording (from a `label`) from this one array. Roles: `control_center, charter, component,
decision_management, founder_approval, metrics, jobs, automations, knowledge, decisions,
improvements, archive`.

- **Per-system anatomy** (Option A, founder-approved): systems are not required to share a common
  folder shell. Executive (BS-001) uses an 18-folder anatomy; Operations (BS-002) uses a 20-folder
  anatomy. `00 Control Center` and `01 Charter` are invariant by role and index; the remaining
  roles are invariant by role but may sit at system-specific indices.
- **Jobs are per-system**: each system's `jobs` array is generated into that system's `jobs` role
  folder. There is no cross-system/global Job mechanism today.
- **Charter wording** is overridable per system via `operating_boundary` / `success_condition`
  (defaults reproduce Executive; Operations overrides them).
- **Decision registry fallback**: a system without a `decision_management` folder folds its Decision
  Registry into its `decisions` folder.

## Global registries

Generated at `06 Registry/`: **Business System**, **Project**, **Job**, **Metric**, **Automation**.
Project entries use deterministic `PRJ-NNN` IDs with title/status/owner read from each project's
frontmatter (no facts inferred).

## Knowledge sources

Each system's `knowledge_sources` entry either resolves inside the generated OS (`present`), is
`referenced-external` (canonical where it lives — e.g. `contracts/EXECUTION_CONTRACT.md`,
`HQ/Active Priorities.md` — and non-resolving inside the OS by design), or is `NOT IN SOURCE`.

## Validation and tests

- `scripts/validate_generated.py` reads the compile's `BUILD METADATA.json` and reports pass/fail.
- The compiler's `validate_output` is generic: it discovers every system under `02 Business Systems`
  and requires each system's Control Center + Charter plus the global Business System Registry, and
  that every generated `.md` carries frontmatter (except README/registry files).
- `tests/test_compile_smoke.py` covers all compiled systems: anatomy match, jobs/metrics/automations
  placement, registry inclusion, knowledge-source resolution, a negative validation test, and a
  per-system **byte-identical golden regression** (`tests/goldens/`, dates normalized).

## Committed Business Systems

| System | ID | Anatomy | State |
|---|---|---|---|
| Executive System | BS-001 | 18 folders | Compiled, validated, golden-locked; status `review` |
| Operations System | BS-002 | 20 folders | Compiled, validated, golden-locked; status `review` |
