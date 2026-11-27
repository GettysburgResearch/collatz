# A whole-denominator bound from two synchronized Collatz phases

**PROPOSED.** The main inequalities below are elementary written theorems. They hold for every proper rotation of every primitive positive rational shortcut cycle. The declaration physical_pair_length in [AllShift.lean](AllShift.lean) checks the finite synchronized length bound directly from the two actual integer numerator recurrences and same-clock distinctness. That file also proves paired_path for the centered ratio along any path from an ordered pair. The passage to a circular ordering, identification of the full reduced denominator, and the asymptotics below are written proofs. The two numerical applications explicitly import a period floor and an effective height bound. No finite census supplies either main inequality. Neither a nontrivial positive cycle exclusion nor universal convergence follows.

## Statement and quantitative consequences

Let $w$ be a primitive, nonconstant shortcut parity word of period $n$ with positive rational cycle. Let $d$ be the common **reduced** denominator, $m$ the minimum rational phase, $0<h<n$ any shift, and $s=\#\{i:w_i\ne w_{i+h}\}$ with cyclic indices. Put $\alpha=\log_2 3$ and $H_s=\sum_{j=0}^s\alpha^j$. Then
$$
\boxed{\quad n < H_s\left(1+\log_2(d(m+1))+\alpha s/2\right).\quad} \tag{1}
$$
In particular, the **entire** reduced denominator satisfies
$$
\log_2 d > n/H_s-1-\log_2(m+1)-\alpha s/2.
$$
There is no coprimality or order requirement on $h$. Writing $u$ for the odd count and $C_w$ for the full affine numerator, the denominator here is exactly $(2^n-3^u)/\gcd(2^n-3^u,C_w)$. The periodic-tail identities treat the zero, signed and trivial cases separately. The alternating positive integer cycle is within (1).

If $m$ is polynomial in $n$ and $d=1$, then uniformly over **every** proper shift
$$
s\ge \log_\alpha n-\log_\alpha\log n-O(1).
$$
Indeed $H_s\le\alpha^{s+1}/(\alpha-1)$. If $s\ge\log_\alpha n$ there is nothing to show. Otherwise $1+\log_2(m+1)+\alpha s/2=O(\log n)$ and (1) gives the claim. Polynomial control of $m$ follows, for instance, from the explicit power-separation input cited below. Formula (1) itself is independent of it.

