# Independent review of the scalar and canonical-fibre deductions

23 November 2026. Reviewer: root. Authors reviewed: source_construction
and actual_collision. Parent commit:
a9b23dcee61a4b65a63aa4e7ca653d875a405037.

The following verdicts bind only the listed file bytes, claim ranges and
explicit hypotheses. They do not audit the whole parent commit, an entire
peer PR, or every upstream source theorem.

## 1. Frozen sources

| Source | SHA-256 |
|---|---|
| research/literature-push-20261123/rigidity/SCALAR_BOUNDARY_AND_SECOND_CENTER.md | e5b8ac874505bbecfd2ae889cfe81eb9586b68e4ad19fb3a0ee6dbe61a493c73 |
| research/literature-push-20261123/rigidity/FINITE_FILTER_TEST.md | 132d23447fd01aeaebfb40cfe4315facf446ab0b8b1659d3d31da5e579b51a89 |
| research/literature-push-20261123/boundary/CANONICAL_FIBRE_DEPTH.md | 118ce0a322d68ae683789d1647060c4bc16e39086ee96ae443f68d877c2b1999 |

Each lane's source ledger additionally identifies upstream repository files
by full commit, path and inspected claim range. The new commit carrying
these bytes is identified in the release record; a commit cannot contain
its own hash.

## 2. Scalar natural-boundary theorem

**Verdict: VERIFIED as a written deduction using the stated primary
rationality theorem and the credited rational-series consumer.**

I independently checked the source identity and each radius. A positive
ordinary source has infinitely many odd inputs. Sampling the cumulative
odd density at odd-input clocks recovers both extrema: the intervening
constant-count stretches attain their extrema at their endpoints, up to
a single count or clock. The Cauchy--Hadamard formulas therefore retain
the actual liminf and limsup. Every nonzero coefficient is a unit at
primes other than three.

With a density limit, the complex/ternary radius product is exactly one.
A genuine scalar continuation across a boundary point enlarges the
complex conformal radius strictly. The Schwarz-lemma argument proves
strictness; a smooth inner exhaustion retains a positive margin.
Choosing the ternary radius just below its original radius makes the
capacitary degree strictly positive.

I read Bost--Chambert-Loir, arXiv:math/0702593v3, Definition 3.7,
Theorem 7.9, its sufficient integral-model condition 2', and Example
7.10 in the primary PDF:
<https://arxiv.org/pdf/math/0702593v3>.
The coefficients in Z[1/3] and the analytic germs at all places provide
the required arithmetic model. The algebraicity-assumed equality
theorem is not substituted for the strict positive-degree theorem.

The conclusion concerns the individual scalar series, under a density
limit. It is distinct from a uniform-family norm boundary and does not
prove that every escaping ordinary source has a density limit.
Rationality forces eventual periodicity by the retained finite-window
recurrence argument; the final conversion of repeated parity to repeated
ordinary state uses divisibility of one fixed full residual by
arbitrarily large powers of two. It does not exclude a different cycle.

## 3. Deflation and the critical two-center criterion

**Verdict: VERIFIED within the explicit Jet hypothesis J.**

For deflation I recomputed each coefficient by formal division:
the apparent binary denominator cancels using the complete affine
identity, leaving minus the actual next integer divided by its full
power of three. At a post-odd clock that integer is a ternary unit.
At every other prime it is a unit infinitely often: eventual
divisibility of every state by a fixed prime would contradict an odd
step. The real coefficient lower bound from positivity forces radius
at most two. These facts prove the exact product at most one, with no
inferred identification of the real value and the binary value.

I read the primary multipoint paper
Chambert-Loir--Noûs, arXiv:2305.17210v2, Sections 2.1--2.8 and
4.1--4.3:
<https://arxiv.org/pdf/2305.17210>.
Section 4.1 requires full formal arithmetic germs and compatible local
meromorphic realizations. The stated J provides the common finite
denominator-prime set and all small analytic discs. At two, both full
germs are realized by the same original function on a single unit disc;
at the other places the stated disjoint components are allowed.
The good-prime domains are precisely the union of the two reduction
residue discs of the standard projective-line model.

With coordinates z and z-2, the only off-diagonal contribution in the
chosen construction is log 2 at the binary place. The first diagonal
loses O(epsilon), and the second is log epsilon plus a fixed finite
constant. I recomputed the equal-payoff row weight and verified the
strict positive value when the product of the diagonals is below
(log 2)^2. Theorem 4.3 then gives rationality.

The proof does not supply J. The ordinary value supplies only the
constant coefficient; even the first derivative is not proved rational
for a general source. Later-state value identities reduce to the same
single equation. The finite confluent Hasse determinant is indeed
2^(rs), with its binary and real factors exactly balanced.

The subsequent root-authored GENERAL_DENSITY_JET.md addendum is outside
this independent-review verdict. It has a separate review boundary.

