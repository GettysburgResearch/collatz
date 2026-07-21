#!/usr/bin/env python3
"""Exact checks for L-0007, L-0008, and T-0006.

Standard library only; all arithmetic is exact.
"""

from __future__ import annotations

from itertools import product


def affine_constant(word: str) -> int:
    remaining = word.count("1")
    value = 0
    for index, bit in enumerate(word):
        if bit == "1":
            remaining -= 1
            value += (1 << index) * (3**remaining)
        elif bit != "0":
            raise ValueError("nonbinary word")
    return value


def v3(value: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero is not used")
    value = abs(value)
    exponent = 0
    while value % 3 == 0:
        value //= 3
        exponent += 1
    return exponent


def one_word(length: int, position: int) -> str:
    chars = ["0"] * length
    chars[position] = "1"
    return "".join(chars)


def atomic_code(precision: int) -> tuple[str, str]:
    radius = 2 * 3 ** (precision - 1)
    length = radius + 1
    return one_word(length, 0), one_word(length, radius)


def concatenate(left: tuple[str, ...], right: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(u + v for u, v in product(left, right))


def code_precision(code: tuple[str, ...]) -> int:
    reference = affine_constant(code[0])
    return min(v3(affine_constant(word) - reference) for word in code[1:])


def offsets(code: tuple[str, ...], denominator_power: int | None = None) -> tuple[int, ...]:
    weight = code[0].count("1") if denominator_power is None else denominator_power
    denominator = 3**weight
    reference = affine_constant(code[0])
    values = []
    for word in code:
        difference = affine_constant(word) - reference
        assert difference % denominator == 0
        values.append(-difference // denominator)
    return tuple(values)


def crt_pair(a: int, modulus_a: int, b: int, modulus_b: int) -> int:
    """Least nonnegative x with x=a mod modulus_a and x=b mod modulus_b."""
    inverse = pow(modulus_a, -1, modulus_b)
    multiplier = ((b - a) * inverse) % modulus_b
    return a + modulus_a * multiplier


def shortcut(value: int) -> int:
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def trace_word(value: int, length: int) -> tuple[str, int]:
    bits = []
    state = value
    for _ in range(length):
        bits.append(str(state & 1))
        state = shortcut(state)
    return "".join(bits), state


def verify_atomic_codes() -> None:
    for precision in range(1, 9):
        low, high = atomic_code(precision)
        difference = affine_constant(high) - affine_constant(low)
        radius = 2 * 3 ** (precision - 1)
        assert difference == 2**radius - 1
        assert v3(difference) == precision
        quotient = difference // 3**precision
        assert quotient % 2 == 1
    print("verified L-0008 for precisions 1..8")


def verify_tensor_hierarchy() -> tuple[str, ...]:
    # A small base code of length 7, weight 2, and precision exactly 4.
    base = ("1010000", "0001001")
    assert [affine_constant(word) for word in base] == [7, 88]
    assert code_precision(base) == 4
    assert sorted(offsets(base)) == [-9, 0]

    code = base
    previous_offsets = set(offsets(code))
    expected_rows = [
        (1, 4, 26, 3, 3),
        (2, 8, 81, 4, 4),
        (3, 16, 244, 5, 5),
    ]

    for index, precision in enumerate((3, 4, 5), start=1):
        left = code
        right = atomic_code(precision)
        left_length = len(left[0])
        left_weight = left[0].count("1")
        total_weight = left_weight + 1

        left_offsets = offsets(left)
        right_offsets = offsets(right, denominator_power=total_weight)
        predicted = {
            left_offset + (1 << left_length) * right_offset
            for left_offset in left_offsets
            for right_offset in right_offsets
        }

        code = concatenate(left, right)
        actual = set(offsets(code))
        assert actual == predicted
        assert len(actual) == len(left) * len(right)
        assert previous_offsets.issubset(actual)
        assert {-9, 0}.issubset(actual)
        assert 9 in {x - y for x in actual for y in actual}

        row = (
            index,
            len(code),
            len(code[0]),
            code[0].count("1"),
            code_precision(code),
        )
        assert row == expected_rows[index - 1]
        print(
            f"level={index} words={row[1]} length={row[2]} "
            f"weight={row[3]} precision={row[4]}"
        )
        previous_offsets = actual

    return code


def verify_odd_tail_geometry() -> None:
    base = ("1010000", "0001001")
    code = concatenate(base, atomic_code(3))
    length = len(code[0])
    weight = code[0].count("1")
    modulus_three = 3**weight
    signature = (pow(2**length, -1, modulus_three) * affine_constant(code[0])) % modulus_three

    tail = 1
    while not (
        2**tail - 1 > 3**weight
        and 3 ** (weight + tail) > 2 ** (length + tail)
    ):
        tail += 1
    assert tail == 37

    common_output = crt_pair(signature, modulus_three, -1 % 2**tail, 2**tail)
    roots = []
    for word in code:
        numerator = 2**length * common_output - affine_constant(word)
        assert numerator % modulus_three == 0
        root = numerator // modulus_three
        observed_word, reached = trace_word(root, length)
        assert observed_word == word
        assert reached == common_output
        tail_word, _ = trace_word(common_output, tail)
        assert tail_word == "1" * tail
        roots.append(root)

    root_offsets = {root - roots[0] for root in roots}
    assert root_offsets == set(offsets(code))
    assert 3 ** (weight + tail) > 2 ** (length + tail)
    ratio_num = 3 ** (weight + tail)
    ratio_den = 2 ** (length + tail)
    assert ratio_num <= 3 * ratio_den // 2 + 1
    print(
        f"verified finite odd-tail promotion: prefix_length={length} "
        f"tail={tail} branches={len(code)}"
    )


def main() -> None:
    verify_atomic_codes()
    final_code = verify_tensor_hierarchy()
    assert len(final_code) == 16
    verify_odd_tail_geometry()
    print("all offset-tensor checks passed")


if __name__ == "__main__":
    main()
