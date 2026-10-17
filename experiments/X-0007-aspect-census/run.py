#!/usr/bin/env python3
"""Exact normalized-aspect census through depth 22 and checks for O-0007."""

from __future__ import annotations

from array import array
from dataclasses import dataclass
from fractions import Fraction


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trace(n: int, length: int) -> tuple[str, int]:
    bits: list[str] = []
    x = n
    for _ in range(length):
        bits.append(str(x & 1))
        x = T(x)
    return "".join(bits), x


def next_tables(
    odd_counts: array, outputs: array, length: int
) -> tuple[array, array]:
    previous_modulus = 1 << (length - 1)
    new_odd_counts = array("B", [0]) * (2 * previous_modulus)
    new_outputs = array("Q", [0]) * (2 * previous_modulus)
    powers_of_three = [3**k for k in range(length + 1)]

    for k in range(previous_modulus):
        new_odd_counts[2 * k] = odd_counts[k]
        new_outputs[2 * k] = outputs[k]

        quotient, residue = divmod(3 * k + 2, previous_modulus)
        remaining_odds = odd_counts[residue]
        new_odd_counts[2 * k + 1] = 1 + remaining_odds
        new_outputs[2 * k + 1] = (
            powers_of_three[remaining_odds] * quotient + outputs[residue]
        )

    return new_odd_counts, new_outputs


@dataclass(frozen=True)
class AspectFiber:
    length: int
    odd_steps: int
    common_output: int
    members: tuple[int, ...]

    @property
    def M(self) -> int:
        return 1 << self.length

    @property
    def N(self) -> int:
        return 3**self.odd_steps

    @property
    def gap(self) -> int:
        return self.N - self.M

    @property
    def width(self) -> int:
        return self.members[-1] - self.members[0]

    @property
    def aspect(self) -> Fraction:
        return Fraction(self.width, self.gap)


def best_aspect_fiber(
    length: int, odd_counts: array, outputs: array
) -> AspectFiber | None:
    modulus = 1 << length
    groups: dict[tuple[int, int], list[int]] = {}

    for residue, (odd_steps, common_output) in enumerate(zip(odd_counts, outputs)):
        if 3**odd_steps <= modulus:
            continue
        groups.setdefault((int(odd_steps), int(common_output)), []).append(residue)

    best: AspectFiber | None = None
    for (odd_steps, common_output), members in groups.items():
        if len(members) < 2:
            continue
        candidate = AspectFiber(
            length,
            odd_steps,
            common_output,
            tuple(members),
        )
        if best is None:
            best = candidate
            continue
        left = candidate.width * best.gap
        right = best.width * candidate.gap
        if left > right:
            best = candidate
        elif left == right:
            # Prefer the target with smallest magnitude v=N-s; this selects
            # cycle phases such as O-0007 when the geometry ties.
            candidate_v = candidate.N - candidate.common_output
            best_v = best.N - best.common_output
            if candidate_v < best_v:
                best = candidate
    return best


def verify_o0007(odd_counts: array, outputs: array) -> None:
    length = 11
    M = 1 << length
    N = 3**7
    r = 1912
    s = 2051
    digits = (0, 2, 4, 5)
    expected_words = (
        "00011110111",
        "01001110111",
        "00111110011",
        "10011110011",
    )

    for digit, expected_word in zip(digits, expected_words):
        residue = r + digit
        assert odd_counts[residue] == 7
        assert outputs[residue] == s

        word, output = trace(residue, length)
        assert word == expected_word
        assert output == s

        template = M - residue
        negative_word, negative_output = trace(-template, length)
        assert negative_word == expected_word
        assert negative_output == -136

        for q in (0, 1, 2, 7, 101):
            assert trace(M * q - template, length)[1] == N * q - 136

    cycle = []
    x = -61
    for _ in range(11):
        cycle.append(x)
        x = T(x)
    assert cycle == [-61, -91, -136, -68, -34, -17, -25, -37, -55, -82, -41]
    assert x == -61

    assert Fraction(max(digits) - min(digits), N - M) == Fraction(5, 139)


def main() -> None:
    odd_counts = array("B", [0])
    outputs = array("Q", [0])
    depth_11_tables: tuple[array, array] | None = None

    for length in range(1, 23):
        odd_counts, outputs = next_tables(odd_counts, outputs, length)
        if length == 11:
            depth_11_tables = (odd_counts[:], outputs[:])

        best = best_aspect_fiber(length, odd_counts, outputs)
        if best is None:
            continue
        print(
            f"L={length:2d} a={best.odd_steps:2d} size={len(best.members):2d} "
            f"residues=[{best.members[0]},{best.members[-1]}] "
            f"width={best.width} gap={best.gap} "
            f"aspect={float(best.aspect):.12g} s={best.common_output}"
        )

    assert depth_11_tables is not None
    verify_o0007(*depth_11_tables)
    print("verified O-0007 and the negative 11-cycle")
    print("all aspect-census checks passed")


if __name__ == "__main__":
    main()
