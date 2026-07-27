# SVOS Package Status

Updated: 2026-07-26
Owner: Founder

| Package | Name | Status | Version | Notes |
|---|---|---|---|---|
| B1 | SVOS Core Specification | Complete | 1.0.0 | Committed and pushed |
| B2 | Template Library | Complete | 1.0.0 | Eight template packages committed and pushed |
| B3 | Compiler Engine | Active | 1.0.0 | **No longer skipped.** Adopted as the compiler architecture via ADR-001; generalized to a folder object model via ADR-002 |
| B4 | Validation and Release Management | Complete | 1.0.0 | Committed and pushed |
| I1 | Canonical SessionVue Inputs | In Progress | 1.0.0 | company-brain + two Projects authored and committed; global Jobs input `NOT IN SOURCE` |
| 2.1 | Executive System | Compiler-built (review) | 1.0.0 | BS-001; compiled via generic compiler; byte-identical golden test; directly-authored tree retired |
| 2.2 | Operations System | Compiler-built (review) | 1.0.0 | BS-002; compiled via generic compiler (ADR-002); golden test; committed |
| 2.3 | Marketing System | Canonical | 1.0.0 | BS-003; compiled via generic compiler; 19-folder anatomy; golden test (`003.sha`); committed and pushed |
| BS-004 | Analytics System | Deferred (valid boundary) | — | Founder decision 2026-07-26: valid constitutional ownership boundary; authoring deferred until canonical launch metrics + Engineering instrumentation exist |
| BS-005 | Product System | Next | — | Current priority — greater immediate launch leverage (founder decision 2026-07-26) |
| BS-006 | Engineering System | Not Started | — | Candidate |

# ADR-001 Record — Compiler Architecture Adopted (2026-07-26)

- **B3 is no longer skipped.** [ADR-001](adr/ADR-001-adopt-compiler-supersede-b3.md) **supersedes** the prior B3-skip decision (`DEC-EXE-001`).
- **The compiler architecture is active.** Business Systems are compiled, not hand-authored.
- **`inputs/sessionvue/` is canonical** — the single hand-authored source of truth.
- **`generated/sessionvue-os/` is reproducible, disposable output** — gitignored, never committed inside svos-core.
- **Generated files must not be edited manually** — correct the input/template/compiler and recompile.
- **The Executive compiler path is validated** — compile, generated-output validation, and smoke tests all pass; parity with the retired directly-authored tree is confirmed (see [ADR-001 parity report](adr/ADR-001-parity-report.md)).
- **Global Jobs input remains incomplete** — `inputs/sessionvue/jobs/` is a checkpoint stub marked `NOT IN SOURCE`. (Projects input is authored: two active projects.)

# ADR-002 Record — Generic Business-System Compiler (2026-07-26)

- **[ADR-002](adr/ADR-002-generic-business-system-compiler.md)** generalized the compiler to a single per-system **folder object model** (`id, index, title, role, purpose`); each Business System declares its own folder anatomy.
- **Executive (BS-001)** was migrated to declare its anatomy; output proven **byte-identical** (55/55).
- **Operations (BS-002)** was authored and compiled under this model with its own 20-folder anatomy; Executive parity re-verified.
- **Project Registry** is generated at `06 Registry/Project Registry.md`; external knowledge references are marked `referenced-external` (non-resolving by design).
- **Per-system anatomy retained** (Option A, founder-approved); no shared-shell standard adopted.
- **Regression tests** lock both systems' output via byte-identical golden baselines (`tests/goldens/`).

# ADR-003 Record — SVOS Constitution Adopted (2026-07-26) · SVOS Core v1 complete

- **[SVOS Constitution](SVOS_CONSTITUTION.md)** adopted by **[ADR-003](adr/ADR-003-adopt-svos-constitution.md)** as the highest governing document. Governing hierarchy: Founder → SVOS Constitution → Operating Doctrine → Specification Layer (LOCKED specs + Execution Contract) → Business Systems → Executable Objects → Execution → Operating State; ADRs are the amendment ledger.
- **Terminology reconciled** (no implementation change): Business Systems are ownership boundaries, not departments; SVOS is tenant-agnostic (SessionVue = first instance); CONTRACT-001 authority references resolve to the SVOS Constitution + Operating Doctrine.
- **SVOS Core v1 is complete.** No further architectural work begins automatically; **Marketing (BS-003)** is the next capability and begins only as a separate founder-approved architecture session.
