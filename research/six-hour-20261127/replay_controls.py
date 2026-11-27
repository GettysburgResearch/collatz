#!/usr/bin/env python3
"""Replay frozen finite controls in both Python modes; no mathematical extrapolation."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CONTROLS = [
    ("gates/gate_background_controls.py", [], "gates/GATE_BACKGROUND_CONTROLS.json"),
    ("cycles/check_toric_windows.py", [], "cycles/TORIC_WINDOW_CONTROLS.json"),
    ("pointwise/check_multi_block.py", [], "pointwise/MULTI_BLOCK_CONTROLS.json"),
    ("pointwise/check_negative17_minimum.py", [], "pointwise/NEGATIVE17_CONTROLS.json"),
    ("pointwise/independent_audit.py", ["pointwise/NEGATIVE17_EXACT_MINIMA.md"],
     "pointwise/INDEPENDENT_MINIMUM_CONTROLS.json"),
    ("pointwise/check_adaptive_anchors.py", [], "pointwise/ADAPTIVE_ANCHOR_CONTROLS.json"),
    ("pointwise/check_signed_anchor.py", [], "pointwise/SIGNED_ANCHOR_CONTROLS.json"),
    ("pointwise/check_extra_budget.py", [], "pointwise/EXTRA_BUDGET_CONTROLS.json"),
    ("pointwise/check_positive_anchors.py", [], "pointwise/POSITIVE_ANCHOR_CONTROLS.json"),
    ("pointwise/check_fourth.py", [], "pointwise/FOURTH_EXTRA_CONTROLS.json"),
    ("pointwise/check_overhead_spectrum.py", [], "pointwise/ORDINARY_OVERHEAD_CONTROLS.json"),
    ("pointwise/check_positive_cone_independent.py", [], "pointwise/POSITIVE_CONE_INDEPENDENT.json"),
    ("pointwise/check_inverse_extensions_independent.py", [], "pointwise/INDEPENDENT_EXTENSIONS.json"),
    ("cycles/check_clock_shadows.py", [], "cycles/CLOCK_SHADOW_CONTROLS.json"),
    ("cycles/check_clock_mesh.py", [], "cycles/CLOCK_MESH_CONTROLS.json"),
    ("cycles/check_resonant_interval.py", [], "cycles/RESONANT_INTERVAL_CONTROLS.json"),
    ("cycles/check_dense_denominators.py", [], "cycles/DENSE_DENOMINATOR_CONTROLS.json"),
    ("cycles/check_cycles_independent.py", [], "cycles/INDEPENDENT_CYCLES.json"),
    ("pointwise/check_shadow_packets.py", [], "pointwise/SHADOW_PACKET_CONTROLS.json"),
    ("pointwise/check_moving_review.py", [], "pointwise/MOVING_REVIEW_CONTROLS.json"),
    ("pointwise/check_grade_split.py", [], "pointwise/GRADE_SPLIT_CONTROLS.json"),
    ("pointwise/check_grade_digits.py", [], "pointwise/GRADE_DIGITS_CONTROLS.json"),
    ("pointwise/check_signed_grade_independent.py", [], "pointwise/SIGNED_GRADE_INDEPENDENT_CONTROLS.json"),
    ("cycles/bridge_energy_certificate.py", [], "cycles/BRIDGE_ENERGY_CHECK.json"),
    ("cycles/check_binary_energy_independent.py", [], "cycles/BINARY_ENERGY_INDEPENDENT_CONTROLS.json"),
    ("cycles/full_bridge_pressure.py", [], "cycles/FULL_BRIDGE_PRESSURE.json"),
    ("cycles/check_free_bridge_review.py", [], "cycles/FREE_BRIDGE_REVIEW_CONTROLS.json"),
]
DEPENDENCIES = {
    "pointwise/check_positive_anchors.py": ["pointwise/check_extra_budget.py"],
    "pointwise/check_fourth.py": ["pointwise/check_extra_budget.py"],
    "pointwise/check_overhead_spectrum.py": [
        "pointwise/check_extra_budget.py", "pointwise/check_positive_anchors.py"],
    "cycles/full_bridge_pressure.py": ["cycles/bridge_energy_certificate.py"],
}


def main():
    receipt = []
    for script, inputs, expected in CONTROLS:
        outputs = []
        for mode in ([], ["-O"]):
            result = subprocess.run(
                [sys.executable, *mode, "-B", str(ROOT / script),
                 *(str(ROOT / value) for value in inputs)],
                cwd=ROOT, capture_output=True)
            if result.returncode or result.stderr:
                sys.stderr.buffer.write(result.stdout + result.stderr)
                raise SystemExit(result.returncode or 1)
            outputs.append(result.stdout)
        frozen = (ROOT / expected).read_bytes()
        if outputs[0] != outputs[1] or outputs[0] != frozen:
            raise SystemExit(f"complete output differs: {script}")
        receipt.append({
            "script": script,
            "sha256": hashlib.sha256((ROOT / script).read_bytes()).hexdigest(),
            "inputs": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in inputs},
            "dependencies": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                             for p in DEPENDENCIES.get(script, [])},
            "expected": expected,
            "output_sha256": hashlib.sha256(frozen).hexdigest(),
            "normal_exit_code": 0,
            "optimized_exit_code": 0,
            "byte_identical": True,
        })
        print(f"{script}: both modes reproduce the frozen output", file=sys.stderr, flush=True)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
