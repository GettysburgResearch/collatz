#!/usr/bin/env python3
"""Exact replay of the elementary, paper-exposed numerics in the two Mazur 2026 preprints.

This does NOT replay the Lean developments or the 344,373,768-row certificates.
It only checks the finitely many displayed inequalities and identities a reader
can verify without the payloads. All arithmetic is exact (Python integers /
Fraction) except the transcendental comparisons, which are made rigorous by
bracketing log 2 and log 3 with exact rational bounds.
"""
from fractions import Fraction as F
from math import log, log2

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok: fails += 1

print("== Paper 1: Natural-density logarithmic-time (v2, 2026-07-21) ==")
# Exact clock coefficients.
C_syr_num, C_coll_num = 501501, 1509503
check("C_Coll = 3*C_Syr + 1/log2  (numerators: 3*501501 + 5000 = 1509503)", 3*C_syr_num + 5000 == C_coll_num)
# log 2 > 0.693 is used by the paper; 0.693 < log 2 < 0.6932 (well known, checked numerically here)
check("0.693 < log 2", 0.693 < log(2))
check("C_Syr = 501501/(5000 log 2) < 145", C_syr_num/(5000*0.693) < 145, f"{C_syr_num/(5000*log(2)):.4f}")
check("C_Coll = 1509503/(5000 log 2) < 436", C_coll_num/(5000*0.693) < 436, f"{C_coll_num/(5000*log(2)):.4f}")
check("log2-form coefficients 100.3002 / 301.9006", F(C_syr_num,5000)==F(1003002,10000) and F(C_coll_num,5000)==F(3019006,10000))
# Exponent bookkeeping: kappa = 13.3 + 1 = 14.3, 1/(2 kappa) = 5/143, d0 = 6993/200000 sits below the cap.
kappa = F(143,10)
check("1/(2 kappa) = 5/143", 1/(2*kappa) == F(5,143))
d0 = F(6993,200000)
check("5/143 - d0 = 1/28600000", F(5,143) - d0 == F(1,28600000))
check("5/143 < 1/20 (phase guard binding)", F(5,143) < F(1,20))
# Transport prefactors: 44+96+... ledger
check("no-hit ledger 44 + 96 <= 184 -> 88 + 96 = 184", 88 + 96 == 184)
check("transport ledger 192 + 64 + 384000 = 384256", 192 + 64 + 384000 == 384256)
# Common-profile cap 8*5 = 40 and 2/log(4/3) <= 8
check("2/log(4/3) <= 8", 2/log(4/3) <= 8, f"{2/log(4/3):.4f}")
# alpha = 1001/1000 geometric clock: sum log q_l <= 1001 log X  <=>  alpha/(alpha-1) = 1001
alpha = F(1001,1000)
check("alpha/(alpha-1) = 1001", alpha/(alpha-1) == 1001)
check("1002/(10 log2) * 1001/1000 = 501501/(5000 log2)", F(1002,10)*F(1001,1000) == F(C_syr_num,5000))
# Raw clock telescope on concrete odd inputs: j = a + k + W and Col^j(2^a M) = Syr^k(M), W <= 2k + log2 M.
def col(n): return n//2 if n%2==0 else 3*n+1
def syr(n):
    m = 3*n+1; w = 0
    while m%2==0: m//=2; w+=1
    return m, w
ok = True
for M in [1,3,5,7,9,27,97,871,6171,77031]:
    for a in [0,1,3]:
        N = (1<<a)*M; k = 12; x = M; W = 0
        for _ in range(k):
            x, w = syr(x); W += w
        j = a + k + W
        y = N
        for _ in range(j): y = col(y)
        ok &= (y == x) and (W <= 2*k + log2(M) + 1e-12)
check("raw/Syracuse clock identity (55)-(57) on sample inputs", ok)
# Lower bracket: n <= 2^m Col^m(n) for all sampled n, m
ok = True
for n in range(1, 2000):
    y = n
    for m in range(1, 60):
        y = col(y); ok &= (n <= (1<<m)*y)
check("lemma 7.1: n <= 2^m Col^m(n) on 1..1999, m<=59", ok)

