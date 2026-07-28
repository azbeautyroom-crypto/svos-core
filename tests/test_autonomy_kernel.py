"""End-to-end proof that Kernel v1.0 executes one Job safely."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

from autonomy.kernel.models import STAGE_ORDER, RunStatus
from autonomy.kernel.runner import run_job


@pytest.fixture()
def isolated_runs(tmp_path):
    """Point runner persistence at a temp runs directory."""
    runs = tmp_path / "runs"
    for name in ("queue", "registry", "logs", "artifacts"):
        (runs / name).mkdir(parents=True)
    return runs


def _stage_names(work):
    return [s.name for s in work.stages]


def test_complete_job_through_all_stages(isolated_runs):
    work = run_job("job.prove_kernel_execution", runs_root=isolated_runs)

    assert work.status == RunStatus.COMPLETED
    assert work.blocked_reason is None
    assert _stage_names(work) == list(STAGE_ORDER)
    assert all(s.ok for s in work.stages)

    artifact = ROOT / work.artifact_path
    assert artifact.is_file()
    payload = json.loads(artifact.read_text(encoding="utf-8"))
    assert payload["job_id"] == "job.prove_kernel_execution"
    assert payload["machine_capability_id"] == "mc.write_autonomy_run_record"
    assert payload["status"] == "completed"
    assert "run_id" in payload
    assert "completed_at" in payload

    registry = isolated_runs / "registry" / f"{work.run_id}.json"
    assert registry.is_file()
    log = isolated_runs / "logs" / f"{work.run_id}.jsonl"
    assert log.is_file()


def test_kill_switch_blocks(isolated_runs):
    work = run_job(
        "job.prove_kernel_execution",
        runs_root=isolated_runs,
        kill_switch_override={"enabled": False, "reason": "test"},
    )
    assert work.status == RunStatus.BLOCKED
    assert work.blocked_reason and "Kill switch" in work.blocked_reason
    assert "Eligibility" in _stage_names(work)
    assert "Execution" not in _stage_names(work)


def test_unknown_machine_capability_blocks(isolated_runs):
    work = run_job(
        "job.prove_kernel_execution",
        runs_root=isolated_runs,
        override_machine_capabilities=["mc.does_not_exist"],
    )
    assert work.status == RunStatus.BLOCKED
    assert "Unknown Machine Capability" in (work.blocked_reason or "")
    assert "MachineCapabilityResolution" in _stage_names(work)
    assert "Execution" not in _stage_names(work)


def test_path_outside_allowlist_denied(isolated_runs):
    work = run_job(
        "job.prove_kernel_execution",
        runs_root=isolated_runs,
        force_destination="tmp/illegal-write.json",
    )
    assert work.status == RunStatus.BLOCKED
    assert work.blocked_reason
    assert "allowlist" in work.blocked_reason.lower() or "outside" in work.blocked_reason.lower()
    assert "Execution" not in _stage_names(work) or not any(
        s.name == "Execution" and s.ok for s in work.stages
    )


def test_unmet_dependency_blocks(isolated_runs, monkeypatch):
    import autonomy.kernel.runner as runner

    real_load = runner._load_json

    def load_with_dependency(path):
        data = real_load(path)
        if path.name == "prove_kernel_execution.json":
            data = dict(data)
            data["dependencies"] = ["job.missing_prerequisite"]
        return data

    monkeypatch.setattr(runner, "_load_json", load_with_dependency)
    work = run_job("job.prove_kernel_execution", runs_root=isolated_runs)
    assert work.status == RunStatus.BLOCKED
    assert "Unmet dependencies" in (work.blocked_reason or "")
    assert "Dependency" in _stage_names(work)
    assert "Execution" not in _stage_names(work)


def test_validation_failure_blocks(isolated_runs, monkeypatch):
    import autonomy.kernel.runner as runner

    def write_incomplete_artifact(*, run_id, job_id, machine_capability_id, tool, destination_relpath=None):
        relpath = destination_relpath or f"autonomy/runs/artifacts/{run_id}.json"
        abs_path = ROOT / relpath
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        # Omit required fields so Validation must block.
        abs_path.write_text(
            json.dumps({"run_id": run_id, "status": "completed"}, indent=2) + "\n",
            encoding="utf-8",
        )
        return abs_path

    monkeypatch.setattr(runner, "_tool_write_run_artifact", write_incomplete_artifact)
    work = run_job("job.prove_kernel_execution", runs_root=isolated_runs)
    assert work.status == RunStatus.BLOCKED
    assert "Artifact missing fields" in (work.blocked_reason or "")
    assert "Validation" in _stage_names(work)
    validation = next(s for s in work.stages if s.name == "Validation")
    assert validation.ok is False


def test_company_capability_never_consulted(isolated_runs):
    """Runner must not open Company Capability / Company Asset catalog paths."""
    opened: list[str] = []
    real_read_text = Path.read_text

    def tracking_read_text(self, *args, **kwargs):
        opened.append(str(self))
        return real_read_text(self, *args, **kwargs)

    Path.read_text = tracking_read_text  # type: ignore[method-assign]
    try:
        work = run_job("job.prove_kernel_execution", runs_root=isolated_runs)
        assert work.status == RunStatus.COMPLETED
    finally:
        Path.read_text = real_read_text  # type: ignore[method-assign]

    forbidden = (
        "company capability",
        "company asset",
        "company-capability",
        "company_capability",
        "company-asset",
        "company_asset",
        "business capability",
    )
    for path in opened:
        lower = path.lower().replace(" ", "-")
        for fragment in forbidden:
            assert fragment.replace(" ", "-") not in lower, f"Consulted forbidden path: {path}"
