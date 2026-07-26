# Link Validation

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
