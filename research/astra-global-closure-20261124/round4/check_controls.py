"""Replay the round-four finite controls in normal and optimized Python."""

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
    reports = repo / "reports/astra-global-closure-20261124/round4"
    cases = [
        (here / "ordinary/check.py", reports / "ordinary/controls.json"),
        (here / "arithmetic/controls.py", reports / "arithmetic/controls.json"),
        (here / "head/controls.py", reports / "head/controls.json"),
        (reports / "head/check_cyclotomic_example.py", reports / "head/cyclotomic-example.json"),
    ]
    receipt = {"scope": "Exact finite arithmetic only; no universal dynamical inference.",
               "python_version": platform.python_version(),
               "runner_sha256": digest(Path(__file__)), "runs": [], "status": "INCOMPLETE"}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    for source, expected_file in cases:
        before = digest(source)
        expected = json.loads(expected_file.read_text())
        for flags in (["-B"], ["-O", "-B"]):
            proc = subprocess.run([sys.executable, *flags, str(source)], cwd=repo,
                                  text=True, capture_output=True, timeout=240)
            actual = json.loads(proc.stdout) if proc.returncode == 0 else None
            passed = (proc.returncode == 0 and actual == expected and
                      before == digest(source) and not proc.stderr)
            receipt["runs"].append({
                "source": str(source.relative_to(repo)), "source_sha256": before,
                "flags": flags, "exit_code": proc.returncode,
                "source_unchanged": before == digest(source),
                "expected_output": str(expected_file.relative_to(repo)),
                "expected_output_sha256": digest(expected_file),
                "output_matches": actual == expected,
                "stdout_sha256": hashlib.sha256(proc.stdout.encode()).hexdigest(),
                "stderr": proc.stderr, "passed": passed,
            })
            args.report.write_text(json.dumps(receipt, indent=2) + "\n")
            print(f"{source.parent.name}/{source.name} {' '.join(flags)}: "
                  + ("PASS" if passed else "FAIL"), flush=True)
            if not passed:
                print(proc.stdout + proc.stderr, flush=True)
                raise SystemExit(1)
    receipt["status"] = "PASS"
    args.report.write_text(json.dumps(receipt, indent=2) + "\n")


if __name__ == "__main__":
    main()
