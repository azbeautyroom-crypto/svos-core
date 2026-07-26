# ADR-001 — Adopt compiler-based architecture; supersede the B3 skip

Status: accepted
Date: 2026-07-26
Owner: founder
Decision Type: architecture
SVOS Version: 1.0.0
Affected Version: 2.0.0 (major — canonical build model changes)

# Context

B3 — Compiler Engine was previously **intentionally skipped** by founder decision (recorded as `DEC-EXE-001`). Under that decision, Phase 2 Business Systems were to be **directly authored** from locked templates and validated through B4. Package 2.1 — Executive System was built that way: 54 files under `generated/001 Executive System/`, validated to a full PASS (17/17 checks), awaiting founder approval.

A compiler package has since been introduced into `svos-core`: the **SVOS Execution Contract (CONTRACT-001)** plus a working compiler (`scripts/compile_sessionvue.py`). It reads hand-authored canonical input from `inputs/sessionvue/` and generates `generated/sessionvue-os/`. Its reported build result: 172 generated files, 0 missing required files, 0 missing frontmatter, compile validation PASS, 2 smoke tests PASS.

# Current State

- Two Executive Systems now exist in the repository:
  - `generated/001 Executive System/` — directly authored (Package 2.1), 14-folder taxonomy, validated PASS, uncommitted.
  - `generated/sessionvue-os/02 Business Systems/001 Executive System/` — compiled, 18-folder taxonomy, produced by the new compiler.
- `docs/PACKAGE_STATUS.md` and `docs/CHANGE_CONTROL.md` record B3 as intentionally skipped and state it must not be silently reintroduced.
- The Execution Contract (`contracts/EXECUTION_CONTRACT.md`) declares `generated/` output must never be edited manually; defects are fixed upstream (input, template, compiler rule, validation) and recompiled.

# Decision Required

Whether to adopt the compiler-based architecture as canonical and formally supersede the prior decision to skip B3.

# Evidence

- `BUILD_RESULT.md`: 172 files, compile validation PASS, 2 smoke tests PASS.
- `contracts/EXECUTION_CONTRACT.md` (CONTRACT-001): mandatory execution anatomy, generated-output rule, change control requiring an ADR.
- `compiler/COMPILER_CONTRACT.md`, `compiler/EXECUTION_CONTRACT_BINDING.md`: compile sequence and source order.
- `inputs/sessionvue/systems/executive.system.json`: single hand-authored source of the Executive System.
- Package 2.1 validation report: the directly-authored tree passed B4 validation but is a hand-authored artifact, not reproducible from a source input.

# Options

## Option 1 — Adopt the compiler (chosen)

Make `inputs/sessionvue/ → svos-core compile → generated/sessionvue-os/` the canonical model. Retire the directly-authored tree after content parity is confirmed.

## Option 2 — Keep directly-authored Package 2.1

Discard the compiler; continue hand-authoring generated Business Systems. Preserves B3 skip but leaves output non-reproducible and prone to structural drift.

## Option 3 — Hybrid

Maintain both. Rejected: guarantees drift and two competing sources of truth.

# Recommendation

Option 1 — adopt the compiler.

# Founder Decision

`ACCEPTED` — Adopt the compiler-based architecture. The prior decision to skip B3 (`DEC-EXE-001`) is superseded. (Founder ruling, 2026-07-26.)

# Rationale

- **Prevent structural drift** — one compiler enforces one anatomy across all Business Systems.
- **Preserve one source of truth** — hand-authored input in `inputs/sessionvue/` is canonical; everything else is derived.
- **Make Business Systems reproducible** — any system can be regenerated deterministically from input + templates + compiler.
- **Generated output must not be edited manually** — corrections happen upstream, then recompile.

# Consequences

- B3 is **un-skipped**. `DEC-EXE-001` is superseded (not deleted; retained with a superseded marker for history).
- `generated/sessionvue-os/` becomes the **canonical** generated SessionVue OS output.
- `generated/001 Executive System/` becomes **non-canonical**, marked for retirement, archived only after content parity is confirmed (per this ADR's migration plan). Not deleted yet.
- `docs/PACKAGE_STATUS.md`, `docs/CHANGELOG.md`, `docs/ROADMAP.md`, `docs/CHANGE_CONTROL.md` must be updated to reflect the adopted compiler and the superseded B3 exception.
- All future Business Systems are authored as input + compiled, never hand-edited under `generated/`.

# Affected Objects

- `DEC-EXE-001` (B3 skip) — superseded by this ADR.
- Package B3 row in `docs/PACKAGE_STATUS.md`.
- `generated/001 Executive System/` (entire directly-authored tree) — marked for retirement.
- `docs/CHANGE_CONTROL.md` "B3 Exception" section.

# Files to Update

- `docs/PACKAGE_STATUS.md` — B3 status; Package 2.1 status/source.
- `docs/CHANGELOG.md` — record ADR-001 and the architecture change.
- `docs/ROADMAP.md` — reflect compiler adoption.
- `docs/CHANGE_CONTROL.md` — supersede the B3 exception.
- Decision Registry (canonical, in the compiled tree once regenerated) — record the supersession.

# Tests to Update

- `tests/test_compile_smoke.py` — keep green; extend to cover any content migrated upstream.
- B4 validation / `scripts/validate_generated.py` — enforce contract validation on the compiled tree.

# Regeneration Required

- yes

# Version Impact

- major

# Migration Plan

1. Compare `generated/001 Executive System/` against `generated/sessionvue-os/02 Business Systems/001 Executive System/`.
2. Identify approved content present only in the directly-authored tree.
3. Move that content upstream into the appropriate input (`inputs/sessionvue/…`), template, or compiler source.
4. Recompile via `scripts/compile_sessionvue.py`.
5. Validate via `scripts/validate_generated.py` and `tests/test_compile_smoke.py`.
6. Confirm parity — no approved content lost.
7. Archive (do not delete) the directly-authored Executive tree.
8. Update the docs listed above.

# Rollback Plan

- All changes remain uncommitted until founder approval; the directly-authored tree is preserved (archived, not deleted) so it can be restored.
- Git history provides full rollback: revert the adoption commit to return to the pre-compiler state.

# Validation Required

- architecture
- naming
- links
- YAML
- ontology
- registries
- acceptance tests
- release gates
- execution-contract validation (CONTRACT-001)
