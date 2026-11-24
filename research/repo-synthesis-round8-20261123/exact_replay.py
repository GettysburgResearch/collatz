#!/usr/bin/env python3
"""Execute the four round-eight exact control lanes and bind their inputs."""

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
INPUTS = (
    "README.md", "REPO_SYNTHESIS.md", "SOURCES.json", "GERM_BRIDGE.md",
    "SCALAR_SEPARATION.md", "LITERATURE_BOUNDARY.md", "PRESSURE_CONSTRUCTION.md",
    "ORDINARY_SELECTOR.md", "GermBridge.lean", "OrdinarySelector.lean",
    "germ_bridge_controls.py", "scalar_controls.py", "pressure_controls.py",
    "selector_controls.py", "exact_replay.py",
)


def run_checks():
    before = {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in INPUTS}
    results = {}
    for name in ("germ_bridge", "scalar", "pressure", "selector"):
        module_name = name + "_controls"
        spec = importlib.util.spec_from_file_location(module_name, ROOT / (module_name + ".py"))
        if spec is None or spec.loader is None:
            raise RuntimeError("cannot load exact control " + module_name)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        result = module.run_checks()
        if str(result.get("status")).lower() != "pass":
            raise RuntimeError("exact control failed " + module_name)
        results[name] = result
    for name, digest in before.items():
        if sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError("scientific input changed during execution " + name)
    return {
        "success": True,
        "scope": "exact finite ordinary and modular controls, not a universal Collatz proof or an all-depth computation",
        "source_sha256": before,
        **results,
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
