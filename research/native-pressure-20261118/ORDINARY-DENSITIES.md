# Pointwise ternary densities at ordinary odd targets

Let g_q(t)=3^q μ_q(t mod 3^q), including g_0=1. Let U be the odd
Syracuse map and P(t) the ordinary predecessor cone under unshortened
Collatz. For every fixed odd unit t, both

    sup_q g_q(t) < ∞,
    liminf_(Q→∞) (1/Q) sum_(0≤q<Q) g_q(t) ≥ c t lower_density(P(t)) > 0.  (1)

Here c>0 is absolute. The upper bound is Ct for nonperiodic t. For a
periodic t of odd cycle multiplier J_c it is (C+1)t/(1−J_c).
The first conclusion uses the antichain estimate based on Mazur's weighted
inverse-path input. The positivity uses his fixed-target and natural-density
moving-floor results. These are statements at specified ternary points,
where an almost-everywhere density theorem alone gives no conclusion.

## Exact levels and an upper bound

A valuation word of length q and sum A has formal forward offset F and
multiplier J=3^q/2^A. Its compatibility at t is exactly F≡t modulo 3^q.
The inverse divisions by 3 are integral step by step by reduction modulo
successive powers, and each inverse step (2^a y−1)/3 from a positive odd
integer, when integral, is a positive odd integer. Distinct compatible
words ending at t and of the same depth have different sources by forward
determinism. Thus by the geometric word probabilities

    g_q(t) = sum_(U^q x=t) J_q(x),      J_q(x) ≤ t/x.              (2)

For q≥1 and t nonperiodic, distinct sources on this level are incomparable:
otherwise a positive return of t follows by applying q steps and commuting
the two iterates. Ordinary reachability between odd numbers coincides with
odd-only reachability. The harmonic weight of unit sources on the level is
bounded by an absolute constant by (1) in the antichain note. The nonunit
sources inject into the unit sources by L(x)=4x+1, since U(L(x))=U(x);
1/x≤5/L(x). This proves the first upper bound.

For periodic t consider the first-hit sources of exact length d. Nonperiodic
sources on this layer form an antichain: a path between two of them must
precede its first visit to the cycle vertex t. There is at most one periodic
source on any exact d-level. In replacing a nonunit nonperiodic source
by L(x), its first hit still occurs at d unless L(x) is periodic. Periodic
images are covered by that single possible periodic source on the full
level. Thus the first-hit level contributes at most (C+1)t, enlarging the
absolute C if necessary. Include the empty first hit. Every further return
appends complete cycles, each with multiplier J_c<1 by the positive affine
intercept on the cycle. Sum the geometric series at any prescribed depth.

[Harmonic antichain estimate](ANTICHAINS.md).

## Uniform distortion of simple paths

The translated packing estimate bounds the number of vertices of a simple
shortcut segment in any interval of length Y by 16Y^(19/20). Odd sources
of an odd-only first-hit segment constitute a subset of such a simple
segment (terminate at its first hit of t; if t is on a cycle, no prior
repetition is possible). Hence the total reciprocal sum of those odd
vertices is at most D=16 sum_(j≥0) 2^(−j/20), uniformly over all segments.
Multiplication along a segment x→t gives

    J_q(x)/t = (1/x) product_(0≤i<q) (1+1/(3U^i x))^(−1)
             ≥ exp(−D/3)/x.                                        (3)

[Translated simple-orbit packing](../novel-swarm-20261030/pass4/WINDOWS.md).

## Transfer of ordinary predecessor density into depth averages

Write δ for the lower natural density of P(t), positive by Mazur's
fixed-target result. For each integer B bound the first ordinary hitting
time of t from all y≤B that actually hit it by a finite number H_t(B)
(use zero for an empty set). Choose an integer function f(n) tending
to infinity sufficiently slowly that H_t(f(n))≤log n for all sufficiently
large n. Mazur's natural-density logarithmic-time theorem then gives a
density-one set of n hitting height at most f(n) within 436 log n ordinary
steps. If such n lies in P(t), it either already hit t or that low point
belongs to P(t). Thus the set E of n reaching t in at most 437 log n
ordinary steps has lower density at least δ.

Partial summation gives sum_(n≤X,n in E) 1/n ≥ (δ−o(1))log X. The
odd part x of n reaches the odd t by at most 437 log X odd steps,
and all even lifts of x together have harmonic weight at most 2/x.
For X=exp((Q−1)/437) every such x therefore belongs to a first-hit
level 0≤q<Q. Applying (2) and (3) to these sources yields the second
bound in (1) with c=exp(−D/3)/874.

[Mazur, natural-density almost-boundedness in logarithmic time](https://www.proofatlas.ai/formalizations/natural-density-log-time-collatz/).
[Mazur, positive lower density for fixed targets](https://proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).