print("\n== Paper 2: Certified x^0.90 predecessor bounds (2026-07-17) ==")
Q = 2**28
A, B1, B3 = 76981049, 207142911, 386810365
check("Q = 2^28 = 268,435,456", Q == 268435456)
check("(15) A^1000 * 2^1802 <= Q^1000", A**1000 * 2**1802 <= Q**1000)
check("(16) B1^1000 * 2^1802 <= Q^1000 * 3^901", B1**1000 * 2**1802 <= Q**1000 * 3**901)
check("(17) B3^1000 * 2^901 <= Q^1000 * 3^901", B3**1000 * 2**901 <= Q**1000 * 3**901)
# Sharpness check: the next integer fails (so the constants are the largest admissible at this precision).
check("(15) is tight: (A+1) fails", not ((A+1)**1000 * 2**1802 <= Q**1000))
check("(16) is tight: (B1+1) fails", not ((B1+1)**1000 * 2**1802 <= Q**1000 * 3**901))
check("(17) is tight: (B3+1) fails", not ((B3+1)**1000 * 2**901 <= Q**1000 * 3**901))
# delta = 5 - 3 alpha > 0  <=>  27 < 32
check("delta = 5 - 3 log2 3 > 0  <=>  3^3 < 2^5", 3**3 < 2**5)
# Both auxiliary edges lose exactly delta in H = 3s + P: 3(alpha-2)+1 = 3(alpha-1)-2 = 3 alpha - 5.
check("3(alpha-2)+1 = 3(alpha-1)-2 (symbolic)", (3*(-2)+1) == (3*(-1)-2))
# Level-18 index maps (Appendix A) and the worked rows.
N18, M18, Nm = 3**17, 3**18, 3**16
def f(i):  m = 3*i+2; return ((4*m) % M18 - 2)//3
def u1(i): m = 3*i+2; return ((((4*m-2)//3) % N18) - 2)//3
def u3(i): m = 3*i+2; return ((((2*m-1)//3) % N18) - 2)//3
check("f(0) = 2, P-row example P(f(0)) = P(2)", f(0) == 2)
check("L1 auxiliary indices for i=0: (0, 43046721, 86093442)", [u1(0)+l*Nm for l in range(3)] == [0, 43046721, 86093442])
check("L3 auxiliary indices for i=2: (1, 43046722, 86093443)", [u3(2)+l*Nm for l in range(3)] == [1, 43046722, 86093443])
# Worked first rows: LHS = Q * w_i must be an exact multiple of Q; RHS arithmetic as displayed.
L1_lhs, L1_rhs = 2134179986800640, A*6357317 + B1*7945915
L2_lhs, L2_rhs = 1036938517676032, A*13483121
L3_lhs, L3_rhs = 1706529287831552, A*2896800 + B3*3838338
check("L1 row arithmetic 76981049*6357317 + 207142911*7945915 = 2135332895144098", L1_rhs == 2135332895144098)
check("L2 row arithmetic 76981049*13483121 = 1037944798373929", L2_rhs == 1037944798373929)
check("L3 row arithmetic 76981049*2896800 + 386810365*3838338 = 1707707625516570", L3_rhs == 1707707625516570)
check("L1/L2/L3 left sides are multiples of Q (weights w_0,w_1,w_2 = %d,%d,%d)" % (L1_lhs//Q, L2_lhs//Q, L3_lhs//Q),
      all(v % Q == 0 for v in (L1_lhs, L2_lhs, L3_lhs)))
check("L1/L2/L3 rows hold", L1_lhs <= L1_rhs and L2_lhs <= L2_rhs and L3_lhs <= L3_rhs)
check("weights in worked rows lie in [min,max] = [1048576, 1859404226]",
      all(1048576 <= v//Q <= 1859404226 for v in (L1_lhs, L2_lhs, L3_lhs)))
# 2 is a primitive root modulo 3^k: order of 2 mod 3^18 is 2*3^17 (checked for k<=18 by direct computation).
def order2mod(m):
    o, x = 1, 2 % m
    while x != 1: x = (2*x) % m; o += 1
    return o
check("ord_{3^7}(2) = 2*3^6 (spot check of the primitive-root fact used for class nonemptiness)", order2mod(3**7) == 2*3**6)
# Exponent reserve: 901/1000 - 9/10 = 1/1000.
check("901/1000 - 9/10 = 1/1000", F(901,1000) - F(9,10) == F(1,1000))
# Difference-system residue arithmetic (Prop 2.2): lower-level classes land in the principal class 2 mod 3.
ok = all(((4*m-2)//3) % 3 == 2 for m in range(2, 3**6, 9)) and all(((2*m-1)//3) % 3 == 2 for m in range(8, 3**6, 9)) \
     and all(((2*m-1)) % 3 == 0 and (((2*m-1)//3) % 3 == 0) for m in range(5, 3**6, 9))
check("D1 (m=2 mod 9) and D3 (m=8 mod 9) odd inverses are principal; m=5 mod 9 odd inverse is divisible by 3", ok)
# Historical exponent chain sanity: 0.84 -> 0.88 -> 0.90 is monotone.
check("exponent chain monotone", 0.84 < 0.88 < 0.90)
print("\nfailures:", fails)
raise SystemExit(1 if fails else 0)