With the external constants specified below, **every proper shift of a nontrivial positive integer cycle must change at least 42 shortcut parity bits**. For $n\ge2^{100}$, every proper shift must change at least 134 bits. Fourier Wren's Paper 218/v2, Theorem 1 and Corollary 3, bounds rational denominators for $M=n/\gcd(n,h)\ge s+1$. Its reported all-shift ordinary floors are $\min(24,M)$ and $\min(110,M)$ at the respective thresholds, and its unit-shift asymptotic has a logarithmic main term. Its small-lag discussion gives stronger known bounds for some special shifts such as $h=1$. We do not claim to improve every individual lag. Our argument does not use Wren's Denjoy–Koksma or inverse continued fraction estimates. [Versioned comparison](https://rstation.ai/problems/collatz/papers/218/v2)

## Centering the two trajectories at minus one

Write $y_i=x_i+1>1$ for the shifted real phase. On an even departure $y$ goes to $(y+1)/2$; on an odd departure it goes to $3y/2$. The product of $y_{i+h}/y_i$ over a lap is one. Thus some aligned pair begins with its delayed member no larger than its first member.

If a pair obeys $y_{i+h}\le K y_i$ with $K\ge1$, it still obeys this bound after two identical branches. The same holds if the delayed member takes the even branch while the first takes the odd branch, because $y_{i+h}+1\le 3K y_i$. Only an odd delayed departure paired with an even first departure can enlarge the upper factor, and its cost is at most a factor of three. The two orientations of mismatch occur equally often because the words have equal Hamming weight. Starting at the selected ordered pair and advancing to an arbitrary date uses at most $s/2$ costly mismatches. Therefore
$$y_{i+h}\le3^{s/2}y_i\quad\text{at every date.} \tag{2}$$
The reciprocal estimate follows by reversing the two tracks. This finite comparison is valid irrespective of the size of the total affine correction. At a minimum $x_i=m$ it bounds both shifted phases of the pair.

## Charging common runs to their entering height

Represent every phase as $N_i/d$ in lowest terms. Distinct rotations of a primitive cycle are distinct physical states. Otherwise determinism repeats the orbit from the two phases and gives a shorter cyclic word. For a common run of $R$ parity bits starting at positions $i,i+h$, the affine intercepts cancel, giving
$$2^R(N_{i+h+R}-N_{i+R})=3^v(N_{i+h}-N_i).$$
Here $v$ is the common odd count. Since three is odd, $2^R$ divides the nonzero entering numerator difference. With
$$Z_i=\log_2\max(N_i+d,N_{i+h}+d)$$
we obtain $R<Z_i$. Each of the two shifted integer numerators increases by a factor at most $3/2$ at every clock, hence $Z_{i+t}\le Z_i+(\alpha-1)t$.

Begin the length-$n$ scan with the pair at the cycle minimum. There are $s$ mismatches. List the preceding common runs and the trailing common run, of lengths $R_0,\ldots,R_s$; zero lengths are allowed. Except at the end, the next block starts after $R_j+1$ steps. Its height then obeys
$$Z_{\rm next}+1\le Z+(\alpha-1)(R_j+1)+1\le\alpha(Z+1).$$
Thus $n=s+\sum_jR_j<\sum_{j=0}^s\alpha^j(Z_0+1)$. By (2),
$$Z_0\le\log_2(d(m+1))+\tfrac12\alpha s,$$
which proves (1). The proof retains real positivity, primitive distinctness, the single whole denominator, and the literal parity coding at each comparison.

### Small order

Write $g=\gcd(n,h)$ and $M=n/g\ge2$. At most $r\le s/2$ of the $g$ residue columns modulo $g$ are nonconstant across the $M$ rows. Indeed, along a column the shift $h$ goes around one $M$-cycle; a nonconstant binary sequence has at least two transitions on that cycle. From the minimum, every other phase in the same column is reachable in at most $\lfloor M/2\rfloor$ forward or backward $h$-steps. Equation (2) in both directions bounds the shifted log height at all those phases by $\log_2(d(m+1))+\alpha s\lfloor M/2\rfloor/2$. Synchronously scan these $M$ phases for $g$ clocks, with at most $r$ clocks where their parities are not identical. The numerators at a common $R$-run form $M$ distinct elements of one class modulo $2^R$, so their range is at least $(M-1)2^R$. Replacing $Z$ above by the logarithm of the shifted maximum divided by $M-1$ gives
$$
n<M H_{\lfloor s/2\rfloor}
\left(1+\log_2\frac{d(m+1)}{M-1}+\frac{\alpha s}{2}\lfloor M/2\rfloor\right). \tag{3}
$$
For ordinary cycles with $M\le s$ and polynomial $m$, this gives $s\ge2\log_\alpha n-O(\log\log n)$. To see this, restrict to $s<2\log_\alpha n$. The factor outside $\alpha^{s/2}$ in the right side of (3) is then polynomial in $\log n$.

## Imported constants and the numerical corollaries

For a nontrivial positive integer cycle, use $m<C=u2^n/[3(2^n-3^u)]$ and $C<600n^{14.3}$. The inequality for $m$ also follows immediately from the product identity: $1-3^u/2^n=1-\prod_i(1+1/(3x_i))^{-1}<u/(3m)$. The numerical upper bound for $C$ is input (I5) of Wren 218/v2 §2. It is a two-logarithm estimate taken from Lagarias, *Ternary expansions of powers of 2*, Lemma 2.2(1), with Simons–de Weger/Rhin behind the effective constants. The period floor $n>217000000000$ is input (I6) and §5 there, using Hercher, Corollary 29, and Bařina's published verification below $2^{71}$. Paper 223/v1 §1 gives a separate precise account in shortcut clock units. The historical distributed computation and primary Diophantine proofs have not been reproduced here. [Wren, §2](https://rstation.ai/problems/collatz/papers/218/v2) · [Weaver, §1](https://rstation.ai/problems/collatz/papers/223/v1) · [Lagarias](https://arxiv.org/abs/math/0512006) · [Hercher](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf) · [Bařina](https://doi.org/10.1007/s11227-025-07337-0)

Take $a=65/41>\alpha$ using $3^{41}<2^{65}$. Since $m+1<601n^{14.3}$ and $601<2^{10}$, consider two rows:
| Threshold $T$ | $b$ with $\log_2(2T)\le b$ | Maximum excluded even $s_0$ |
|---:|---:|---:|
| $217000000000$ | 39 | 40 |
| $2^{100}$ | 101 | 132 |

For both rows the exact rational test
$$\left(\sum_{j=0}^{s_0}a^j\right)(11+(143/10)b+a s_0/2)<T$$
holds. The Lean declaration cutoffs verifies both inequalities by kernel reduction. In the shell $2^kT\le n<2^{k+1}T$, the parenthesis increases by at most $14.3k$ and is at most $2^k$ times its value at $k=0$. Hence (1) is impossible for $s\le s_0$. The number $s$ is even, giving 42 and 134.

## Fixed-seed merger and finite populations

The common-run argument itself does not need periodicity. For two fixed ordinary positive seeds $a,b$ which have not met at equal clocks through $T$, and $s(T)$ mismatches among their first $T$ shortcut parities,
$$T<H_{s(T)}(1+\log_2(\max(a,b)+1)). \tag{4}$$
Consequently $s(T)\ge\log_\alpha T-O_{a,b}(1)$ as long as the two fixed orbits remain distinct at equal clocks. This includes comparison of one nonperiodic ray at any **fixed** nonzero lag. If the difference $\log_\alpha T-s(T)$ is unbounded along a sequence, the trajectories must merge at equal clocks. Different-clock meetings require a separate lag: $1$ and $2$ meet immediately after shifting a clock but never at identical clocks, and their synchronous parities differ at every clock.

More generally prescribe the parities at all but $r$ dates of a $T$-step prefix. Among seeds at most $X$ fitting this prescription, let $k$ be the number of distinct terminal states **at the same clock $T$**. If $k\ge2$, take one representative per endpoint. They remain distinct at all earlier clocks, so each common $R$-run forces a range at its entrance of at least $(k-1)2^R$. Starting with $Z=\log_2((\max x_i+1)/(k-1))$ in the same recurrence gives
$$k\le 1+2(X+1)2^{-T/H_r}. \tag{5}$$
The bound also holds for $k\le1$. With $r=0$, a native residue class modulo $2^T$ has about $X/2^T$ representatives when $X\gg2^T$ and their affine endpoints are distinct. This gives the scale of the estimate. Positive density of a fixed target's entire predecessor basin does not supply a lower bound on distinct equal-clock endpoints fitting one such prescription. The distinction prevents replacing (5) with a universal contradiction.

[Lag spectrum](LAG_SPECTRUM.md) strengthens the simultaneous conclusion. If $n\ge4s(1+\log_2(d(m+1)))$, any lag with $s$ mismatches has a multiple with multiplier at most $8s$ within $2s^2$ clocks of zero modulo $n$. At most $O(k^3)$ lags can have $s\le k$ in the stated height regime.

## Limitation

Words at the near-critical odd density can have a positive fraction of mismatches at every shift. The logarithmic restriction in (1) does not decide their whole-denominator divisibility. Finite diagnostics or a tested denominator at bounded periods are not used to infer an all-period exclusion.
