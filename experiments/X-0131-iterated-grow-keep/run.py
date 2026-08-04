#!/usr/bin/env python3
"""X-0131: iterate grow+keep excursions on the -17 chart (follow-up to X-0128).

X-0128 model B found finite grow+keep events (growth>1 and v2(n+17) nondecreasing).
This experiment asks whether such moves can be *iterated* to produce unbounded
archimedean growth while maintaining a depth floor — the divergence-certificate
shape suggested by the valuation-fuel path.
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


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    template = "11110111000"
    target = -17
    Lt = len(template)
    alphabet = [
        "1",
        "11",
        "111",
        "1111",
        "101",
        "1101",
        "1011",
        "11111",
        "10",
        "01",
        "010",
        "0",
        "00",
        # allow template periods as "hold" moves
        template,
    ]

    # seeds: deep cylinders
    seeds = []
    for m in (11, 22, 33):
        prefix = (template * ((m + Lt - 1) // Lt + 2))[:m]
        rt = residue_of(prefix)
        for q in range(0, 40):
            n = (1 << m) * q + rt
            if n > 0:
                seeds.append({"n": n, "m": m})

    DEPTH_FLOOR = 2
    MAX_ITERS = 30
    MAX_BRANCH = 4  # keep top branch factors per node

    trajectories = []
    escaped = []  # size grew by factor >= 2^10 from start with depth floor held
    stalled = 0
    collapsed = 0  # depth fell below floor

    for seed in seeds[:120]:
        n0 = seed["n"]
        start_size = n0.bit_length()
        # state: n, depth, log, path
        frontier = [(n0, v2(n0 - target), [], n0)]
        best_n = n0
        best_depth = v2(n0 - target)
        hit_escape = False
        hit_collapse = False
        for it in range(MAX_ITERS):
            nxt = []
            for n, d, path, n_start in frontier:
                cands = []
                for w in alphabet:
                    if not follows(n, w):
                        continue
                    n2 = apply_word(n, w)
                    if n2 <= 0:
                        continue
                    d2 = v2(n2 - target)
                    growth = n2 / n
                    # grow+keep relative to current, or mild repair if depth low
                    if d2 < DEPTH_FLOOR:
                        continue
                    score = None
                    if growth > 1 and d2 >= d:
                        score = (2, growth, d2)
                    elif d2 > d and growth >= 0.25:
                        # repair move
                        score = (1, d2 - d, growth)
                    elif w == template and d2 >= DEPTH_FLOOR:
                        score = (0, d2, 1.0)
                    if score is not None:
                        cands.append((score, n2, d2, w, growth))
                cands.sort(reverse=True)
                for score, n2, d2, w, growth in cands[:MAX_BRANCH]:
                    nxt.append((n2, d2, path + [w], n_start))
                    if n2 > best_n:
                        best_n = n2
                        best_depth = d2
                    if n2.bit_length() >= start_size + 10 and d2 >= DEPTH_FLOOR:
                        escaped.append(
                            {
                                "seed": n0,
                                "m": seed["m"],
                                "n_final": n2,
                                "depth": d2,
                                "iters": it + 1,
                                "path": path + [w],
                                "bit_gain": n2.bit_length() - start_size,
                            }
                        )
                        hit_escape = True
            if not nxt:
                stalled += 1
                break
            # prune frontier by size*depth
            nxt.sort(key=lambda t: (t[0].bit_length(), t[1]), reverse=True)
            frontier = nxt[:12]
            if hit_escape:
                break
        # check if depth collapsed along the way — already filtered
        trajectories.append(
            {
                "seed": n0,
                "m": seed["m"],
                "start_depth": v2(n0 - target),
                "best_n": best_n,
                "best_depth": best_depth,
                "bit_gain": best_n.bit_length() - start_size,
                "escaped": hit_escape,
            }
        )

    gains = sorted(trajectories, key=lambda t: -t["bit_gain"])
    summary = {
        "template": template,
        "fp": target,
        "depth_floor": DEPTH_FLOOR,
        "max_iters": MAX_ITERS,
        "seeds": len(trajectories),
        "escaped_count": len(escaped),
        "stalled_frontiers": stalled,
        "best_bit_gains": gains[:20],
        "escape_samples": escaped[:15],
        "max_bit_gain": gains[0]["bit_gain"] if gains else 0,
        "conclusion": (
            "Iterate grow+keep / repair moves on -17 with depth floor; "
            "escapes with +10 bits while holding depth would support a "
            "fuel-regenerative divergence certificate."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"seeds={len(trajectories)} escaped={len(escaped)} "
        f"max_bit_gain={summary['max_bit_gain']} stalled={stalled}",
    ]
    for t in gains[:8]:
        lines.append(
            f"  seed_m={t['m']} bit_gain={t['bit_gain']} "
            f"depth:{t['start_depth']}->{t['best_depth']} best_n={t['best_n']}"
        )
    for e in escaped[:5]:
        lines.append(
            f"  ESCAPE +{e['bit_gain']}bits depth={e['depth']} "
            f"iters={e['iters']} path={e['path'][:8]}..."
        )
    if not escaped:
        lines.append("  (no +10-bit escapes holding depth floor)")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
