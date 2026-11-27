# Ordinary mergers with bounded difference between clocks

Let $T,P,D$ and linkage have their definitions from [the finite-class theorem](README.md). The following assertions concern equality of actual ordinary endpoints.

**Theorem.** Fix any positive integers $w,y$ and nonnegative integer $B$. If the forward orbit of $y$ is not eventually periodic, only finitely many exponents $r$ admit clocks $h,k\ge0$ with

$$
 T^h(3^rw)=T^k(y), \qquad |h-k|\le B .
$$

There is no restriction on either clock, on the two words, or on the number of their odd departures.

**Proof.** Every source satisfying this equality has a non-eventually-periodic orbit and hence both prefixes are simple. Define the integers $d=h-k$ and $g=r+P_h(3^rw)-P_k(y)$. Exact endpoint evaluation gives

$$
 3^g=2^d\,\frac{yD_k(y)}{wD_h(3^rw)},\qquad
 |g\log 3-d\log 2-\log(y/w)|\le160 .
$$

The inequality follows since both natural log corrections are in $[0,160]$. There are only finitely many pairs $(d,g)$ for $|d|\le B$. For any two sources with the same pair, advance their reference clocks to the later of the two $k$'s. Both source clocks are now equal to that reference clock plus $d$, the endpoints agree, and both accumulated source grades equal the reference odd count plus $g$. The two sources are linked. Each such fiber is contained in one finite class on the fixed tower by Theorem 1. For even $w$, the identical initial halving steps on all arms may be removed, as proved in its even-base corollary. This proves finiteness.

In particular the ordinary common-clock coalescence class of every non-eventually-periodic fixed reference meets any fixed tower only finitely often. If infinitely many points on one tower belong to a given nonperiodic ordinary component, their clock differences relative to a fixed reference in that component eventually leave every bounded interval. For an eventually periodic reference the ordinary clock-lag assertion can fail because one arm can repeatedly traverse the cycle while the other approaches it.

## An explicit slope separation above a verified range

For every finite simple path the following numerical bound on its odd inputs holds:

$$
 \sum_{\substack{n\ \mathrm{odd\ departed}\\n\ge 2^{64}}}\frac1n
 <\frac{29}{10}<3 .                                                    \tag{1}
$$

Here the small finite calculation concerns 1,936 binomial sums alone. It does not enumerate Collatz trajectories. Let $N_o(X)$ count all odd departed states at most $X$. For $65\le j\le2000$ set $p=\lfloor3j/5\rfloor-1$. Discard the last at most $j$ departures that do not have a $j$-step endpoint on the simple segment. At each remaining odd input the first bit of the $j$-step word is 1. Among the integers $1,\ldots,2^j$ there are exactly

$$
 H_j=\sum_{k=p}^{j-1}{j-1\choose k}
$$

such words with more than $p$ odd steps. With at most $p$ odd steps, the $j$-step endpoint is at most $3^p+(3/2)^p$. Indeed the homogeneous part is at most $3^p2^{-j}n$, and the additive part starting at zero is at most $(3/2)^p-1$: deleting halving maps can only increase this additive part. Distinct observation times have distinct $j$-step endpoints. Consequently

$$
 N_o(2^j)\le U_j=j+H_j+3^p+\lfloor(3/2)^p\rfloor .
$$

Layer cake, subdivided at powers of two, bounds the portion of the integral between $2^{64}$ and $2^{2000}$ by $\sum_{j=65}^{2000}U_j/2^j$, since the integral of $dt/t^2$ on $[2^{j-1},2^j]$ is $2^{-j}$. Above $2^{2000}$ the elementary estimate $N_o(t)\le6t^{79/80}$ contributes at most $480\cdot2^{-25}$. Exact integer arithmetic verifies

$$
 10\left(\sum_{j=65}^{2000}2^{2000-j}U_j+480\cdot2^{1975}\right)<29\cdot2^{2000}.
$$

The checker computes each binomial tail from its first coefficient with the usual integer recurrence and compares the scaled integers. [Reproducible check](check.py)

It follows that $1\le D<e^{29/30}<3$ on every simple prefix whose odd departures are at least $2^{64}$. For two such prefixes on the same tower meeting at the same clock, $3^{r+P_h(x_r)-s-P_h(x_s)}=D_h(x_s)/D_h(x_r)$ lies strictly between $1/3$ and 3. Hence the exponent is zero: the ordinary merger is automatically augmented. This implication for high paths uses only (1).

Bařina reports exhaustive convergence verification through $2^{71}$; the present project has not repeated that computation. Using this published finite input, every non-eventually-periodic orbit stays above $2^{64}$, and hence ordinary same-clock meeting and linkage coincide on every such tower component. For unequal clocks a bounded difference still permits several integral exponent differences, as in the theorem above. [Bařina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81 (2025)](https://doi.org/10.1007/s11227-025-07337-0)

Neither this equality nor finiteness of the bounded-lag fibers rules out an ordinary merger at unbounded clock difference. For a first tower failure, the ordinary frontier asks for some merger to a good lower source. The component and lag statements isolate restrictions on possible witnesses without establishing their existence.
