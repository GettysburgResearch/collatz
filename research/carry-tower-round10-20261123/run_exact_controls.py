#!/usr/bin/env python3
"""Run the three round-ten finite control lanes with bound source bytes."""

import ast
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LANES = {
    "arbitrary_return_tower": "tower_controls.py",
    "general_rational_phase": "general_phase_controls.py",
    "sparse_arithmetic_scripts": "arithmetic_tower_controls.py",
}


def bindings():
    return {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(ROOT.iterdir()) if path.is_file()
            and path.suffix in (".md", ".lean", ".py", ".json")}


def main():
    before = bindings()
    assertion_counts = {}
    for name in before:
        if not name.endswith(".py"):
            continue
        tree = ast.parse((ROOT / name).read_text(encoding="utf-8"), filename=name)
        count = sum(isinstance(node, ast.Assert) for node in ast.walk(tree))
        assertion_counts[name] = count
        if count:
            raise RuntimeError("disabled-under-optimization assertion in " + name)
    results = {}
    for lane, name in LANES.items():
        spec = importlib.util.spec_from_file_location("round10_" + lane, ROOT / name)
        if spec is None or spec.loader is None:
            raise RuntimeError("could not load " + name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.run_checks()
        if result.get("status") != "PASS" or result.get("exact_checks", 0) <= 0:
            raise RuntimeError("unsuccessful finite lane " + lane)
        results[lane] = result
    after = bindings()
    if before != after:
        raise RuntimeError("scientific inputs changed during execution")
    print(json.dumps({
        "schema": "collatz-round10-exact-controls/v1",
        "status": "PASS",
        "published_parent": "c369ae3c426ec6aaf9a280ec9578b9910c2147d5",
        "scope": "finite exact controls, distinct from the actual scalar Lean theorem and the written return and 2-adic arguments",
        "input_sha256": before,
        "python_assert_counts": assertion_counts,
        "lanes": results,
        "total_explicit_checks": sum(result["exact_checks"] for result in results.values()),
        "not_claimed": "Collatz closure or a fixed positive ordinary realization of a symbolic infinite word",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
