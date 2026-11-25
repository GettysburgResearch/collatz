"""Build the frozen PR 206 modules, then compile and audit the clock bridge."""

import argparse
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


SOURCE_HASHES = {
    "TernaryItinerary": "b6a2bce0e51455a8c5177a473b751219da82021086e158698564cb4c920b6b56",
    "FixedGate": "d6663ef25ccc82f53c1eff91a59fc13350e5d42939455fa4e5cbbb4f59013360",
    "CycleRows": "c00508d25bb8b72fc128181b2c08721102fc552da5b5436d51a1b40d04cf74f0",
    "CycleDetection": "36fe77bda861ff82a6d1f7ec6846df0542d8d7b0bdc617e314703843987004d0",
    "CycleAmplification": "3b6d3d6f64d97fe50291c8d0a073e8d9beb9efb7032ca701f909e7475b33a689",
    "ClosureProposal": "eb91552efac88b983f174b491b0dca06fdc786348d0753994381f60054d8ee21",
}

PUBLIC = {
    "rowSum_eq_range", "ordinary_lift", "ordinary_pressure", "high_odd_row_bound",
    "clock_le_implies_odds", "clock_failure_bound", "exponentially_sparse_clock",
    "balanced_forces_cross", "balanced_suffix_iff", "balanced_failure_needs_suffix",
    "early_balanced_height", "aligned_balanced_height", "minimum_tail_fails", "crossing_predecessor", "backward_transfer_control",
    "unit_prefix", "arbitrarily_long_failure", "split_pair", "pair_left_crosses",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default="lean", help="Lean 4.34.1 executable")
    args = parser.parse_args()
    found = shutil.which(args.lean)
    if not found:
        raise SystemExit(f"Lean executable not found: {args.lean}")
    lean = str(Path(found).resolve())
    version = subprocess.check_output([lean, "--version"], text=True).strip()
    if not version.startswith("Lean (version 4.34.1,"):
        raise SystemExit(f"expected Lean 4.34.1, found {version}")
    print(version, flush=True)
    clock = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(prefix="collatz-clock-") as tmp:
        env = dict(os.environ, LEAN_PATH=tmp)
        for name in [*SOURCE_HASHES, "ClockBridge"]:
            frozen = name in SOURCE_HASHES
            source = (clock / "pr206" if frozen else clock.parent / "formal") / (name + ".lean")
            if frozen and hashlib.sha256(source.read_bytes()).hexdigest() != SOURCE_HASHES[name]:
                raise SystemExit(f"pinned bytes differ: {source}")
            options = ["-DautoImplicit=false"]
            if not frozen:
                options.append("-DwarningAsError=true")
            cmd = [lean, *options, "-o", str(Path(tmp) / (name + ".olean")), source.name]
            build = subprocess.run(cmd, cwd=source.parent, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(build.stdout, end="", flush=True)
            build.check_returncode()
            if not frozen:
                claims = re.findall(
                    r"'Collatz\.Itinerary\.ClockBridge\.(\w+)' "
                    r"(?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",
                    build.stdout,
                )
                if {name for name, _ in claims} != PUBLIC:
                    raise SystemExit("public axiom audit was incomplete")
                for claim, axioms in claims:
                    allowed = {"propext", "Quot.sound"}
                    if claim in {"minimum_tail_fails", "balanced_failure_needs_suffix"}:
                        allowed.add("Classical.choice")
                    for axiom in filter(None, (part.strip() for part in axioms.split(","))):
                        if axiom not in allowed:
                            raise SystemExit(f"unexpected axiom for {claim}: {axiom}")
    print(f"verified {len(SOURCE_HASHES)} frozen sources and {len(PUBLIC)} public declarations")


if __name__ == "__main__":
    main()
