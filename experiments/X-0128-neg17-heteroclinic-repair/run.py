#!/usr/bin/env python3
"""X-0128: -17 heteroclinic with mild/subcritical depth-repair (model B).

Template: 11110111000, fp = -17.

Methodological note
-------------------
Prior probe X-0125 used model A: require n0 to lie in a template cylinder AND
have the excursion as its *immediate* parity prefix. That forces excursion
words to be compatible with the template prefix, so mild words starting with
`0` are vacuously impossible for templates starting with `1`.

Model B (this experiment):
  1. Take n0 in a deep template cylinder (shadow depth m).
  2. Apply k full template periods (stay on cycle chart).
  3. From the image, apply an excursion word (deviation).
  4. Measure genuine v2(n+17) before deviation and after excursion.

This is the correct "shadow then leave" heteroclinic move.
Also tests grow-then-repair sandwiches after a shadow prefix.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import log
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
    return Fraction(-B_of(word), 3**a - (1 << L))


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def follows(n: int, word: str) -> bool:
    x = n
    for bit in word:
        if (x & 1) != int(bit):
            return False
        x = T(x)
    return True


LOG32 = log(2) / log(3)


def kind(word: str) -> str:
    d = word.count("1") / len(word)
    if d > LOG32 + 1e-12:
        return "super"
    if d < LOG32 - 1e-12:
        return "sub"
    return "critical"


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    template = "11110111000"
    target = -17
    Lt = len(template)
    tr = residue_of(template)
    assert fp(template) == -17
    x = -17
    for bit in template:
        assert (x % 2) == int(bit)
        x = T(x)
    assert x == -17

    super_ex = ["1", "11", "111", "1111", "11111", "1011", "1101"]
    mild_ex = ["0", "00", "000", "10", "010", "0010", "0001", "1000", "0100", "00100"]
    depths = [11, 22, 33, 44]
    # after shadowing m bits worth of template, apply k extra full periods then ex
    extra_periods = [0, 1, 2]

    rows = []
    for m in depths:
        reps = (m + Lt - 1) // Lt
        prefix = (template * (reps + 2))[:m]
        rt = residue_of(prefix)
        mod = 1 << m
        for q in range(0, 48):
            n0 = mod * q + rt
            if n0 <= 0:
                continue
            d0 = v2(n0 - target)
            for k in extra_periods:
                n_shadow = n0
                for _ in range(k):
                    n_shadow = apply_word(n_shadow, template)
                d_shadow = v2(n_shadow - target)
                for ex in super_ex + mild_ex:
                    if not follows(n_shadow, ex):
                        continue
                    n1 = apply_word(n_shadow, ex)
                    if n1 == 0:
                        continue
                    d1 = v2(n1 - target)
                    growth = n1 / n_shadow if n_shadow else 0
                    # periods of template still possible after
                    x = n1
                    periods = 0
                    while x % (1 << Lt) == tr and periods < 40:
                        x = apply_word(x, template)
                        periods += 1
                    rows.append(
                        {
                            "m": m,
                            "q": q,
                            "k": k,
                            "ex": ex,
                            "kind": kind(ex),
                            "n0": n0,
                            "n_shadow": n_shadow,
                            "n1": n1,
                            "growth": growth,
                            "v2_cylinder": d0,
                            "v2_before_ex": d_shadow,
                            "v2_after": d1,
                            "depth_delta": d1 - d_shadow,
                            "periods_after": periods,
                        }
                    )

    # best stats per (ex,m,k)
    def best_by(pred, key):
        bag = {}
        for r in rows:
            if not pred(r):
                continue
            key_id = (r["ex"], r["m"], r["k"])
            if key_id not in bag or key(r) > key(bag[key_id]):
                bag[key_id] = r
        return list(bag.values())

    growing = [r for r in rows if r["growth"] > 1]
    grow_destroy = [r for r in growing if r["depth_delta"] < 0]
    grow_preserve = [r for r in growing if r["depth_delta"] >= 0]
    mild = [r for r in rows if r["kind"] == "sub"]
    mild_repair = [r for r in mild if r["depth_delta"] > 0]
    mild_preserve = [r for r in mild if r["depth_delta"] >= 0]

    # sandwiches: from shadowed point, grow_ex then repair_ex
    sandwiches = []
    for m in [22, 33, 44]:
        reps = (m + Lt - 1) // Lt
        prefix = (template * (reps + 2))[:m]
        rt = residue_of(prefix)
        mod = 1 << m
        for q in range(0, 48):
            n0 = mod * q + rt
            if n0 <= 0:
                continue
            n_shadow = apply_word(n0, template)  # one period then deviate
            for g in ["1", "11", "111"]:
                if not follows(n_shadow, g):
                    continue
                mid = apply_word(n_shadow, g)
                for rep in ["0", "00", "000", "10", "010", "0010"]:
                    if not follows(mid, rep):
                        continue
                    n1 = apply_word(mid, rep)
                    if n_shadow == 0 or n1 == 0:
                        continue
                    sandwiches.append(
                        {
                            "m": m,
                            "grow_ex": g,
                            "repair_ex": rep,
                            "n_shadow": n_shadow,
                            "mid": mid,
                            "n1": n1,
                            "growth_net": n1 / n_shadow,
                            "v2": [
                                v2(n_shadow - target),
                                v2(mid - target),
                                v2(n1 - target),
                            ],
                            "depth_delta_net": v2(n1 - target) - v2(n_shadow - target),
                        }
                    )

    sand_good = [
        s for s in sandwiches if s["growth_net"] > 1 and s["depth_delta_net"] >= 0
    ]
    sand_repair_only = [s for s in sandwiches if s["depth_delta_net"] > 0]

    # representatives
    best_grow_destroy = sorted(
        best_by(lambda r: r["growth"] > 1 and r["depth_delta"] < 0, lambda r: (r["growth"],)),
        key=lambda r: (r["depth_delta"], -r["growth"]),
    )[:10]
    best_grow_preserve = sorted(
        grow_preserve, key=lambda r: (-r["depth_delta"], -r["growth"])
    )[:10]
    best_mild_repair = sorted(mild_repair, key=lambda r: -r["depth_delta"])[:10]

    summary = {
        "template": template,
        "fp": target,
        "model": "B_shadow_then_deviate",
        "rows": len(rows),
        "growing": len(growing),
        "grow_destroy": len(grow_destroy),
        "grow_preserve": len(grow_preserve),
        "mild": len(mild),
        "mild_repair": len(mild_repair),
        "mild_preserve": len(mild_preserve),
        "sandwiches": len(sandwiches),
        "sandwiches_grow_preserve_depth": len(sand_good),
        "sandwiches_any_repair": len(sand_repair_only),
        "best_grow_destroy": best_grow_destroy,
        "best_grow_preserve": best_grow_preserve,
        "best_mild_repair": best_mild_repair,
        "sample_sand_good": sand_good[:10],
        "sample_sand_repair": sorted(
            sand_repair_only, key=lambda s: -s["depth_delta_net"]
        )[:10],
        "conclusion": (
            "Model B (shadow then deviate) for -17: supercritical antagonism, "
            "mild depth-repair, and grow+repair sandwiches with true v2(n+17)."
        ),
    }
    # JSON-safe: trim huge int lists already ok
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"rows={len(rows)} growing={len(growing)} grow_destroy={len(grow_destroy)} "
        f"grow_preserve={len(grow_preserve)}",
        f"mild={len(mild)} mild_repair={len(mild_repair)} mild_preserve={len(mild_preserve)}",
        f"sandwiches={len(sandwiches)} grow+preserve={len(sand_good)} "
        f"any_repair={len(sand_repair_only)}",
    ]
    for r in best_grow_destroy[:4]:
        lines.append(
            f"  DESTROY ex={r['ex']} m={r['m']} k={r['k']} growth={r['growth']:.3f} "
            f"v2:{r['v2_before_ex']}->{r['v2_after']}"
        )
    for r in best_grow_preserve[:4]:
        lines.append(
            f"  GROW+KEEP ex={r['ex']} m={r['m']} k={r['k']} growth={r['growth']:.3f} "
            f"v2:{r['v2_before_ex']}->{r['v2_after']}"
        )
    for r in best_mild_repair[:4]:
        lines.append(
            f"  REPAIR ex={r['ex']} m={r['m']} k={r['k']} growth={r['growth']:.3f} "
            f"v2:{r['v2_before_ex']}->{r['v2_after']} delta={r['depth_delta']}"
        )
    if not mild_repair:
        lines.append("  (no mild depth-repair events)")
    for s in sand_good[:3]:
        lines.append(
            f"  SAND_GOOD grow={s['grow_ex']} repair={s['repair_ex']} "
            f"net_growth={s['growth_net']:.3f} v2:{s['v2']}"
        )
    if not sand_good:
        lines.append("  (no grow+preserve-depth sandwiches)")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
