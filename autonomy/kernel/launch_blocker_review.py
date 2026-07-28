"""Deterministic Launch Blocker Review report builder.

Reads only in-repo canonical inputs. Never invents blockers.
Active Priorities is vault-only → NOT IN SOURCE.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

# Fixed relative paths under the repository root.
SOURCES: dict[str, str] = {
    "landing_page_project": "inputs/sessionvue/projects/Landing Page (Waitlist Website).md",
    "gtm_project": "inputs/sessionvue/projects/Pre-Launch Go-to-Market.md",
    "integration_brain": "inputs/sessionvue/company-brain/Integrations/Integration Brain.md",
    "product_brain": "inputs/sessionvue/company-brain/Products/Product Brain.md",
    "product_implementation_audit": "inputs/sessionvue/company-brain/Products/Product Implementation Audit.md",
    "founder_directives": "inputs/sessionvue/company-brain/Company/Founder Directives.md",
}


def _read(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _section(text: str, heading: str) -> str:
    pattern = rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


def _bullet_lines(section_text: str) -> list[str]:
    lines: list[str] = []
    for raw in section_text.splitlines():
        line = raw.strip()
        if line.startswith("- "):
            lines.append(line[2:].strip())
    return lines


def _verbatim_status(text: str) -> dict[str, str]:
    status: dict[str, str] = {}
    for key in ("project_status", "next_action"):
        match = re.search(rf"(?m)^- {key}:\s*\*\*(.+?)\*\*\s*$", text)
        if match:
            status[key] = match.group(1).strip()
        else:
            status[key] = "NOT IN SOURCE"
    return status


def _directive_rows(text: str, names: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for name in names:
        match = re.search(
            rf"(?m)^\|\s*{re.escape(name)}\s*\|\s*([^|]+)\|\s*([^|]+)\|",
            text,
        )
        if match:
            rows.append(
                {
                    "directive": name,
                    "ruling": match.group(1).strip(),
                    "locked": match.group(2).strip(),
                }
            )
        else:
            rows.append(
                {
                    "directive": name,
                    "ruling": "NOT IN SOURCE",
                    "locked": "NOT IN SOURCE",
                }
            )
    return rows


def build_launch_blocker_report() -> dict[str, Any]:
    """Build a deterministic report body from canonical inputs."""
    loaded: dict[str, str] = {}
    source_meta: list[dict[str, str]] = []
    for key, relpath in sorted(SOURCES.items()):
        text = _read(relpath)
        loaded[key] = text
        source_meta.append(
            {
                "id": key,
                "path": relpath,
                "sha256": _sha256(text),
            }
        )

    landing = loaded["landing_page_project"]
    gtm = loaded["gtm_project"]
    integration = loaded["integration_brain"]
    directives = loaded["founder_directives"]

    blockers: list[dict[str, str]] = []
    for source_id, text, label in (
        ("landing_page_project", landing, "Landing Page (Waitlist Website)"),
        ("gtm_project", gtm, "Pre-Launch Go-to-Market"),
    ):
        for item in _bullet_lines(_section(text, "Dependencies / Blockers")):
            blockers.append(
                {
                    "source_id": source_id,
                    "source_title": label,
                    "blocker": item,
                }
            )

    # Integration Brain: sending domain Heat 5 gap (verbatim excerpt).
    domain_match = re.search(
        r"(?m)^- Sending domain:\s*(.+)$",
        integration,
    )
    blockers.append(
        {
            "source_id": "integration_brain",
            "source_title": "Integration Brain",
            "blocker": (
                f"Sending domain: {domain_match.group(1).strip()}"
                if domain_match
                else "Sending domain: NOT IN SOURCE"
            ),
        }
    )

    # Stable ordering for identical inputs → identical report body.
    blockers = sorted(
        blockers,
        key=lambda row: (row["source_id"], row["blocker"]),
    )

    report: dict[str, Any] = {
        "job": "job.launch_blocker_review",
        "title": "Launch Blocker Review",
        "active_priorities": {
            "status": "NOT IN SOURCE",
            "path": "HQ/Active Priorities.md",
            "note": "Vault-only; not mirrored into svos-core inputs.",
        },
        "sources": source_meta,
        "projects": {
            "landing_page": {
                "path": SOURCES["landing_page_project"],
                **_verbatim_status(landing),
                "open_items": _bullet_lines(_section(landing, "Open Items")),
            },
            "gtm": {
                "path": SOURCES["gtm_project"],
                **_verbatim_status(gtm),
            },
        },
        "blockers": blockers,
        "founder_directives": _directive_rows(
            directives,
            ["One launch event", "Waitlist RLS"],
        ),
        "product_inputs": {
            "product_brain_path": SOURCES["product_brain"],
            "product_brain_sha256": next(
                s["sha256"] for s in source_meta if s["id"] == "product_brain"
            ),
            "product_implementation_audit_path": SOURCES["product_implementation_audit"],
            "product_implementation_audit_sha256": next(
                s["sha256"]
                for s in source_meta
                if s["id"] == "product_implementation_audit"
            ),
            "note": (
                "Product Brain = intent only. Product Implementation Audit = gaps. "
                "This Job does not rank Audit gaps as launch blockers."
            ),
        },
    }
    return report
