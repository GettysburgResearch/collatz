#!/usr/bin/env python3
"""The 3x-1 map on positive odd integers (equivalently 3x+1 on negative integers) as a control.

Its 2-adic and 3-adic statistics are those of 3x+1, yet it has three known cycles.  This script
measures the basins of the cycles through 1, 5 and 17 by dyadic scale and by residue class mod 9.
Usage: python3 minus_one.py [X]     (default 2000000; about 10 s)
"""
import json, sys
import numpy as np
X = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
CYCLES = {1: 0, 5: 1, 7: 1, 17: 2, 25: 2, 37: 2, 55: 2, 41: 2, 61: 2, 91: 2}
basin = np.full(X + 1, -1, dtype=np.int8)
for N in range(1, X + 1, 2):
    y = N
    while True:
        if y in CYCLES: b = CYCLES[y]; break
        if y < N: b = int(basin[y]); break
        y = 3 * y - 1
        while y % 2 == 0: y //= 2
    basin[N] = b
odd = np.arange(1, X + 1, 2); b = basin[1::2]
rows = []
lo = 1024
while lo * 2 <= X:
    sel = (odd >= lo) & (odd < 2 * lo); rows.append(dict(scale=lo, shares=[float(np.mean(b[sel] == c)) for c in range(3)])); lo *= 4
top = (odd >= X // 2)
by9 = {int(r): [float(np.mean(b[top & (odd % 9 == r)] == c)) for c in range(3)] for r in (1, 2, 4, 5, 7, 8)}
json.dump(dict(X=X, by_scale=rows, top_half_by_residue_mod_9=by9, unassigned=int(np.sum(b < 0))),
          open(__file__.replace("minus_one.py", "results_minus_one.json"), "w"), indent=1)
print("unassigned:", int(np.sum(b < 0)))
print("share of basins of the cycles through 1, 5, 17 among odd N in [scale, 2 scale):")
for r in rows: print("  %8d  " % r["scale"] + "  ".join("%.4f" % s for s in r["shares"]))
print("same, N in [X/2, X], by residue mod 9:")
for r, s in by9.items(): print("  %d  " % r + "  ".join("%.4f" % v for v in s))
