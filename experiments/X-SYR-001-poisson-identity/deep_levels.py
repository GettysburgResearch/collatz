#!/usr/bin/env python3
"""Deep run for the table in research/syracuse-poisson-identity/README.md.  Needs numpy.

Run:  python3 deep_levels.py 17      (about 6 GB of memory and 10 minutes for N = 17)
Writes deep_rows.json in the current directory: for each level n the collision energy Q_n,
the odometer autocorrelations gamma_n(1..6), and the least and greatest density over units.
Binary64, sum over a truncated at a <= 66.  EMPIRICAL evidence only.
"""
import numpy as np, time, sys, json
NMAX = int(sys.argv[1]); AMAX = 66
m = np.array([1.0]); t0 = time.time(); rows = []
for n in range(1, NMAX + 1):
    M = 3 ** n
    new = np.zeros(M)
    x = np.arange(M, dtype=np.int64)
    p = 1
    for a in range(1, AMAX + 1):
        p = (p * 2) % M
        t = x * p
        t %= M
        r = t % 3
        idx = np.nonzero(r == 1)[0]
        new[idx] += 2.0 ** (-a) * m[(t[idx] - 1) // 3]
        del t, r, idx
    m = new
    Q = M * float(np.dot(m, m))
    R = []
    y = x
    for j in range(1, 7):
        y = (4 * y + 1) % M
        R.append(M * float(np.dot(m, m[y])))
    units = m[(x % 3) != 0]
    rows.append(dict(n=n, Q=Q, R=R, min_density=float(M * units.min()), max_density=float(M * m.max())))
    print(json.dumps(rows[-1]), f"t={time.time()-t0:.0f}s", flush=True)
    del x, y, units
json.dump(rows, open("deep_rows.json", "w"))
