#!/usr/bin/env python3
"""X-9303: exact dual meet-in-the-middle minima for survivor rooms."""

from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import platform
from collections.abc import Iterator, Sequence
from pathlib import Path


DEFAULT_DEPTHS = (2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 46)


def parse_depths(text: str) -> tuple[int, ...]:
    try:
        depths = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if not depths or any(depth < 2 for depth in depths):
        raise argparse.ArgumentTypeError("depths must be comma-separated integers >= 2")
    return depths


def gray_subset_sums(
    generators: Sequence[int],
    modulus: int,
    *,
    include_mask: bool = False,
) -> Iterator[int] | Iterator[tuple[int, int]]:
    """Enumerate all subset sums using one modular update per Gray-code step."""

    current = 0
    previous_gray = 0
    if include_mask:
        yield 0, 0
    else:
        yield 0

    for index in range(1, 1 << len(generators)):
        gray = index ^ (index >> 1)
        changed = gray ^ previous_gray
        bit = (changed & -changed).bit_length() - 1
        if gray & (1 << bit):
            current = (current + generators[bit]) % modulus
        else:
            current = (current - generators[bit]) % modulus

        if include_mask:
            yield current, gray
        else:
            yield current
        previous_gray = gray


def find_mask(generators: Sequence[int], modulus: int, target: int) -> int:
    for value, mask in gray_subset_sums(generators, modulus, include_mask=True):
        if value == target:
            return mask
    raise AssertionError("recorded subset sum was not reproducible")


def standard_generators(depth: int) -> tuple[int, list[int]]:
    """Return Q=81^depth and the depth-j Cantor subset-sum generators."""

    modulus = 81**depth
    generators = [
        (-17 * pow(81, position, modulus) * pow(64, -(position + 1), modulus))
        % modulus
        for position in range(depth)
    ]
    return modulus, generators


def first_admissible_candidate(
    left_sum: int,
    sorted_right: Sequence[int],
    start: int,
    stop: int,
    modulus: int,
) -> tuple[int, int] | None:
    """Return the first combined residue >1 in a monotone right-sum interval."""

    for index in range(start, stop):
        right_sum = sorted_right[index]
        residue = (left_sum + right_sum) % modulus
        if residue > 1:
            return residue, right_sum
    return None


def minimum_nontrivial_class(depth: int) -> tuple[int, str]:
    """Compute min(C_depth \ {0,1}) exactly and return one minimizing word."""

    modulus, generators = standard_generators(depth)
    split = depth // 2
    left_generators = generators[:split]
    right_generators = generators[split:]

    right_sums = list(gray_subset_sums(right_generators, modulus))
    right_sums.sort()

    best = modulus
    best_left = -1
    best_right = -1

    for left_sum in gray_subset_sums(left_generators, modulus):
        target = (-left_sum) % modulus
        insertion = bisect.bisect_left(right_sums, target)

        # At and above the insertion point, combined residues begin at zero and
        # increase. Below it they are the non-wrapped residues and also increase.
        # We skip the two trivial residues 0 and 1 explicitly.
        candidates = (
            first_admissible_candidate(
                left_sum, right_sums, insertion, len(right_sums), modulus
            ),
            first_admissible_candidate(left_sum, right_sums, 0, insertion, modulus),
        )
        for candidate in candidates:
            if candidate is None:
                continue
            residue, right_sum = candidate
            if residue < best:
                best = residue
                best_left = left_sum
                best_right = right_sum

    if not (1 < best < modulus):
        raise AssertionError("failed to locate a nontrivial Cantor class")

    left_mask = find_mask(left_generators, modulus, best_left)
    right_mask = find_mask(right_generators, modulus, best_right)
    full_mask = left_mask | (right_mask << split)
    word = "".join(
        "1" if full_mask & (1 << position) else "0"
        for position in range(depth)
    )

    replay = sum(
        generator
        for position, generator in enumerate(generators)
        if full_mask & (1 << position)
    ) % modulus
    if replay != best:
        raise AssertionError("minimizing word does not replay to the minimum")

    return best, word


