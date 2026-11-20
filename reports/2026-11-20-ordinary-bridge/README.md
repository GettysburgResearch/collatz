# Ordinary Collatz bridges: inverse credit, representative classes, powered cycles

**Verdict: Collatz is not resolved by this investigation.** This branch contains
new scoped arguments, exact arithmetic checks, and independent reconstruction
within the agent team. It does not assert mathematical acceptance by the project
or a formal proof-assistant verification.

## Results ready for review

### An explicit inverse compiler with slope 25/12

For every `t>=1` and `0<c<3^t` with `3` not dividing `c`, the new finite
certificate constructs `k,r` satisfying

\[
0<r<2^k,\qquad
T^k(2^k x+r)=3^t x+c\quad\text{for every positive integer }x,
\qquad k\le\left\lfloor\frac{25t+120}{12}\right\rfloor.
\]

The common parity prefix has exactly `t` odd inputs. This improves the explicit
bound `floor((13t+65)/6)` in frozen PR #147. It is an unconditional finite
certificate and does not use the separate source-qualified stationarity input.

The construction works with physical inverse actions `E(z)=2z` and
`O(z)=(2z-1)/3`. A nonnegative integer credit on every ternary unit modulo
`3^17` pays for an action at every state and every hidden-digit lift.
An E action strictly decreases credit, forcing an O action within a bounded
gap. Telescoping and a terminal refund give the displayed compiler bound.

An independently written scalar verifier checked all **86,093,442 unit
states**, **258,280,326 collapsed lifted transitions**, and the terminal
refund at every state. The maximum credit is `133`; the selected odd-gap
cap is `10`. The compressed policy is accompanied by deterministic integer
reconstruction and separate verification, so the result is reproducible
without rerunning the policy search.

This constructs predecessors of a specified target. It does not prove that
an arbitrary prescribed starting integer follows one of those paths, reaches
a smaller integer, or reaches 1. The slope remains above `log_2(3)`; no forward
contraction or solution of Collatz is inferred from this improvement.

[Proof, certificate, and replay](../../research/inverse-escape-20261120/README.md)
· [Independent review](../inverse-physical-review-20261120/README.md).

### An entire sector of permanent merger representatives

For a positive integer already known to reach 1, let `tau` be its first-arrival
shortcut time and `q` its odd-input count. The grade `g=2q-tau` exactly classifies
eventual mergers that match both the clock and odd count. This identifies the
permanent representatives retained by PR #146's balanced-prefix filter.

Among convergent starts congruent to one modulo three, the permanent
representatives of nonpositive grade are exactly

\[
\{4^m:m\ge0\}\ \cup\ \{10\cdot4^m:m\ge0\}\ \cup\ \{7\}.
\]

The proof includes the sharp inequality `n*2^g(n)>=5/4` for convergent
non-powers of two, with equality exactly at `5*2^j`. All the upper-bit
obligations in this classified sector reduce to the two shifted-power families
already isolated in PR #146. Their convergence remains open. Positive grades,
unknown nonconvergent sources, and transient representatives are outside the
classification.

[Statements and significance](../../research/forward-bridge-20261120/README.md)
· [Elementary proofs FB-001–004](../../research/forward-bridge-20261120/PROOF.md)
· [Exact bounded checker](../../research/forward-bridge-20261120/check.py)
· [Independent reconstruction](../../research/independent-attack-20261120/FORWARD_REVIEW.md).

### Finiteness for four powered factors with a minimum-containing cube

The new CUBE-4 argument proves finiteness of primitive positive ordinary cycles
whose cyclic parity word is exactly four powered factors, each exponent at
least two, with the least phase in a factor of exponent three. The roots and
the other exponents may vary without bound.

The new comparison transports the leading terms of a rising square to the
leading monomial of the descending cube. It uses only two or three coordinates
in the rational p-adic Subspace Theorem, even when intervening exponents are
unbounded. Seven bounded rational polytopes exhaust the three-rise case. A
separate height-deficit estimate handles two rises and another descent.

