#!/usr/bin/env python3
"""Independent X-6801 verifier.

This file does not import run.py.  It reconstructs the mechanical counts,
canonical source/end pair by one-bit lifting, all finite rows, the semantic
digest, and the three exact induction bases.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def exact_count(m: int) -> int:
    q = 0
    lhs = 1
    rhs = 1 << m
    while lhs < rhs:
        lhs *= 3
        q += 1
    return q


def word_for(j: int) -> tuple[list[int], int]:
    c = [exact_count(m) for m in range(j)]
    return [c[m + 1] - c[m] for m in range(j - 1)] + [0], c[-1]


def lift_pair(bits: list[int]) -> tuple[int, int, int, int]:
    P = Q = 1
    r = s = 1
    A = 0
    q = 0
    for bit in bits:
        epsilon = (bit - s) & 1
        z = s + epsilon * Q
        new_r = r + epsilon * P
        new_s = ((3 if bit else 1) * z + bit) // 2
        new_A = (3 if bit else 1) * A + (P if bit else 0)
        P, Q = 2 * P, (3 if bit else 1) * Q
        r, s, A = new_r, new_s, new_A
        q += bit
        if P * s != Q * r + A:
            raise AssertionError("one-bit rectangle identity failed")
    return r, s, A, q


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    args = parser.parse_args()
    data = json.loads(args.canonical.read_text(encoding="utf-8"))

    if data["experiment_id"] != "X-6801":
        raise SystemExit("wrong experiment id")
    expected_rows = []
    for j in range(2, 373):
        bits, q = word_for(j)
        if not (3**q >= 1 << (j - 1) and 3**q < 1 << j):
            continue
        r, s, A, q2 = lift_pair(bits)
        if q != q2:
            raise AssertionError("weight mismatch")
        delta = r - s
        if j == 2:
            assert bits == [1, 0] and (r, s, delta) == (1, 1, 0)
        else:
            assert delta > 0
        expected_rows.append(
            {
                "j": j,
                "q": q,
                "word": "".join(str(b) for b in bits),
                "affine_numerator": str(A),
                "canonical_root": str(r),
                "canonical_endpoint": str(s),
                "descent_defect": str(delta),
            }
        )
    bases = []
    for j in (373, 374, 375):
        L = (j - 1) // 3
        H = 2 * ((1 << L) + 1) - 3 * (j - 1)
        bases.append(
            {
                "j": j,
                "factor_length": L,
                "lower_numerator": str(H),
                "lower_denominator": 6,
                "rhin_power_comparison": H > 0 and H**10 > 6**10 * j**143,
                "three_step_power_growth": (j + 3) ** 143 < 2**10 * j**143,
            }
        )
    if data["analytic_base_rows"] != bases:
        raise SystemExit("analytic base mismatch")

    lines = [
        f"{row['j']}:{row['q']}:{row['canonical_root']}:{row['canonical_endpoint']}:{row['descent_defect']}"
        for row in expected_rows
    ]
    lines.extend(
        f"B:{row['j']}:{row['factor_length']}:{row['lower_numerator']}:"
        f"{int(row['rhin_power_comparison'])}:{int(row['three_step_power_growth'])}"
        for row in bases
    )
    digest = hashlib.sha256(("\n".join(lines) + "\n").encode()).hexdigest()
    if digest != data["semantic_sha256"]:
        raise SystemExit("semantic digest mismatch")
    if data["valid_mechanical_rows"] != len(expected_rows):
        raise SystemExit("row-count mismatch")
    if data["first_valid_j"] != expected_rows[0]["j"]:
        raise SystemExit("first-row mismatch")
    if data["last_valid_j"] != expected_rows[-1]["j"]:
        raise SystemExit("last-row mismatch")
    positive = [row for row in expected_rows if int(row["descent_defect"]) > 0]
    minimum = min(positive, key=lambda row: (int(row["descent_defect"]), int(row["j"])))
    expected_minimum = {"j": minimum["j"], "defect": minimum["descent_defect"]}
    if data["minimum_positive_defect"] != expected_minimum:
        raise SystemExit("minimum-defect mismatch")
    sample_js = {2, 4, 5, 370, 371}
    expected_samples = [row for row in expected_rows if row["j"] in sample_js]
    if data["sample_rows"] != expected_samples:
        raise SystemExit("sample-row mismatch")
    if data["nontrivial_failures"] != 0:
        raise SystemExit("failure flag mismatch")
    print("all independent X-6801 checks passed")
    print(digest)


if __name__ == "__main__":
    main()
