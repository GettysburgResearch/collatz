#!/usr/bin/env python3
"""X-0137: 3-adic depth probe (bootstrap D-ADIC3).

Find small integers c where the shortcut map has a short cycle in the
rationals with 3-adic interest, and measure whether v3(n-c) is preserved
or burned under expanding excursions — the 3-adic dual of L-0114.
"""

from __future__ import annotations

import json
from fractions import Fraction
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


def apply_word(n: int, word: str) -> int:
    a = word.count("1")
    L = len(word)
    return (3**a * n + B_of(word)) // (1 << L)


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


def v3(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def fp(word: str) -> Fraction:
    L = len(word)
    a = word.count("1")
    return Fraction(-B_of(word), 3**a - (1 << L))


def follows(n: int, w: str) -> bool:
    x = n
    for bit in w:
        if (x & 1) != int(bit):
            return False
        x = T(x)
    return True


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    # rational fixed points of short words; keep those with denom power of 3
    # or integer c with interesting v3
    fps = []
    for L in range(1, 10):
        for mask in range(1 << L):
            w = format(mask, f"0{L}b")[::-1]
            if "1" not in w:
                continue
            a = w.count("1")
            den = 3**a - (1 << L)
            if den == 0:
                continue
            f = Fraction(-B_of(w), den)
            fps.append({"word": w, "fp": f, "int": f.denominator == 1})

    int_fps = [f for f in fps if f["int"]]
    # also test c = 0 as 3-adic origin, and integers near multiples of high 3-powers
    targets = sorted({int(f["fp"]) for f in int_fps} | {0, -1, 1, -5, -17})

    rows = []
    for c in targets:
        for w in ["1", "11", "111", "10", "01", "110"]:
            # kappa3 analog: not the same — measure empirical v3 burn
            re = residue_of(w)
            L = len(w)
            best = None
            for q in range(0, 5000):
                n = re + q * (1 << L)
                if n <= 0:
                    continue
                if not follows(n, w):
                    continue
                d0 = v3(n - c)
                if d0 < 2:
                    continue
                n1 = apply_word(n, w)
                d1 = v3(n1 - c)
                growth = n1 / n
                rec = {
                    "c": c,
                    "w": w,
                    "n": n,
                    "v3_before": d0,
                    "v3_after": d1,
                    "delta": d1 - d0,
                    "growth": growth,
                }
                if best is None or (growth > 1 and d1 >= best["v3_after"]):
                    best = rec
            if best:
                rows.append(best)

    growing_preserve = [
        r for r in rows if r["growth"] > 1 and r["delta"] >= 0
    ]
    growing_burn = [r for r in rows if r["growth"] > 1 and r["delta"] < 0]

    summary = {
        "integer_fixed_points": [
            {"word": f["word"], "fp": int(f["fp"])} for f in int_fps
        ][:40],
        "rows": rows,
        "growing_preserve_v3": growing_preserve[:20],
        "growing_burn_v3": growing_burn[:20],
        "counts": {
            "rows": len(rows),
            "grow_preserve": len(growing_preserve),
            "grow_burn": len(growing_burn),
        },
        "conclusion": (
            "Bootstrap 3-adic depth probe: search growing excursions that "
            "preserve v3(n-c) for small integer targets c."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"rows={len(rows)} grow_preserve={len(growing_preserve)} "
        f"grow_burn={len(growing_burn)} int_fps={len(int_fps)}",
    ]
    for r in growing_preserve[:6]:
        lines.append(
            f"  KEEP c={r['c']} w={r['w']} g={r['growth']:.3f} "
            f"v3:{r['v3_before']}->{r['v3_after']}"
        )
    for r in growing_burn[:4]:
        lines.append(
            f"  BURN c={r['c']} w={r['w']} g={r['growth']:.3f} "
            f"v3:{r['v3_before']}->{r['v3_after']}"
        )
    if not growing_preserve:
        lines.append("  (no grow+preserve v3 events in scan)")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
