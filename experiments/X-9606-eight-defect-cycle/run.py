#!/usr/bin/env python3
"""X-9606: exact eight-defect accelerated-cycle exclusion audit."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from math import ceil
from pathlib import Path
from typing import Iterator, Sequence

S = 8


def centered_data(word: Sequence[int]) -> tuple[int, int, int]:
    k = len(word)
    prefix = 0
    c = 0
    sparse = 0
    for j, valuation in enumerate(word):
        term = 3 ** (k - 1 - j) * 2**prefix
        c += term
        sparse += term * (4 - 2**valuation)
        prefix += valuation
    d = 2**prefix - 3**k
    e = c - d
    if e != sparse:
        raise AssertionError("centered identity failed")
    return c, d, e


def rotations(word: Sequence[int]) -> Iterator[tuple[int, ...]]:
    data = tuple(word)
    for shift in range(len(data)):
        yield data[shift:] + data[:shift]


def canonical_rotation(word: Sequence[int]) -> tuple[int, ...]:
    return min(rotations(word))


def unique_cyclic_multiset_words(values: Sequence[int]) -> list[tuple[int, ...]]:
    return sorted({canonical_rotation(p) for p in set(itertools.permutations(values))})


def weak_compositions(total: int, parts: int) -> Iterator[tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, parts - 1):
            yield (first,) + rest


def arrangements(kind: str) -> list[tuple[int, ...]]:
    if kind == "1^8":
        return [(1,) * S]
    if kind.startswith("1^7,"):
        high = int(kind.rsplit(",", 1)[1])
        rows = []
        for position in range(S):
            word = [1] * S
            word[position] = high
            rows.append(tuple(word))
        return rows
    rows = []
    if kind == "1^6,3,3":
        for p, q in itertools.combinations(range(S), 2):
            word = [1] * S
            word[p] = word[q] = 3
            rows.append(tuple(word))
        return rows
    if kind == "1^6,3,4":
        for p in range(S):
            for q in range(S):
                if p == q:
                    continue
                word = [1] * S
                word[p] = 3
                word[q] = 4
                rows.append(tuple(word))
        return rows
    raise ValueError(kind)


def core_word(exceptional: Sequence[int], gaps: Sequence[int]) -> tuple[int, ...]:
    word: list[int] = []
    for index, valuation in enumerate(exceptional):
        word.append(valuation)
        if index < S - 1:
            word.extend([2] * gaps[index])
    return tuple(word)


def contraction_packet() -> dict[str, object]:
    high_rows = []
    for high_count in range(3, S + 1):
        reps = {
            canonical_rotation(tuple(3 if i in positions else 1 for i in range(S)))
            for positions in itertools.combinations(range(S), high_count)
        }
        audited = []
        for word in sorted(reps):
            _, d, e = centered_data(word)
            audited.append((e - 2 * d, word, d, e))
        maximum = max(audited)
        if maximum[0] >= 0:
            raise AssertionError("h>=3 contraction classification failed")
        high_rows.append(
            {
                "high_count": high_count,
                "cyclic_classes": len(audited),
                "maximum_E_minus_2D": maximum[0],
                "maximizing_word": list(maximum[1]),
                "D": maximum[2],
                "E": maximum[3],
            }
        )

    pair_rows = []
    for pair in ((4, 4), (3, 5)):
        audited = []
        for word in unique_cyclic_multiset_words([1] * 6 + list(pair)):
            _, d, e = centered_data(word)
            audited.append((e - 2 * d, word, d, e))
        maximum = max(audited)
        if maximum[0] >= 0:
            raise AssertionError("two-high contraction classification failed")
        pair_rows.append(
            {
                "lowered_pair": list(pair),
                "cyclic_classes": len(audited),
                "maximum_E_minus_2D": maximum[0],
                "maximizing_word": list(maximum[1]),
                "D": maximum[2],
                "E": maximum[3],
            }
        )

    word = (1,) * 7 + (7,)
    _, d, e = centered_data(word)
    if not (d > 0 and e < 2 * d):
        raise AssertionError("one-high b>=7 contraction failed")
    return {
        "high_count_at_least_three": high_rows,
        "two_high_excluded_reductions": pair_rows,
        "one_high_at_least_seven": {
            "lowered_word": list(word),
            "D": d,
            "E": e,
            "E_minus_2D": e - 2 * d,
        },
        "surviving_types": [
            "1^8",
            "1^7,3",
            "1^7,4",
            "1^7,5",
            "1^7,6",
            "1^6,3,3",
            "1^6,3,4",
        ],
    }


TYPE_DATA: dict[str, dict[str, object]] = {
    "1^8": {"values": [1] * 8, "positive_R": 12, "first_excluded_R": 17},
    "1^7,3": {"values": [1] * 7 + [3], "positive_R": 7, "first_excluded_R": 17},
    "1^7,4": {"values": [1] * 7 + [4], "positive_R": 5, "first_excluded_R": 17},
    "1^7,5": {"values": [1] * 7 + [5], "positive_R": 2, "first_excluded_R": 17},
    "1^7,6": {"values": [1] * 7 + [6], "positive_R": 0, "first_excluded_R": 17},
    "1^6,3,3": {"values": [1] * 6 + [3, 3], "positive_R": 2, "first_excluded_R": 9},
    "1^6,3,4": {"values": [1] * 6 + [3, 4], "positive_R": 0, "first_excluded_R": 9},
}


def positive_bound(values: Sequence[int]) -> int:
    high_sum = sum(value for value in values if value >= 3)
    ones = sum(value == 1 for value in values)
    return 2 ** (high_sum + 1) * (3**ones - 2**ones)


def full_denominator(values: Sequence[int], neutral_count: int) -> int:
    return 2 ** sum(values) * 4**neutral_count - 3**S * 3**neutral_count


def cutoff_packet() -> list[dict[str, object]]:
    rows = []
    for kind, metadata in TYPE_DATA.items():
        values = metadata["values"]
        assert isinstance(values, list)
        positive_r = int(metadata["positive_R"])
        first_excluded = int(metadata["first_excluded_R"])
        coefficient = positive_bound(values)
        if full_denominator(values, positive_r) <= 0:
            raise AssertionError("positivity start failed")
        if positive_r and full_denominator(values, positive_r - 1) > 0:
            raise AssertionError("positivity start not minimal")

        def upper(r: int) -> int:
            return coefficient * 4 ** (r - ceil(r / S))

        if 2 * full_denominator(values, first_excluded) <= upper(first_excluded):
            raise AssertionError("cutoff failed")
        for r in range(first_excluded, first_excluded + 100):
            if 2 * full_denominator(values, r) <= upper(r):
                raise AssertionError("cutoff persistence failed")
        rows.append(
            {
                "type": kind,
                "B": sum(values),
                "positive_part_coefficient": coefficient,
                "positive_R": positive_r,
                "first_excluded_R": first_excluded,
                "upper_bound_at_first_excluded": upper(first_excluded),
                "two_D_at_first_excluded": 2 * full_denominator(values, first_excluded),
            }
        )
    return rows


def finite_table() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rows = []
    hits = []
    for kind, metadata in TYPE_DATA.items():
        values = metadata["values"]
        assert isinstance(values, list)
        possible = arrangements(kind)
        for neutral_count in range(int(metadata["positive_R"]), int(metadata["first_excluded_R"])):
            d = full_denominator(values, neutral_count)
            count = 0
            maximum = None
            height = 0
            rho = None
            for gaps in weak_compositions(neutral_count, S):
                if gaps[-1] != max(gaps):
                    continue
                for exceptional in possible:
                    count += 1
                    word = core_word(exceptional, gaps)
                    _, _, e = centered_data(word)
                    maximum = e if maximum is None else max(maximum, e)
                    remainder = e % d
                    if remainder == 0:
                        hits.append(
                            {
                                "type": kind,
                                "R": neutral_count,
                                "exceptional": list(exceptional),
                                "gaps": list(gaps),
                                "D": d,
                                "E_core": e,
                                "E_full": 3 ** gaps[-1] * e,
                                "start": 1 + 3 ** gaps[-1] * e // d,
                                "word": list(word) + [2] * gaps[-1],
                            }
                        )
                    if e >= 2 * d:
                        height += 1
                        if remainder:
                            circular = min(remainder, d - remainder)
                            rho = circular if rho is None else min(rho, circular)
            rows.append(
                {
                    "type": kind,
                    "R": neutral_count,
                    "D": d,
                    "largest_gap_candidates": count,
                    "max_E_core": maximum,
                    "height_survivors": height,
                    "least_nonzero_circular_remainder": rho,
                }
            )
    return rows, hits


def replay(start: int, word: Sequence[int]) -> None:
    current = start
    for valuation in word:
        numerator = 3 * current + 1
        if numerator % 2**valuation:
            raise AssertionError("bad valuation")
        current = numerator // 2**valuation
        if current <= 0 or current % 2 == 0:
            raise AssertionError("bad accelerated state")
    if current != start:
        raise AssertionError("bad return")


def canonical_payload() -> dict[str, object]:
    contractions = contraction_packet()
    cutoffs = cutoff_packet()
    rows, hits = finite_table()
    for hit in hits:
        replay(int(hit["start"]), hit["word"])
    aggregates = []
    for kind in TYPE_DATA:
        selected = [row for row in rows if row["type"] == kind]
        circular = [
            int(row["least_nonzero_circular_remainder"])
            for row in selected
            if row["least_nonzero_circular_remainder"] is not None
        ]
        aggregates.append(
            {
                "type": kind,
                "rows": len(selected),
                "largest_gap_candidates": sum(int(row["largest_gap_candidates"]) for row in selected),
                "height_survivors": sum(int(row["height_survivors"]) for row in selected),
                "least_nonzero_circular_remainder": min(circular) if circular else None,
            }
        )
    semantic = {"contractions": contractions, "cutoffs": cutoffs, "finite_rows": rows, "hits": hits}
    semantic_digest = hashlib.sha256(json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {
        "experiment_id": "X-9606",
        "schema_version": 1,
        "arithmetic": "exact Python integers",
        "claim": "no accelerated positive cycle has exactly eight valuations different from 2",
        "contraction_packet": contractions,
        "cutoff_packet": cutoffs,
        "finite_rows": rows,
        "aggregates": aggregates,
        "totals": {
            "finite_rows": len(rows),
            "largest_gap_candidates": sum(int(row["largest_gap_candidates"]) for row in rows),
            "height_survivors": sum(int(row["height_survivors"]) for row in rows),
            "formal_divisor_hits": len(hits),
            "nontrivial_cycle_hits": sum(int(hit["start"]) > 1 for hit in hits),
        },
        "semantic_audit_sha256": semantic_digest,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()
    payload = canonical_payload()
    payload["results_sha256"] = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    if args.check_results:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        if frozen != payload:
            raise SystemExit("frozen result mismatch")
        print("frozen result check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
