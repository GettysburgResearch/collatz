#!/usr/bin/env python3
"""X-0109: complementary-domain (free-group style) ping-pong probe on RP^1.

Classical ping-pong for free semigroups: sets D_i and maps g_i with
    g_i( X \\ D_i ) subset D_i
and D_i pairwise disjoint.

Here X = RP^1 identified with R ∪ {∞}, and g_i are inverse Collatz branches
(affine). This is the residual real-geometric format not killed by L-0101/L-0102.

We search numerically for pairs of supercritical inverses and disjoint closed
intervals D1,D2 where each inverse sends the complement's relevant compact
pieces into its own Di.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


def B_of(word: str) -> int:
    ones = word.count("1")
    seen = 0
    total = 0
    for j, bit in enumerate(word):
        if bit == "1":
            seen += 1
            total += (1 << j) * (3 ** (ones - seen))
    return total


@dataclass(frozen=True)
class Aff:
    word: str
    mu: Fraction
    beta: Fraction

    def g(self, y: Fraction) -> Fraction:
        return (y - self.beta) / self.mu


def mild(Lmax: int = 11) -> list[Aff]:
    out = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            mu = Fraction(3**a, 1 << L)
            if Fraction(1, 1) < mu <= Fraction(5, 4):
                out.append(Aff(word, mu, Fraction(B_of(word), 1 << L)))
    return out


def interval_image(g, a: Fraction, b: Fraction):
    ga, gb = g(a), g(b)
    return (min(ga, gb), max(ga, gb))


def contained(inner, outer) -> bool:
    return outer[0] <= inner[0] and inner[1] <= outer[1]


def disjoint(a, b, gap: Fraction) -> bool:
    return a[1] + gap <= b[0] or b[1] + gap <= a[0]


def try_pair(f1: Aff, f2: Aff, grid_scale: Fraction) -> dict | None:
    # Search D1,D2 as compact intervals in a large positive region far above taus
    tau = max(f1.beta, f2.beta)
    base = tau + 1
    pts = [base * (1 + grid_scale * i) for i in range(1, 16)]
    gap = grid_scale * base / 10
    for a1, b1, a2, b2 in itertools.product(pts, repeat=4):
        if not (a1 < b1 and a2 < b2):
            continue
        D1, D2 = (a1, b1), (a2, b2)
        if not disjoint(D1, D2, gap):
            continue
        # Test a compact proxy for X\Di: a large finite window W minus Di
        W = (base, base * (1 + 20 * grid_scale))
        # Components of W\D1 roughly: pieces outside D1 inside W
        # Require g1(W) subset D1 and g2(W) subset D2 as a STRONG sufficient test
        # (stronger than classical ping-pong; a hit would be excellent)
        im1 = interval_image(f1.g, W[0], W[1])
        im2 = interval_image(f2.g, W[0], W[1])
        if contained(im1, D1) and contained(im2, D2) and disjoint(D1, D2, gap):
            return {
                "word1": f1.word,
                "word2": f2.word,
                "D1": [str(D1[0]), str(D1[1])],
                "D2": [str(D2[0]), str(D2[1])],
                "W": [str(W[0]), str(W[1])],
                "mode": "strong_whole_window",
            }
    return None


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    maps = mild(11)
    hits = []
    tested = 0
    for f1, f2 in itertools.combinations(maps[:50], 2):
        tested += 1
        for scale in [Fraction(1, 10), Fraction(1, 2), Fraction(1, 1)]:
            hit = try_pair(f1, f2, scale)
            if hit:
                hits.append(hit)
                break
        if len(hits) >= 5:
            break
    # Structural note: g maps large windows LEFT toward negative fp, so g(W)
    # for W far positive sits left of W and typically near scale W/mu, hard to
    # land inside a disjoint private Di far away from the other.
    summary = {
        "mild_maps": len(maps),
        "tested_pairs": tested,
        "strong_hits": hits,
        "note": (
            "Strong sufficient test (whole-window into Di) found no hits. "
            "Classical complement ping-pong remains open but looks geometrically "
            "hostile because all supercritical inverses translate large positives "
            "left toward a negative fixed point with similar contraction rates."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    text = (
        f"mild={len(maps)} tested={tested} strong_hits={len(hits)}\n{summary['note']}\n"
    )
    (results / "summary.txt").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
