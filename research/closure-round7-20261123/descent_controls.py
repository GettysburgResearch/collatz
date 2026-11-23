"""Exact controls for prime-five delay and convergent ordinary shadows.

The delayed-prime examples are positive rational cycles, not ordinary
integer cycles. Only the denominator prime five is delayed; other primes
can already occur in the constant coefficient. The ordinary witnesses
are different convergent integers for different finite prefixes.

All decisions use exact integer or rational arithmetic. These bounded
controls supplement the all-order proofs in ORDINARY_DESCENT.md; they do
not prove a universal ordinary descent or rational-germ construction.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, gcd
import json


class CheckFailure(RuntimeError):
    """A claimed exact finite control failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def valuation(value: int, prime: int) -> int:
    require(value != 0 and prime > 1, "valuation requires a nonzero integer")
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def family_word(a: int, p: int, m: int) -> tuple[int, ...]:
    require(a % 20 == 3 and p % 20 == 1, "wrong base clock residue classes")
    require(a - p >= 2 and p >= 1 and m >= 2, "invalid positive family parameters")
    require(2**a > 3**p, "base clock has nonpositive denominator")
    u = (1,) * p + (0,) * (a - p)
    v = (0,) + (1,) * p + (0,) * (a - p - 1)
    return u * (m - 1) + v


def carry(word: tuple[int, ...]) -> int:
    result = 0
    for degree, bit in enumerate(word):
        require(bit in (0, 1), "nonbinary parity entry")
        if bit:
            result = 3 * result + 2**degree
    return result


def translated_carry(word: tuple[int, ...], count: int) -> list[int]:
    """Translate the full chronological numerator using its append rule."""
    result = [0] * count
    for degree, bit in enumerate(word):
        if bit:
            for j in range(count):
                result[j] *= 3
                if j <= degree:
                    result[j] += comb(degree, j) * 2 ** (degree - j)
    return result


def cycle_jet(word: tuple[int, ...], count: int) -> list[Fraction]:
    numerator = translated_carry(word, count)
    length, odds = len(word), sum(word)
    denominator = [
        -comb(length, j) * 2 ** (length - j) if j <= length else 0
        for j in range(count)
    ]
    denominator[0] += 3**odds
    require(denominator[0] != 0, "Taylor center is a pole")
    result: list[Fraction] = []
    for j in range(count):
        previous = sum(
            (denominator[i] * result[j - i] for i in range(1, j + 1)),
            Fraction(0),
        )
        result.append((numerator[j] - previous) / denominator[0])
    return result


def exact_delay_parameter(a: int, p: int, order: int) -> int:
    """Choose a nonroot lift to give v5((1-m)^a-3^p) exactly order."""
    require(order >= 1, "delay order must be positive")
    require(a % 20 == 3 and p % 20 == 1, "wrong Hensel residue classes")
    root, modulus = 4, 5
    for _ in range(1, order):
        next_modulus = 5 * modulus
        lifts = [
            root + digit * modulus
            for digit in range(5)
            if (pow(1 - root - digit * modulus, a, next_modulus)
                - pow(3, p, next_modulus)) % next_modulus == 0
        ]
        require(len(lifts) == 1, "simple Hensel root did not have a unique lift")
        root, modulus = lifts[0], next_modulus
    next_modulus = 5 * modulus
    candidates = [
        root + digit * modulus
        for digit in range(5)
        if (pow(1 - root - digit * modulus, a, next_modulus)
            - pow(3, p, next_modulus)) % next_modulus != 0
    ]
    require(len(candidates) == 4, "simple root did not have four exact-order lifts")
    m = min(candidates)
    require(m >= 4 and m % 5 == 4, "lift left the positive family")
    require(valuation((1 - m)**a - 3**p, 5) == order,
            "chosen Hensel nonroot lift has the wrong exact valuation")
    return m


