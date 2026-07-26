#!/usr/bin/env python3
"""Compile canonical SessionVue inputs into generated/sessionvue-os."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "compiler/contracts/sessionvue.compile.json"


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def frontmatter(title: str, object_type: str, *, status: str = "review", owner: str = "founder", **extra: Any) -> str:
    values: dict[str, Any] = {
        "title": title,
        "object_type": object_type,
        "status": status,
        "owner": owner,
        "updated": date.today().isoformat(),
        **extra,
    }
    lines = ["---"]
    for key, value in values.items():
        if isinstance(value, bool):
            value = str(value).lower()
        lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def copy_tree(source: Path, destination: Path) -> None:
    if not source.exists():
        raise SystemExit(f"Required input directory missing: {source}")
    shutil.copytree(source, destination, dirs_exist_ok=True)


def wiki(path: str, label: str | None = None) -> str:
    target = path[:-3] if path.endswith(".md") else path
    return f"[[{target}{'|' + label if label else ''}]]"


def render_job(system: dict[str, Any], job_name: str, index: int) -> str:
    job_id = f"{system['system_id']}-JOB-{index:03d}"
    return f"""{frontmatter(job_name, 'job', status='review', owner=system['owner'], job_id=job_id, governing_system=system['system_id'])}

# {job_name}

## Purpose

Execute the Executive responsibility named **{job_name}** using verified company sources and visible approval gates.

## Trigger

Manual founder request, scheduled Executive review, threshold breach, or routed Operations request.

## Owner

{system['owner']}

## Governing System

[[../00 Control Center/CONTROL CENTER|{system['name']}]]

## Project

The active Project that triggered the Job, when applicable.

## Inputs

- Active company priorities
- Relevant Project state
- Relevant Business System status
- Canonical company Knowledge
- Current metrics, risks, decisions, and approvals

## Required Sources

""" + "\n".join(f"- {wiki(source)}" for source in system["knowledge_sources"]) + """

## Preconditions

- Required sources exist.
- The request is within Executive scope.
- Material facts are verified.
- Founder approval requirements are known.

## Steps

1. Identify the objective and triggering Project or company condition.
2. Load canonical Knowledge and current system state.
3. Verify metrics, risks, open decisions, and dependencies.
4. Produce the Executive recommendation or review result.
5. Route execution work to Operations rather than performing department work directly.
6. Create an Approval or Decision record when required.
7. Update the Executive Control Center and affected registries.

## Decision Rules

- IF evidence is missing, THEN mark `NOT IN SOURCE` and stop the affected conclusion.
- IF the request belongs to a department, THEN route it through Operations.
- IF a locked founder decision conflicts, THEN create a visible Decision request.
- IF an external state change is required, THEN require Change Control and founder approval.

## Output

An Executive review, decision recommendation, priority directive, approval request, or company-health update.

## Destination

Executive System, active Project, Decision Registry, Approval Registry, or Operations routing queue.

## Quality Check

- Mission and vision alignment checked
- Canonical sources linked
- No unsupported claim
- Owner and next action explicit
- Execution correctly routed

## Approval

Founder approval is required for strategic changes, policies, resource-allocation changes, and final company-level decisions.

## Failure Handling

Record the blocker, owner, missing source, and exact next action. Do not infer approval.

## Retry Rule

Retry after the missing evidence, approval, or dependency becomes available.

## Completion

The Executive output is documented, routed, registered, and reflected in the Control Center.

## Lessons

Record founder corrections that should improve this Job.
"""


def render_metric(system: dict[str, Any], metric_name: str, index: int) -> str:
    metric_id = f"{system['system_id']}-MET-{index:03d}"
    return f"""{frontmatter(metric_name, 'metric', status='review', owner=system['owner'], metric_id=metric_id, governing_system=system['system_id'])}

# {metric_name}

## Definition

`NOT IN SOURCE — define the exact measurement.`

## Type

Executive system-health or outcome metric.

## System

[[../00 Control Center/CONTROL CENTER|{system['name']}]]

## Formula

`NOT IN SOURCE`

