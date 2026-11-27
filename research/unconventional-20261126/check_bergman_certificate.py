#!/usr/bin/env python3
"""Independently check a positive table on all three actual ternary lifts.

This verifier does not run or import the supersolution search. It checks the
original lifted transfer inequality at every residue modulo 3^(h+1), using
integers only. The table's standard SHA identifies the published certificate.
"""

import argparse
import hashlib
import json
from pathlib import Path


NUMERATOR = 5516102802
DENOMINATOR = 2482245023
EXPECTED_HASH = "91170eb02223527b842d0e06d8370ba6e8278f71f5a108f33075660de54dae88"


def verify(values, numerator=NUMERATOR, denominator=DENOMINATOR):
    modulus = len(values)
    if modulus != 3**10 or any(type(v) is not int or v <= 0 for v in values):
        raise ValueError("the certificate must have 3^10 strictly positive integer entries")
    if numerator <= 0 or denominator <= 0:
        raise ValueError("invalid positive bound")
    rows = 0
    for endpoint in range(3 * modulus):
        # Three times L(v), at this actual lift, with no maximum shortcut.
        lhs = 6 * values[(2 * endpoint) % modulus]
        if endpoint % 3 == 2:
            predecessor = (2 * endpoint - 1) // 3
            lhs += 2 * values[predecessor % modulus]
        rhs = 3 * numerator * values[endpoint % modulus]
        if denominator * lhs > rhs:
            raise ValueError(f"supersolution inequality fails at lifted residue {endpoint}")
        rows += 1
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vector", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    data = args.vector.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_HASH:
        raise SystemExit("published certificate hash mismatch")
    values = [int(line) for line in data.decode("ascii").splitlines()]
    rows = verify(values)
    corruptions = []
    for name, candidate, numerator in (
        ("zero_entry", [0, *values[1:]], NUMERATOR),
        ("lowered_branch_entry", [*values[:2], 1, *values[3:]], NUMERATOR),
        ("claimed_radius_sqrt_two", values, 2 * DENOMINATOR),
    ):
        try:
            verify(candidate, numerator=numerator)
        except ValueError:
            corruptions.append(name)
        else:
            raise RuntimeError(f"corruption unexpectedly accepted: {name}")
    receipt = {
        "scope": "all lifted residue inequalities for the stated Bergman upper bound",
        "entries": len(values),
        "lifted_rows_checked": rows,
        "vector_sha256": digest,
        "upper_squared": f"{NUMERATOR}/{DENOMINATOR}",
        "mutations_rejected": corruptions,
        "analytic_bridge": "BERGMAN_RADIUS.md, positive supersolution and published norm identity",
        "not_claimed": "exact radius, all operator-theorem formalization, or Collatz convergence",
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    if args.receipt:
        args.receipt.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()
