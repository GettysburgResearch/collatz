"""Replay this packet's finite arithmetic controls in normal and optimized Python."""

import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys


BASE = Path("research/astra-joint-closure-20261124")
CASES = ["pressure/check_weighted_pressure.py", "ordinary/check_internal_merge.py",
         "arithmetic/check_cycle.py"]


def require(test, message):
    if not test:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    repo = args.repo.resolve()
    result = {"python": sys.version, "cases": []}
    for relative in CASES:
        path = BASE / relative
        source = (repo / path).read_bytes()
        asserts = sum(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(source)))
        require(asserts == 0, "Assertions would weaken optimized verification")
        runs = []
        for flags in (["-B"], ["-O", "-B"]):
            command = [sys.executable, *flags, str(path)]
            process = subprocess.run(command, cwd=repo, capture_output=True, text=True)
            require(process.returncode == 0,
                    str(path) + " failed:\n" + process.stdout + process.stderr)
            require(not process.stderr, "Unexpected diagnostic: " + process.stderr)
            runs.append({"command": ["python", *command[1:]],
                         "exit_code": process.returncode, "stdout": process.stdout})
        require(runs[0]["stdout"] == runs[1]["stdout"], "Optimization changes output")
        if relative.startswith("pressure/"):
            expected = json.loads((repo / "reports/astra-joint-closure-20261124/pressure/WEIGHTED_PRESSURE.json").read_text())
            require(json.loads(runs[0]["stdout"]) == expected,
                    "Pressure certificate differs from its frozen result")
        result["cases"].append({"path": path.as_posix(),
                                "sha256": hashlib.sha256(source).hexdigest(),
                                "assert_nodes": asserts, "runs": runs})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
