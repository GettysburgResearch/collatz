"""Exact instances of the joint rational-cycle construction.

This checks a constructive family and CRT realizations, not a cycle census
or an exclusion of positive integer escape. All decisions use integers and
fractions; optimized Python executes the same explicit guards.
"""
from __future__ import annotations

import json
from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def valuation_two(n: int) -> int:
    require(n != 0, "valuation at zero")
    n = abs(n)
    return (n & -n).bit_length() - 1


def correction(word: list[int]) -> int:
    value, power = 0, 1
    for gap in word:
        require(gap > 0, "nonpositive gap")
        value = 3 * value + power
        power <<= gap
    return value


def fraction_residue(x: Fraction, modulus: int) -> int:
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus


def construct(binary: int, binary_depth: int, ternary: int,
              ternary_depth: int, sign: int = -1) -> dict:
    require(binary_depth > 0 and ternary_depth > 0, "positive precision required")
    require(binary % 2 == 1 and ternary % 3 != 0, "unit cylinders required")
    require(sign in (-1, 1), "cycle sign")
    q = binary % (1 << binary_depth)
    while q % 3 == 0:
        q += 1 << binary_depth
    endpoint = q
    prefix: list[int] = []
    total = 0
    while total < binary_depth:
        gap = valuation_two(3 * endpoint + 1)
        prefix.append(gap)
        total += gap
        endpoint = (3 * endpoint + 1) >> gap
    modulus = 3 ** ternary_depth
    period = 2 * 3 ** (ternary_depth - 1)
    last = next(e for e in range(1, period + 1)
                if (-2 * pow(2, -e, modulus)) % modulus == ternary % modulus)
    ones = ternary_depth - 1
    if sign < 0:
        while 3 ** (len(prefix) + ones + 1) <= 2 ** (total + ones + last):
            ones += 1
    else:
        while 2 ** (total + ones + last) <= 3 ** (len(prefix) + ones + 1):
            last += period
    word = prefix + [1] * ones + [last]
    count, clock = len(word), sum(word)
    numerator = correction(word)
    denominator = (1 << clock) - 3 ** count
    root = Fraction(numerator, denominator)
    require((root > 0) == (sign > 0), "incorrect real sign")
    require(numerator == 3 ** (ones + 1) * (correction(prefix) + (1 << total))
            - (1 << (total + ones + 1)), "whole numerator identity")
    require(fraction_residue(root, 1 << binary_depth) == binary % (1 << binary_depth),
            "initial binary cylinder")
    require(fraction_residue(root, modulus) == ternary % modulus,
            "initial ternary cylinder")
    state = root
    for gap in word:
        require(state.numerator % 2 == 1 and state.denominator % 6 in (1, 5)
                and state.numerator % 3 != 0, "rational state is not a joint unit")
        require((state > 0) == (sign > 0), "rotation changed sign")
        numerator_step = 3 * state + 1
        require(valuation_two(numerator_step.numerator) == gap, "nonexact rational gap")
        state = numerator_step / (1 << gap)
    require(state == root, "cycle did not close")

    crt_checks = []
    for precision in (1, 3, 5):
        binary_modulus = 1 << (clock + precision + 1)
        ternary_modulus = 3 ** precision
        binary_value = fraction_residue(root, binary_modulus)
        ternary_value = fraction_residue(root, ternary_modulus)
        lift = ((ternary_value - binary_value)
                * pow(binary_modulus, -1, ternary_modulus)) % ternary_modulus
        full_modulus = binary_modulus * ternary_modulus
        start = binary_value + binary_modulus * lift + full_modulus
        state_n = start
        for gap in word:
            require(valuation_two(3 * state_n + 1) == gap, "CRT ordinary gap mismatch")
            state_n = (3 * state_n + 1) >> gap
            require(state_n > 0 and state_n % 6 in (1, 5), "ordinary state left domain")
        require((1 << clock) * state_n == 3 ** count * start + numerator,
                "ordinary full affine identity")
        for prime in (2, 3):
            pmod = prime ** precision
            require(start % pmod == fraction_residue(root, pmod), "initial CRT phase")
            require(state_n % pmod == fraction_residue(root, pmod), "terminal CRT phase")
        crt_checks.append({"precision": precision, "start_bits": start.bit_length(),
                           "endpoint_bits": state_n.bit_length()})
    return {"binary": binary, "binary_depth": binary_depth,
            "ternary": ternary, "ternary_depth": ternary_depth,
            "sign": sign, "prefix": prefix, "ones": ones, "last": last,
            "word_length": count, "total_gap": clock,
            "numerator": root.numerator, "denominator": root.denominator,
            "crt_checks": crt_checks}


