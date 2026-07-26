#!/usr/bin/env python3
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
output = root / "generated/sessionvue-os"
metadata = output / "BUILD METADATA.json"
if not metadata.exists():
    print("Generated output is missing. Run: python3 scripts/compile_sessionvue.py")
    sys.exit(1)
data = json.loads(metadata.read_text(encoding="utf-8"))
print(json.dumps(data["validation"], indent=2))
sys.exit(0 if data["validation"].get("passed") else 1)
