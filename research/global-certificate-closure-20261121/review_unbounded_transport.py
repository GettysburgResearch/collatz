#!/usr/bin/env python3
"""Independent exact checks of UF1--UF5; imports no author checker.

Uses ordinary affine parity words and dyadic rational power enclosures.
Universal proofs remain in the accompanying notes. No Collatz completion
or absolute remainder estimate is inferred from these checks.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json


def require(value, message):
    if not value:
        raise ValueError(message)


def inverse_affine(word):
    slope, intercept = Q(1), Q(0)
    for exponent in reversed(word):
        slope = (2**exponent * slope) / 3
        intercept = (2**exponent * intercept - 1) / 3
    return slope, intercept


def seed_proof():
    # Treat v=2^(b-3) q and z=(4/3)^(r-3) as free rational variables.
    # Matching the coefficients of z*v, z, and 1 proves the identity
    # for every r,b once their ordinary inverse guards are imposed.
    output = []
    for a, final_prefix in [(2, (3, 3, 1)), (4, (3, 1, 5))]:
        s_slope, s_intercept = inverse_affine((1, a))
        s_slope, s_intercept = s_slope * Q(8, 3), s_intercept - s_slope / 3
        # Above composition is I_1 I_a ((8*v-1)/3).
        t_slope, t_intercept = inverse_affine(final_prefix)
        t_slope, t_intercept = t_slope * Q(5, 3), t_intercept - t_slope / 3
        source = (Q(640, 81) * s_slope,
                  Q(640, 81) * (s_intercept - 1), Q(5, 3))
        target = (Q(64, 27) * t_slope,
                  Q(64, 27) * (t_intercept - 1), Q(5, 3))
        require(source == target, "unbounded formal seed identity")
        output.append({"a": a, "bilinear_coefficients": [str(x) for x in source]})
    return output


def ordinary_bits(word):
    return tuple(bit for exponent in word for bit in (1,) + (0,) * (exponent - 1))


def affine_replay(slope, intercept, bits):
    for bit in bits:
        require(slope.denominator == intercept.denominator == 1, "integrality")
        require(slope.numerator % 2 == 0, "free lift changes a forced parity")
        require(intercept.numerator % 2 == bit, "wrong ordinary parity")
        if bit:
            slope, intercept = 3 * slope / 2, (3 * intercept + 1) / 2
        else:
            slope, intercept = slope / 2, intercept / 2
    require(slope.denominator == intercept.denominator == 1, "endpoint integrality")
    return slope, intercept


def cylinder_proof_controls():
    count = 0
    for run in range(3, 25):
        for a, middle in [(2, (3, 3, 1)), (4, (3, 1, 5))]:
            source = (1,) + (2,) * run + (1, a, 4)
            target = (1, 1, 4) + (2,) * (run - 3) + middle + (1,)
            clock = sum(source)
            modulus = 2**clock
            correction = (84 + 2**(a + 2)) * 4**run - 27 * 3**run
            residue = (-correction * pow(3**(run + 4), -1, modulus)) % modulus
            require(residue > 0, "nonpositive cylinder representative")
            left = affine_replay(Q(modulus), Q(residue), ordinary_bits(source))
            right = affine_replay(Q(5 * modulus), Q(5 * residue), ordinary_bits(target))
            require(right == (5 * left[0], 5 * left[1]), "whole-cell endpoint identity")
            require(7 * left[0] <= modulus and 7 * left[1] <= residue,
                    "whole-cell endpoint contraction")
            require((3 * residue - 1) % 2**(2 * run + 2) == 0 and
                    (3 * residue - 1) % 2**(2 * run + 3) != 0,
                    "binary separating invariant")
            count += 1
    require(Q(85, 1536) + Q(5, 24576) == Q(455, 8192), "density sum")
    require(7 * Q(2187, 16384) < 1 and 1075 * 43 >= 44800,
            "uniform contraction coefficient")
    return count


def logarithms(modulus):
    result = {}
    value = 1
    while value not in result:
        result[value] = len(result)
        value = 2 * value % modulus
    require(value == 1 and len(result) == 2 * modulus // 3,
            "incomplete ternary unit group")
    require(set(result) == {v for v in range(modulus) if v % 3}, "unit coverage")
    return result


LOGS = {m: logarithms(m) for m in (9, 27, 81, 729)}


def first_exponent(q, rhs, modulus, offset, floor):
    table = LOGS[modulus]
    exponent = (table[(rhs * pow(q, -1, modulus)) % modulus] - offset) % len(table)
    if exponent < floor:
        exponent += ((floor - exponent + len(table) - 1) // len(table)) * len(table)
    require(exponent >= floor and pow(2, exponent + offset, modulus) * q % modulus == rhs % modulus,
            "discrete logarithm guard")
    return exponent


def least_odd_unit(c, modulus):
    value = c if c % 2 else c + modulus
    if value < 5:
        value += 2 * modulus
    require(value >= 5 and value % 2 and value % 3 and value % modulus == c,
            "endpoint minimum")
    return value


DYADIC = 2**42
POWER_CACHE = {}


def power_upper(value, exponent):
    if exponent == 1:
        return value
    key = (value.numerator, value.denominator)
    if key in POWER_CACHE:
        return POWER_CACHE[key]
    # Independent dyadic enclosure, rather than the author's decimal grid.
    num = value.numerator**21 * DYADIC**25
    den = value.denominator**21
    low, high = 0, DYADIC
    while high**25 * den < num:
        high *= 2
    while high - low > 1:
        mid = (high + low) // 2
        if mid**25 * den >= num:
            high = mid
        else:
            low = mid
    require(high**25 * den >= num, "upper power certificate")
    require((high - 1)**25 * den < num, "minimal upper enclosure")
    result = Q(high, DYADIC)
    POWER_CACHE[key] = result
    return result


def old_bound(c, exponent):
    q = least_odd_unit(c, 81)
    total = Q(0)
    for run in (1, 2):
        m = 3**(run + 1)
        b = first_exponent(c, 4, m, 0, 4)
        constant = 4**(run + 1) - m
        ratio = Q(m, 1) / (2**(2 * run + b) - Q(constant, q))
        total += power_upper(ratio, exponent) / (1 - power_upper(Q(1, 2**(2 * 3**run)), exponent))
    b = first_exponent(c, 4, 81, 0, 4)
    tail = Q(3, 1) / (2**b - Q(4, q))
    z = power_upper(Q(3, 4), exponent)
    total += power_upper(tail, exponent) * z**3 / ((1 - z) * (1 - power_upper(Q(1, 2**54), exponent)))
    for a, constant, floor in [(1, 65, 6), (2, 73, 4), (4, 121, 4)]:
        b = first_exponent(c, constant, 81, a + 2, floor)
        ratio = Q(81, 1) / (2**(a + 2 + b) - Q(constant, q))
        total += power_upper(ratio, exponent) / (1 - power_upper(Q(1, 2**54), exponent))
    return total


def renewal_certificate():
    maxima = {}
    old_cache = {}
    for exponent, bound in [(1, Q(5, 8)), (Q(21, 25), Q(91, 100))]:
        best = (Q(-1), None)
        count = 0
        for c in range(1, 729):
            if c % 3 == 0:
                continue
            key = c % 81, exponent
            if key not in old_cache:
                old_cache[key] = old_bound(*key)
            total = old_cache[key]
            q = least_odd_unit(c, 729)
            for a, constant in [(2, 100), (4, 148)]:
                b = first_exponent(c, constant, 729, a + 2, 4)
                ratio = Q(2187, 64) / (2**(b + a + 2) - Q(constant, q))
                require(ratio > 0, "positive new inverse fiber")
                total += power_upper(ratio, exponent) / (1 - power_upper(Q(1, 2**486), exponent))
            require(total < bound, "renewal coefficient threshold")
            if total > best[0]:
                best = total, c
            count += 1
        require(count == 486, "missing endpoint residue")
        maxima[str(exponent)] = {"residue": best[1], "upper_fraction": str(best[0]),
                                 "threshold": str(bound), "rows": count}
    return maxima


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "status": "PASS: independent UF1-UF5 checks, no global closure",
        "seed_polynomial_identities": seed_proof(),
        "unrestricted_affine_cylinder_controls": cylinder_proof_controls(),
        "coefficient_maxima": renewal_certificate(),
        "power_enclosure_denominator": DYADIC,
        "author_checker_imported": False,
        "full_collatz_proved": False,
    }
    proof = Path(__file__).with_name('UNBOUNDED_FIRST_ONE_TRANSPORT.md')
    report['proof_sha256'] = hashlib.sha256(proof.read_bytes()).hexdigest()
    payload = json.dumps(report, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(payload)
    print(json.dumps({"status": report['status'], "endpoint_residues": 486,
                      "affine_cylinders": report['unrestricted_affine_cylinder_controls'],
                      "report_sha256": hashlib.sha256(payload.encode()).hexdigest()}, sort_keys=True))


if __name__ == '__main__':
    main()
