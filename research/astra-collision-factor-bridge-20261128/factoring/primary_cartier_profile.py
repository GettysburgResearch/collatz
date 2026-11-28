#!/usr/bin/env python3
"""Exact primary Cartier extraction for a fixed rational profile series.

This independently implements the single-denominator B^(2e) formula from the
pinned factoring source cited in AGGREGATE_PROFILE_TRANSFER.md. Both coefficient
addresses are prescribed; no row-span/content substitute is used. All arithmetic
is integer arithmetic. The finite tests compare to actual shortcut trajectories,
literal large-index binomial sums, and independent prime-power factorials.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path

Poly = dict[tuple[int, int], int]


def require(condition: bool, detail: object) -> None:
    """Proof-consumer checks remain active under python -O."""
    if not condition:
        raise RuntimeError("Primary Cartier validation failed: " + repr(detail))


def clean(poly: Poly, modulus: int | None = None) -> Poly:
    if modulus is None:
        return {key: value for key, value in poly.items() if value}
    return {key: value % modulus for key, value in poly.items() if value % modulus}


def add(left: Poly, right: Poly, modulus: int | None = None) -> Poly:
    result = left.copy()
    for key, value in right.items():
        result[key] = result.get(key, 0) + value
    return clean(result, modulus)


def scale(poly: Poly, scalar: int, modulus: int | None = None) -> Poly:
    return clean({key: scalar * value for key, value in poly.items()}, modulus)


def mul(left: Poly, right: Poly, modulus: int | None = None) -> Poly:
    result: Poly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            key = i + k, j + ell
            result[key] = result.get(key, 0) + a * b
    return clean(result, modulus)


def power(poly: Poly, exponent: int, modulus: int | None = None) -> Poly:
    result = {(0, 0): 1}
    while exponent:
        if exponent & 1:
            result = mul(result, poly, modulus)
        exponent >>= 1
        if exponent:
            poly = mul(poly, poly, modulus)
    return result


def section(poly: Poly, digit_t: int, digit_u: int, prime: int) -> Poly:
    return {((i - digit_t) // prime, (j - digit_u) // prime): value
            for (i, j), value in poly.items()
            if i % prime == digit_t and j % prime == digit_u}


class PrimaryCartier:
    """Coefficient [t^h u^a] A/B modulo p^e, with B(0,0)=1."""

    def __init__(self, numerator: Poly, denominator: Poly,
                 prime: int = 3, precision: int = 1):
        if prime < 2 or precision < 1 or denominator.get((0, 0), 0) != 1:
            raise ValueError("Need p >= 2, e >= 1, B(0,0) = 1")
        # Callers supply a prime. The shipped tests only use p=3.
        self.prime = prime
        self.precision = precision
        self.modulus = prime ** precision
        K = 2 * precision
        s = (K + prime - 1) // prime
        require(s <= precision, "primary denominator exponent")
        inflated = {(prime * i, prime * j): value
                    for (i, j), value in denominator.items()}
        defect_numerator = add(power(denominator, prime), scale(inflated, -1))
        require(all(value % prime == 0 for value in defect_numerator.values()),
                "Frobenius defect must be exactly divisible by p")
        defect = clean({key: value // prime
                        for key, value in defect_numerator.items()}, self.modulus)
        self.initial = mul(numerator, power(denominator, K - 1, self.modulus),
                           self.modulus)
        self.left: list[Poly] = []
        self.right: list[Poly] = []
        common = power(denominator, prime * s - K, self.modulus)
        for i in range(precision):
            self.left.append(mul(common, power(defect, i, self.modulus),
                                 self.modulus))
            scalar = (-prime) ** i * math.comb(s + i - 1, i)
            self.right.append(scale(
                power(denominator, K - s - i, self.modulus),
                scalar, self.modulus))
        keys = set(numerator) | set(denominator)
        self.bounds = (
            K * max((i for i, _ in keys), default=0),
            K * max((j for _, j in keys), default=0),
        )
        self.calls = 0
        self.transitions = 0
        self.largest_support = len(self.initial)

    def coefficient(self, h: int, a: int) -> int:
        if h < 0 or a < 0:
            return 0
        self.calls += 1
        row = self.initial
        while h or a:
            digit_t, digit_u = h % self.prime, a % self.prime
            next_row: Poly = {}
            for left, right in zip(self.left, self.right):
                selected = section(mul(row, left, self.modulus),
                                   digit_t, digit_u, self.prime)
                next_row = add(next_row, mul(right, selected, self.modulus),
                               self.modulus)
            row = next_row
            require(all(i <= self.bounds[0] and j <= self.bounds[1]
                        for i, j in row), "stable numerator degree box")
            self.largest_support = max(self.largest_support, len(row))
            self.transitions += 1
            h //= self.prime
            a //= self.prime
            if not row:
                return 0
        # The common denominator B^(2e) has constant term one.
        return row.get((0, 0), 0) % self.modulus


def profile_functions():
    one = {(0, 0): 1}
    t, u = {(1, 0): 1}, {(0, 1): 1}
    one_minus_t = add(one, scale(t, -1))
    one_plus_u = add(one, u)
    t2 = power(t, 2)
    count_denominator = mul(one_minus_t, add(one,
        scale(mul(t2, power(one_plus_u, 2)), -1)))
    count1 = mul(t, u)
    count2 = mul(mul(t2, u), one_plus_u)
    alpha = scale(one_plus_u, 2)
    beta = add(one, scale(u, 3))
    moment_denominator = mul(one_minus_t, mul(
        add(one, scale(mul(t2, power(alpha, 2)), -1)),
        add(one, scale(mul(t2, power(beta, 2)), -1))))
    moment1 = mul(mul(t, u), add(one, scale(mul(t2,
        add(one, add(scale(u, -3), scale(power(u, 2), -6)))), -1)))
    moment2 = mul(mul(t2, u), add(
        add(scale(one, 2), scale(u, 5)),
        scale(mul(t2, mul(alpha, beta)), -1)))
    root_count_denominator = mul(add(one, scale(t2, -1)),
        add(one, scale(mul(t, one_plus_u), -1)))
    root_moment_denominator = mul(add(one, t), mul(
        add(one, scale(mul(t, alpha), -1)),
        add(one, scale(mul(t, beta), -1))))
    return {
        "count1": (count1, count_denominator),
        "count2": (count2, count_denominator),
        "moment1": (moment1, moment_denominator),
        "moment2": (moment2, moment_denominator),
        "root_count1": (mul(t2, u), root_count_denominator),
        "root_count2": (mul(t, u), root_count_denominator),
        "root_moment1": (mul(t2, u), root_moment_denominator),
        "root_moment2": (mul(t, u), root_moment_denominator),
    }


def actual_profile(h: int):
    """Independent native replay of all binary source cylinders."""
    counts: dict[tuple[int, int], int] = {}
    moments: dict[tuple[int, int], int] = {}
    root_counts: dict[tuple[int, int], int] = {}
    root_moments: dict[tuple[int, int], int] = {}
    for source in range(1 << h):
        value, grade = source, 0
        for _ in range(h):
            if value & 1:
                grade += 1
                value = (3 * value + 1) // 2
            else:
                value //= 2
        carry = (1 << h) * value - 3 ** grade * source
        require(carry >= 0, ("negative actual carry", h, source, carry))
        key = grade, carry % 3
        counts[key] = counts.get(key, 0) + 1
        moments[key] = moments.get(key, 0) + carry
        root_key = grade, value % 3
        require(carry * pow(2, -h, 3) % 3 == value % 3,
                ("normalized actual endpoint residue", source, h, grade))
        root_counts[root_key] = root_counts.get(root_key, 0) + 1
        root_moments[root_key] = root_moments.get(root_key, 0) + carry
    return counts, moments, root_counts, root_moments


def binomial_mod_prime_power(n: int, k: int, p: int, e: int) -> int:
    """Independent factorial-unit recursion; numerical p^e is small in tests."""
    if not 0 <= k <= n:
        return 0
    modulus = p ** e
    prefix = [1]
    for i in range(1, modulus + 1):
        prefix.append(prefix[-1] * (i if i % p else 1) % modulus)

    def valuation(m: int) -> int:
        result = 0
        while m:
            m //= p
            result += m
        return result

    def unit_factorial(m: int) -> int:
        result = 1
        while m:
            result = (result * pow(prefix[-1], m // modulus, modulus)
                      * prefix[m % modulus]) % modulus
            m //= p
        return result

    v = valuation(n) - valuation(k) - valuation(n - k)
    if v >= e:
        return 0
    return (unit_factorial(n) * pow(unit_factorial(k), -1, modulus)
            * pow(unit_factorial(n - k), -1, modulus) * p ** v) % modulus


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    functions = profile_functions()
    machines = {(name, e): PrimaryCartier(A, B, precision=e)
                for name, (A, B) in functions.items()
                for e in ((1, 2, 3) if "count" in name else (1, 2))}
    tests = 0
    for h in range(9):
        counts, moments, root_counts, root_moments = actual_profile(h)
        require(sum(counts.values()) == 1 << h, ("cylinder census", h))
        for a in range(h + 1):
            require(sum(counts.get((a, r), 0) for r in range(3)) == math.comb(h, a),
                    ("odd-grade census", h, a))
            for residue in (1, 2):
                for kind, expected in (("count", counts), ("moment", moments),
                                       ("root_count", root_counts),
                                       ("root_moment", root_moments)):
                    # All small native cases at p; selected cases at p^2.
                    precisions = (1, 2) if (h + a) % 3 == 0 else (1,)
                    for e in precisions:
                        got = machines[(kind + str(residue), e)].coefficient(h, a)
                        require(got == expected.get((a, residue), 0) % (3 ** e),
                                (kind, h, a, residue, e, got, expected))
                        tests += 1
    for h, a in ((20, 9), (63, 31), (128, 59), (511, 255)):
        for prefix in ("count", "root_count"):
            for residue in (1, 2):
                parity = 0 if residue == 1 else 1
                if prefix == "root_count":
                    parity = (h if residue == 1 else h - 1) % 2
                exact = sum(math.comb(j, a - 1) for j in range(a - 1, h)
                            if j % 2 == parity)
                for e in (1, 2, 3):
                    got = machines[(prefix + str(residue), e)].coefficient(h, a)
                    require(got == exact % (3 ** e),
                            ("literal binomial profile", prefix, h, a, residue,
                             e, got, exact))
                    tests += 1
    remote = (1 << 127) + 17
    remote_checks = []
    for e in (1, 2):
        for a in (1, remote // 2, remote - 1):
            residues = [machines[("count" + str(r), e)].coefficient(remote, a)
                        for r in (1, 2)]
            expected_total = binomial_mod_prime_power(remote, a, 3, e)
            require(sum(residues) % (3 ** e) == expected_total,
                    ("remote factorial total", e, a, residues, expected_total))
            if a == 1:
                require(residues == [((remote + 1) // 2) % (3 ** e),
                                     (remote // 2) % (3 ** e)],
                        ("remote grade-one census", e, residues))
            remote_checks.append({"clock_bits": remote.bit_length(), "grade": str(a),
                                  "precision": e, "residues": residues,
                                  "total_modulus": expected_total})
            tests += 1
            root_residues = [machines[("root_count" + str(r), e)].coefficient(remote, a)
                             for r in (1, 2)]
            require(sum(root_residues) % (3 ** e) == expected_total,
                    ("remote normalized factorial total", e, a,
                     root_residues, expected_total))
            if a == 1:
                require(root_residues == [(remote // 2) % (3 ** e),
                                         ((remote + 1) // 2) % (3 ** e)],
                        ("remote normalized grade-one census", e, root_residues))
            remote_checks.append({"clock_bits": remote.bit_length(), "grade": str(a),
                                  "precision": e, "normalized_residue": True,
                                  "residues": root_residues,
                                  "total_modulus": expected_total})
            tests += 1
        if e == 1:
            for residue, count, factor in (
                (1, (remote + 1) // 2, 1), (2, remote // 2, 2)):
                lifted_modulus = 3 ** (e + 1)
                geometric = (pow(4, count, lifted_modulus) - 1) // 3
                expected = factor * geometric % (3 ** e)
                got = machines[("moment" + str(residue), e)].coefficient(remote, 1)
                require(got == expected,
                        ("remote geometric moment", residue, e, got, expected))
                tests += 1
                root_residue = residue * pow(2, -remote, 3) % 3
                root_got = machines[("root_moment" + str(root_residue), e)].coefficient(remote, 1)
                require(root_got == expected,
                        ("remote normalized geometric moment", root_residue,
                         e, root_got, expected))
                tests += 1
    report = {
        "schema": "collatz-primary-cartier-profile/v1",
        "utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Exact integer arithmetic. Ternary conductor k=1, all odd grades, counts and real carry first moments, for both A mod 3 and the joint normalized endpoint R=A/2^h mod 3. No growing-conductor or moving-window theorem.",
        "tests": tests,
        "remote_checks": remote_checks,
        "machines": {name + "_e" + str(e): {
            "calls": machine.calls, "transitions": machine.transitions,
            "largest_support": machine.largest_support,
            "numerator_box": machine.bounds,
        } for (name, e), machine in machines.items()},
        "success": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"success": True, "tests": tests,
                      "remote_clock_bits": remote.bit_length(),
                      "scope": report["scope"]}, indent=2))


if __name__ == "__main__":
    main()
