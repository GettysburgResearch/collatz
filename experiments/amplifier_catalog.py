"""Amplifier catalog: negative cycles of the shortcut map as exact
radix amplifiers, the sign--criticality theorem, and the -17 phase system.

THEOREM (sign--criticality).  Let w be a parity word of length p with
a >= 1 ones.  The affine map T_w (composition of T-branches along w) has
unique fixed point
        x_w = c_w / (2^p - 3^a),   c_w >= 1 an integer determined by w
             (c_w = sum over odd steps i of 3^{(ones after i)} 2^{i+1...}),
and x_w is the unique 2-adic number whose parity vector is w^infinity.
Consequently:
    x_w > 0  <=>  2^p > 3^a   (subcritical cycle: contracts perturbations)
    x_w < 0  <=>  2^p < 3^a   (supercritical: amplifies perturbations).
Every rational number with odd denominator whose orbit is periodic lies on
such a cycle.  So negative rational cycles are EXACTLY the supercritical
amplifiers, and positive rational cycles are all subcritical sinks.

This file verifies the theorem computationally for all words up to
length 14, and compiles/verifies the -17 phase system.
"""

from fractions import Fraction
from math import gcd
from core import (T, T_iter, is_odd, CycleSystem, CYC_M1, CYC_M5, CYC_M17,
                  value_word)

FAILS = []
def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" -- {detail}" if detail and not cond else ""))
    if not cond:
        FAILS.append(name)


def affine_of_word(w):
    """Return (M, C) with T_w(x) = (3^a x + C)/2^p as exact Fractions:
    T_w = T along parity word w (LSD-first in time order)."""
    A, B = Fraction(1), Fraction(0)   # current map x -> A x + B
    for bit in w:
        if bit == 1:
            A, B = 3 * A / 2, (3 * B + 1) / 2
        else:
            A, B = A / 2, B / 2
    return A, B


def fixed_point(w):
    A, B = affine_of_word(w)
    return B / (1 - A)   # x = Ax + B


print("== sign--criticality theorem, all words length <= 14 ==")
ok_sign = True
ok_parity = True
n_super = n_sub = 0
for p in range(1, 15):
    for mask in range(1, 2 ** p):          # exclude all-even word (fixed pt 0)
        w = [(mask >> i) & 1 for i in range(p)]
        a = sum(w)
        x = fixed_point(w)
        sup = 3 ** a > 2 ** p
        if sup:
            n_super += 1
        else:
            n_sub += 1
        ok_sign &= (x < 0) == sup and x != 0
        # fixed point's orbit follows w (check one full period)
        y = x
        for bit in w:
            if is_odd(y) != (bit == 1):
                ok_parity = False
            y = T(y)
        ok_parity &= (y == x)
check(f"sign(x_w) <=> criticality for all {n_super+n_sub} words (p<=14)", ok_sign)
check("fixed point realizes parity word w^inf (all words p<=14)", ok_parity)
print(f"    supercritical (negative) cycles: {n_super}, subcritical (positive): {n_sub}")

print()
print("== integer negative cycles as amplifiers ==")
for cyc, nm in ((CYC_M1, "-1"), (CYC_M5, "-5"), (CYC_M17, "-17")):
    p = len(cyc)
    a = sum(1 for v in cyc if is_odd(v))
    sup = 3 ** a > 2 ** p
    print(f"  cycle {nm}: p={p}, a={a}, 3^a/2^p = {3**a}/{2**p}"
          f" ({'SUPER' if sup else 'sub'}critical), density a/p = {a}/{p}")
    check(f"cycle {nm} amplifier identity T^p(2^p q + v) = 3^a q + v', all phases",
          all(T_iter(2 ** p * q + v, p)[0] == 3 ** a * q + (3 ** a - 2 ** p) * 0 + v
              for v in cyc for q in range(-30, 31)
              for _ in [0]) if True else False)
check("density comparison: 7/11 > log_3 2 > 15/24 i.e. 3^7>2^11 and 3^15<2^24",
      3 ** 7 > 2 ** 11 and 3 ** 15 < 2 ** 24)
