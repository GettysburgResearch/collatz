"""THEOREM-GRADE computation: an upper bound on n for every counterexample with chi(n) = j.

A counterexample to chi = sigma has, at j = chi(n),   n <= c_w/D,  D = 2^j - 3^{k_j}.
So if  Bmax(j) = max over qualifying length-j words of c_w/D,  then every counterexample with
chi(n) = j has n <= Bmax(j).  Combined with the exhaustive verification n <= V, this gives

    no counterexample has chi(n) = j,  for every j with Bmax(j) <= V.

Single-pass DP: the above-line filter at time t does not depend on the target length j, so one
pass records, at each t, the states that have just dropped below (those are the j = t words).
"""
import math
from math import ceil
from fractions import Fraction
import sys

ALPHA = math.log(2)/math.log(3)
J = int(sys.argv[1]) if len(sys.argv) > 1 else 400
V = 2*10**9                      # exhaustive verification bound used here (conservative)

M = {0: 0}                       # k -> max c over above-line prefixes of current length
best_overall = Fraction(0); best_j = None
records = []
for t in range(J):
    M2 = {}
    for k, c in M.items():
        if M2.get(k, -1) < c: M2[k] = c
        v = 3*c + (1 << t)
        if M2.get(k+1, -1) < v: M2[k+1] = v
    j = t+1
    need = ceil(ALPHA*j - 1e-12)
    # states with k < need have just dropped below the line: these are the chi = j words
    Bmax = Fraction(0); bk = None
    for k, c in M2.items():
        if k >= need: continue
        D = (1 << j) - 3**k
        if D <= 0: continue
        r = Fraction(c, D)
        if r > Bmax: Bmax, bk = r, k
    records.append((j, Bmax, bk))
    if Bmax > best_overall:
        best_overall, best_j = Bmax, j
    M = {k: c for k, c in M2.items() if k >= need}

print(f"{'j':>5} {'k':>6} {'Bmax(j) = bound on n':>24} {'running max':>16}")
run = Fraction(0)
for j, b, k in records:
    if b > run:
        run = b
        if j % 1 == 0 and (j < 30 or float(b) > 1e3):
            print(f"{j:>5} {str(k):>6} {float(b):>24.4g} {float(run):>16.4g}")
print(f"\nrunning max at selected j:")
run = Fraction(0); marks = {}
for j, b, k in records:
    if b > run: run = b
    marks[j] = run
for j in (50, 100, 150, 200, 250, 300, 350, 400):
    if j in marks: print(f"   j <= {j:>4}:  every counterexample has n <= {float(marks[j]):.4g}")
# the decisive threshold
first_exceed = next((j for j, _, _ in records if marks[j] > V), None)
print(f"\nverification bound used: V = {V:.3g}")
if first_exceed:
    print(f"running max first exceeds V at j = {first_exceed}")
    print(f"=> THEOREM: no counterexample to chi = sigma has chi(n) <= {first_exceed-1}.")
else:
    print(f"running max never exceeds V for j <= {J}")
    print(f"=> THEOREM: no counterexample to chi = sigma has chi(n) <= {J}.")
