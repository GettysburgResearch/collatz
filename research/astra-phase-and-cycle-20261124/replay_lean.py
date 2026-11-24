"""Build the packet from fresh sources and audit the transitive axioms."""

import argparse
from datetime import datetime, timezone
from difflib import unified_diff
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

PACKET = Path(__file__).resolve().parent
MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
VENDOR_BLOB = "85385ac9b4dbc2bab8b3f78f02d4f865ed16d2b8"
VENDOR_SHA256 = "5b0f035ad14624376ce722bfdff5d9d216b266a0d7066efc3715fcc19d37f4a9"
SOURCES = ("vendor/ActualScalar.lean", "OneRun.lean", "OrdinaryShadow.lean",
           "PhaseBounds.lean", "ActualOneRun.lean", "AllAxioms.lean")
UPSTREAM = "Collatz.CarryTowerRoundTen.ActualScalar."
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def persist(output, record):
    temporary = output / "receipt.tmp"
    temporary.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output / "receipt.json")


def run(record, output, label, argv, cwd, env=None):
    argv = list(map(str, argv))
    step = {"command": argv, "cwd": str(cwd), "started": now(), "label": label}
    record["commands"].append(step)
    persist(output, record)
    proc = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    for channel in ("stdout", "stderr"):
        name = f"{len(record['commands']):02}-{label}.{channel}.log"
        (output / name).write_text(getattr(proc, channel), encoding="utf-8")
        step[channel] = name
    step.update(returncode=proc.returncode, finished=now())
    persist(output, record)
    require(proc.returncode == 0, f"{label} exited {proc.returncode}; see {step['stdout']} and {step['stderr']}")
    return proc.stdout


def visibility_port(data):
    # Only the initial import block changes. Preserve every byte of the body.
    lines = data.splitlines(keepends=True)
    i = 0
    while i < len(lines) and lines[i].startswith(b"import "):
        i += 1
    require(i > 0 and i < len(lines) and lines[i] == b"\n",
            "expected an initial import block followed by a blank line")
    return (b"module\n\n" + b"".join(b"public " + line for line in lines[:i]) +
            b"\npublic section\n\n" + b"".join(lines[i+1:]))


def check_audits(source_dir, output_text):
    names = re.findall(r"^#print axioms ([\w.]+)\s*$",
                       (source_dir / "AllAxioms.lean").read_text(), re.MULTILINE)
    require(len(names) == len(set(names)), "duplicate #print axioms directive")
    public = set()
    for source in SOURCES[1:-1]:
        body = (source_dir / source).read_text()
        namespaces = re.findall(r"^namespace ([\w.]+)$", body, re.MULTILINE)
        require(len(namespaces) == 1, f"update public audit inventory for namespaces in {source}")
        for name in re.findall(r"^(?:theorem|lemma) (\w+)", body, re.MULTILINE):
            public.add(namespaces[0] + "." + name)
    new = {n for n in names if not n.startswith(UPSTREAM)}
    require(public == new, f"public theorem inventory differs from AllAxioms: {public ^ new}")
    groups = {"new": {}, "upstream": {}}
    pattern = re.compile(r"'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)")
    seen = set()
    for match in pattern.finditer(output_text):
        name, items = match.groups()
        require(name in names and name not in seen, f"unexpected/duplicate axiom report: {name}")
        seen.add(name)
        axioms = [item.strip() for item in (items or "").split(",") if item.strip()]
        require(set(axioms) <= ALLOWED, f"{name}: unexpected axioms {set(axioms) - ALLOWED}")
        groups["upstream" if name.startswith(UPSTREAM) else "new"][name] = axioms
    require(seen == set(names), f"missing axiom reports: {set(names) - seen}")
    return {group: {"count": len(rows), "declarations": rows} for group, rows in groups.items()}