## 4. Finite rational filter denominator theorem

**Verdict: VERIFIED as a written all-source, all-fixed-filter deduction.**

I reconstructed the finite-window convolution. After removing the
current complete power of three, its nonzero coefficient multipliers
come from a finite set depending only on the fixed rational polynomial.
Their three-adic valuations have a finite maximum. This gives the
claimed surviving denominator lower bound, including possible
denominators at other primes.

For the one positive ordinary source, the elementary bound
x_t <= n*2^(2p_t-t) follows from odd-step growth at most two and exact
halving at even steps. It gives a linear lower bound for p_t.
Consequently every arbitrarily late nonzero filtered coefficient has
an exponentially large reduced denominator. A subexponential common
denominator cannot coexist with such a sequence, so the filtered
series must be a polynomial.

Clearing both rational-function filters preserves subexponential common
denominator growth up to fixed factors and finite convolutions.
The exceptional-set version retains its exceptional coefficients;
it does not erase them from the primary theorem's conclusion.

I directly inspected Bell--Gunn--Nguyen--Saunders,
arXiv:2206.00862v1, Theorem 1.2 and its specified exceptional-set
condition in the primary PDF:
<https://arxiv.org/pdf/2206.00862>.
The new result is the exact applicability test for the chosen
regularization class, not a general limitation on all rationality
methods or a construction of a recurrence.

## 5. Renewal-tail application

**Verdict: VERIFIED as an application of a checked primary theorem to
the specified iid model.**

The geometric-gap series and the fair two-branch perpetuity describe
the same real model. I recomputed its moments:

- E A = 1;
- E log A = (log 3 - 2 log 2)/2 < 0;
- E(A log A) = (3 log 3 - 4 log 2)/4 > 0;
- E B = 1/4;
- each subunit moment follows from strict concavity and the stated
  positive series estimate.

I read Jelenkovic--Olvera-Cravioto, *Implicit renewal theory and power
tails on trees*, Theorem 3.1, including the coefficient moment,
nonarithmetic, independent-copy, subunit-moment and integrable tail
difference conditions:
<https://molvera.web.unc.edu/wp-content/uploads/sites/19443/2019/01/Jelenkovic_Olvera_WBP_AAP_final.pdf>.

The two logarithmic increments generate no discrete additive subgroup:
a nonzero frequency cannot give phase one to both, by multiplicative
independence of two and three. This is the renewal nonarithmetic
condition. The tail difference integral is nonnegative and equals
E B by Tonelli applied to the coupling. No subtraction of divergent
expectations occurs. Thus the tail constant is exactly
1/log(27/16), and enlarging a tail bound supplies a global constant
K_R/x. The model tail is not attributed to an actual orbit.

## 6. Fixed-original-source depth payment

**Verdict: VERIFIED WITH THE STATED UPSTREAM QUALIFICATIONS.
The requested qualification is explicit in the frozen source.**

I independently reconstructed the forward multiplicative correction
and the reversed inverse-prefix carry. For the literal original source
q_0 and a later root q_j,

chi_j*q_0 = Lambda_j*q_j,

and the entire reversed prefix has real carry
(1-Lambda_j)*q_j >= q_j/(3q_0+1).
Its exact canonical cylinder probability is
chi_j*h(q_0)/h(q_j). Every continuation through that cylinder remains
above the carry. This proves the finite lower bound with Lambda_j,
without an infinite capacity or summability assumption.

The uniform square-height statement separately needs
Lambda_* = inf_j Lambda_j > 0. I requested that this imported
hypothesis be explicit in the title, opening, theorem consequence and
evidence boundary. It is explicit in the frozen file listed above.
It is not silently derived from escape alone.

I inspected the primary source manuscript's Section 9.2, F1--F8:
<https://rstation.ai/problems/collatz/papers/19>.
The law is a trace-weighted Cesaro limit for each fixed root. It is not
an individual-depth limit or an average of separately normalized
conditionals. Its original trace existence and selection inputs remain
source-qualified.

Dropping only the nonnegative ternary restriction bounds a depth-m
measure on the height-scaled test by
2*K_R*3^m/(epsilon*q). Combining this with the cylinder lower bound
yields the arbitrary-positive-weight budget and the precise Cesaro
condition 3^M/M >= c*q^2. The common model's real and ternary coordinates
need not be independent.

The normalization/total-variation inequality is correct for a bounded
test in [0,1]. Its corollary separately assumes an upper bound on h(q)/q;
that input is not needed for the unnormalized depth budget. The
coordinate transformation R=q-chi*Z also preserves the stated Fourier
frequency warning.

These are necessary lower budgets for a proposed bridge. They give
neither a sufficient conditioning depth, a fixed-root
frequency-dependent convergence rate, nor a contradiction to escape.
No infinite measure or potential-theory statement in this review is
claimed as Lean-checked.
