#!/usr/bin/env python3
"""X-0139: verify L-0115 3-adic valuation ledger."""

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


def v3(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 3 == 0:
        n //= 3
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


def predict(w: str, c: int, n: int) -> int:
    kap = kappa(w, c)
    a = w.count("1")
    d0 = v3(n - c)
    vn = d0 + a
    if kap == 0:
        return vn
    vk = v3(kap)
    if vk < vn:
        return vk
    if vn < vk:
        return vn
    # equal leading valuations: allow cancellation
    return v3(kap + (3**a) * (n - c))


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    rows = []
    mismatches = []
    for c in (-1, -5, -10, -17, 1, 5):
        for w in ["1", "11", "111", "110", "10", "101", "011"]:
            re = residue_of(w)
            L = len(w)
            found = 0
            for q in range(0, 20000):
                n = re + q * (1 << L)
                if n <= 1 or not follows(n, w):
                    continue
                d0 = v3(n - c)
                if d0 == 0 and kappa(w, c) != 0 and v3(kappa(w, c)) == 0:
                    continue
                n1 = apply_word(n, w)
                d1 = v3(n1 - c)
                pred = predict(w, c, n)
                rec = {
                    "c": c,
                    "w": w,
                    "n": n,
                    "kappa": kappa(w, c),
                    "d0": d0,
                    "d1": d1,
                    "pred": pred,
                    "match": d1 == pred,
                    "growth": n1 / n,
                }
                rows.append(rec)
                if d1 != pred:
                    mismatches.append(rec)
                found += 1
                if found >= 8:
                    break
    summary = {
        "checked": len(rows),
        "mismatches": len(mismatches),
        "sample_mismatches": mismatches[:10],
        "sample_matches": [r for r in rows if r["match"]][:15],
        "conclusion": "Verification of L-0115 3-adic ledger.",
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"checked={len(rows)} mismatches={len(mismatches)}",
    ]
    for r in rows[:12]:
        lines.append(
            f"  c={r['c']} w={r['w']} d0={r['d0']} d1={r['d1']} "
            f"pred={r['pred']} match={r['match']} g={r['growth']:.3f}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:20]))


if __name__ == "__main__":
    main()
