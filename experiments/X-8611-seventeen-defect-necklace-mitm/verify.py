#!/usr/bin/env python3
"""Independent product-window, necklace, count, and small-cell audit."""
from __future__ import annotations
from functools import lru_cache
from math import comb
from pathlib import Path
import sys

@lru_cache(None)
def defect_count(n, total):
    if n == 0:
        return int(total == 0)
    return sum(defect_count(n - 1, total - a)
               for a in range(1, total + 1) if a != 2)

def defect_words(n, total, prefix=()):
    if n == 0:
        if total == 0:
            yield prefix
        return
    for a in range(1, total + 1):
        if a != 2:
            yield from defect_words(n - 1, total - a, prefix + (a,))

def necklace_count(total):
    # Burnside for prime length 17: every nonconstant orbit has size 17.
    raw = defect_count(17, total)
    fixed = int(total % 17 == 0 and total // 17 >= 1 and total // 17 != 2)
    assert (raw + 16 * fixed) % 17 == 0
    result = (raw + 16 * fixed) // 17
    # Independent explicit check on every defect total occurring here.
    explicit = {min(w[i:] + w[:i] for i in range(17))
                for w in defect_words(17, total)}
    assert len(explicit) == result
    return result

def product_windows():
    cells = []
    for r in range(100):
        for b in range(17, 120):
            exponent = b + 2 * r
            length = 17 + r
            if (1 << exponent) * 7**length > 22**length:
                break
            if 3**length < (1 << exponent) and defect_count(17, b):
                cells.append((r, b))
    return cells

def half_counts(r):
    stored = queries = 0
    for u in range(r + 1):
        left = comb(u + 7, 7)
        right = comb(r - u + 8, 8)
        stored += min(left, right)
        queries += max(left, right)
    return stored, queries

def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from compositions(total - first, parts - 1, prefix + (first,))

def affine_constant(word):
    c = 0
    exponent = 0
    for a in word:
        c = 3 * c + (1 << exponent)
        exponent += a
    return c, exponent

def direct_small():
    # Exhaust every anchored word in the three smallest product cells.
    for r, b in [(0, 27), (0, 28), (1, 27)]:
        denominator = (1 << (b + 2 * r)) - 3**(17 + r)
        seen = 0
        for defects in defect_words(17, b):
            for gaps in compositions(r, 17):
                word = []
                for a, g in zip(defects, gaps):
                    word.append(a)
                    word.extend([2] * g)
                c, exponent = affine_constant(word)
                assert exponent == b + 2 * r
                assert c % denominator
                seen += 1
        assert seen == defect_count(17, b) * comb(r + 16, 16)

def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1
                else "results/canonical.txt")
    text = path.read_text()
    cells = product_windows()
    parsed = []
    for line in text.splitlines():
        if line.startswith("window R="):
            fields = dict(item.split("=") for item in line.split()[1:])
            assert fields["formal"] == "0" and fields["exact"] == "0"
            parsed.append((int(fields["R"]), int(fields["B"])))
    assert parsed == cells

    anchored = canonical_instances = stored = queries = 0
    for r, b in cells:
        raw = defect_count(17, b)
        necklaces = necklace_count(b)
        gaps = comb(r + 16, 16)
        anchored += raw * gaps
        canonical_instances += necklaces * gaps
        st, qu = half_counts(r)
        stored += necklaces * st
        queries += necklaces * qu

    assert (len(cells), anchored, canonical_instances, stored, queries) == (
        55, 16_071_941_097_518, 4_856_645_105_230,
        17_053_060, 2_471_674_701)
    expected = {
        "windows=55",
        "anchored_words=16071941097518",
        "canonical_pattern_gap_instances=4856645105230",
        "stored_states=17053060",
        "queries=2471674701",
        "formal_matches=0",
        "exact_cycles=0",
    }
    assert expected.issubset(set(text.splitlines()))
    direct_small()
    print("X-8611 independent window/necklace/count/direct audit passed")

if __name__ == "__main__":
    main()
