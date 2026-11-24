# Canonical scalar complexity forces prefix growth

**Status.** Proposed written theorem for each fixed ordinary nonperiodic odd orbit. The finite separation and window-counting statements are checked in [CanonicalWindows.lean](CanonicalWindows.lean). Escape and nonstandard cycles remain open.

## Sources and definitions

Use the actual positive odd map $2^{a_i}q_{i+1}=3q_i+1$, with $a_i=v_2(3q_i+1)$. The actual discounted scalar and its normalized digits satisfy

$$
h_i=\sum_{j\ge0}a_{i+j}/3^{j+1},\qquad
h_i=c_i+f_i,\quad \tfrac12<f_i\le\tfrac32,\quad
b_i=3f_i-f_{i+1}\in\{1,2,3\},\quad
a_i+c_{i+1}=b_i+3c_i.
$$

The sources are PR182 at f94a2ae1caba9a1857feda892ee1779695eea9d2, research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md, and PR188 at beed685ab713923191ae40c9559bf7400298d2d3, research/scalar-carry-cocycle-20261124/SCALAR_COCYCLE.md. Define

$$
B_N=\sum_{i<N}b_i,\quad K_N=\sum_{i<N}c_i,\quad
P_N=3^N2^{-B_N},\quad R_N=\max_{i\le N}P_i,\quad M_N=\max_{i\le N}q_i .
$$

Write $p_b(m)$ for the number of distinct length-$m$ factors of the infinite canonical digit sequence and $\kappa=\lim_{m\to\infty}m^{-1}\log p_b(m)$. The limit exists by subadditivity. Logs are natural unless a base is shown.

For a single injective orbit, PR182 at cbec52dde5bed390a693310dd04e911033ba0cc9, research/phase-packing-round12-20261124/README.md, R12-1, establishes

$$
E_N=\prod_{i<N}(1+1/(3q_i))\le E_*<\infty,\qquad
q_i/(1+\log q_i)^\gamma \le C P_i,\quad \gamma=\log_3 4. \tag{1}
$$

The product bound uses the global occupation count for the same injective orbit. Source-dependent constants suffice. These analytic inputs retain their upstream written-proof status.

## CW1. Finite packing with all nonzero carries charged

Fix $0\le m\le N$ and suppose $q_0,\ldots,q_N$ are distinct and below $3^m$. Let $p_{b,N}(m)$ count the length-$m$ factors starting from 0 through $N-m$. Then

$$
N-m+1\le p_{b,N}(m)+(m+1)\#\{0\le i\le N:c_i>0\}
\le p_{b,N}(m)+(m+1)(K_N+1). \tag{2}
$$

An index with $c_i>0$ meets at most $m+1$ closed vertex intervals $[j,j+m]$. On every interval meeting none, all $m$ actual gaps equal their canonical digits. Equal actual words give congruent endpoints modulo $3^m$. Start modulo 1, multiply the congruence before each edge by 3 (gaining one power), add 1 and cancel the common power of 2, a ternary unit. Distinct endpoints below the modulus consequently require distinct words. The final $+1$ in (2) is the indicator at $N$; no bound on the size of $c_N$ is required.

## CW2. Entropy lower bound on scalar prefix expansion

For every injective ordinary odd orbit, put $\ell=\log_2 3$, $u=\ell-1$, and let $z$ be the positive root of $(2-u)z^2+(1-u)z-u=0$. Set

$$
H_3=\log(1+z+z^2)-u\log z=0.9649092013\ldots .
$$

Then

$$
\boxed{\liminf_{N\to\infty}\frac{\log R_N}{\log N}
\ \ge\ \frac{\log3}{\min(\kappa,H_3)}
\ \ge\ \frac{\log3}{H_3}
=1.1385654599\ldots .} \tag{3}
$$

A zero denominator means $+\infty$. Every escaping ordinary orbit with subexponential canonical factor complexity must have $R_N$ eventually above *every* fixed power of $N$, even when the canonical lower mean is strictly subcritical. The exponent in (3) is for the maximum canonical prefix expansion.

**Proof.** The normalized height $X_i=q_i2^{-c_i}$ satisfies $X_i\ge1$. Indeed $c_i<1/2+(\log_2 q_i)/3$. When $c_i\ge1$ this gives $\log_2 q_i>3c_i-3/2\ge c_i$, and $c_i=0$ is immediate. The exact ordinary product and the summed carry equation give

