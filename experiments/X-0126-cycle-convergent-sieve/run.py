#!/usr/bin/env python3
"""X-0126: cycle hunt near log3(2) convergent denominators.

Target L in {5,6,8,11,13,16,19,24,29,...} related to continued-fraction
approximations of log3(2), with a = floor(L*log3(2)) or ceil, requiring
subcritical 3^a < 2^L. Exact integrality scan of all weight-a words when
binomial coefficient permits; otherwise random sample + modular filter.
"""

from __future__ import annotations

import json
import random
from itertools import combinations
from math import comb, log
from pathlib import Path


def B_of_ones(ones: tuple[int, ...], L: int) -> int:
    # ones positions, a = len(ones)
    a = len(ones)
    # chronological word with those ones
    total = 0
    ones_set = set(ones)
    # B formula
    seen = 0
    for j in range(L):
        if j in ones_set:
            seen += 1
            total += (1 << j) * (3 ** (a - seen))
    return total


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def follows(n: int, ones: tuple[int, ...], L: int) -> bool:
    ones_set = set(ones)
    x = n
    for j in range(L):
        bit = 1 if j in ones_set else 0
        if (x & 1) != bit:
            return False
        x = T(x)
    return x == n


def scan_La(L: int, a: int, max_enum: int = 30000, sample: int = 50000) -> dict:
    den = (1 << L) - 3**a
    if den <= 0:
        return {"L": L, "a": a, "status": "not_subcritical"}
    C = comb(L, a)
    hits = []
    checked = 0
    if C <= max_enum:
        for ones in combinations(range(L), a):
            checked += 1
            B = B_of_ones(ones, L)
            if B % den == 0:
                n = B // den
                if n > 2 and follows(n, ones, L):
                    hits.append({"ones": ones, "n": n})
        mode = "full"
    else:
        mode = "sample"
        rng = random.Random(L * 1000 + a)
        for _ in range(sample):
            ones = tuple(sorted(rng.sample(range(L), a)))
            checked += 1
            B = B_of_ones(ones, L)
            if B % den == 0:
                n = B // den
                if n > 2 and follows(n, ones, L):
                    hits.append({"ones": ones, "n": n})
    return {
        "L": L,
        "a": a,
        "den": den,
        "binom": C,
        "mode": mode,
        "checked": checked,
        "hits": hits,
        "log_ratio": a / L,
        "log3_2": log(2) / log(3),
    }


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    # convergent-ish L and nearby
    Ls = [5, 6, 7, 8, 9, 11, 12, 13, 16, 17, 19, 20, 24]
    rows = []
    for L in Ls:
        # a max subcritical: 3^a < 2^L => a < L log3(2)
        amax = int(L * log(2) / log(3))
        for a in {amax, max(1, amax - 1), max(1, amax - 2)}:
            if 3**a < (1 << L):
                rows.append(scan_La(L, a))
    nontrivial = [r for r in rows if r.get("hits")]
    summary = {
        "rows": rows,
        "nontrivial_rows": nontrivial,
        "total_hits": sum(len(r.get("hits", [])) for r in rows),
        "conclusion": (
            "Convergent-neighborhood cycle sieve; hits with n>2 would be K-candidates."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"configs={len(rows)} nontrivial_configs={len(nontrivial)} total_hits={summary['total_hits']}",
    ]
    for r in rows:
        lines.append(
            f"L={r['L']} a={r['a']} mode={r.get('mode')} checked={r.get('checked')} hits={len(r.get('hits', []))}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
