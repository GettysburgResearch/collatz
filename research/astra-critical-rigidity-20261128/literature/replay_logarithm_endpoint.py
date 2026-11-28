"""Rebuild the October 2026 rational-log ratio and audit the 3/2 specialization."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from audit_logarithm_sources import LIB, STANDARD, digest, get_archive, read, verify_manifest


HERE = Path(__file__).resolve().parent
PROJECT_ROOT = "QuadraticPi.RationalTwoLogLinearForm"
PUBLIC_ROOTS = (
    "QuadraticPi.rationalLogRatio_finite_good",
    "QuadraticPi.rationalLogRatio_irrationalityExponent_bounds",
    "QuadraticPi.log_two_div_log_three_irrationalityExponent_bounds",
    "QuadraticPi.rationalTwoLog_linearForm_lowerBound",
)
LOCAL_ROOTS = tuple("Collatz.ChudnovskyLog32." + name for name in
                    ("exponent_bounds", "finite_good", "uniform_linear_form"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work", type=Path, help="fresh work directory with ample disk space")
    parser.add_argument("--archive", help="local arXiv 2610.28079v1 source archive")
    parser.add_argument("--no-cache-get", action="store_true", help="skip official Mathlib cache retrieval")
    args = parser.parse_args()
    args.work.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix="log-ratio-", dir=args.work.resolve()))
    with get_archive("october", args.archive) as archive:
        index = verify_manifest(archive, LIB + "SOURCE-MANIFEST.json")
        if digest(read(archive, "main.tex")) != index["manuscript_sha256"]:
            raise ValueError("October manuscript hash mismatch")
        archive.extractall(stage, filter="data")
    project = stage / LIB
    lake = [sys.executable, str(project / "scripts/bounded_lake.py")]
    compiler = subprocess.check_output(lake + ["env", "lean", "--version"], cwd=project, text=True)
    if "version 4.34.1," not in compiler or "5045d0056413266e57c625dcd7c365b10e377c52" not in compiler:
        raise ValueError("Lean compiler version or commit differs from the release")
    if not args.no_cache_get:
        subprocess.run(lake + ["exe", "cache", "get"], cwd=project, check=True)
    plan = subprocess.run(lake + ["build", PROJECT_ROOT], cwd=project)
    plan.check_returncode()
    wrapper = HERE / "ChudnovskyLog32.lean"
    shutil.copyfile(wrapper, project / wrapper.name)
    lines = ["import ChudnovskyLog32"]
    for root in (*PUBLIC_ROOTS, *LOCAL_ROOTS):
        lines.extend([f"#check {root}", f"#print axioms {root}"])
    (project / "PublicEndpointAudit.lean").write_text("\n".join(lines) + "\n")
    subprocess.run(lake + ["env", "lean", "-o", ".lake/build/lib/lean/ChudnovskyLog32.olean", wrapper.name],
                   cwd=project, check=True)
    output = subprocess.check_output(lake + ["env", "lean", "PublicEndpointAudit.lean"], cwd=project, text=True)
    for root in (*PUBLIC_ROOTS, *LOCAL_ROOTS):
        audit = re.search(re.escape("'" + root + "' depends on axioms: [") + r"([^\]]+)\]", output)
        if not audit or {word.strip() for word in audit[1].split(",")} != STANDARD:
            raise ValueError(f"Unexpected axiom audit for {root}")
    print(output)
    print(json.dumps({"compiler": compiler.strip(), "verified_roots": [*PUBLIC_ROOTS, *LOCAL_ROOTS],
                      "wrapper_sha256": digest(wrapper.read_bytes()), "stage": str(stage)}, indent=2))


if __name__ == "__main__":
    main()
