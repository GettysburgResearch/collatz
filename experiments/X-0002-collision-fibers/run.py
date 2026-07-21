#!/usr/bin/env python3
"""Exact checks for arbitrary collision fibers and induced-map structure.

The script uses only Python's standard library and ordinary integer arithmetic.
It:

* builds every affine residue table through depth 22 using L-0003;
* enumerates all nontrivial supercritical collision fibers;
* verifies the eighteen-branch depth-22 chart O-0004;
* checks the arbitrary-fiber conjugacy T-0002;
* reconstructs the universal zero-output carry pump L-0004;
* checks the short 512 -> 729 admissible-output carry cycle; and
* verifies the run-length skeleton T-0004 on exact finite trajectories.
"""

from __future__ import annotations

from array import array
from dataclasses import dataclass
from typing import Iterable, Sequence


def T(n: int) -> int:
    """Shortcut Collatz map on nonnegative integers."""
    if n < 0:
        raise ValueError("this experiment is restricted to n >= 0")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trace(n: int, length: int) -> tuple[str, int]:
    bits: list[str] = []
    x = n
    for _ in range(length):
        bits.append(str(x & 1))
        x = T(x)
    return "".join(bits), x


def affine_constant(word: str) -> int:
    """B(w) in T^L(n)=(3^a*n+B(w))/2^L."""
    remaining_ones = word.count("1")
    value = 0
    for index, bit in enumerate(word):
        if bit == "1":
            remaining_ones -= 1
            value += (1 << index) * (3**remaining_ones)
        elif bit != "0":
            raise ValueError(f"invalid parity symbol {bit!r}")
    return value


@dataclass(frozen=True)
class FiberSummary:
    length: int
    nontrivial_count: int
    max_size: int
    odd_steps: int | None
    common_output: int | None
    members: tuple[int, ...]


def next_affine_tables(
    odd_counts: array, outputs: array, length: int
) -> tuple[array, array]:
    """Apply the exact L-0003 recursion from depth length-1 to length."""
    if length < 1:
        raise ValueError("length must be positive")
    previous_modulus = 1 << (length - 1)
    if len(odd_counts) != previous_modulus or len(outputs) != previous_modulus:
        raise ValueError("table size does not match requested recursion depth")

    new_odd_counts = array("B", [0]) * (2 * previous_modulus)
    new_outputs = array("Q", [0]) * (2 * previous_modulus)
    powers_of_three = [3**k for k in range(length + 1)]

    for k in range(previous_modulus):
        # Even residue 2k.
        new_odd_counts[2 * k] = odd_counts[k]
        new_outputs[2 * k] = outputs[k]

        # Odd residue 2k+1 first maps to 3k+2.
        quotient, residue = divmod(3 * k + 2, previous_modulus)
        remaining_odds = odd_counts[residue]
        new_odd_counts[2 * k + 1] = 1 + remaining_odds
        new_outputs[2 * k + 1] = (
            powers_of_three[remaining_odds] * quotient + outputs[residue]
        )

    return new_odd_counts, new_outputs


def supercritical_fiber_summary(
    length: int, odd_counts: Sequence[int], outputs: Sequence[int]
) -> FiberSummary:
    modulus = 1 << length
    groups: dict[tuple[int, int], list[int]] = {}

    for residue, (odd_steps, common_output) in enumerate(zip(odd_counts, outputs)):
        if 3**odd_steps <= modulus:
            continue
        groups.setdefault((int(odd_steps), int(common_output)), []).append(residue)

    nontrivial = [
        (key, members) for key, members in groups.items() if len(members) >= 2
    ]
    if not nontrivial:
        return FiberSummary(length, 0, 0, None, None, ())

    max_size = max(len(members) for _, members in nontrivial)
    key, members = min(
        ((key, members) for key, members in nontrivial if len(members) == max_size),
        key=lambda item: item[1],
    )
    odd_steps, common_output = key
    return FiberSummary(
        length=length,
        nontrivial_count=len(nontrivial),
        max_size=max_size,
        odd_steps=odd_steps,
        common_output=common_output,
        members=tuple(members),
    )


def build_and_summarize(max_length: int) -> tuple[list[FiberSummary], array, array]:
    odd_counts = array("B", [0])
    outputs = array("Q", [0])
    summaries: list[FiberSummary] = []

    for length in range(1, max_length + 1):
        odd_counts, outputs = next_affine_tables(odd_counts, outputs, length)
        summaries.append(
            supercritical_fiber_summary(length, odd_counts, outputs)
        )

    return summaries, odd_counts, outputs


