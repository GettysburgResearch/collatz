#!/usr/bin/env python3
"""X-0125: heteroclinic probe using the -5 cycle template.

Shortcut cycle: -5 → -7 → -10 → -5 with parity word of period 3?
Check: T(-5)=(-15+1)/2=-7; T(-7)=(-21+1)/2=-10; T(-10)=-5.
Parities of -5,-7,-10 in two's complement sense for odds/evens:
-5 odd, -7 odd, -10 even → word 110 (chronological).

Rational fp of (110)^ω should be -5.
Measure: CRT gluing of deep cylinders of (110)^k with supercritical
excursions; track v2(n - (-5)) after return attempts and growth.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def T(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return (3 * n + 1) // 2


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


def fp(word: str) -> Fraction:
    L = len(word)
    a = word.count("1")
    B = B_of(word)
    return Fraction(-B, 3**a - (1 << L))


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    template = "110"
    assert fp(template) == -5
    # verify cycle on negatives
    x = -5
    for bit in template:
        assert (x % 2 == 1) == (bit == "1") or (x % 2 == 0) == (bit == "0")
        # careful with python % for negatives: (-5)%2 == 1 in Python
        x = T(x)
    assert x == -5

    excursions = ["1", "11", "111", "101", "1111", "1111010"]
    rows = []
    for ex in excursions:
        Le = len(ex)
        re = residue_of(ex)
        for m in (6, 9, 12, 15, 18, 21):
            reps = (m + 2) // 3
            prefix = (template * (reps + 2))[:m]
            rt = residue_of(prefix)
            # CRT powers of 2
            if m >= Le:
                if rt % (1 << Le) != re:
                    rows.append({"ex": ex, "m": m, "ok": False, "reason": "incompatible"})
                    continue
                mod, r = 1 << m, rt
            else:
                if re % (1 << m) != rt:
                    rows.append({"ex": ex, "m": m, "ok": False, "reason": "incompatible"})
                    continue
                mod, r = 1 << Le, re
            best = None
            for q in range(0, 64):
                n0 = mod * q + r
                # prefer positive
                if n0 <= 0:
                    continue
                if n0 % (1 << Le) != re:
                    continue
                n1 = apply_word(n0, ex)
                growth = n1 / n0
                # 2-adic distance to -5
                d0 = v2(n0 - (-5))
                d1 = v2(n1 - (-5))
                # how many template periods remain possible
                x = n1
                periods = 0
                tr = residue_of(template)
                while x % 8 == tr and periods < 40:  # 2^3
                    x = apply_word(x, template)
                    periods += 1
                rec = {
                    "n0": n0,
                    "n1": n1,
                    "growth": growth,
                    "v2_n0_plus5": d0,
                    "v2_n1_plus5": d1,
                    "depth_delta": d1 - d0,
                    "periods_after": periods,
                }
                if best is None or (
                    growth > 1
                    and (
                        best["growth"] <= 1
                        or d1 > best["v2_n1_plus5"]
                        or (d1 == best["v2_n1_plus5"] and growth > best["growth"])
                    )
                ):
                    best = rec
            rows.append(
                {
                    "ex": ex,
                    "m": m,
                    "ok": best is not None,
                    "best": best,
                    "fp": -5,
                }
            )

    growing = [
        r
        for r in rows
        if r.get("ok") and r.get("best") and r["best"]["growth"] > 1
    ]
    # destruction: cases where growth>1 but v2 depth falls
    destroy = [r for r in growing if r["best"]["depth_delta"] < 0]
    preserve = [r for r in growing if r["best"]["depth_delta"] >= 0]
    summary = {
        "template": template,
        "fp": -5,
        "rows": rows,
        "growing": len(growing),
        "depth_destroyed": len(destroy),
        "depth_preserved_or_gained": len(preserve),
        "best_preserve": sorted(
            preserve,
            key=lambda r: (-r["best"]["v2_n1_plus5"], -r["best"]["growth"]),
        )[:10],
        "best_destroy": sorted(
            destroy, key=lambda r: (r["best"]["depth_delta"], -r["best"]["growth"])
        )[:10],
        "conclusion": (
            "For -5 template (110): record whether supercritical excursions can "
            "grow archimedean size without destroying v2(n+5) shadowing depth."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"growing={len(growing)} destroyed_depth={len(destroy)} preserved={len(preserve)}",
    ]
    for r in summary["best_preserve"][:5]:
        b = r["best"]
        lines.append(
            f"  PRESERVE ex={r['ex']} m={r['m']} growth={b['growth']:.3f} "
            f"v2:{b['v2_n0_plus5']}->{b['v2_n1_plus5']} delta={b['depth_delta']}"
        )
    for r in summary["best_destroy"][:5]:
        b = r["best"]
        lines.append(
            f"  DESTROY  ex={r['ex']} m={r['m']} growth={b['growth']:.3f} "
            f"v2:{b['v2_n0_plus5']}->{b['v2_n1_plus5']} delta={b['depth_delta']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
