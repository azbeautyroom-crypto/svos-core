# Architecture Validation

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
