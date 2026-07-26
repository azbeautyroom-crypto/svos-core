# SVOS Specification

Version: 1.0.0
Status: LOCKED
Authority: Founder

---

# Purpose

The `spec` folder is the canonical architectural source for SVOS Core.

It defines:

* what SVOS is;
* how the operating system is structured;
* which Objects exist;
* how Objects relate;
* where authority lives;
* how Objects are named;
* how versions are managed;
* what the compiler is allowed to generate.

No generated Business System, Project, Job, Workflow, Automation, Registry, or output may redefine this folder.

---

# Specification Files

## `OS_SPECIFICATION.md`

Defines the purpose, layers, authority, compilation order, and end state of SVOS.

Answers:

> What is SVOS?

---

## `ARCHITECTURE.md`

Defines the permanent operating layers.

Answers:

> How is SVOS structurally organized?

---

## `OBJECT_MODEL.md`

Defines the canonical Object types, properties, ownership, lifecycle, and validation requirements.

Answers:

> What exists inside SVOS?

---

## `RELATIONSHIPS.md`

Defines how Objects interact and how knowledge, execution, outputs, metrics, and improvement move through the operating system.

Answers:

> How do SVOS Objects relate?

---

## `SOURCE_OF_TRUTH.md`

Defines authority, canonical ownership, conflict handling, missing information, assumptions, and duplication rules.

Answers:

> Where does truth live?

---

## `NAMING.md`

Defines canonical names, IDs, filenames, folder names, statuses, and renaming rules.

Answers:

> What is everything called?

---

## `VERSIONING.md`

Defines semantic versioning, compatibility, release states, metadata, migrations, deprecation, and rollback.

Answers:

> How does SVOS change safely?

---

# Specification Authority

Authority order:

1. Founder Decisions
2. SVOS Specification
3. Architecture Standards
4. Company Brain
5. Templates
6. Business Systems
7. Projects
8. Jobs
9. Generated Output

A lower authority may not redefine a higher authority.

---

# Editing Rules

Specification files are manually authored and locked.

AI may:

* read;
* analyze;
* identify conflicts;
* propose changes;
* prepare an Architecture Decision Record.

AI may not:

* silently edit;
* rename;
* remove;
* restructure;
* reinterpret;
* regenerate

a locked specification file without founder approval.

---

# Change Process

A specification change requires:

1. identify the exact problem;
2. identify affected files and Objects;
3. create an Architecture Decision Record;
4. describe available options;
5. document compatibility impact;
6. define migration requirements;
7. receive founder approval;
8. update specification version;
9. update tests;
10. regenerate affected outputs;
11. validate;
12. publish release notes.

---

# Build Dependency

Every compiler run must load the specification before:

* templates;
* Company Brain;
* Business System definitions;
* Project definitions;
* Job definitions;
* generated outputs.

Compilation order:

```text
Specification
→ Architecture Standards
→ Company Brain
→ Templates
→ Compiler Rules
→ Generation
→ Validation
→ Release
```

---

# Completion Criteria

The specification layer is complete when:

* all required files exist;
* terminology is consistent;
* Object ownership is unambiguous;
* authority order is explicit;
* naming is deterministic;
* versioning is deterministic;
* validation requirements are explicit;
* no unresolved architectural conflict remains.

---

# Current Specification Status

| File             | Status   |
| ---------------- | -------- |
| OS Specification | Complete |
| Architecture     | Complete |
| Object Model     | Complete |
| Relationships    | Complete |
| Source of Truth  | Complete |
| Naming           | Complete |
| Versioning       | Complete |

---

# Next Build Layer

After the `spec` folder is complete, proceed to:

```text
templates/
```

The first template to build is:

```text
templates/business-system/
```

Do not generate Executive, Operations, Marketing, Product, or Engineering until the template and validation layers are complete.
