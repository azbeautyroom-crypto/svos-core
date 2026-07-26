# SVOS Validation Engine

Version: 1.0.0
Status: LOCKED
Owner: SVOS Core

---

# Purpose

The Validation Engine guarantees structural integrity across the SessionVue Operating System.

No Business System, Project, Job, Workflow, Automation, Registry, or generated output may be released without passing validation.

Validation protects architecture, canonical knowledge, relationships, naming, versioning, YAML, registries, object ownership, and generated output.

# Validation Philosophy

SVOS is deterministic. Validation never guesses.

Every required check returns PASS, FAIL, or NOT APPLICABLE. NOT APPLICABLE requires a written reason.

# Validation Order

```text
Architecture
→ Required Folders
→ Required Files
→ YAML
→ Naming
→ Objects
→ Relationships
→ Registries
→ Knowledge
→ Business Systems
→ Projects
→ Jobs
→ Automations
→ Generated Output
→ Acceptance Tests
→ Release Gates
```

# Package Rule

Every package must pass validation before it may be described as complete, committed as complete, pushed as a release candidate, tagged, installed, or merged into the released SessionVue OS.

# B3 Status

B3 — Compiler Engine was intentionally skipped by founder decision.

B4 validates directly authored packages created from the locked specification and templates.
