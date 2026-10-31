# Certified all-source moment traces from finite ternary tables

**PROPOSED mathematical interface; finite computational results only.**
This note computes the new D_q, the earlier S_q, and the earlier E_q at
specified finite clocks, including EVERY positive odd source. It does NOT
prove a bound uniform in q. The implementation uses integer intervals, not
floating-point extrapolation.

## T1. Exact periodic populations, with positive ordinary realization

For s=2 or 4 define

    Z_(q,s)(t)=sum_(U^q(x)=t, x positive odd) J_q(x)^s.

At q=0 this equals one. At q>=1 it depends only on t modulo 3^q, for odd
positive t. Write z_(q,s) for this finite residue table. Values at even
residues refer to the corresponding POSITIVE ODD representative, not to
application of the odd map to an even number.

For a positive odd unit t modulo 3, set a0=2 when t=1 mod3 and a0=1 when
t=2 mod3. All its immediate odd predecessors are

    x_j=(2^(a0+2j)t-1)/3=L^j(x_0), L(x)=4x+1, j>=0.

They are positive, integral, and have EXACT valuation a0+2j. There are no
odd predecessors when 3 divides t. Hence with b=2^s and m=3^q,

    H(n)=sum_(j>=0) b^(-2j) z_(q,s)(L^j(n) mod m),
    z_(q+1,s)(t)=3^s b^(-a0) H((2^a0 t-1)/3 mod m).       (1)

This proves periodicity inductively. Replacing t by t+3m changes x_0 by
2^a0 m, so the table does not depend on the chosen odd representative.
No negative trajectory or independent-forward-valuation assumption is used.

The geometric tilted-law interpretation is already present in PR140
pass2/INVERSE_PRESSURE.md, P5, and EXACT_DENSITY.md. Here s=4 is needed for
the DIAGONAL moment, while s=2 supplies E_q and S_q. Generalizing a geometric
law parameter is not claimed as an independent breakthrough.

## T2. One affine permutation cycle gives a separate checking algorithm

Modulo m=3^q, L(n)=4n+1 is one cycle of length m. Indeed

    3L^j(n)+1=4^j(3n+1),

and 3n+1 is a ternary unit. The elementary valuation identity
v3(4^j-1)=1+v3(j) implies the period is exactly 3^q for every n. The identity
follows from cubing and A^3-1=(A-1)(A^2+A+1), together with the binomial
expansion for an exponent not divisible by 3.

Thus H is also the unique solution of

    H(n)=z_(q,s)(n)+b^-2 H(L(n)).                          (2)

The producer encloses (1) using 32 terms and a rigorous geometric tail.
If the table is between lower and upper bounds, the omitted tail is at most

    max(upper)/[(b^2-1)b^(2(32-1))].                       (3)

Every division is rounded outwards at 96 binary fractional bits.

The separate verifier does NOT use this truncated series. It walks the full
affine permutation cycle backwards, beginning with the interval
[0,max(upper)/(1-b^-2)] at one coordinate, and repeatedly applies (2).
At least two complete sweeps are used, with extra sweeps for tiny tables.
It works at 128 fractional bits and checks containment in the producer's
final trace intervals. Every residue is included. Neither program imports
the other, and neither relies on a numerical linear-system solver.

As a whole-table check, summing (1) gives

    sum_r z_(q,2)(r)=3^q,
    sum_r z_(q,4)(r)=(27/5)^q.                            (4)

Both identities are checked by exact integer cross multiplication at every
level. Their normalized means are 1 and (9/5)^q, respectively; this mean
exponential growth does NOT determine the one-sided ordinary trace below.

## T3. Exact positive-integer traces and rigorously bounded tails

Let o_r be the unique positive odd representative of r modulo m in [1,2m),
with o_0=m. Define

    W_m(r)=sum_(k>=0)(o_r+2mk)^-2.

Then nonnegative regrouping gives the exact ALL-SOURCE identities

    E_q=sum_r z_(q,2)(r) W_m(r),
    D_q=sum_r z_(q,4)(r) W_m(r),
    S_q=sum_r z_(q,2)(r)^2 W_m(r).                         (5)

The ordinary-positive representative is essential: the negative residue -1
has a large density spike, but its first positive odd representative is
2*3^q-1. Substituting the signed integer -1 into the positive trace weight
would completely change (5).

No special-function library is needed. For h=2m and any integer K>=1,
monotonicity and integration give

    sum_(k<K)1/(o+hk)^2 + 1/[h(o+hK)]
      <= W_m(r)
      <= sum_(k<K)1/(o+hk)^2 + 1/[h(o+h(K-1))].             (6)

All arithmetic is integer rational enclosure. The runs use K=128 at q<=3
and K=16 thereafter. These deliberately simple tail bounds leave explicit
nonzero interval widths; digits outside the recorded intervals are not
claimed certified. Final trace bounds use 60 fractional bits and an outward
padding of eight units; all computations before that rounding are exact.

The arithmetic work at fixed precision is O(3^q) per level, with constants
from the geometric and reciprocal-tail lengths, and O(3^q) storage. This is
EXPONENTIAL in the odd clock q. It is not an efficient universal asymptotic
bound and not an algorithm deciding pressure decay.

## T4. Executed all-source enclosures

The complete tables were enclosed through q=12: 797,161 residue entries per
power across levels 0..12. Both powers were independently reconstructed.
Some outward-rounded, intentionally shorter decimal intervals are:

| q | D_q, diagonal | S_q, collision |
|---|---|---|
| 0 | (1.23369, 1.23371) | (1.23369, 1.23371) |
| 1 | (0.63420, 0.63422) | (0.71876, 0.71878) |
| 4 | (0.10331, 0.10344) | (0.15181, 0.15197) |
| 8 | (0.07438, 0.07440) | (0.12439, 0.12442) |
| 10 | (0.12953, 0.12955) | (0.21898, 0.21900) |
| 12 | (0.23594, 0.23596) | (0.39986, 0.39988) |

These include the full infinite set of positive odd sources at those clocks.
They are stronger in that respect than a finite-source lower approximation,
but they establish NO polynomial all-clock upper bound.

The separate finite-bank experiment uses all 2,048 odd sources through 4095
and clocks 0..80, retaining all cycle visits for D_j while killing them only
for Ebar. It checks 165,888 source/clock entries. At clock 80, ONE inspected
source is still active; the packet does not call it a counterexample or
pretend that all inspected sources have been completed. Its future pressure
contribution is retained in the bound. Raw reconstruction uses 326,379
shortcut steps.

For these finite source families the verifier also checks the envelope
interpolation, the elementary beta=1 coercivity inequality, and the
beta=19/20 version using an exact nineteenth power. These are regressions,
not proofs of the universally quantified inequality in PROOF.md.

## T5. Evidence boundaries and negative controls

The proposed proof uses exact identities and inequalities, not the numeric
shape of the table. D_q itself is not monotone: the certified D_12 lower
bound exceeds the certified D_8 upper bound. No stepwise contraction is used.

The producer and separate verifier both passed normally and under -OO;
corresponding complete outputs agree byte-for-byte. Thirteen direct schema,
semantic, interval, and duplicate-key corruptions were rejected. They are
not resealed full-corpus mutation attacks. These are separate code paths
written in one session, NOT independent mathematical peer review.

A grouped execution timed out after its first producer had successfully
finished. The optimized producer was rerun separately to completion, and
both verifier modes completed separately. Only the completed commands are
reported as successful. No full repository checkout validator, remote CI,
formal proof assistant, or independent AI swarm was run.
