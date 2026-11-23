#!/usr/bin/env python3
"""Check only this checkpoint's new sources; write an external JSON receipt."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv: list[str], cwd: Path, env: dict[str, str] | None = None) -> dict:
    result = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(json.dumps({"argv": argv, "cwd": str(cwd),
                                      "returncode": result.returncode,
                                      "stdout": result.stdout, "stderr": result.stderr}, indent=2))
    return {"argv": argv, "exit_code": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    checkout = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                           cwd=packet, text=True).strip())
    receipt_path = args.receipt.resolve()
    if receipt_path.is_relative_to(checkout):
        raise ValueError("receipt must be outside the repository checkout")
    lean = args.lean.resolve()
    mathlib = args.mathlib.resolve()
    source = packet / "lean/InverseRealSeparation.lean"
    audit = packet / "lean/AuditInverseRealSeparation.lean"
    declarations = re.findall(r"^(?:def|theorem)\s+(\w+)", source.read_text(), re.MULTILINE)
    audited = re.findall(r"^#print axioms CollatzInverseReal\.(\w+)", audit.read_text(), re.MULTILINE)
    if set(declarations) != set(audited) or len(declarations) != len(audited):
        raise ValueError("audit must cover every new definition and theorem exactly once")
    # Match proof tokens, not prose descriptions of excluded shortcuts.
    forbidden = re.compile(r"\b(sorry|admit|axiom|native_decide)\b")
    if forbidden.search(re.sub(r"/-.*?-/", "", source.read_text(), flags=re.DOTALL)):
        raise ValueError("unexpected admission, custom axiom, or native proof shortcut")
    receipt = {
        "schema": "collatz-integer-boundary-checks/v1",
        "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "scope": "new Lean real-separation bridge and three finite arithmetic controls; not full Collatz or an end-to-end formalization of the written infinite classification",
        "python": sys.version,
        "lean_version": run([str(lean), "--version"], packet)["stdout"].strip(),
        "mathlib_head": run(["git", "rev-parse", "HEAD"], mathlib)["stdout"].strip(),
        "mathlib_tracked_status": run(["git", "status", "--short", "--untracked-files=no"], mathlib)["stdout"],
        "dependencies": "existing Mathlib and package objects reused; no historical project Lean modules rebuilt",
        "source_hashes": {str(p.relative_to(packet)): digest(p) for p in [source, audit, Path(__file__)]},
        "declarations": declarations,
        "finite_controls": [],
    }
    for name in ["check_pressure_wiener.py", "check_numen_inverse_fiber.py", "check_band_remainder.py"]:
        path = packet / name
        normal = run([sys.executable, "-X", "utf8", "-B", str(path)], packet)
        optimized = run([sys.executable, "-X", "utf8", "-B", "-O", str(path)], packet)
        if normal["stdout"] != optimized["stdout"]:
            raise ValueError(f"normal/optimized output mismatch for {name}")
        receipt["source_hashes"][name] = digest(path)
        receipt["finite_controls"].append({"file": name, "normal_exit_code": 0,
            "optimized_exit_code": 0, "identical_output": True,
            "output_sha256": hashlib.sha256(normal["stdout"].encode()).hexdigest(),
            "result": json.loads(normal["stdout"])})
    with tempfile.TemporaryDirectory(prefix="collatz-integer-boundary-") as temp:
        build = Path(temp)
        shutil.copy2(source, build / source.name)
        shutil.copy2(audit, build / audit.name)
        paths = [build, mathlib / ".lake/build/lib/lean"]
        paths += sorted(p / ".lake/build/lib/lean" for p in (mathlib / ".lake/packages").iterdir())
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
        receipt["lean_compile"] = run([str(lean), "-DwarningAsError=true", "-o",
                                       "InverseRealSeparation.olean", source.name], build, env)
        receipt["lean_audit"] = run([str(lean), "-DwarningAsError=true", audit.name], build, env)
    output = receipt["lean_audit"]["stdout"]
    lists = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", output)
    axioms = sorted({a.strip() for group in lists for a in group.split(",") if a.strip()})
    allowed = {"propext", "Classical.choice", "Quot.sound"}
    if set(axioms) - allowed or "sorryAx" in output:
        raise ValueError(f"unexpected axiom closure: {axioms}")
    for name in declarations:
        if f"CollatzInverseReal.{name}" not in output:
            raise ValueError(f"missing printed axiom audit: {name}")
    receipt["axiom_union"] = axioms
    receipt["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    receipt["success"] = True
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"success": True, "declarations_audited": len(declarations),
                      "axioms": axioms, "receipt": str(receipt_path)}, indent=2))


if __name__ == "__main__":
    main()
