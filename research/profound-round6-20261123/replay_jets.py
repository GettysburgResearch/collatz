"""Bounded exact controls for the actual translated Collatz Taylor series.

The primitive-word census concerns positive rational cycles with odd reduced
denominators. It does not manufacture positive ordinary integer cycles. The
ordinary-source checks follow the literal shortcut map until its first hit
of one, with a fixed cap, and compare two independent coefficient formulas.

All arithmetic is exact. Finite coefficient observations do not verify an
asymptotic denominator-growth conclusion or a universal germ hypothesis.
No optional dependency is needed. Normal and optimized Python run the same
explicit checks; there are no optimization-sensitive assertions.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, gcd
import json


CYCLE_MAX_LENGTH = 10
CYCLE_COEFFICIENTS = 12
ORDINARY_COEFFICIENTS = 32
ORDINARY_STEP_CAP = 10_000


class CheckFailure(RuntimeError):
    """An exact bounded replay identity failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def carry(word: tuple[int, ...]) -> int:
    """Complete chronological affine carry, using an append recurrence."""
    result = 0
    for k, bit in enumerate(word):
        require(bit in (0, 1), "word contains a nonbinary entry")
        if bit:
            result = 3 * result + 2**k
    return result


def primitive(word: tuple[int, ...]) -> bool:
    size = len(word)
    return not any(
        size % period == 0 and word == word[:period] * (size // period)
        for period in range(1, size)
    )


def cycle_numerator(word: tuple[int, ...]) -> list[int]:
    """N(z) in B(z)=N(z)/(3^p-z^A), independently of carry()."""
    total_odds = sum(word)
    seen = 0
    coefficients = []
    for bit in word:
        seen += bit
        coefficients.append(3 ** (total_odds - seen) if bit else 0)
    return coefficients


def evaluate_at_two(coefficients: list[int]) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = 2 * result + coefficient
    return result


def binomial_remainder(coefficients: list[int], u: int, v: int) -> list[int]:
    """Exact integer remainder modulo z^u-3^v, with zero padding retained."""
    require(u > 0 and v > 0, "nonpositive reduced clock")
    result = [0] * u
    for degree, coefficient in enumerate(coefficients):
        quotient, residue = divmod(degree, u)
        result[residue] += coefficient * 3 ** (v * quotient)
    return result


def translate_at_two(coefficients: list[int], count: int) -> list[int]:
    """The first count coefficients of an integer polynomial at z=2+t."""
    result = [0] * count
    for degree, coefficient in enumerate(coefficients):
        if coefficient:
            for j in range(min(degree + 1, count)):
                result[j] += coefficient * comb(degree, j) * 2 ** (degree - j)
    return result


def cycle_jet(word: tuple[int, ...], count: int) -> list[Fraction]:
    """Exact Taylor coefficients from the translated rational denominator."""
    size, odds = len(word), sum(word)
    numerator = translate_at_two(cycle_numerator(word), count)
    denominator = [-comb(size, j) * 2 ** (size - j)
                   if j <= size else 0 for j in range(count)]
    denominator[0] += 3**odds
    require(denominator[0] != 0, "Taylor center is a cycle pole")
    coefficients: list[Fraction] = []
    for j in range(count):
        convolution = sum(
            (denominator[i] * coefficients[j - i] for i in range(1, j + 1)),
            Fraction(0),
        )
        coefficients.append((numerator[j] - convolution) / denominator[0])
    return coefficients


def forward_jet(coefficients: list[Fraction], bit: int) -> list[Fraction]:
    """Solve (2+t) J_next=3^bit J_current-bit, coefficient by coefficient."""
    result: list[Fraction] = []
    for j, coefficient in enumerate(coefficients):
        correction = bit if j == 0 else result[j - 1]
        result.append((3**bit * coefficient - correction) / 2)
    return result


def prime_factors(value: int) -> dict[int, int]:
    require(value > 0, "factorization requires a positive integer")
    result: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            exponent = 0
            while value % divisor == 0:
                value //= divisor
                exponent += 1
            result[divisor] = exponent
        divisor += 1
    if value > 1:
        result[value] = 1
    return result


def valuation(value: int, prime: int) -> int:
    require(value > 0 and prime > 1, "invalid finite valuation arguments")
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def check_rational_cycle(word: tuple[int, ...], count: int) -> dict:
    """Check one complete rational cycle and every chronological jet step."""
    size, odds = len(word), sum(word)
    full_denominator = 2**size - 3**odds
    require(odds > 0 and full_denominator > 0, "cycle is outside positive scope")
    complete_carry = carry(word)
    numerator = cycle_numerator(word)
    require(evaluate_at_two(numerator) == complete_carry,
            "polynomial numerator lost a chronological affine carry")
    numerical_gcd = gcd(full_denominator, complete_carry)
    source = Fraction(complete_carry, full_denominator)
    require(source > 0 and source.denominator % 2 == 1,
            "rational cycle is not positive with odd reduced denominator")
    require(source.denominator == full_denominator // numerical_gcd,
            "full numerical gcd did not retain the reduced denominator")

    common = gcd(size, odds)
    u, v = size // common, odds // common
    reduced_denominator = 2**u - 3**v
    require(reduced_denominator > 0 and gcd(u, v) == 1,
            "invalid positive coprime reduced clock")
    require(full_denominator % reduced_denominator == 0,
            "reduced-clock value does not divide the full denominator")
    remainder = binomial_remainder(numerator, u, v)
    require(all(coefficient >= 0 for coefficient in remainder)
            and any(coefficient > 0 for coefficient in remainder),
            "positive cycle numerator cancelled the reduced-clock polynomial")
    denominator_polynomial = [3**odds] + [0] * (size - 1) + [-1]
    require(not any(binomial_remainder(denominator_polynomial, u, v)),
            "reduced-clock polynomial does not divide the full denominator polynomial")
    require((evaluate_at_two(remainder) - complete_carry) % reduced_denominator == 0,
            "polynomial remainder and numerical full carry disagree modulo F(2)")
    reduced_numerical_gcd = gcd(reduced_denominator, complete_carry)
    require(source.denominator % (reduced_denominator // reduced_numerical_gcd) == 0,
            "reduced-factor numerical denominator was not retained in the full quotient")

    coefficients = cycle_jet(word, count)
    require(coefficients[0] == -source, "cycle constant coefficient is not its negative source")
    current_source, current_jet = source, coefficients
    states = []
    for bit in word:
        require(current_source > 0 and current_source.denominator % 2 == 1,
                "literal rational step left the positive odd-denominator domain")
        require(current_source.numerator % 2 == bit,
                "prescribed bit disagrees with the literal rational parity")
        require(current_jet[0] == -current_source,
                "chronological Taylor transport lost the actual rational state")
        states.append(current_source)
        current_source = ((3 * current_source + 1) / 2 if bit
                          else current_source / 2)
        current_jet = forward_jet(current_jet, bit)
    require(current_source == source, "rational word did not return to its original source")
    require(current_jet == coefficients, "Taylor recurrence failed after a complete cycle")
    if primitive(word):
        require(len(set(states)) == size, "primitive parity word had a smaller state period")

    factors = prime_factors(reduced_denominator)
    observed, cancelled_at_constant, reappeared = 0, 0, 0
    for prime, exponent in factors.items():
        require(prime not in (2, 3), "reduced denominator acquired a two or three factor")
        full_exponent = valuation(full_denominator, prime)
        carry_exponent = valuation(complete_carry, prime)
        require(exponent <= full_exponent, "a reduced prime power exceeded its full power")
        require(valuation(numerical_gcd, prime) == min(full_exponent, carry_exponent),
                "full numerical gcd lost a prime-power valuation")
        require(valuation(source.denominator, prime) == max(0, full_exponent - carry_exponent),
                "reduced rational source lost a full-denominator prime power")
        seen_in_checked_jet = any(coefficient.denominator % prime == 0
                                  for coefficient in coefficients)
        observed += int(seen_in_checked_jet)
        if coefficients[0].denominator % prime != 0:
            cancelled_at_constant += 1
            reappeared += int(seen_in_checked_jet)

    return {
        "word": "".join(map(str, word)),
        "A": size,
        "p": odds,
        "full_denominator": full_denominator,
        "complete_carry": complete_carry,
        "full_numerical_gcd": numerical_gcd,
        "reduced_clock_denominator": reduced_denominator,
        "reduced_clock_numerical_gcd": reduced_numerical_gcd,
        "source": source,
        "states": states,
        "numerator_remainder": remainder,
        "coefficients": coefficients,
        "reduced_prime_instances": len(factors),
        "observed_reduced_prime_instances": observed,
        "cancelled_reduced_primes_at_constant": cancelled_at_constant,
        "reappeared_in_checked_coefficients": reappeared,
    }


def terminal_one_jet(count: int) -> list[Fraction]:
    """J_1(t)=-1/(1+4t+t^2), computed by its integer recurrence."""
    require(count > 0, "empty terminal jet")
    result = [Fraction(-1)]
    for j in range(1, count):
        result.append(-4 * result[j - 1] - (result[j - 2] if j >= 2 else 0))
    require(all(coefficient.denominator == 1 for coefficient in result),
            "standard-cycle translated coefficients are not integral")
    return result


def ordinary_prefix(source: int) -> tuple[tuple[int, ...], list[int]]:
    require(source > 0, "ordinary replay source must be positive")
    states, bits = [source], []
    current = source
    while current != 1:
        require(len(bits) < ORDINARY_STEP_CAP, "ordinary source exceeded the finite step cap")
        bit = current % 2
        bits.append(bit)
        current = (3 * current + 1) // 2 if bit else current // 2
        require(current > 0, "ordinary shortcut step is not positive")
        states.append(current)
    return tuple(bits), states


def reverse_prefix_jet(word: tuple[int, ...], count: int) -> list[Fraction]:
    """Construct J_n backwards from J_1 using each actual shortcut step."""
    coefficients = terminal_one_jet(count)
    for bit in reversed(word):
        previous = coefficients
        coefficients = [
            (2 * previous[j] + (bit if j == 0 else previous[j - 1])) / 3**bit
            for j in range(count)
        ]
    return coefficients


def direct_prefix_jet(word: tuple[int, ...], count: int) -> list[Fraction]:
    """Independently translate P_N(z)+z^N*3^(-s)/(3-z^2)."""
    result = [Fraction(0) for _ in range(count)]
    seen = 0
    for degree, bit in enumerate(word):
        seen += bit
        if bit:
            for j in range(min(degree + 1, count)):
                result[j] += Fraction(comb(degree, j) * 2 ** (degree - j), 3**seen)
    size, odds = len(word), sum(word)
    translated_multiplier = [
        Fraction(comb(size, j) * 2 ** (size - j), 3**odds) if j <= size else Fraction(0)
        for j in range(count)
    ]
    terminal = terminal_one_jet(count)
    for j in range(count):
        result[j] += sum(
            (translated_multiplier[i] * terminal[j - i] for i in range(j + 1)),
            Fraction(0),
        )
    return result


def run_checks() -> dict:
    census = {
        "maximum_word_length": CYCLE_MAX_LENGTH,
        "coefficients_per_word": CYCLE_COEFFICIENTS,
        "primitive_positive_rational_words": 0,
        "literal_rational_steps": 0,
        "nonzero_positive_polynomial_remainders": 0,
        "reduced_clock_value_one_words": 0,
        "entire_reduced_clock_value_cancels_at_constant": 0,
        "reduced_prime_instances": 0,
        "observed_reduced_prime_instances": 0,
        "cancelled_reduced_primes_at_constant": 0,
        "reappeared_in_checked_coefficients": 0,
        "ordinary_integer_cycle_words_in_this_census": [],
    }
    for size in range(1, CYCLE_MAX_LENGTH + 1):
        for mask in range(1, 2**size):
            word = tuple((mask >> k) & 1 for k in range(size))
            if not primitive(word) or 2**size <= 3 ** sum(word):
                continue
            control = check_rational_cycle(word, CYCLE_COEFFICIENTS)
            census["primitive_positive_rational_words"] += 1
            census["literal_rational_steps"] += size
            census["nonzero_positive_polynomial_remainders"] += 1
            reduced = control["reduced_clock_denominator"]
            census["reduced_clock_value_one_words"] += int(reduced == 1)
            census["entire_reduced_clock_value_cancels_at_constant"] += int(
                reduced > 1 and control["complete_carry"] % reduced == 0
            )
            for key in (
                "reduced_prime_instances", "observed_reduced_prime_instances",
                "cancelled_reduced_primes_at_constant", "reappeared_in_checked_coefficients",
            ):
                census[key] += control[key]
            if control["source"].denominator == 1:
                census["ordinary_integer_cycle_words_in_this_census"].append(control["word"])
    census["ordinary_integer_cycle_words_in_this_census"].sort()
    require(census["ordinary_integer_cycle_words_in_this_census"] == ["01", "10"],
            "bounded primitive ordinary-cycle control differs from the standard two rotations")
    census["unobserved_reduced_prime_instances_in_this_finite_jet"] = (
        census["reduced_prime_instances"] - census["observed_reduced_prime_instances"]
    )

    example = check_rational_cycle((1, 1, 0, 0, 0, 0), 32)
    require(example["source"] == Fraction(1, 11), "110000 has the wrong rational source")
    require(example["full_denominator"] == 55 and example["complete_carry"] == 5,
            "110000 did not retain its complete denominator and carry")
    require(example["full_numerical_gcd"] == 5
            and example["reduced_clock_denominator"] == 5,
            "110000 did not exhibit the reduced-clock cancellation at its value")
    require(example["coefficients"][0] == Fraction(-1, 11)
            and example["coefficients"][1] == Fraction(181, 605),
            "110000 did not exhibit the exact first-derivative denominator reappearance")
    for j in range(1, 32):
        require(valuation(example["coefficients"][j].denominator, 5) == j,
                f"110000 denominator exponent at order {j} differs from j")
    example_output = {
        "word": example["word"],
        "kind": "positive rational cycle; not an ordinary integer cycle",
        "source": str(example["source"]),
        "states": list(map(str, example["states"])),
        "complete_carry": example["complete_carry"],
        "full_denominator": example["full_denominator"],
        "full_numerical_gcd": example["full_numerical_gcd"],
        "reduced_clock_denominator": example["reduced_clock_denominator"],
        "numerator_remainder_mod_reduced_polynomial": example["numerator_remainder"],
        "c0": str(example["coefficients"][0]),
        "c1": str(example["coefficients"][1]),
        "exact_five_adic_denominator_control": {
            "identity": "v_5(den(c_j)) = j",
            "first_checked_order": 1,
            "last_checked_order": 31,
            "scope": "31 finite checks; the unrestricted identity requires the written induction",
        },
    }

    sources = sorted(set(range(1, 129)) | {27, 6171, 77031, 837799})
    ordinary = {
        "initial_source_interval": [1, 128],
        "additional_requested_sources": [27, 6171, 77031, 837799],
        "distinct_sources_checked": len(sources),
        "coefficients_per_source": ORDINARY_COEFFICIENTS,
        "step_cap_per_source": ORDINARY_STEP_CAP,
        "independent_coefficient_comparisons": 0,
        "literal_shortcut_steps_total": 0,
        "maximum_steps_to_first_one": 0,
        "maximum_prefix_odd_count": 0,
        "largest_ordinary_state_encountered": 1,
        "uniform_ternary_denominator_checks": 0,
    }
    for source in sources:
        word, states = ordinary_prefix(source)
        size, odds = len(word), sum(word)
        require(states[0] == source and states[-1] == 1,
                "ordinary prefix has the wrong original source or terminal state")
        require(2**size == 3**odds * source + carry(word),
                "ordinary prefix violates its complete affine identity")
        reverse = reverse_prefix_jet(word, ORDINARY_COEFFICIENTS)
        direct = direct_prefix_jet(word, ORDINARY_COEFFICIENTS)
        require(reverse == direct, f"independent Taylor constructions differ at source {source}")
        require(reverse[0] == -source, f"ordinary Taylor constant differs at source {source}")
        scale = 3**odds
        for coefficient in reverse:
            require(scale % coefficient.denominator == 0,
                    f"coefficient denominator does not divide 3^s at source {source}")
            require(set(prime_factors(coefficient.denominator)) <= {3},
                    f"nonternary coefficient denominator at source {source}")
        ordinary["independent_coefficient_comparisons"] += ORDINARY_COEFFICIENTS
        ordinary["uniform_ternary_denominator_checks"] += ORDINARY_COEFFICIENTS
        ordinary["literal_shortcut_steps_total"] += size
        ordinary["maximum_steps_to_first_one"] = max(ordinary["maximum_steps_to_first_one"], size)
        ordinary["maximum_prefix_odd_count"] = max(ordinary["maximum_prefix_odd_count"], odds)
        ordinary["largest_ordinary_state_encountered"] = max(
            ordinary["largest_ordinary_state_encountered"], max(states)
        )

    return {
        "status": "PASS",
        "arithmetic": "exact Python integers and fractions; explicit checks active under -O",
        "scope": (
            "Finite primitive rational-cycle census and finite actual convergent-source controls. "
            "No asymptotic denominator-growth extrapolation, arbitrary-source germ construction, "
            "or unrestricted cycle exclusion is established by this replay."
        ),
        "cycle_census": census,
        "constant_cancellation_control": example_output,
        "ordinary_convergent_controls": ordinary,
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
