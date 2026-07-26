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

# B3 Exception

B3 — Compiler Engine is intentionally skipped.

Until revisited, Business System packages may be directly authored from locked templates, but they must still pass B4 validation.

This exception does not permit architecture changes.
