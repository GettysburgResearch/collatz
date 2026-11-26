"""Replay the four exact finite controls in normal and optimized Python."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-dir", required=True, type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = here.parents[1]
    report = args.report_dir.resolve()
    report.mkdir(parents=True, exist_ok=True)
    receipt = {
        "status": "INCOMPLETE", "python": sys.version,
        "scope": "Exact finite controls on the stated ordinary or fixed-denominator domains. These executions do not prove universal Collatz convergence or the accompanying unbounded written theorems.",
        "runner_sha256": digest(Path(__file__).read_bytes()), "scripts": [],
    }
    for lane, output_name in [("adelic", "control.json"), ("cycle", "control.json"),
                              ("renormalization", "finite.json"), ("spectral", "control.json")]:
        source = here / lane / "check.py"
        before = digest(source.read_bytes())
        outputs, commands = [], []
        for options in (["-B"], ["-O", "-B"]):
            command = [sys.executable, *options, str(source.relative_to(repo))]
            result = subprocess.run(command, cwd=repo, capture_output=True, timeout=300)
            if result.returncode or result.stderr:
                raise RuntimeError(lane + " failed: " + result.stderr.decode(errors="replace"))
            json.loads(result.stdout)
            outputs.append(result.stdout)
            commands.append({"argv": command, "exit": result.returncode,
                             "stdout_sha256": digest(result.stdout)})
        if outputs[0] != outputs[1] or before != digest(source.read_bytes()):
            raise RuntimeError(lane + ": output mismatch or source changed during replay")
        artifact = report / lane / output_name
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_bytes(outputs[0])
        receipt["scripts"].append({
            "script": str(source.relative_to(repo)), "source_sha256": before,
            "commands": commands, "normal_equals_optimized": True, "source_unchanged": True,
            "output": str(artifact.relative_to(repo)) if artifact.is_relative_to(repo) else str(artifact),
            "stdout_sha256": digest(outputs[0]),
        })
        (report / "control-replay.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(lane + ": PASS (normal and optimized outputs identical)", flush=True)
    receipt.update(status="PASS", scripts_count=4, executions=8)
    (report / "control-replay.json").write_text(json.dumps(receipt, indent=2) + "\n")


if __name__ == "__main__":
    main()
