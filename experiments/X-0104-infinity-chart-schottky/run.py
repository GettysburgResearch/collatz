#!/usr/bin/env python3
"""X-0104: Schottky search in the chart at infinity t=1/x.

Forward supercritical map f(x)=μx+β becomes
    h(t)=t/(μ + β t)
near t=0. Search for disjoint compact intervals in (0,ε] forming a classical
ping-pong for two or more such Möbius maps.
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
class HMap:
    word: str
    mu: Fraction
    beta: Fraction

    def h(self, t: Fraction) -> Fraction:
        return t / (self.mu + self.beta * t)

    def h_interval(self, a: Fraction, b: Fraction) -> tuple[Fraction, Fraction]:
        ha, hb = self.h(a), self.h(b)
        return (ha, hb) if ha <= hb else (hb, ha)


def mild_maps(Lmax: int) -> list[HMap]:
    out = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            mu = Fraction(3**a, 1 << L)
            if Fraction(1, 1) < mu <= Fraction(4, 3):  # very mild
                beta = Fraction(B_of(word), 1 << L)
                out.append(HMap(word, mu, beta))
    out.sort(key=lambda m: float(m.mu))
    return out


def disjoint(ints: list[tuple[Fraction, Fraction]], gap: Fraction) -> bool:
    for (a1, b1), (a2, b2) in itertools.combinations(ints, 2):
        if b1 + gap <= a2 or b2 + gap <= a1:
            continue
        return False
    return True


def try_pair(m1: HMap, m2: HMap, eps: Fraction, split: Fraction, gap: Fraction):
    """Try I1=(0,split], I2=[split+gap, eps] — note I1 contains 0-neighborhood.

    Better: both intervals away from 0:
    I1=[a1,b1], I2=[a2,b2] inside (0,eps].
    """
    # Grid search on endpoints
    grid = []
    n = 12
    for i in range(1, n):
        grid.append(eps * Fraction(i, n))
    best = None
    for a1, b1, a2, b2 in itertools.product(grid, repeat=4):
        if not (0 < a1 < b1 < a2 < b2 <= eps):
            continue
        I1, I2 = (a1, b1), (a2, b2)
        # Need h1(I1∪I2) ⊂ I1 and h2(I1∪I2) ⊂ I2
        imgs1 = [m1.h_interval(*I1), m1.h_interval(*I2)]
        imgs2 = [m2.h_interval(*I1), m2.h_interval(*I2)]
        union1_lo = min(imgs1[0][0], imgs1[1][0])
        union1_hi = max(imgs1[0][1], imgs1[1][1])
        union2_lo = min(imgs2[0][0], imgs2[1][0])
        union2_hi = max(imgs2[0][1], imgs2[1][1])
        if union1_lo >= I1[0] and union1_hi <= I1[1] and union2_lo >= I2[0] and union2_hi <= I2[1]:
            return {
                "word1": m1.word,
                "word2": m2.word,
                "mu": [str(m1.mu), str(m2.mu)],
                "I1": [str(I1[0]), str(I1[1])],
                "I2": [str(I2[0]), str(I2[1])],
                "eps": str(eps),
            }
    return best


def nested_image_obstruction(maps: list[HMap], eps: Fraction) -> dict:
    """h maps (0,eps] to (0, h(eps)], nested at 0 — images not separable from 0."""
    data = []
    for m in maps[:20]:
        he = m.h(eps)
        data.append({"word": m.word, "h(eps)": str(he), "mu": str(m.mu)})
    # Prove: h((0,eps])=(0,h(eps)], so any family of images intersects every
    # left neighborhood of 0; classical disjoint-compact ping-pong using images
    # of a common neighborhood of 0 is impossible.
    return {
        "note": (
            "Each h((0,eps])=(0,h(eps)] contains a left neighborhood of 0; "
            "images of any 0-neighborhood are nested/overlapping at 0, so "
            "disjoint-image IFS ping-pong cannot use a domain containing a "
            "punctured neighborhood of 0 shared by all generators."
        ),
        "samples": data,
    }


def annulus_search(maps: list[HMap]) -> dict:
    hits = []
    tested = 0
    for eps in [Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000), Fraction(1, 10**6)]:
        for m1, m2 in itertools.combinations(maps[:40], 2):
            tested += 1
            hit = try_pair(m1, m2, eps, eps / 2, eps / 100)
            if hit:
                hits.append(hit)
                if len(hits) >= 5:
                    return {"tested": tested, "hits": hits}
    return {"tested": tested, "hits": hits}


def endpoint_monotonicity_scan(maps: list[HMap]) -> dict:
    """Check whether h maps can send a right annulus into a left annulus.

    h is increasing and h(t)<t/μ < t for t>0. So h moves every point left toward 0.
    Thus h cannot map a right interval I2 into itself if we also need to cover
    points from a left interval — quantitative scan below.
    """
    failures_self = 0
    checks = 0
    for m in maps[:50]:
        for a in [Fraction(1, 10**k) for k in range(1, 8)]:
            b = 2 * a
            checks += 1
            lo, hi = m.h_interval(a, b)
            # self-preservation of [a,b]?
            if lo >= a and hi <= b:
                failures_self += 1  # unexpected success
    return {
        "annulus_self_preservation_checks": checks,
        "unexpected_self_preservations": failures_self,
        "lemma_hint": (
            "h(t)=t/(μ+βt)<t/μ<t for μ>1,t>0, so h(a)<a and no compact "
            "interval [a,b]⊂(0,∞) is preserved by a single supercritical h."
        ),
    }


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    maps = mild_maps(Lmax=12)
    nest = nested_image_obstruction(maps, Fraction(1, 1000))
    scan = endpoint_monotonicity_scan(maps)
    ann = annulus_search(maps)
    summary = {
        "mild_maps": len(maps),
        "nested_obstruction": nest,
        "annulus_scan": scan,
        "annulus_search": ann,
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"mild maps={len(maps)}",
        scan["lemma_hint"],
        nest["note"],
        f"annulus self-preservation unexpected successes={scan['unexpected_self_preservations']}/{scan['annulus_self_preservation_checks']}",
        f"annulus pair search tested={ann['tested']} hits={len(ann['hits'])}",
    ]
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