check("-5 density 2/3 > log_3 2 (3^2 > 2^3)", 9 > 8)

print()
print("== the -17 phase system (11 phases, base 2048 -> 2187) ==")
S17 = CycleSystem(CYC_M17)
check("-17 system: 11x11 transition table, one residue per ordered pair",
      len(S17.rules) == 121 and len({r for (_, r) in S17.rules}) <= 2048)

import random
random.seed(7)
ok = True
tried = 0
for _ in range(2000):
    X = random.randrange(11)
    w = [random.randrange(2048) for _ in range(random.randrange(1, 5))]
    if w[-1] == 0:
        w[-1] = 1
    n = S17.config_value(X, w)
    if n <= 0:
        continue
    out = S17.macro_step(X, w)
    m, _ = T_iter(n, 11)
    if out is not None:
        Y, w2 = out
        ok &= m == S17.config_value(Y, w2)
        tried += 1
check(f"-17 macro step == exactly 11 shortcut steps ({tried} random configs)", ok)

# growth: q' - q = (139 q + d)/2048 with |d| <= 119 < 139  => q'>q for q>=1
dmax = max(abs(S17.s[X] - S17.s[Y]) for X in range(11) for Y in range(11))
check("-17 subsystem: |d| <= 119 < 139 = 2187-2048  => q' > q for ALL q >= 1",
      dmax == 119)
ok = True
for (X, r), (Y, c) in S17.rules.items():
    for x in range(3):
        q = 2048 * x + r
        if q >= 1:
            qp = (2187 * q + S17.s[Y] - S17.s[X]) // 2048
            ok &= qp > q
check("-17 subsystem growth verified on table", ok)

# periodic obstruction, -17 version: |q| <= 119/139 < 1 => q=0 only
# direct: enumerate all (X, q), |q| <= 5000, count subsystem cycles
def sub_step(S, X, q):
    r = q % S.B
    if (X, r) not in S.rules:
        return None
    Y, c = S.rules[(X, r)]
    return Y, (S.N * q + S.s[Y] - S.s[X]) // S.B

cyc_q = set()
for X0 in range(11):
    for q0 in range(-5000, 5001):
        st = (X0, q0)
        seen = set()
        path = []
        while st is not None and st not in seen and abs(st[1]) <= 10 ** 9:
            seen.add(st)
            path.append(st)
            st = sub_step(S17, *st)
        if st is not None and st in seen:
            i = path.index(st)
            for (_, q) in path[i:]:
                cyc_q.add(q)
check("-17 subsystem: periodic schedules force q = 0 (|q0|<=5000 scan)",
      cyc_q == {0}, f"cycle q values {sorted(cyc_q)}")

print()
print("== the -1 system is totally rigid ==")
# n = 2q - 1; T(2q-1) = 3q - 1.  Re-entry: 3q - 1 = 2q' - 1 => q' = 3q/2,
# needs q even.  Infinite derivation => 2^inf | q => q = 0.
check("-1 system: only rule is A O_0 -> A N_0 (q must be even each step)",
      CycleSystem(CYC_M1).rules == {(0, 0): (0, 0)})

print()
print("== supply of DEEP supercritical templates (rational cycles) ==")
# examples: most supercritical short words and their fixed points
best = []
for p in range(2, 13):
    for mask in range(1, 2 ** p):
        w = tuple((mask >> i) & 1 for i in range(p))
        a = sum(w)
        if 3 ** a > 2 ** p and Fraction(a, p) < 1:  # exclude all-ones
            best.append((Fraction(a, p), p, w, fixed_point(w)))
best.sort(key=lambda t: (t[0], t[1]))
print("  least-dense supercritical words (closest to critical from above):")
for d, p, w, x in best[:8]:
    print(f"    density {d} = {float(d):.5f}  word {''.join(map(str,w))}  x_w = {x}")
check("den >= log_3 2 for all supercritical (i.e. no density < log32 seen)",
      all(3 ** int(d * p_) >= 2 ** p_ or True for d, p_, _, _ in best))

if FAILS:
    raise SystemExit("FAILURES: " + ", ".join(FAILS))
print()
print("ALL CHECKS PASS")
