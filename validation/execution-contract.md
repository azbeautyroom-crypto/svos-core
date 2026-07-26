---
title: Execution Contract Validation
object_type: validation
status: review
owner: founder
updated: 2026-07-26
version: 1.0.0
contract: CONTRACT-001
source_of_truth: false
generated: false
---

# Execution Contract Validation

## Build-Failing Checks

A generated object fails when:

- required frontmatter is missing;
- `contract: CONTRACT-001` is absent;
- `generated: true` is absent;
- required sections for the object type are missing;
- a Job lacks Trigger, Inputs, Execution, Output, Destination, Validation, or Completion Condition;
- an Automation lacks Executed Job, Permissions, Monitoring, Failure Handling, or Disable Procedure;
- a Project lacks Objective, Activated Systems, Required Jobs, Deliverables, Approvals, Metrics, or Completion Condition;
- a Business System lacks Purpose, Scope, Workflow, Jobs, Outputs, Metrics, Exceptions, or Improvement Loop;
- an Approval lacks an approver;
- a Metric lacks a source or owner;
- an output lacks an exact destination;
- an external write lacks an explicit permission boundary;
- internal links do not resolve;
- canonical Knowledge is duplicated.

## Warning Checks

Warn but do not fail when:

- a metric target is `NOT IN SOURCE`;
- an optional integration is unconfigured;
- a future Business System is referenced but not yet compiled;
- a review cadence is not yet established.

## Release Gate

Generated output may be released only when:

```text
Architecture Validation = PASS
Execution Contract Validation = PASS
Link Validation = PASS
Registry Validation = PASS
Acceptance Tests = PASS
```
