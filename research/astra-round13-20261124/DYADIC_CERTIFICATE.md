# Kernel arithmetic for the finite dyadic budget

DyadicSubtotal.lean SHA-256 a86bb1ed94ade9741bb5a32ede55d631acd5fac69fb8ec3c80c48177907da785 passed Lean 4.34.1 (compiler commit 5045d0056413266e57c625dcd7c365b10e377c52), `lean -j1 -DwarningAsError=true DyadicSubtotal.lean`, exit 0. Both closed arithmetic declarations print empty axiom sets. They use `decide +kernel`.

For the shell n, set m=floor(log_3(2^(n−2))), T=sum_(j≥m) binom(n−1,j) and H=binom(n−1,m−1). T is the number of binary strings in the relevant binomial tail, before dividing by 2^(n−1). Begin at n=4 with m=1, T=7, H=1. When the shell doubles its dyadic threshold, the next clock is either m or m+1. It increases precisely when 3^(m+1)≤2·2^(n−2). Put J=H(n−m)/m=binom(n−1,m). Appending one bit and using the binomial boundary identity gives the following updates.

| Next clock | New tail count | New boundary coefficient |
|---|---:|---:|
| m | 2T+H | Hn/(n−m+1) |
| m+1 | 2T−J | H+J |

The total accumulator doubles the previous subtotal numerator on each shell and adds the new tail count only for shell n≥69. Its denominator after shell n is 2^(n−1). After 507 iterations, shell 511 is reached, and the closed strict integer comparison gives the upper bound 335142/10^6 on one third of the finite subtotal. The second closed comparison is exactly 8r^64/(3(1−r))<3/10^6 for r=390625/497664.

The kernel checks both stated finite integer comparisons. The correspondence of its recursive fields with the binomial coefficients and the common-denominator subtotal is the written induction above. A separate Python check also compared every T, H, 2^(n−2), 3^m, and the two bounding powers at all 508 shells 4 through 511 with direct integers.
