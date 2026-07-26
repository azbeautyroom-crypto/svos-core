# SVOS Package Status

Updated: 2026-07-26
Owner: Founder

| Package | Name | Status | Version | Notes |
|---|---|---|---|---|
| B1 | SVOS Core Specification | Complete | 1.0.0 | Committed and pushed |
| B2 | Template Library | Complete | 1.0.0 | Eight template packages committed and pushed |
| B3 | Compiler Engine | Active | 1.0.0 | **No longer skipped.** Adopted as the compiler architecture via ADR-001 |
| B4 | Validation and Release Management | Complete | 1.0.0 | Committed and pushed |
| I1 | Canonical SessionVue Inputs | In Progress | 1.0.0 | company-brain authored; Projects and global Jobs inputs incomplete |
| 2.1 | Executive System | Compiler-validated | 1.0.0 | Executive compiler path validated; directly-authored tree retired |
| 2.2 | Operations System | Not Started | — | Follows Executive |
| 2.3 | Marketing System | Not Started | — | Follows Operations |
| 2.4 | Product System | Not Started | — | Follows Marketing |
| 2.5 | Engineering System | Not Started | — | Follows Product |

# ADR-001 Record — Compiler Architecture Adopted (2026-07-26)

- **B3 is no longer skipped.** [ADR-001](adr/ADR-001-adopt-compiler-supersede-b3.md) **supersedes** the prior B3-skip decision (`DEC-EXE-001`).
- **The compiler architecture is active.** Business Systems are compiled, not hand-authored.
- **`inputs/sessionvue/` is canonical** — the single hand-authored source of truth.
- **`generated/sessionvue-os/` is reproducible, disposable output** — gitignored, never committed inside svos-core.
- **Generated files must not be edited manually** — correct the input/template/compiler and recompile.
- **The Executive compiler path is validated** — compile, generated-output validation, and smoke tests all pass; parity with the retired directly-authored tree is confirmed (see [ADR-001 parity report](adr/ADR-001-parity-report.md)).
- **Full Projects and global Jobs inputs remain incomplete** — `inputs/sessionvue/projects/` and `inputs/sessionvue/jobs/` are checkpoint stubs marked `NOT IN SOURCE`.
