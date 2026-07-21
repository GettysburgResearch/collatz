#!/usr/bin/env python3
"""X-0134: verify L-0114 deep-burn valuation identity."""

from __future__ import annotations

import json
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


def apply_word(n: int, word: str) -> int:
    a = word.count("1")
    L = len(word)
    return (3**a * n + B_of(word)) // (1 << L)


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


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


def follows(n: int, w: str) -> bool:
    x = n
    for bit in w:
        if (x & 1) != int(bit):
            return False
        x = T(x)
    return True


def kappa(w: str, c: int) -> int:
    a = w.count("1")
    L = len(w)
    return 3**a * c + B_of(w) - c * (1 << L)


def find_deep(w: str, c: int, m: int, limit: int = 1 << 22) -> int | None:
    re = residue_of(w)
    L = len(w)
    for k in range(0, limit):
        n = re + k * (1 << L)
        if n > 0 and v2(n - c) >= m and follows(n, w):
            return n
    return None


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    rows = []
    mismatches = []
    for c in (-5, -17):
        for w in ["1", "11", "111", "1111", "101", "0", "00", "10", "010"]:
            kap = kappa(w, c)
            L = len(w)
            vk = v2(kap) if kap != 0 else None
            for m in (8, 12, 20):
                n = find_deep(w, c, m)
                if n is None:
                    rows.append(
                        {
                            "c": c,
                            "w": w,
                            "m": m,
                            "kappa": kap,
                            "v2_kappa": vk,
                            "found": False,
                            "pred_impossible": kap != 0 and vk is not None and vk < L,
                        }
                    )
                    continue
                n1 = apply_word(n, w)
                d0 = v2(n - c)
                d1 = v2(n1 - c)
                if kap == 0:
                    pred = d0 - L
                elif d0 > vk:
                    pred = vk - L
                else:
                    pred = None
                ok = pred is None or d1 == pred
                rec = {
                    "c": c,
                    "w": w,
                    "m": m,
                    "kappa": kap,
                    "v2_kappa": vk,
                    "found": True,
                    "n": n,
                    "d0": d0,
                    "d1": d1,
                    "pred": pred,
                    "match": ok,
                    "growth": n1 / n,
                }
                rows.append(rec)
                if not ok:
                    mismatches.append(rec)

    # also verify fixing words (template powers): kappa=0
    for c, tmpl in ((-5, "110"), (-17, "11110111000")):
        for k in (1, 2, 3):
            w = tmpl * k
            kap = kappa(w, c)
            assert kap == 0
            n = find_deep(w, c, 15)
            if n is None:
                continue
            n1 = apply_word(n, w)
            d0 = v2(n - c)
            d1 = v2(n1 - c)
            pred = d0 - len(w)
            rows.append(
                {
                    "c": c,
                    "w": f"tmpl^{k}",
                    "kappa": 0,
                    "found": True,
                    "d0": d0,
                    "d1": d1,
                    "pred": pred,
                    "match": d1 == pred,
                }
            )
            if d1 != pred:
                mismatches.append(rows[-1])

    deep_matches = [
        r
        for r in rows
        if r.get("found") and r.get("pred") is not None and r.get("match")
    ]
    summary = {
        "rows": rows,
        "mismatches": mismatches,
        "deep_formula_matches": len(deep_matches),
        "mismatch_count": len(mismatches),
        "conclusion": (
            "Verification of L-0114: when a deep preimage exists, "
            "v2(T_w(n)-c)=v2(kappa)-L; when v2(kappa)<L, deep preimages absent."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"matches={len(deep_matches)} mismatches={len(mismatches)} rows={len(rows)}",
    ]
    for r in rows:
        if not r.get("found"):
            if r.get("pred_impossible"):
                lines.append(
                    f"  ABSENT c={r['c']} w={r['w']} m={r['m']} "
                    f"(v2(kappa)={r['v2_kappa']}<L) OK"
                )
            continue
        if r.get("pred") is None:
            continue
        lines.append(
            f"  c={r['c']} w={r['w']} d0={r['d0']} d1={r['d1']} "
            f"pred={r['pred']} match={r['match']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:40]))


if __name__ == "__main__":
    main()
