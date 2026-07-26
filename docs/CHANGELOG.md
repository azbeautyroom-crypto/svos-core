
## ADR-001 — Compiler Architecture Adopted (2026-07-26)

### Decisions

- **B3 is no longer skipped.** ADR-001 supersedes the prior B3-skip decision (`DEC-EXE-001`).
- **The compiler architecture is active** — Business Systems are compiled from canonical inputs, not directly authored.

### Changed

- **`inputs/sessionvue/` is canonical** — the single hand-authored source of truth (adds Package I1 — Canonical SessionVue Inputs; company-brain authored from `10 Company/Facts.md`).
- **`generated/sessionvue-os/` is reproducible, disposable output** — gitignored, never committed inside svos-core.
- **Generated files must not be edited manually** — correct the input/template/compiler and recompile.
- **The Executive compiler path is validated** — dry-run, full compile, generated-output validation, and smoke tests all pass; parity with the retired directly-authored tree confirmed (ADR-001 parity report).

### Removed / Retired

- Retired the directly-authored Executive tree (`generated/001 Executive System/`) and its installer (`scripts/install_package_2_1.py`); approved content migrated upstream into canonical inputs.
- Removed package-delivery scaffolding (BUILD_RESULT.md, MERGE_INSTRUCTIONS.md, PACKAGE_MANIFEST.json, scripts/cleanup_repo.py.md).

### Known gaps

- **Full Projects and global Jobs inputs remain incomplete** — `inputs/sessionvue/projects/` and `inputs/sessionvue/jobs/` are checkpoint stubs marked `NOT IN SOURCE`.

### Superseded records

- The "Decisions" and "Package 2.1 — Executive System" entries below predate ADR-001 and are retained for history; their B3-skip and directly-authored statements are superseded by this section.

## Unreleased

### Added

- B4 validation standards
- Acceptance test framework
- Release gates
- Release process
- Change-control process
- Architecture Decision Record template
- Package status tracking

### Decisions

- B3 — Compiler Engine was intentionally skipped by founder decision.
- Phase 2 Business Systems will be directly authored from locked templates and validated through B4 until B3 is revisited.

## Package 2.1 — Executive System

### Added

- Executive System Control Center
- Executive purpose and scope
- Executive policies and approval authority
- Eight Executive workflows
- Twelve executable Executive Jobs
- Six Executive templates
- Eight Executive metrics
- Six proposed automation contracts
- Executive integration and knowledge maps
- Executive Decision Registry
- Executive improvement records
- Package manifest
- Package validation report

### Status

- Package installed for review.
- Validation not yet run.
- Founder approval pending.
- B3 remains intentionally skipped.
