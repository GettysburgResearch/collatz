#!/usr/bin/env python3
"""Exact checks for T-0008, T-0009, T-0010, and L-0011."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trace(n: int, length: int) -> tuple[tuple[int, ...], int]:
    bits: list[int] = []
    x = n
    for _ in range(length):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits), x


def verify_chart(
    name: str,
    length: int,
    odd_steps: int,
    first_residue: int,
    common_output: int,
    offsets: list[int],
) -> tuple[str, int, int, int, int, int, Fraction, int, int]:
    M = 1 << length
    N = 3**odd_steps
    gap = N - M
    v = N - common_output
    residues = [first_residue + d for d in offsets]
    templates = [M - r for r in residues]
    digits = [v - u for u in templates]

    for residue, template in zip(residues, templates):
        bits, output = trace(-template, length)
        assert sum(bits) == odd_steps
        assert output == -v

        for quotient in (0, 1, 2, 7):
            assert trace(M * quotient - template, length)[1] == N * quotient - v

    width = max(residues) - min(residues)
    assert max(digits) - min(digits) == width
    aspect = Fraction(width, gap)
    return (
        name,
        len(offsets),
        M,
        N,
        gap,
        width,
        aspect,
        min(digits),
        max(digits),
    )


def verify_address(
    q0: int,
    M: int,
    N: int,
    alphabet: set[int],
    steps: int,
) -> tuple[list[int], list[int]]:
    q = q0
    digits: list[int] = []
    quotients = [q]

    for _ in range(steps):
        digit = (N * q) % M
        assert digit in alphabet
        q = (N * q - digit) // M
        digits.append(digit)
        quotients.append(q)

    left = N**steps * quotients[0] - M**steps * quotients[-1]
    right = sum(
        digit * N ** (steps - 1 - t) * M**t
        for t, digit in enumerate(digits)
    )
    assert left == right
    return quotients, digits


def affine_constant(word: tuple[int, ...]) -> int:
    total = sum(word)
    seen = 0
    value = 0
    for j, bit in enumerate(word):
        if bit:
            seen += 1
            value += (1 << j) * 3 ** (total - seen)
    return value


def prefix_family(b: int) -> list[tuple[int, ...]]:
    words: list[tuple[int, ...]] = []
    for x in product((0, 1), repeat=b):
        missing = b - sum(x)
        words.append(tuple(x) + (1,) * missing + (0,) * (b - missing))
    return words


def correction_code(b: int) -> list[tuple[int, ...]]:
    p = b + 1
    modulus = 3**p
    period = 2 * 3 ** (p - 1)
    target = 1
    logarithm = {pow(2, j, modulus): j for j in range(period)}

    words: list[tuple[int, ...]] = []
    for prefix in prefix_family(b):
        right = (
            (target - 3 * affine_constant(prefix))
            * pow(pow(2, len(prefix), modulus), -1, modulus)
        ) % modulus
        j = logarithm[right]
        suffix = tuple(1 if t == j else 0 for t in range(period))
        words.append(prefix + suffix)
    return words


def crt(a: int, m: int, b: int, n: int) -> int:
    return (a + m * (((b - a) * pow(m, -1, n)) % n)) % (m * n)


def dyadic_tail_aspect(
    b: int,
) -> tuple[int, int, int, int, int, int, Fraction]:
    words = correction_code(b)
    length = len(words[0])
    odd_steps = b + 1
    modulus = 3**odd_steps
    signature = (
        pow(2, -length, modulus) * affine_constant(words[0])
    ) % modulus

    tail = 1
    while 3 ** (odd_steps + tail) <= 2 ** (length + tail):
        tail += 1

    root = crt(signature, modulus, -1 % (1 << tail), 1 << tail)
    root += modulus * (1 << tail)
    starts = [
        ((1 << length) * root - affine_constant(word)) // modulus
        for word in words
    ]

    width = max(starts) - min(starts)
    M = 1 << (length + tail)
    N = 3 ** (odd_steps + tail)
    gap = N - M
    aspect = Fraction(width, gap)

    # Exact identity from L-0011.
    assert aspect == Fraction(width, 1 << length) / (
        (1 << tail) * Fraction(gap, M)
    )
    return b, len(words), length, tail, width, gap, aspect


def main() -> None:
    rows = [
        verify_chart("O-0001", 6, 4, 14, 20, [0, 1]),
        verify_chart("O-0002", 9, 6, 124, 182, [0, 1, 2]),
        verify_chart("O-0003", 17, 11, 9090, 12302, list(range(6))),
        verify_chart(
            "O-0004",
            22,
            14,
            621248,
            708587,
            [0, 16, 20, 21, 32, 34, 35, 40, 42, 49, 68, 69, 70, 78, 79, 92, 93, 94],
        ),
    ]

    offsets_path = (
        Path(__file__).resolve().parents[1]
        / "X-0003-signature-tail-fibers"
        / "results"
        / "m8-offsets.txt"
    )
    o5_offsets = [int(x) for x in offsets_path.read_text().split()]
    assert len(o5_offsets) == 339
    rows.append(
        verify_chart(
            "O-0005",
            44,
            28,
            8_952_950_628_352,
            11_642_373_114_938,
            o5_offsets,
        )
    )

    for name, size, _, _, gap, width, aspect, low, high in rows:
        print(
            f"{name} branches={size} width={width} gap={gap} "
            f"aspect={float(aspect):.12g} A=[{low},{high}]"
        )

    quotients, digits = verify_address(45_836, 64, 81, {11, 12}, 3)
    assert quotients == [45_836, 58_011, 73_420, 92_922]
    assert digits == [12, 11, 12]
    print("verified O-0001 rational-base address:", quotients, digits)

    # The complete one-step return table around -1 illustrates T-0009's
    # forced contracting branch.
    assert trace(-1, 1)[1] == -1
    assert trace(-2, 1)[1] == -1
    for q in range(2, 50):
        if q % 2 == 0:
            q_next = 3 * q // 2
        else:
            q_next = (q + 1) // 2
        assert trace(q - 1, 1)[1] == q_next - 1
    print(
        "verified renewal obstruction witness: "
        "even q uses -1 odd return; odd q uses -2 even return"
    )

    for b in range(1, 6):
        bb, size, length, tail, width, _, aspect = dyadic_tail_aspect(b)
        print(
            f"b={bb} branches={size} core={length} tail={tail} "
            f"width={width} aspect={float(aspect):.12g}"
        )

    print("all negative-shadow and aspect-ratio checks passed")


if __name__ == "__main__":
    main()
