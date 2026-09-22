#!/usr/bin/env python3
"""Independent exact checks for L-9608, L-9609, and T-9608.

The script uses only Python integers.  It is corroboration of the displayed
identities and finite exceptional target classifications; the unbounded
conclusions rest on the committed proofs.
"""

from itertools import combinations, product
from math import comb


def uncentered_constants(a: int, b: int):
    """Return (B positions, C_w) from direct chronological composition."""
    length = a + b
    rows = []
    for b_positions in combinations(range(length), b):
        b_set = set(b_positions)
        constant = 0
        binary_exponent = 0
        for position in range(length):
            if position in b_set:
                constant = 9 * constant + 21 * (1 << binary_exponent)
                binary_exponent += 4
            else:
                constant = 9 * constant
                binary_exponent += 3
        assert binary_exponent == 3 * a + 4 * b
        rows.append((b_positions, constant))
    assert len(rows) == comb(a + b, b)
    return rows


def centered_rows(a: int, b: int):
    q = 8**a * 16**b
    p = 9 ** (a + b)
    d = q - p
    return q, p, d, [
        (positions, constant - 3 * d)
        for positions, constant in uncentered_constants(a, b)
    ]


def direct_centered_constant(word: str) -> int:
    """Compose A: 8y'=9y+3 and B: 16y'=9y directly."""
    constant = 0
    binary_exponent = 0
    for letter in word:
        if letter == "A":
            constant = 9 * constant + 3 * (1 << binary_exponent)
            binary_exponent += 3
        else:
            constant = 9 * constant
            binary_exponent += 4
    return constant


def macro_composite_constant(p: int, q: int, constants) -> int:
    """For q*y'=p*y+e, compose chronological constants."""
    total = 0
    for index, constant in enumerate(constants):
        total = p * total + constant * q**index
    return total


