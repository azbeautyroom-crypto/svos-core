# SVOS Source of Truth Standard

Version: 1.0.0
Status: LOCKED

---

# Purpose

SVOS requires one canonical source for every fact, rule, object, decision, workflow, and operational state.

The purpose of this standard is to prevent duplication, contradiction, hidden memory, and unsupported claims.

---

# Core Rule

Every durable piece of information has exactly one Source of Truth.

Other files may reference it.

Other files may summarize it.

Other files may not redefine it.

---

# Authority Order

1. Founder Decisions
2. SVOS Core
3. Company Brain
4. Business Systems
5. Projects
6. Jobs
7. Generated Outputs
8. External Sources

A lower authority may not override a higher authority.

---

# Canonical Source Types

## Architecture

Canonical location:

`spec/`

Owns:

* OS architecture
* object model
* relationships
* naming
* versioning
* validation
* source-of-truth rules

---

## Company Knowledge

Canonical location:

Company Brain

Owns:

* mission
* vision
* company identity
* products
* memberships
* pricing
* customers
* brand
* integrations
* company objects
* founder directives

---

## Business System Logic

Canonical location:

Business System specification

Owns:

* policies
* workflows
* Jobs
* metrics
* automations
* integration use
* decision rules
* exception handling

---

## Project Information

Canonical location:

Active Project

Owns:

* objective
* scope
* deadline
* deliverables
* dependencies
* activated Systems
* approval state
* project metrics
* next action

Projects may not redefine Business System logic.

---

## Job Procedure

Canonical location:

Job specification

Owns:

* trigger
* required inputs
* required sources
* execution steps
* decision rules
* output
* destination
* quality check
* approval
* failure handling
* completion condition

---

## Production Code

Canonical location:

GitHub repository

Owns:

* source code
* configuration
* migrations
* tests
* deployment history

---

## Production Data

Canonical location:

Approved production database or application service

Examples:

* Supabase
* email platform
* analytics platform
* Airtable when explicitly assigned

---

## Decisions

Canonical location:

Decision Record

Owns:

* issue
* evidence
* options
* founder decision
* rationale
* affected Objects
* required updates

A decision is not complete until all affected canonical sources are updated.

---

# Missing Information

When a required fact is unavailable, write:

`NOT IN SOURCE — needs [owner]`

Do not guess.

Do not silently infer.

Do not replace missing company knowledge with general knowledge.

---

# Assumptions

Every assumption must be visible.

Format:

`[ASSUMPTION: description]`

Assumptions are temporary.

Assumptions may not become canonical without approval.

---

# Conflicts

When two sources conflict:

1. Identify both sources.
2. Determine authority order.
3. Treat the higher source as controlling.
4. Flag the lower source as stale.
5. Do not silently rewrite the lower source.
6. Create a Decision Record when policy or architecture changes.
7. Update every affected reference.

---

# Duplication

Compilation fails when:

* two files claim canonical ownership;
* the same Object has multiple owners;
* a Project duplicates System logic;
* a Job duplicates canonical Knowledge;
* generated output becomes manually maintained;
* copied facts diverge from their canonical source.

---

# External Information

External content is evidence, not authority.

External information may support:

* research
* comparisons
* verification
* recommendations
* market analysis

External information may not override:

* founder decisions
* architecture
* company facts
* locked brand rules
* membership rules
* product definitions

---

# Memory

Chat history and native AI memory are not canonical company memory.

Anything worth retaining must be written into its proper Source of Truth.

---

# Validation Rules

Every Object must declare:

* canonical source;
* owner;
* authority;
* status;
* version;
* related Objects.

Every generated file must link back to its canonical source.

No unresolved canonical conflict may pass validation.
