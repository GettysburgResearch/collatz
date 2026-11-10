#!/usr/bin/env python3
"""Excursion law for true Collatz orbits against the constant m' = log 3 - (4/3) log 2.

For random odd y, count the odd iterates Syr^k(y), k >= 1, with Syr^k(y)/y in [r, 2r).
Renewal prediction for large r:  expected count = 1/(2 m' r).
Also reports r * P(max_k Syr^k(y)/y >= r), which should approach a constant (exponent 1).
Usage: python3 excursion.py [samples]     (default 100000; about 40 s)
"""
import json, math, sys
import numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000
MP = math.log(3) - 4 / 3 * math.log(2)
BANDS = [2, 4, 8, 16, 32, 64, 128]
rng = np.random.default_rng(7)

def run(bits):
    y0 = rng.integers(2 ** (bits - 1), 2 ** bits, size=N, dtype=np.int64) * 2 + 1
    y = y0.copy(); alive = np.ones(N, bool); cnt = np.zeros(len(BANDS)); mx = np.ones(N)
    while alive.any():
        y = np.where(alive, 3 * y + 1, y)
        while True:
            ev = alive & (y % 2 == 0)
            if not ev.any(): break
            y = np.where(ev, y // 2, y)
        ratio = y / y0
        for i, r in enumerate(BANDS): cnt[i] += np.count_nonzero(alive & (ratio >= r) & (ratio < 2 * r))
        mx = np.maximum(mx, np.where(alive, ratio, 0)); alive &= y != 1
    return dict(bits=bits + 1, visits=list(cnt / N), predicted=[1 / (2 * MP * r) for r in BANDS],
                r_times_tail=[float(r * np.mean(mx >= r)) for r in BANDS])
rows = [run(b) for b in (30, 40)]
json.dump(dict(samples=N, bands=BANDS, m_prime=MP, rows=rows), open(__file__.replace("excursion.py", "results_excursion.json"), "w"), indent=1)
for r in rows:
    print(f"y near 2^{r['bits']}:")
    print("  r            " + " ".join(f"{b:>7}" for b in BANDS))
    print("  visits       " + " ".join(f"{v:7.4f}" for v in r["visits"]))
    print("  1/(2 m' r)   " + " ".join(f"{v:7.4f}" for v in r["predicted"]))
    print("  r P(max>=r)  " + " ".join(f"{v:7.4f}" for v in r["r_times_tail"]))
ok = all(abs(v / p - 1) < 0.08 for r in rows for v, p in zip(r["visits"][2:], r["predicted"][2:]))
print("PASS" if ok else "FAIL", "visits within 8% of prediction for r >= 8"); sys.exit(0 if ok else 1)
