#!/usr/bin/env python3
"""Exact checks for the first collision-rewrite research packet.

The script uses only Python's standard library and ordinary integer arithmetic.
It verifies the proposed parity-affine formula, three concrete supercritical
collision bundles, the 64->81 carry cycle, and the finite-horizon stack
amplifier. It also enumerates consecutive collision bundles through L=17.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


def T(n: int) -> int:
    """Shortcut Collatz map on nonnegative integers."""
    if n < 0:
        raise ValueError("this experiment is restricted to n >= 0")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trace(n: int, length: int) -> tuple[str, int]:
    """Return the chronological parity word and T**length(n)."""
    bits: list[str] = []
    x = n
    for _ in range(length):
        bits.append(str(x & 1))
        x = T(x)
    return "".join(bits), x


def affine_constant(word: str) -> int:
    """Constant B(w) in T^L(n) = (3^a n + B(w))/2^L."""
    ones_seen = 0
    total_ones = word.count("1")
    value = 0
    for j, bit in enumerate(word):
        if bit == "1":
            ones_seen += 1
            value += (1 << j) * (3 ** (total_ones - ones_seen))
        elif bit != "0":
            raise ValueError(f"invalid parity symbol {bit!r}")
    return value


@dataclass(frozen=True)
class CollisionBundle:
    length: int
    start_residue: int
    width: int
    odd_steps: int
    common_output: int
    words: tuple[str, ...]

    @property
    def input_radix(self) -> int:
        return 1 << self.length

    @property
    def output_radix(self) -> int:
        return 3 ** self.odd_steps

    @property
    def supercritical(self) -> bool:
        return self.output_radix > self.input_radix


def collision_bundles(length: int) -> list[CollisionBundle]:
    """Enumerate maximal runs of consecutive residues with one affine image."""
    modulus = 1 << length
    data: list[tuple[int, int, str]] = []
    for residue in range(modulus):
        word, output = trace(residue, length)
        data.append((word.count("1"), output, word))

    bundles: list[CollisionBundle] = []
    left = 0
    while left < modulus:
        odd_steps, output, _ = data[left]
        right = left + 1
        while right < modulus and data[right][:2] == (odd_steps, output):
            right += 1
        if right - left >= 2:
            bundles.append(
                CollisionBundle(
                    length=length,
                    start_residue=left,
                    width=right - left,
                    odd_steps=odd_steps,
                    common_output=output,
                    words=tuple(data[k][2] for k in range(left, right)),
                )
            )
        left = right
    return bundles


def verify_bundle(bundle: CollisionBundle, q_values: Iterable[int]) -> None:
    """Verify a bundle symbolically and on selected lifted residue classes."""
    L = bundle.length
    M = 1 << L
    N = 3 ** bundle.odd_steps
    r = bundle.start_residue
    s = bundle.common_output

    assert bundle.supercritical
    assert len(bundle.words) == bundle.width

    for j, expected_word in enumerate(bundle.words):
        word, output = trace(r + j, L)
        assert word == expected_word
        assert output == s
        assert word.count("1") == bundle.odd_steps
        B = affine_constant(word)
        assert N * (r + j) + B == M * s

        for q in q_values:
            lifted_word, lifted_output = trace(M * q + r + j, L)
            assert lifted_word == expected_word
            assert lifted_output == N * q + s

    # Check the affine conjugacy from T-0001.
    c = N - M
    d = M * s - N * r
    h = s - r
    for q in q_values:
        A = c * q + h
        for j in range(bundle.width):
            n = M * q + r + j
            assert c * n + d == M * A + c * j
        n_out = N * q + s
        assert c * n_out + d == N * A


def normalize_carry(
    carry: int, digits_low_first: Sequence[int], M: int, N: int
) -> tuple[list[int], int]:
    """Normalize R_c L_d... using N*d+c = M*q+r."""
    emitted: list[int] = []
    c = carry
    for digit in digits_low_first:
        q, r = divmod(N * digit + c, M)
        assert 0 <= r < M
        assert 0 <= q < N
        emitted.append(r)
        c = q
    return emitted, c


def value_with_tail(digits_low_first: Sequence[int], tail: int, base: int) -> int:
    """Evaluate low-order-first digits followed by an integer high-order tail."""
    value = tail
    for digit in reversed(digits_low_first):
        if not 0 <= digit < base:
            raise ValueError("digit outside radix")
        value = base * value + digit
    return value


def H(A: int, M: int, N: int, alphabet_size: int) -> int:
    """Partial radix map H(M*B+j)=N*B+j for 0 <= j < alphabet_size."""
    B, j = divmod(A, M)
    if j >= alphabet_size:
        raise ValueError(f"state has inadmissible least digit {j}")
    return N * B + j


def verify_pair_stack_amplifier() -> None:
    M, N, alphabet_size = 64, 81, 2
    W = [15, 29, 43, 57, 7, 22, 36, 50, 0]

    emitted, final_carry = normalize_carry(1, W, M, N)
    assert emitted == [0] * 9
    assert final_carry == 1

    block_value = value_with_tail(W, 0, M)
    assert 81 * block_value + 1 == 64**9
    assert block_value == (64**9 - 1) // 81

    for m in range(0, 5):
        for x in (0, 1, 2, 17, 12345):
            digits = [1] + W * m
            S = value_with_tail(digits, x, M)
            formula = 64 ** (9 * m + 1) * x + (64 ** (9 * m + 1) + 17) // 81
            assert S == formula

            state = S
            for _ in range(9 * m + 1):
                state = H(state, M, N, alphabet_size)
            assert state == 81 ** (9 * m) * (81 * x + 1)


def main() -> None:
    known = [
        CollisionBundle(
            length=6,
            start_residue=14,
            width=2,
            odd_steps=4,
            common_output=20,
            words=("011101", "111100"),
        ),
        CollisionBundle(
            length=9,
            start_residue=124,
            width=3,
            odd_steps=6,
            common_output=182,
            words=("001111101", "100111101", "011111100"),
        ),
        CollisionBundle(
            length=17,
            start_residue=9090,
            width=6,
            odd_steps=11,
            common_output=12302,
            words=(
                "01010100111111011",
                "11000100111111011",
                "00101011111111001",
                "10001011111111001",
                "01100011111111001",
                "11101000011111011",
            ),
        ),
    ]

    for bundle in known:
        verify_bundle(bundle, q_values=(0, 1, 2, 7, 101))
        print(
            "verified bundle:",
            f"L={bundle.length}",
            f"r={bundle.start_residue}",
            f"width={bundle.width}",
            f"a={bundle.odd_steps}",
            f"M={bundle.input_radix}",
            f"N={bundle.output_radix}",
            f"s={bundle.common_output}",
        )

    verify_pair_stack_amplifier()
    print("verified 64->81 nine-column carry cycle and stack amplifier")

    print("\nmaximal supercritical consecutive bundles through L=17:")
    for L in range(1, 18):
        bundles = [b for b in collision_bundles(L) if b.supercritical]
        if not bundles:
            print(f"L={L:2d}: none")
            continue
        best = min(
            (b for b in bundles if b.width == max(x.width for x in bundles)),
            key=lambda b: b.start_residue,
        )
        print(
            f"L={L:2d}: count={len(bundles):5d} "
            f"max_width={best.width} first_r={best.start_residue} "
            f"a={best.odd_steps} s={best.common_output}"
        )


if __name__ == "__main__":
    main()
