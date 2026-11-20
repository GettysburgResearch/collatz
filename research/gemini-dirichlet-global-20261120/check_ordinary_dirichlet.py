#!/usr/bin/env python3
"""Exact finite replay for ORDINARY_DIRICHLET_COERCIVITY.md.

No solver or floating point arithmetic is used.  This checks the finite
ordinary path data and rational models of the scalar kernels.  The infinite
coarea/Tonelli/Fourier arguments are mathematical proofs in the companion note,
not claims of this executable.  No Collatz resolution is claimed.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


PIN = "7d04c4dd756cfe495eb3eee78eba35a99085cd2a"
SOURCE_HASHES = {
    "research/upper-bit-mergers/TRIPLING_VARIATION.md":
        "1a3aef543f1ec76db6b585041108eaa105f1d4ceb0c04fe421f1b15ed47d21bb",
    "research/upper-bit-mergers/THREE_RAY_VARIATION.md":
        "f7f2d0b5803e9ec8c302402e5b7a53fbc06c2ec1cdf92f8d4e816a1c3de5c0d0",
    "research/upper-bit-mergers/THREE_RAY_DENSITY.md":
        "567ecc84a34d41d01ca9bf63a4b4074a92b350c1cbbdc77060927fb1ed72f3b5",
}


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_data(data) -> str:
    return digest_bytes(json.dumps(data, sort_keys=True, separators=(",", ":")).encode())


def affine_step(pair):
    """One shortcut step on a*t+b with parity fixed for EVERY integer t."""
    a, b = pair
    require(a % 2 == 0, 'verification condition failed at source line 41')
    odd = b % 2
    if odd:
        return (3 * a // 2, (3 * b + 1) // 2), 1
    return (a // 2, b // 2), 0


def affine_iterate(pair, steps):
    odd = 0
    parity = []
    for _ in range(steps):
        pair, bit = affine_step(pair)
        parity.append(bit)
        odd += bit
    return pair, odd, parity


def cylinders():
    data = []
    for modulus, left, right, clock, endpoint, odd_count in [
        (16, 2, 3, 4, 2, 2),
        (8, 4, 5, 3, 2, 1),
        (128, 49, 50, 7, 11, 3),
        (32, 5, 6, 5, 2, 2),
    ]:
        a = affine_iterate((modulus, left), clock)
        b = affine_iterate((modulus, right), clock)
        require(a[0] == b[0], 'verification condition failed at source line 68')
        require(a[0][1] == endpoint, 'verification condition failed at source line 69')
        require(a[1] == b[1] == odd_count, 'verification condition failed at source line 70')
        data.append({
            "modulus": modulus, "left_base": left, "right_base": right,
            "clock": clock, "common_affine_endpoint": a[0],
            "odd_inputs_per_arm": odd_count, "left_word": a[2], "right_word": b[2],
        })
    return data


def residue_coverage():
    minus = {}
    for w in range(1, 16, 2):
        js = [j for j in range(2, 6) if (pow(3, j, 16) * w) % 16 in (3, 5)]
        require(js, 'verification condition failed at source line 83')
        minus[w] = min(js)
    plus = {}
    for w in range(1, 128, 2):
        js = [j for j in range(2, 34)
              if (pow(3, j, 128) * w) % 128 == 49
              or (pow(3, j, 32) * w) % 32 == 5]
        require(js, 'verification condition failed at source line 90')
        plus[w] = min(js)
    return {"minus_mod16": minus, "plus_mod128": plus}


def ordinary_identities():
    """All affine inputs are expressions in arbitrary positive integer u."""
    identities = [
        ((2, -1), 1, (3, -1)),
        ((4, -1), 2, (9, -1)),
        ((8, -1), 3, (27, -1)),
        ((24, -3), 3, (9, -1)),
        ((4, 1), 2, (3, 1)),
        ((48, 3), 4, (27, 2)),
        ((18, 1), 1, (27, 2)),
        ((20, 1), 2, (15, 1)),
    ]
    checked = []
    for start, clock, end in identities:
        result, odd, parity = affine_iterate(start, clock)
        require(result == end, 'verification condition failed at source line 110')
        checked.append({"input": start, "clock": clock, "output": end,
                        "odd_inputs": odd, "word": parity})
    return checked


def smooth_exponents(n):
    a = b = 0
    while n % 2 == 0:
        a += 1
        n //= 2
    while n % 3 == 0:
        b += 1
        n //= 3
    require(n == 1, 'verification condition failed at source line 124')
    return a, b


def chain():
    offsets = [0, 18, 24, 32, 33, 36, 48, 64, 63, 72, 96, 99,
               108, 144, 192, 198, 216, 288]
    plus = {(0, 18), (32, 33), (96, 99), (192, 198)}
    odd = {(48, 64), (144, 192)}
    data = []
    for p, q in zip(offsets, offsets[1:]):
        scale = abs(p - q)
        exps = smooth_exponents(scale)
        lo, hi = min(p, q), max(p, q)
        require(288 % scale == lo % scale == hi % scale == 0, 'verification condition failed at source line 138')
        slope, low, high = 288 // scale, lo // scale, hi // scale
        require(high == low + 1, 'verification condition failed at source line 140')
        if (p, q) in plus:
            require(slope % 16 == low % 16 == 0, 'verification condition failed at source line 142')
            h = (slope // 16, low // 16)
            kind = "16h,16h+1"
        elif (p, q) in odd:
            require(slope % 3 == low % 3 == 0, 'verification condition failed at source line 146')
            h = (slope // 3, low // 3)
            require(h[0] % 2 == 0 and h[1] % 2 == 1, 'verification condition failed at source line 148')
            kind = "3h,3h+1 with h odd"
        else:
            require(slope % 4 == high % 4 == 0, 'verification condition failed at source line 151')
            h = (slope // 4, high // 4)
            kind = "4h-1,4h"
        require(h[0] >= 1 and h[0] + h[1] >= 1, 'verification condition failed at source line 154')
        data.append({"offsets": (p, q), "smooth_divisor": scale,
                     "divisor_exponents_2_3": exps, "h_affine": h, "kind": kind})
    require(len(data) == 17, 'verification condition failed at source line 157')
    require(smooth_exponents(288) == (5, 2), 'verification condition failed at source line 158')
    return data


def rational_kernels():
    """z=2^-s ranges over (1/2,1); all these checks are rational identities.

    For a defect entering the cumulative count at shell r, the exact infinite
    double kernel is [(2z)z^r/(1-z)-2^(1-r)]/(2z-1).  Its stated geometric
    upper bound exceeds it by 2^(1-r)/(2z-1).  This independently distinguishes
    odd-defect and full-defect norm constants.
    """
    cases = 0
    for numerator in range(65, 128):
        z = F(numerator, 128)
        q = 2 * z
        for r in range(33):
            row = sum(q ** k for k in range(r + 1))
            row_bound = q ** r / (1 - 1 / q)
            require(row == (q ** (r + 1) - 1) / (q - 1), 'verification condition failed at source line 177')
            require(0 < row < row_bound, 'verification condition failed at source line 178')
            exact_double = (q * z ** r / (1 - z) - F(2) ** (1 - r)) / (q - 1)
            double_bound = z ** r / ((1 - 1 / q) * (1 - z))
            require(double_bound - exact_double == F(2) ** (1 - r) / (q - 1), 'verification condition failed at source line 181')
            require(exact_double > 0, 'verification condition failed at source line 182')
            # A finite partial sum plus its exact geometric tail is the same value.
            cutoff = r + 7
            partial = sum(F(1, 2) ** j * sum(q ** k for k in range(j + 1))
                          for j in range(r, cutoff + 1))
            tail = (q * z ** (cutoff + 1) / (1 - z)
                    - F(2) ** (-cutoff)) / (q - 1)
            require(partial + tail == exact_double, 'verification condition failed at source line 189')
            # Convert odd defect norm to full defect norm: denominator cancels.
            require(double_bound * (1 - z) == z ** r / (1 - 1 / q), 'verification condition failed at source line 191')
            cases += 1
    # Dropping the second denominator while retaining the ODD norm is false.
    z = F(3, 4)
    exact_double = (2 * z / (1 - z) - 2) / (2 * z - 1)
    wrong_odd_bound = 1 / (1 - 1 / (2 * z))
    require(exact_double == 8 and wrong_odd_bound == 3, 'verification condition failed at source line 197')
    return {"rational_cases": cases,
            "negative_control_odd_norm_missing_denominator": {
                "z": str(z), "exact_kernel": str(exact_double),
                "incorrect_one_denominator_bound": str(wrong_odd_bound),
                "rejected": exact_double > wrong_odd_bound},
            "full_norm_cancellation_checked": True}


def source_hashes(root):
    data = {}
    for rel, expected in SOURCE_HASHES.items():
        actual = digest_bytes((root / rel).read_bytes())
        require(actual == expected, (rel, actual, expected))
        data[rel] = actual
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True,
                        help="PR146 worktree pinned at the documented commit")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    finite = {"cylinders": cylinders(), "residue_coverage": residue_coverage(),
              "ordinary_affine_identities": ordinary_identities(), "chain": chain()}
    receipt = {
        "status": "PASS",
        "scope": "Exact finite path data and rational scalar-kernel replay only; "
                 "infinite proofs are in ORDINARY_DIRICHLET_COERCIVITY.md; "
                 "no all-level LP or Collatz proof claimed.",
        "source_revision": PIN,
        "source_hashes": source_hashes(args.source_root),
        "checker_sha256": digest_bytes(Path(__file__).read_bytes()),
        "note_sha256": digest_bytes(Path(__file__).with_name(
            "ORDINARY_DIRICHLET_COERCIVITY.md").read_bytes()),
        "finite_reconstruction_sha256": digest_data(finite),
        "finite_reconstruction": finite,
        "scalar_kernel_checks": rational_kernels(),
        "five_ray_disjointness": "For odd x, 3x is odd and 4x has v2=2; "
                                  "each parameter map is injective.",
    }
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(json.dumps({k: v for k, v in receipt.items()
                      if k != "finite_reconstruction"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
