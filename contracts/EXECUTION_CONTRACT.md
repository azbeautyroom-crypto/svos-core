---
title: SVOS Execution Contract
object_type: architecture
status: review
owner: founder
updated: 2026-07-26
contract_id: CONTRACT-001
version: 1.0.0
authority: canonical
locked: true
applies_to:
  - business-system
  - project
  - job
  - workflow
  - automation
  - metric
  - decision
  - approval
  - knowledge
  - map
---

# SVOS Execution Contract

## Purpose

Define the mandatory execution anatomy for every executable object created, compiled, or maintained by SVOS.

This contract prevents passive documentation from entering the operating system.

Every governed object must help the company:

- make a decision;
- initiate or execute work;
- validate work;
- route an approval;
- monitor performance;
- update company state;
- or improve a System.

## Authority

This contract is subordinate only to:

1. current founder instruction;
2. locked founder decisions;
3. the SVOS Constitution;
4. the Operating Doctrine.

No Business System, Project, Job, Workflow, Automation, Metric, Decision, Approval, Knowledge object, or Map may redefine this execution anatomy.

## Mandatory Execution Anatomy

Every governed object must define the applicable sections below.

### 1. Purpose

The exact business outcome or operating responsibility this object exists to support.

### 2. Trigger

The event, schedule, state change, threshold, or founder command that activates the object.

### 3. Inputs

The structured information required before execution may begin.

### 4. Required Sources

The canonical Knowledge, Decisions, Systems, Projects, metrics, or external sources that must be read.

### 5. Preconditions

The conditions that must be true before execution.

### 6. Owner

The person, agent, runner, or Business System accountable for the object.

### 7. Execution

The ordered actions performed when the object runs.

### 8. Decision Logic

Explicit rules written as:

```text
IF condition
THEN action
ELSE alternative
ESCALATE WHEN condition
```

### 9. Outputs

The artifacts, records, decisions, state changes, or reports produced.

### 10. Destinations

The exact approved locations where outputs are written or routed.

### 11. Updates

The Systems, Projects, registries, metrics, decisions, or Knowledge records that must reflect the result.

### 12. Validation

The checks required before the output may proceed.

### 13. Approval

Whether approval is required, who approves, what invalidates approval, and what happens when approval is denied or expires.

### 14. Exceptions

Known failure conditions and the required response for each.

### 15. Permissions

The allowed reads, allowed writes, prohibited actions, and external state boundaries.

### 16. Connected Objects

The related Systems, Projects, Jobs, Knowledge, Decisions, Automations, Metrics, and integrations.

### 17. Metrics

The measures used to determine whether the object executed correctly and created value.

### 18. Completion Condition

The exact state that proves execution is complete.

### 19. Improvement Loop

How corrections, failures, founder feedback, and performance results update the governing System or Job.

## Applicability by Object Type

### Business System

Must define all sections at the System level and link to executable Jobs for operational steps.

A Business System governs execution but does not perform all work directly.

### Project

Must define the temporary objective, activated Systems, required Jobs, deliverables, approvals, metrics, and completion condition.

A Project may not duplicate reusable System or Job logic.

### Job

Must define every section in the Mandatory Execution Anatomy.

Jobs are the primary executable units of SVOS.

### Workflow

Must define triggers, states, owners, transitions, gates, exceptions, outputs, and exit conditions.

### Automation

Must define the executed Job, trigger, tools, credentials by reference, permissions, dry run, monitoring, retries, rollback, and disable procedure.

### Metric

Must define its source, formula, cadence, thresholds, owner, and the action taken when performance changes.

### Decision

Must define the issue, evidence, options, founder decision, affected objects, propagation steps, and revisit trigger.

### Approval

Must define the requested decision, evidence, approver, options, result, expiration, and follow-up actions.

### Knowledge

Canonical Knowledge is not required to execute actions itself.

It must define:

- purpose;
- source;
- authority;
- owner;
- consumers;
- review cadence;
- update conditions;
- and conflict handling.

Knowledge must never silently contain a procedure that should be a Job.

### Map

Must define entry point, object relationships, allowed routes, exit point, and exceptions.

## Passive Documentation Test

A file fails this contract when it only describes a topic and does not provide one or more of the following:

- canonical authority;
- executable behavior;
- decision support;
- validation;
- measurable state;
- approval routing;
- or operating continuity.

A failed file must be:

1. converted into an executable object;
2. moved into canonical Knowledge;
3. merged into an existing authority with founder approval;
4. or excluded from SVOS.

## Required Frontmatter

Every governed object must include:

```yaml
---
title:
object_type:
status:
owner:
updated:
version:
system:
project:
contract:
source_of_truth:
generated:
---
```

Use only applicable fields, but `title`, `object_type`, `status`, `owner`, `updated`, `version`, and `contract` are mandatory.

The contract value must include:

```yaml
contract: CONTRACT-001
```

## Generated Output Rule

Files under `generated/` are compiler output.

They must not be edited manually.

When generated output fails this contract:

1. identify whether the defect belongs to input, template, compiler rule, or validation;
2. fix the upstream source;
3. regenerate;
4. validate again.

## Validation Rules

Every build must verify:

- required frontmatter exists;
- `contract: CONTRACT-001` is present;
- the object type is registered;
- required execution sections exist for that object type;
- all internal links resolve;
- outputs have destinations;
- every approval names an approver;
- every metric names a source and owner;
- every automation names an executed Job;
- every external write declares permissions;
- no canonical Knowledge is duplicated;
- no generated file is marked as manually authored.

## Failure Behavior

If an object fails validation:

1. mark the build failed;
2. identify the exact missing or conflicting section;
3. do not release the generated output;
4. correct the upstream source;
5. rerun the compiler and validation.

## Change Control

This contract is locked.

Changes require:

- an Architecture Decision Record;
- impact analysis;
- migration plan;
- validation updates;
- compiler updates;
- template updates;
- founder approval;
- version increment.

## Acceptance Condition

This contract is successfully installed when:

- it exists at `contracts/EXECUTION_CONTRACT.md`;
- compiler rules reference it;
- validation rules enforce it;
- templates declare `CONTRACT-001`;
- newly generated objects pass contract validation;
- generated output is not manually edited.
