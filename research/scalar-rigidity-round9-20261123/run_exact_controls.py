#!/usr/bin/env python3
"""Run the four round-nine finite control lanes with bound source bytes."""

import ast
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LANES = {
    "actual_source_law": "law_controls.py",
    "arithmetic_rigidity": "arithmetic_controls.py",
    "ordinary_carry_return": "carry_controls.py",
    "complete_denominator_rigidity": "phase_controls.py",
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
        spec = importlib.util.spec_from_file_location("round9_" + lane, ROOT / name)
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
        "schema": "collatz-round9-exact-controls/v1",
        "status": "PASS",
        "published_parent": "6352608dd6c04735e1f8bd86fef4ebc97b1aeacb",
        "scope": "finite exact controls, distinct from the written universal proofs and Lean compilation",
        "input_sha256": before,
        "python_assert_counts": assertion_counts,
        "lanes": results,
        "total_explicit_checks": sum(result["exact_checks"] for result in results.values()),
        "not_claimed": "Collatz closure or a fixed positive ordinary realization of a symbolic infinite word",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
