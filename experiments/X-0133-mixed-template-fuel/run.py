#!/usr/bin/env python3
"""X-0133: mixed-template fuel (-5 <-> -17 chart switches).

Hypothesis: grow+keep stalls on a single chart because repair and growth
live in incompatible residue classes. Allow the walker to switch between
the -5 (word 110) and -17 (word 11110111000) charts, scoring depth as
max(v2(n+5), v2(n+17)), and seek multi-epoch bit growth.
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


def dual_depth(n: int) -> tuple[int, int, int]:
    d5 = v2(n + 5)
    d17 = v2(n + 17)
    return d5, d17, max(d5, d17)


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    t5 = "110"
    t17 = "11110111000"
    holds = [t5, t17]
    grow = ["1", "11", "111", "1111", "1011"]
    repair = ["0", "00", "000", "10", "010", "01"]
    alphabet = grow + repair + holds

    seeds = []
    for tmpl, m_list in ((t5, [6, 12, 18, 24]), (t17, [11, 22, 33])):
        Lt = len(tmpl)
        for m in m_list:
            prefix = (tmpl * ((m + Lt - 1) // Lt + 2))[:m]
            rt = residue_of(prefix)
            for q in range(0, 24):
                n = (1 << m) * q + rt
                if n > 0:
                    seeds.append({"n": n, "chart": "5" if tmpl == t5 else "17", "m": m})

    DEPTH_FLOOR = 2
    MAX_ITERS = 40
    traj = []
    escapes = []

    for seed in seeds[:160]:
        n0 = seed["n"]
        start_bits = n0.bit_length()
        frontier = [(n0, dual_depth(n0)[2], [])]
        best_bits = start_bits
        best_depth = dual_depth(n0)[2]
        escaped = False
        for it in range(MAX_ITERS):
            nxt = []
            for n, d, path in frontier:
                cands = []
                for w in alphabet:
                    if not follows(n, w):
                        continue
                    n2 = apply_word(n, w)
                    if n2 <= 0:
                        continue
                    d5, d17, d2 = dual_depth(n2)
                    if d2 < DEPTH_FLOOR:
                        continue
                    growth = n2 / n
                    if growth > 1 and d2 >= d:
                        score = (3, growth, d2)
                    elif d2 > d:
                        score = (2, d2 - d, growth)
                    elif w in holds and d2 >= DEPTH_FLOOR:
                        score = (1, d2, 1.0)
                    elif growth > 1 and d2 >= DEPTH_FLOOR:
                        # allow mild depth dip within floor
                        score = (0, growth, d2)
                    else:
                        continue
                    cands.append((score, n2, d2, w, d5, d17))
                cands.sort(reverse=True)
                for score, n2, d2, w, d5, d17 in cands[:5]:
                    nxt.append((n2, d2, path + [w]))
                    bits = n2.bit_length()
                    if bits > best_bits:
                        best_bits = bits
                        best_depth = d2
                    if bits >= start_bits + 10 and d2 >= DEPTH_FLOOR:
                        escapes.append(
                            {
                                "seed": n0,
                                "chart0": seed["chart"],
                                "final": n2,
                                "bit_gain": bits - start_bits,
                                "depth": d2,
                                "d5": d5,
                                "d17": d17,
                                "iters": it + 1,
                                "path": path + [w],
                            }
                        )
                        escaped = True
            if not nxt or escaped:
                break
            nxt.sort(key=lambda t: (t[0].bit_length(), t[1]), reverse=True)
            frontier = nxt[:16]
        traj.append(
            {
                "seed": n0,
                "chart0": seed["chart"],
                "m": seed["m"],
                "bit_gain": best_bits - start_bits,
                "best_depth": best_depth,
                "escaped": escaped,
            }
        )

    best = sorted(traj, key=lambda t: -t["bit_gain"])
    summary = {
        "depth_floor": DEPTH_FLOOR,
        "seeds": len(traj),
        "escapes": len(escapes),
        "max_bit_gain": best[0]["bit_gain"] if best else 0,
        "best": best[:20],
        "escape_samples": escapes[:10],
        "conclusion": (
            "Mixed -5/-17 fuel search with dual-depth max(v2(n+5),v2(n+17)); "
            "+10-bit escapes holding depth floor would challenge C-0104."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"seeds={len(traj)} escapes={len(escapes)} max_bit_gain={summary['max_bit_gain']}",
    ]
    for t in best[:8]:
        lines.append(
            f"  chart0={t['chart0']} m={t['m']} bit_gain={t['bit_gain']} "
            f"best_depth={t['best_depth']}"
        )
    if not escapes:
        lines.append("  (no +10-bit dual-depth escapes)")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
