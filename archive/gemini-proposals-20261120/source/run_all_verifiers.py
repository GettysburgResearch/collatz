#!/usr/bin/env python3
"""
Master Verification Runner for the GettysburgResearch/collatz Multi-Route Proposals Package.
Runs all five route verifiers, computes SHA-256 hashes of all package files, and writes
a deterministic verification_receipt.json.
"""

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent

VERIFIERS = [
    "route_1_merger_families_pr146/verify_merger_families.py",
    "route_2_inverse_compiler_sub2_pr147_148/verify_inverse_compiler.py",
    "route_3_all_word_potential_and_lyapunov_pr149/verify_lyapunov_potential.py",
    "route_4_diophantine_sc_fc_and_powered_cycles_pr148/verify_diophantine_cycles.py",
    "route_5_transducer_merging_and_lean4_kernel/verify_transducer_merging.py",
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
        if p.is_file() and p.name != "verification_receipt.json" and "__pycache__" not in p.parts:
            hashes[str(p.relative_to(ROOT))] = sha256_file(p)

    receipt = {
        "package": "collatz_multi_route_proposals_2026-11-20",
        "overall_status": "PASS" if all_passed else "FAIL",
        "non_claim_notice": "Local lemmas and bounded computational replays only; does NOT claim a Collatz proof.",
        "verifier_results": results,
        "file_sha256": hashes,
    }
    receipt_path = ROOT / "verification_receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"overall_status": receipt["overall_status"], "verifiers_run": len(results)}, indent=2))
    if not all_passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
