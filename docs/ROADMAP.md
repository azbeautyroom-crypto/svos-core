
## Package Roadmap

- B1 — SVOS Core Specification: Complete
- B2 — Template Library: Complete
- B3 — Compiler Engine: **Active** — adopted as the compiler architecture via ADR-001 (no longer skipped)
- B4 — Validation and Release Management: Complete
- I1 — Canonical SessionVue Inputs: In Progress (company-brain + two Projects authored; global Jobs input incomplete)
- Package 2.1 — Executive System (BS-001): Compiler-built and committed
- Package 2.2 — Operations System (BS-002): Compiler-built and committed
- Package 2.3 — Marketing System (BS-003): **Canonical** — compiler-built and committed
- BS-004 — Analytics System: **Valid ownership boundary; authoring DEFERRED** (founder decision 2026-07-26). Gate: deferred until canonical launch metrics and Engineering instrumentation exist.
- **Next capability: Product** (BS-005) — greater immediate launch leverage (founder decision 2026-07-26).
- BS-006 — Engineering System: Candidate

## Founder Decision — 2026-07-26 (operational; no governing change)

- **BS-004 Analytics is a valid constitutional ownership boundary** (canonical owner of company measurement; evidence: OSP ownership map "Metrics → Analytics", Marketing's canonical dependency, all metrics `NOT IN SOURCE`).
- **Authoring is deferred** until canonical launch metrics **and** Engineering instrumentation exist — until then Analytics would define measurement over `NOT IN SOURCE` placeholders.
- **Priority shifts to Product (BS-005)** for greater immediate launch leverage, per the launch-first mission.

## Architecture (committed)

- **SVOS Constitution** ([`docs/SVOS_CONSTITUTION.md`](SVOS_CONSTITUTION.md)) — highest governing document; adopted by **ADR-003**. Marks completion of **SVOS Core v1**. Governing hierarchy: Founder → SVOS Constitution → Operating Doctrine → Specification Layer → Business Systems → Executable Objects → Execution → Operating State.
- **ADR-001** — compiler architecture adopted; supersedes the B3-skip decision.
- **ADR-002** — generic Business-System compiler driven by a single per-system folder object model (`id, index, title, role, purpose`); each system declares its own anatomy.
- `inputs/sessionvue/` is the canonical, hand-authored source of truth.
- `generated/sessionvue-os/` is reproducible, disposable output — gitignored, never committed; generated files must not be edited manually.
- Global registries are generated at `06 Registry/`: Business System, Project, Job, Metric, Automation.
- Knowledge sources either resolve inside the OS, or are marked `referenced-external` (non-resolving by design) or `NOT IN SOURCE`.
- Executive (BS-001) and Operations (BS-002) are compiled and validated; both outputs are locked by per-system byte-identical golden regression tests (`tests/goldens/`).
- The global Jobs input remains a checkpoint stub (`NOT IN SOURCE`); no cross-system Job exists yet, and Business Systems use only system-owned Jobs.