$$
X_N=X_0 P_N4^{-K_N}E_N,\qquad
2K_N\le \log_2 P_N+\log_2(X_0 E_*). \tag{4}
$$

In particular $P_N$ is bounded below by a positive constant, so $B_N\le\ell N+O(1)$.

Assume $R_N\le N^A$ along an unbounded sequence, for some fixed $A>0$. Equations (1) and (4) give $K_N=O(\log N)$ and $M_N\le N^{A+o(1)}$. For the latter bound, inversion of $x/(1+\log x)^\gamma\le C N^A$ first gives $x=O(N^{2A})$, then $x=O(N^A(1+\log N)^\gamma)$. Take $m=\lfloor\log_3 M_N\rfloor+1$. Injectivity gives $M_N\ge N+1$, thus $m\to\infty$, $m\le(A/\log3+o(1))\log N$, and eventually $m\le N$. At most $O((\log N)^2)$ windows contain a positive carry. Equation (2) gives $p_b(m)\ge N-o(N)$, so $A\kappa\ge\log3$.

A second count uses the finite canonical alphabet. Averaging the digit sums in these same windows gives mean at most $m B_N/(N-m+1)\le m(\ell+o(1))$. For each fixed $\epsilon>0$, a positive fraction, depending on $\epsilon$, have sum at most $m(\ell+\epsilon)$ by Markov's inequality. Discard the $o(N)$ contaminated windows. The remaining $c_\epsilon N$ words are distinct. For every $0<s<1$, the total number of canonical words with sum at most $m(\ell+\epsilon)$ is bounded by

$$
[s^{-(u+\epsilon)}(1+s+s^2)]^m .
$$

This is the generating polynomial for $b_i-1$ with nonnegative coefficients. Choose $s=z\in(0,1)$, which minimizes the expression at $\epsilon=0$. Take logarithms and then $\epsilon\downarrow0$. This gives $A H_3\ge\log3$. Taking every $A$ strictly above the possible finite lower exponent proves (3).

R12-2 already excludes zero-complexity critical-mean phases with polynomial prefix maxima on an unbounded sequence. It also gives lower bounds on *physical* heights involving the possible carry entropy at the global lower canonical mean. Equation (3) uses the carry count at a small *canonical prefix maximum* and bounds that maximum for every global mean.

**Pointwise refinement.** For $g=\log3/H_3$ and every sufficiently large $N$ on this same orbit,

$$
 R_N \ge c_{q_0} N^g(\log N)^{g/2-\gamma}. \tag{5}
$$

Here is the prefactor argument. If $R_N>N^2$ this is immediate since $g<2$ (for example the entropy of the two-letter distribution at mean $\ell$ is already greater than $\log3/2$). Otherwise the proof above gives $m=O(\log N)$, $m\ge\log_3(N+1)$ and $L=N-O((\log N)^2)$ distinct clean words. The mean of the excess cost $r=\sum(b_i-1)$ over these words is at most $m B_N/L-m\le mu+o(1)$. Put $T=\lfloor mu\rfloor+2$. Summing $(T+1-r)_+$ over *all* ternary words therefore gives an upper bound for $L$.

For $Z=1+z+z^2$ and $p_j=z^j/Z$, Fourier inversion for a polynomial gives the uniform coefficient bound
$$
 [x^r](1+x+x^2)^m \le C Z^m z^{-r}/\sqrt m .
$$
Indeed the squared modulus of $p_0+p_1 e^{it}+p_2e^{2it}$ is at most $1-2p_0p_1(1-\cos t)$, hence its $m$-th power in modulus is at most $\exp(-c m t^2)$ on $[-\pi,\pi]$. Integrating gives the stated bound. Summing the coefficients against $(T+1-r)_+$ costs the convergent factor $\sum_{d\ge0}(d+1)z^d$ and gives $L\le C e^{mH_3}/\sqrt m$. Since $3^m\le3M_N$, this implies $M_N\ge c N^g(\log N)^{g/2}$ in the small-$R_N$ case. Apply (1) at an index attaining $M_N$ and use $\log M_N=O(\log N)$ there. This proves (5). A simple exact substitute for the optimized entropy is $H_3\le\log(21/8)$, obtained by setting $s=1/2$.