def direct_minimum(depth: int) -> int:
    """Small-depth independent full enumeration used as an internal cross-check."""

    modulus, generators = standard_generators(depth)
    values = list(gray_subset_sums(generators, modulus))
    return min(value for value in values if value > 1)


def starting_room_and_replay(
    depth: int,
    final_class: int,
    low_to_high_word: str,
) -> tuple[int, str]:
    """Convert the minimizing past class to a chronological survivor and replay it."""

    chronological_word = low_to_high_word[::-1]
    digits = [int(character) for character in chronological_word]
    prefix_polynomial = 17 * sum(
        digit * 81 ** (depth - 1 - position) * 64**position
        for position, digit in enumerate(digits)
    )
    numerator = 64**depth * final_class + prefix_polynomial
    denominator = 81**depth
    if numerator % denominator:
        raise AssertionError("fixed-room numerator is not divisible by 81^depth")
    starting_room = numerator // denominator

    expected = (final_class * 64**depth + denominator - 1) // denominator
    if starting_room != expected:
        raise AssertionError("fixed-room value is not the monotone ceiling transform")
    if not (1 < starting_room < 64**depth):
        raise AssertionError("nontrivial starting room is outside the standard range")

    state = starting_room
    for digit in digits:
        if state % 64 != digit:
            raise AssertionError("chronological word does not match the room digit")
        state = (81 * state - 17 * digit) // 64
    if state != final_class:
        raise AssertionError("survivor replay does not end at the minimizing class")

    return starting_room, chronological_word


def record_for_depth(depth: int) -> dict[str, int | str]:
    minimum, low_to_high_word = minimum_nontrivial_class(depth)
    starting_room, chronological_word = starting_room_and_replay(
        depth, minimum, low_to_high_word
    )

    if depth <= 16 and minimum != direct_minimum(depth):
        raise AssertionError("meet-in-the-middle and direct minima disagree")

    return {
        "depth": depth,
        "class_count": 1 << depth,
        "minimum_nontrivial_class": minimum,
        "minimizing_low_to_high_word": low_to_high_word,
        "chronological_survivor_word": chronological_word,
        "final_tail_class": minimum,
        "minimum_nontrivial_survivor": starting_room,
        "ordinary_survivor_lower_bound": starting_room,
        "lower_bound_bits": starting_room.bit_length(),
    }


def canonical_payload(depths: Sequence[int]) -> dict[str, object]:
    return {
        "experiment_id": "X-9303",
        "schema_version": 2,
        "arithmetic": (
            "exact integers; meet-in-the-middle subset sums modulo 81^j; "
            "direct survivor replay"
        ),
        "depths": list(depths),
        "records": [record_for_depth(depth) for depth in depths],
    }


def payload_digest(payload: dict[str, object]) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def check_frozen(path: Path, payload: dict[str, object], digest: str) -> None:
    frozen = json.loads(path.read_text(encoding="utf-8"))
    expected_digest = frozen.pop("results_sha256", None)
    if expected_digest != digest:
        raise SystemExit(
            f"digest mismatch: computed {digest}, frozen {expected_digest}"
        )
    if frozen != payload:
        raise SystemExit("computed payload differs from frozen canonical JSON")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--depths",
        type=parse_depths,
        default=DEFAULT_DEPTHS,
        help="comma-separated depths (default: frozen checkpoint list)",
    )
    parser.add_argument(
        "--check-results",
        type=Path,
        help="compare against a frozen canonical JSON result",
    )
    args = parser.parse_args()

    payload = canonical_payload(args.depths)
    digest = payload_digest(payload)
    output = dict(payload)
    output["results_sha256"] = digest

    print(f"python={platform.python_version()}")
    print(json.dumps(output, sort_keys=True, indent=2))

    if args.check_results is not None:
        check_frozen(args.check_results, payload, digest)
        print("frozen result check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
