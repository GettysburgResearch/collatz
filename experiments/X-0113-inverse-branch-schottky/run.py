#!/usr/bin/env python3
"""X-0113: inverse-branch integer Schottky probe.

Inverse branches of the shortcut map T:
  g0(x) = 2x                         (always)
  g1(x) = (2x - 1)/3                 when this is an odd positive integer

A divergent forward orbit starting at n0 is equivalent to n0 lying on an
infinite forward path. Constructively, one may try to build large numbers by
inverse walks that end at a small seed — but a positive divergent counterexample
requires an infinite FORWARD path from a finite seed. Equivalently: the seed
is the limit of a coherent nested sequence of inverse images along an infinite
forward itinerary (the 2-adic coding). This experiment:

1) maps the inverse graph on odds / positives;
2) searches for finite inverse ping-pong pairs (disjoint image sets) among
   depth-limited inverse words;
3) tests whether any inverse IFS with mixed g0/g1 yields a positive integer
   in its attractor other than known cycles.

Also records the elementary fact that pure g1^k itineraries converge to -1.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def g0(x: int) -> int:
    return 2 * x


def g1(x: int) -> int | None:
    num = 2 * x - 1
    if num % 3 != 0:
        return None
    m = num // 3
    if m > 0 and m % 2 == 1 and T(m) == x:
        return m
    return None


def inverse_preimages(x: int) -> list[tuple[str, int]]:
    outs = [("0", g0(x))]
    m = g1(x)
    if m is not None:
        outs.append(("1", m))
    return outs


def inverse_words_from(seed: int, depth: int) -> list[tuple[str, int]]:
    """All inverse images at exact depth (words over {0,1} applied as g's)."""
    layer = [("", seed)]
    for _ in range(depth):
        nxt = []
        for w, x in layer:
            for b, y in inverse_preimages(x):
                nxt.append((b + w, y))  # b applied last in forward time? 
                # forward: from y, first bit is b then follows w to seed.
        layer = nxt
    return layer


def pingpong_disjoint_test(depth: int, window: int) -> dict:
    """At a depth, partition inverse images by first forward bit and see if
    the integer sets in a window are disjoint (they should be: different residues).
    """
    # From seed 1, build depth-d inverse cloud
    cloud = inverse_words_from(1, depth)
    by_first = {"0": [], "1": []}
    for w, n in cloud:
        if n <= window and w:
            by_first[w[0]].append(n)
    s0, s1 = set(by_first["0"]), set(by_first["1"])
    return {
        "depth": depth,
        "window": window,
        "cloud": len(cloud),
        "|S0|": len(s0),
        "|S1|": len(s1),
        "overlap": len(s0 & s1),
        "note": "Forward-bit cylinders are always disjoint on integers; this is coding, not a new Schottky.",
    }


def real_inverse_ifs_obstruction() -> dict:
    """g0(x)=2x expands; g1(x)=(2x-1)/3 contracts with slope 2/3.
    For a compact positive I to be preserved by both, g0(I)⊂I is impossible
    unless I empty/unbounded: g0([a,b])=[2a,2b] escapes any bounded I.
    So mixed inverse IFS on a compact positive interval cannot include g0.
    Pure g1-IFS: unique attractor fp of g1 is solution x=(2x-1)/3 ⇒ x=-1.
    """
    # fixed point g1: x=(2x-1)/3 => 3x=2x-1 => x=-1
    # fixed point g0: only 0
    return {
        "g0_compact_obstruction": "g0([a,b])=[2a,2b] not subset of bounded [a,b]",
        "g1_attractor": -1,
        "conclusion": (
            "No compact positive inverse IFS using {g0,g1}. Pure g1 attracts to -1. "
            "Inverse Schottky on positives requires unbounded domains or non-IFS formats."
        ),
    }


def nested_cylinder_integers(word: str) -> dict:
    """Integers following a finite forward word: one residue class.
    Infinite word => at most one 2-adic."""
    # verify class size
    L = len(word)
    # count n < 2^{L+3} following word
    count = 0
    sample = []
    bound = 1 << (L + 4)
    for n in range(1, bound):
        x = n
        ok = True
        for bit in word:
            if str(x & 1) != bit:
                ok = False
                break
            x = T(x)
        if ok:
            count += 1
            if len(sample) < 5:
                sample.append(n)
    return {"word": word, "L": L, "count_below": count, "expected_approx": bound // (1 << L), "sample": sample}


def try_build_divergent_by_inverse_ladder(max_depth: int = 20) -> dict:
    """Heuristic: start from a large odd, walk forward, try to see if we can
    find a pattern of inverse branches that would close a Schottky loop.
    Also: from seed 1, the inverse tree is the entire positive integers that
    eventually reach 1 — useless for counterexamples. From a seed not reaching
    1 we'd need a different component — which is the conjecture.
    """
    # Measure branching factor of inverse tree
    branch_stats = []
    for seed in [1, 5, 7, 27]:
        total = 1
        layer = [seed]
        growth = []
        for d in range(max_depth):
            nxt = []
            for x in layer:
                for _, y in inverse_preimages(x):
                    nxt.append(y)
            growth.append(len(nxt))
            layer = nxt
            total += len(nxt)
            if len(layer) > 50000:
                break
        branch_stats.append({"seed": seed, "growth": growth[:15], "layers": len(growth)})
    return {
        "branch_stats": branch_stats,
        "note": (
            "Inverse tree from 1 enumerates Collatz precursors of 1 (not counterexamples). "
            "A counterexample component would be an inverse tree not feeding into 1."
        ),
    }


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    obs = real_inverse_ifs_obstruction()
    ping = [pingpong_disjoint_test(d, 10**6) for d in (6, 10, 12)]
    cyl = nested_cylinder_integers("1011011")
    ladder = try_build_divergent_by_inverse_ladder(12)
    summary = {
        "real_ifs": obs,
        "cylinder_disjoint": ping,
        "cylinder_count": cyl,
        "inverse_tree": ladder,
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        obs["conclusion"],
        f"g1 attractor={obs['g1_attractor']}",
        f"cylinder word={cyl['word']} count={cyl['count_below']} ~expected={cyl['expected_approx']}",
        "inverse tree growth from 1:",
        str(ladder["branch_stats"][0]["growth"][:12]),
    ]
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
