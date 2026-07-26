# SVOS Versioning Standard

Version: 1.0.0
Status: LOCKED

---

# Purpose

Define how SVOS Core, generated Business Systems, templates, Projects, Jobs, and releases are versioned.

Versioning makes every generated Object traceable to the exact architecture, specification, and template set that produced it.

---

# Version Format

SVOS uses Semantic Versioning:

`MAJOR.MINOR.PATCH`

Example:

`1.0.0`

---

# Major Version

Increase the MAJOR version when an approved change alters the operating architecture.

Examples:

* changing the root folder structure;
* changing the Business System anatomy;
* changing the Object Model;
* changing required YAML fields;
* changing registry structure;
* changing ownership rules;
* changing source-of-truth priority;
* removing or renaming a core Object type.

Example:

`1.0.0 → 2.0.0`

Major changes require:

* Architecture Decision Record;
* founder approval;
* impact assessment;
* migration plan;
* regeneration plan;
* rollback plan;
* full validation.

---

# Minor Version

Increase the MINOR version when functionality is added without breaking the existing architecture.

Examples:

* adding a new template;
* adding a validation rule;
* adding a supported Object subtype;
* adding a compiler capability;
* adding a generated report;
* adding a new Business System that follows existing standards.

Example:

`1.0.0 → 1.1.0`

Minor changes require:

* documented change;
* validation;
* affected tests;
* release notes.

---

# Patch Version

Increase the PATCH version when correcting an error without changing architecture or expected behavior.

Examples:

* fixing a broken link;
* correcting template wording;
* fixing generated YAML;
* correcting a registry entry;
* repairing a compiler defect;
* clarifying documentation without changing a rule.

Example:

`1.0.0 → 1.0.1`

Patch changes require:

* documented fix;
* validation;
* release-note entry.

---

# Versioned Components

The following components must declare a version:

* SVOS Core;
* OS Specification;
* Architecture Standards;
* Object Model;
* Template Library;
* Compiler;
* Validation Engine;
* generated Business Systems;
* generated Project structures;
* generated Job structures;
* release packages.

---

# Required Version Metadata

Generated Objects must include:

```yaml
os_version: 1.0.0
spec_version: 1.0.0
architecture_version: 1.0.0
template_version: 1.0.0
compiler_version: 1.0.0
generated_at:
generated_by:
```

Use the exact versions that produced the Object.

Do not automatically replace historical metadata when the Core version changes.

---

# Compatibility

A generated Object is compatible only when:

* its declared architecture version is supported;
* its template version exists;
* its required Object types exist;
* its registry structure remains valid;
* its links pass validation;
* its lifecycle states remain supported.

---

# Compilation Compatibility

Before compilation, the compiler must confirm:

1. specification version exists;
2. architecture version exists;
3. requested template version exists;
4. Company Brain version is available;
5. output does not require unsupported Objects;
6. migration is not required.

Compilation must fail when compatibility cannot be confirmed.

---

# Generated-System Versioning

Each Business System declares:

```yaml
business_system_version:
compiled_against_os:
compiled_against_spec:
compiled_against_template:
```

Example:

```yaml
business_system_version: 1.0.0
compiled_against_os: 1.0.0
compiled_against_spec: 1.0.0
compiled_against_template: 1.0.0
```

---

# Company Brain Versioning

Canonical Company Brain files retain their own version history.

A Company Brain update does not automatically require an SVOS Core version change.

Examples:

* adding an approved feature;
* changing pricing;
* adding a customer definition;
* updating brand rules.

These changes require:

* source update;
* decision record when material;
* dependent-system review;
* regeneration of affected outputs.

---

# Template Versioning

Templates are versioned independently.

A template change must identify whether it is:

* backward compatible;
* migration required;
* regeneration required;
* validation-only.

Generated Objects must retain the template version used at compilation.

---

# Compiler Versioning

Compiler behavior is versioned separately from the specification.

A compiler update may not silently change generated structure without:

* corresponding specification or template version;
* test updates;
* release notes;
* compatibility review.

---

# Release States

Every release uses one of these states:

* development
* candidate
* approved
* released
* deprecated
* retired

---

# Release Naming

Format:

`SVOS vMAJOR.MINOR.PATCH`

Examples:

* `SVOS v1.0.0`
* `SVOS v1.1.0`
* `SVOS v2.0.0`

Package naming:

`svos-core-v1.0.0`

Generated release naming:

`sessionvue-os-v1.0.0`

---

# Release Requirements

A release may not be marked `released` until:

* specifications pass validation;
* architecture tests pass;
* templates pass validation;
* compiler tests pass;
* generated sample system passes acceptance tests;
* unresolved links equal zero;
* registry conflicts equal zero;
* required approvals are recorded;
* release notes exist.

---

# Deprecation

Deprecated components remain available for migration and audit.

They must declare:

* replacement;
* deprecation date;
* migration instructions;
* removal target version;
* affected Objects.

Deprecated components are never silently deleted.

---

# Rollback

Every release must preserve the ability to return to the previous approved version.

Rollback requires:

* previous release tag;
* previous generated output;
* migration reversal instructions;
* affected-data review;
* validation after rollback.

---

# Git Tags

Approved releases should be tagged using:

```text
v1.0.0
v1.1.0
v2.0.0
```

Do not tag drafts or incomplete releases as approved releases.

---

# Changelog

Every version change must update:

`docs/CHANGELOG.md`

Each entry must include:

* version;
* date;
* change type;
* summary;
* affected components;
* migration requirement;
* approval;
* validation result.

---

# Validation Rules

Compilation fails when:

* required version metadata is missing;
* a referenced version does not exist;
* incompatible versions are combined;
* a generated Object claims the wrong compiler version;
* a breaking change is released as a minor or patch version;
* a release lacks validation evidence;
* a deprecated component is removed without migration.
