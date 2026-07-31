#!/usr/bin/env python3
"""X-6801: exact upper-mechanical first-crossing descent certificate.

All decisions use Python integers.  The only imported analytic ingredient in the
associated theorem is Rhin's lower bound lambda >= j^(-13.3), not checked here.
This program certifies the finite range and the exact induction base used by the
all-length argument.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def ceil_alpha_times(m: int) -> int:
    """ceil(m*log(2)/log(3)), using only exact integer comparisons."""
    if m < 0:
        raise ValueError("m must be nonnegative")
    q = 0
    p3 = 1
    target = 1 << m
    while p3 < target:
        q += 1
        p3 *= 3
    return q


def mechanical_word(j: int) -> tuple[list[int], int]:
    if j < 2:
        raise ValueError("j must be at least 2")
    counts = [ceil_alpha_times(m) for m in range(j)]
    bits = [counts[m + 1] - counts[m] for m in range(j - 1)]
    bits.append(0)
    return bits, counts[-1]


def affine(bits: list[int]) -> tuple[int, int, int]:
    A = 0
    q = 0
    for m, bit in enumerate(bits):
        if bit not in (0, 1):
            raise AssertionError("nonbinary bit")
        A = (3 if bit else 1) * A + (1 << m if bit else 0)
        q += bit
    return len(bits), q, A


def canonical_pair(bits: list[int]) -> tuple[int, int, int, int]:
    j, q, A = affine(bits)
    P = 1 << j
    Q = 3**q
    r = (-A * pow(Q, -1, P)) % P
    if r == 0:
        r = P
    numerator = Q * r + A
    if numerator % P:
        raise AssertionError("canonical endpoint is not integral")
    s = numerator // P
    if not (1 <= r <= P and 1 <= s <= Q):
        raise AssertionError("canonical pair outside its rectangle")
    return r, s, A, q


def valid_first_crossing(j: int, q: int) -> bool:
    return 3**q >= 1 << (j - 1) and 3**q < 1 << j


def analytic_base_row(j: int) -> dict[str, str | int | bool]:
    L = (j - 1) // 3
    H = 2 * ((1 << L) + 1) - 3 * (j - 1)
    base_ok = H > 0 and H**10 > 6**10 * j**143
    growth_ok = (j + 3) ** 143 < 2**10 * j**143
    return {
        "j": j,
        "factor_length": L,
        "lower_numerator": str(H),
        "lower_denominator": 6,
        "rhin_power_comparison": base_ok,
        "three_step_power_growth": growth_ok,
    }


def build() -> dict:
    rows: list[dict[str, str | int]] = []
    for j in range(2, 373):
        bits, q = mechanical_word(j)
        if not valid_first_crossing(j, q):
            continue
        r, s, A, q2 = canonical_pair(bits)
        if q != q2:
            raise AssertionError("weight mismatch")
        delta = r - s
        if j == 2:
            if bits != [1, 0] or (r, s, delta) != (1, 1, 0):
                raise AssertionError("trivial boundary mismatch")
        elif delta <= 0:
            raise AssertionError(f"nontrivial mechanical failure at j={j}")
        rows.append(
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

    bases = [analytic_base_row(j) for j in (373, 374, 375)]
    if not all(row["rhin_power_comparison"] and row["three_step_power_growth"] for row in bases):
        raise AssertionError("analytic induction base failed")

    semantic_lines = [
        f"{row['j']}:{row['q']}:{row['canonical_root']}:{row['canonical_endpoint']}:{row['descent_defect']}"
        for row in rows
    ]
    semantic_lines.extend(
        f"B:{row['j']}:{row['factor_length']}:{row['lower_numerator']}:"
        f"{int(bool(row['rhin_power_comparison']))}:{int(bool(row['three_step_power_growth']))}"
        for row in bases
    )
    digest = hashlib.sha256(("\n".join(semantic_lines) + "\n").encode()).hexdigest()

    positive = [row for row in rows if int(row["descent_defect"]) > 0]
    minimum = min(positive, key=lambda row: (int(row["descent_defect"]), int(row["j"])))
    sample_js = {2, 4, 5, 370, 371}
    samples = [row for row in rows if int(row["j"]) in sample_js]

    return {
        "experiment_id": "X-6801",
        "status": "EXACT FINITE CERTIFICATE / SOURCE-QUALIFIED ALL-LENGTH INTERFACE",
        "finite_max_j": 372,
        "valid_mechanical_rows": len(rows),
        "first_valid_j": int(rows[0]["j"]),
        "last_valid_j": int(rows[-1]["j"]),
        "trivial_equality": {"j": 2, "word": "10", "root": 1, "endpoint": 1},
        "minimum_positive_defect": {
            "j": int(minimum["j"]),
            "defect": minimum["descent_defect"],
        },
        "nontrivial_failures": 0,
        "analytic_induction_start": 373,
        "analytic_base_rows": bases,
        "semantic_sha256": digest,
        "sample_rows": samples,
        "interpretation": {
            "proved_exactly": (
                "every valid upper-mechanical first-crossing canonical pair with j<373 "
                "descends, except the trivial word 10; and the integer induction bases "
                "for j>=373 pass"
            ),
            "source_dependency": (
                "the all-length theorem additionally imports the quoted Rhin bound "
                "|j log 2-q log 3| >= j^(-13.3)"
            ),
            "not_proved": (
                "descent for arbitrary nonmechanical first crossings, CST, or Collatz"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    result = build()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")

    if args.check_results:
        expected = args.check_results.read_text(encoding="utf-8")
        if text != expected:
            raise SystemExit("canonical result mismatch")


if __name__ == "__main__":
    main()