## CW2a. The stationary law at the limiting exponent

Suppose $R_N\le N^{A+o(1)}$ along an unbounded sequence. Every stationary subsequential limit $\mu$ of the uniform empirical canonical-digit laws along that same sequence has mean $\ell$ and entropy rate $h(\mu)\ge\log3/A$. In particular, if $\log R_N/\log N$ tends to $\log3/H_3$ there, all fixed-length empirical canonical words converge to the independent product law with probabilities $(1,z,z^2)/(1+z+z^2)$. The same finite-word conclusion holds for the actual gaps at those clocks.

To see this, sample a length-$m$ word uniformly over the starting positions in CW2. Conditional on avoiding a positive carry the word is uniform on at least $N-o(N)$ distinct words. Conditioning reduces entropy, so the unconditional length-$m$ Shannon entropy is at least $(1-o(1))\log N$. Fix $k$. Split the sampled word into disjoint $k$-blocks and a remainder shorter than $k$. The law of each complete $k$-block differs by $O(m/N)$ in total variation from the law of a uniformly sampled $k$-block on the original prefix, uniformly over its offset. On the fixed finite alphabet, entropy is uniformly continuous. Subadditivity therefore bounds the length-$m$ entropy above by $(m/k)(H_{N,k}+o(1))+k\log 3$, where $H_{N,k}$ is that empirical $k$-block entropy. Formula (4) and the small-prefix assumption give $B_N=\ell N+O(\log N)$. At any subsequential limit, the mean is thus $\ell$ and $H_k(\mu)/k\ge\log 3/A$. Such limits are stationary since shifting the sampling range by one alters its law by $O(1/N)$. Take the infimum over $k$ to obtain the entropy rate bound.

At the stated limiting exponent, the lower bound equals $H_3$. Relative entropy with respect to $(1,z,z^2)/(1+z+z^2)$ gives one-letter entropy at most $H_3$ at this mean, with equality only for that law. The entropy rate can equal this one-letter entropy only if every finite block is independent. Uniqueness of all subsequential limits on a finite alphabet gives convergence. At most $(k+1)(K_N+1)=O_k(\log N)$ raw $k$-words can differ from their canonical partners, so the empirical raw laws have the same limits. This identifies a necessary same-source law at equality; ordinary realization of that law is unresolved.

## An oscillating scalar phase

The following irrational digit itinerary obeys the earlier prefix divergence and summability tests and has strictly subcritical lower canonical mean. Set $t_0=32768$ and $t_{k+1}=2^{\lfloor t_k/1024\rfloor}$. On $[t_k,2t_k)$ alternate 1,2. On each complementary interval restart the mechanical word

$$
b_i=1+\lfloor(j+1)(\ell-1)\rfloor-\lfloor j(\ell-1)\rfloor,
$$

where $j$ starts at zero on the interval. Let $\delta=\ell-3/2>0$. A length-$n$ mechanical prefix has sum $\ell n+O(1)$, and an alternating prefix has sum $3n/2+O(1)$. Thus $\log_2 P_n$ equals $\delta$ times the total number of alternating positions before $n$, up to $O(k+1)$ in the $k$-th pair. Earlier burst lengths sum to $o(t_k)$. At $2t_k$, the cumulative alternating proportion tends to $1/2$. This is its upper limit because the proportion increases in bursts and decreases between them. Hence $\liminf B_n/n=\ell-\delta/2<\ell$, while $B_{t_k}/t_k\to\ell$. The canonical word is not eventually periodic, so its corresponding centered ternary scalar is irrational.

At the end of each long complementary interval,

$$
\frac{\log R_{t_{k+1}}}{\log t_{k+1}}\longrightarrow 1024\delta
=87.0\ldots .
$$

The prefix maximum differs by at most $O(k+1)$ in its binary logarithm from the accumulated burst contribution. The same asymptotic ratio holds for $P_{t_{k+1}}$ itself. Also $P_n\ge c n^2$ for all sufficiently large $n$. During a burst use the inherited value $P_{t_k}\ge t_k^{80}$ eventually, bounded rounding error, and $n\le2t_k$. On the complementary interval $P_n\ge 2^{(\delta+o(1))t_k}$ and $n\le2^{t_k/1024}$.

