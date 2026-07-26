# SVOS Change Control

Version: 1.0.0
Status: LOCKED
Owner: Founder

# Change Classes

1. Architecture Change
2. Business System Change
3. Canonical Knowledge Change
4. Project Change
5. Patch

Architecture changes require an ADR, founder approval, compatibility analysis, migration, rollback, version review, and complete validation.

# B3 Exception — SUPERSEDED by ADR-001 (2026-07-26)

The prior B3 exception (B3 — Compiler Engine intentionally skipped; Business Systems directly authored from locked templates) is **superseded**. See [ADR-001](adr/ADR-001-adopt-compiler-supersede-b3.md).

- **B3 is no longer skipped.** ADR-001 supersedes the prior B3-skip decision (`DEC-EXE-001`).
- **The compiler architecture is active.** Business Systems are compiled from canonical inputs, not directly authored.
- **`inputs/sessionvue/` is canonical**; `generated/sessionvue-os/` is reproducible, disposable output that is gitignored and **must not be edited manually** — correct the input/template/compiler and recompile.
- The Executive compiler path is validated; parity with the retired directly-authored tree is confirmed.
- Full Projects and global Jobs inputs remain incomplete (checkpoint stubs marked `NOT IN SOURCE`).

Adopting the compiler was itself an Architecture Change and followed this document's requirements: ADR (ADR-001), founder approval, parity/compatibility analysis, migration of approved content upstream, rollback via git, and complete validation.