def bridge(source_binary: int, source_binary_depth: int, source_ternary: int,
           source_ternary_depth: int, target_binary: int, target_binary_depth: int,
           target_ternary: int, target_ternary_depth: int) -> dict:
    """An actual ordinary path between two prescribed product cylinders."""
    require(source_binary % 2 == target_binary % 2 == 1, "binary units required")
    require(source_ternary % 3 != 0 and target_ternary % 3 != 0, "ternary units required")
    q = source_binary % (1 << source_binary_depth)
    while q % 3 == 0:
        q += 1 << source_binary_depth
    word, prefix_clock = [], 0
    while prefix_clock < source_binary_depth:
        gap = valuation_two(3 * q + 1)
        word.append(gap)
        prefix_clock += gap
        q = (3 * q + 1) >> gap
    ternary_modulus = 3 ** target_ternary_depth
    period = 2 * 3 ** (target_ternary_depth - 1)
    last = next(e for e in range(1, period + 1)
                if (-2 * pow(2, -e, ternary_modulus)) % ternary_modulus
                == target_ternary % ternary_modulus)
    word += [1] * target_ternary_depth + [last]
    clock, count = sum(word), len(word)
    binary_modulus = 1 << (clock + target_binary_depth)
    initial_binary = (((1 << clock) * target_binary - correction(word))
                      * pow(3 ** count, -1, binary_modulus)) % binary_modulus
    initial_ternary_modulus = 3 ** source_ternary_depth
    lift = ((source_ternary - initial_binary)
            * pow(binary_modulus, -1, initial_ternary_modulus)) % initial_ternary_modulus
    start = initial_binary + binary_modulus * lift + binary_modulus * initial_ternary_modulus
    endpoint = start
    for gap in word:
        require(valuation_two(3 * endpoint + 1) == gap, "bridge gap mismatch")
        endpoint = (3 * endpoint + 1) >> gap
    require(start % (1 << source_binary_depth) == source_binary % (1 << source_binary_depth),
            "bridge source binary")
    require(start % initial_ternary_modulus == source_ternary % initial_ternary_modulus,
            "bridge source ternary")
    require(endpoint % (1 << target_binary_depth) == target_binary % (1 << target_binary_depth),
            "bridge target binary")
    require(endpoint % ternary_modulus == target_ternary % ternary_modulus,
            "bridge target ternary")
    return {"source": [source_binary, source_binary_depth, source_ternary, source_ternary_depth],
            "target": [target_binary, target_binary_depth, target_ternary, target_ternary_depth],
            "word": word, "start": start, "endpoint": endpoint}


def main() -> None:
    parameters = [(1, 1, 1, 1), (1, 1, 2, 1), (3, 2, 4, 2),
                  (5, 3, 8, 2), (7, 3, 10, 3), (9, 4, 13, 3),
                  (11, 4, 17, 3), (13, 4, 23, 3), (15, 4, 26, 3),
                  (17, 5, 31, 4), (23, 5, 59, 4), (31, 5, 80, 4)]
    cases = [construct(*p, sign) for sign in (-1, 1) for p in parameters]
    bridges = [bridge(*parameters[i], *parameters[(5 * i + 3) % len(parameters)])
               for i in range(len(parameters))]
    print(json.dumps({"scope": "exact rational cycle construction and finite ordinary CRT paths",
                      "cases": cases, "cycle_rotations_checked": sum(c["word_length"] for c in cases),
                      "ordinary_paths_checked": sum(len(c["crt_checks"]) for c in cases),
                      "product_cylinder_bridges": bridges,
                      "status": "PASS; not a positive integer cycle exclusion"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
