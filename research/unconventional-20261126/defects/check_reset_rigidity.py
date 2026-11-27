#!/usr/bin/env python3
"""Verify finite reset identities, sharpness families and selected actual fates."""
from fractions import Fraction
from math import gcd
import json


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def valuation_two(value):
    require(value > 0, "valuation at a nonpositive input")
    return (value & -value).bit_length() - 1


def block_from(x):
    shifted = x + 1
    t = valuation_two(shifted)
    w = shifted >> t
    numerator = 3 ** t * w - 1
    b = valuation_two(numerator)
    return t, w, b, numerator >> b


def physical_block(x):
    current = x
    for odd_time in range(1, (x + 1).bit_length() + 1):
        numerator = 3 * current + 1
        a = valuation_two(numerator)
        current = numerator >> a
        if a > 1:
            return odd_time, a - 1, current
    raise ArithmeticError("could not reach first reset within the integer bit budget")


def remove_primes(numerator, denominator, primes):
    common = gcd(numerator, denominator)
    numerator //= common
    denominator //= common
    powers = []
    for p in primes:
        power = 0
        while numerator % p == 0:
            numerator //= p
            power += 1
        while denominator % p == 0:
            denominator //= p
            power -= 1
        powers.append(power)
    return powers, Fraction(numerator, denominator)


def exhaustive_blocks():
    visits = 0
    highest_gcd = (0, 0, 0)
    for x in range(1, 65536, 2):
        t, w, b, z = block_from(x)
        require(physical_block(x) == (t, b, z), "explicit block differs from true path")
        g = gcd(w, z + 1)
        require(g == gcd(w, (1 << b) - 1), "reset divisor identity")
        require(z * g < 3 ** t * w, "retained divisor and physical landing")
        for m, d in [(8, 5), (65, 41)]:
            require(3 ** d <= 2 ** m, "invalid rational approximation")
            require(z ** d * g ** m < (x + 1) ** m, "integer retention inequality")
        u = w // g
        v = ((1 << b) - 1) // g
        large = 3 ** t * u
        content = gcd(large, v)
        content_without_three = content
        while content_without_three % 3 == 0:
            content_without_three //= 3
        require(content_without_three == 1, "nonternary vector content")
        require((large + v) % (1 << b) == 0, "dyadic linear form")
        require(
            large * ((1 << b) - 1) == v * ((1 << b) * z + 1),
            "physical projective slope",
        )
        if z >= x + 1:
            visits += 1
            highest_gcd = max(highest_gcd, (g, x, z))
    return {
        "positive_odd_starts": 32768,
        "max_start": 65535,
        "complete_blocks_landing_at_least_start_plus_one": visits,
        "largest_retained_divisor_in_those_blocks_and_witness": highest_gcd,
    }


def prefix_budgets():
    tested = 0
    with_reset = 0
    test_primes = [2, 3, 5, 7, 11]
    for x in range(1, 2048, 2):
        current = x
        total = resets = bank = 0
        floor = None
        for k in range(1, 33):
            numerator = 3 * current + 1
            a = valuation_two(numerator)
            next_state = numerator >> a
            bank = 3 * bank + (1 << total) * ((1 << a) - 2)
            total += a
            if a >= 2:
                resets += 1
                floor = next_state + 1 if floor is None else min(floor, next_state + 1)
            scaled = (1 << total) * (next_state + 1)
            require(scaled == 3 ** k * (x + 1) + bank, "centered bank identity")
            require((bank > 0) == (resets > 0), "positive bank marker")
            if resets:
                require(floor * bank < resets * scaled, "unrestricted reset budget")
                with_reset += 1
            powers, rough = remove_primes(next_state + 1, x + 1, test_primes)
            recovered = rough
            for p, e in zip(test_primes, powers):
                recovered *= Fraction(p) ** e
            require(recovered == Fraction(next_state + 1, x + 1), "quotient reconstruction")
            current = next_state
            tested += 1
    return {"actual_prefixes": tested, "positive_defect_prefixes": with_reset}


def first_balance_time(b, n, d):
    if 2 * n <= d:
        return 0
    def condition(t):
        return 3 ** (d * t) >= 1 << (n * t + (2 * n - d) * b)
    lower, upper = 0, 1
    while not condition(upper):
        lower, upper = upper, upper * 2
    while upper - lower > 1:
        middle = (lower + upper) // 2
        if condition(middle):
            upper = middle
        else:
            lower = middle
    return upper


def sharp_example(b, n, d):
    t = first_balance_time(b, n, d) + 16
    two_b = 1 << b
    g = two_b - 1
    modulus = 2 * two_b
    coefficient = pow(3, t, modulus) * g
    residue = ((two_b + 1) * pow(coefficient, -1, modulus)) % modulus
    ternary = pow(pow(2, t, 3) * g, -1, 3)
    u = residue + modulus * (((ternary - residue) * pow(modulus, -1, 3)) % 3)
    if u < two_b:
        u += 3 * modulus
    require(two_b <= u < 7 * two_b, "CRT representative")
    x = (g * u << t) - 1
    actual_t, w, actual_b, z = block_from(x)
    require(x % 6 == 3 and (t, b) == (actual_t, actual_b), "ordinary triple and true block")
    require(g == gcd(w, z + 1), "exact retained divisor")
    require(z ** d >= (x + 1) ** n, "prescribed power floor")
    return x, z, t, g


def first_one(x, cap=1000000):
    current = x
    count = 0
    while current != 1 and count < cap:
        current = current // 2 if current % 2 == 0 else (3 * current + 1) // 2
        count += 1
    require(current == 1, "first-hit cap exceeded")
    return count


def sharpness_checks():
    rows = []
    for n, d in [(0, 1), (1, 2), (3, 4), (1, 1), (5, 4), (3, 2)]:
        for b in [3, 11, 31, 127, 511]:
            x, z, t, g = sharp_example(b, n, d)
            row = {
                "sigma": str(Fraction(n, d)), "b": b, "t": t,
                "source_bits": x.bit_length(), "landing_bits": z.bit_length(),
                "gcd_bits": g.bit_length(),
            }
            if b <= 127:
                require(physical_block(x) == (t, b, z), "sharpness true-step replay")
            if n == d:
                require(z > x and physical_block(x) == (t, b, z), "actual protected triple")
                row["first_one_shortcut_triple"] = first_one(x)
                row["first_one_shortcut_cofactor"] = first_one(x // 3)
            rows.append(row)
    return rows


if __name__ == "__main__":
    print(json.dumps({
        "scope": "Finite exact controls. The asymptotic Subspace and logarithmic-forms conclusions are written arguments.",
        "all_small_blocks": exhaustive_blocks(),
        "prefixes": prefix_budgets(),
        "sharpness": sharpness_checks(),
    }, indent=2, sort_keys=True))
