"""Compile smoke + regression tests for the generic (folder-object-model) compiler.

Covers every compiled Business System (not just Executive):
- dry-run and full compile succeed
- each system's Control Center + Charter exist
- generated folder anatomy == the system input's declared `folders`
- jobs/metrics/automations counts and placement in their role folders
- global registries include every system
- knowledge-source resolution (present / referenced-external / NOT IN SOURCE)
- byte-identical golden regression per system (dates normalized so it survives across days)
- validate_output detects missing required artifacts (negative test)

Runnable with pytest, or directly via the project's function-runner harness.
"""
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated/sessionvue-os"
BSROOT = OUT / "02 Business Systems"
SYS_INPUTS = ROOT / "inputs/sessionvue/systems"
GOLDENS = Path(__file__).resolve().parent / "goldens"

_compiled = False


def _compile():
    global _compiled
    if _compiled:
        return
    result = subprocess.run([sys.executable, str(ROOT / "scripts/compile_sessionvue.py")], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    _compiled = True


def _systems():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(SYS_INPUTS.glob("*.system.json"))]


def _sys_dir(system):
    return BSROOT / system["folder_name"]


def _role_folder(system, role):
    for folder in system["folders"]:
        if folder.get("role") == role:
            return folder["id"]
    return None


def _normalize(text):
    # The only nondeterministic content in a system subtree is the frontmatter date.
    return re.sub(r"(?m)^updated: \d{4}-\d{2}-\d{2}$", "updated: <DATE>", text)


def _subtree_hashes(root):
    out = {}
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        out[rel] = hashlib.sha256(_normalize(path.read_text(encoding="utf-8")).encode()).hexdigest()
    return out


def _golden_file(system):
    return GOLDENS / (system["folder_name"].split(" ", 1)[0] + ".sha")


def _load_golden(path):
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        sha, rel = line.split("  ", 1)
        result[rel] = sha
    return result


# ---- tests ----

def test_compile_dry_run():
    result = subprocess.run([sys.executable, str(ROOT / "scripts/compile_sessionvue.py"), "--dry-run"], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert "executive.system.json" in data["systems"]


def test_compile_output():
    _compile()
    assert (BSROOT / "001 Executive System/00 Control Center/CONTROL CENTER.md").exists()


def test_all_systems_control_center_and_charter():
    _compile()
    for system in _systems():
        base = _sys_dir(system)
        assert (base / "00 Control Center/CONTROL CENTER.md").exists(), system["name"]
        assert (base / "01 Charter/CHARTER.md").exists(), system["name"]


def test_folder_anatomy_matches_input():
    _compile()
    for system in _systems():
        generated = sorted(p.name for p in _sys_dir(system).iterdir() if p.is_dir())
        declared = sorted(folder["id"] for folder in system["folders"])
        assert generated == declared, (system["name"], generated, declared)


def test_jobs_metrics_automations_placement():
    _compile()
    for system in _systems():
        base = _sys_dir(system)
        for role in ("jobs", "metrics", "automations"):
            folder = _role_folder(system, role)
            assert folder, (system["name"], role)
            count = sum(1 for p in (base / folder).glob("*.md") if re.match(r"\d{3} — ", p.name))
            assert count == len(system[role]), (system["name"], role, count, len(system[role]))


def test_global_registries_include_all_systems():
    _compile()
    bsr = (OUT / "06 Registry/Business System Registry.md").read_text(encoding="utf-8")
    jr = (OUT / "06 Registry/Job Registry.md").read_text(encoding="utf-8")
    for system in _systems():
        assert system["system_id"] in bsr, system["system_id"]
        assert system["system_id"] in jr, system["system_id"]


def test_knowledge_source_resolution():
    _compile()
    for system in _systems():
        for src in system["knowledge_sources"]:
            if isinstance(src, str):
                assert (OUT / src).exists(), (system["name"], src)
            else:
                status = src.get("status")
                assert status in ("present", "referenced-external", "NOT IN SOURCE"), (system["name"], src)
                if status == "present":
                    assert (OUT / src["path"]).exists(), (system["name"], src["path"])


def test_golden_parity():
    _compile()
    for system in _systems():
        golden_file = _golden_file(system)
        assert golden_file.exists(), f"missing golden {golden_file.name}"
        current = _subtree_hashes(_sys_dir(system))
        golden = _load_golden(golden_file)
        added = sorted(set(current) - set(golden))
        removed = sorted(set(golden) - set(current))
        changed = sorted(k for k in current if k in golden and current[k] != golden[k])
        assert not (added or removed or changed), (system["name"], {"added": added, "removed": removed, "changed": changed})


def test_validate_output_detects_missing_required():
    spec = importlib.util.spec_from_file_location("compmod", ROOT / "scripts/compile_sessionvue.py")
    comp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(comp)
    with tempfile.TemporaryDirectory() as td:
        result = comp.validate_output(Path(td))
        assert not result["passed"]
        assert result["missing_required"]
