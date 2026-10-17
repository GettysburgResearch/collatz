#!/usr/bin/env python3
"""Exact checks for parity-signature collision codes and odd-tail amplification.

The experiment uses only Python's standard library and ordinary integers.  It
constructs, for 1 <= m <= 8, the largest equal-signature class among all
length-3m parity words of weight m, appends the shortest all-odd tail that
makes the resulting block supercritical, and verifies the resulting exact
Collatz collision fiber.

The construction is theorem-driven: the search only selects a particularly
large signature class.  T-0005 proves a class of at least
ceil(binomial(3m,m)/3^m) exists for every m, independently of this program.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from math import ceil, comb
from typing import Iterable, Sequence


def T(n: int) -> int:
    if n < 0:
        raise ValueError("T is restricted to nonnegative integers here")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trace(n: int, length: int) -> tuple[str, int]:
    bits: list[str] = []
    x = n
    for _ in range(length):
        bits.append(str(x & 1))
        x = T(x)
    return "".join(bits), x


def affine_constant_from_positions(
    length: int, positions: Sequence[int]
) -> int:
    """B(w) for a word whose one-positions are listed increasingly."""
    if any(not 0 <= position < length for position in positions):
        raise ValueError("one-position outside the word")
    if tuple(positions) != tuple(sorted(set(positions))):
        raise ValueError("positions must be distinct and increasing")

    weight = len(positions)
    return sum(
        (1 << position) * (3 ** (weight - index - 1))
        for index, position in enumerate(positions)
    )



def affine_constant(word: str) -> int:
    remaining = word.count("1")
    value = 0
    for index, bit in enumerate(word):
        if bit == "1":
            remaining -= 1
            value += (1 << index) * (3**remaining)
        elif bit != "0":
            raise ValueError(f"invalid parity symbol {bit!r}")
    return value



def verify_inverse_signature_small(max_length: int = 8) -> None:
    """Exhaustively check L-0005 on every short parity word."""
    from itertools import product

    for length in range(1, max_length + 1):
        modulus = 1 << length
        for bits in product("01", repeat=length):
            word = "".join(bits)
            weight = word.count("1")
            constant = affine_constant(word)
            assert 0 <= constant < modulus * (3**weight)

            residue = (-constant * pow(3**weight, -1, modulus)) % modulus
            traced_word, _ = trace(residue, length)
            assert traced_word == word

            if weight == 0:
                continue
            odd_multiplier = 3**weight
            signature = (constant * pow(modulus, -1, odd_multiplier)) % odd_multiplier
            for lift in range(4):
                output = signature + odd_multiplier * lift
                numerator = modulus * output - constant
                assert numerator % odd_multiplier == 0
                start = numerator // odd_multiplier
                if start >= 0:
                    traced_word, traced_output = trace(start, length)
                    assert traced_word == word
                    assert traced_output == output


def verify_collision_code_composition() -> None:
    """Check L-0006's concatenation and precision-surplus example."""
    prefix_code = ("100", "001")
    suffix_code = ("100100", "010001")

    assert {word.count("1") for word in prefix_code} == {1}
    assert {affine_constant(word) % 3 for word in prefix_code} == {1}

    assert {word.count("1") for word in suffix_code} == {2}
    assert {affine_constant(word) % 27 for word in suffix_code} == {11}

    concatenated = tuple(left + right for left in prefix_code for right in suffix_code)
    assert len(concatenated) == 4
    assert {word.count("1") for word in concatenated} == {3}
    assert {affine_constant(word) % 27 for word in concatenated} == {16}

    for left in prefix_code:
        for right in suffix_code:
            direct = affine_constant(left + right)
            composed = (3 ** right.count("1")) * affine_constant(left) + (
                2 ** len(left)
            ) * affine_constant(right)
            assert direct == composed


def word_from_positions(length: int, positions: Sequence[int]) -> str:
    ones = set(positions)
    return "".join("1" if index in ones else "0" for index in range(length))


def crt_coprime(a: int, modulus_a: int, b: int, modulus_b: int) -> int:
    """Least nonnegative solution to two coprime congruences."""
    if modulus_a <= 0 or modulus_b <= 0:
        raise ValueError("moduli must be positive")
    return (
        a
        + modulus_a
        * (((b - a) * pow(modulus_a, -1, modulus_b)) % modulus_b)
    ) % (modulus_a * modulus_b)


