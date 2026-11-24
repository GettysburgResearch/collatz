#!/usr/bin/env python3
"""Replay only this research packet. Lean proofs and finite controls are distinct."""
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

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def compile_one(path, lean, out):
    body = path.read_text()
    namespace = re.search(r"^namespace (\w+)", body, re.M).group(1)
    names = [namespace+"."+n for n in re.findall(r"^theorem (\w+)", body, re.M)]
    audited = out / path.name
    audited.write_text(body+"\n"+"\n".join("#print axioms "+n for n in names)+"\n")
    command = [str(lean), "-j1", "-DwarningAsError=true", str(audited)]
    started = time.monotonic()
    proc = subprocess.run(command, capture_output=True, text=True, timeout=600)
    log = proc.stdout + proc.stderr
    (out/(path.stem+".log")).write_text(log)
    records = {}
    for name, ax in re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", log):
        records[name] = [x.strip() for x in ax.split(",") if x.strip()]
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        records[name] = []
    passed = proc.returncode == 0 and all(
        n in records and set(records[n]) <= ALLOWED for n in names
    )
    row = dict(source=path.name, sha256=sha(path), audited_copy_sha256=sha(audited),
               command=command, exit_code=proc.returncode,
               seconds=round(time.monotonic()-started,3), public_theorems=names,
               axioms={n:records.get(n) for n in names}, success=passed)
    print(path.name, "PASS" if passed else "FAIL", flush=True)
    return row

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--modules", nargs="+", choices=["CycleCore.lean", "EscapeCore.lean", "ShadowCore.lean"], default=["CycleCore.lean", "EscapeCore.lean", "ShadowCore.lean"])
    parser.add_argument("--controls", nargs="+", choices=["cycle_check.py", "shadow_check.py", "escape_check.py", "coverage_bound.py"], default=["cycle_check.py", "shadow_check.py", "escape_check.py", "coverage_bound.py"])
    args = parser.parse_args()
    out = args.out.resolve()
    if out.is_relative_to(HERE):
        parser.error("--out must be outside the research packet")
    out.mkdir(parents=True, exist_ok=True)
    lean = args.lean.resolve()
    version = subprocess.run([str(lean),"--version"],capture_output=True,text=True,check=True).stdout.strip()
    sources = [HERE/name for name in args.modules]
    with ThreadPoolExecutor(max_workers=3) as pool:
        formal = list(pool.map(lambda p:compile_one(p,lean,out),sources))
    finite = []
    for name in args.controls:
        outputs = []
        for mode in ([],["-O"]):
            cmd = [sys.executable,"-B",*mode,str(HERE/name)]
            proc = subprocess.run(cmd,capture_output=True,text=True,timeout=120)
            outputs.append(proc.stdout)
            finite.append(dict(source=name,sha256=sha(HERE/name),command=cmd,
                               exit_code=proc.returncode,stdout=proc.stdout,stderr=proc.stderr))
        if outputs[0] != outputs[1]:
            raise RuntimeError("Normal and optimized controls differ: "+name)
    success = all(r["success"] for r in formal) and all(r["exit_code"]==0 for r in finite)
    receipt = dict(schema="collatz-astra-universal-descent/v1",lean=version,
                   scope="New finite Lean declarations and bounded controls; not a proof of Collatz",
                   formal=formal,finite_controls=finite,success=success)
    (out/"CHECKS.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print("PUBLIC THEOREMS",sum(len(r["public_theorems"]) for r in formal),flush=True)
    for r in finite[::2]:
        print(r["source"]+"\n"+r["stdout"],flush=True)
    print("PASS" if success else "FAIL",flush=True)
    return 0 if success else 1

if __name__ == "__main__":
    raise SystemExit(main())

