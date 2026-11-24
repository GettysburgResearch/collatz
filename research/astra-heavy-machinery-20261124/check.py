#!/usr/bin/env python3
"""Audit this packet's new Lean sources and bounded ordinary arithmetic controls.

The analytic and topological arguments in the Markdown files are written proofs.
This driver does not formalize or validate the external literature inputs.
"""
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
MODULES = ("ergodic/ErgodicWindow.lean", "diophantine/MahlerCore.lean",
           "dynamics/KernelTransfer.lean")
CONTROLS = ("ergodic/check.py", "diophantine/check.py",
            "diophantine/mixed_check.py", "dynamics/controls.py")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def compile_one(name, lean, out):
    source = HERE / name
    original = source.read_bytes()
    body = original.decode()
    namespace = re.search(r"^namespace ([\w.]+)$", body, re.M).group(1)
    names = [namespace + "." + name
             for name in re.findall(r"^theorem (\w+)", body, re.M)]
    if not names:
        raise RuntimeError("No public theorems in " + str(source))
    audited = out / source.name
    audit_text = body + "\n" + "\n".join("#print axioms " + n for n in names) + "\n"
    audited.write_text(audit_text)
    command = [str(lean), "-j1", "-DwarningAsError=true", str(audited)]
    started = time.monotonic()
    process = subprocess.run(command, capture_output=True, text=True, timeout=600)
    log = process.stdout + process.stderr
    (out / (source.stem + ".log")).write_text(log)
    records = {}
    for theorem, axioms in re.findall(
            r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", log):
        records[theorem] = [a.strip() for a in axioms.split(",") if a.strip()]
    for theorem in re.findall(r"'([^']+)' does not depend on any axioms", log):
        records[theorem] = []
    stable = source.read_bytes() == original and audited.read_text() == audit_text
    success = process.returncode == 0 and stable and all(
        n in records and set(records[n]) <= ALLOWED for n in names)
    print(name, "PASS" if success else "FAIL", flush=True)
    return dict(source=name, sha256=digest(original),
                audited_copy_sha256=digest(audited.read_bytes()),
                command=command, exit_code=process.returncode,
                seconds=round(time.monotonic() - started, 3),
                public_theorems=names, axioms={n: records.get(n) for n in names},
                source_and_audit_stable=stable, success=success)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    arguments = parser.parse_args()
    out = arguments.out.resolve()
    if out.is_relative_to(HERE):
        parser.error("--out must be outside the scientific packet")
    out.mkdir(parents=True, exist_ok=True)
    lean = arguments.lean.resolve()
    version = subprocess.run([str(lean), "--version"], capture_output=True,
                             text=True, check=True).stdout.strip()
    with ThreadPoolExecutor(max_workers=3) as pool:
        formal = list(pool.map(lambda name: compile_one(name, lean, out), MODULES))
    finite = []
    for name in CONTROLS:
        path = HERE / name
        original = path.read_bytes()
        outputs = []
        for flags in ([], ["-O"]):
            command = [sys.executable, "-B", *flags, str(path)]
            process = subprocess.run(command, capture_output=True, text=True, timeout=180)
            outputs.append(process.stdout)
            finite.append(dict(source=name, sha256=digest(original), command=command,
                               exit_code=process.returncode, stdout=process.stdout,
                               stderr=process.stderr,
                               source_stable=path.read_bytes() == original))
        if outputs[0] != outputs[1]:
            raise RuntimeError("Normal and optimized outputs differ: " + name)
    success = (all(r["success"] for r in formal)
               and all(r["exit_code"] == 0 and r["source_stable"] for r in finite))
    receipt = dict(schema="collatz-astra-heavy-machinery/v1", lean=version,
                   scope="All public theorems in the three new Std-only modules; "
                         "bounded exact ordinary controls. External analytic results "
                         "and written infinite proofs are not part of this Lean audit.",
                   formal=formal, finite_controls=finite, success=success)
    (out / "CHECKS.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PUBLIC THEOREMS", sum(len(r["public_theorems"]) for r in formal), flush=True)
    for row in finite[::2]:
        print(row["source"] + "\n" + row["stdout"], flush=True)
    print("PASS" if success else "FAIL", flush=True)
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
