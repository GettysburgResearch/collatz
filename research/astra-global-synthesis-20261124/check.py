#!/usr/bin/env python3
"""Check this packet's new Lean declarations and bounded exact controls only."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
MODULES = ("section/ForwardAnchors.lean", "arithmetic/OctaveProfiles.lean",
           "merger/PaidPairs.lean", "arithmetic/OptimalReset.lean",
           "merger/MixedPaid.lean", "arithmetic/WindowControl.lean")
CONTROLS = ("arithmetic/check.py", "merger/check.py", "merger/mixed_check.py",
            "arithmetic/window_control.py")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compile_one(name, lean, out):
    path = HERE / name
    body = path.read_text()
    namespace = re.search(r"^namespace ([\w.]+)$", body, re.M).group(1)
    names = [namespace + "." + n
             for n in re.findall(r"^theorem (\w+)", body, re.M)]
    if not names:
        raise RuntimeError("No public theorems found: " + name)
    audited = out / path.name
    audited.write_text(body + "\n" + "\n".join("#print axioms " + n for n in names) + "\n")
    command = [str(lean), "-j1", "-DwarningAsError=true", str(audited)]
    started = time.monotonic()
    proc = subprocess.run(command, capture_output=True, text=True, timeout=600)
    log = proc.stdout + proc.stderr
    (out / (path.stem + ".log")).write_text(log)
    records = {}
    for theorem, axioms in re.findall(
            r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", log):
        records[theorem] = [x.strip() for x in axioms.split(",") if x.strip()]
    for theorem in re.findall(r"'([^']+)' does not depend on any axioms", log):
        records[theorem] = []
    passed = proc.returncode == 0 and all(
        n in records and set(records[n]) <= ALLOWED for n in names)
    print(name, "PASS" if passed else "FAIL", flush=True)
    return dict(source=name, sha256=sha(path), audited_copy_sha256=sha(audited),
                command=command, exit_code=proc.returncode,
                seconds=round(time.monotonic() - started, 3),
                public_theorems=names, axioms={n: records.get(n) for n in names},
                success=passed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--modules", nargs="+", choices=MODULES, default=MODULES)
    parser.add_argument("--controls", nargs="*", choices=CONTROLS, default=CONTROLS)
    args = parser.parse_args()
    out = args.out.resolve()
    if out.is_relative_to(HERE):
        parser.error("--out must be outside the scientific packet")
    out.mkdir(parents=True, exist_ok=True)
    lean = args.lean.resolve()
    version = subprocess.run([str(lean), "--version"], capture_output=True,
                             text=True, check=True).stdout.strip()
    with ThreadPoolExecutor(max_workers=3) as pool:
        formal = list(pool.map(lambda n: compile_one(n, lean, out), args.modules))
    finite = []
    for name in args.controls:
        outputs = []
        for flags in ([], ["-O"]):
            command = [sys.executable, "-B", *flags, str(HERE / name)]
            proc = subprocess.run(command, capture_output=True, text=True, timeout=180)
            outputs.append(proc.stdout)
            finite.append(dict(source=name, sha256=sha(HERE / name), command=command,
                               exit_code=proc.returncode, stdout=proc.stdout,
                               stderr=proc.stderr))
        if outputs[0] != outputs[1]:
            raise RuntimeError("Normal and optimized outputs differ: " + name)
    success = (all(r["success"] for r in formal)
               and all(r["exit_code"] == 0 for r in finite))
    receipt = dict(schema="collatz-astra-global-synthesis/v1", lean=version,
                   scope="All public theorems in the selected new Std-only modules; "
                         "bounded exact controls; no universal Collatz claim",
                   formal=formal, finite_controls=finite, success=success)
    (out / "CHECKS.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PUBLIC THEOREMS", sum(len(r["public_theorems"]) for r in formal), flush=True)
    for row in finite[::2]:
        print(row["source"] + "\n" + row["stdout"], flush=True)
    print("PASS" if success else "FAIL", flush=True)
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
