from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"

OBJECTS = {
    "business-system": {
        "id": "TPL-BS-001",
        "object_type": "business-system",
        "name": "Business System",
        "folders": [
            "00 Control Center",
            "01 Purpose",
            "02 Scope",
            "03 Policies",
            "04 Workflows",
            "05 Jobs",
            "06 Templates",
            "07 Metrics",
            "08 Automations",
            "09 Integrations",
            "10 Knowledge",
            "11 Decisions",
            "12 Improvements",
            "13 Archive",
        ],
        "sections": [
            "Identity",
            "Purpose",
            "Outcome",
            "Owner",
            "Scope",
            "Out of Scope",
            "Customers",
            "Dependencies",
            "Policies",
            "Workflows",
            "Jobs",
            "Outputs",
            "Metrics",
            "Automations",
            "Integrations",
            "Knowledge",
            "Decisions",
            "Exceptions",
            "Improvement Loop",
            "Completion Conditions",
        ],
    },
    "project": {
        "id": "TPL-PRJ-001",
        "object_type": "project",
        "name": "Project",
        "sections": [
            "Project Identity",
            "Objective",
            "Business Outcome",
            "Owning Business System",
            "Supporting Business Systems",
            "Activated Universal Systems",
            "Required Jobs",
            "Required Knowledge",
            "Scope",
            "Out of Scope",
            "Deliverables",
            "Dependencies",
            "Timeline",
            "Execution",
            "Approvals",
            "Metrics",
            "Risks and Exceptions",
            "Decisions",
            "Documentation Updates",
            "Completion Checklist",
            "Next Action",
        ],
    },
    "job": {
        "id": "TPL-JOB-001",
        "object_type": "job",
        "name": "Job",
        "sections": [
            "Purpose",
            "Trigger",
            "Owner",
            "Governing System",
            "Project",
            "Inputs",
            "Required Sources",
            "Preconditions",
            "Steps",
            "Decision Rules",
            "Output",
            "Destination",
            "Quality Check",
            "Approval Requirement",
            "Failure Handling",
            "Retry Rule",
            "Completion Condition",
            "Lessons",
        ],
    },
    "workflow": {
        "id": "TPL-WF-001",
        "object_type": "workflow",
        "name": "Workflow",
        "sections": [
            "Purpose",
            "Entry Condition",
            "Exit Condition",
            "Stages",
            "Allowed Transitions",
            "Owners by Stage",
            "Required Inputs",
            "Required Outputs",
            "Decision Gates",
            "Approval Gates",
            "Exceptions",
            "Metrics",
        ],
    },
    "automation": {
        "id": "TPL-AUTO-001",
        "object_type": "automation",
        "name": "Automation",
        "sections": [
            "Purpose",
            "Governing System",
            "Executed Job",
            "Trigger",
            "Inputs",
            "Tools",
            "Credential References",
            "Allowed Reads",
            "Allowed Writes",
            "Prohibited Actions",
            "Dry Run",
            "Approval Gate",
            "Monitoring",
            "Failure Handling",
            "Maximum Retries",
            "Rollback",
            "Disable Procedure",
            "Owner",
            "Status",
        ],
    },
    "registry": {
        "id": "TPL-REG-001",
        "object_type": "registry",
        "name": "Registry",
        "sections": [
            "Purpose",
            "Authority",
            "Owner",
            "Object Type",
            "Required Fields",
            "Entry Rules",
            "Update Rules",
            "Conflict Rules",
            "Archive Rules",
            "Validation",
        ],
    },
    "control-center": {
        "id": "TPL-CC-001",
        "object_type": "control-center",
        "name": "Control Center",
        "sections": [
            "System Identity",
            "Purpose",
            "Current Status",
            "Owner",
            "Active Projects",
            "Active Jobs",
            "Open Approvals",
            "Blocked Items",
            "Primary Metrics",
            "Automation Health",
            "Dependencies",
            "Recent Decisions",
            "Last Review",
            "Next Action",
        ],
    },
    "decision": {
        "id": "TPL-DEC-001",
        "object_type": "decision",
        "name": "Decision",
        "sections": [
            "Decision ID",
            "Issue",
            "Evidence",
            "Options",
            "Recommendation",
            "Founder Decision",
            "Rationale",
            "Affected Objects",
            "Files to Update",
            "Revisit Trigger",
        ],
    },
}

README = """# SVOS Template Library

Version: 1.0.0
Status: LOCKED

Templates define the structure of generated SVOS Objects.

Generated Objects must compile from these templates.

Do not manually alter generated Objects to change structure.

Improve the template, validate it, version it, and regenerate.
"""

def frontmatter(template_id: str, object_type: str) -> str:
    return f"""---
template_id: {template_id}
object_type: template
generates: {object_type}
template_version: 1.0.0
os_version: 1.0.0
spec_version: 1.0.0
status: locked
owner: founder
---

"""

def build_template(name: str, config: dict) -> str:
    lines = [
        frontmatter(config["id"], config["object_type"]),
        f"# {{{{ object_name }}}}",
        "",
        f"Object Type: `{config['object_type']}`",
        "Version: `{{ object_version }}`",
        "Status: `{{ status }}`",
        "",
    ]

    for section in config["sections"]:
        key = (
            section.lower()
            .replace(" and ", "_")
            .replace(" ", "_")
            .replace("-", "_")
        )
        lines.extend([
            f"## {section}",
            "",
            f"{{{{ {key} }}}}",
            "",
        ])

    return "\n".join(lines).rstrip() + "\n"

def build_manifest(config: dict) -> str:
    folders = config.get("folders", [])
    folder_yaml = "\n".join(f"  - {folder}" for folder in folders) or "  []"

    return f"""template_id: {config["id"]}
name: {config["name"]}
object_type: {config["object_type"]}
template_version: 1.0.0
os_version: 1.0.0
spec_version: 1.0.0
status: locked
owner: founder
required_files:
  - template.md
required_folders:
{folder_yaml}
validation:
  yaml_required: true
  owner_required: true
  source_of_truth_required: true
  version_metadata_required: true
  registry_entry_required: true
"""

def main() -> None:
    TEMPLATES.mkdir(parents=True, exist_ok=True)
    (TEMPLATES / "README.md").write_text(README, encoding="utf-8")

    for folder_name, config in OBJECTS.items():
        folder = TEMPLATES / folder_name
        folder.mkdir(parents=True, exist_ok=True)

        (folder / "template.md").write_text(
            build_template(folder_name, config),
            encoding="utf-8",
        )

        (folder / "manifest.yaml").write_text(
            build_manifest(config),
            encoding="utf-8",
        )

    print(f"Built {len(OBJECTS)} template packages in {TEMPLATES}")

if __name__ == "__main__":
    main()
