# Registry Validation

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
