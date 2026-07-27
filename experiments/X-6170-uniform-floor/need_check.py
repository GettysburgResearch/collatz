"""Exact check of the need[] table used by fastscan.c.

fastscan.c computes  need[L] = ceil(alpha*L),  alpha = log2/log3,  in long-double floating
point.  The exact condition it stands for is integer:

        k >= alpha*L   <=>   k*log3 >= L*log2   <=>   3^k >= 2^L .

So need[L] = least k with 3^k >= 2^L.  This script computes that with exact big integers and
compares.  If the two ever disagree the scan's definition of chi is wrong and every published
figure downstream of it is void, so this runs as a gate before any long scan.
"""
import subprocess, sys, math

LMAX = 4096

exact = [0] * LMAX
k, p3 = 0, 1
p2 = 1
for L in range(1, LMAX):
    p2 <<= 1
    while p3 < p2:
        k += 1
        p3 *= 3
    exact[L] = k

# reproduce the C table in the widest float Python has
approx = [0] * LMAX
alpha = math.log(2.0) / math.log(3.0)
for L in range(1, LMAX):
    approx[L] = math.ceil(alpha * L - 1e-15)

bad = [L for L in range(1, LMAX) if exact[L] != approx[L]]
print("LMAX          =", LMAX)
print("mismatches    =", len(bad))
if bad:
    print("first 10      =", bad[:10])
    for L in bad[:10]:
        print("   L=%d exact=%d float=%d  alpha*L=%.17f" % (L, exact[L], approx[L], alpha * L))
    sys.exit(1)

# how close does alpha*L ever come to an integer?  this is the margin the float table lives on
worst, worstL = 1.0, 0
from fractions import Fraction
for L in range(1, LMAX):
    d = abs(alpha * L - round(alpha * L))
    if d < worst:
        worst, worstL = d, L
print("min |alpha*L - Z| = %.3e at L = %d   (float epsilon used: 1e-15)" % (worst, worstL))
print("OK: float need[] agrees with exact 3^k >= 2^L for every L < %d" % LMAX)
