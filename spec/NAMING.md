# SVOS Naming Standard

Version: 1.0.0
Status: LOCKED

---

# Purpose

Create predictable names so humans, AI agents, scripts, registries, and generated files identify the same Object consistently.

---

# Core Rules

1. Every Object has one canonical name.
2. Names describe function, not personality.
3. Names remain stable after activation.
4. Abbreviations are prohibited unless defined here.
5. Renaming requires dependency review.
6. Generated names must follow this standard exactly.

---

# Repository Name

Canonical repository:

`svos-core`

Generated SessionVue operating-system repository:

`sessionvue-os`

Application repository:

`sessionvue-platform`

---

# Business Systems

Format:

`NNN System Name`

Examples:

* `001 Executive System`
* `002 Operations System`
* `003 Marketing System`
* `004 Product System`
* `005 Engineering System`

Business System IDs:

`BS-NNN`

Examples:

* `BS-001`
* `BS-002`

---

# Projects

Folder format:

`PRJ-NNN — Project Name`

Examples:

* `PRJ-001 — SessionVue Pre-Launch`
* `PRJ-002 — Professional Waitlist Conversion`

Project ID:

`PRJ-NNN`

Project names describe the outcome or initiative.

Avoid vague names such as:

* Marketing Work
* Miscellaneous
* Updates
* New Project

---

# Jobs

Format:

`JOB-NNN — Verb Object`

Examples:

* `JOB-001 — Route Project Request`
* `JOB-002 — Load Company Context`
* `JOB-003 — Validate Tier Language`
* `JOB-004 — Load Business Foundation`

Job names must begin with an action verb.

---

# Workflows

Format:

`WF-NNN — Workflow Name`

Examples:

* `WF-001 — Strategic Priority Review`
* `WF-002 — Content Approval`

---

# Automations

Format:

`AUTO-NNN — Automation Name`

Examples:

* `AUTO-001 — Daily Brief`
* `AUTO-002 — Content Queue Push`

---

# Decisions

Format:

`DEC-NNN — Decision Title`

Examples:

* `DEC-001 — Establish Growth as Target Tier`
* `DEC-002 — Use Sage for Marketing CTAs`

---

# Metrics

Format:

`MET-NNN — Metric Name`

Examples:

* `MET-001 — Professional Waitlist Conversion Rate`
* `MET-002 — Activation Rate`

---

# Integrations

Use the official product or service name.

Examples:

* Supabase
* Airtable
* GitHub
* Claude
* Cursor
* Obsidian
* PostHog
* Sentry
* Google Workspace

Do not invent alternate integration names.

---

# Knowledge Objects

Use a clear canonical noun phrase.

Examples:

* Company Identity
* Mission
* Vision
* Membership Matrix
* Tier Language Policy
* Product Brain
* Product Implementation Audit
* Brand Tokens

Avoid dates in canonical Knowledge titles unless the Knowledge is inherently time-bound.

---

# Files

Use Title Case for Markdown filenames.

Examples:

* `Control Center.md`
* `Source Map.md`
* `Decision Rules.md`
* `Improvement Loop.md`

Special root files may use uppercase names when defined by a template:

* `CLAUDE.md`
* `README.md`
* `PROJECT.md`
* `JOB.md`

---

# Folder Names

Use numbered folders only where order matters.

Business System anatomy:

```text
00 Control Center
01 Purpose
02 Scope
03 Policies
04 Workflows
05 Jobs
06 Templates
07 Metrics
08 Automations
09 Integrations
10 Knowledge
11 Decisions
12 Improvements
13 Archive
```

Do not create alternative folder names for the same function.

---

# Customer and Membership Names

Use these exact names:

* Beauty Client
* Visitor
* Student
* Launch Pro
* Growth Pro
* Power Pro
* Salon Owner
* Brand Partner
* Educator
* Agency
* Vendor

---

# Prohibited Membership Names

Never use:

* Legacy
* Legacy Pro
* Legacy Membership
* Starter
* Basic
* Beginner Tier

---

# Status Names

Document statuses:

* draft
* review
* verified
* archived

Lifecycle statuses:

* proposed
* designed
* approved
* active
* maintained
* paused
* retired
* archived

Approval statuses:

* not-required
* draft
* submitted
* under-review
* changes-requested
* approved
* rejected
* expired
* released

Do not invent new status words without an Architecture Decision Record.

---

# Renaming Rules

Before renaming an Object:

1. Check the registry.
2. Identify inbound links.
3. Identify generated references.
4. Identify scripts and templates using the name.
5. Create a Decision Record.
6. Update the canonical source.
7. Regenerate affected outputs.
8. Validate all links.

Do not rename an active Object silently.

---

# Validation Rules

Compilation fails when:

* an ID is duplicated;
* a name violates its Object format;
* two names refer to one Object;
* one name refers to multiple Objects;
* a prohibited tier term appears;
* an undefined status is used;
* a generated folder deviates from the naming standard.
