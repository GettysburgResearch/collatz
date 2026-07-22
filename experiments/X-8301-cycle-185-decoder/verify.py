#!/usr/bin/env python3
"""Independent checker for X-8301. Does not import the author implementation."""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

K = 185
P = 3**K


def affine_constant(word: list[int]) -> int:
    prefix = 0
    result = 0
    for index, value in enumerate(word):
        result += 3 ** (K - 1 - index) * 2**prefix
        prefix += value
    return result


def make(kind: str):
    if kind == "AA":
        word = [1]
        positions = []
        for _ in range(92):
            word += [1, 2]
            positions.append(len(word) - 1)
        minimum_h, uniform_max = 17, 539_801
    elif kind == "DD":
        word = [1, 2, 2]
        positions = [1, 2]
        for _ in range(2, 93):
            word += [1, 2]
            positions.append(len(word) - 1)
        minimum_h, uniform_max = 16, 566_791
    else:
        raise ValueError(kind)

    assert len(word) == K
    prefix = 0
    terms = []
    for index, value in enumerate(word):
        terms.append(3 ** (K - 1 - index) * 2**prefix)
        prefix += value
    suffix = [sum(terms[position + 1 :]) for position in positions]
    valuations = [
        None if value == 0 else (value & -value).bit_length() - 1
        for value in suffix
    ]
    assert suffix[-1] == 0
    assert all(
        valuations[index] < valuations[index + 1]
        for index in range(len(valuations) - 2)
    )
    return word, positions, minimum_h, uniform_max, sum(word), affine_constant(word), suffix, valuations


def test_ordered_jump(kind: str) -> None:
    word, positions, *_rest, suffix, _valuations = make(kind)
    base = affine_constant(word)
    rng = random.Random(8301 + (kind == "DD"))
    for height in range(30):
        for _ in range(100):
            indices = sorted(rng.randrange(len(positions)) for _ in range(height))
            candidate = word[:]
            for index in indices:
                candidate[positions[index]] += 1
            predicted = base + sum(
                (1 << rank) * suffix[index]
                for rank, index in enumerate(indices)
            )
            assert affine_constant(candidate) == predicted


def scan(kind: str, height: int, first: int, last: int) -> dict[str, object]:
    _word, _positions, _minimum_h, _uniform_max, base_total, base_constant, suffix, vals = make(kind)
    lookup = {value: index for index, value in enumerate(vals[:-1])}
    denominator = 2 ** (base_total + height) - P
    reasons: dict[str, int] = {}
    max_depth = 0
    max_valuation = 0
    solutions: list[dict[str, int]] = []

    for multiplier in range(first, last + 1):
        remainder = multiplier * denominator - base_constant
        previous = 0
        reason = None
        depth = 0
        if remainder < 0:
            reason = "initial_negative"
        else:
            for rank in range(height):
                if remainder == 0:
                    reason = "success_final_tail"
                    depth = rank
                    break
                valuation = (remainder & -remainder).bit_length() - 1
                max_valuation = max(max_valuation, valuation)
                index = lookup.get(valuation - rank)
                if index is None:
                    reason = "invalid_valuation"
                    depth = rank
                    break
                if index < previous:
                    reason = "decreasing_position"
                    depth = rank
                    break
                term = (1 << rank) * suffix[index]
                if term > remainder:
                    reason = "negative_remainder"
                    depth = rank + 1
                    break
                remainder -= term
                previous = index
                depth = rank + 1
            if reason is None:
                reason = "success" if remainder == 0 else "nonzero_terminal_remainder"
        reasons[reason] = reasons.get(reason, 0) + 1
        max_depth = max(max_depth, depth)
        if reason.startswith("success"):
            solutions.append({"multiplier": multiplier, "decoded_depth": depth})

    return {
        "h": height,
        "first_multiplier": first,
        "last_multiplier": last,
        "multipliers_scanned": last - first + 1,
        "maximum_decoded_depth": max_depth,
        "maximum_remainder_valuation": max_valuation,
        "stop_reasons": dict(sorted(reasons.items())),
        "solutions": solutions,
    }


def bounds(kind: str, height: int) -> tuple[int, int]:
    _w, _p, _h, _u, base_total, base_constant, suffix, _v = make(kind)
    denominator = 2 ** (base_total + height) - P
    return (
        (base_constant + denominator - 1) // denominator,
        (base_constant + ((1 << height) - 1) * suffix[0]) // denominator,
    )


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py canonical.json")
    expected = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    for kind in ("AA", "DD"):
        test_ordered_jump(kind)
        record = expected["skeletons"][kind]
        for frozen in record["direct_scans"]:
            first, last = bounds(kind, frozen["h"])
            actual = scan(kind, frozen["h"], first, last)
            if actual != frozen:
                raise AssertionError(f"direct scan mismatch: {kind} H={frozen['h']}")
        ref = record["reference_scan"]
        actual_ref = scan(kind, 31, 1, record["uniform_multiplier_max"])
        if actual_ref != ref:
            raise AssertionError(f"reference mismatch: {kind}")
        if set(actual_ref["stop_reasons"]) != {"invalid_valuation"}:
            raise AssertionError("reference failure is not stable")

    print("independent X-8301 verification passed")


if __name__ == "__main__":
    main()
