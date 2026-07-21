#!/usr/bin/env python3
"""X-0136: mixed-modulus CRT growth ladder (corrected).

State = concatenated chronological word. Extend by short supercritical blocks
when CRT on residue_of(word) is compatible with optional odd-modulus filters
on the starting integer. Score by true affine growth 3^a/2^L of the full word
and by forward peak of sample integers in the class.
"""

from __future__ import annotations

import json
from math import gcd, log
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


def crt_pair(a1: int, m1: int, a2: int, m2: int) -> tuple[int, int] | None:
    g = gcd(m1, m2)
    if (a1 - a2) % g != 0:
        return None
    m2g = m2 // g
    inv = pow((m1 // g) % m2g, -1, m2g)
    t = ((a2 - a1) // g) * inv % m2g
    x = a1 + m1 * t
    M = m1 * m2 // g
    return x % M, M


def growth_of(word: str) -> float:
    a = word.count("1")
    L = len(word)
    return (3**a) / (2**L)


def forward_peak_ratio(n: int, steps: int = 300) -> tuple[float, bool]:
    x = n
    peak = n
    for _ in range(steps):
        x = T(x)
        if x > peak:
            peak = x
        if x in (1, 2):
            return peak / n, True
    return peak / n, False


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    blocks = []
    for L in range(1, 7):
        for mask in range(1 << L):
            w = format(mask, f"0{L}b")[::-1]
            if growth_of(w) > 1.05 and "1" in w:
                blocks.append(w)
    blocks.sort(key=lambda w: -growth_of(w))

    # beam of words + optional odd modulus filter (mod, residue)
    beam = [("", 1, 0)]  # word, odd_mod, odd_res
    history = []
    BEAM = 40
    for stage in range(12):
        nxt = []
        for word, omod, ores in beam:
            for b in blocks:
                w2 = word + b
                if len(w2) > 48:
                    continue
                r = residue_of(w2)
                m = 1 << len(w2)
                # apply odd filter if any
                if omod > 1:
                    lift = crt_pair(r, m, ores, omod)
                    if lift is None:
                        continue
                    r, m = lift
                g = growth_of(w2)
                # also try adding a fresh odd-modulus filter
                variants = [(w2, omod, ores, r, m, g)]
                if omod == 1 and len(w2) <= 24:
                    for p in (3, 5):
                        for a in range(p):
                            lp = crt_pair(r, m, a, p)
                            if lp:
                                variants.append((w2, p, a, lp[0], lp[1], g))
                for w3, om, ora, rr, mm, gg in variants:
                    # sample
                    n = rr if rr > 1 else rr + mm
                    if n <= 1:
                        n += mm
                    n1 = apply_word(n, w3)
                    realized = n1 / n if n else 0
                    score = log(gg) + 0.01 * log(mm)
                    nxt.append((score, w3, om, ora, rr, mm, gg, realized, n))
        if not nxt:
            history.append({"stage": stage, "extinct": True})
            break
        nxt.sort(reverse=True)
        seen = set()
        beam2 = []
        for item in nxt:
            key = (item[1], item[2], item[3])  # word, omod, ores
            if key in seen:
                continue
            seen.add(key)
            beam2.append((item[1], item[2], item[3]))
            if len(beam2) >= BEAM:
                break
        best = nxt[0]
        history.append(
            {
                "stage": stage,
                "beam": len(beam2),
                "best_word": best[1],
                "best_L": len(best[1]),
                "best_a": best[1].count("1"),
                "affine_growth": best[6],
                "realized_sample": best[7],
                "mod_bits": best[5].bit_length(),
                "odd_mod": best[2],
                "sample_n": best[8],
            }
        )
        beam = beam2

    evaluations = []
    for word, omod, ores in beam[:12]:
        r = residue_of(word)
        m = 1 << len(word)
        if omod > 1:
            lp = crt_pair(r, m, ores, omod)
            if not lp:
                continue
            r, m = lp
        best_eval = None
        for q in range(0, 25):
            n = r + q * m
            if n <= 1:
                continue
            n1 = apply_word(n, word)
            peak_r, triv = forward_peak_ratio(n, 400)
            rec = {
                "word_L": len(word),
                "word_a": word.count("1"),
                "affine_growth": growth_of(word),
                "odd_mod": omod,
                "n": n,
                "after": n1,
                "realized": n1 / n,
                "peak_ratio": peak_r,
                "hit_trivial": triv,
            }
            if best_eval is None or rec["peak_ratio"] > best_eval["peak_ratio"]:
                best_eval = rec
        if best_eval:
            evaluations.append(best_eval)

    evaluations.sort(key=lambda e: -e["peak_ratio"])
    nontriv = [e for e in evaluations if not e["hit_trivial"]]
    summary = {
        "history": history,
        "evaluations": evaluations,
        "nontrivial_survivors": nontriv,
        "max_affine": max((h.get("affine_growth") or 0) for h in history),
        "max_peak": max((e["peak_ratio"] for e in evaluations), default=0),
        "conclusion": (
            "Corrected mixed-modulus ladder: concatenate supercritical blocks "
            "under 2^L (+ optional 3/5) CRT; look for non-trivial forward survivors."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"stages={len(history)} max_affine={summary['max_affine']:.3f} "
        f"max_peak={summary['max_peak']:.3f} nontriv={len(nontriv)}",
    ]
    for h in history:
        if h.get("extinct"):
            lines.append(f"  stage {h['stage']}: EXTINCT")
        else:
            lines.append(
                f"  stage {h['stage']}: L={h['best_L']} a={h['best_a']} "
                f"aff_g={h['affine_growth']:.3e} real={h['realized_sample']:.3e} "
                f"mod_bits={h['mod_bits']} odd_mod={h['odd_mod']}"
            )
    for e in evaluations[:6]:
        lines.append(
            f"  EVAL L={e['word_L']} aff={e['affine_growth']:.3e} n={e['n']} "
            f"peak={e['peak_ratio']:.3f} trivial={e['hit_trivial']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
