
## Package Roadmap

- B1 — SVOS Core Specification: Complete
- B2 — Template Library: Complete
- B3 — Compiler Engine: **Active** — adopted as the compiler architecture via ADR-001 (no longer skipped)
- B4 — Validation and Release Management: Complete
- I1 — Canonical SessionVue Inputs: In Progress (company-brain + two Projects authored; global Jobs input incomplete)
- Package 2.1 — Executive System (BS-001): Compiler-built and committed
- Package 2.2 — Operations System (BS-002): Compiler-built and committed
- Package 2.3 — Marketing System: Next (not started; approved to build under ADR-002, Option A)
- Package 2.4 — Product System: Not started
- Package 2.5 — Engineering System: Not started

## Architecture (committed)

- **ADR-001** — compiler architecture adopted; supersedes the B3-skip decision.
- **ADR-002** — generic Business-System compiler driven by a single per-system folder object model (`id, index, title, role, purpose`); each system declares its own anatomy.
- `inputs/sessionvue/` is the canonical, hand-authored source of truth.
- `generated/sessionvue-os/` is reproducible, disposable output — gitignored, never committed; generated files must not be edited manually.
- Global registries are generated at `06 Registry/`: Business System, Project, Job, Metric, Automation.
- Knowledge sources either resolve inside the OS, or are marked `referenced-external` (non-resolving by design) or `NOT IN SOURCE`.
- Executive (BS-001) and Operations (BS-002) are compiled and validated; both outputs are locked by per-system byte-identical golden regression tests (`tests/goldens/`).
- The global Jobs input remains a checkpoint stub (`NOT IN SOURCE`); no cross-system Job exists yet, and Business Systems use only system-owned Jobs.