def replay(args, output, record):
    mathlib = args.mathlib.resolve(strict=True)
    executable = shutil.which(args.lean)
    require(executable is not None, f"Lean executable unavailable: {args.lean}")
    lean = Path(executable).absolute()
    version = run(record, output, "lean-version", [lean, "--version"], mathlib).strip()
    require(re.search(r"\bversion 4\.34\.1(?:,|\))", version), f"expected Lean 4.34.1, got {version}")
    head = run(record, output, "mathlib-head", ["git", "rev-parse", "HEAD"], mathlib).strip()
    require(head == MATHLIB, f"expected Mathlib {MATHLIB}, got {head}")
    record.update(lean_version=version, mathlib=str(mathlib), mathlib_head=head)
    record["source_head"] = run(record, output, "source-head",
                                ["git", "rev-parse", "HEAD"], PACKET).strip()
    record["source_status"] = run(record, output, "source-status",
                                  ["git", "status", "--short", "--", "."], PACKET)
    source_dir = output / "src"
    original_dir = output / "src-original"
    build = output / "olean"
    original_dir.mkdir()
    source_dir.mkdir()
    build.mkdir()
    manifest_data = (PACKET / "VENDOR.json").read_bytes()
    manifest = json.loads(manifest_data)
    record["vendor_manifest_sha256"] = sha256(manifest_data)
    require(manifest["toolchain"] == "leanprover/lean4:v4.34.1" and
            manifest["mathlib_commit"] == head and manifest["local_path"] == SOURCES[0],
            "vendor manifest toolchain, Mathlib or path does not match replay")
    require(manifest["git_blob"] == VENDOR_BLOB and manifest["sha256"] == VENDOR_SHA256,
            "vendor manifest disagrees with the packet's frozen pins")
    record["sources"] = {}
    record["compiled_sources"] = {}
    record["source_mode"] = "generated visibility-only port" if args.module_port else "byte-exact"
    patch = []
    for source in SOURCES:
        data = (PACKET / source).read_bytes()
        digest = sha256(data)
        if source == SOURCES[0]:
            blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            require(blob == VENDOR_BLOB and digest == VENDOR_SHA256, "vendor bytes differ from pin")
            record["vendor_git_blob"] = blob
        name = Path(source).name
        (original_dir / name).write_bytes(data)
        generated = visibility_port(data) if args.module_port else data
        (source_dir / name).write_bytes(generated)
        record["sources"][source] = digest
        record["compiled_sources"][name] = sha256(generated)
        if args.module_port:
            patch.extend(unified_diff(data.decode().splitlines(keepends=True),
                                      generated.decode().splitlines(keepends=True),
                                      fromfile="original/" + name, tofile="generated/" + name))
    if args.module_port:
        patch_bytes = "".join(patch).encode()
        (output / "visibility-port.patch").write_bytes(patch_bytes)
        record["visibility_port_patch_sha256"] = sha256(patch_bytes)
    path = args.lean_path
    if path is None:
        path = run(record, output, "lake-lean-path",
                   [lean.with_name("lake"), "env", "printenv", "LEAN_PATH"], mathlib).strip()
    require(path and "\n" not in path, "expected exactly one nonempty LEAN_PATH")
    paths = [(mathlib / item).resolve() for item in path.split(os.pathsep) if item]
    mathlib_lib = mathlib / ".lake" / "build" / "lib" / "lean"
    for line in (original_dir / "ActualScalar.lean").read_text().splitlines():
        if line.startswith("import Mathlib."):
            module = Path(*line.split()[1].split(".")).with_suffix(".olean")
            first = next((p for p in paths if (p / module).is_file()), None)
            require(first == mathlib_lib, f"{module} must resolve to the pinned Mathlib; got {first}")
    env = {**os.environ, "LEAN_PATH": os.pathsep.join(map(str, [build, *paths]))}
    record["lean_path"] = env["LEAN_PATH"]
    record["objects"] = {}
    record["companion_objects"] = {}
    for source in SOURCES:
        name = Path(source).stem
        obj = build / (name + ".olean")
        stdout = run(record, output, name,
                     [lean, "-j1", "-DwarningAsError=true", "-o", obj, name + ".lean"],
                     source_dir, env)
        require(obj.is_file() and obj.stat().st_size > 0, f"missing fresh {name}.olean")
        record["objects"][name] = sha256(obj.read_bytes())
        for companion in sorted(build.glob(name + ".olean.*")):
            record["companion_objects"][companion.name] = sha256(companion.read_bytes())
        if name == "AllAxioms":
            record["axioms"] = check_audits(source_dir, stdout)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, help="Lean 4.34.1 executable")
    parser.add_argument("--mathlib", required=True, type=Path, help="existing pinned, built Mathlib checkout")
    parser.add_argument("--lean-path", help="existing dependency search path; default comes from sibling Lake")
    parser.add_argument("--module-port", action="store_true",
                        help="compile generated module/public import/public section headers; retain exact originals and diff")
    parser.add_argument("--output", required=True, type=Path, help="empty or new directory outside the repository")
    args = parser.parse_args()
    repo = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                        cwd=PACKET, text=True).strip()).resolve()
    output = args.output.resolve()
    if output.is_relative_to(repo) or (output.exists() and
            (not output.is_dir() or any(output.iterdir()))):
        parser.error("--output must be an empty or new directory outside the repository")
    output.mkdir(parents=True, exist_ok=True)
    with (output / "receipt.json").open("x", encoding="utf-8") as stream:
        stream.write("{}\n")
    record = {"status": "running", "started": now(), "commands": [],
              "replay_sha256": sha256(Path(__file__).read_bytes()),
              "allowed_axioms": sorted(ALLOWED)}
    try:
        replay(args, output, record)
        record["status"] = "passed"
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        record.update(status="failed", error=str(error))
        print(str(error), file=sys.stderr)
    finally:
        record["finished"] = now()
        persist(output, record)
    print(output / "receipt.json")
    return 0 if record["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
