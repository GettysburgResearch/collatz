# Simultaneous shifted cofactors on physical cycle phases

**Status — proposed consequence of the actual-ray cofactor proof.**
Use the finite rational phase set $Z$, common denominator $D$,
per-cycle prime pool $S$, tolerance $\epsilon$, and
$\beta=\log_3 2$ from [the shifted cofactor theorem](SHIFTED_COFACTORS.md).
Call a native phase *good* when all the simultaneous inequalities
(C1) hold at its physical integer for this pool.

Let $C_j$ be any sequence of distinct primitive positive
ordinary shortcut cycles, if such a sequence exists. In each cycle
make a single choice of at most $r$ primes, allowed to depend on
its whole period. Then
$$
 \liminf_{j\to\infty}
  {\#\{\text{good native phases in }C_j\}
    \over \#\{\text{native phases in }C_j\}}\ \ge\ \beta .             \tag{F2}
$$
If every $z\in Z$ is nonperiodic under the dyadic shortcut map,
the ratio tends to one. The bilateral localization of C2 also holds
with an exceptional proportion tending to zero. A single fixed
cycle is outside this asymptotic claim.

Write $\mu_j$ and $L_j$ for the native minimum and native period.
The minima tend to infinity since a bounded integer determines
at most one primitive cycle. If the period word has grade $p$
and carry $C$, then
$\mu_j=C/(2^{L_j}-3^p)\le3^{L_j}$. Its denominator is a positive
integer and its numerator is positive and at most $3^{L_j}-2^{L_j}$.
In one primitive lap every odd phase is distinct. The uniform
simple-path count T-A3-651 bounds the number of its odd phases up
to $X$ by $5X^{39/40}$. Summing over the bands
$[2^k\mu_j,2^{k+1}\mu_j)$ gives
$$
              \sum_{\text{one lap, odd }x}1/x\ll\mu_j^{-1/40}.
$$

Form a finite true window from $M_j=\lfloor\mu_j^{1/80}\rfloor$
laps, starting at the minimum. Its total reciprocal distortion
input tends to zero, its minimum tends to infinity, and its
starting charge is $O(L_j)=o(M_jL_j)$. The interval form of
[adelic Theorem A](../adelic/README.md), section 3, applies to
families of genuine windows with exactly these local uniform
conditions: minimum tending to infinity and sum of reciprocal
odd departures tending to zero. Every subwindow inherits both.
Thus for every fixed interval budget and tolerance, (C4) holds
throughout this family on all subwindows with lengths tending to
infinity. This is the varying-family consequence proved there.

Use the same deterministic cuts (C3) on the $M_jL_j$ departures.
The initial charge just bounded is negligible. The number of
pieces divided by the total length tends to zero because every
piece starts at log-height at least $\log_2(\mu_j+1)\to\infty$.
The bounded-length pieces cost negligible time. The remaining
ones give (F2) by (C2)–(C4) with the same order of limits in
$K$ and $\eta$. For precision, the limit of the supremum of the
fractional deficit in (C4) is at most zero as both cycle index
and window length tend to infinity. Otherwise a diagonal choice
of one violating window from successively larger cycles would
contradict the cited varying-family form. The nonperiodic and
bilateral statements use the same bounded number of groups per
piece. The fraction in the repeated orbit agrees exactly with
the original cycle fraction because one prime pool was used for
the whole period and all its repeats. This proof uses no effective
upper bound on the minimum in terms of its period beyond the
displayed integer carry bound.