## Source

`NOT IN SOURCE`

## Cadence

`NOT IN SOURCE`

## Target

`NOT IN SOURCE`

## Warning

`NOT IN SOURCE`

## Failure

`NOT IN SOURCE`

## Owner

{system['owner']}

## Action

Route threshold breaches to Executive review, Monitoring, and the owning Business System.
"""


def render_automation(system: dict[str, Any], automation_name: str, index: int) -> str:
    automation_id = f"{system['system_id']}-AUTO-{index:03d}"
    return f"""{frontmatter(automation_name, 'automation', status='proposed', owner=system['owner'], automation_id=automation_id, governing_system=system['system_id'])}

# {automation_name}

## Purpose

Prepare or route the Executive process named **{automation_name}**.

## Governing System

[[../00 Control Center/CONTROL CENTER|{system['name']}]]

## Executed Job

`NOT IN SOURCE — link the approved Executive Job before activation.`

## Trigger

`NOT IN SOURCE`

## Inputs

Canonical Executive sources, current metrics, Project state, decisions, approvals, and system health.

## Tools

`NOT IN SOURCE`

## Credentials

Reference approved secret storage only. Never store values here.

## Allowed Reads

Approved vault sources and explicitly authorized connected systems.

## Allowed Writes

Drafts and vault records only until a founder-approved grant expands the boundary.

## Prohibited Actions

- Sending or publishing without approval
- Database or production writes without approval
- Permission expansion
- Secret storage
- Strategic decisions without founder approval

## Dry Run

Required.

## Approval Gate

Founder approval required before activation.

## Monitoring

`NOT IN SOURCE`

## Failure Handling

Stop, record the failure, and route to the Incident System.

## Retries

`NOT IN SOURCE`

## Rollback

`NOT IN SOURCE`

## Disable

`NOT IN SOURCE`

## Owner

{system['owner']}

## Status

Proposed; inactive.
"""


def compile_system(system_path: Path, business_root: Path, registries: dict[str, list[list[str]]]) -> None:
    system = load_json(system_path)
    required = ["system_id", "folder_name", "name", "owner", "purpose", "authority", "out_of_scope", "knowledge_sources", "jobs", "metrics", "automations"]
    missing = [field for field in required if field not in system]
    if missing:
        raise SystemExit(f"{system_path} missing fields: {', '.join(missing)}")

    root = business_root / system["folder_name"]
    folders = [
        "00 Control Center", "01 Charter", "02 Strategic Planning", "03 Company Priorities",
        "04 Decision Management", "05 Founder Approval", "06 Resource Allocation",
        "07 Cross-System Governance", "08 Risk Management", "09 Executive Reviews",
        "10 Company Health", "11 Metrics", "12 Jobs", "13 Automations", "14 Knowledge",
        "15 Decisions", "16 Improvements", "17 Archive"
    ]
    for folder in folders:
        (root / folder).mkdir(parents=True, exist_ok=True)

    source_links = "\n".join(f"- {wiki(source)}" for source in system["knowledge_sources"])
    connected = "\n".join(f"- {name}" for name in system.get("connected_systems", []))
    authority = "\n".join(f"- {item}" for item in system["authority"])
    out_scope = "\n".join(f"- {item}" for item in system["out_of_scope"])

    write(root / "00 Control Center/CONTROL CENTER.md", f"""{frontmatter(system['name'], 'business-system-control-center', status=system['status'], owner=system['owner'], system_id=system['system_id'], compiled='true')}

# {system['name']}

## Purpose

{system['purpose']}

## Current State

- Lifecycle: designed
- Operational status: ready for founder review
- Owner: {system['owner']}
- Automation level: 0
- Active projects: none connected
- Open approvals: see [[../05 Founder Approval/APPROVAL REGISTRY]]
- Open decisions: see [[../04 Decision Management/DECISION REGISTRY]]
- Current blocker: metrics and live integrations require founder configuration

## Authority

{authority}

## Connected Systems

{connected}

## Canonical Knowledge

{source_links}

## System Map

