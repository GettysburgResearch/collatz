#!/usr/bin/env python3
"""Independent exact finite-cut and binary escape-model controls.

These are algebraic identities and model checks. The model is not Collatz,
and no analytic density input is verified by this program.
"""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def binary_map(n):
    level = n.bit_length() - 1
    power = 1 << level
    if n == power:
        return 2 * power
    half = power // 2
    return half + ((n - power) % half)


def binary_density(n):
    level = n.bit_length() - 1
    power = 1 << level
    return Fraction(2 * power - 1, 2 * power) if n == power else Fraction(1, power)


def cutoff_checks():
    comparisons = 0
    for cutoff in range(1, 151):
        label = {n: Fraction((n * n + 7 * n + 3) % 29, 29)
                 for n in range(1, 2 * cutoff + 1)}
        divergence = sum((label[v] ** 2 - sum(label[n] ** 2
                          for n in range(1, 2 * cutoff + 1) if shortcut(n) == v)
                          for v in range(1, cutoff + 1)), Fraction(0))
        annulus = sum((label[n] ** 2 for n in range(1, cutoff + 1)
                       if n % 2 and 3 * n > 2 * cutoff - 1), Fraction(0))
        annulus -= sum((label[n] ** 2 for n in range(cutoff + 1, 2 * cutoff + 1)
                        if not n % 2), Fraction(0))
        require(annulus == divergence, "physical annular sign or endpoint error")
        comparisons += 1
    return comparisons


def binary_checks():
    source_limit, target_limit = 4096, 8192
    visits = [0] * (target_limit + 1)
    for start in range(1, source_limit + 1):
        n, seen = start, set()
        while n <= target_limit:
            require(n not in seen, "binary model failed to escape")
            seen.add(n)
            visits[n] += 1
            n = binary_map(n)
    worst = max(abs(Fraction(visits[n], source_limit) - binary_density(n))
                for n in range(1, target_limit + 1))
    require(worst <= Fraction(2, source_limit), "uniform empirical bound failed")
    currents = []
    for k in range(2, 12):
        cutoff = (1 << k) - 1
        current = sum((binary_density(n) ** 2 *
                       (int(n <= cutoff) - int(binary_map(n) <= cutoff))
                       for n in range(1, 3 * cutoff + 1)), Fraction(0))
        require(0 < current < 1 and 1 - current <= Fraction(4, cutoff),
                "binary escape current estimate failed")
        currents.append({"cutoff": cutoff, "quadratic_current": str(current)})
    selected = [n for n in range(1, target_limit + 1) if binary_density(n) > Fraction(1, 2)]
    require(selected == [1 << j for j in range(1, 14)], "threshold rays mismatch")
    return {"sources": source_limit, "targets": target_limit,
            "maximum_empirical_error": str(worst), "currents": currents,
            "selected_ray_count": 1}


if __name__ == "__main__":
    print(json.dumps({"physical_cutoffs": cutoff_checks(), "binary_model": binary_checks(),
                      "scope": "finite identities and independent non-Collatz model"}, indent=2))
