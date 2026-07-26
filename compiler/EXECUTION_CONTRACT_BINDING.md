---
title: Execution Contract Compiler Binding
object_type: architecture
status: review
owner: founder
updated: 2026-07-26
version: 1.0.0
contract: CONTRACT-001
source_of_truth: false
generated: false
---

# Execution Contract Compiler Binding

## Required Compiler Behavior

Every compile must:

1. Load `contracts/EXECUTION_CONTRACT.md`.
2. Load the applicable object template.
3. Load canonical company inputs.
4. Generate every required execution section.
5. Add `contract: CONTRACT-001` to frontmatter.
6. Validate the output before release.
7. Fail the build when required sections are missing.
8. Never repair generated files directly.

## Source Order

```text
Founder Instructions
→ Locked Decisions
→ Architecture
→ Execution Contract
→ Company Inputs
→ Object Template
→ Compiler Rules
→ Generated Output
```

## Generated Output

All generated objects must include:

```yaml
contract: CONTRACT-001
generated: true
```

Hand-authored compiler inputs must include:

```yaml
contract: CONTRACT-001
generated: false
```
