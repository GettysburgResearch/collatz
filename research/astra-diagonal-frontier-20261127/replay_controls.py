#!/usr/bin/env python3
"""Replay the bounded exact controls, normally and optimized, without mutating inputs."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
PACKET = Path(__file__).resolve().parent
CASES = [
    ("check_native_gate.py", "native_gate_controls.json"),
    ("mass/check_seed_spread.py", "mass/seed_spread_controls.json"),
    ("mass/check_first_entry_law.py", "mass/first_entry_controls.json"),
    ("mass/check_native_shells.py", "mass/native_shell_checks.json"),
    ("mass/check_first_arrival_energy.py", "mass/first_arrival_energy_checks.json"),
    ("arithmetic/check_polynomial_rank.py", "arithmetic/polynomial_rank_controls.json"),
    ("arithmetic/check_higher_differences.py", "arithmetic/higher_difference_controls.json"),
    ("arithmetic/check_rotation_cuts.py", "arithmetic/rotation_cut_controls.json"),
    ("arithmetic/check_weighted_clock.py", "arithmetic/weighted_clock_controls.json"),
    ("arithmetic/check_sparse_rational_clock.py", "arithmetic/sparse_rational_clock_controls.json"),
    ("arithmetic/check_homogeneous_meetings.py", "arithmetic/homogeneous_meeting_controls.json"),
    ("arithmetic/check_shifted_clocks.py", "arithmetic/shifted_clock_controls.json"),
    ("arithmetic/check_odd_height_pressure.py", "arithmetic/odd_height_pressure_controls.json"),
    ("arithmetic/check_tetrad_rank.py", "arithmetic/tetrad_rank_controls.json"),
    ("arithmetic/check_dual_cuts.py", "arithmetic/dual_cut_controls.json"),
    ("arithmetic/check_full_step_chart.py", "arithmetic/full_step_chart_controls.json"),
    ("arithmetic/check_full_circuit_inversions.py", "arithmetic/full_circuit_inversion_controls.json"),
    ("arithmetic/check_farey_tile.py", "arithmetic/farey_tile_controls.json"),
    ("arithmetic/check_width_three.py", "arithmetic/width_three_controls.json"),
    ("arithmetic/check_upper_bundle.py", "arithmetic/upper_bundle_controls.json"),
    ("arithmetic/check_plateau_components.py", "arithmetic/plateau_components_controls.json"),
    ("linear/check_controls.py", None),
    ("linear/check_automata.py", None),
    ("linear/check_local_landing.py", None),
    ("linear/check_source_suffix.py", None),
    ("inverse/check_retained_trees.py", None),
    ("inverse/check_frozen_root.py", None),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--only", action="append", choices=[source for source, _ in CASES],
                        help="run only this declared checker; repeat for several; omit for the full packet")
    args = parser.parse_args()
    selected = [(source, record) for source, record in CASES
                if not args.only or source in args.only]
    receipt = args.receipt.resolve()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    result = {"schema": "collatz-astra-diagonal-controls/v1", "success": False,
              "started_utc": datetime.now(timezone.utc).isoformat(),
              "python": sys.version, "scope": "Finite exact controls only; no asymptotic or universal conclusion.",
              "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "selection": {"mode": "subset" if args.only else "all",
                            "declared_cases": len(CASES), "executed_cases": len(selected),
                            "not_executed": [source for source, record in CASES
                                             if (source, record) not in selected]},
              "cases": []}
    for rel, record in selected:
        source = PACKET/rel
        before_bytes = source.read_bytes()
        outputs, rows = [], []
        for optimized in (False, True):
            command = [sys.executable, "-X", "utf8", "-B"]
            if optimized:
                command += ["-O"]
            command += [str(source)]
            start = time.monotonic()
            run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=300)
            outputs.append(run.stdout)
            rows.append({"optimized": optimized, "exit_code": run.returncode,
                         "seconds": round(time.monotonic()-start, 3), "stderr": run.stderr})
        equal = outputs[0] == outputs[1]
        record_ok = record is None or json.loads(outputs[0]) == json.loads((PACKET/record).read_text())
        stable = source.read_bytes() == before_bytes
        success = equal and record_ok and stable and all(row["exit_code"] == 0 for row in rows)
        result["cases"].append({"source": source.relative_to(ROOT).as_posix(),
            "source_sha256": hashlib.sha256(before_bytes).hexdigest(), "runs": rows,
            "normal_optimized_identical": equal, "recorded_output_matches": record_ok,
            "source_unchanged": stable, "stdout": outputs[0], "success": success})
        receipt.write_text(json.dumps(result, indent=2)+"\n")
        print(f"{rel}: {'PASS' if success else 'FAIL'} in both modes", flush=True)
        if not success:
            raise SystemExit(1)
    result["success"] = True
    result["finished_utc"] = datetime.now(timezone.utc).isoformat()
    receipt.write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