""" + "\n".join(f"- [[../{folder}/{folder.split(' ',1)[1].upper()}]]" for folder in folders[1:11]) + """
- [[../11 Metrics/METRIC REGISTRY]]
- [[../12 Jobs/JOB REGISTRY]]
- [[../13 Automations/AUTOMATION REGISTRY]]
- [[../14 Knowledge/KNOWLEDGE MAP]]
- [[../15 Decisions/DECISIONS]]
- [[../16 Improvements/IMPROVEMENTS]]
- [[../17 Archive/README]]

## Next Action

Founder reviews the Charter, then configures the first Executive metrics and activates the first Executive Job.
""")

    write(root / "01 Charter/CHARTER.md", f"""{frontmatter(f"{system['name']} Charter", 'business-system-charter', status=system['status'], owner=system['owner'], system_id=system['system_id'])}

# Charter

## Purpose

{system['purpose']}

## Authority

{authority}

## Out of Scope

{out_scope}

## Operating Boundary

Executive decides direction, priorities, company-level policies, and strategic approvals. Operations routes and orchestrates execution. Departments perform their specialized work.

## Success Condition

Company priorities are explicit, strategic decisions are documented, risks are visible, approvals are controlled, and execution is routed to the correct Business Systems.
""")

    section_files = {
        "02 Strategic Planning/STRATEGIC PLANNING.md": "Annual, quarterly, monthly, and weekly planning aligned to Mission and Vision.",
        "03 Company Priorities/COMPANY PRIORITIES.md": "The canonical ordered list of active company priorities and deferred initiatives.",
        "04 Decision Management/DECISION MANAGEMENT.md": "Govern company-level decision creation, evidence, approval, propagation, and review.",
        "05 Founder Approval/FOUNDER APPROVAL.md": "Govern all items requiring explicit founder approval.",
        "06 Resource Allocation/RESOURCE ALLOCATION.md": "Set resource direction across time, money, capacity, and strategic attention.",
        "07 Cross-System Governance/CROSS-SYSTEM GOVERNANCE.md": "Define how Executive aligns and resolves conflicts among Business Systems.",
        "08 Risk Management/RISK MANAGEMENT.md": "Identify, score, assign, monitor, and resolve material company risks.",
        "09 Executive Reviews/EXECUTIVE REVIEWS.md": "Define daily, weekly, monthly, quarterly, and annual Executive reviews.",
        "10 Company Health/COMPANY HEALTH.md": "Summarize strategic, product, operational, financial, customer, and technical health.",
    }
    for rel, purpose in section_files.items():
        title = Path(rel).stem.replace("_", " ").title()
        write(root / rel, f"""{frontmatter(title, 'business-system-component', status='review', owner=system['owner'], system_id=system['system_id'])}

# {title}

## Purpose

{purpose}

## Inputs

Current Projects, Business System state, canonical Knowledge, metrics, risks, decisions, and approvals.

## Workflow

```text
Collect
→ Verify
→ Review
→ Decide or Recommend
→ Route Through Operations
→ Record
→ Monitor
```

## Outputs

Visible Executive records, directives, approvals, decisions, risks, or review results.

## Completion

