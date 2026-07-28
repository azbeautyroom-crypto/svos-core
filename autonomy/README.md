# Autonomy Foundation (Kernel Proof)

Minimum Autonomy Foundation that proves SVOS Kernel v1.0 can safely
execute one complete Job through:

```
Trigger → Queue → Machine Capability Resolution → Eligibility → Dependency
→ Permission → Execution → Validation → State → Logs
```

## Boundaries

- Machine Capability is the only executable capability type.
- Company Capability / Company Asset catalogs are never consulted.
- Event Bus is deferred (ADR-007).
- Writes are allowlisted to `autonomy/runs/` only (repo sandbox).
- Proof Job autonomy level is LEVEL 1. LEVEL 3 is never inferred.

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

## Run the proof Job

```bash
.venv/bin/python -m autonomy.kernel.runner job.prove_kernel_execution
```

## Test

```bash
.venv/bin/python -m pytest tests/test_autonomy_kernel.py -q
```

Expected: all tests pass.

## Catalog

| Object | ID |
|---|---|
| Job | `job.prove_kernel_execution` |
| Machine Capability | `mc.write_autonomy_run_record` |
| Adapter | `adapter.filesystem` |
| Tool | `tool.write_run_artifact` |
