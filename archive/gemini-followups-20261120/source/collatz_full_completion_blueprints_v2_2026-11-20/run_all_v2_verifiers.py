#!/usr/bin/env python3
"""
Master Verification Runner for Full-Completion Collatz Blueprints (v2).
Executes all 4 deep-completion blueprint verifiers and writes verification_receipt_v2.json.
"""

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent

VERIFIERS = [
    "blueprint_1_mahler_generating_function/verify_mahler_functional.py",
    "blueprint_2_dirichlet_ruelle_singularity/verify_dirichlet_ruelle.py",
    "blueprint_3_krasikov_lagarias_exponent_crossing/verify_exponent_crossing.py",
    "blueprint_4_adelic_w1_and_rational_cycle_separation/verify_adelic_w1.py",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main():
    results = []
    all_passed = True
    for rel in VERIFIERS:
        script = ROOT / rel
        proc = subprocess.run(
            [sys.executable, "-X", "utf8", "-B", str(script)],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            all_passed = False
            results.append({
                "script": rel,
                "status": "FAIL",
                "returncode": proc.returncode,
                "stderr": proc.stderr.strip(),
            })
        else:
            parsed = json.loads(proc.stdout)
            results.append({
                "script": rel,
                "status": parsed.get("status", "UNKNOWN"),
                "output": parsed,
            })

    hashes = {}
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p.name != "verification_receipt_v2.json" and "__pycache__" not in p.parts:
            hashes[str(p.relative_to(ROOT))] = sha256_file(p)

    receipt = {
        "package": "collatz_full_completion_blueprints_v2_2026-11-20",
        "overall_status": "PASS" if all_passed else "FAIL",
        "non_claim_notice": "Verified local theorems, identities, and full-completion research blueprints; does NOT claim a completed proof of Collatz.",
        "verifier_results": results,
        "file_sha256": hashes,
    }
    (ROOT / "verification_receipt_v2.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"overall_status": receipt["overall_status"], "verifiers_run": len(results)}, indent=2))
    if not all_passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
