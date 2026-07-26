import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_compile_dry_run():
    result = subprocess.run([sys.executable, str(ROOT / "scripts/compile_sessionvue.py"), "--dry-run"], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert "executive.system.json" in data["systems"]


def test_compile_output():
    result = subprocess.run([sys.executable, str(ROOT / "scripts/compile_sessionvue.py")], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    expected = ROOT / "generated/sessionvue-os/02 Business Systems/001 Executive System/00 Control Center/CONTROL CENTER.md"
    assert expected.exists()