Its length-$m$ windows have $O(1+\log m)$ switches uniformly. The switch positions $t_k,2t_k,t_{k+1},\ldots$ increase by at least a factor of two. For $r$ switches there are at most $(m+1)^r$ choices of cut positions. An alternating piece has at most two variants. A mechanical piece of a given length $l\le m$ has at most $l+1$ variants by the partition of the intercept circle by its $l+1$ boundary points. Therefore $\log p_b(m)=O((1+\log m)^2)$ and $\kappa=0$. Equation (3) excludes realization by any positive ordinary source, whatever its initial integer carry. An eventually periodic ordinary orbit would give a rational scalar directly.

## CW3. Local separation from triadic half-integers

For every positive ordinary source, any run of $n$ canonical digits all equal to 1, or all equal to 3, beginning at $q_j$, satisfies

$$
2^{n+c_j}\le q_j. \tag{6}
$$

Indeed $2^{b_i+2c_i}X_{i+1}=3X_i+2^{-c_i}\le4X_i$. Thus $2X_{i+1}\le X_i$ for a digit 3, and also for a digit 1 with $c_i\ge1$. For a run of 3s use $X_{j+n}\ge1$. For a run of 1s, use this same contraction until the first zero carry. While $b_i=1,c_i=0$, positivity of $a_i$ forces $a_i=1,c_{i+1}=0$. If $t$ such steps remain from $q_v$, then $2^t(q_{v+t}+1)=3^t(q_v+1)$. The endpoint is odd, so $2^{t+1}\mid q_v+1$, giving $q_v\ge2^t$ also for $t=0$. Combine the portions. This all-source proof uses no injectivity or global product bound.

Write $\|x\|=\inf_{k\in\mathbb Z}|x-k|$ for distance to the nearest integer and put $y=h_0-1/2$. Multiplication by 3 on $y\bmod 1$ has the right-closed ternary digit itinerary $b_i-1$. With $n=\lfloor\log_2 q_j\rfloor+1$, a distance strictly less than $3^{-n}$ from an integer would force $n$ extreme digits, contrary to (6). At an integer the right-closed representation gives digits all 2, also impossible. Hence

$$
\|3^j y\|\ge3^{-1-\lfloor\log_2 q_j\rfloor}.
$$

Since $q_j+1\le(3/2)^j(q_0+1)$, for every $j\ge0,k\in\mathbb Z$,

$$
\left|h_0-\frac{2k+1}{2\cdot3^j}\right|
\ \ge\ \frac{3^{-1-\log_2(q_0+1)}}{3^{j\log_2 3}} .
$$

This is a bound at the indicated denominators and numerators. It does not give a general irrationality exponent for $h_0$.

## Evidence and reproduction

Lean 4.34.1 (5045d0056413266e57c625dcd7c365b10e377c52), with mathlib d13f23b723b8a846827a245b89c10fc7d3f11612, compiled [CanonicalWindows.lean](CanonicalWindows.lean) and [ActualCanonicalWindows.lean](ActualCanonicalWindows.lean) with one worker and warnings as errors. The second module imports the literal scalar and carry definitions through ActualCarry and instantiates (2) for the original positive odd source. Its assumptions are finite injectivity and the displayed height cut. All three printed theorem axiom lists contain only propext, Classical.choice, and Quot.sound. CW2, CW2a, the example and CW3 are written proofs.

[canonical_window_controls.py](canonical_window_controls.py) produced [WINDOW_CONTROLS.json](WINDOW_CONTROLS.json) byte-identically in normal and optimized Python. The bounded tests use exact rational actual scalars obtained by tracing the 1,024 odd sources below 2,048 to one, then applying the scalar recurrence backwards. They check 49,649 finite windows, 19,131 extreme-run suffixes and 26,461 phase distances. The optimized analytic exponent is reported to twelve decimal places for orientation. An independent integer inequality checks the coarser strict bound $g>1138/1000$.

## Remaining implication

The results exclude prescribed scalar phases and force a uniform prefix exponent on a putative escaping orbit. No argument here bounds the prefix growth of every actual source from above or forces a contradiction for exponential-growth phases such as the low rational phase $7/8$. Nonstandard positive cycles are outside CW2.
