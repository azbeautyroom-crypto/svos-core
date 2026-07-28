"""Production Job: Launch Blocker Review through Kernel v1.0."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

from autonomy.kernel.models import STAGE_ORDER, RunStatus
from autonomy.kernel.runner import run_job


@pytest.fixture()
def isolated_runs(tmp_path):
    runs = tmp_path / "runs"
    for name in ("queue", "registry", "logs", "artifacts", "reports"):
        (runs / name).mkdir(parents=True)
    return runs


def _stage_names(work):
    return [s.name for s in work.stages]


def test_launch_blocker_review_full_runtime_path(isolated_runs):
    work = run_job("job.launch_blocker_review", runs_root=isolated_runs)

    assert work.status == RunStatus.COMPLETED
    assert _stage_names(work) == list(STAGE_ORDER)
    assert all(s.ok for s in work.stages)

    artifact = ROOT / work.artifact_path
    assert artifact.is_file()
    assert work.artifact_path.startswith("autonomy/runs/")
    payload = json.loads(artifact.read_text(encoding="utf-8"))
    assert payload["job_id"] == "job.launch_blocker_review"
    assert payload["machine_capability_id"] == "mc.write_launch_blocker_review"
    assert payload["status"] == "completed"
    report = payload["report"]
    assert report["title"] == "Launch Blocker Review"
    assert report["active_priorities"]["status"] == "NOT IN SOURCE"
    assert isinstance(report["blockers"], list) and len(report["blockers"]) >= 1
    assert any("Sending domain" in b["blocker"] for b in report["blockers"])

    assert (isolated_runs / "queue" / f"{work.work_id}.json").is_file()
    assert (isolated_runs / "registry" / f"{work.run_id}.json").is_file()
    assert (isolated_runs / "logs" / f"{work.run_id}.jsonl").is_file()

    registry = json.loads(
        (isolated_runs / "registry" / f"{work.run_id}.json").read_text(encoding="utf-8")
    )
    # Run Registry stage list is execution evidence, not a Decision Log.
    assert [s["name"] for s in registry["stages"]] == list(STAGE_ORDER)


def test_launch_blocker_review_deterministic(isolated_runs):
    first = run_job("job.launch_blocker_review", runs_root=isolated_runs)
    second = run_job("job.launch_blocker_review", runs_root=isolated_runs)
    assert first.status == RunStatus.COMPLETED
    assert second.status == RunStatus.COMPLETED

    report_a = json.loads((ROOT / first.artifact_path).read_text(encoding="utf-8"))["report"]
    report_b = json.loads((ROOT / second.artifact_path).read_text(encoding="utf-8"))["report"]
    assert report_a == report_b


def test_launch_blocker_review_kill_switch(isolated_runs):
    work = run_job(
        "job.launch_blocker_review",
        runs_root=isolated_runs,
        kill_switch_override={"enabled": False, "reason": "test"},
    )
    assert work.status == RunStatus.BLOCKED
    assert "Kill switch" in (work.blocked_reason or "")
    assert "Execution" not in _stage_names(work)
