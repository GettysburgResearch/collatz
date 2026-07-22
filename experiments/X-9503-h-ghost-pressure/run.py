#!/usr/bin/env python3
"""Exact audit for H ghost IFS and mixed-sign crossing threshold.

Standard library only. Finite verification is evidence, not a universal proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


def e(r: int) -> int:
    return 3 * r + 2


def s(r: int) -> int:
    return 2 * r + 1


@lru_cache(maxsize=None)
def ghost_residues(K: int) -> frozenset[int]:
    if K <= 0:
        return frozenset({0})
    modulus = 1 << K
    values = {0}
    r = 0
    while e(r) < K:
        unit = pow(3, -s(r), modulus)
        scale = 1 << e(r)
        for x in ghost_residues(K - e(r)):
            values.add((scale * unit * (x - 1)) % modulus)
        r += 1
    return frozenset(values)


@dataclass(frozen=True)
class WordNode:
    word: tuple[int, ...]
    U: int
    V: int
    A: int
    Y: int
    sigma_num: int
    sigma_den: int

    @property
    def sigma(self) -> Fraction:
        return Fraction(self.sigma_num, self.sigma_den)


def one_data(r: int) -> tuple[int, int, int, int]:
    U = 1 << e(r)
    V = 3 ** s(r)
    A = 1 << (3 * r)
    Y = (V + 1) // 4
    return U, V, A, Y


def start_node(r: int) -> WordNode:
    U, V, A, Y = one_data(r)
    sigma = Fraction(U, V)
    return WordNode((r,), U, V, A, Y, sigma.numerator, sigma.denominator)


def append_node(node: WordNode, r: int) -> tuple[WordNode, int, int]:
    U_r, V_r, A_r, Y_r = one_data(r)
    h = ((A_r - node.Y) * pow(node.V, -1, U_r)) % U_r
    N = node.Y + h * node.V
    j = (N - A_r) // U_r
    if not (0 <= j < node.V):
        raise AssertionError(("bad output carry", node.word, r, h, j))
    U = node.U * U_r
    V = node.V * V_r
    A = node.A + h * node.U
    Y = Y_r + j * V_r
    sigma = node.sigma + Fraction(U, V)
    child = WordNode(
        node.word + (r,), U, V, A, Y, sigma.numerator, sigma.denominator
    )
    return child, h, N


@dataclass(frozen=True)
class Summary:
    max_precision: int
    residue_counts: list[int]
    residue_recurrence_checks: int
    branch_partition_checks: int
    first_crossing_max_prefix_length: int
    first_crossing_max_letter: int
    first_crossings_checked: int
    zero_carry_crossings: int
    positive_carry_crossings: int
    threshold_failures: int
    minimum_threshold_ratio: str
    minimum_threshold_word: list[int]
    minimum_threshold_carry: int
    minimum_threshold_state: int
    digest_sha256: str


def audit(max_precision: int, max_prefix_length: int, max_letter: int) -> Summary:
    digest = hashlib.sha256()

    counts = []
    recurrence_checks = 0
    branch_checks = 0
    for K in range(1, max_precision + 1):
        residues = ghost_residues(K)
        counts.append(len(residues))
        if K >= 4:
            if len(residues) != counts[K - 3] + counts[K - 4]:
                raise AssertionError(("plastic recurrence", K, len(residues)))
            recurrence_checks += 1

        modulus = 1 << K
        seen = {0}
        r = 0
        while e(r) < K:
            branch = {
                ((1 << e(r)) * pow(3, -s(r), modulus) * (x - 1)) % modulus
                for x in ghost_residues(K - e(r))
            }
            if seen.intersection(branch):
                raise AssertionError(("branch overlap", K, r))
            if any((x & -x).bit_length() - 1 != e(r) for x in branch):
                raise AssertionError(("wrong branch valuation", K, r))
            seen.update(branch)
            branch_checks += 1
            r += 1
        if seen != set(residues):
            raise AssertionError(("branch partition mismatch", K))
        digest.update(
            json.dumps(
                {"K": K, "count": len(residues), "residues": sorted(residues)},
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        )

    frontier = [
        start_node(r)
        for r in range(max_letter + 1)
        if 3 ** s(r) > 2 ** e(r)
    ]
    crossings = 0
    zero = 0
    positive = 0
    failures = 0
    min_ratio: Fraction | None = None
    min_record: tuple[tuple[int, ...], int, int] | None = None

    for _prefix_length in range(1, max_prefix_length + 1):
        for node in frontier:
            for r in range(3):
                child, h, N = append_node(node, r)
                if child.V >= child.U:
                    continue
                crossings += 1
                if h == 0:
                    zero += 1
                else:
                    positive += 1
                U_r, V_r, _, _ = one_data(r)
                slope_gap = Fraction(node.U, node.V) - Fraction(V_r, U_r)
                threshold = (1 + node.sigma) / (4 * slope_gap)
                ratio = Fraction(N, 1) / threshold
                if ratio <= 1:
                    failures += 1
                if min_ratio is None or ratio < min_ratio:
                    min_ratio = ratio
                    min_record = (child.word, h, N)
                digest.update(
                    json.dumps(
                        {
                            "word": child.word,
                            "h": h,
                            "N": N,
                            "threshold_num": threshold.numerator,
                            "threshold_den": threshold.denominator,
                            "ratio_num": ratio.numerator,
                            "ratio_den": ratio.denominator,
                        },
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode("utf-8")
                )

        next_frontier: list[WordNode] = []
        for node in frontier:
            for r in range(max_letter + 1):
                child, _, _ = append_node(node, r)
                if child.V > child.U:
                    next_frontier.append(child)
        frontier = next_frontier

    if min_ratio is None or min_record is None:
        raise AssertionError("no first crossings generated")

    return Summary(
        max_precision=max_precision,
        residue_counts=counts,
        residue_recurrence_checks=recurrence_checks,
        branch_partition_checks=branch_checks,
        first_crossing_max_prefix_length=max_prefix_length,
        first_crossing_max_letter=max_letter,
        first_crossings_checked=crossings,
        zero_carry_crossings=zero,
        positive_carry_crossings=positive,
        threshold_failures=failures,
        minimum_threshold_ratio=f"{min_ratio.numerator}/{min_ratio.denominator}",
        minimum_threshold_word=list(min_record[0]),
        minimum_threshold_carry=min_record[1],
        minimum_threshold_state=min_record[2],
        digest_sha256=digest.hexdigest(),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-precision", type=int, default=24)
    parser.add_argument("--max-prefix-length", type=int, default=6)
    parser.add_argument("--max-letter", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    summary = audit(args.max_precision, args.max_prefix_length, args.max_letter)
    rendered = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