The record has an owner, source links, status, destination, and next action.
""")

    # Registries and index files
    write(root / "04 Decision Management/DECISION REGISTRY.md", "# Decision Registry\n\n| Decision ID | Title | Status | Owner | Record |\n|---|---|---|---|---|\n")
    write(root / "05 Founder Approval/APPROVAL REGISTRY.md", "# Approval Registry\n\n| Approval ID | Item | Status | Requested | Decision |\n|---|---|---|---|---|\n")

    job_rows = []
    for idx, job_name in enumerate(system["jobs"], 1):
        filename = f"{idx:03d} — {job_name}.md"
        write(root / "12 Jobs" / filename, render_job(system, job_name, idx))
        job_id = f"{system['system_id']}-JOB-{idx:03d}"
        job_rows.append(f"| {job_id} | {job_name} | review | [[{filename[:-3]}]] |")
        registries["jobs"].append([job_id, job_name, system["system_id"], "review", f"02 Business Systems/{system['folder_name']}/12 Jobs/{filename[:-3]}"])
    write(root / "12 Jobs/JOB REGISTRY.md", "# Job Registry\n\n| Job ID | Job | Status | File |\n|---|---|---|---|\n" + "\n".join(job_rows) + "\n")

    metric_rows = []
    for idx, metric_name in enumerate(system["metrics"], 1):
        filename = f"{idx:03d} — {metric_name}.md"
        write(root / "11 Metrics" / filename, render_metric(system, metric_name, idx))
        metric_id = f"{system['system_id']}-MET-{idx:03d}"
        metric_rows.append(f"| {metric_id} | {metric_name} | review | [[{filename[:-3]}]] |")
        registries["metrics"].append([metric_id, metric_name, system["system_id"], "review", f"02 Business Systems/{system['folder_name']}/11 Metrics/{filename[:-3]}"])
    write(root / "11 Metrics/METRIC REGISTRY.md", "# Metric Registry\n\n| Metric ID | Metric | Status | File |\n|---|---|---|---|\n" + "\n".join(metric_rows) + "\n")

    automation_rows = []
    for idx, automation_name in enumerate(system["automations"], 1):
        filename = f"{idx:03d} — {automation_name}.md"
        write(root / "13 Automations" / filename, render_automation(system, automation_name, idx))
        auto_id = f"{system['system_id']}-AUTO-{idx:03d}"
        automation_rows.append(f"| {auto_id} | {automation_name} | proposed | [[{filename[:-3]}]] |")
        registries["automations"].append([auto_id, automation_name, system["system_id"], "proposed", f"02 Business Systems/{system['folder_name']}/13 Automations/{filename[:-3]}"])
    write(root / "13 Automations/AUTOMATION REGISTRY.md", "# Automation Registry\n\n| Automation ID | Automation | Status | File |\n|---|---|---|---|\n" + "\n".join(automation_rows) + "\n")

    write(root / "14 Knowledge/KNOWLEDGE MAP.md", f"{frontmatter('Executive Knowledge Map', 'knowledge-map', status='review', owner=system['owner'], system_id=system['system_id'])}\n\n# Knowledge Map\n\n{source_links}\n")
    write(root / "15 Decisions/DECISIONS.md", f"{frontmatter('Executive Decisions', 'decision-index', status='review', owner=system['owner'], system_id=system['system_id'])}\n\n# Approved Executive Decisions\n\nApproved Decision records are linked here.\n")
    write(root / "16 Improvements/IMPROVEMENTS.md", f"{frontmatter('Executive System Improvements', 'improvement-index', status='review', owner=system['owner'], system_id=system['system_id'])}\n\n# Executive System Improvements\n\n| Improvement | Source | Status | Decision |\n|---|---|---|---|\n")
    write(root / "17 Archive/README.md", "# Executive Archive\n\nSuperseded Executive records are archived here and never silently deleted.\n")

    registries["systems"].append([system["system_id"], system["name"], system["status"], system["owner"], f"02 Business Systems/{system['folder_name']}/00 Control Center/CONTROL CENTER"])


def render_global_registries(output: Path, registries: dict[str, list[list[str]]]) -> None:
    reg_root = output / "06 Registry"
    reg_root.mkdir(parents=True, exist_ok=True)
    specs = {
        "Business System Registry.md": ("system_id", "name", "status", "owner", "control_center", registries["systems"]),
        "Job Registry.md": ("job_id", "name", "system", "status", "file", registries["jobs"]),
        "Metric Registry.md": ("metric_id", "name", "system", "status", "file", registries["metrics"]),
        "Automation Registry.md": ("automation_id", "name", "system", "status", "file", registries["automations"]),
    }
    for filename, spec in specs.items():
        *headers, rows = spec
        table = "|" + "|".join(headers) + "|\n|" + "|".join(["---"] * len(headers)) + "|\n"
        table += "\n".join("|" + "|".join(row) + "|" for row in rows)
        write(reg_root / filename, f"{frontmatter(Path(filename).stem, 'registry', status='review', owner='founder', compiled='true')}\n\n# {Path(filename).stem}\n\n{table}\n")


def validate_output(output: Path) -> dict[str, Any]:
    markdown = list(output.rglob("*.md"))
    no_frontmatter = []
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        # Generated registries/readmes may intentionally be plain markdown.
        if path.name not in {"README.md", "DECISION REGISTRY.md", "APPROVAL REGISTRY.md", "JOB REGISTRY.md", "METRIC REGISTRY.md", "AUTOMATION REGISTRY.md"} and not text.startswith("---\n"):
            no_frontmatter.append(str(path.relative_to(output)))
    required = [
        output / "02 Business Systems/001 Executive System/00 Control Center/CONTROL CENTER.md",
        output / "02 Business Systems/001 Executive System/01 Charter/CHARTER.md",
        output / "06 Registry/Business System Registry.md",
    ]
    missing = [str(path.relative_to(output)) for path in required if not path.exists()]
    return {
        "markdown_files": len(markdown),
        "missing_required": missing,
        "files_without_expected_frontmatter": no_frontmatter,
        "passed": not missing and not no_frontmatter,
    }


def tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        digest.update(str(path.relative_to(root)).encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Validate inputs and show intended output without writing it.")
    parser.add_argument("--no-clean", action="store_true", help="Do not remove the existing generated output first.")
    args = parser.parse_args()

    contract = load_json(CONTRACT_PATH)
    input_root = ROOT / contract["input_root"]
    output = ROOT / contract["output_root"]
    systems_root = input_root / contract["systems_root"]
    system_files = sorted(systems_root.glob("*.system.json"))
    if not system_files:
        raise SystemExit(f"No system definitions found in {systems_root}")

    for item in contract["copy_inputs"]:
        source = input_root / item["from"]
        if not source.exists():
            raise SystemExit(f"Missing required compiler input: {source}")

    if args.dry_run:
        print(json.dumps({
            "contract": str(CONTRACT_PATH.relative_to(ROOT)),
            "company": contract["company_id"],
            "systems": [path.name for path in system_files],
            "output": str(output.relative_to(ROOT)),
            "would_clean": contract["clean_output_before_compile"] and not args.no_clean,
        }, indent=2))
        return 0

    if output.exists() and contract["clean_output_before_compile"] and not args.no_clean:
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    for item in contract["copy_inputs"]:
        copy_tree(input_root / item["from"], output / item["to"])

    registries: dict[str, list[list[str]]] = {"systems": [], "jobs": [], "metrics": [], "automations": []}
    business_root = output / contract["generated_business_systems_root"]
    for system_file in system_files:
        compile_system(system_file, business_root, registries)
    render_global_registries(output, registries)

    validation = validate_output(output)
    metadata = {
        "company": contract["company_id"],
        "contract_version": contract["contract_version"],
        "compiled_at": datetime.now(timezone.utc).isoformat(),
        "source_contract": str(CONTRACT_PATH.relative_to(ROOT)),
        "systems": [path.name for path in system_files],
        "validation": validation,
        "output_sha256": tree_hash(output),
    }
    write(output / "BUILD METADATA.json", json.dumps(metadata, indent=2))
    report = [
        "# Compile Validation Report", "",
        f"- Passed: {validation['passed']}",
        f"- Markdown files: {validation['markdown_files']}",
        f"- Missing required: {len(validation['missing_required'])}",
        f"- Unexpected missing frontmatter: {len(validation['files_without_expected_frontmatter'])}",
    ]
    if validation["missing_required"]:
        report += ["", "## Missing Required"] + [f"- `{item}`" for item in validation["missing_required"]]
    if validation["files_without_expected_frontmatter"]:
        report += ["", "## Missing Frontmatter"] + [f"- `{item}`" for item in validation["files_without_expected_frontmatter"]]
    write(output / "COMPILE VALIDATION.md", "\n".join(report))

    if not validation["passed"]:
        print(json.dumps(metadata, indent=2))
        return 1
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
