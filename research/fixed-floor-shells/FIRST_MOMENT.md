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
theorem. The known all-order inverse-logarithmic upper tails do not
imply a finite first moment. Also Theorem 15 of the cited rStation
paper precludes a uniform flat $O(1/M)$ upper on all first-landing
atoms. A bound for arbitrary comparable-scale landings must still
control the specific targets in $\mathcal R$. The explicit
[prefix-tree control](FLOOR_CONTROL.md) has a positive-density escaping
component and floor density of order $1/B$, consistent with
logarithmic growth of a truncated first moment.
