#!/usr/bin/env python3
"""Authenticate and replay the three supplied packages in temporary copies.

The original scripts contain unsupported mathematical labels. Successful
execution is reported only as execution, never as acceptance of those labels.
The numerical packages need NumPy and SciPy; this wrapper uses the standard
library. No archived input file is modified.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "archive/gemini-followups-20261120"
BUNDLE = "collatz_routes_bundle"
V2 = "collatz_full_completion_blueprints_v2_2026-11-20"
V3 = "collatz_farkas_dirichlet_breakthrough_v3_2026-11-20"
RUNS = [
    (BUNDLE, "route1_tripling_and_sibling_mergers/algebraic_coalescence_sieve.py"),
    (BUNDLE, "route2_inverse_compiler_and_bellman/bellman_potential_certifier.py"),
    (BUNDLE, "route3_global_integrality_and_cube4/rational_barrier_and_diophantine.py"),
    (BUNDLE, "route4_adelic_spectral_operators/transfer_operator_spectrum.py"),
    (BUNDLE, "route5_agentic_pr_roadmap/barrier_falsification_harness.py"),
    (V2, "run_all_v2_verifiers.py"),
    (V3, "verify_farkas_certificates.py"),
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def authenticate() -> tuple[dict, int]:
    manifest = json.loads((ARCHIVE / "source-manifest.json").read_text())
    count = 0
    expected_paths = set()
    for bundle in manifest["archives"]:
        for row in bundle["files"]:
            require(row["path"] not in expected_paths, "Duplicate source path")
            expected_paths.add(row["path"])
            p = ARCHIVE / "source" / row["path"]
            data = p.read_bytes()
            require(len(data) == row["bytes"], "Source size mismatch: " + row["path"])
            require(sha256(data).hexdigest() == row["sha256"],
                    "Source hash mismatch: " + row["path"])
            count += 1
    actual_paths = {p.relative_to(ARCHIVE / "source").as_posix()
                    for p in (ARCHIVE / "source").rglob("*") if p.is_file()}
    require(actual_paths == expected_paths, "Unexpected or missing source file")
    return manifest, count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    manifest, count = authenticate()
    result = {
        "schema": "collatz-gemini-followups-original-replay/v1",
        "scope": "Original script execution and byte authentication only; not acceptance of proof labels.",
        "collatz_proved": False,
        "archived_files_authenticated": count,
        "python": sys.version,
        "zip_sha256": {x["archive"]: x["sha256"] for x in manifest["archives"]},
        "runs": [],
        "generated_receipt_comparisons": [],
    }
    with TemporaryDirectory(prefix="collatz-gemini-followups-") as scratch:
        copied = Path(scratch) / "source"
        shutil.copytree(ARCHIVE / "source", copied)
        for package, script in RUNS:
            completed = subprocess.run(
                [sys.executable, "-X", "utf8", "-B", str(copied / package / script)],
                cwd=copied / package, capture_output=True, text=True,
                encoding="utf-8", timeout=180, check=False,
            )
            try:
                output = json.loads(completed.stdout)
            except json.JSONDecodeError:
                output = completed.stdout
            result["runs"].append({
                "package": package, "script": script,
                "exit_code": completed.returncode,
                "output": output, "stderr": completed.stderr,
            })
        for package, filename in [
            (V2, "verification_receipt_v2.json"),
            (V3, "verification_receipt_v3.json"),
            (V3, "farkas_certificates_r4_r6.json"),
        ]:
            original = (ARCHIVE / "source" / package / filename).read_bytes()
            generated = (copied / package / filename).read_bytes()
            result["generated_receipt_comparisons"].append({
                "package": package, "file": filename,
                "bytes_identical": original == generated,
                "json_identical": json.loads(original) == json.loads(generated),
                "original_sha256": sha256(original).hexdigest(),
                "generated_sha256": sha256(generated).hexdigest(),
            })
            if filename.startswith("verification_receipt"):
                result["generated_receipt_comparisons"][-1]["generated_output"] = json.loads(generated)
    _, count_after = authenticate()
    require(count == count_after, "Source count changed during replay")
    result["original_scripts_succeeded"] = all(x["exit_code"] == 0 for x in result["runs"])
    v2_run = next(x for x in result["runs"] if x["package"] == V2)
    v2_output = v2_run["output"]
    v2_receipt = next(x["generated_output"]
                      for x in result["generated_receipt_comparisons"]
                      if x["package"] == V2)
    v2_leaf_rows = v2_receipt.get("verifier_results", [])
    v2_leaf_count = len(v2_leaf_rows)
    result["leaf_scripts_reported"] = len(RUNS) - 1 + v2_leaf_count
    require(isinstance(v2_output, dict) and
            v2_output.get("verifiers_run") == v2_leaf_count == 4 and
            v2_run["exit_code"] == 0 and
            all(x.get("returncode", 0) == 0 and "output" in x
                for x in v2_leaf_rows),
            "The v2 runner did not report four completed leaf verifiers")
    result["source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0 if result["original_scripts_succeeded"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
