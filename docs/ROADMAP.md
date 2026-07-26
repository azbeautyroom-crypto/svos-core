
## Package Roadmap

- B1 — SVOS Core Specification: Complete
- B2 — Template Library: Complete
- B3 — Compiler Engine: **Active** — adopted as the compiler architecture via ADR-001 (no longer skipped)
- B4 — Validation and Release Management: Complete
- I1 — Canonical SessionVue Inputs: In Progress (company-brain authored; Projects and global Jobs inputs incomplete)
- Package 2.1 — Executive System: Compiler-validated (directly-authored tree retired)
- Package 2.2 — Operations System: Next

## Architecture (ADR-001, 2026-07-26)

- ADR-001 supersedes the prior B3-skip decision; the compiler architecture is active.
- `inputs/sessionvue/` is the canonical, hand-authored source of truth.
- `generated/sessionvue-os/` is reproducible, disposable output — gitignored, never committed; generated files must not be edited manually.
- The Executive compiler path is validated (compile + generated-output validation + smoke tests pass; parity confirmed).
- Full Projects and global Jobs inputs remain incomplete (checkpoint stubs marked `NOT IN SOURCE`).
