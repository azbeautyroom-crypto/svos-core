"""Autonomy kernel data models."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class RunStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"


STAGE_ORDER = (
    "Trigger",
    "Queue",
    "MachineCapabilityResolution",
    "Eligibility",
    "Dependency",
    "Permission",
    "Execution",
    "Validation",
    "State",
    "Logs",
)


@dataclass
class StageResult:
    name: str
    ok: bool
    detail: str = ""
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkItem:
    work_id: str
    job_id: str
    run_id: str
    status: RunStatus = RunStatus.QUEUED
    autonomy_level: int = 0
    stages: list[StageResult] = field(default_factory=list)
    blocked_reason: str | None = None
    artifact_path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "work_id": self.work_id,
            "job_id": self.job_id,
            "run_id": self.run_id,
            "status": self.status.value,
            "autonomy_level": self.autonomy_level,
            "blocked_reason": self.blocked_reason,
            "artifact_path": self.artifact_path,
            "stages": [
                {
                    "name": s.name,
                    "ok": s.ok,
                    "detail": s.detail,
                    "data": s.data,
                }
                for s in self.stages
            ],
        }
