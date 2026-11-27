# A cross-class merger gives a small ordinary visitor or a large clock mismatch

**PROPOSED written theorem with an external two-logarithm input.**
Let $m,t\ge1$, $P_j=3^j-1$, and take an actual merger
$T^iP_m=T^lP_t$ for the shortcut map. Suppose the two departure
prefixes are simple. This always holds when each arm makes its
first visit to a chosen common endpoint. Set $p=Q_i(P_m)$,
$q=Q_l(P_t)$ and
\[
       a=i-l,\qquad b=m+p-t-q,\qquad D=2+|a|+|b|.
\]
Let $S$ be the least positive integer occurring on the two arms,
including their common endpoint. There are effective absolute
constants $K,A$ such that either $a=b=0$ or $S\le K D^A$.
This estimate has no dependence on the lengths common to the
two native clocks or to the two augmented odd counts. For arbitrary
prefixes, including repeated laps, the weaker estimate
$S\le K(i+l+1)D^A$ holds in the nonzero case.

In particular, take a sequence of original hard parents for which an
actual merger with an earlier peak of a different augmented class is
supplied. If $\log D=o(m)$ at first visits to the common endpoints,
then each pair contains an actual ordinary visitor of size
$\exp(o(m))$. Inspecting those finite prefixes produces it.
It lies in the component of the original parent. If that parent
were bad, this would be a bad visitor below the $2^{-40}z_m$
threshold for all sufficiently large members. This corollary uses
the pinned quantitative return to exclude such an original least
parent. It does not turn that visitor itself into a canonical
two-arm representative. If $t$ is itself a hard exponent, its
literal upper hitting-clock transfer is already available as in
[the linear classification](PEAK_RIGIDITY.md).

## Calculation

Write
\[
  D_j(x)=\prod_{\substack{0\le v<j\\T^vx\ {\rm even}}}
       \left(1+\frac1{T^v x+1}\right).
\]
Multiplying the actual shifted-height updates gives
$2^j(T^jx+1)=3^{Q_j(x)}(x+1)D_j(x)$.
Cancelling the common positive endpoint gives precisely
\[
   a\log2-b\log3=\log D_i(P_m)-\log D_l(P_t).
\]
Both logarithms on the right are nonnegative. Each is bounded by
the sum of reciprocals of its departed sites. On a simple path
whose floor is $S$, this sum is $\le C S^{-\delta}$ for absolute
effective $C,\delta>0$ by the binary entropy argument in
[the class-finiteness proof](PEAK_RIGIDITY.md). Therefore
$|a\log2-b\log3|\le C S^{-\delta}$. On arbitrary prefixes one
can instead use $\max(i,l)/(S+1)$.

Unique factorization shows the linear form is nonzero whenever
$(a,b)\ne(0,0)$. The two-number specialization of Matveev's
logarithmic-form bound on the fixed rationals $2,3$ gives
$|a\log2-b\log3|\ge cD^{-\kappa}$ for some absolute effective
$c,\kappa>0$. A zero coefficient is covered directly. Combining
the bounds proves both claims. The stronger estimate is also valid
with $D$ replaced by any upper bound on the simultaneous mismatches.
[Matveev, *Izvestiya: Mathematics* 64 (2000), Corollary 2.3](https://doi.org/10.1070/IM2000v064n06ABEH000314)

If $a=0,b\ne0$ or $a\ne0,b=0$, the absolute linear form is at
least $\log2$. Thus a simple-prefix merger with exactly one vanishing
mismatch must pass through a fixed finite set of ordinary positive
integers, even for arbitrarily large *other* mismatch.
[The explicit finite-floor bound](FINITE_FLOOR.md) places such a
visitor in the computationally verified convergence range and also
accepts additional nonzero clock and grade pairs. A floor $S\asymp 2^m$ at a nonzero mismatch forces
$D\ge c'2^{\epsilon m}$ for absolute $\epsilon,c'>0$.

The shifted product on complete Mersenne classes and the simple-path
reciprocal estimate are prior arguments in PR195,
51d97cbe17054415acaf95e422801a3532545033,
research/astra-global-closure-20261124/round13/trace/FINITE_FAMILY.md,
“Every actual augmented class is finite.” PR192,
ed7a6fe30b8602407f77855ceb74ce0489ce9c10,
research/astra-unconventional-20261126/descent/POSTPEAK_DELAY.md,
uses the two logarithms in a finite mixed prepeak/postpeak window.
Here the logarithmic form is the mismatch between independently
timed ordinary arms. The floor in the resulting inequality is a
visited integer on one of those two same arms.

**Unresolved step.** The argument uses a supplied actual cross-class
meeting. No such meeting at subexponential mismatch has been proved
for every residual original $m$. A merger on other parents cannot
provide either hypothesis here.
