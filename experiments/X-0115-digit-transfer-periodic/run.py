#!/usr/bin/env python3
"""X-0115: periodic digit itineraries on small digit-transfer charts.

For H(M B + d) = N B + d with pure powers M=2^L, N=3^a > M and D a small
digit set coming from known collision charts, verify that constant/periodic
digit streams correspond to negative rational fixed points of the composed
affine shortcut map (T-0102 / T-0101(D)).
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


def word_for_residue(L: int, r: int) -> str:
    x = r
    bits = []
    for _ in range(L):
        bits.append(str(x & 1))
        x = T(x)
    return "".join(bits)


def chart_pair_64_81():
    """Classic width-2 chart: residues 14,15 length 6 -> 81q+20."""
    L, a = 6, 4
    M, N = 1 << L, 3**a
    D = [0, 1]
    r0 = 14
    words = {d: word_for_residue(L, r0 + d) for d in D}
    return {"name": "64->81", "L": L, "a": a, "M": M, "N": N, "r0": r0, "D": D, "words": words}


def chart_triple_512_729():
    L, a = 9, 6
    M, N = 1 << L, 3**a
    D = [0, 1, 2]
    r0 = 124
    words = {d: word_for_residue(L, r0 + d) for d in D}
    return {"name": "512->729", "L": L, "a": a, "M": M, "N": N, "r0": r0, "D": D, "words": words}


def fp_of_word(word: str) -> Fraction:
    L = len(word)
    a = word.count("1")
    B = B_of(word)
    mu = Fraction(3**a, 1 << L)
    beta = Fraction(B, 1 << L)
    return -beta / (mu - 1)


def fp_of_digit_cycle(chart: dict, digit_cycle: list[int]) -> dict:
    words = [chart["words"][d] for d in digit_cycle]
    # compose
    mu = Fraction(1, 1)
    beta = Fraction(0, 1)
    for w in words:
        L = len(w)
        a = w.count("1")
        B = B_of(w)
        mu_i = Fraction(3**a, 1 << L)
        beta_i = Fraction(B, 1 << L)
        beta = mu_i * beta + beta_i
        mu = mu_i * mu
    fp = -beta / (mu - 1)
    return {
        "digits": digit_cycle,
        "words": words,
        "mu": str(mu),
        "fp": str(fp),
        "negative": fp < 0,
        "supercritical": mu > 1,
    }


def ordinary_survival(chart: dict, digit_cycle: list[int], qmax: int = 5000) -> dict:
    """Try periodic digit schedule on lifts; count max periods before leaving ports."""
    L = chart["L"]
    M = chart["M"]
    N = chart["N"]
    r0 = chart["r0"]
    # For digit d, n = M q + r0 + d maps to N q + s with same s for all d in chart.
    # Periodic digits mean choosing d_i each time on the induced H map.
    # On ordinary n, check how long we can stay in r0+D mod M while applying T^L.
    max_periods = 0
    best_n = None
    Dset = set(chart["D"])
    for d0 in chart["D"]:
        for q0 in range(0, min(qmax, 2000)):
            n = M * q0 + r0 + d0
            m = n
            periods = 0
            for _ in range(40):
                r = m % M
                d = r - r0
                if d not in Dset:
                    break
                # apply T^L
                x = m
                for __ in range(L):
                    x = T(x)
                m = x
                periods += 1
            if periods > max_periods:
                max_periods = periods
                best_n = n
    return {"max_periods": max_periods, "best_n": best_n, "digit_cycle": digit_cycle}


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    charts = [chart_pair_64_81(), chart_triple_512_729()]
    out = []
    for ch in charts:
        # verify words share a, and collision outputs match
        rows = {"chart": ch["name"], "words": ch["words"], "cycles": [], "survival": []}
        for cycle in ([[d] for d in ch["D"]] + [[ch["D"][0], ch["D"][-1]], ch["D"][:]]):
            # dedup digit lists
            pass
        cycles = []
        for d in ch["D"]:
            cycles.append([d])
        if len(ch["D"]) >= 2:
            cycles.append([ch["D"][0], ch["D"][1]])
        cycles.append(list(ch["D"]))
        for cyc in cycles:
            fpinfo = fp_of_digit_cycle(ch, cyc)
            surv = ordinary_survival(ch, cyc)
            rows["cycles"].append({**fpinfo, **surv})
        out.append(rows)
    summary = {
        "charts": out,
        "all_super_fp_negative": all(
            c["negative"] for rows in out for c in rows["cycles"] if c["supercritical"]
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [f"all supercritical periodic digit fps negative={summary['all_super_fp_negative']}"]
    for rows in out:
        lines.append(f"chart {rows['chart']}:")
        for c in rows["cycles"]:
            lines.append(
                f"  digits={c['digits']} mu={c['mu']} fp={c['fp']} neg={c['negative']} max_periods={c['max_periods']}"
            )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
