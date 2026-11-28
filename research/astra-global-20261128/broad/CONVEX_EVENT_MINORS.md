# Consecutive event minors at the binary, ternary and ordinary places

**Written finite theorem.** Start at an ordinary nonnegative even $x$. Number its even inputs from zero, put $t_j$ for their times, $u_j=t_j-j$, $g_j=u_{j+1}-u_j$, $p_j=2^{t_j}/3^{u_j}$, $S_j=\sum_{l<j}p_l$, and $y=-(x+1)$. Fix $H>n\ge1$ and observe actual inputs through $t_{H+n+1}$. Assume $u_{H-n}>0$, $g_j\ge2$ across $H-n\le j<H+n+1$, and $g_{j+1}-g_j\ge1$ whenever both gaps occur there. In addition assume $u_{H-n-1}<u_{H-n}$, needed to identify the earliest ternary denominator exactly.

Take the $n$ rows $a_{ik}=p_{H+i-k}$ ($1\le i\le n$, $0\le k\le n$). Append the row $a_{0k}=y-S_{H-k+1}$ on top and call the resulting determinant $F$. Let $G$ be the greatest common divisor, away from the primes 2 and 3, of all the numerators of the $n$-row maximal minors in lowest terms. At least one such minor is nonzero by strict binary rearrangement. Put
$$D=\sum_{i=0}^n u_{H-n+2i}.$$
Then
$$ v_2(F)=(n+1)t_{H+1},\qquad v_3(F)=-D,\qquad
  2^{(n+1)t_{H+1}} G\le 3^D(n+1)!(x+1+S_{H+1})p_H^n. \tag{1} $$
This requires no real sign condition on $F$ or its cofactors.

**Proof.** Subtract all $n$ lower rows from the top one. Its $k$th entry becomes $y-S_{H+n+1-k}=-p_{H+n+1-k}(T^{t_{H+n+1-k}}x+1)$ by finite calibration. The terminal state is even, so the added row now has binary valuations $t_{H+n+1-k}$. Move it to the bottom. With rows indexed $1,\ldots,n+1$ and columns $0,\ldots,n$, strict convexity of $t$ makes the aligned pairing $k=i-1$ the unique minimum of $\sum_i t_{H+i-k}$. Indeed exchanging inverted columns assigns the same sum of two indices less disparately, reducing the sum of their strictly convex costs. Every binary summand has an odd unit at its expected valuation. The unique minimum gives the first equality.

In the original top row, $p_{H-k}$ has strictly larger ternary denominator exponent than all earlier terms and the integer $y$. Therefore $v_3(y-S_{H-k+1})=-u_{H-k}$. With rows now indexed $0,\ldots,n$, the reverse pairing $k=n-i$ uniquely **maximizes** $\sum_i u_{H+i-k}$ by the same exchange in the opposite direction. Its valuation is strictly smaller than that of every other term, yielding $v_3(F)=-D$. All denominators are powers of three. The integer $3^D F$ is divisible by $G$ by expansion in the first row and localization away from 2 and 3; it is also divisible by $2^{(n+1)t_{H+1}}$.

Finally $j\mapsto \log_2 p_j=j-(\log_23-1)u_j$ is concave and nonincreasing in the relevant window. For each permutation of the lower rows into $n$ distinct columns, the average of its $n$ indices $H+i-k$ is at least $H$, since $\sum k\le1+\cdots+n$. Piecewise-linear concavity gives $\prod_i p_{H+i-k_i}\le p_H^n$. The original top row has absolute entries at most $x+1+S_{H+1}$. Expanding the determinant proves the size inequality in (1).

**The unaccounted primes.** Write $\gamma=\log_23$. Up to $\log_2((n+1)!)$ the exponent payoff from (1) is
$$ t_H+(n+1)(1+g_H)-\gamma u_H-\gamma \sum_{i=0}^n(u_{H-n+2i}-u_H)+\log_2 G. \tag{2} $$
If all relevant second differences are at least $\kappa$, subtract $\kappa\binom{j}{2}$ before using convexity and symmetry around $H$. It gives $\sum_i(u_{H-n+2i}-u_H)\ge\kappa n(n+1)(n+2)/6$. Common binary and ternary factors alone cannot improve (2): scaling every cofactor by $2^a3^b$ changes the three log sizes by quantities summing to zero in the product formula.

For orientation, on a profile with $1\le g_{j+1}-g_j\le J$ globally and fixed $g_0$, the payoff computed **without** $G$ tends to minus infinity as $H\to\infty$, uniformly for $1\le n<H$. Indeed $g_H=O_J(H+g_0)$, $u_H\ge\binom H2+Hg_0$, and the maximum over real $n\ge0$ of $O_J(n(H+g_0))-\gamma n^3/6$ is $O_J((H+g_0)^{3/2})$. Thus the leading negative quadratic contribution $-(\gamma-1)u_H$ dominates. This identifies the arithmetic missing from this particular cofactor bound, without excluding alternative determinant families.

**The exact quadratic case recovers the missing scale.** Suppose $u_j=bj+h\binom j2$ on all indices used by the $n$ lower rows. After removing row and column rational factors supported on $\{2,3\}$, these rows are the evaluations of the monomials $X^k$ at $X_i=(3/2)^{hi}$. Every maximal minor is divisible, in $\mathbb Z[1/6]$, by the Vandermonde product. Omitting the last column gives exactly that product and identifies the common divisor outside $\{2,3\}$:
$$G=\prod_{d=1}^{n-1}(3^{hd}-2^{hd})^{n-d}.$$
Consequently $\log_2G=\gamma h(n^3-n)/6+O_h(n)$, by summing $(n-d)\log_2(1-(2/3)^{hd})$. This cancels the leading cubic convexity penalty in (2). The same factorization need not survive independent bounded perturbations of the exponents. A global improvement would require enough remaining divisibility, a smaller archimedean determinant, or a different family of correlated certificates. The previous box-and-sign restriction and the finite identity here impose different hypotheses.
