"""Compile the finite fixed-source gcd proof and audit its declared axioms.

This checks only the six named finite arithmetic theorems. The written
asymptotic, analytic, probabilistic and Collatz closure claims are outside
the formalization.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile


THEOREMS = (
    "affine_gcd_exact",
    "affine_gcd_dvd_displacement",
    "collatz_prefix_gcd_exact",
    "collatz_prefix_gcd_le_displacement",
    "prefix_affine_from_edges",
    "all_prefix_gcd_le_displacement",
)
ALLOWED_AXIOMS = {"propext", "Quot.sound"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    lean = args.lean.resolve(strict=True)
    source = Path(__file__).with_name("FixedSourcePrefixGcd.lean").resolve()
    version = subprocess.run([str(lean), "--version"], text=True,
                             capture_output=True, check=False)
    require(version.returncode == 0, "Lean version command failed")
    require("Lean (version 4.34.1," in version.stdout,
            "This receipt is pinned to Lean 4.34.1")

    with tempfile.TemporaryDirectory(prefix="collatz-prefix-gcd-") as tmp:
        artifact = Path(tmp) / "FixedSourcePrefixGcd.olean"
        command = [str(lean), "-DwarningAsError=true", "-o", str(artifact),
                   str(source)]
        result = subprocess.run(command, text=True, capture_output=True,
                                cwd=source.parent, check=False)
        require(result.returncode == 0,
                "Lean compilation failed:\n" + result.stdout + result.stderr)
        require(artifact.is_file() and artifact.stat().st_size > 0,
                "Fresh Lean object file was not produced")
        records = {}
        for theorem in THEOREMS:
            name = "FixedSourcePrefixGcd." + theorem
            pattern = (r"'" + re.escape(name)
                       + r"' depends on axioms: \[([^\]]*)\]")
            match = re.search(pattern, result.stdout)
            require(match is not None, "Missing axiom audit for " + name)
            axioms = {a.strip() for a in match.group(1).split(",") if a.strip()}
            require(axioms <= ALLOWED_AXIOMS,
                    "Unexpected axioms for " + name + ": " + repr(axioms))
            records[name] = sorted(axioms)
        require("sorryAx" not in result.stdout + result.stderr,
                "A proof placeholder occurred in the compiled audit")
        receipt = {
            "status": "PASS",
            "scope": "six finite arithmetic theorems; no asymptotic or Collatz closure theorem",
            "source": str(source),
            "source_sha256": digest(source),
            "checker_sha256": digest(Path(__file__)),
            "compiler": str(lean),
            "compiler_version": version.stdout.strip(),
            "compiler_sha256": digest(lean),
            "command": command,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "fresh_olean_emitted": True,
            "olean_sha256": digest(artifact),
            "axioms": records,
            "mathlib_used": False,
        }
    output = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.receipt is not None:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