def minimum_targets(d: int, q: int, e_max: int, modulus: int):
    targets = set()
    for minimum in range(1, e_max // d + 1):
        max_carry = (e_max - d * minimum) // q
        for carry in range(max_carry + 1):
            if (minimum + carry) % modulus == 0:
                targets.add(d * minimum + q * carry)
    return targets


def check_generic_lemmas() -> None:
    # L-9608: exhaustive small arbitrary narrow alphabets and word lengths.
    for p, q, alphabet in [
        (3, 8, (4, 7, 11)),
        (5, 16, (19, 25, 31, 34)),
        (7, 32, (100, 106, 113)),
    ]:
        assert max(alphabet) - min(alphabet) < q
        for length in range(1, 6):
            denominator = q**length - p**length
            for indices in product(range(len(alphabet)), repeat=length):
                constants = [alphabet[i] for i in indices]
                numerator = macro_composite_constant(p, q, constants)
                if numerator % denominator == 0:
                    fixed = numerator // denominator
                    states = [fixed]
                    current = fixed
                    legal = True
                    for constant in constants:
                        value = p * current + constant
                        if value % q:
                            legal = False
                            break
                        current = value // q
                        states.append(current)
                    assert legal and current == fixed
                    assert len(set(constants)) == 1
                    assert len(set(states)) == 1
                    assert constants[0] == (q - p) * fixed

    # L-9609: every exact small cycle exposes a target at its minimum.
    p, q = 3, 8
    d = q - p
    alphabet = (5, 10, 15, 20, 25)
    for length in range(1, 7):
        denominator = q**length - p**length
        for constants in product(alphabet, repeat=length):
            numerator = macro_composite_constant(p, q, constants)
            if numerator % denominator:
                continue
            start = numerator // denominator
            if start <= 0:
                continue
            states = [start]
            current = start
            legal = True
            for constant in constants:
                value = p * current + constant
                if value % q:
                    legal = False
                    break
                current = value // q
                states.append(current)
            if not legal or current != start:
                continue
            minimum = min(states[:-1])
            index = states[:-1].index(minimum)
            next_state = states[index + 1]
            carry = next_state - minimum
            assert carry >= 0
            assert constants[index] == d * minimum + q * carry


def check_pulse_formulas() -> None:
    # Direct and shifted formulas, extrema, and divisibility by three.
    for a in range(0, 7):
        for b in range(1, 13):
            q, p, d, rows = centered_rows(a, b)
            values = [value for _, value in rows]
            assert min(values) == 3 * 9**b * (9**a - 8**a)
            assert max(values) == 3 * 16**b * (9**a - 8**a)
            assert all(value % 3 == 0 for value in values)

            for positions, centered in rows:
                b_set = set(positions)
                word = "".join(
                    "B" if index in b_set else "A"
                    for index in range(a + b)
                )
                assert centered == direct_centered_constant(word)

            # Every subcritical packet covered by the theorem misses the exact
            # g=3 minimum target set.  This is finite corroboration through b=12.
            if 1 <= a <= 5 and p < q:
                targets = minimum_targets(d, q, max(values), 3)
                assert set(values).isdisjoint(targets)

    # Exact symbolic height-region boundary checks.
    for a, b in [(2, 1), (3, 2), (4, 3), (5, 4)]:
        assert 9**a * (16**b + 9**b) < 2 * 8**a * 16**b
        assert 9 ** (a + b) < 8**a * 16**b


def check_exception_packets() -> None:
    # Narrow one-pulse packets a=3,4.
    for a, denominator in [(3, 1631), (4, 6487)]:
        b = 1
        q, p, d, rows = centered_rows(a, b)
        assert d == denominator
        uncentered = [constant for _, constant in uncentered_constants(a, b)]
        width = max(uncentered) - min(uncentered)
        assert p < q and width < q
        assert all(constant % d != 0 for constant in uncentered)

    # (a,b)=(4,2): only 3D survives the size filter, then mod 7 rejects it.
    q, p, d, rows = centered_rows(4, 2)
    values = {value for _, value in rows}
    targets = minimum_targets(d, q, max(values), 3)
    assert targets == {3 * d}
    assert {value % 7 for value in values} == {5}
    assert {target % 7 for target in targets} == {2}

    # (a,b)=(5,2): two targets, both 6 mod 9; alphabet is 0/3 mod 9.
    q, p, d, rows = centered_rows(5, 2)
    values = {value for _, value in rows}
    targets = minimum_targets(d, q, max(values), 3)
    assert targets == {2 * d + q, 3 * d}
    assert {value % 9 for value in values} == {0, 3}
    assert {target % 9 for target in targets} == {6}

    # (a,b)=(5,3): two targets 5/6 mod 8; alphabet is 0/3 mod 8.
    q, p, d, rows = centered_rows(5, 3)
    values = {value for _, value in rows}
    targets = minimum_targets(d, q, max(values), 3)
    assert targets == {2 * d + q, 3 * d}
    assert {value % 8 for value in values} == {0, 3}
    assert {target % 8 for target in targets} == {5, 6}

    # Exact one-pulse phase transition.
    for a in range(0, 6):
        q = 16 * 8**a
        p = 9 ** (a + 1)
        values = [constant for _, constant in uncentered_constants(a, 1)]
        width = max(values) - min(values)
        if a <= 4:
            assert p < q and width < q
        else:
            assert p > q and width > q
            assert p - q == 7153


def check_small_all_repetition_packets() -> None:
    # Direct word-level audit of selected multi-macro alphabets.  This is not
    # used to extrapolate the theorem; it checks composition orientation.
    packets = [
        (1, 2, 5),
        (2, 2, 4),
        (3, 2, 3),
        (4, 2, 3),
        (5, 2, 2),
        (5, 3, 2),
    ]
    for a, b, max_length in packets:
        q, p, d, rows = centered_rows(a, b)
        alphabet = [value for _, value in rows]
        assert p < q
        for length in range(1, max_length + 1):
            denominator = q**length - p**length
            for indices in product(range(len(alphabet)), repeat=length):
                numerator = macro_composite_constant(
                    p, q, [alphabet[index] for index in indices]
                )
                assert numerator % denominator != 0


def main() -> None:
    check_generic_lemmas()
    check_pulse_formulas()
    check_exception_packets()
    check_small_all_repetition_packets()
    print("all independent L-9608/L-9609/T-9608 checks passed")


if __name__ == "__main__":
    main()
