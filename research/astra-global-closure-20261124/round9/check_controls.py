"""Replay the five round-nine finite controls with and without Python assertions."""

import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = here.parents[2]
    reports = repo / "reports/astra-global-closure-20261124/round9"
    cases = [
        (here / "critical/check.py", reports / "critical/controls.json"),
        (here / "critical/depth_sieve.py", reports / "critical/depth_sieve.json"),
        (here / "arithmetic/check.py", reports / "arithmetic/controls.json"),
        (here / "rows/check.py", reports / "rows/controls.json"),
        (reports / "arithmetic/review_rows.py", reports / "arithmetic/row_review_controls.json"),
    ]
    receipt = {
        "scope": "Five exact finite controls in normal and optimized Python; byte-for-byte agreement with recorded outputs. No universal dynamical inference from finite tests.",
        "python_version": platform.python_version(),
        "runner_sha256": digest(Path(__file__)), "runs": [], "status": "INCOMPLETE",
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    for source, expected_file in cases:
        before = digest(source)
        expected = expected_file.read_bytes()
        for flags in (["-B"], ["-O", "-B"]):
            proc = subprocess.run([sys.executable, *flags, str(source)], cwd=repo,
                                  capture_output=True, timeout=600)
            passed = (proc.returncode == 0 and proc.stdout == expected and
                      before == digest(source) and not proc.stderr)
            receipt["runs"].append({
                "source": str(source.relative_to(repo)), "source_sha256": before,
                "flags": flags, "exit_code": proc.returncode,
                "source_unchanged": before == digest(source),
                "expected_output": str(expected_file.relative_to(repo)),
                "expected_output_sha256": digest(expected_file),
                "output_bytes_match": proc.stdout == expected,
                "stdout_sha256": hashlib.sha256(proc.stdout).hexdigest(),
                "stderr": proc.stderr.decode(), "passed": passed,
            })
            args.report.write_text(json.dumps(receipt, indent=2) + "\n")
            print(str(source.relative_to(repo)) + " " + " ".join(flags) + ": " + ("PASS" if passed else "FAIL"), flush=True)
            if not passed:
                print(proc.stdout.decode(), proc.stderr.decode(), flush=True)
                raise SystemExit(1)
    receipt.update(status="PASS", control_script_count=len(cases), execution_count=2*len(cases))
    args.report.write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: ten replays; frozen output bytes match.", flush=True)


if __name__ == "__main__":
    main()
