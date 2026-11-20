#!/usr/bin/env python3
"""Exact affine checks of SE-001, not a test of endpoint propagation."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def add(x, constant):
    return x[0], x[1] + constant


def scale(x, multiplier):
    return x[0] * multiplier, x[1] * multiplier


def divide(x, divisor):
    require(all(value % divisor == 0 for value in x),
            ("nonintegral affine quotient", x, divisor))
    return x[0] // divisor, x[1] // divisor


def residue(x, modulus):
    require(x[0] % modulus == 0, ("nonconstant residue", x, modulus))
    return x[1] % modulus


def shortcut(x):
    parity = residue(x, 2)
    return divide(x, 2) if parity == 0 else divide(add(scale(x, 3), 1), 2)


def nonnegative(x):
    return x[0] >= 0 and x[1] >= 0


def minus(x, y):
    return x[0] - y[0], x[1] - y[1]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    cells = []
    for r in (0, 1):
        m = (3, r)
        n = add(scale(m, 4), 1)
        a = add(scale(m, 15), 4)
        b = add(scale(m, 3), 1)
        require(residue(n, 4) == 1 and residue(n, 3) != 0, ("query domain", n))
        require(residue(b, 3) != 0, ("second query domain", b))
        require(shortcut(shortcut(n)) == b, ("first ordinary path", n))
        require(shortcut(shortcut(scale(n, 5))) == a, ("second ordinary path", n))
        require(add(a, 1) == scale(b, 5), ("adjacent identity", n))
        require(residue(a, 45) == 15 * r + 4, ("adjacent residue", a))
        require(minus(scale(a, 4), scale(n, 15)) == (0, 1), "first weight bound")
        require(nonnegative(minus(a, scale(b, 4))), "second weight bound")
        require(a[0] > 0 and n[0] > 0 and b[0] > 0, "injectivity")
        cells.append({"m": m, "n": n, "a": a, "b": b,
                      "adjacent_residue_mod_45": residue(a, 45)})

    excluded_m = (3, 2)
    excluded_n = add(scale(excluded_m, 4), 1)
    excluded_a = add(scale(excluded_m, 15), 4)
    require(residue(excluded_n, 3) == 0, "excluded query must not be a unit")
    require(residue(excluded_a, 45) == 34, "excluded adjacent class")
    require(Fraction(4, 15) + Fraction(1, 4) / (1 - Fraction(1, 2))
            == Fraction(23, 30), "harmonic constant")

    j = (5, 2)
    n = divide(add(scale(j, 72), 1), 5)
    b = divide(add(scale(j, 54), 2), 5)
    a = add(scale(j, 54), 1)
    require(residue(n, 4) == 1 and residue(n, 3) != 0, "sparse first query domain")
    require(residue(b, 3) != 0, "sparse second query domain")
    require(shortcut(shortcut(n)) == b, "sparse first path")
    require(shortcut(shortcut(scale(n, 5))) == a, "sparse second path")
    require(add(a, 1) == scale(b, 5), "sparse adjacent path")
    sparse_direct = {"j": j, "n": n, "a": a, "b": b}

    # The ordinary inverse adjacent-pair transport, over every a=3*k+1.
    old_a = (3, 1)
    new_a = divide(add(scale(old_a, 4), -1), 3)
    require(residue(new_a, 4) == 1, "adjacent transport parity")
    require(shortcut(shortcut(new_a)) == old_a, "adjacent transport first arm")
    require(shortcut(shortcut(add(new_a, 1))) == add(old_a, 1),
            "adjacent transport second arm")
    j = (5, 4)
    old_a = add(scale(j, 54), 1)
    a = add(scale(j, 72), 1)
    n = divide(add(scale(j, 96), 1), 5)
    b = divide(add(scale(j, 72), 2), 5)
    require(a == divide(add(scale(old_a, 4), -1), 3), "sparse transport identity")
    require(residue(a, 45) == 19, "transported sparse residue")
    require(residue(n, 4) == 1 and residue(n, 3) != 0, "transported first query")
    require(residue(b, 3) != 0, "transported second query")
    require(shortcut(shortcut(n)) == b, "transported first path")
    require(shortcut(shortcut(scale(n, 5))) == a, "transported second path")
    require(add(a, 1) == scale(b, 5), "transported adjacent path")
    require(minus(scale(old_a, 4), scale(a, 3)) == (0, 1),
            "transported harmonic weight comparison")
    require((1 + Fraction(4, 3)) * Fraction(23, 30) == Fraction(161, 90),
            "two quinary classes constant")
    sparse_transported = {"j": j, "n": n, "a": a, "b": b, "old_a": old_a}

    directory = Path(__file__).resolve().parent
    report = {
        "status": "PASS",
        "scope": "exact all-lift affine checks; no global energy or Collatz conclusion",
        "normalization": "positive shortcut map; metric invariant labels",
        "allowed_cells": cells,
        "excluded_cell": {"m": excluded_m, "n": excluded_n, "a": excluded_a,
                          "reason": "the required M5 query is divisible by three"},
        "harmonic_constant": "23/30",
        "oddpart_factor_at_s_one": "2",
        "sparse_target_direct": sparse_direct,
        "sparse_target_transported": sparse_transported,
        "two_quinary_classes_constant": "161/90",
        "source_hashes": {
            "checker": sha256(Path(__file__).resolve()),
            "single_slice_note": sha256(directory / "SINGLE_SLICE_ENERGY.md"),
            "critical_note": sha256(directory / "CRITICAL_SINGULARITY.md"),
        },
        "not_verified_by_this_script": [
            "PD external positive lower density theorem",
            "UP infinite synchronization estimate",
            "EP limiting logarithmic profile theorem",
            "propagation from the two adjacent classes to all adjacent edges",
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
