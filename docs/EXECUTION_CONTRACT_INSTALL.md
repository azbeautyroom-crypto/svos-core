# Install CONTRACT-001

Merge this package into the root of `svos-core`.

Expected paths:

```text
contracts/EXECUTION_CONTRACT.md
compiler/EXECUTION_CONTRACT_BINDING.md
validation/execution-contract.md
docs/EXECUTION_CONTRACT_INSTALL.md
```

Do not put the outer package folder inside `svos-core`.

After merging, run:

```bash
git status
git diff -- contracts compiler validation docs
```

Then commit only after review:

```bash
git add contracts/EXECUTION_CONTRACT.md \
  compiler/EXECUTION_CONTRACT_BINDING.md \
  validation/execution-contract.md \
  docs/EXECUTION_CONTRACT_INSTALL.md

git commit -m "Add canonical SVOS execution contract"
git push
```

## Current Phase

```text
Phase 0 — SVOS Core: complete
Phase 1 — Company Brain: complete
Compile Layer: complete
Phase 2.1 — Executive System: in progress
Current package: Execution Contract prerequisite before Package 2.4
Next package: Executive Company Priorities
```
