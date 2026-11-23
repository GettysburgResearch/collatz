#!/usr/bin/env python3
"""Two exact controls for the written all-finite-prime construction.

This is not a cycle search or a proof of the infinite selection theorem.
Checks use explicit exceptions and remain active under python -O.
"""
from __future__ import annotations

import hashlib
import json
import math


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def control(primes: tuple[int, ...], height: int) -> dict[str, object]:
    require(height > 0, "The target floor must be positive")
    require(all(is_prime(ell) for ell in primes), "The place list must consist of primes")
    L = math.lcm(2, *(ell - 1 for ell in primes if ell != 2))
    threshold = max(14 * L, 6 * height * (2 ** (2 * L) - 1))
    p = ((threshold // L) + 1) * L + 1
    while not is_prime(p):
        p += L
    require(p > threshold and p % L == 1, "Prime progression/floor threshold")
    three_p = 3 ** p
    b = (three_p.bit_length() + L - 1) // L
    A = L * (b + 1)
    two_A = 2 ** A
    D = two_A - three_p
    require(b >= 1 and 2 ** (L * (b - 1)) < three_p < 2 ** (L * b),
            "Least b has the advertised strict power brackets")
    require(p < A < 2 * p and 4 * A < 7 * p, "Positive-cycle cone")
    require(math.gcd(A, p) == 1, "Primitive balanced word")
    require(2 ** L * three_p < two_A < 2 ** (2 * L) * three_p,
            "The complete B interval")
    require(D > 1 and all(D % ell for ell in primes), "Denominator avoids every listed place")

    positions = [A * i // p for i in range(p)]
    gaps = [positions[i + 1] - positions[i] for i in range(p - 1)]
    gaps.append(A - positions[-1])
    C = sum(2 ** positions[i] * 3 ** (p - 1 - i) for i in range(p))
    require(math.gcd(C, D) == 1, "Full denominator at the initial rotation")
    initial = C
    minimum = C
    orbit_hash = hashlib.sha256()
    for gap in gaps:
        require(gap > 0 and C % 2 == 1, "An actual odd rational state")
        orbit_hash.update(str(C).encode("ascii") + b"\n")
        following, remainder = divmod(3 * C + D, 2 ** gap)
        require(remainder == 0 and following % 2 == 1, "Exact rational 2-adic gap")
        require(math.gcd(following, D) == 1, "Full reduced D at every odd rotation")
        C = following
        minimum = min(minimum, C)
    require(C == initial, "Full return with the original numerator")
    require(6 * minimum > p * three_p, "All-rotation sharp floor bound")
    require(minimum > height * D, "Every odd state exceeds the prescribed floor")
    # Intermediate shortcut states are powers of two times the next odd state.
    return {
        "primes": list(primes), "requested_floor": height,
        "L": L, "p": p, "A": A,
        "D_bits": D.bit_length(), "D_sha256": hashlib.sha256(str(D).encode()).hexdigest(),
        "minimum_state_integer_part": minimum // D,
        "all_rotations_checked": p, "shortcut_period": A,
        "orbit_numerator_sha256": orbit_hash.hexdigest(),
        "full_denominator_everywhere": True, "all_checks_passed": True,
    }


def main() -> None:
    print(json.dumps({
        "scope": "Two exact construction controls; the general theorem is written mathematics",
        "controls": [control((2, 3), 1), control((2, 3, 5), 2)],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
