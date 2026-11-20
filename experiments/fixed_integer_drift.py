#!/usr/bin/env python3
"""Exact finite interfaces for translated Collatz path occupancy.

No third-party dependencies. This is bounded replay, not a universal
coefficient-stopping certificate. The proof is in
research/fixed-integer-descent/drift.md.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from math import comb
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def affine(word: tuple[int, ...]) -> tuple[int, int, int]:
    """Return length, odd count and unnormalized affine constant."""
    a = q = 0
    for i, bit in enumerate(word):
        if bit:
            a = 3 * a + (1 << i)
            q += 1
    return len(word), q, a


def replay_word(n: int, word: tuple[int, ...]) -> int:
    for bit in word:
        require(n % 2 == bit, "parity residue is wrong")
        n = step(n)
    return n


def low_band_count(width: int, k: int, q: int) -> int:
    return (3**q * (width + (1 << (k - q))) - 1) // (1 << k)


def interval_bound(width: int, k: int, h: int) -> int:
    require(width >= 1 and 0 <= h <= k, "invalid bound arguments")
    modulus = 1 << k
    high = ((width + modulus - 1) // modulus) * sum(
        comb(k, q) for q in range(h + 1, k + 1)
    )
    low = sum(low_band_count(width, k, q) for q in range(h + 1))
    return k + high + low


@lru_cache(maxsize=None)
def best_bound(width: int) -> tuple[int, int, int]:
    """Evaluate (2) exactly, including the always valid k=0 choice."""
    require(width >= 1, "interval width must be positive")
    best = (width, 0, 0)
    for k in range(1, width.bit_length() + 1):
        modulus = 1 << k
        factor = (width + modulus - 1) // modulus
        tail = (1 << k) - 1
        low = low_band_count(width, k, 0)
        best = min(best, (k + factor * tail + low, k, 0))
        for h in range(1, k + 1):
            tail -= comb(k, h)
            low += low_band_count(width, k, h)
            best = min(best, (k + factor * tail + low, k, h))
    return best


def simple_path(n: int, cap: int = 10000) -> list[int]:
    path = []
    seen = set()
    while n not in seen and len(path) < cap:
        path.append(n)
        seen.add(n)
        n = step(n)
    require(n in seen, "finite replay cap reached before a repetition")
    return path


def verify_simple_path(path: list[int]) -> None:
    require(len(path) == len(set(path)), "path has a repeated state")
    require(all(x >= 1 for x in path), "path is not positive ordinary")
    require(all(step(a) == b for a, b in zip(path, path[1:])), "bad edge")


def max_occupancy(path: list[int], width: int) -> int:
    """All translated integer windows, by a two-pointer sweep."""
    ordered = sorted(path)
    left = maximum = 0
    for right, value in enumerate(ordered):
        while value - ordered[left] >= width:
            left += 1
        maximum = max(maximum, right - left + 1)
    return maximum


def verify_record_window(
    records: list[int], lower: int, width: int
) -> None:
    require(width >= 1, "empty record window")
    require(all(lower <= x < lower + width for x in records), "record outside window")
    require(len(records) <= best_bound(width)[0], "record occupancy bound violated")


def check_words(depth: int) -> dict[str, int]:
    words = lifts = literal_steps = 0
    for k in range(depth + 1):
        residues = set()
        counts: Counter[int] = Counter()
        for bits in product((0, 1), repeat=k):
            _, q, a = affine(bits)
            modulus = 1 << k
            residue = (-a * pow(3**q, -1, modulus)) % modulus if k else 0
            require(residue not in residues, "parity cylinders collide")
            residues.add(residue)
            counts[q] += 1
            require(
                a * (1 << q) <= modulus * (3**q - (1 << q)),
                "sharp affine remainder bound violated",
            )
            for lift in (1, 7):
                n = residue + modulus * lift
                endpoint = replay_word(n, bits)
                require(modulus * endpoint == 3**q * n + a, "affine identity failed")
                lifts += 1
                literal_steps += k
            words += 1
        require(len(residues) == 1 << k, "cylinder coverage is incomplete")
        require(all(counts[q] == comb(k, q) for q in range(k + 1)), "weight census failed")
        for q in range(k + 1):
            _, _, a = affine((0,) * (k - q) + (1,) * q)
            require(a * (1 << q) == (1 << k) * (3**q - (1 << q)), "extremal word is not sharp")
    return {"parity_words": words, "ordinary_lifts": lifts, "literal_steps": literal_steps}


def check_interval_images() -> dict[str, int]:
    cohorts = source_replays = image_interfaces = 0
    starts = (1, 29, (1 << 20) + 3, 10**30 + 17)
    widths = (1, 3, 16, 63, 128, 257, 512, 1024)
    for a in starts:
        for width in widths:
            for k in (0, 1, 2, 4, 7, 10, 12):
                images: dict[int, set[int]] = defaultdict(set)
                source_counts: Counter[int] = Counter()
                modulus = 1 << k
                for source in range(a, a + width):
                    value, q = source, 0
                    for _ in range(k):
                        q += value % 2
                        value = step(value)
                    images[q].add(value)
                    source_counts[q] += 1
                    left = 3**q * a
                    right = 3**q * (a + width) + 3**q * (1 << (k - q)) - modulus
                    require(left <= modulus * value < right, "translated affine band failed")
                    source_replays += 1
                all_images = set().union(*images.values())
                for h in {0, k, 39 * k // 64}:
                    low = sum(low_band_count(width, k, q) for q in range(h + 1))
                    high = ((width + modulus - 1) // modulus) * sum(
                        comb(k, q) for q in range(h + 1, k + 1)
                    )
                    require(sum(source_counts[q] for q in range(h + 1, k + 1)) <= high, "high-count cylinder bound failed")
                    for q in range(h + 1):
                        require(len(images[q]) <= low_band_count(width, k, q), "low-count image bound failed")
                    require(len(all_images) <= high + low, "total image bound failed")
                    require(interval_bound(width, k, h) == k + high + low, "bound implementations disagree")
                    image_interfaces += 1
                cohorts += 1
    return {"translated_cohorts": cohorts, "source_replays": source_replays, "image_interfaces": image_interfaces}


def check_paths(limit: int) -> dict[str, int]:
    windows = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1 << 20)
    counts = {"simple_paths": 0, "listed_states": 0, "translated_window_checks": 0}
    for source in range(1, limit + 1):
        path = simple_path(source)
        verify_simple_path(path)
        counts["simple_paths"] += 1
        counts["listed_states"] += len(path)
        for width in windows:
            bound, k, h = best_bound(width)
            require(bound == interval_bound(width, k, h), "optimized bound mismatch")
            require(max_occupancy(path, width) <= bound, "simple-path interval bound failed")
            counts["translated_window_checks"] += 1
    return counts


def check_record_prefixes() -> dict[str, int]:
    counts = {"record_paths": 0, "product_edges": 0, "record_prefix_checks": 0, "no_descent_prefix_checks": 0, "maximum_records": 0}
    for source in sorted(set(range(1, 257)) | {993, 6171, 703, 1819, 27, 97}):
        path = simple_path(source)
        verify_simple_path(path)
        selected = {0, 1, 2, 5, 10, len(path) // 2, len(path) - 1}
        coefficient = Fraction(1)
        smallest_coefficient = Fraction(1)
        correction = Fraction(1)
        minimum = source
        records = [source]
        for i, value in enumerate(path):
            minimum = min(minimum, value)
            if i:
                prev = path[i - 1]
                coefficient *= Fraction(3 if prev & 1 else 1, 2)
                if prev & 1:
                    correction *= Fraction(3 * prev + 1, 3 * prev)
                require(value == source * coefficient * correction, "correction product failed")
                if coefficient < smallest_coefficient:
                    smallest_coefficient = coefficient
                    records.append(value)
                counts["product_edges"] += 1
            if i in selected:
                top = source * correction
                width = top.numerator // top.denominator - minimum + 1
                verify_record_window(records, minimum, width)
                counts["record_prefix_checks"] += 1
                if minimum == source:
                    budget = source * (correction - 1)
                    require(width == budget.numerator // budget.denominator + 1, "no-descent width mismatch")
                    counts["no_descent_prefix_checks"] += 1
                counts["maximum_records"] = max(counts["maximum_records"], len(records))
        counts["record_paths"] += 1
    return counts


def negative_controls() -> list[str]:
    rejected = []

    def expect_rejection(name: str, operation) -> None:
        try:
            operation()
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError("negative control was accepted: " + name)

    expect_rejection("repeated_cycle_counted_with_multiplicity", lambda: verify_simple_path([1, 2, 1]))
    expect_rejection("wrong_parity_residue", lambda: replay_word(2, (1,)))
    expect_rejection("empty_record_window", lambda: verify_record_window([2], 2, 0))
    expect_rejection("omitted_odd_affine_correction", lambda: require(2 * step(1) == 3, "missing affine correction"))
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-limit", type=int, default=4096)
    parser.add_argument("--word-depth", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    require(1 <= args.source_limit <= 100000, "unsupported finite source limit")
    require(0 <= args.word_depth <= 16, "unsupported finite word depth")
    require(3**1170 < 2**1856, "rational exponent comparison one failed")
    require(2**9664 < 39**1170 * 25**750, "rational exponent comparison two failed")
    report = {
        "status": "PASS",
        "scope": "Bounded exact arithmetic replay; no universal stopping, cycle exclusion, or instantiation of the enormous universal record window.",
        "parameters": {"source_limit": args.source_limit, "word_depth": args.word_depth},
        "words": check_words(args.word_depth),
        "interval_images": check_interval_images(),
        "paths": check_paths(args.source_limit),
        "records": check_record_prefixes(),
        "rejected_mutations": negative_controls(),
        "rational_exponent_certificates": ["3^1170 < 2^1856", "2^9664 < 39^1170 * 25^750"],
        "selected_exact_bounds": [
            {"width": width, "bound": result[0], "k": result[1], "h": result[2]}
            for width in (128, 4096, 100000, 10**10, 10**20, 10**50)
            for result in [best_bound(width)]
        ],
    }
    text = json.dumps(report, indent=2) + "\n"
    if args.compare:
        require(report == json.loads(args.compare.read_text(encoding="utf-8")), "replay differs from frozen report")
    if args.output:
        require(not args.output.exists(), "refusing to overwrite existing evidence")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
