# Unbounded carry amortization on the actual discounted scalar

## Definitions and exact source

Use positive odd states $q_{i+1}=(3q_i+1)/2^{a_i}$ with $a_i=v_2(3q_i+1)$.
Use the actual scalar from PR182 at f94a2ae1caba9a1857feda892ee1779695eea9d2, research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md and ActualScalar.lean (R10-G1--G3):
$$
h_i=\sum_{k\ge0}\frac{a_{i+k}}{3^{k+1}},\qquad
h_{i+1}=3h_i-a_i,\qquad \frac12<h_i\le1+\frac{\log_2 q_i}{3}.
$$
These are actual-source identities, no independence or rationality assumed. Put
$$
c_i=\lceil h_i-1/2\rceil-1\in\mathbb N,\qquad f_i=h_i-c_i\in(1/2,3/2].
$$
The right-closed representative is important. Then
$$
b_i=3f_i-f_{i+1}\in\{1,2,3\},\qquad a_i+c_{i+1}=b_i+3c_i.
$$
Indeed $b_i$ is integral and strictly between 0 and 4. Writing $y_i=f_i-1/2\in(0,1]$, one has $y_{i+1}=3y_i-(b_i-1)$ with the right-closed convention. Thus $(b_i-1)$ is the canonical ternary digit itinerary of the centered fractional scalar, uniquely determined by $f_0$. The unbounded integer carries are the only extra variables in this relation.

## Theorem SC1 (all-reset carry cocycle)

For any integers $c,d\ge0$ with $d\le3c+2$,
$$
8^d(c+1)^4\le8^{3c}(d+1)^4.
$$
Proof: if $d\le c$, use $(c+1)^4\le2^{4c}\le8^{2c}$ and $(d+1)^4\ge1$. If $c\le d\le3c$, both factors are monotone in the required directions. For $d=3c+1$, use $8(c+1)^4\le(3c+2)^4$ since $3c+2\ge2(c+1)$. For $d=3c+2$, use $64(c+1)^4\le81(c+1)^4=(3c+3)^4$. These cases exhaust the hypothesis.

In the actual recurrence $d=c_{i+1}\le3c_i+2$ since $a_i\ge1$ and $b_i\le3$. Multiply the inequality by the appropriate power of 8 and cancel using $a_i+d=b_i+3c_i$. This gives
$$
8^{b_i}(c_i+1)^4\le8^{a_i}(c_{i+1}+1)^4.
$$
For every interval $[j,i)$, write $A_{j,i}=\sum_{k=j}^{i-1}a_k$, $B_{j,i}=\sum_{k=j}^{i-1}b_k$. Multiplication telescopes:
$$
\boxed{8^{B_{j,i}}(c_j+1)^4\le8^{A_{j,i}}(c_i+1)^4.}
$$
Equivalently, $2^{B_{j,i}-A_{j,i}}\le((c_i+1)/(c_j+1))^{4/3}$. No bound on the number of resets, maximum carry or interval length is imposed. The integer version is the intended finite Lean kernel.

## Theorem SC2 (physical height from canonical drawup)

Define a scalar-only maximum over all subintervals of a prefix:
$$
D_N=\max_{0\le j\le i\le N}\frac{3^{i-j}}{2^{B_{j,i}}}\ge1,\qquad
M_N=\max_{0\le i\le N}q_i.
$$
The empty interval is included. The exact affine iterate of the odd map gives, with $\chi_{j,i}=3^{i-j}/2^{A_{j,i}}$,
$$
q_i=\chi_{0,i}q_0+\frac13\sum_{j=0}^{i-1}\chi_{j,i}.
$$
SC1 gives $\chi_{j,i}\le D_N((c_i+1)/(c_j+1))^{4/3}$. Since $c_j+1\ge1$, $c_i+1<1.5+\log_2 q_i/3$ follows from the actual scalar bounds (the representative $f_i>1/2$). Therefore
$$
\boxed{M_N\le D_N(q_0+N/3)(3/2+\log_2 M_N/3)^{4/3}.}
$$
This is a deterministic real-height bound for the original ordinary source, not a distributional comparison.

## Theorem SC3 (escape requires scalar phase drawup)

