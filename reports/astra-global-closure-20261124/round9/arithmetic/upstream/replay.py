"""Verify the two targeted source inventories or rebuild one and save its full logs."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
RECEIPT = json.loads((HERE / "audit_receipt.json").read_text())
REPORT_PATTERN = re.compile(
    r"^'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])$",
    re.MULTILINE,
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def bound_bytes(row):
    path = row["source"]
    if row["revision"]:
        data = subprocess.check_output(["git", "show", row["revision"] + ":" + path], cwd=REPO)
    else:
        data = (REPO / path).read_bytes()
        normalization = row.get("publication_normalization")
        if normalization:
            check(digest(data) == normalization["published_source_sha256"],
                  "normalized publication source hash mismatch: " + path)
            # Reconstruct the exact originally audited bytes, not a new proof claim.
            data += normalization["removed_trailing_bytes"].encode()
    check(digest(data) == row["sha256"], "source hash mismatch: " + path)
    return data


def read_reports(data):
    rows = REPORT_PATTERN.findall(data.decode())
    reports = {name: sorted(a.strip() for a in group.split(",") if a) for name, group in rows}
    check(len(reports) == len(rows), "duplicate theorem name in compiler reports")
    return reports


def verify(run):
    stdout = (HERE / run["original_stdout"]).read_bytes()
    check(digest(stdout) == run["original_stdout_sha256"], "agent console digest mismatch")
    report_count = 0
    for row in run["modules"]:
        src = bound_bytes(row).decode()
        if row["action"] == "dependency":
            continue
        namespace = re.search(r"^namespace ([\w.]+)", src, re.MULTILINE).group(1)
        declared = [namespace + "." + name for name in re.findall(r"^theorem ([\w.]+)", src, re.MULTILINE)]
        wanted = row["expected_reports"]
        check(declared == list(wanted), "public inventory differs: " + row["source"])
        old_reports = read_reports(bound_bytes(row["corroborating_log"]))
        if row["source"].endswith("/BarrierEnvelope.lean"):
            helper = RECEIPT["supplementary_helper_query"]
            data = (HERE / helper["log"]).read_bytes()
            check(digest(data) == helper["log_sha256"], "helper log digest mismatch")
            check(row["sha256"] == helper["input_module_source_sha256"], "helper source mismatch")
            old_reports.update(read_reports(data))
        check(old_reports == wanted, "archived reports differ: " + row["source"])
        check(all(set(a) <= set(RECEIPT["allowed_axioms"]) for a in wanted.values()), "unexpected axiom")
        report_count += len(declared)
    check(report_count == run["public_theorem_count"], "total public inventory differs")
    for row in run.get("controls", []):
        bound_bytes(row)
    return report_count


def execute(run, lean, mathlib, logs):
    lean = lean.resolve()
    check(digest(lean.read_bytes()) == RECEIPT["compiler_sha256"], "compiler digest differs")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    check(version == RECEIPT["compiler"], "compiler version differs")
    logs.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="collatz-targeted-audit-") as temp:
        work = Path(temp)
        paths = [work]
        if run.get("controls"):
            check(mathlib is not None, "upstream65 needs --mathlib")
            mathlib = mathlib.resolve()
            sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib, text=True).strip()
            check(sha == RECEIPT["mathlib_revision"], "Mathlib revision differs")
            paths.append(mathlib / ".lake/build/lib/lean")
            paths.extend(sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean")))
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
        imports = []
        reports = {}
        commands = []

        def capture(name, argv):
            proc = subprocess.run(argv, cwd=work, env=env, capture_output=True)
            output = proc.stdout + proc.stderr
            (logs / (name + ".log")).write_bytes(output)
            commands.append({"label": name, "argv": argv, "returncode": proc.returncode, "log_sha256": digest(output)})
            check(proc.returncode == 0, "command failed; see " + str(logs / (name + ".log")))
            return output

        for row in run["modules"]:
            filename = Path(row["source"]).name
            module = Path(filename).stem
            (work / filename).write_bytes(bound_bytes(row))
            capture(module, [str(lean), *run["flags"], "-o", module + ".olean", filename])
            if row["action"] == "audit":
                imports.append("import " + module)
                reports.update(row["expected_reports"])
        harness = "\n".join(imports + ["#print axioms " + name for name in reports]) + "\n"
        (work / "Audit.lean").write_text(harness)
        (logs / "harness.txt").write_text(harness)
        output = capture("all_public_theorems", [str(lean), *run["flags"], "Audit.lean"])
        check(read_reports(output) == reports, "fresh and archived public theorem inventories differ")
        for row in run.get("controls", []):
            filename = Path(row["source"]).name
            (work / filename).write_bytes(bound_bytes(row))
            for mode, flags in (("normal", []), ("optimized", ["-O"])):
                output = capture(Path(filename).stem + "_" + mode, [sys.executable, *flags, "-B", filename])
                check(digest(output) == row["combined_output_sha256"], "control output differs: " + filename)
    result = {"compiler": version, "flags": run["flags"], "theorem_count": len(reports), "commands": commands}
    (logs / "replay_result.json").write_text(json.dumps(result, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", choices=RECEIPT["runs"], help="rebuild one audit after verifying the sources")
    parser.add_argument("--lean", type=Path)
    parser.add_argument("--mathlib", type=Path)
    parser.add_argument("--logs", type=Path, help="destination for the new full compiler streams")
    args = parser.parse_args()
    names = [args.run] if args.run else RECEIPT["runs"]
    for name in names:
        run = RECEIPT["runs"][name]
        print(f"{name}: {verify(run)} theorem names, source hashes and archived results verified")
    if args.run:
        if args.lean is None or args.logs is None:
            parser.error("--run requires --lean and --logs")
        execute(RECEIPT["runs"][args.run], args.lean, args.mathlib, args.logs.resolve())


if __name__ == "__main__":
    main()
