"""Theorem 4: schedule-locking analysis of the regeneration demands.

Fast formula (validated against the full (8.2) residue): for j <= 9m'+1,
  r_{m,m'} mod 64^j = 81^{-(9m+1)} (17*81^{-1} - 81^{9m}) mod 64^j,
independent of m'.  Hence the demand at depth j is a function of
m mod 2^{6j-4} only (2-automatic in m).

(i) Eventually-periodic gap schedules (gap-sum G per period): demands
    along the schedule are periodic with period 2^{6j-4}/gcd(G, 2^{6j-4})
    at depth j -- CONSTANT only to depth j <= (v2(G)+4)/6.  Since v2(G)
    is fixed, demands at deeper digits have unbounded period: no finite
    word grammar supplies them.  (Periodic schedules are already dead
    geometrically by the transcendental slope; this kills them again at
    the residue level.)
(ii) Sturmian schedules (gaps 17/18 with the slope's frequency): demands
    are never eventually periodic (verified to period 1500 at depth 2;
    m_t mod 256 follows an irrational-rotation orbit) but are
    Ostrowski-computable.  Closure of the certificate = a fixed point
    between this Ostrowski-automatic demand stream and the supply stream
    (digits of 81^{9m}-multiples) -- the digits-of-3-smooth-numbers wall,
    i.e. Furstenberg x64/x81 rigidity territory.
"""
import math
from collections import Counter

def regen_r_full(m, mp, j):
    M = 64 ** (9 * mp + 1)
    cst = (M + 17) // 81
    return pow(81, -(9 * m + 1), M) * (cst - 81 ** (9 * m)) % M % 64 ** j

def regen_r_fast(m, j):
    Mj = 64 ** j
    i81 = pow(81, -1, Mj)
    return pow(i81, 9 * m + 1, Mj) * (17 * i81 - pow(81, 9 * m, Mj)) % Mj

assert all(regen_r_full(m, m + g, j) == regen_r_fast(m, j)
           for m in range(1, 8) for g in (3, 17) for j in (1, 2, 3))
print("fast demand formula validated")

for G in (17, 18, 32, 64, 68, 256):
    j = 2
    P = 2 ** (6 * j - 4)
    per = P // math.gcd(G, P)
    seq = [regen_r_fast(1 + t * G, j) for t in range(3 * per + 8)]
    assert all(seq[i] == seq[i + per] for i in range(len(seq) - per))
    assert per == 1 or any(seq[i] != seq[i + per // 2] for i in range(per // 2))
    print(f"gap G={G:3d}: demand period {per:3d} = 2^8/gcd(G,2^8) at depth 2")

sl = math.log(81) / math.log(64)
alpha = 1 / (sl - 1) - 17
m, x = 1, 0.0
ms = [m]
for t in range(6000):
    x += alpha
    if x >= 1:
        m += 18; x -= 1
    else:
        m += 17
    ms.append(m)
demand = [regen_r_fast(mt, 2) for mt in ms[:5000]]
tail = demand[1000:]
assert not any(all(tail[i] == tail[i + p] for i in range(len(tail) - p))
               for p in range(1, 1500))
c = Counter(mt % 256 for mt in ms)
print(f"Sturmian: demands aperiodic (no period <= 1500); m_t mod 256 "
      f"visits {len(c)}/256 classes")
print("ALL CHECKS PASS")
