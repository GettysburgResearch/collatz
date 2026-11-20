#!/usr/bin/env python3
"""Small independent literal and exact-power replay for a frozen V1--V4 note."""

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def need(value, message):
    if not value:
        raise RuntimeError(message)


def accelerated(n):
    need(n > 0 and n % 2 == 1, "positive odd ordinary input required")
    m = 3 * n + 1
    a = 0
    while m % 2 == 0:
        a += 1
        m //= 2
    return m, a


def word(n, count):
    exponents = []
    values = [n]
    for _ in range(count):
        n, a = accelerated(n)
        values.append(n)
        exponents.append(a)
    return n, exponents, values


def main():
    for j in range(128):
        x = 271 + 512 * j
        q, source, sv = word(x, 4)
        five_q, target, tv = word(5 * x, 4)
        need(source[:3] == [1, 1, 1] and source[3] >= 6, "source B cylinder failed")
        need(target == [1, 2, 5, source[3] - 5], "paired target word failed")
        need(five_q == 5 * q and 6 * q <= x, "paired endpoint/height failed")
        need(min(sv[:-1] + tv) > 1, "unintended first hit in B block")

    for k in range(9):
        x = (2 ** (54 * k + 31) - 65) // 81
        need(81 * x == 2 ** (54 * k + 31) - 65, "closed source integrality failed")
        q, source, sv = word(x, 4)
        end, target, tv = word(5 * x, 5)
        need((q, source) == (1, [1, 1, 1, 54 * k + 28]), "closed source failed")
        need((end, target) == (1, [1, 2, 5, 54 * k + 23, 4]), "closed target failed")
        need(min(sv[:-1] + tv[:-1]) > 1, "closed certificate early first hit")
        need(x % 3 == 2 * k % 3, "closed family ternary guard failed")

    for k in range(13):
        z = (2 ** (6 * k + 5) - 5) // 9
        need(9 * z == 2 ** (6 * k + 5) - 5, "residual source integrality failed")
        q, source, _ = word(z, 2)
        need((q, source) == (1, [1, 6 * k + 4]), "residual source word failed")
        n, odd_count = 5 * z, 0
        for _ in range(6 * k + 8):
            need(n > 1, "residual forced path hit one early")
            if n % 2:
                n = (3 * n + 1) // 2
                odd_count += 1
            else:
                n //= 2
        need(8 * n == 5 * (3 ** (4 * k + 2) - 1), "residual endpoint identity failed")
        need(n >= 5 and n % 2 == 1 and odd_count == 4 * k + 4,
             "residual endpoint/rank failed")
        need(z % 3 == 2 * k % 3, "residual ternary guard failed")

    comparisons = [
        (Q(3, 4), Q(393, 500)), (Q(3, 4), Q(4, 5)),
        (Q(1, 64), Q(1, 32)), (Q(1, 7), Q(1, 5)),
        (Q(5, 52), Q(1, 7)), (Q(81, 499), Q(1, 4)),
        (Q(61, 324), Q(1, 4)), (Q(81, 32755), Q(1, 129)),
        (Q(1, 2 ** 54), Q(1, 129)),
    ]
    for a, b in comparisons:
        need(a ** 21 < b ** 25, "fractional-power comparison failed")
    case_a = Q(32, 155) + Q(512, 1085) + Q(8, 31)
    case_b = Q(3144, 3317) + Q(1, 128)
    need(case_a == Q(1016, 1085) < case_b == Q(405749, 424576) < 1,
         "joint energy coefficients failed")
    need(1 / (1 - case_b) == Q(424576, 18827), "finite-energy multiplier failed")
    report = {"status": "PASS", "evidence": "independent bounded exact arithmetic",
              "paired_B_sources": 128, "closed_family_certificates": 9,
              "residual_family_forced_paths": 13, "exact_power_comparisons": len(comparisons),
              "case_a": str(case_a), "case_b": str(case_b),
              "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "Finite checks support the independently reconstructed V1--V4 proof; no Collatz closure."}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
