"""Compile the fixed-source Collatz certificate in parallel Lean modules."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contents(source):
    raw = source.read_text(encoding="utf-8").replace("\r\n", "\n").strip()
    start = raw.index("private theorem assemble")
    pre, proof = raw[:start], raw[start:]
    edge_pattern = r"^private theorem edge(\d+) : run .+? := checked_edge.+$"
    edges = list(re.finditer(edge_pattern, pre, re.M))
    if [int(m.group(1)) for m in edges] != list(range(48)):
        raise ValueError("expected every original edge exactly once and in order")
    base = re.sub(edge_pattern, "", pre, flags=re.M)
    # The shared module exposes the same definitions and proof terms to the six batches.
    base = base.replace("@[reducible] private def cp0", "private def cp0")
    base = base.replace("private def ", "def ").replace("private theorem ", "theorem ")
    base = base.rstrip() + "\nend Collatz.Itinerary.ReturnDescent\n"
    units = {"ReturnDescentLongBase": base}
    batch_names = []
    for batch in range(6):
        name = f"ReturnDescentLongBatch{batch}"
        batch_names.append(name)
        proofs = [m.group().removeprefix("private ") for i, m in enumerate(edges) if i % 6 == batch]
        units[name] = ("module\npublic import ReturnDescentLongBase\n"
            "import all ReturnDescentLongBase\nimport all TernaryItinerary\n"
            "public section\nnamespace Collatz.Itinerary.ReturnDescent\n"
            "set_option maxRecDepth 100000\nset_option maxHeartbeats 4000000\n"
            + "\n".join(proofs) + "\nend Collatz.Itinerary.ReturnDescent\n")
    units["ReturnDescentLongReceipt"] = ("module\n"
        + "\n".join("public import " + name for name in batch_names)
        + "\nimport all ReturnDescentLongBase\nimport all TernaryItinerary\n"
          "public section\nnamespace Collatz.Itinerary.ReturnDescent\n"
          "set_option maxRecDepth 100000\n" + proof)
    return units, batch_names


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--dependencies", type=Path, required=True, help="directory holding the compiled ReturnDescent and its dependencies")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--jobs", type=int, default=6)
    parser.add_argument("--check-sources", action="store_true", help="compare generated module contents to an existing scratch replay")
    args = parser.parse_args()
    units, batches = contents(args.source)
    args.out.mkdir(parents=True, exist_ok=True)
    for name, body in units.items():
        path = args.out / (name + ".lean")
        if args.check_sources:
            if body.strip() != path.read_text(encoding="utf-8").strip():
                raise ValueError(f"derived source differs: {name}")
        else:
            path.write_text(body.rstrip() + "\n", encoding="utf-8")
    if args.check_sources:
        print(f"{len(units)} derived modules match the frozen source, modulo terminal newlines")
        return
    env = dict(os.environ)
    libs = [str(args.out.resolve()), str(args.dependencies.resolve())]
    if env.get("LEAN_PATH"):
        libs.append(env["LEAN_PATH"])
    env["LEAN_PATH"] = os.pathsep.join(libs)
    flags = ["-j1", "-DwarningAsError=true", "-DautoImplicit=false", "-DElab.async=false"]
    def build(name):
        path = args.out / (name + ".lean")
        obj = args.out / (name + ".olean")
        started = time.monotonic()
        proc = subprocess.run([str(args.lean.resolve()), *flags, "-o", str(obj.resolve()), path.name],
                              cwd=args.out, env=env, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
        print(proc.stdout + proc.stderr, end="", flush=True)
        if proc.returncode:
            raise RuntimeError(f"Lean rejected {name} with code {proc.returncode}")
        log = proc.stdout + proc.stderr
        if name == "ReturnDescentLongReceipt":
            reports = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", log)
            axioms = {a.strip() for report in reports for a in report.split(",") if a.strip()}
            if len(reports) != 1 or axioms - {"propext", "Classical.choice", "Quot.sound"}:
                raise ValueError(f"unexpected axiom audit for {name}: {log}")
        return {"module": name, "source_sha256": digest(path), "olean_sha256": digest(obj),
                "seconds": round(time.monotonic() - started, 2), "lean_output": proc.stdout + proc.stderr}
    checked = [build("ReturnDescentLongBase")]
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        checked += list(pool.map(build, batches))
    checked.append(build("ReturnDescentLongReceipt"))
    receipt = {"standalone_sha256": digest(args.source), "strict_flags": flags, "verified": checked}
    (args.out / "replay-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