def verify_recursion_against_direct_trace(max_length: int = 12) -> None:
    odd_counts = array("B", [0])
    outputs = array("Q", [0])

    for length in range(1, max_length + 1):
        odd_counts, outputs = next_affine_tables(odd_counts, outputs, length)
        for residue in range(1 << length):
            word, direct_output = trace(residue, length)
            assert odd_counts[residue] == word.count("1")
            assert outputs[residue] == direct_output


def verify_sparse_eighteen_fiber(
    odd_counts: Sequence[int], outputs: Sequence[int]
) -> None:
    length = 22
    M = 1 << length
    N = 3**14
    r = 621_248
    s = 708_587
    digits = (
        0,
        16,
        20,
        21,
        32,
        34,
        35,
        40,
        42,
        49,
        68,
        69,
        70,
        78,
        79,
        92,
        93,
        94,
    )

    c = N - M
    kappa = M * s - N * r
    h = s - r
    assert (M, N, c, kappa, h) == (
        4_194_304,
        4_782_969,
        588_665,
        619_363_136,
        87_339,
    )

    for digit in digits:
        residue = r + digit
        assert odd_counts[residue] == 14
        assert outputs[residue] == s

        word, direct_output = trace(residue, length)
        assert word.count("1") == 14
        assert direct_output == s
        B = affine_constant(word)
        assert N * residue + B == M * s

        for q in (0, 1, 2, 7, 101):
            lifted_word, lifted_output = trace(M * q + residue, length)
            assert lifted_word == word
            assert lifted_output == N * q + s

            A = c * q + h
            phi_input = c * (M * q + residue) + kappa
            phi_output = c * (N * q + s) + kappa
            assert phi_input == M * A + c * digit
            assert phi_output == N * A

        # Verify one actual induced step in the invariant lifting class.
        quotient = ((h - digit) * pow(M, -1, c)) % c + c
        A = M * quotient + digit
        assert A >= M and A % c == h
        A_next = N * quotient + digit
        assert A_next % c == h
        n = (N * A - kappa) // c
        n_next = (N * A_next - kappa) // c
        assert n > 0
        assert trace(n, length)[1] == n_next


def normalize_carry(
    carry: int, digits_low_first: Sequence[int], M: int, N: int
) -> tuple[list[int], int]:
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
    value = tail
    for digit in reversed(digits_low_first):
        if not 0 <= digit < base:
            raise ValueError("digit outside radix")
        value = base * value + digit
    return value


def H(A: int, M: int, N: int, digits: set[int]) -> int:
    quotient, digit = divmod(A, M)
    if digit not in digits:
        raise ValueError(f"inadmissible least digit {digit}")
    return N * quotient + digit


def zero_output_cycle(M: int, N: int, carry: int) -> tuple[list[int], int]:
    """Construct L-0004's least positive zero-output carry cycle."""
    if not 0 < carry < N:
        raise ValueError("carry must be nonzero and less than N")
    inverse_M = pow(M, -1, N)
    start = carry
    digits: list[int] = []

    while True:
        next_carry = (inverse_M * carry) % N
        numerator = M * next_carry - carry
        assert numerator % N == 0
        digit = numerator // N
        assert 0 <= digit < M
        digits.append(digit)
        carry = next_carry
        if carry == start:
            return digits, len(digits)


def verify_universal_carry_pump() -> None:
    # Recover L-0002 exactly.
    M, N, j = 64, 81, 1
    digits, length = zero_output_cycle(M, N, j)
    assert length == 9
    assert digits == [15, 29, 43, 57, 7, 22, 36, 50, 0]
    emitted, final_carry = normalize_carry(j, digits, M, N)
    assert emitted == [0] * length
    assert final_carry == j

    block = value_with_tail(digits, 0, M)
    assert block == j * (M**length - 1) // N

    for repetitions in range(5):
        for tail in (0, 1, 2, 17, 12_345):
            state = value_with_tail([j] + digits * repetitions, tail, M)
            expected_start = (
                M ** (length * repetitions + 1) * tail
                + j
                * (M ** (length * repetitions + 1) + (N - M))
                // N
            )
            assert state == expected_start
            for _ in range(length * repetitions + 1):
                state = H(state, M, N, {0, 1})
            assert state == N ** (length * repetitions) * (N * tail + j)

    # A short nonzero-output cycle in the width-three chart.
    M, N = 512, 729
    input_word = [361, 0]
    output_word = [2, 2]
    emitted, final_carry = normalize_carry(1, input_word, M, N)
    assert emitted == output_word
    assert final_carry == 1
    assert N * value_with_tail(input_word, 0, M) + 1 == (
        value_with_tail(output_word, 0, M) + M**2
    )


