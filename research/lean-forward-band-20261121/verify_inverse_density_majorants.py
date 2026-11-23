#!/usr/bin/env python3
"""Exact certificates for two failed global inverse-density potentials.

The infinite-series upper bound is analytic, stated explicitly in the output:
for even J=2K its remaining tail is at most 4*sqrt(q+1)/2**K.  We replace
sqrt(q+1) by an integer upper bound and check the resulting rational gap.
This does not validate a Collatz convergence or density theorem.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def v3(n: int) -> int:
    require(n > 0, "The ternary valuation requires a positive integer")
    exponent = 0
    while n % 3 == 0:
        exponent += 1
        n //= 3
    return exponent


def prefix(q: int, length: int) -> tuple[Fraction, list[int]]:
    valuations = [v3(2**j * q + 1) for j in range(length)]
    return sum((Fraction(3, 2)**v / 2**j
                for j, v in enumerate(valuations)), Fraction()), valuations


def exact_fraction(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source, target, exponent, length = 7, 11, 1, 12
    require(3*source+1 == 2**exponent*target, "Incorrect actual odd edge")
    require(all(n % 2 == 1 and n % 3 != 0 for n in (source, target)),
            "The actual edge must join odd ternary units")
    source_lower, source_values = prefix(source, length)
    target_prefix, target_values = prefix(target, length)
    sqrt_upper = isqrt(target+1)+1
    require(target+1 < sqrt_upper**2, "Incorrect square-root upper bound")
    tail_upper = Fraction(4*sqrt_upper, 2**(length//2))
    gap = Fraction(3, 2**exponent)*source_lower-target_prefix-tail_upper
    require(source_lower == Fraction(154611, 65536), "Source prefix mismatch")
    require(target_prefix == Fraction(2925, 1024), "Target prefix mismatch")
    require(tail_upper == Fraction(1, 4), "Infinite tail bound mismatch")
    require(gap == Fraction(56665, 131072) > 0, "Strict transfer gap failed")
    carry_family = []
    for k in range(1, 9):
        n = 2*3**(2*k)-1
        q = (3**(2*k+1)-1)//2
        require(3*n+1 == 4*q, "Incorrect family edge")
        require(all(x % 2 == 1 and x % 3 != 0 for x in (n, q)),
                "Family edge must join odd ternary units")
        require(v3(n+1) == 2*k and v3(q+1) == 0, "Family valuation mismatch")
        gap0 = Fraction(3, 4)*Fraction(3, 2)**v3(n+1)-1
        require(gap0 > 0, "Family transfer gap is not positive")
        carry_family.append({"k": k, "source": n, "target": q,
                             "transfer_gap": exact_fraction(gap0)})
    result = {
        "status": "exact_replay_passed",
        "scope": "Arithmetic witnesses refuting the two stated candidate potentials.",
        "not_established": ["A global sublinear density envelope", "Collatz convergence"],
        "infinite_series_candidate": {
            "formula": "sum(j>=0) 2^(-j)*(3/2)^v3(2^j*q+1)",
            "source": source, "target": target, "odd_exponent": exponent,
            "prefix_length": length,
            "source_valuations": source_values, "target_valuations": target_values,
            "source_lower": exact_fraction(source_lower),
            "target_prefix": exact_fraction(target_prefix),
            "analytic_tail_inequality": "tail from 2K <= 4*sqrt(q+1)/2^K",
            "target_sqrt_upper": sqrt_upper,
            "target_tail_upper": exact_fraction(tail_upper),
            "strict_transfer_gap_lower": exact_fraction(gap),
        },
        "carry_candidate_family": {
            "formula": "source=2*3^(2k)-1, target=(3^(2k+1)-1)/2, k>=1",
            "proof": "v3(source+1)=2k, v3(target+1)=0; weight=3/4",
            "finite_examples": carry_family,
        },
    }
    text = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
