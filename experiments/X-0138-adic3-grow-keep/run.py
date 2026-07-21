#!/usr/bin/env python3
"""X-0138: iterate 3-adic grow+keep (follow-up to X-0137).

X-0137 found grow+preserve v3 events for c in {-10,-5,-1}.
Iterate those moves with a v3 depth floor and ask for +10-bit escapes —
the 3-adic analogue of X-0131, testing whether L-0114's 2-adic burn has a
3-adic bypass.
"""

from __future__ import annotations

import json
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


def v3(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


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

    alphabet = ["1", "11", "111", "1111", "10", "01", "110", "101", "0", "00"]
    targets = [-1, -5, -10, -17]
    # seeds: n ≡ c mod 3^d for d>=2, positive
    seeds = []
    for c in targets:
        for d in (2, 3, 4, 5, 6):
            mod = 3**d
            # n = c + k*3^d > 0
            for k in range(0, 40):
                n = c + k * mod
                if n > 1:
                    seeds.append((n, c, d))

    DEPTH_FLOOR = 2
    MAX_ITERS = 25
    traj = []
    escapes = []

    for n0, c, d0 in seeds[:200]:
        start_bits = n0.bit_length()
        frontier = [(n0, v3(n0 - c))]
        best_bits = start_bits
        best_depth = v3(n0 - c)
        escaped = False
        for it in range(MAX_ITERS):
            nxt = []
            for n, depth in frontier:
                cands = []
                for w in alphabet:
                    if not follows(n, w):
                        continue
                    n2 = apply_word(n, w)
                    if n2 <= 0:
                        continue
                    d2 = v3(n2 - c)
                    if d2 < DEPTH_FLOOR:
                        continue
                    growth = n2 / n
                    if growth > 1 and d2 >= depth:
                        score = (2, growth, d2)
                    elif d2 > depth:
                        score = (1, d2 - depth, growth)
                    else:
                        continue
                    cands.append((score, n2, d2))
                cands.sort(reverse=True)
                for score, n2, d2 in cands[:4]:
                    nxt.append((n2, d2))
                    bits = n2.bit_length()
                    if bits > best_bits:
                        best_bits = bits
                        best_depth = d2
                    if bits >= start_bits + 10 and d2 >= DEPTH_FLOOR:
                        escapes.append(
                            {
                                "c": c,
                                "seed": n0,
                                "final": n2,
                                "bit_gain": bits - start_bits,
                                "v3": d2,
                                "iters": it + 1,
                            }
                        )
                        escaped = True
            if not nxt or escaped:
                break
            nxt.sort(key=lambda t: (t[0].bit_length(), t[1]), reverse=True)
            frontier = nxt[:12]
        traj.append(
            {
                "c": c,
                "seed": n0,
                "d0": d0,
                "bit_gain": best_bits - start_bits,
                "best_depth": best_depth,
                "escaped": escaped,
            }
        )

    by_c = {}
    for t in traj:
        by_c.setdefault(t["c"], []).append(t)
    summary = {
        "depth_floor": DEPTH_FLOOR,
        "seeds": len(traj),
        "escapes": escapes,
        "escape_count": len(escapes),
        "max_bit_gain": max((t["bit_gain"] for t in traj), default=0),
        "best_by_c": {
            str(c): sorted(rows, key=lambda t: -t["bit_gain"])[:5]
            for c, rows in by_c.items()
        },
        "conclusion": (
            "Iterate 3-adic grow+keep for c in {-1,-5,-10,-17}; "
            "+10-bit escapes would open a true 3-adic fuel engine."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"seeds={len(traj)} escapes={len(escapes)} max_bit_gain={summary['max_bit_gain']}",
    ]
    for c, rows in by_c.items():
        top = max(rows, key=lambda t: t["bit_gain"])
        lines.append(
            f"  c={c}: max_bit_gain={top['bit_gain']} best_depth={top['best_depth']} "
            f"escapes={sum(1 for t in rows if t['escaped'])}"
        )
    for e in escapes[:5]:
        lines.append(
            f"  ESCAPE c={e['c']} +{e['bit_gain']}bits v3={e['v3']} final={e['final']}"
        )
    if not escapes:
        lines.append("  (no +10-bit v3 escapes)")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