The conclusion is **ineffective finiteness**, not emptiness: no period cutoff
is supplied and no individual hypothetical cycle is eliminated merely by this
finiteness conclusion. The descending-square cone left by the method has an
explicit retained rational witness. The result says nothing about a divergent
positive orbit or about arbitrary cycles without this four-factor cover.

A separate exact obstruction strengthens the diagnosis of the remaining
descending-square case: the entire box of radius `1/100` around
`(1/2,1/2,1)` lies strictly in the necessary height domain and defeats all 18
specified charged comparisons, as well as the full-displacement comparison.
This persists for the actual logarithm `log_2(3)`, not just a rounded constant.
It is a failure of these particular sufficient tests, not an ordinary cycle
or a proof that other arithmetic arguments must fail.

The follow-up MD-001 supplies additional ordinary information: the location
of the least phase determines an exact improvement to the multiplier costs.
For an unbounded family with a limiting gain vector in that box, the weighted
parity defect must satisfy `2*r_1+kappa<11191/48500`. In particular, the first
rising root's limiting even-input fraction is less than
`2003189/19971815` (about `10.0301%`). This is a necessary condition on possible
limiting profiles, not an effective finite cycle exclusion. Sublinearly many
exceptional inputs may remain even when their normalized count is zero.

[Statement and comparison to prior work](../../research/independent-attack-20261120/README.md)
· [Proof CUBE-4](../../research/independent-attack-20261120/PROOF.md)
· [Exact cone certificate](../../research/independent-attack-20261120/check_cubic_descent.py)
· [Independent reconstruction](../../research/forward-bridge-20261120/CYCLE_REVIEW.md)
· [Whole-box obstruction](../../research/independent-attack-20261120/SQUARE_OBSTRUCTION.md)
· [Separate obstruction checker](../../research/independent-attack-20261120/check_square_obstruction.py)
· [Minimum-location refinement MD-001](../../research/independent-attack-20261120/MINIMUM_DEFECT.md)
· [Independent MD-001 reconstruction](MINIMUM_DEFECT_REVIEW.md).

## What was tested, and what was not proved

The merger checker passes 25,000 first arrivals, 2,048 exact product identities,
4,857 classified sources, 410 high-bit identities, twelve exceptional upper
arms, and two negative controls. The cycle checker passes the seven cone covers
in 308 recursive nodes, 378 physical powered-block identities, and two negative
controls. The proofs supply their all-family quantifiers; these finite checks
do not supply them by extrapolation.

The separate square-obstruction checker uses exact rational affine extrema over
the whole box. Its minimum domain margin is `49/100`, its weakest certified
charge-failure gap is `3974/9725`, and it rejects an oversized-box mutation and
a zero-charge mutation. The parent independently read and ran this checker.
The MD-001 checker additionally passes 186 ordinary minimum-split identities,
the exact box constants, a strict divisibility margin, and a retained
zero-defect negative control. The parent independently reconstructed its
limiting argument and inspected the use of the same analytic inputs.

The parent and another agent independently reconstructed the load-bearing
arguments. The parent inspected the stated logarithmic-form input and the
p-adic Subspace Theorem, including its projective normalization. Those external
theorems were not reproved. See the packet reviews for their precise boundaries.

The pressure route from PRs #143–144 was also examined. Its needed all-clock
bound on the actual positive-integer diagonal moment was not obtained. The
fixed-target higher-moment vanishing already proved in PR #140 cannot be
interchanged with a moving-target infinite sum. No pressure-decay claim has
been added on that basis.

## Frozen inputs

| Source | Full commit |
| --- | --- |
| main | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` |
| PR #141 | `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b` |
| PR #143 | `41a408e5e617fb4e65142485f6f3ff3e6ef6c408` |
| PR #144 | `df756794e1d8de5cabff148ef433df505e3b68b4` |
| PR #145 | `dd245a712f985909f541590e3f6c179b7ba011e4` |
| PR #146 | `92820dd336b010215eb8a6eb4878a31b58a67656` |
| PR #147 | `b74b2d466f58844a742a6ed6bcdf06844269f361` |

Main's scientific verdict and integrated claims are unchanged. These additive
packets are submitted for review at their own published commit.
