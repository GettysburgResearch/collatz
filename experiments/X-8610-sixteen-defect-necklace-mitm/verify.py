#!/usr/bin/env python3
"""Independent coverage, necklace, count, and small-cell audit for X-8610."""
from __future__ import annotations
from functools import lru_cache
from math import comb
from pathlib import Path
import sys

@lru_cache(None)
def defect_count(n: int, total: int) -> int:
    if n == 0:
        return int(total == 0)
    return sum(
        defect_count(n - 1, total - a)
        for a in range(1, total + 1)
        if a != 2
    )

def defect_words(n: int, total: int, prefix=()):
    if n == 0:
        if total == 0:
            yield prefix
        return
    for a in range(1, total + 1):
        if a != 2:
            yield from defect_words(n - 1, total - a, prefix + (a,))

def least_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))

@lru_cache(None)
def necklace_count(total: int) -> int:
    canonical = set()
    raw = 0
    for word in defect_words(16, total):
        raw += 1
        canonical.add(least_rotation(word))
    assert raw == defect_count(16, total)
    # Every raw word maps to exactly one retained rotation class.
    assert all(least_rotation(word) in canonical
               for word in defect_words(16, total))
    return len(canonical)

def product_windows():
    cells = []
    for r in range(100):
        for b in range(16, 100):
            exponent = b + 2 * r
            length = 16 + r
            if (1 << exponent) * 7**length > 22**length:
                break
            if 3**length < (1 << exponent) and defect_count(16, b):
                cells.append((r, b))
    return cells

def half_counts(r: int):
    stored = queries = 0
    for left_neutral in range(r + 1):
        left = comb(left_neutral + 7, 7)
        right = comb(r - left_neutral + 7, 7)
        stored += min(left, right)
        queries += max(left, right)
    return stored, queries

def weak_compositions(total: int, parts: int, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from weak_compositions(total - first, parts - 1,
                                     prefix + (first,))

def affine_constant(word):
    constant = 0
    exponent = 0
    for a in word:
        constant = 3 * constant + (1 << exponent)
        exponent += a
    return constant, exponent

def direct_small_cells():
    # R=0 has one gap vector and 31,824 anchored defect words.  Test every one
    # directly; this does not use the C++ join or its cyclic quotient.
    r, b = 0, 26
    denominator = (1 << b) - 3**16
    seen = 0
    for defects in defect_words(16, b):
        constant, exponent = affine_constant(defects)
        assert exponent == b
        assert constant % denominator
        seen += 1
    assert seen == 31_824

    # Also check all cells with R=1 by direct word construction.
    for b in (25, 26):
        denominator = (1 << (b + 2)) - 3**17
        seen = 0
        for defects in defect_words(16, b):
            for gaps in weak_compositions(1, 16):
                word = []
                for a, g in zip(defects, gaps):
                    word.append(a)
                    word.extend([2] * g)
                constant, exponent = affine_constant(word)
                assert exponent == b + 2
                assert constant % denominator
                seen += 1
        assert seen == defect_count(16, b) * 16

def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1
                else "results/canonical.txt")
    text = path.read_text()
    cells = product_windows()
    parsed = []
    for line in text.splitlines():
        if line.startswith("window R="):
            fields = dict(item.split("=") for item in line.split()[1:])
            assert fields["formal"] == "0"
            assert fields["exact"] == "0"
            parsed.append((int(fields["R"]), int(fields["B"])))
    assert parsed == cells

    anchored = canonical_instances = stored = queries = 0
    for r, b in cells:
        raw = defect_count(16, b)
        necklaces = necklace_count(b)
        gap_count = comb(r + 15, 15)
        anchored += raw * gap_count
        canonical_instances += necklaces * gap_count
        st, qu = half_counts(r)
        stored += necklaces * st
        queries += necklaces * qu

    expected = {
        "windows=48",
        "anchored_words=2216415791876",
        "canonical_pattern_gap_instances=724990098067",
        "stored_states=6134501",
        "queries=543652557",
        "formal_matches=0",
        "exact_cycles=0",
    }
    assert expected.issubset(set(text.splitlines()))
    assert (len(cells), anchored, canonical_instances, stored, queries) == (
        48, 2_216_415_791_876, 724_990_098_067,
        6_134_501, 543_652_557)
    direct_small_cells()
    print("X-8610 independent window/necklace/count/direct audit passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
