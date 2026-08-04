#!/usr/bin/env python3
"""Exact finite minimum for the ordinary section of the H ghost attractor.

For each precision K, compute the full ghost residue set G mod 2^K and the
least P >= 16 with P == 1 mod 3 whose residue belongs to G. A decoded itinerary
prefix is included for one minimizing residue.

Standard library only. Finite minima do not prove asymptotic divergence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path


def e(r: int) -> int:
    return 3 * r + 2


def s(r: int) -> int:
    return 2 * r + 1


@lru_cache(maxsize=None)
def ghost_residues(K: int) -> frozenset[int]:
    """Return the H ghost closure modulo 2^K."""
    if K <= 0:
        return frozenset({0})
    modulus = 1 << K
    values = {0}
    r = 0
    while e(r) < K:
        scale = 1 << e(r)
        unit = pow(3, -s(r), modulus)
        for x in ghost_residues(K - e(r)):
            values.add((scale * unit * (x - 1)) % modulus)
        r += 1
    return frozenset(values)


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0) is not finite")
    return (n & -n).bit_length() - 1


def decode_prefix(residue: int, K: int) -> list[int]:
    """Decode the unique nonzero branch path visible at precision K."""
    path: list[int] = []
    x = residue
    precision = K
    while x != 0:
        valuation = v2(x)
        if valuation < 2 or (valuation - 2) % 3:
            raise AssertionError(("invalid ghost valuation", precision, x, valuation))
        r = (valuation - 2) // 3
        if e(r) >= precision:
            raise AssertionError(("branch not visible", precision, x, r))
        next_precision = precision - e(r)
        next_modulus = 1 << next_precision
        odd_part = x >> e(r)
        x = (1 + pow(3, s(r), next_modulus) * odd_part) % next_modulus
        path.append(r)
        precision = next_precision
    return path


def least_admissible(residues: frozenset[int], K: int) -> tuple[int, int]:
    modulus = 1 << K
    inverse_modulus = pow(modulus, -1, 3)
    period = 3 * modulus
    best: int | None = None
    best_residue = 0
    for residue in residues:
        t = ((1 - residue) * inverse_modulus) % 3
        candidate = residue + modulus * t
        if candidate < 16:
            candidate += ((16 - candidate + period - 1) // period) * period
        if best is None or candidate < best:
            best = candidate
            best_residue = residue
    if best is None:
        raise AssertionError("empty ghost residue set")
    return best, best_residue


@dataclass(frozen=True)
class Record:
    K: int
    count: int
    minimum: int
    residue: int
    prefix: list[int]


@dataclass(frozen=True)
class Summary:
    min_precision: int
    max_precision: int
    final_count: int
    final_minimum: int
    final_prefix: list[int]
    records: list[Record]
    digest_sha256: str


def audit(min_precision: int, max_precision: int) -> Summary:
    records: list[Record] = []
    for K in range(min_precision, max_precision + 1):
        residues = ghost_residues(K)
        minimum, residue = least_admissible(residues, K)
        prefix = decode_prefix(residue, K)
        record = Record(K, len(residues), minimum, residue, prefix)
        if records and minimum < records[-1].minimum:
            raise AssertionError(("minimum decreased", records[-1], record))
        records.append(record)

    payload = json.dumps(
        [asdict(record) for record in records],
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    final = records[-1]
    return Summary(
        min_precision=min_precision,
        max_precision=max_precision,
        final_count=final.count,
        final_minimum=final.minimum,
        final_prefix=final.prefix,
        records=records,
        digest_sha256=digest,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-precision", type=int, default=3)
    parser.add_argument("--max-precision", type=int, default=40)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.min_precision < 1 or args.max_precision < args.min_precision:
        raise SystemExit("invalid precision range")
    summary = audit(args.min_precision, args.max_precision)
    rendered = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
