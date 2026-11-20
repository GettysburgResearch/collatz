#!/usr/bin/env python3
"""Narrow, optimization-stable replay of the uploaded routes 1 and 5.

The attachment is an explicit input, not an imported mathematical authority.
This checks local arithmetic and exposes the rank-domain validation defect.
It does not establish a complete selector or Collatz convergence.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path


SOURCES = {
    "r1": (
        "route_1_merger_families_pr146/verify_merger_families.py",
        "918bfd76af673d1ca950262dc1f5e07607ee0afeeb3056d8d02b109efac4eac9",
    ),
    "r5": (
        "route_5_transducer_merging_and_lean4_kernel/verify_transducer_merging.py",
        "bcb71c5f35614017c11daddc0ba8f184c6384c08e753a94d87ebadb7afa97066",
    ),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_source(root, name):
    relative, digest = SOURCES[name]
    path = root / relative
    require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
            "Attachment source hash mismatch: " + relative)
    spec = importlib.util.spec_from_file_location("audited_attachment_" + name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def cylinder_endpoint(m, r, slope, offset, clock):
    """Replay whole-class legality and endpoint as coefficients of k."""
    a, b, odds = slope * 2**m, slope * r + offset, 0
    for _ in range(clock):
        require(a % 2 == 0, "Parity is not fixed on the full cylinder")
        if b % 2:
            a, b, odds = 3 * a // 2, (3 * b + 1) // 2, odds + 1
        else:
            a, b = a // 2, b // 2
    return a, b, odds


def collision_valid(row):
    left = cylinder_endpoint(row["m"], row["r"], 1, 0, row["s_n"])
    right = cylinder_endpoint(row["m"], row["r"], 3, 0, row["s_3n"])
    return (left[:2] == right[:2] == (row["A"], row["B"])
            and row["s_n"] == row["s_3n"] and left[2] == right[2] + 1)


def antichain_density(rows):
    for i, row in enumerate(rows):
        for other in rows[:i]:
            precision = min(row["m"], other["m"])
            require(row["r"] % 2**precision != other["r"] % 2**precision,
                    "Overlapping reported cylinder leaves")
    return sum((Fraction(1, 2**row["m"]) for row in rows), Fraction(0))


def independent_descent_residues():
    """Recount at fixed modulus using rational affine words from base orbits."""
    modulus, count = 1024, 0
    for residue in range(modulus):
        base, multiplier, remainder = residue, Fraction(1), Fraction(0)
        for _ in range(10):
            odd = base % 2
            scale = Fraction(3 if odd else 1, 2)
            multiplier *= scale
            remainder = scale * remainder + Fraction(odd, 2)
            base = step(base)
            a = multiplier * modulus
            b = multiplier * residue + remainder
            require(a.denominator == b.denominator == 1,
                    "Nonintegral endpoint on a fixed binary cylinder")
            first_k = int(residue == 0)
            if a < modulus and a * first_k + b < modulus * first_k + residue:
                count += 1
                break
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proposal-root", type=Path, required=True)
    args = parser.parse_args()
    r1, r5 = (load_source(args.proposal_root, name) for name in ("r1", "r5"))

    collisions, reported_density = r1.check_n_3n_affine_collisions()
    require(len(collisions) == 43, "Changed merger leaf count")
    require(all(collision_valid(row) for row in collisions), "False affine merger")
    require(antichain_density(collisions) == reported_density == Fraction(41, 256),
            "Changed merger density")
    corrupted = dict(collisions[0], B=collisions[0]["B"] + 1)
    require(not collision_valid(corrupted), "Corrupted intercept accepted")

    contractions, contraction_density = r1.check_5t1_contraction_classes()
    require(len(contractions) == 33, "Changed second-arm contraction count")
    for row in contractions:
        a, b, _ = cylinder_endpoint(row["m"], row["r"], 5, 1, row["s"])
        require((a, b) == (row["A"], row["B"]), "False contraction endpoint")
        modulus, k0 = 2**row["m"], int(row["r"] == 0)
        require(a < modulus and a * k0 + b < modulus * k0 + row["r"],
                "Contraction fails on the first positive lift")
    require(antichain_density(contractions) == contraction_density == Fraction(59, 128),
            "Changed second-arm contraction density")

    witness = r5.find_physical_merger_for_source(121, max_steps=25)
    require(witness == {"source": 121, "witness": 91, "clock_source": 2,
                        "clock_witness": 0, "endpoint": 91}, "Changed source-121 witness")
    require(step(step(121)) == 91 < 121, "False direct descent")
    leaves, density = r5.transducer_descent_coverage()
    residue_count = independent_descent_residues()
    require((leaves, density) == (34, Fraction(959, 1024)) and residue_count == 959,
            "Independent descent recount disagrees")

    negative_rank = [((0, 1, 0), (-1, 100, 100))]
    require(r5.verify_lexicographic_transducer(negative_rank) is True,
            "Expected attachment domain defect was not reproduced")
    require(any(c < 0 for edge in negative_rank for rank in edge for c in rank),
            "Invalid-domain control does not leave the naturals")

    result = {
        "status": "PASS_LOCAL_AUDIT_ONLY",
        "source_hashes": {rel: digest for rel, digest in SOURCES.values()},
        "route1_affine_leaves": len(collisions),
        "route1_affine_density": str(reported_density),
        "route1_second_arm_contraction_leaves": len(contractions),
        "route1_second_arm_contraction_density": str(contraction_density),
        "route5_forward_descent_leaves": leaves,
        "route5_forward_descent_residues_mod1024": residue_count,
        "source121": witness,
        "corrupted_intercept_rejected": True,
        "attachment_negative_coordinate_bug_reproduced": True,
        "complete_selector_established": False,
        "collatz_proved": False,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