def shortest_supercritical_tail(m: int) -> int:
    """Least k with 3^(m+k) > 2^(3m+k)."""
    if m < 1:
        raise ValueError("m must be positive")
    k = 0
    while 3 ** (m + k) <= 2 ** (3 * m + k):
        k += 1
    return k


@dataclass(frozen=True)
class SignatureFiber:
    m: int
    tail_length: int
    signature: int
    core_words: int
    theorem_lower_bound: int
    members: tuple[tuple[int, tuple[int, ...]], ...]
    root: int
    common_output: int
    input_radix: int
    output_radix: int

    @property
    def total_length(self) -> int:
        return 3 * self.m + self.tail_length

    @property
    def total_odd_steps(self) -> int:
        return self.m + self.tail_length

    @property
    def residues(self) -> tuple[int, ...]:
        return tuple(sorted(residue for residue, _ in self.members))

    @property
    def base_residue(self) -> int:
        return self.residues[0]

    @property
    def offsets(self) -> tuple[int, ...]:
        base = self.base_residue
        return tuple(residue - base for residue in self.residues)

    @property
    def diameter(self) -> int:
        return self.residues[-1] - self.residues[0]


def largest_signature_fiber(m: int) -> SignatureFiber:
    core_length = 3 * m
    core_modulus = 1 << core_length
    core_odd_multiplier = 3**m
    inverse_core_modulus = pow(core_modulus, -1, core_odd_multiplier)

    counts: Counter[int] = Counter()
    for positions in combinations(range(core_length), m):
        constant = affine_constant_from_positions(core_length, positions)
        signature = (constant * inverse_core_modulus) % core_odd_multiplier
        counts[signature] += 1

    # Deterministic tie break: smallest signature.  A second pass retains only
    # the selected class, keeping memory independent of binomial(3m,m).
    signature = min(
        candidate
        for candidate, count in counts.items()
        if count == max(counts.values())
    )
    selected: list[tuple[int, tuple[int, ...]]] = []
    for positions in combinations(range(core_length), m):
        constant = affine_constant_from_positions(core_length, positions)
        candidate = (constant * inverse_core_modulus) % core_odd_multiplier
        if candidate == signature:
            selected.append((constant, positions))

    tail_length = shortest_supercritical_tail(m)
    tail_modulus = 1 << tail_length
    root = crt_coprime(
        signature,
        core_odd_multiplier,
        tail_modulus - 1,
        tail_modulus,
    )

    total_length = core_length + tail_length
    total_odd_steps = m + tail_length
    input_radix = 1 << total_length
    output_radix = 3**total_odd_steps
    common_output = 3**tail_length * ((root + 1) // tail_modulus) - 1

    members: list[tuple[int, tuple[int, ...]]] = []
    for constant, positions in selected:
        numerator = core_modulus * root - constant
        assert numerator % core_odd_multiplier == 0
        residue = numerator // core_odd_multiplier
        assert 0 < residue < input_radix
        members.append((residue, positions))

    return SignatureFiber(
        m=m,
        tail_length=tail_length,
        signature=signature,
        core_words=comb(3 * m, m),
        theorem_lower_bound=ceil(comb(3 * m, m) / (3**m)),
        members=tuple(sorted(members)),
        root=root,
        common_output=common_output,
        input_radix=input_radix,
        output_radix=output_radix,
    )


def verify_fiber(fiber: SignatureFiber, q_values: Iterable[int]) -> None:
    m = fiber.m
    core_length = 3 * m
    tail_length = fiber.tail_length
    total_length = fiber.total_length
    expected_weight = fiber.total_odd_steps
    core_modulus = 1 << core_length
    core_odd_multiplier = 3**m

    assert fiber.output_radix > fiber.input_radix
    assert fiber.output_radix <= 3 * fiber.input_radix // 2 + 1
    assert fiber.tail_length >= 2 * m + 1
    assert (1 << fiber.tail_length) - 1 > 3**m
    assert fiber.root % core_odd_multiplier == fiber.signature
    assert fiber.root % (1 << tail_length) == (1 << tail_length) - 1
    assert len(fiber.members) >= fiber.theorem_lower_bound

    seen_words: set[str] = set()
    for residue, positions in fiber.members:
        core_word = word_from_positions(core_length, positions)
        total_word = core_word + "1" * tail_length
        assert total_word.count("1") == expected_weight
        assert total_word not in seen_words
        seen_words.add(total_word)

        constant = affine_constant_from_positions(core_length, positions)
        assert (
            constant * pow(core_modulus, -1, core_odd_multiplier)
        ) % core_odd_multiplier == fiber.signature

        core_trace, core_output = trace(residue, core_length)
        assert core_trace == core_word
        assert core_output == fiber.root

        full_trace, full_output = trace(residue, total_length)
        assert full_trace == total_word
        assert full_output == fiber.common_output

        for q in q_values:
            lifted_word, lifted_output = trace(
                fiber.input_radix * q + residue, total_length
            )
            assert lifted_word == total_word
            assert (
                lifted_output
                == fiber.output_radix * q + fiber.common_output
            )

    offsets_text = "\n".join(str(x) for x in fiber.offsets) + "\n"
    assert len(offsets_text) > 0


def consecutive_run_length(values: Sequence[int]) -> int:
    if not values:
        return 0
    longest = current = 1
    for left, right in zip(values, values[1:]):
        if right == left + 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    return longest


def centered_difference_radius(values: Sequence[int]) -> int:
    differences = {right - left for left in values for right in values}
    radius = 0
    while radius + 1 in differences and -(radius + 1) in differences:
        radius += 1
    return radius


def summarize(fibers: Sequence[SignatureFiber]) -> str:
    lines = [
        "verified L-0005 inverse signatures exhaustively through length 8",
        "verified L-0006 collision-code composition calculus",
        "verified T-0005 signature-pigeonhole and odd-tail construction",
        "",
        "largest equal-signature classes among weight-m words of length 3m:",
    ]
    for fiber in fibers:
        lines.append(
            "m={m:2d} core_words={words:7d} guaranteed={guaranteed:3d} "
            "largest={largest:3d} signature={signature:5d} tail={tail:2d} "
            "L={length:2d} a={odd:2d} diameter={diameter:5d}".format(
                m=fiber.m,
                words=fiber.core_words,
                guaranteed=fiber.theorem_lower_bound,
                largest=len(fiber.members),
                signature=fiber.signature,
                tail=fiber.tail_length,
                length=fiber.total_length,
                odd=fiber.total_odd_steps,
                diameter=fiber.diameter,
            )
        )

    explicit = fibers[-1]
    offsets_text = "\n".join(str(x) for x in explicit.offsets) + "\n"
    offset_digest = sha256(offsets_text.encode("utf-8")).hexdigest()
    residues = explicit.residues
    offsets = explicit.offsets
    projections_mod_16 = len({value % 16 for value in offsets})
    difference_radius = centered_difference_radius(offsets)
    run_length = consecutive_run_length(residues)

    lines.extend(
        [
            "",
            "verified O-0005 explicit 339-branch chart:",
            f"M=2^44={explicit.input_radix}",
            f"N=3^28={explicit.output_radix}",
            f"root={explicit.root}",
            f"base_residue={explicit.base_residue}",
            f"common_output={explicit.common_output}",
            f"fiber_size={len(explicit.members)}",
            f"offset_diameter={explicit.diameter}",
            f"longest_consecutive_residue_run={run_length}",
            f"offset_residue_classes_mod_16={projections_mod_16}",
            f"centered_difference_radius={difference_radius}",
            f"offset_sha256={offset_digest}",
            "",
            "first 20 offsets:",
            " ".join(str(value) for value in offsets[:20]),
            "last 20 offsets:",
            " ".join(str(value) for value in offsets[-20:]),
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    verify_inverse_signature_small()
    verify_collision_code_composition()
    fibers = [largest_signature_fiber(m) for m in range(1, 9)]
    for fiber in fibers:
        verify_fiber(fiber, q_values=(0, 1, 2, 7))

    explicit = fibers[-1]
    assert explicit.tail_length == 20
    assert explicit.total_length == 44
    assert explicit.total_odd_steps == 28
    assert explicit.signature == 2_906
    assert explicit.root == 3_501_195_263
    assert explicit.input_radix == 17_592_186_044_416
    assert explicit.output_radix == 22_876_792_454_961
    assert explicit.base_residue == 8_952_950_628_352
    assert explicit.common_output == 11_642_373_114_938
    assert len(explicit.members) == 339
    assert explicit.diameter == 17_207
    assert consecutive_run_length(explicit.residues) == 7
    assert len({value % 16 for value in explicit.offsets}) == 16
    assert centered_difference_radius(explicit.offsets) == 934

    checked_offsets = Path(__file__).with_name("results") / "m8-offsets.txt"
    if checked_offsets.exists():
        expected_text = "\n".join(str(value) for value in explicit.offsets) + "\n"
        assert checked_offsets.read_text(encoding="utf-8") == expected_text

    print(summarize(fibers), end="")


if __name__ == "__main__":
    main()
