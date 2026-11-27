# A quantitative mismatch bound for subpower rank offsets

Let $P\to\infty$ through positive ordinary Collatz cycles of canonical height at most one, allowing accelerated valuation three. For a proper chronological lag $h$ write $\epsilon_h=P^{-1}\#\{i:e_i\ne e_{i+h}\}$, and let $t$ be the smaller of its two complementary nonzero rank offsets. Suppose $\log t/\log P\to v<1$ and $\epsilon_h\to\epsilon$ along any subsequence. If $M$ is an upper bound for the irrationality exponent of $\log_2 3$, then
$$
 H(\epsilon)+\epsilon\log2\ \ge\ \frac{\log3}{M-1+v}
 \qquad\text{whenever }0\le\epsilon\le2/3.                         \tag{1}
$$
Here $H$ is binary entropy in nats with $H(0)=0$. In particular, for every sequence of lags with $t=P^{o(1)}$,
$$
 \liminf\epsilon_h>1/17\quad\text{using the published 2018 bound},\qquad
 \liminf\epsilon_h>5/32\quad\text{using the separately quoted }M=3. \tag{2}
$$
Half these respective fractions give the corresponding strict lower limits for cyclic windows whose length-$h$ exponent sum differs from any prescribed integer. Reversing chronological orientation leaves mismatches unchanged. Both statements use strict rank convexity and require no integral Subspace Theorem. The conditional statement at $M=3$ retains the named 2026 irrationality input.

## The scale of a short positive gap

Use the fundamental labels $L_r$ from the strict convexity theorem, extended by $L_{r+P}=2L_r$. Put $g_r=L_{r+1}-L_r$, $G_r=L_{r+t}-L_r$ and $X=\max_i x_i$. The strict curvature gives $0<g_0\le g_r<2g_0$ on the fundamental octave; the second octave has gaps less than $4g_0$. Since $Pg_0\le\sum_{r<P}g_r=L_0\le2X$, for every fundamental $r$,
$$
 0<G_r<4tg_0\le8tX/P .
$$
This remains true when the interval of $t$ adjacent gaps crosses the seam. The gap values are distinct by strict convexity. Take the common mechanical record length $b=\lceil\log_3(1+8tX/P)\rceil$. A length-$b$ word of mechanical divisors and signed drifts determines its terminal gap modulo $3^b$ by its exact affine recurrence. Because the gap is positive and bounded by $8tX/P$, its terminal value is uniquely determined by the residue. Uniform cyclic starting rank therefore gives terminal entropy exactly $\log P$.

At fixed starting phase cell the mechanical schedule and the wrap of the rank-$t$ pair are fixed. Their whole-window entropy costs $O(\log(b+1))$. At a given site write $w=z_{r+t\bmod P}-z_r-\mathbf1_{r+t\ge P}$. With the wrap known, exactly three $w$ values are possible. Given $w$ and the wrap, only a wrapped equal-grade pair is ambiguous, with at most two possible drifts. Its mean proportion is at most $t/P$. The conditional profile entropy for $0<y\le1$ is at most
$$
 b\big[\log(1+2y)-\epsilon_h\log y\big]+O_y(1).
$$
Indeed one retains a factor $y$ for every change of $w$, exactly an exponent mismatch. For a given preceding symbol the sum of the weights of the three possible next symbols is at most $1+2y$. The first factor is at most three, and entropy against this weighted count gives the displayed estimate. These are the profile and ambiguity estimates of the two-orientations manuscript, applied to the smaller actual interval. For $v<1$ we have $t/P\to0$, and $b\le [(M-1+v+o(1))/\log3]\log P$ since the cycle cap and the Diophantine input give $X\le P^{M+o(1)}$. Also $b\to\infty$ because $G_r$ takes $P$ distinct positive integer values. Divide the entropy inequality by $b$, then minimize over $y\in(0,1]$. The optimum at $y=\epsilon/[2(1-\epsilon)]$ for $0<\epsilon\le2/3$ gives (1). The endpoint $\epsilon=0$ follows by taking $y\downarrow0$. Rates above $2/3$ already exceed (2).

The function on the left of (1) is continuous and strictly increasing below $2/3$. For $M=5.116201$, use $M-1<33/8$. The exact comparison
$$
 17^{561}2^{33}<16^{528}3^{136}
$$
gives $(33/8)[H(1/17)+(\log2)/17]<\log3$. For $M=3$ the integer comparison
$$
 32^{64}2^{10}<5^{10}27^{54}3^{32}
$$
gives $2[H(5/32)+(5/32)\log2]<\log3$. Compactness excludes an entire neighborhood of each contrary endpoint. For each proper lag the successive window sums differ by $e_{i+h}-e_i$, and each window sum unequal to a given $B$ can account for at most two such mismatches.

## Review of the unrestricted-offset consumer

I also checked the frozen original `CONVEX_RANK_CONSUMERS.md` at SHA-256 `c9cac812d35845b40ca10f8a9a24e9c45a6918e8b96c8aa81ed7b2a260a0c56c`. Its all-lag argument uses the common upper gap scale $4X$ and singleton gap fibres. Substitution into the two-orientation entropy estimates gives the stated strict fractions $1/1000$ and $1/36$ without an earlier height lower input or separated source estimate. Its independent spacing bound $g_0\ge P$ follows from $P$ increasing integers in $[g_0,2g_0)$. The asserted lower bound for $L_0$ follows by summing $g_r\ge g_0+r$. The displayed arithmetic-progression counterexample for third differences follows actual accelerated odd trajectories, with columns overlapping after two steps of the shortest calendar, and genuinely reverses third-difference sign while first and second differences stay positive. These are local physical segments, without an asserted global cycle. The present improvement (1) additionally changes the terminal congruence horizon to the true sublinear-offset scale.

The exact checker verifies the two new entropy comparisons, all three earlier endpoint comparisons, the wrap interval on finite doubled convex arrays, and the displayed physical third-difference chain directly from ordinary odd iteration. The author source replay independently reproduces all six five-letter calendars. [Published 2018 linear-form input](https://m.mathnet.ru/links/79505d0269e906a6bf62eae1d2929560/cheb619.pdf) · [Conditional exponent-three input](https://arxiv.org/html/2610.28079v1#S11)

Prepared by the independent all-height auditor, 27 November 2026 UTC.