def check_family(a: int, p: int, m: int, extra_coefficients: int = 5) -> dict:
    word = family_word(a, p, m)
    q_power, p_power = 2**a, 3**p
    base_carry = p_power - 2**p
    base_denominator = q_power - p_power
    q = Fraction(base_carry, base_denominator)
    geometric = sum(p_power ** (m - 1 - i) * q_power**i for i in range(m))
    full_denominator = q_power**m - p_power**m
    full_carry = base_carry * (geometric + q_power ** (m - 1))
    require(full_denominator == base_denominator * geometric,
            "full denominator factorization failed")
    require(carry(word) == full_carry, "literal carry disagrees with the full family formula")
    require(gcd(geometric, geometric + q_power ** (m - 1)) == 1,
            "the geometric factor was not retained after full reduction")
    require(geometric > base_carry > 0, "nonintegrality size obstruction failed")
    require(full_carry % full_denominator != 0, "rational control became an ordinary cycle")
    source = Fraction(full_carry, full_denominator)
    require(q < source < 2 * q, "cycle source left its exact base interval")
    require(source.denominator > 1 and source.denominator % 2 == 1,
            "cycle source was not a nonintegral odd-denominator rational")

    # Keep the complete odd denominator fixed during literal iteration.
    # Reduction cannot change parity because every cancelled factor is odd.
    numerator = full_carry
    smallest_numerator = numerator
    for bit in word:
        require(numerator > 0, "literal rational orbit lost positivity")
        require(numerator % 2 == bit, "family word disagrees with actual rational parity")
        smallest_numerator = min(smallest_numerator, numerator)
        numerator = ((3 * numerator + full_denominator) // 2 if bit
                     else numerator // 2)
    require(numerator == full_carry, "literal rational family did not close")
    minimum = Fraction(smallest_numerator, full_denominator)
    require(minimum > q / 2, "literal orbit violated the claimed strict floor")

    # The cyclic word starts at the first one of a run. Its zero-run lengths
    # have one unique maximum, proving that this is a primitive word.
    zero_runs, run = [], 0
    for bit in word[1:] + word[:1]:
        if bit == 0:
            run += 1
        elif run:
            zero_runs.append(run)
            run = 0
    require(zero_runs.count(a - p + 1) == 1,
            "primitive-word certificate lost its unique longest zero run")
    require(sorted(zero_runs) == sorted([a - p] * (m - 2) + [a - p - 1, a - p + 1]),
            "cyclic zero-run census disagrees with the construction")

    require(m % 5 == 4, "delay test requires m congruent to four modulo five")
    delay = valuation((1 - m)**a - p_power, 5)
    require(valuation(full_denominator, 5) == 1,
            "complete denominator has an unexpected five-adic valuation")
    require(valuation(full_carry, 5) >= 1,
            "the constant coefficient did not cancel denominator five")
    coefficients = cycle_jet(word, delay + extra_coefficients)
    require(coefficients[0] == -source, "actual Taylor constant is not the negative source")
    observed = [valuation(coefficient.denominator, 5) for coefficient in coefficients]
    expected = [max(0, j + 1 - delay) for j in range(len(coefficients))]
    require(observed == expected, "exact prime-five denominator law failed")
    return {
        "A": a,
        "p": p,
        "m": m,
        "word_length": len(word),
        "odd_steps": sum(word),
        "full_denominator_bits": full_denominator.bit_length(),
        "reduced_source_denominator_bits": source.denominator.bit_length(),
        "primitive_word": True,
        "ordinary_integer_source": False,
        "minimum_greater_than": str(q / 2) if a <= 3 else minimum.numerator // minimum.denominator,
        "first_denominator_five_order": delay,
        "checked_denominator_five_exponents": observed,
        "all_literal_cycle_steps_checked": len(word),
    }


def convergent_shadow(word: tuple[int, ...], rational_source: Fraction, count: int) -> dict:
    """Construct and follow a genuine ordinary prefix ending at a power of two."""
    length, odds = len(word), sum(word)
    require(odds > 0, "power-of-two shadow control requires an odd step")
    full_carry = carry(word)
    modulus = 3**odds
    period = 2 * 3 ** (odds - 1)
    require(gcd(full_carry, 3) == 1, "complete carry was not a unit modulo three")
    require(period <= 5000, "bounded shadow replay exceeded its declared exponent search")
    target = full_carry % modulus
    residue = pow(2, length, modulus)
    endpoint_exponent = None
    for candidate in range(period):
        if residue == target:
            endpoint_exponent = candidate
            break
        residue = 2 * residue % modulus
    require(endpoint_exponent is not None, "unit power-of-two endpoint was not found")
    while Fraction(2 ** (length + endpoint_exponent) - full_carry, modulus) <= rational_source:
        endpoint_exponent += period
    source = (2 ** (length + endpoint_exponent) - full_carry) // modulus
    require(modulus * source + full_carry == 2 ** (length + endpoint_exponent),
            "ordinary endpoint construction lost exact divisibility")
    require(source > rational_source and source > 0, "ordinary shadow is not above its rational source")

    ordinary, rational = source, rational_source
    for bit in word:
        require(ordinary % 2 == bit, "ordinary prefix disagrees with its prescribed parity")
        require(rational.numerator % 2 == bit and rational.denominator % 2 == 1,
                "rational prefix disagrees with its prescribed parity")
        require(ordinary >= rational, "ordinary finite segment fell below its rational shadow")
        ordinary = (3 * ordinary + 1) // 2 if bit else ordinary // 2
        rational = (3 * rational + 1) / 2 if bit else rational / 2
    require(ordinary == 2**endpoint_exponent, "ordinary prefix did not reach its power-of-two endpoint")
    for _ in range(endpoint_exponent):
        require(ordinary % 2 == 0, "power-of-two tail acquired an odd step before one")
        ordinary //= 2
    require(ordinary == 1, "constructed ordinary shadow failed to converge")

    # After the prescribed word and the zero tail, the actual tail at one is
    # 1/(3-z^2). Its translated denominator has unit constant term -1.
    one_jet: list[Fraction] = []
    for j in range(count):
        one_jet.append(Fraction(-1) if j == 0 else
                       -4 * one_jet[j - 1] - (one_jet[j - 2] if j >= 2 else 0))
    prefix_jet = translated_carry(word, count)
    shift = length + endpoint_exponent
    ordinary_jet = [
        (prefix_jet[j] + sum(
            (comb(shift, i) * 2 ** (shift - i) * one_jet[j - i]
             for i in range(min(j, shift) + 1)), Fraction(0),
        )) / modulus
        for j in range(count)
    ]
    rational_jet = cycle_jet(word, count)
    require(ordinary_jet[0] == -source, "ordinary Taylor source identity failed")
    bounds = []
    for j, (ordinary_coefficient, rational_coefficient) in enumerate(zip(ordinary_jet, rational_jet)):
        denominator = ordinary_coefficient.denominator
        while denominator % 3 == 0:
            denominator //= 3
        require(denominator == 1, "convergent ordinary coefficient acquired a forbidden prime")
        difference = ordinary_coefficient - rational_coefficient
        require(difference.denominator % 2 == 1, "binary jet difference is not two-integral")
        observed = None if difference == 0 else valuation(difference.numerator, 2)
        if j <= length:
            require(observed is None or observed >= length - j,
                    "ordinary/rational finite jet shadow bound failed")
        bounds.append(observed)
    return {
        "prefix_length": length,
        "prefix_odd_steps": odds,
        "ordinary_source": source if source.bit_length() <= 64 else None,
        "ordinary_source_bits": source.bit_length(),
        "power_of_two_endpoint_exponent": endpoint_exponent,
        "literal_steps_through_hit_one": length + endpoint_exponent,
        "checked_ordinary_coefficients_in_Z_one_third": count,
        "binary_jet_difference_valuations": bounds,
        "binary_jet_difference_lower_bounds": [length - j for j in range(count)],
        "changing_ordinary_witness": True,
    }


def run_checks() -> dict:
    hensel_parameters = [exact_delay_parameter(3, 1, order) for order in range(1, 5)]
    require(hensel_parameters == [4, 14, 39, 414], "deterministic Hensel fixtures changed")
    families = [check_family(3, 1, m) for m in hensel_parameters]
    high_floor = check_family(6183, 3901, 4)
    high_q = Fraction(3**3901 - 2**3901, 2**6183 - 3**3901)
    require(high_q / 2 > 11, "high-floor control did not stay strictly above eleven")
    high_floor["minimum_greater_than"] = 11
    families.append(high_floor)
    base_word = family_word(3, 1, 4)
    base_source = Fraction(carry(base_word), 2 ** len(base_word) - 3 ** sum(base_word))
    shadows = [convergent_shadow(base_word * repetitions, base_source, 8)
               for repetitions in (1, 2)]
    return {
        "status": "PASS",
        "arithmetic": "exact integers and fractions; no optimization-sensitive assertions",
        "family_controls": families,
        "convergent_ordinary_shadows": shadows,
        "scope": {
            "delay_concerns_only_prime_five": True,
            "rational_family_has_other_source_denominator_primes": True,
            "all_order_delay_proof_is_written_mathematics": True,
            "finite_jet_replay_is_not_an_all_order_computation": True,
            "ordinary_shadow_source_changes_with_prefix": True,
            "ordinary_collatz_conjecture_proved": False,
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
