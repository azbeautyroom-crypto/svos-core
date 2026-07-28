# Autonomy Foundation (Kernel v1.0 baseline)

Minimum Autonomy Foundation that executes Jobs through:

```
Trigger → Queue → Machine Capability Resolution → Eligibility → Dependency
→ Permission → Execution → Validation → State → Logs
```

## Boundaries

- Machine Capability is the only executable capability type.
- Company Capability / Company Asset catalogs are never consulted.
- Event Bus is deferred (ADR-007).
- Writes are allowlisted to `autonomy/runs/` only (repo sandbox).
- Production Jobs in this package are LEVEL 1. LEVEL 3 is never inferred.

## Clean-room setup

Prerequisites:

- Python 3.9+
- Repository root as the working directory

```bash
cd /path/to/svos-core
python3 -m venv .venv
.venv/bin/pip install pytest
export PYTHONPATH=.
```

On Windows PowerShell, set `PYTHONPATH` to the repo root before running commands below.

## Production Job — Launch Blocker Review

```bash
.venv/bin/python -m autonomy.kernel.runner job.launch_blocker_review
```

Reads in-repo Projects, Integration Brain, Product Brain, Product Implementation
Audit, and Founder Directives. Writes a deterministic report under
`autonomy/runs/reports/`.

`HQ/Active Priorities.md` is vault-only and is recorded as `NOT IN SOURCE`.

## Proof Job

```bash
.venv/bin/python -m autonomy.kernel.runner job.prove_kernel_execution
```

## Test

```bash
.venv/bin/python -m pytest tests/test_autonomy_kernel.py tests/test_launch_blocker_review.py -q
```

Expected: all tests pass.

## Catalog

| Object | ID |
|---|---|
| Job (proof) | `job.prove_kernel_execution` |
| Job (production) | `job.launch_blocker_review` |
| Machine Capability | `mc.write_autonomy_run_record` |
| Machine Capability | `mc.write_launch_blocker_review` |
| Adapter | `adapter.filesystem` |
| Tool | `tool.write_run_artifact` |
| Tool | `tool.write_launch_blocker_review` |
