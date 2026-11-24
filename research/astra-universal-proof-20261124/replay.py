"""Compile only this packet's five new Std modules and audit public theorems."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import time


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lean", required=True)
    parser.add_argument("--report-dir", required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    reports = Path(args.report_dir).resolve()
    reports.mkdir(parents=True, exist_ok=True)
    compiler = str(Path(args.lean).resolve())
    version = subprocess.run(
        [compiler, "--version"], capture_output=True, text=True, check=True
    ).stdout.strip()
    allowed = {"propext", "Classical.choice", "Quot.sound"}
    modules = [
        "UniversalProposal.lean",
        "minimum/MovingOctaveOrder.lean",
        "critical/OctaveOccupation.lean",
        "minimum/RunClock.lean",
        "interior/OrdinaryStationary.lean",
    ]
    rows = []
    with tempfile.TemporaryDirectory(prefix="collatz-universal-lean-") as temp:
        for relative in modules:
            source = packet / relative
            data = source.read_bytes()
            content = data.decode()
            namespace = re.findall(r"^namespace ([\w.]+)$", content, re.M)
            if len(namespace) != 1:
                raise RuntimeError(f"expected one explicit namespace: {relative}")
            declarations = re.findall(r"^theorem (\w+)", content, re.M)
            names = [namespace[0] + "." + name for name in declarations]
            # Only print directives are removed; declaration bytes are preserved.
            harness_text = re.sub(r"^#print axioms .*\n", "", content, flags=re.M)
            harness_text += "\n" + "\n".join(
                "#print axioms " + name for name in names
            ) + "\n"
            harness = Path(temp) / source.name
            harness.write_text(harness_text)
            command = [
                compiler, "-DwarningAsError=true", "-DautoImplicit=false", str(harness)
            ]
            start = time.monotonic()
            run = subprocess.run(command, capture_output=True, text=True, timeout=180)
            output = run.stdout + run.stderr
            log_name = source.stem + ".log"
            (reports / log_name).write_text(output)
            found = {}
            for name, axioms in re.findall(
                r"'([^']+)' depends on axioms: \[([^\]]*)\]", output
            ):
                found[name] = [a.strip() for a in axioms.split(",") if a.strip()]
            for name in re.findall(r"'([^']+)' does not depend on any axioms", output):
                found[name] = []
            passed = (
                run.returncode == 0
                and set(found) == set(names)
                and all(set(a) <= allowed for a in found.values())
                and "sorryAx" not in output
            )
            rows.append({
                "source": relative,
                "sha256": digest(data),
                "harness_sha256": digest(harness_text.encode()),
                "flags": ["warningAsError=true", "autoImplicit=false"],
                "exit_code": run.returncode,
                "seconds": round(time.monotonic() - start, 3),
                "public_theorems": len(names),
                "axioms": found,
                "log": log_name,
                "log_sha256": digest(output.encode()),
                "pass": passed,
            })
            if not passed:
                print(output)
                raise RuntimeError(f"Lean/audit failure: {relative}")

    controls = []
    for flags in ([], ["-O"]):
        command = ["python", *flags, "-B", str(packet / "minimum" / "check.py")]
        run = subprocess.run(command, capture_output=True, text=True, timeout=180)
        output = run.stdout + run.stderr
        name = "ordinary_optimized.log" if flags else "ordinary_normal.log"
        (reports / name).write_text(output)
        controls.append({
            "flags": flags,
            "exit_code": run.returncode,
            "log": name,
            "log_sha256": digest(output.encode()),
        })
        if run.returncode:
            raise RuntimeError(f"ordinary replay failure: {output}")
    if controls[0]["log_sha256"] != controls[1]["log_sha256"]:
        raise RuntimeError("normal/optimized replay outputs differ")
    receipt = {
        "status": "PASS",
        "compiler": version,
        "compiler_path": compiler,
        "compiler_sha256": digest(Path(compiler).read_bytes()),
        "module_count": len(rows),
        "public_theorem_count": sum(r["public_theorems"] for r in rows),
        "modules": rows,
        "ordinary_controls": controls,
        "scope": (
            "New finite kernels and conditional universal theorem only. "
            "No formalization of the asymptotic cycle theorem, the external "
            "logarithmic-form theorem, or universal certificate coverage."
        ),
    }
    (reports / "LEAN_REPLAY.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({
        "status": receipt["status"],
        "modules": receipt["module_count"],
        "public_theorems": receipt["public_theorem_count"],
        "ordinary_modes": len(controls),
    }))


if __name__ == "__main__":
    main()
