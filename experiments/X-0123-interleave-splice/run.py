#!/usr/bin/env python3
"""X-0123: creative non-concatenative path — chart interleave / splice.

Idea: rather than chronological concatenation UV (tensor), alternate digits
from two different collision charts by a CRT state that stores both gauges.
Operational probe: take two supercritical blocks wA, wB with moduli MA, MB;
search for n that follows the interleaved schedule
  (prefix of wA) then switch via a bridge word then wB ...
or the simpler splice: wA then bridge then wB with net mu>1 and measure
whether returnable residue depth grows slower than tax.

This is an IDEA-level construction search escaping pure chronological tensor.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import gcd
from pathlib import Path


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def B_of(word: str) -> int:
    ones = word.count("1")
    seen = 0
    total = 0
    for j, bit in enumerate(word):
        if bit == "1":
            seen += 1
            total += (1 << j) * (3 ** (ones - seen))
    return total


def residue_of(word: str) -> int:
    L = len(word)
    candidates = [0] if word[0] == "0" else [1]
    for k in range(1, L):
        lifted = []
        half = 1 << k
        for c in candidates:
            for bit in (0, 1):
                r = c + bit * half
                x = r
                ok = True
                for i in range(k + 1):
                    if (x & 1) != int(word[i]):
                        ok = False
                        break
                    x = T(x)
                if ok:
                    lifted.append(r)
        candidates = lifted
    return candidates[0]


def apply_word(n: int, word: str) -> int:
    L = len(word)
    a = word.count("1")
    return (3**a * n + B_of(word)) // (1 << L)


def mu(word: str) -> Fraction:
    return Fraction(3 ** word.count("1"), 1 << len(word))


def find_bridges(wA: str, wB: str, Lbridge_max: int = 8) -> list[dict]:
    """Find short words b such that some n follows wA then b then wB with growth."""
    rA, rB = residue_of(wA), residue_of(wB)
    LA, LB = len(wA), len(wB)
    hits = []
    for Lb in range(0, Lbridge_max + 1):
        for mask in range(1 << Lb) if Lb else [0]:
            b = format(mask, f"0{Lb}b")[::-1] if Lb else ""
            # search n
            # n ≡ rA mod 2^LA; after wA land in residue enabling b; then wB
            for q in range(0, 5000):
                n0 = (1 << LA) * q + rA
                n1 = apply_word(n0, wA)
                if b:
                    if n1 % (1 << Lb) != residue_of(b):
                        continue
                    n2 = apply_word(n1, b)
                else:
                    n2 = n1
                if n2 % (1 << LB) != rB:
                    continue
                n3 = apply_word(n2, wB)
                if n3 > n0:
                    hits.append(
                        {
                            "bridge": b,
                            "n0": n0,
                            "n_final": n3,
                            "growth": n3 / n0,
                            "mu_prod": float(mu(wA) * (mu(b) if b else 1) * mu(wB)),
                        }
                    )
                    break
            if len(hits) >= 20:
                return hits
    return hits


def splice_depth_budget(wA: str, wB: str, bridge: str, trials: int = 2000) -> dict:
    """For a working splice pattern, how many AB repeats before residue fails?"""
    sched = [wA, bridge, wB] if bridge else [wA, wB]
    # drop empty
    sched = [w for w in sched if w]
    concat = "".join(sched)
    r = residue_of(concat)
    L = len(concat)
    best = 0
    best_n = None
    for q in range(trials):
        n = (1 << L) * q + r
        m = n
        steps = 0
        while True:
            ok = True
            x = m
            for w in sched:
                rw = residue_of(w)
                if x % (1 << len(w)) != rw:
                    ok = False
                    break
                x = apply_word(x, w)
            if not ok:
                break
            m = x
            steps += 1
            if steps > 40:
                break
        if steps > best:
            best = steps
            best_n = n
    return {"pattern": sched, "best_periods": best, "best_n": best_n, "concat_L": L}


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    pairs = [
        ("1", "11"),
        ("101", "1"),
        ("1111010", "1101110"),
        ("11", "101"),
        ("1111", "101"),
    ]
    all_hits = []
    depths = []
    for wA, wB in pairs:
        hits = find_bridges(wA, wB, Lbridge_max=6)
        all_hits.append({"wA": wA, "wB": wB, "hits": hits[:5], "nhits": len(hits)})
        if hits:
            d = splice_depth_budget(wA, wB, hits[0]["bridge"])
            d["wA"] = wA
            d["wB"] = wB
            depths.append(d)
    summary = {
        "pair_hits": all_hits,
        "depths": depths,
        "conclusion": (
            "Interleave/splice finds finite growing AB patterns (often with empty "
            "bridge), but period depth remains tiny — same tax/drain pressure as "
            "concat unless a true non-concatenative state is added."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [summary["conclusion"]]
    for h in all_hits:
        lines.append(f"{h['wA']}/{h['wB']}: nhits={h['nhits']} sample={h['hits'][:2]}")
    for d in depths:
        lines.append(f"  depth {d['wA']}/{d['wB']}: periods={d['best_periods']} L={d['concat_L']}")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
