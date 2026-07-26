# YAML Validation

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
