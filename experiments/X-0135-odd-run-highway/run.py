#!/usr/bin/env python3
"""X-0135: inverse / forward odd-run highway ladder (new path).

Build nested residue constraints that force odd-runs (all-1 words) of
increasing length, lift by CRT (mod 2^L and optionally mod 3), and record
whether the realized positive integers exhibit sustained forward growth.

Also scan "evergreen" candidates: numbers that begin with many consecutive
odd shortcut steps, then measure post-highway survival (steps until below start).
"""

from __future__ import annotations

import json
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
    candidates = [0] if word[0] == "0" else [1]
    for k in range(1, len(word)):
        lifted = []
        half = 1 << k
        for c0 in candidates:
            for bit in (0, 1):
                r = c0 + bit * half
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
    a = word.count("1")
    L = len(word)
    return (3**a * n + B_of(word)) // (1 << L)


def crt(a1: int, m1: int, a2: int, m2: int) -> tuple[int, int] | None:
    """Solve x≡a1 (m1), x≡a2 (m2)."""
    g = gcd(m1, m2)
    if (a2 - a1) % g != 0:
        return None
    # simple incremental
    x = a1
    while x % m2 != a2 % m2:
        x += m1
        if x > a1 + m1 * m2:
            return None
    return x % (m1 * m2 // g), m1 * m2 // g


def odd_run_len(n: int, cap: int = 80) -> int:
    x = n
    k = 0
    while k < cap and x % 2 == 1:
        x = T(x)
        k += 1
    return k


def forward_stats(n: int, max_steps: int = 500) -> dict:
    x = n
    peak = n
    steps_above = 0
    first_below = None
    for s in range(1, max_steps + 1):
        x = T(x)
        if x > peak:
            peak = x
        if x >= n:
            steps_above += 1
        if first_below is None and x < n:
            first_below = s
        if x == 1 or x == 2:
            return {
                "steps": s,
                "peak": peak,
                "peak_ratio": peak / n,
                "first_below": first_below,
                "hit_trivial": True,
                "steps_above": steps_above,
                "final": x,
            }
    return {
        "steps": max_steps,
        "peak": peak,
        "peak_ratio": peak / n,
        "first_below": first_below,
        "hit_trivial": False,
        "steps_above": steps_above,
        "final": x,
    }


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    # 1) Pure odd-run residues: word 1^k, sample lifts, measure growth
    highway_rows = []
    for k in range(1, 21):
        w = "1" * k
        r = residue_of(w)
        mod = 1 << k
        best = None
        for q in range(0, 64):
            n = mod * q + r
            if n <= 0:
                continue
            n1 = apply_word(n, w)
            growth = n1 / n
            st = forward_stats(n1, max_steps=300)
            rec = {
                "k": k,
                "n": n,
                "after_highway": n1,
                "highway_growth": growth,
                "expected": (3 / 2) ** k,
                "post_peak_ratio": st["peak_ratio"],
                "first_below_from_n": None,
                "hit_trivial": st["hit_trivial"],
                "survived_300": not st["hit_trivial"] and st["final"] > n,
            }
            # full trajectory from n
            full = forward_stats(n, max_steps=400)
            rec["first_below_from_n"] = full["first_below"]
            rec["full_peak_ratio"] = full["peak_ratio"]
            rec["full_hit_trivial"] = full["hit_trivial"]
            if best is None or (
                rec["full_peak_ratio"] > best["full_peak_ratio"]
                or (
                    rec["survived_300"]
                    and not best.get("survived_300")
                )
            ):
                best = rec
        highway_rows.append(best)

    # 2) Nested ladder: chain odd-runs with CRT, optionally mod 3
    ladder = []
    # start with k=3 highway
    r, m = residue_of("111"), 8
    n_seed = r
    for stage, k in enumerate([3, 5, 7, 9, 11, 13]):
        w = "1" * k
        rw, mw = residue_of(w), 1 << k
        lifted = crt(r, m, rw, mw)
        if lifted is None:
            # try mod 3 constraint variants on previous
            ok = False
            for a3 in range(3):
                c1 = crt(r, m, a3, 3)
                if c1 is None:
                    continue
                c2 = crt(c1[0], c1[1], rw, mw)
                if c2 is None:
                    continue
                lifted = c2
                ok = True
                break
            if not ok:
                ladder.append({"stage": stage, "k": k, "ok": False})
                break
        r, m = lifted
        # pick positive representative and a few lifts
        stage_best = None
        for q in range(0, 40):
            n = r + q * m
            if n <= 1:
                continue
            st = forward_stats(n, max_steps=500)
            rec = {
                "stage": stage,
                "k": k,
                "mod": m,
                "n": n,
                "odd_run": odd_run_len(n),
                "peak_ratio": st["peak_ratio"],
                "first_below": st["first_below"],
                "hit_trivial": st["hit_trivial"],
                "final": st["final"],
            }
            if stage_best is None or rec["peak_ratio"] > stage_best["peak_ratio"]:
                stage_best = rec
        ladder.append({"stage": stage, "k": k, "ok": True, "best": stage_best})
        n_seed = stage_best["n"] if stage_best else n_seed

    # 3) Brute evergreen: scan n≡-1 mod 2^k for large k (odd-run rich)
    evergreen = []
    for k in (8, 12, 16, 20):
        r = (1 << k) - 1  # all-odd prefix likely
        # actually residue of 1^k:
        r = residue_of("1" * k)
        for q in range(1, 30):
            n = q * (1 << k) + r
            st = forward_stats(n, max_steps=800)
            evergreen.append(
                {
                    "k": k,
                    "n": n,
                    "odd_run": odd_run_len(n),
                    "peak_ratio": st["peak_ratio"],
                    "first_below": st["first_below"],
                    "hit_trivial": st["hit_trivial"],
                    "steps_above": st["steps_above"],
                }
            )
    evergreen.sort(key=lambda e: (-e["peak_ratio"], -(e["first_below"] or 0)))

    survivors = [h for h in highway_rows if h and h.get("survived_300")]
    summary = {
        "highway_rows": highway_rows,
        "ladder": ladder,
        "evergreen_top": evergreen[:25],
        "highway_survivors_300": len(survivors),
        "max_highway_peak": max((h["full_peak_ratio"] for h in highway_rows if h), default=0),
        "max_evergreen_peak": evergreen[0]["peak_ratio"] if evergreen else 0,
        "conclusion": (
            "Odd-run highway ladder: measure whether nested CRT odd-run "
            "constraints produce sustained forward growth / divergent survivors."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"highway_survivors_300={len(survivors)} "
        f"max_highway_peak={summary['max_highway_peak']:.3f} "
        f"max_evergreen_peak={summary['max_evergreen_peak']:.3f}",
    ]
    for h in highway_rows[::2]:
        if not h:
            continue
        lines.append(
            f"  k={h['k']} n={h['n']} hwy_g={h['highway_growth']:.3f} "
            f"peak={h['full_peak_ratio']:.3f} below@{h['first_below_from_n']} "
            f"trivial={h['full_hit_trivial']}"
        )
    for L in ladder:
        if not L.get("ok"):
            lines.append(f"  LADDER break at k={L.get('k')}")
            break
        b = L["best"]
        lines.append(
            f"  LADDER k={L['k']} mod~2^{b['mod'].bit_length()-1} n={b['n']} "
            f"odd_run={b['odd_run']} peak={b['peak_ratio']:.3f} "
            f"below@{b['first_below']}"
        )
    for e in evergreen[:5]:
        lines.append(
            f"  EVER n={e['n']} k={e['k']} odd_run={e['odd_run']} "
            f"peak={e['peak_ratio']:.3f} below@{e['first_below']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
