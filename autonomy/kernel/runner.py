"""SVOS Kernel v1.0 runner — Trigger → Logs.

Machine Capability is the only executable type.
Company Capability / Company Asset catalogs are never consulted.
"""

from __future__ import annotations

import argparse
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from autonomy.kernel.models import STAGE_ORDER, RunStatus, StageResult, WorkItem

ROOT = Path(__file__).resolve().parents[2]
AUTONOMY = ROOT / "autonomy"
CATALOG = AUTONOMY / "catalog"
JOBS = AUTONOMY / "jobs"
CONTROL = AUTONOMY / "control"
RUNS = AUTONOMY / "runs"

# Hard deny: Company Brain capability/asset catalogs are outside runtime.
FORBIDDEN_SOURCE_FRAGMENTS = (
    "Company Capability",
    "Company Asset",
    "company-capability",
    "company_capability",
    "company-asset",
    "company_asset",
    "Business Capability",
)


def _relpath_or_abs(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _glob_match(path: str, pattern: str) -> bool:
    """Match path against a simple ** allowlist pattern relative to repo root."""
    path = path.replace("\\", "/").lstrip("./")
    pattern = pattern.replace("\\", "/")
    if pattern.endswith("/**"):
        prefix = pattern[:-3]
        return path == prefix or path.startswith(prefix.rstrip("/") + "/")
    if "*" not in pattern and "?" not in pattern:
        return path == pattern
    regex = re.escape(pattern).replace(r"\*\*", ".*").replace(r"\*", "[^/]*")
    return re.fullmatch(regex, path) is not None


def _path_allowed(relpath: str, allowlists: list[str]) -> bool:
    return any(_glob_match(relpath, pattern) for pattern in allowlists)


def _assert_no_company_catalog_consultation(opened_paths: list[Path]) -> None:
    for path in opened_paths:
        text = str(path)
        for fragment in FORBIDDEN_SOURCE_FRAGMENTS:
            if fragment.lower().replace(" ", "-") in text.lower().replace(" ", "-"):
                raise RuntimeError(
                    f"Company Capability/Asset consultation forbidden; opened {path}"
                )


def load_job(job_id: str) -> dict[str, Any]:
    path = JOBS / f"{job_id.removeprefix('job.')}.json"
    if not path.exists():
        # Also allow exact filename match
        path = JOBS / f"{job_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Job not found: {job_id}")
    return _load_json(path)


def load_kill_switch() -> dict[str, Any]:
    return _load_json(CONTROL / "kill_switch.json")


def load_machine_capabilities() -> dict[str, dict[str, Any]]:
    data = _load_json(CATALOG / "machine_capabilities.json")
    return {item["id"]: item for item in data["machine_capabilities"]}


def load_adapters() -> dict[str, dict[str, Any]]:
    data = _load_json(CATALOG / "adapters.json")
    return {item["id"]: item for item in data["adapters"]}


def load_tools() -> dict[str, dict[str, Any]]:
    data = _load_json(CATALOG / "tools.json")
    return {item["id"]: item for item in data["tools"]}


def _tool_write_run_artifact(
    *,
    run_id: str,
    job_id: str,
    machine_capability_id: str,
    tool: dict[str, Any],
    destination_relpath: str | None = None,
) -> Path:
    allowlist = tool["path_allowlist"]
    relpath = destination_relpath or f"autonomy/runs/artifacts/{run_id}.json"
    if not _path_allowed(relpath, allowlist):
        raise PermissionError(f"Path outside tool allowlist: {relpath}")
    if not relpath.endswith(".json"):
        raise PermissionError(f"Disallowed extension for tool: {relpath}")

    abs_path = ROOT / relpath
    # Defense in depth: must stay under autonomy/runs/
    runs_root = (ROOT / "autonomy" / "runs").resolve()
    if runs_root not in abs_path.resolve().parents and abs_path.resolve() != runs_root:
        raise PermissionError(f"Refusing write outside autonomy/runs/: {relpath}")

    payload = {
        "run_id": run_id,
        "job_id": job_id,
        "machine_capability_id": machine_capability_id,
        "status": "completed",
        "completed_at": _utc_now(),
    }
    _write_json(abs_path, payload)
    return abs_path


