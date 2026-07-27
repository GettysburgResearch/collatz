"""X-6240 — attack the coefficient-stopping-time question quantitatively.

chi(n) = min{j : k_j(n) < alpha j}   (coefficient stopping time)
sigma(n) = min{j : T^j(n) < n}       (stopping time);   chi <= sigma always (L-6173a).
The open question is whether chi = sigma for all n > 1.

L-6173(b): chi(n) < sigma(n) iff, at j = chi(n),   n * D <= c_j ,  D = 2^j - 3^{k_j} >= 1.
Since n is determined mod 2^j by its word w, and the least positive element r_w of that class
is equidistributed in [1, 2^j], the expected number of counterexamples with chi = j is

    E_j  =  sum_w  min(1, c_w / (D_w * 2^j))

over words w of length j that stay above the line for i < j and drop below at j.

sum_w c_w is computable EXACTLY by dynamic programming, because c evolves by
    c <- 3c + 2^t   on a 1-step,     c <- c   on a 0-step,
so N[t][k] (word count) and S[t][k] (sum of c) satisfy a linear recursion.  No sampling.
"""
import math
from math import ceil

ALPHA = math.log(2)/math.log(3)


def analyse(J):
    """Return per-j expected counterexample counts, exactly."""
    out = []
    for j in range(2, J+1):
        # DP over t = 0..j-1 with the above-line constraint enforced for t = 1..j-1
        N = {0: 1}          # k -> count
        S = {0: 0}          # k -> sum of c
        for t in range(j):
            N2, S2 = {}, {}
            for k, cnt in N.items():
                s = S[k]
                # 0-step
                N2[k] = N2.get(k, 0) + cnt
                S2[k] = S2.get(k, 0) + s
                # 1-step
                N2[k+1] = N2.get(k+1, 0) + cnt
                S2[k+1] = S2.get(k+1, 0) + 3*s + (1 << t)*cnt
            # enforce above-line at time t+1, EXCEPT at the final step t+1 = j
            if t+1 < j:
                need = ceil(ALPHA*(t+1) - 1e-12)
                N2 = {k: v for k, v in N2.items() if k >= need}
                S2 = {k: S2[k] for k in N2}
            N, S = N2, S2
        needj = ceil(ALPHA*j - 1e-12)
        E = 0.0
        words = 0
        for k, cnt in N.items():
            if k >= needj:
                continue                      # did not drop below: chi > j
            D = (1 << j) - 3**k
            if D <= 0:
                continue
            words += cnt
            # sum over the words of min(1, c/(D*2^j)); use the mean c as the estimator
            E += S[k]/(D * float(1 << j))
        out.append((j, words, E))
    return out


rows = analyse(34)
print(f"{'j':>4} {'above-line words dropping at j':>31} {'E_j':>14} {'cumulative':>14}")
cum = 0.0
for j, w, E in rows:
    cum += E
    if j % 2 == 0 or j < 8:
        print(f"{j:>4} {w:>31,} {E:>14.6e} {cum:>14.6f}")
print(f"\ntotal expected counterexamples with chi <= {rows[-1][0]}: {cum:.6f}")
ratios = [rows[i][2]/rows[i-1][2] for i in range(1, len(rows)) if rows[i-1][2] > 0]
print(f"E_j ratio over the last 10 j: "
      f"{[f'{r:.3f}' for r in ratios[-10:]]}")
print(f"mean ratio (last 10): {sum(ratios[-10:])/10:.4f}")
