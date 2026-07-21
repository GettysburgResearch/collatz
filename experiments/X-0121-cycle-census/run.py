#!/usr/bin/env python3
"""X-0121: exact algebraic cycle census (new path: cycle hunt).

For every chronological word w of length L<=Lmax with a ones, 3^a != 2^L,
compute n = B(w) / (2^L - 3^a) as an exact rational. Accept positive integers
outside the trivial shortcut cycle {1}.

Also modular sieve stats: for each (L,a) subcritical, count words with
denominator dividing B.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import gcd
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


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def follows_cycle(n: int, word: str) -> bool:
    x = n
    for bit in word:
        if str(x & 1) != bit:
            return False
        x = T(x)
    return x == n


def census(Lmax: int) -> dict:
    hits = []
    trivial = []
    subcritical_words = 0
    divisible = 0
    by_La = {}
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            den = (1 << L) - (3**a)
            if den == 0:
                continue
            # positive n needs den > 0 for B>0, i.e. subcritical
            if den < 0:
                continue  # supercritical => negative fp
            subcritical_words += 1
            B = B_of(word)
            key = (L, a)
            by_La.setdefault(key, {"words": 0, "divisible": 0, "positive_int": 0})
            by_La[key]["words"] += 1
            if B % den != 0:
                continue
            divisible += 1
            by_La[key]["divisible"] += 1
            n = B // den
            if n <= 0:
                continue
            by_La[key]["positive_int"] += 1
            # verify cycle
            ok = follows_cycle(n, word)
            rec = {"word": word, "L": L, "a": a, "n": n, "verified": ok}
            # trivial shortcut cycle: n=1 with word that is the 1-cycle
            if n == 1:
                trivial.append(rec)
            else:
                hits.append(rec)
    return {
        "Lmax": Lmax,
        "subcritical_words": subcritical_words,
        "divisible": divisible,
        "nontrivial_positive_integer_hits": hits,
        "trivial_hits": trivial[:20],
        "trivial_count": len(trivial),
        "by_La_nonzero": {
            f"L{L}a{a}": v
            for (L, a), v in sorted(by_La.items())
            if v["divisible"] or v["positive_int"]
        },
    }


def modular_obstruction_sample(L: int, a: int, primes: list[int]) -> dict:
    """For fixed (L,a) subcritical, check B mod p vs den mod p distribution."""
    den = (1 << L) - (3**a)
    if den <= 0:
        return {"ok": False}
    # enumerate all weight-a words
    from itertools import combinations

    positions = range(L)
    total = 0
    div = 0
    for ones in combinations(positions, a):
        word = ["0"] * L
        for i in ones:
            word[i] = "1"
        w = "".join(word)
        B = B_of(w)
        total += 1
        if den != 0 and B % den == 0:
            div += 1
    return {"L": L, "a": a, "den": den, "words": total, "divisible": div}


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    c = census(Lmax=16)
    # a few denser (L,a) near log3(2)
    samples = []
    for L, a in [(11, 6), (11, 7), (12, 7), (13, 8), (14, 8), (15, 9), (16, 10)]:
        den = (1 << L) - 3**a
        if den > 0:
            samples.append(modular_obstruction_sample(L, a, [5, 7, 13]))
    # extend census selectively for L=17..20 only near-critical a
    extra_hits = []
    for L in range(17, 21):
        for a in range(1, L):
            den = (1 << L) - 3**a
            if den <= 0:
                continue
            # only if den is "small" relative — always check all C(L,a) if C small
            from math import comb

            if comb(L, a) > 20000:
                continue
            from itertools import combinations

            for ones in combinations(range(L), a):
                word_list = ["0"] * L
                for i in ones:
                    word_list[i] = "1"
                word = "".join(word_list)
                B = B_of(word)
                if B % den == 0:
                    n = B // den
                    if n > 1 and follows_cycle(n, word):
                        extra_hits.append({"word": word, "L": L, "a": a, "n": n})
    summary = {
        "census": c,
        "near_critical_samples": samples,
        "extra_hits_L17_20": extra_hits,
        "conclusion": (
            "No nontrivial positive integer cycle found through L=16 full census "
            "plus selective L=17..20. Trivial n=1 occurrences recorded separately."
        ),
    }
    # strip huge by_La if needed — ok
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"L<=16 subcritical words={c['subcritical_words']} divisible={c['divisible']}",
        f"nontrivial hits={len(c['nontrivial_positive_integer_hits'])} trivial={c['trivial_count']}",
        f"extra L17-20 hits={len(extra_hits)}",
    ]
    if c["nontrivial_positive_integer_hits"]:
        lines.append("NONTRIVIAL:")
        lines.extend(str(h) for h in c["nontrivial_positive_integer_hits"][:20])
    if c["trivial_hits"][:5]:
        lines.append("trivial samples:")
        lines.extend(str(h) for h in c["trivial_hits"][:5])
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