def run_job(
    job_id: str,
    *,
    runs_root: Path | None = None,
    force_destination: str | None = None,
    override_machine_capabilities: list[str] | None = None,
    kill_switch_override: dict[str, Any] | None = None,
) -> WorkItem:
    """Execute one Job through the locked Kernel v1.0 path."""
    runs = runs_root or RUNS
    queue_dir = runs / "queue"
    registry_dir = runs / "registry"
    logs_dir = runs / "logs"
    artifacts_dir = runs / "artifacts"
    for d in (queue_dir, registry_dir, logs_dir, artifacts_dir):
        d.mkdir(parents=True, exist_ok=True)

    opened: list[Path] = []
    run_id = str(uuid.uuid4())
    work_id = f"work-{run_id}"
    work = WorkItem(work_id=work_id, job_id=job_id, run_id=run_id)

    def record(stage: StageResult) -> None:
        work.stages.append(stage)

    def block(stage_name: str, reason: str) -> WorkItem:
        record(StageResult(name=stage_name, ok=False, detail=reason))
        work.status = RunStatus.BLOCKED
        work.blocked_reason = reason
        _persist(work, queue_dir, registry_dir, logs_dir)
        return work

    # --- Trigger ---
    record(
        StageResult(
            name="Trigger",
            ok=True,
            detail="Founder/test invocation",
            data={"job_id": job_id, "run_id": run_id},
        )
    )

    # --- Queue ---
    work.status = RunStatus.QUEUED
    queue_path = queue_dir / f"{work_id}.json"
    _write_json(queue_path, work.to_dict())
    record(
        StageResult(
            name="Queue",
            ok=True,
            detail="Work item queued",
            data={"queue_path": _relpath_or_abs(queue_path)},
        )
    )
    work.status = RunStatus.RUNNING

    # Load job definition
    try:
        job_path = JOBS / f"{job_id.removeprefix('job.')}.json"
        if not job_path.exists():
            job_path = JOBS / f"{job_id}.json"
        opened.append(job_path)
        job = _load_json(job_path)
    except FileNotFoundError:
        return block("MachineCapabilityResolution", f"Job not found: {job_id}")

    work.autonomy_level = int(job.get("autonomy_level", 0))
    required_mcs = list(
        override_machine_capabilities
        if override_machine_capabilities is not None
        else job.get("required_machine_capabilities", [])
    )

    # --- Machine Capability Resolution ---
    mc_path = CATALOG / "machine_capabilities.json"
    adapter_path = CATALOG / "adapters.json"
    tool_path = CATALOG / "tools.json"
    opened.extend([mc_path, adapter_path, tool_path])
    _assert_no_company_catalog_consultation(opened)

    mcs = load_machine_capabilities()
    adapters = load_adapters()
    tools = load_tools()

    if not required_mcs:
        return block(
            "MachineCapabilityResolution",
            "Job declares no Machine Capabilities; improvisation forbidden",
        )

    resolved: list[dict[str, Any]] = []
    for mc_id in required_mcs:
        mc = mcs.get(mc_id)
        if mc is None:
            return block(
                "MachineCapabilityResolution",
                f"Unknown Machine Capability: {mc_id}",
            )
        adapter = adapters.get(mc["adapter_id"])
        if adapter is None:
            return block(
                "MachineCapabilityResolution",
                f"Adapter missing for {mc_id}: {mc['adapter_id']}",
            )
        for tool_id in mc["tool_ids"]:
            if tool_id not in tools:
                return block(
                    "MachineCapabilityResolution",
                    f"Tool missing for {mc_id}: {tool_id}",
                )
        resolved.append({"mc": mc, "adapter": adapter, "tools": [tools[t] for t in mc["tool_ids"]]})

    record(
        StageResult(
            name="MachineCapabilityResolution",
            ok=True,
            detail="Resolved required Machine Capabilities",
            data={"machine_capability_ids": required_mcs},
        )
    )

    # --- Eligibility ---
    if kill_switch_override is None:
        kill_path = CONTROL / "kill_switch.json"
        opened.append(kill_path)
        kill = load_kill_switch()
    else:
        kill = kill_switch_override
    if not kill.get("enabled", False):
        return block("Eligibility", "Kill switch disabled; foundation halted")

    record(
        StageResult(
            name="Eligibility",
            ok=True,
            detail="Kill switch enabled; preconditions met",
            data={"kill_switch": True},
        )
    )

    # --- Dependency ---
    deps = job.get("dependencies") or []
    if deps:
        return block("Dependency", f"Unmet dependencies: {deps}")
    record(StageResult(name="Dependency", ok=True, detail="No unmet dependencies"))

    # --- Permission ---
    primary = resolved[0]
    mc = primary["mc"]
    tool = primary["tools"][0]
    level = work.autonomy_level
    max_level = int(mc["max_autonomy_level"])

    if level > max_level:
        return block(
            "Permission",
            f"Requested autonomy level {level} exceeds MC max {max_level}",
        )
    if level >= 3:
        return block("Permission", "LEVEL 3 never inferred; separate grant required")

    allowlists = list(tool["path_allowlist"]) + list(mc.get("path_allowlist", []))
    dest = force_destination or job.get("outputs", {}).get(
        "artifact_relpath", f"autonomy/runs/artifacts/{run_id}.json"
    ).replace("{run_id}", run_id)

    if not _path_allowed(dest, allowlists):
        return block("Permission", f"Destination outside allowlist: {dest}")

    # Ensure destination is under autonomy/runs
    if not dest.replace("\\", "/").startswith("autonomy/runs/"):
        return block("Permission", f"Destination outside autonomy/runs/: {dest}")

    record(
        StageResult(
            name="Permission",
            ok=True,
            detail="Autonomy level and path allowlist approved",
            data={
                "autonomy_level": level,
                "max_autonomy_level": max_level,
                "destination": dest,
            },
        )
    )

    # --- Execution ---
    try:
        artifact_abs = _tool_write_run_artifact(
            run_id=run_id,
            job_id=job_id,
            machine_capability_id=mc["id"],
            tool=tool,
            destination_relpath=dest,
        )
    except PermissionError as exc:
        return block("Execution", str(exc))
    except Exception as exc:  # noqa: BLE001 — surface as failed run
        record(StageResult(name="Execution", ok=False, detail=str(exc)))
        work.status = RunStatus.FAILED
        work.blocked_reason = str(exc)
        _persist(work, queue_dir, registry_dir, logs_dir)
        return work

    work.artifact_path = str(artifact_abs.relative_to(ROOT))
    record(
        StageResult(
            name="Execution",
            ok=True,
            detail="Tool write_run_artifact completed",
            data={"artifact_path": work.artifact_path, "adapter_id": primary["adapter"]["id"]},
        )
    )

    # --- Validation ---
    artifact = _load_json(artifact_abs)
    required_fields = job.get("validation", {}).get("required_artifact_fields", [])
    missing = [f for f in required_fields if f not in artifact]
    if missing:
        return block("Validation", f"Artifact missing fields: {missing}")
    if artifact.get("status") != "completed":
        return block("Validation", "Artifact status is not completed")

    record(
        StageResult(
            name="Validation",
            ok=True,
            detail="Artifact fields valid",
            data={"fields": required_fields},
        )
    )

    # --- State ---
    work.status = RunStatus.COMPLETED
    record(
        StageResult(
            name="State",
            ok=True,
            detail="Run status set to completed",
            data={"status": work.status.value},
        )
    )

    # --- Logs ---
    _assert_no_company_catalog_consultation(opened)
    record(
        StageResult(
            name="Logs",
            ok=True,
            detail="Audit trail persisted",
            data={"stages": list(STAGE_ORDER)},
        )
    )
    _persist(work, queue_dir, registry_dir, logs_dir)
    return work


def _persist(work: WorkItem, queue_dir: Path, registry_dir: Path, logs_dir: Path) -> None:
    payload = work.to_dict()
    payload["updated_at"] = _utc_now()
    _write_json(queue_dir / f"{work.work_id}.json", payload)
    _write_json(registry_dir / f"{work.run_id}.json", payload)
    log_path = logs_dir / f"{work.run_id}.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(payload, sort_keys=True) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SVOS Autonomy Kernel runner")
    parser.add_argument("job_id", help="Job ID to execute (e.g. job.prove_kernel_execution)")
    args = parser.parse_args(argv)
    work = run_job(args.job_id)
    print(json.dumps(work.to_dict(), indent=2, sort_keys=True))
    if work.status == RunStatus.COMPLETED:
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
