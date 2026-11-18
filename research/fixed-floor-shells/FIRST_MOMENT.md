# Minimum atoms and the first-moment test for escape

**FS-022. PROPOSED deductions from source-qualified inputs.** Write
$m(n)$ for the least value of the ordinary positive Collatz orbit and
$p_t$ for its natural-density law (Valbuena; also Leen, Corollary 3.8).
The uniform first-landing result used here predates this project work:
rStation paper 12, Theorem 14 gives absolute $c,C>0$ such that each
odd $3$-unit $a\le M$ receives $\ge cX/M$ odd sources in $(X/4,X]$
whose first Syracuse entry at or below $M$ is $a$, for $X\ge CM$.
Its source dependencies and checks are as stated in that paper.
[First-landing bounds and canonical inverse laws for Collatz, v1](https://rstation.ai/problems/collatz/papers/12)
· [Leen, Brownian motion in Collatz orbits](https://doi.org/10.5281/zenodo.23252395).

Let $\mathcal R$ consist of odd $t$ coprime to 3 satisfying $m(t)=t$.
For $t\in\mathcal R$, take $a=M=t$ in Theorem 14. Before arrival all
odd terms are above $t$, and intervening even terms are at least the
next odd term. Every certified source therefore has exact global
minimum $t$. Consequently, uniformly for $X\ge Ct$,
$$
  \#\{X/4<n\le X:m(n)=t\}\ge cX/t,
  \qquad p_t\ge c/t.
$$
An even $t$ cannot be any orbit minimum, and an odd multiple of 3 has
only its dyadic multiples as ordinary predecessors, a density-zero set.
A target with $m(t)<t$ cannot be a minimum either. Thus
$\operatorname{supp}(p)=\mathcal R$.

**First moment.** The following three statements are equivalent:

1. $\sum_t t p_t<\infty$.
2. $\mathcal R$ is finite.
3. Every positive orbit is eventually periodic and there are finitely
   many positive cycles.

Indeed each $t\in\mathcal R$ contributes at least $c$ to the sum.
Distinct cycles have distinct odd minimum values, each a unit.
On a nonperiodic positive orbit the distinct states tend to infinity.
For every sufficiently large real $B$ let $v$ be its last odd value
$\le B$. The next odd value is at most $(3B+1)/2$, and the least
odd value on the remaining tail belongs to
$\mathcal R\cap(B,(3B+1)/2]$. Thus either divergence or infinitely
many cycles forces infinite support. Conversely, finitely many cycles
capturing all orbits give one uniform bound on every $m(n)$, namely
the largest cycle minimum.

**A weaker empirical test already excludes divergence.** If one positive
orbit diverges, choose $B=2^j$ in the preceding argument. The resulting
intervals are disjoint for all sufficiently large $j$, so there are
$\gg\log X$ distinct $t\in\mathcal R$ with $Ct\le X$. Their certified
sources are disjoint by exact minimum. Therefore
$$
 \frac1X\sum_{X/4<n\le X}m(n)\gg\log X
$$
for every sufficiently large $X$. Even a sequence of shell means
$o(\log X)$ along unbounded $X$ rules out divergence. The same
calculation gives $\sum_{t\le R}t p_t\gg\log R$ under divergence.
Infinitely many cycles with no divergent orbit force unbounded shell
means but this argument does not give their growth rate.

The earlier [polynomial atom argument](FLOOR_TAIL.md) only uses Lau's
absolute predecessor coefficients, without the prior first-landing
theorem. A stronger prior upper is rStation paper 102 v1, Theorem 1 (2).
It includes the *failure* atom, which is exactly $m>R$, and gives
$C\exp(C\sqrt{\log R})R^{-g}$, uniformly in odd source octaves of
scale at least $R$, where $g=1-H_2(\log_3 2)+1/351$. Thus the global
minimum has every positive moment of order $s<g$, both in its limiting
law and uniformly in ordinary finite samples. For the latter assertion
sum the tail by layers, partition even starts according to the power of
two stripped from their odd core, and bound any straddling octave by
the octave beginning at $R$ after dropping its points at most $R$.
The argument does not reach the first moment. [Paper 102 v1](https://rstation.ai/problems/collatz/papers/102/v1). Also Theorem 15 of the cited rStation
paper precludes a uniform flat $O(1/M)$ upper on all first-landing
atoms. A bound for arbitrary comparable-scale landings must still
control the specific targets in $\mathcal R$. The explicit
[prefix-tree control](FLOOR_CONTROL.md) has a positive-density escaping
component and floor density of order $1/B$, consistent with
logarithmic growth of a truncated first moment.

## An unmarked terminal-residue test for divergent orbits

**FS-023. PROPOSED deduction from the retained-word estimate in rStation
paper 12.** Write $R_*(n)$ for the sum of $\log_2(1+1/(3u))$ over the
odd terms before the first attainment of $m(n)$. Let $\nu$ be its
limiting law on all positive starts, as in Leen’s terminal-data theorem.
There are absolute $0<c_0<C_0$ and $c,C>0$ such that for every large
integer $M$ and every $X\ge CM$,
$$
 \frac1X\#\{X/4<n\le X:c_0/M\le R_*(n)\le C_0/M\}
 \ge \frac cM\#(\mathcal R\cap[1,M]).
$$
The same lower bound holds for the $\nu$-mass of this closed interval.
In particular, a divergent orbit would force
$$
 \nu([0,\delta])\gg \delta\log(1/\delta)
$$
for every sufficiently small $\delta>0$, even with the interval restricted
to $[c'\delta,\delta]$ for a fixed $c'>0$. Infinite support would force
$\nu([0,\delta])/\delta\to\infty$. Thus an unbounded sequence of reciprocal
scales at which this ratio stays bounded suffices to imply finite minimum
support and eventual periodicity of every positive orbit. A sequence with
$\nu([0,\delta])=o(\delta\log(1/\delta))$ as $\delta\downarrow0$ suffices
to exclude divergence. These implications do not provide such an upper
bound.

For the proof retain the actual paths used for Theorem 14 of rStation
paper 12. For every odd unit $a\le M$, at least $cX/M$ odd starts in
$(X/4,X]$ first land at $a$ below $M$. Their immediately preceding odd
state $r$ satisfies $c_1M\le r\le C_1M$. For the prefix from the source
$x$ to $r$, Lemma 13 and the proof of Theorem 14 give
$r=A_kx+B_k$ with $A_k=3^k2^{-d_k}$, $0\le B_k\le B_0$ and $B_k<r/2$,
where $B_0$ is absolute. The telescoping product for odd steps gives the
exact accumulated residual to $a$:
$$
 \log_2\!\frac r{r-B_k}+\log_2\!\left(1+\frac1{3r}\right).
$$
This lies in $[c_0/M,C_0/M]$ uniformly, by the bounds on $r,B_k$.
The entire earlier odd path stays above $M$, so $m(x)=m(a)$ and the
displayed quantity equals $R_*(x)-R_*(a)$. If $a=t\in\mathcal R$, then
$R_*(a)=0$ and the certified sources have distinct minimum labels for
distinct $t$. Summing gives the finite bound. At each fixed $M$ the
unrestricted finite-sample probability dominates the shell count divided
by $X$; weak convergence and the closed interval give the limiting bound.
Take $M=\lceil C_0/\delta\rceil$ and use the dyadic future minima on any
divergent orbit proved above. [rStation paper 12, Lemma 13 and proof of Theorem 14](https://rstation.ai/problems/collatz/papers/12/v1)
· [Leen, terminal data](https://doi.org/10.5281/zenodo.23252395).

Taking $M=t$ separately for each $t$ also proves both first-moment tests
above with the weight $m(n)$ restricted to $c_0\le m(n)R_*(n)\le C_0$.
For the limiting first moment, use the closed event with the discrete
minimum label fixed at $t$ before summing. At a single unit $a$ the same
proof places at least $c/M$ mass of the $m(a)$-labelled residue law in
$R_*(a)+[c_0/M,C_0/M]$ for every $M\ge a$ sufficiently large. In
particular the convergent basin alone gives limiting joint probability
$\Pr(m=1,R_*\le\delta)\gg\delta$, consistent with the
logarithmically larger signal required above if an orbit diverges.
