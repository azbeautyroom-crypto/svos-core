#!/usr/bin/env python3
"""Install SVOS Package B4 — Validation and Release Management v1.0.0.

Run from the svos-core repository root:
    python3 scripts/install_b4.py

Optional overwrite mode:
    python3 scripts/install_b4.py --force
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

B4_VERSION = "1.0.0"

FILES = {
    "validation/README.md": '''# SVOS Validation Engine

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
''',
    "validation/architecture.md": '''# Architecture Validation

Version: 1.0.0
Status: LOCKED
Owner: SVOS Core

# Business System Anatomy

Every Business System must contain:

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

# PASS Conditions

- every required folder exists;
- every required file exists;
- names match standards;
- required objects exist;
- no unapproved architecture is introduced;
- no canonical ownership is duplicated;
- declared versions are compatible.

# FAIL Conditions

- missing folder or file;
- renamed standard folder;
- unsupported object type;
- Business System anatomy mismatch;
- duplicate canonical ownership;
- incompatible version;
- architecture changed without an ADR.
''',
    "validation/yaml.md": '''# YAML Validation

Version: 1.0.0
Status: LOCKED
Owner: SVOS Core

# Required Fields

```yaml
id:
object_type:
owner:
status:
version:
source_of_truth:
created:
updated:
os_version:
spec_version:
template_version:
```

# PASS Conditions

- frontmatter parses;
- required fields exist;
- keys are unique;
- IDs follow naming standards;
- statuses are approved values;
- dates use YYYY-MM-DD;
- versions use semantic versioning;
- source-of-truth values are explicit.

# FAIL Conditions

- missing or malformed frontmatter;
- duplicate key;
- missing required field;
- unsupported status;
- invalid date or version;
- ambiguous source of truth.
''',
    "validation/links.md": '''# Link Validation

Version: 1.0.0
Status: LOCKED
Owner: SVOS Core

# Validate

- Obsidian wikilinks;
- Markdown relative links;
- registry references;
- canonical-source references;
- Project-to-System links;
- Project-to-Job links;
- Job-to-Knowledge links.

# PASS Conditions

- unresolved required links equal zero;
- every target exists;
- canonical links resolve to one authority;
- no orphan required object exists;
- no circular authority chain exists.

# FAIL Conditions

- broken, missing, or ambiguous target;
- orphan object;
- circular canonical ownership;
- generated file lacks a canonical-source link.
''',
    "validation/ontology.md": '''# Ontology Validation

Version: 1.0.0
Status: LOCKED
Owner: SVOS Core

# PASS Conditions

Every object has one canonical type, one owner, one source of truth, a supported lifecycle, valid relationships, a unique ID, and a registry entry when required.

# FAIL Conditions

- unknown or duplicate object type;
- multiple owners;
- missing lifecycle or canonical source;
- invalid relationship;
- orphan object;
- one name used for multiple objects.
''',
    "validation/registries.md": '''# Registry Validation

Version: 1.0.0
Status: LOCKED
Owner: SVOS Core

# Validate

- unique IDs;
- canonical names;
- object types;
- ownership;
- source locations;
- versions;
- statuses;
- lifecycle state;
- relationships.

# PASS Conditions

- every required object is registered;
- every ID is unique;
- every path resolves;
- registry state matches the canonical source;
- no object has conflicting owners.

# FAIL Conditions

- duplicate ID;
- missing entry;
- nonexistent target;
- owner conflict;
- version or status mismatch;
- duplicate registry authority.
''',
    "validation/acceptance-tests.md": '''# SVOS Acceptance Tests

Version: 1.0.0
Status: LOCKED
Owner: SVOS Core

# Required Tests

1. Specification Compatibility
2. Required Structure
3. YAML and Metadata
4. Naming
5. Source of Truth
6. Registry Integrity
7. Link Integrity
8. Ontology Integrity
9. Business System Ownership
10. Project Relationship
11. Job Integrity
12. Approval Integrity
13. Automation Safety
14. Integration Boundaries
15. Metric Integrity
16. Locked Policy Compliance
17. Validation Evidence
18. Release Readiness

# Passing Standard

```text
Required Tests Passed: 100%
Unresolved Links: 0
Registry Conflicts: 0
Canonical Conflicts: 0
Architecture Violations: 0
Unapproved Exceptions: 0
```

A failed package must not be described, committed, tagged, installed, or released as complete.
''',
    "validation/release-gates.md": '''# SVOS Release Gates

Version: 1.0.0
Status: LOCKED
Owner: SVOS Core

# Required Gates

1. Scope Complete
2. Architecture Valid
3. Specification Compatible
4. Validation Passed
5. Links Resolved
6. Registries Updated
7. Source of Truth Confirmed
8. Required Approvals Defined
9. Security Boundaries Valid
10. Acceptance Tests Passed
11. Documentation Current
12. Founder Review
13. Git State Clean
14. Release Version Available
15. Rollback Available

# Release Decision

```text
15 PASS
0 FAIL
```

Any other result is RELEASE BLOCKED.
''',
    "docs/RELEASE_PROCESS.md": '''# SVOS Release Process

Version: 1.0.0
Status: LOCKED
Owner: Founder

```text
Define
→ Build
→ Self-Review
→ Validate
→ Correct
→ Revalidate
→ Founder Review
→ Commit
→ Push
→ Tag
→ Release Notes
→ Install
→ Verify
→ Close
```

Every package must be scoped, reviewed, validated, approved when required, committed with explicit paths, pushed, and verified before closure.
''',
    "docs/CHANGE_CONTROL.md": '''# SVOS Change Control

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
''',
    "docs/ADR_TEMPLATE.md": '''# ADR-NNN — Decision Title

Status: proposed
Date: YYYY-MM-DD
Owner: founder
Decision Type: architecture
SVOS Version:
Affected Version:

# Context

# Current State

# Decision Required

# Evidence

# Options

## Option 1

## Option 2

## Option 3

# Recommendation

# Founder Decision

`PENDING`

# Rationale

# Consequences

# Affected Objects

# Files to Update

# Tests to Update

# Regeneration Required

- yes
- no

# Version Impact

- major
- minor
- patch
- none

# Migration Plan

# Rollback Plan

# Validation Required

- architecture
- naming
- links
- YAML
- ontology
- registries
- acceptance tests
- release gates
''',
    "docs/PACKAGE_STATUS.md": '''# SVOS Package Status

Updated: 2026-07-25
Owner: Founder

| Package | Name | Status | Version | Notes |
|---|---|---|---|---|
| B1 | SVOS Core Specification | Complete | 1.0.0 | Committed and pushed |
| B2 | Template Library | Complete | 1.0.0 | Eight template packages committed and pushed |
| B3 | Compiler Engine | Intentionally Skipped | — | Founder decision; may be revisited |
| B4 | Validation and Release Management | In Progress | 1.0.0 | Current package |
| 2.1 | Executive System | Not Started | — | Begins after B4 |
| 2.2 | Operations System | Not Started | — | Follows Executive |
| 2.3 | Marketing System | Not Started | — | Follows Operations |
| 2.4 | Product System | Not Started | — | Follows Marketing |
| 2.5 | Engineering System | Not Started | — | Follows Product |

# B3 Record

B3 must not be shown as accidentally missing, silently reintroduced, completed, or required for Package 2.1.

Until B3 is revisited, Business Systems are directly authored from locked templates and validated through B4.
''',
}

ROADMAP_SECTION = '''## Package Roadmap

- B1 — SVOS Core Specification: Complete
- B2 — Template Library: Complete
- B3 — Compiler Engine: Intentionally Skipped by founder decision
- B4 — Validation and Release Management: In Progress
- Package 2.1 — Executive System: Next

B3 may be revisited later. It is not a dependency for the directly authored and validated Executive System package.
'''

CHANGELOG_SECTION = '''## Unreleased

### Added

- B4 validation standards
- Acceptance test framework
- Release gates
- Release process
- Change-control process
- Architecture Decision Record template
- Package status tracking

### Decisions

- B3 — Compiler Engine was intentionally skipped by founder decision.
- Phase 2 Business Systems will be directly authored from locked templates and validated through B4 until B3 is revisited.
'''


def normalize(text: str) -> str:
    return text.strip() + "\n"


def write_target(path: Path, content: str, force: bool) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    new_content = normalize(content)
    if path.exists():
        current = path.read_text(encoding="utf-8")
        if current == new_content:
            return "unchanged"
        if current.strip() and not force:
            return "skipped"
    path.write_text(new_content, encoding="utf-8")
    return "written"


def append_once(path: Path, marker: str, content: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker in current:
        return "unchanged"
    spacer = "\n" if current.endswith("\n") or not current else "\n\n"
    path.write_text(current + spacer + normalize(content), encoding="utf-8")
    return "updated"


def remove_redundant_gitkeeps(root: Path) -> list[Path]:
    removed = []
    for marker in root.rglob(".gitkeep"):
        others = [p for p in marker.parent.iterdir() if p.name != ".gitkeep"]
        if others:
            marker.unlink()
            removed.append(marker.relative_to(root))
    return removed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo).expanduser().resolve()
    if not (root / "spec").exists():
        print(f"ERROR: {root} does not look like svos-core; spec/ is missing.", file=sys.stderr)
        return 2

    results = {"written": [], "unchanged": [], "skipped": [], "updated": []}
    for relative, content in FILES.items():
        status = write_target(root / relative, content, args.force)
        results[status].append(relative)

    results[append_once(root / "docs/ROADMAP.md", "## Package Roadmap", ROADMAP_SECTION)].append("docs/ROADMAP.md")
    results[append_once(root / "docs/CHANGELOG.md", "B3 — Compiler Engine was intentionally skipped", CHANGELOG_SECTION)].append("docs/CHANGELOG.md")

    removed = remove_redundant_gitkeeps(root)

    print(f"SVOS B4 installer v{B4_VERSION}\n")
    for status in ("written", "updated", "unchanged", "skipped"):
        print(f"{status}: {len(results[status])}")
        for item in results[status]:
            print(f"  - {item}")

    print(f"removed redundant .gitkeep files: {len(removed)}")
    for item in removed:
        print(f"  - {item}")

    if results["skipped"]:
        print("\nNon-empty files were preserved. Review them or rerun with --force if replacement is intentional.", file=sys.stderr)
        return 1

    print("\nNext commands:")
    print("  git status --short")
    print("  git diff -- validation docs")
    print("  git add validation docs scripts/install_b4.py")
    print('  git commit -m "Build SVOS validation and release management v1.0.0"')
    print("  git push origin main")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
