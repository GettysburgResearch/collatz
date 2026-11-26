#!/usr/bin/env python3
"""Replay every second-wave finite control, independently of written proofs.

Each complete JSON payload is compared in normal and optimized Python.  The
depth-ten integer table is regenerated from the frozen first-wave algorithm.
No computational output here proves the infinite pressure or Collatz theorem.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def execute(script, arguments=(), optimized=False):
    flags = ["-O", "-B"] if optimized else ["-B"]
    command = [sys.executable, *flags, str(script), *map(str, arguments)]
    result = subprocess.run(command, text=True, capture_output=True, timeout=300)
    if result.returncode or result.stderr:
        raise RuntimeError(f"{script.name}: {result.stdout}\n{result.stderr}")
    return json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    repo = root.parents[1]
    reports = repo / "reports/unconventional-20261126"
    receipt = {"scope": "second-wave complete exact finite controls only",
               "python": sys.version, "runs": []}
    cases = [
        (root / "arithmetic/check_reference.py", "REFERENCE_CONTROLS.json"),
        (root / "trace/check_trace.py", "TRACE_CONTROLS.json"),
        (root / "trace/check_decoder.py", "DECODER_CONTROLS.json"),
        (root / "arithmetic/check_excursions.py", "EXCURSION_CONTROLS.json"),
        (root / "operator/check_pressure.py", "PRESSURE_CONTROLS.json"),
        (reports / "reviews/review_reference.py", "REFERENCE_REVIEW_CONTROLS.json"),
        (reports / "reviews/review_pressure_entropy.py", "PRESSURE_REVIEW_CONTROLS.json"),
        (reports / "reviews/review_survivor.py", "SURVIVOR_REVIEW_CONTROLS.json"),
        (reports / "reviews/review_excursion.py", "EXCURSION_REVIEW_CONTROLS.json"),
    ]
    with tempfile.TemporaryDirectory(prefix="collatz-second-controls-") as temp:
        vector = Path(temp) / "bergman-h10.txt"
        generator = root / "operator/check_bergman.py"
        before = digest(generator)
        table = execute(generator, ["--depth", "10", "--write-vector", vector])
        expected = [row for row in json.loads((reports / "BERGMAN_CONTROLS.json").read_text())
                    if row["depth"] == 10]
        if table != expected or digest(vector) != expected[0]["vector_sha256"]:
            raise ValueError("regenerated depth-ten certificate mismatch")
        if digest(generator) != before:
            raise RuntimeError("generator changed during replay")
        receipt["vector_regeneration"] = {
            "source_sha256": before, "vector_sha256": digest(vector),
            "complete_record_equal": True, "residues": 59049}
        print("depth-ten table: complete regeneration passed", file=sys.stderr, flush=True)
        for script, record_name in cases:
            record = reports / record_name
            expected = json.loads(record.read_text(encoding="utf-8"))
            before = digest(script)
            arguments = [vector] if script.name == "check_pressure.py" else []
            for optimized in (False, True):
                actual = execute(script, arguments, optimized)
                if actual != expected:
                    raise ValueError(f"complete payload mismatch: {script.name}, optimized={optimized}")
                receipt["runs"].append({
                    "path": script.relative_to(repo).as_posix(),
                    "source_sha256": before, "record": record_name,
                    "record_sha256": digest(record), "optimized": optimized,
                    "exit_code": 0, "complete_payload_equal": True})
                print(f"{script.name}: {'optimized' if optimized else 'normal'} complete replay passed",
                      file=sys.stderr, flush=True)
            if digest(script) != before:
                raise RuntimeError(f"source changed during replay: {script.name}")
    serialized = json.dumps(receipt, indent=2) + "\n"
    if args.receipt:
        args.receipt.write_text(serialized, encoding="utf-8")
    else:
        sys.stdout.write(serialized)


if __name__ == "__main__":
    main()