def ord_M(z: int, M: int) -> int:
    if z <= 0:
        raise ValueError("z must be positive")
    exponent = 0
    while z % M == 0:
        z //= M
        exponent += 1
    return exponent


def verify_run_length_skeleton() -> None:
    M, N, D = 64, 81, {0, 1}
    carry_block, block_length = zero_output_cycle(M, N, 1)

    for repetitions in (1, 2, 3):
        start = value_with_tail([1] + carry_block * repetitions, 7, M)
        state = start
        phases: list[tuple[int, int, int, int]] = []

        while state >= M:
            digit = state % M
            if digit not in D:
                break
            difference = state - digit
            phase_length = ord_M(difference, M)
            assert phase_length >= 1
            cofactor = difference // (M**phase_length)
            assert cofactor > 0 and cofactor % M != 0

            check = state
            for t in range(phase_length + 1):
                assert check == digit + N**t * M ** (phase_length - t) * cofactor
                if t < phase_length:
                    check = H(check, M, N, D)

            boundary = digit + N**phase_length * cofactor
            next_digit = boundary % M
            assert next_digit != digit
            phases.append((digit, phase_length, cofactor, boundary))
            state = boundary
            if next_digit not in D:
                break

        # The stack construction begins with one `1` phase and then the forced
        # zero phase. This checks the exact phase-chain equations.
        assert phases[0][0] == 1
        assert phases[0][1] == 1
        assert phases[1][0] == 0
        assert phases[1][1] >= block_length * repetitions
        for left, right in zip(phases, phases[1:]):
            digit, phase_length, cofactor, boundary = left
            next_digit, next_length, next_cofactor, _ = right
            assert boundary == next_digit + M**next_length * next_cofactor
            assert digit + N**phase_length * cofactor == boundary


def verify_finite_coding_identity() -> None:
    """Check the finite identity underlying T-0003 on exact trajectories."""
    M, N, D = 64, 81, {0, 1}
    c = N - M
    carry_block, _ = zero_output_cycle(M, N, 1)

    for repetitions in (1, 2, 3):
        A0 = value_with_tail([1] + carry_block * repetitions, 7, M)
        state = A0
        digits: list[int] = []
        horizon = 9 * repetitions + 1
        for _ in range(horizon):
            digit = state % M
            assert digit in D
            digits.append(digit)
            state = H(state, M, N, D)

        weighted = sum(
            digit * N ** (horizon - 1 - index) * M**index
            for index, digit in enumerate(digits)
        )
        assert M**horizon * state == N**horizon * A0 - c * weighted


def main() -> None:
    verify_recursion_against_direct_trace()
    print("verified L-0003 recursion against every direct trace through L=12")

    summaries, odd_counts, outputs = build_and_summarize(22)
    print("\nmaximal nontrivial supercritical collision fibers through L=22:")
    for item in summaries:
        if item.max_size == 0:
            print(f"L={item.length:2d}: none")
            continue
        print(
            f"L={item.length:2d}: count={item.nontrivial_count:6d} "
            f"max_cardinality={item.max_size:2d} "
            f"first_r={item.members[0]} a={item.odd_steps} "
            f"s={item.common_output}"
        )

    expected_members = (
        621_248,
        621_264,
        621_268,
        621_269,
        621_280,
        621_282,
        621_283,
        621_288,
        621_290,
        621_297,
        621_316,
        621_317,
        621_318,
        621_326,
        621_327,
        621_340,
        621_341,
        621_342,
    )
    assert summaries[-1].members == expected_members
    verify_sparse_eighteen_fiber(odd_counts, outputs)
    print("\nverified O-0004: depth-22 supercritical fiber of cardinality 18")

    verify_universal_carry_pump()
    print("verified L-0004 carry pumping and the 512->729 two-column tile")

    verify_run_length_skeleton()
    print("verified T-0004 run-length skeleton on exact stack trajectories")

    verify_finite_coding_identity()
    print("verified finite truncations of T-0003's coding identity")


if __name__ == "__main__":
    main()
