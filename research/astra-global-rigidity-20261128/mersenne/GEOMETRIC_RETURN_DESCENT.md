# A smaller state from a repeated multiplicative class on the same trajectory

Let $T(2n)=n$, $T(2n+1)=3n+2$. For an integer $b\ge2$ define $C_b(z)$ by removing all whole factors of $b$ from $2z+1$. Equal labels are equivalent to $(2y+1)/(2x+1)=b^k$ at some signed integer $k$. The principal example is $b=5$, where entire arbitrarily high powers can be erased. Define $r$ as the multiplicative rank of $2,3,b$. It equals 3 if $b$ has a prime factor greater than 3, and equals 2 otherwise.

**Return and physical descent.** Assuming the homogeneous rational-logarithm estimate in Chudnovsky's Corollary 1.2, let two sites $x,y$ on the same supplied positive shortcut trajectory be $d\ge1$ steps apart. If $C_b(x)=C_b(y)$ and every intervening state is at least $M$, then for every $\epsilon>0$
$$
                         d\gg_{b,\epsilon} M^{1/(r+1+\epsilon)}.       \tag{1}
$$
Thus, for any $\theta<1/(r+1)$ and any sufficiently large supplied source $n$, an observed return to the same label in at most $n^\theta$ steps, anywhere on its future trajectory, guarantees an actual state below $n$ in that interval. A finite traversal finds the smaller integer. The threshold in (1) is ineffective. Classical Matveev supplies the same qualitative implication with a smaller effective positive exponent depending on $b$. Neither return assertion requires first descent to have happened beforehand.

Write $w=z+1/2$. For a shortcut departing with parity $e\in\{0,1\}$,
$$
          \frac{2(Tz+1/2)}{3^e(z+1/2)}
                    =1+\frac{1/2}{3^e(z+1/2)}>1.
$$
Multiplication over the actual interval with $q$ odd departures gives
$$
       0< \Lambda=d\log2-q\log3+k\log b
          \le \frac d{2M}.                                            \tag{2}
$$
Each shifted height changes by a factor between $1/2$ and 2. Consequently $|k|\le d\log 2/\log b$, independently of the size of either endpoint or of their common factor. If $b$ has a prime divisor greater than 3 the three rational bases are multiplicatively independent, and Corollary 1.2 yields $\Lambda\gg_{b,\epsilon}d^{-3-\epsilon}$. Otherwise combine the fixed 2 and 3 exponents of $b$ into the first two coefficients and use rank two. The resulting integer vector is nonzero by the strict sign in (2). An integer coefficient zero does not change the estimate. This proves (1).

The recent input is a primary preprint from November 23, 2026. Chudnovsky states that his work with Claude proves a lower bound $C B^{-r-\epsilon}$ for each fixed list of $r$ independent positive rationals, where $B$ is the maximum coefficient height and the constant is ineffective. His Theorem 1.1 allows an additional integer constant; Corollary 1.2 sets it to zero. The published preprint attributes the two-logarithm homogeneous case to the earlier October paper. Appendix A.1 prints the Lean endpoint, and A.2 reports that its foundations are `propext`, `Classical.choice` and `Quot.sound`. We read the theorem and the reported audit, without replaying the ancillary project. The homogeneous estimate used here has exponent $r+\epsilon$, including when $r=3$. Paper 180 §6 previously used a two-logarithm return argument on a different thin family near $2\,3^j$; its bound and its high-minimum requirement concern those targets. [Chudnovsky, §1, §9 and Appendix A](https://arxiv.org/html/2611.30820v1) · [Earlier two-logarithm preprint](https://arxiv.org/abs/2610.28079) · [Paper 180, §6](https://rstation.ai/problems/collatz/papers/180)

### The same arithmetic label on the ordinary inverse entrance law

Suppose a fixed unit odd ray $a_0,a_1,\ldots$ escapes, with $a_i$ the successive odd states. Write $t_i$ for its actual shortcut arrival times, $t_0=0$. Choose an index $I$ uniformly in $\{J,\ldots,2J-1\}$ and then an actual ordinary inverse parent $X$ from the natural entrance law $Q_{a_I}$. Let $M_J$ be the minimum physical shortcut state from $t_{J-1}$ to $t_{2J}$. For every fixed $b$ and $\epsilon>0$, (1) gives
$$
 \max_h\Pr(C_b(X)=h)\ll_{a_0,b,\epsilon} J^{-1}+M_J^{-1/(r+1+\epsilon)}.
                                                                         \tag{3}
$$
Taking $b=5$ makes this a statement about the 5-free part of $2X+1$. In particular the mutual information in nats between $I$ and this coarser observation satisfies
$$
 \mathsf I(I;C_5(X))\ \ge\ \log\min\{J,M_J^{1/(4+\epsilon)}\}-O_{a_0,\epsilon}(1).
                                                                         \tag{4}
$$
Both lower-bound arguments diverge as $J\to\infty$ on a fixed escaping ray. The distribution sampled in (3) uses original ordinary parents.

Indeed $2^{t_i}a_i=\prod_{j<i}(3+1/a_j)\,a_0\le 4^i a_0$, so the full native duration through odd index $2J$ is $O_{a_0}(J)$. By (1), one label can occur at most $1+O_{a_0,b,\epsilon}(J/M_J^{1/(r+1+\epsilon)})$ times among the main parents $a_{I-1}$. For the move from the endpoint to its random true parent, write $d_i$ for the ordinary basin density of $a_i$. These positive densities increase to a finite limit. The conditional main-parent probability is $d_{i-1}/d_i$ by the fixed-root ordinary transition law. Thus
$$
 \Pr(X\ne a_{I-1})\le\frac{d_{2J-1}-d_{J-1}}{Jd_{J-1}}=o(1/J).
$$
This proves (3). The whole-ray Shannon estimate in PR 213 is $\sum_i\mathsf H(Q_{a_i}(X_1\in\cdot))<\infty$. Hence $\mathsf H(C_b(X)\mid I)=o(1/J)$ by data processing. The full label entropy is finite, bounded above by $\log J+\mathsf H(C_b(X)\mid I)$ and below by minus the logarithm of the largest label probability. This proves (4). [Ordinary path entropy, PR 213](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/ORDINARY_ENTROPY_BUDGET.md)

The growing information in (4) is information about an externally selected position on the moving ray. Summability concerns the uncertainty of the parent once its root is specified. An upper bound on the former statistic, or a reason that every supplied orbit must repeat one of the indicated classes within its descent window, is missing. For a finite example the trajectory of 27 contains the distinct odd states 27, 137 and 5 with $C_5=11$, since $55,275,11$ differ by powers of 5. They illustrate the label on ordinary states without estimating the analytic constants.
