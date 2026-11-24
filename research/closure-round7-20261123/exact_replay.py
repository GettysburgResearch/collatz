#!/usr/bin/env python3
"""Run all round-seven exact controls and bind their scientific inputs."""

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
INPUTS = (
    "FINITE_JET_BOUND.md", "GERM_CONSTRUCTION.md", "ORDINARY_DESCENT.md",
    "SOURCE_TRANSFER.md", "GermConstruction.lean", "detector_controls.py",
    "germ_controls.py", "descent_controls.py", "transfer_controls.py",
    "exact_replay.py",
)


def run_checks() -> dict:
    bindings = {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in INPUTS}
    results = {}
    for lane in ("detector", "germ", "descent", "transfer"):
        name = lane + "_controls"
        spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
        if spec is None or spec.loader is None:
            raise RuntimeError("cannot load exact control: " + name)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        result = module.run_checks()
        if str(result.get("status")).lower() != "pass":
            raise RuntimeError("control failed: " + name)
        results[lane] = result
    for name, digest in bindings.items():
        if sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError("source changed during execution: " + name)
    return {
        "success": True,
        "scope": "selected exact finite controls, not a universal Collatz proof or an all-order computation",
        "source_sha256": bindings,
        **results,
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