Use the ordinary injective-segment packing theorem of PR185, scientific commit e04daab0a0ddd59c80f5d16a51b9943fd5149e6c, research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md, Theorem 4, equations (21)--(22). The theorem is unconditional and concerns actual odd orbit segments, not harmonic-flow sampling. With $\ell=\log_2 3$ and
$$
\theta=\frac{\ell\log\ell-(\ell-1)\log(\ell-1)}{\log3}=0.949955527188\ldots,
$$
it gives, for an injective segment, $N+1\le C(1+M_N)^\theta/\sqrt{\log(1+M_N)}$, with absolute $C$. Its inversion yields, for all sufficiently large $N$, $M_N\gtrsim (N+1)^{1/\theta}(\log(N+1))^{1/(2\theta)}$.

A deterministic nonperiodic orbit is injective. The function $x/(3/2+\log_2 x/3)^{4/3}$ increases on $x\ge1$, as is seen by differentiation. Combine this monotonicity and the packing bound with SC2. For any fixed positive odd initial source with nonperiodic orbit:
$$
\boxed{D_N\gtrsim_{q_0}N^{1/\theta-1}(\log N)^{1/(2\theta)-4/3}.}
$$
The polynomial exponent is about 0.05268086; the log exponent is about -0.80699. This forces drawup on the canonical ternary digit sequence independently of how the actual integer carries switch.

Corollary: if $D_N=O(N^\eta)$ along even an unbounded subsequence, for $\eta<1/\theta-1$, then the actual orbit is eventually periodic. In particular bounded canonical drawup is enough. Irrational actual scalars cannot be eventually periodic, since an eventually periodic gap sequence has rational discounted sum; they must therefore have the indicated drawup. A periodic canonical word whose mean gap exceeds $\log_2 3$ has bounded drawup. The corresponding nonperiodic exclusion is not a cycle exclusion.

## Self-contained version: exponent 1/32

The following weaker theorem requires no packing theorem from PR185, only the actual scalar facts and SC1--2. Suppose $D_N=O(N^{1/32})$ on an unbounded subsequence. Since $q_i\le 2^i q_0$, the log factor in SC2 is initially $O(N^{4/3})$. This gives a polynomial bound on $M_N$, then $\log M_N=O(\log N)$. Reapplying SC2 gives
$$
M_N=O_{q_0}(N^{33/32}(\log N)^{4/3})
$$
along the subsequence.

If the orbit is injective, telescope the complete actual equations:
$$
A_{0,N}=N\ell+\log_2(q_0/q_N)+\sum_{j<N}\log_2(1+1/(3q_j))
\le N\ell+O_{q_0}(\log N).
$$
Here the distinct positive integers $q_j$ have reciprocal sum at most the first $N$ harmonic sum. Let $m$ be the least positive multiple of five with $3^m>M_N$. Then $m=O(\log N)$. Across endpoints $m,\ldots,N$, the average cost of length-$m$ past gap words is at most $m A_{0,N}/(N-m+1)\le(159/100)m$ eventually, since $\ell<1.59$. Markov's inequality gives at least $1/160$ of the endpoints with cost at most $8m/5$.

A length-$m$ word of positive gaps determines its endpoint modulo $3^m$, by the full affine formula and invertibility of 2 modulo $3^m$. Since every endpoint lies below $3^m$, the low-cost words for distinct endpoints must be distinct. For $z=3/8$, their number is bounded by
$$
z^{-8m/5}(z/(1-z))^m
=(8^8/(3^3 5^5))^{m/5}<200^{m/5}\le200M_N^{\log_{243}200}.
$$
Thus $N-m+1\le160\cdot200 M_N^{\log_{243}200}$. The exact inequality $200^{33}<243^{32}$ yields $(33/32)\log_{243}200<1$, contradicting this bound as $N\to\infty$ on the chosen subsequence. Therefore the orbit is eventually periodic.

## Remaining global step

Prove a sufficiently small canonical drawup on a subsequence for each actual nonperiodic candidate, or contradict the necessary lower bound using arithmetic of the scalar's ternary expansion and the actual 2-adic valuation recurrence. It is not enough to bound individual carries, or to establish typical behavior for an abstract phase. Low rational phases from PR182, including 7/8, can have large exponential canonical drawups, so this criterion does not settle even those surviving phase families by itself. Nontrivial cycles must still be excluded. No unconditional all-source bound or convergence theorem is asserted.

The finite controls test the local inequality and interval/height bounds on finite ordinary trajectories. The asymptotic argument above is written mathematics, not compiled Lean.
