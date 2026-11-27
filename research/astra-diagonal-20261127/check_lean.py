#!/usr/bin/env python3
"""Build this packet's Lean kernels freshly and inventory every public theorem."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
PACKET = Path(__file__).resolve().parent
MATHLIB_PIN = "d13f23b723b8a846827a245b89c10fc7d3f11612"
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def run(argv: list[str], *, env: dict[str, str] | None = None,
        cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, cwd=cwd, env=env, text=True, capture_output=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--only", nargs="*", help="Optional exact module stems")
    args = parser.parse_args()
    lean = str(args.lean.resolve())
    mathlib = args.mathlib.resolve()
    receipt = args.receipt.resolve()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    logs = receipt.parent / (receipt.stem + "_logs")
    logs.mkdir(exist_ok=True)
    version = run([lean, "--version"])
    if version.returncode or "4.34.1" not in version.stdout:
        raise SystemExit("Lean 4.34.1 is required")
    pin = run(["git", "-C", str(mathlib), "rev-parse", "HEAD"])
    if pin.returncode or pin.stdout.strip() != MATHLIB_PIN:
        raise SystemExit("Mathlib source identity differs from the packet pin")
    sources = sorted(PACKET.rglob("*.lean"))
    if args.only is not None:
        wanted = set(args.only)
        sources = [source for source in sources if source.stem in wanted]
        if {source.stem for source in sources} != wanted:
            raise SystemExit("A requested module is missing")
    if not sources or len({source.stem for source in sources}) != len(sources):
        raise SystemExit("Expected nonempty modules with distinct stems")
    result = {
        "schema": "collatz-astra-diagonal-lean/v1",
        "compiler": version.stdout.strip(),
        "mathlib": MATHLIB_PIN,
        "dependency_manifest_sha256": hashlib.sha256(
            (mathlib / "lake-manifest.json").read_bytes()).hexdigest(),
        "scope": "Fresh compilation and public-theorem axiom inventory of the listed finite kernels. The infinite analytic, probabilistic and arithmetic arguments in the companion notes are written proposals or retained external inputs. This receipt does not prove Collatz or discharge a missing estimate.",
        "modules": [],
        "success": False,
    }
    started = time.monotonic()
    public: list[str] = []
    with tempfile.TemporaryDirectory(prefix="collatz-diagonal-lean-") as temporary:
        obj = Path(temporary)
        cache = mathlib / ".lake/build/lib/lean"
        packages = sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
        env = dict(os.environ)
        env["LEAN_PATH"] = os.pathsep.join(map(str, [obj, cache, *packages]))
        for source in sources:
            original = source.read_bytes()
            namespaces = re.findall(r"^namespace ([A-Za-z_][A-Za-z0-9_.]*)\s*$",
                                    original.decode(), re.MULTILINE)
            if len(namespaces) != 1:
                raise SystemExit("Expected one explicit namespace in " + str(source))
            names = re.findall(
                r"^(?:@\[[^\n]*\]\s*)*(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_'.]*)",
                original.decode(), re.MULTILINE)
            declarations = [namespaces[0] + "." + name for name in names]
            public.extend(declarations)
            before = time.monotonic()
            compiled = run([lean, "-DautoImplicit=false", "-DwarningAsError=true",
                            "-o", str(obj / (source.stem + ".olean")), str(source)], env=env)
            if source.read_bytes() != original:
                raise SystemExit("Source changed during compilation: " + str(source))
            (logs / (source.stem + ".stdout.log")).write_text(compiled.stdout)
            (logs / (source.stem + ".stderr.log")).write_text(compiled.stderr)
            result["modules"].append({
                "module": source.stem,
                "source": source.relative_to(ROOT).as_posix(),
                "sha256": hashlib.sha256(original).hexdigest(),
                "exit_code": compiled.returncode,
                "seconds": round(time.monotonic() - before, 3),
                "public_theorems": declarations,
            })
            receipt.write_text(json.dumps(result, indent=2) + "\n")
            print(f"{source.stem}: exit {compiled.returncode}; {len(declarations)} public theorems", flush=True)
            if compiled.returncode:
                print(compiled.stdout + compiled.stderr)
                raise SystemExit(1)
        audit = "\n".join([*("import " + source.stem for source in sources), "",
                            *("#print axioms " + name for name in public), ""])
        audit_path = obj / "Audit.lean"
        audit_path.write_text(audit)
        checked = run([lean, "-DautoImplicit=false", "-DwarningAsError=true", str(audit_path)], env=env)
        (logs / "Audit.lean").write_text(audit)
        (logs / "Audit.stdout.log").write_text(checked.stdout)
        (logs / "Audit.stderr.log").write_text(checked.stderr)
        inventories = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", checked.stdout)
        axioms = {item.strip() for inventory in inventories for item in inventory.split(",") if item.strip()}
        covered = len(inventories) + checked.stdout.count("does not depend on any axioms")
        success = checked.returncode == 0 and covered == len(public) and not (axioms - STANDARD_AXIOMS)
        result.update({
            "public_theorems": len(public),
            "axiom_audit": {"exit_code": checked.returncode, "audited": covered, "axioms": sorted(axioms)},
            "seconds": round(time.monotonic() - started, 3),
            "success": success,
        })
        receipt.write_text(json.dumps(result, indent=2) + "\n")
        if not success:
            print(checked.stdout + checked.stderr)
            raise SystemExit("Public-theorem axiom audit failed or was incomplete")
    print(json.dumps({"success": True, "modules": len(sources), "public_theorems": len(public), "axioms": sorted(axioms)}))


if __name__ == "__main__":
    main()
