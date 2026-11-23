"""Verify the unit-residue comparable pair without a full word enumeration."""

import argparse
import json
from math import gcd
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--complete-fiber", action="store_true")
args = parser.parse_args()
data = json.loads(Path(__file__).with_name("maxfiber_35_22.json").read_text())
A, p, D, r = (data[k] for k in ("A", "p", "D", "r"))
assert (A, p, D, r) == (35, 22, 2978678759, 2209100811)
assert D == 2**A - 3**p and gcd(r, D) == 1 and gcd(A, p) == 1

by_part = {}
for item in data["words"]:
    positions = item["positions"]
    assert len(positions) == p
    assert all(0 <= d < A for d in positions)
    assert all(a < b for a, b in zip(positions, positions[1:]))
    C = sum(2**d * 3 ** (p - 1 - i) for i, d in enumerate(positions))
    assert C == item["C"] == r + item["integer_part"] * D
    assert item["integer_part"] not in by_part
    by_part[item["integer_part"]] = tuple(positions)
assert sorted(by_part) == [44, 68, 104, 122, 134, 158, 172, 233, 482]

u, v = by_part[44], by_part[233]
assert all(a <= b for a, b in zip(u, v)) and u != v
assert 696241251658 - 133270966207 == 189 * D

if args.complete_fiber:
    low_C = 3**p - 2**p
    high_C = 2 ** (A - p) * low_C
    low_k = max(0, (low_C - r + D - 1) // D)
    high_k = (high_C - r) // D
    assert [low_k, high_k] == data["quotient_bounds"] == [10, 86292]
    recovered = {}
    for k in range(low_k, high_k + 1):
        C = r + k * D
        x = C
        positions = []
        for t in range(A):
            if x % 2:
                positions.append(t)
                x = (3 * x + D) // 2
            else:
                x //= 2
        if x == C and len(positions) == p:
            recovered[k] = tuple(positions)
    assert recovered == by_part
    print("Complete selected fiber recovered from 86,283 exact numerator candidates.")

print("Verified nine distinct unit-residue witnesses and the coordinatewise comparable pair.")
