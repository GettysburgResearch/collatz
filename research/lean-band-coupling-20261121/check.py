#!/usr/bin/env python3
"""Reproduce the pinned Lean packet, including its explicit module-format port.

No downloads and no edits to the checkout are performed. Supply an already
built mathlib at the pinned commit, Lean 4.34.1, and an external build directory.
The original PR173 sources stay byte-for-byte frozen in lean/. The generated
module-mode inputs and their hashes are included in the verification receipt.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time


MODULES = [
    "ShellCover", "ForwardSection", "SectionDynamics", "RisingReturns",
    "ClockSteering", "OffsetDescent", "OffsetHorizon", "ReturnClock",
    "RisingMerge", "SourceBoundedMerge", "LowerMarkedMerger", "Examples", "Audit",
]
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replace_once(text: str, before: str, after: str) -> str:
    if text.count(before) != 1:
        raise ValueError(f"Port rule must match exactly once: {before!r}")
    return text.replace(before, after, 1)


def module_port(name: str, text: str) -> str:
    """Visibility/header changes only; no definition or proof body is changed."""
    if name == "ShellCover":
        text = replace_once(text, "private def GridAt ", "def GridAt ")
        text = replace_once(text,
            "private instance (h p : Nat) : Decidable (GridAt h p)",
            "instance (h p : Nat) : Decidable (GridAt h p)")
    elif name == "ForwardSection":
        for kind, declaration in [
            ("theorem", "phase_orbit"), ("theorem", "grid_point"),
            ("def", "clock"), ("theorem", "clock_exact"),
            ("theorem", "clock_weight"),
        ]:
            text = replace_once(text, f"private {kind} {declaration} ",
                                f"{kind} {declaration} ")
    elif name == "SectionDynamics":
        text = replace_once(text, "private theorem visit_exists ",
                            "theorem visit_exists ")
    if text.startswith("module\n"):
        return text
    lines = text.splitlines(keepends=True)
    positions = [i for i, line in enumerate(lines) if line.startswith("import ")]
    if not positions:
        raise ValueError(f"No imports in {name}")
    for i in positions:
        lines[i] = "public " + lines[i]
    lines.insert(positions[-1] + 1, "\n@[expose] public section\n\n")
    return "module\n\n" + "".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--build-dir", required=True, type=Path)
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    source = packet / "lean"
    build = args.build_dir.resolve()
    if build.is_relative_to(packet):
        parser.error("--build-dir must be outside the packet")
    generated = build / "source"
    output = build / "lib"
    logs = build / "logs"
    for directory in [generated, output, logs]:
        directory.mkdir(parents=True, exist_ok=True)
    pins = json.loads((packet / "source-pins.json").read_text())
    for pin in pins["sources"]:
        actual = digest((source / pin["file"]).read_bytes())
        if actual != pin["sha256"]:
            raise ValueError(f"Frozen source hash mismatch: {pin['file']}")
    lean_version = subprocess.check_output([str(args.lean), "--version"], text=True).strip()
    if f"version {pins['lean']}" not in lean_version:
        raise ValueError(f"Wrong Lean version: {lean_version}")
    mathlib_head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=args.mathlib, text=True).strip()
    if mathlib_head != pins["mathlib_commit"]:
        raise ValueError(f"Wrong mathlib commit: {mathlib_head}")
    deps = [args.mathlib / ".lake/build/lib/lean"]
    deps.extend(sorted((args.mathlib / ".lake/packages").glob("*/.lake/build/lib/lean")))
    if not (deps[0] / "Mathlib/Analysis/SpecialFunctions/Log/Base.olean").exists():
        raise ValueError("The supplied mathlib cache is not built")
    env = dict(os.environ)
    env["LEAN_PATH"] = os.pathsep.join(str(p.resolve()) for p in [output, *deps])
    receipt = {
        "upstream_pr": pins["pr"], "upstream_head": pins["head"],
        "lean_version": lean_version, "mathlib_commit": mathlib_head,
        "module_port": "Headers and listed visibility declarations only; proof bodies unchanged.",
        "modules": [], "complete": False,
    }
    diff = []
    for module in MODULES:
        raw = (source / f"{module}.lean").read_text()
        modern = module_port(module, raw)
        path = generated / f"{module}.lean"
        path.write_text(modern)
        diff.extend(difflib.unified_diff(raw.splitlines(True), modern.splitlines(True),
                    fromfile=f"frozen/{module}.lean", tofile=f"generated/{module}.lean", n=0))
        record = {"module": module, "source_sha256": digest(raw.encode()),
                  "compiled_source_sha256": digest(modern.encode())}
        receipt["modules"].append(record)
    (build / "module-port.patch").write_text("".join(diff))
    if args.prepare_only:
        (build / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(f"Prepared {len(MODULES)} explicit module inputs; no compilation claimed.")
        return
    for record in receipt["modules"]:
        module = record["module"]
        command = [str(args.lean), "-j1"]
        # The new work must be warning-free. Preserve any upstream warnings in
        # the receipt instead of silently editing a frozen theorem source.
        if module not in {p["file"][:-5] for p in pins["sources"]}:
            command.append("-DwarningAsError=true")
        command.extend(["-o", str(output / f"{module}.olean"), f"{module}.lean"])
        print(f"Checking {module} ...", flush=True)
        start = time.monotonic()
        result = subprocess.run(command, cwd=generated, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        record.update(exit_code=result.returncode, elapsed_seconds=round(time.monotonic()-start, 3),
                      compiler_output_sha256=digest(result.stdout.encode()))
        (logs / f"{module}.log").write_text(result.stdout)
        print(result.stdout, end="", flush=True)
        if result.returncode:
            (build / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            raise SystemExit(result.returncode)
        if "sorryAx" in result.stdout:
            raise RuntimeError(f"Unfinished proof dependency in {module}")
        audits = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", result.stdout)
        record["axiom_audits"] = []
        for theorem, axioms in audits:
            names = {a.strip() for a in axioms.split(",") if a.strip()}
            if not names <= ALLOWED_AXIOMS:
                raise RuntimeError(f"Unexpected axiom in {theorem}: {names-ALLOWED_AXIOMS}")
            record["axiom_audits"].append({"theorem": theorem, "axioms": sorted(names)})
        if module == "Audit" and not audits:
            raise RuntimeError("Final theorem audit produced no audit output")
        print(f"Checked {module} in {record['elapsed_seconds']} seconds.", flush=True)
        (build / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    receipt["complete"] = True
    (build / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"All {len(MODULES)} modules passed. Receipt: {build / 'receipt.json'}", flush=True)


if __name__ == "__main__":
    main()
