# Independent review: Haar limits and ordinary labels

23 November 2026. Reviewer: the infinite-optimizer agent, separate from
the coordinating author. This is an internal mathematical reconstruction,
not external peer review or a review of the complete upstream analytic
construction.

## Reviewed bytes and verdict

File:
`research/lean-global-resolvent-20261121/overview/source-construction/HAAR_AND_ORDINARY_LABELS.md`

SHA-256:
`36ad8ee0dba9f628aaa7661917f8f722ec7fd18412be295fa95617b1bf1059c7`.

**PASS in the stated scope.** I read the complete note and independently
reconstructed its finite total-variation comparison, conditional joint
weak-limit theorem, and mixed-phase collision identity. The positive
escaping product, common boundary law, and late conditional-law comparison
remain explicit supplied inputs at the source pins in the note. I have
not independently reconstructed the external higher-rank rigidity theorem
or claimed a new proof of the upstream canonical law.

## 1. Exact comparison of averaging shapes

For each fixed j, the exponent intervals `[-A_j,L-1-A_j]` and `[0,L-1]`
share `max(0,L-A_j)` terms. Cancelling the identical probability measures
leaves mass `min(1,A_j/L)` on each side. Under the stated probability
total-variation convention, their difference is bounded by that mass.
Convexity over j gives (1).

The source bound `A_j<=alpha*j+C`, with `alpha=log_2(3)`, yields

`sum_(j<N) A_j <= alpha*N*(N-1)/2+C*N`.

Dividing by `N^3` at `L=N^2` gives exactly (2), including its `C/N^2`
term. Thus the two compact averages have identical subsequential weak
limits. This removes the chronological valuation shifts from this long
averaging shape; it does not remove dependence of the initial law on
the component. The note makes that distinction.

## 2. The Rajchman implication is conditional and retains the actual marginal

For each nonzero character index `xi in Z[1/6]`, the supplied
`chi_j -> infinity` gives `abs(xi)*chi_j -> infinity`. Rajchman regularity
therefore implies `mu_hat(xi*chi_j) -> 0`. Multiplication by any bounded
continuous endpoint test and Cesaro averaging still tends to zero.
For the zero character the mixed test is precisely the original endpoint
average. Along a subsequence defining the actual ternary time limit nu,
it tends to its integral against nu.

The character algebra separates points of the compact solenoid. Products
with continuous functions on the compact ternary unit space are uniformly
dense in continuous functions on the product. These mixed-test limits
therefore prove exactly `Haar_X6 tensor nu`, with no extra assertion about
which nu can occur for an ordinary orbit.

The actual conditional laws have total-variation distance tending to zero
from the common law. Every composed mixed test has uniformly bounded
supremum norm even though it depends on j. The stated factor-two bound for
bounded complex tests and its Cesaro mean justify transferring the same
limit to those actual laws.

The note explicitly does not prove Rajchman regularity, an integrable
density, or realization of arbitrary abstract endpoint marginals. Its
statement that the compact conclusion supplies no further restriction on
the actual nu is limited to this consumer. No lack of information about
nu is promoted into existence of an escaping orbit.

## 3. The endpoint observable and collisions

For the retained representative `R_j=q_j-chi_j*Z`, the real-leaf character
is `exp(-2*pi*i*h*chi_j*Z/Q)`. Conjugating it and multiplying by
`exp(2*pi*i*h*R_j/Q)` cancels the same Z pointwise, leaving
`exp(2*pi*i*h*q_j/Q)`. This proves (5) before any averaging or limit.

Applying finite Fourier orthogonality to the probability law of the
ordinary q_j modulo Q gives (6). It is the full collision probability;
its ordinary diagonal has not been silently subtracted. Separate
expectations cannot replace the mixed expectation, because the two
factors contain the same boundary variable. The real representative phase
is not a continuous function of the compact quotient alone.

The final source-law clarification is appropriate: under mu_j the affine
intercept is physical; under the common mu it is used as a comparison
expression, without declaring every common-law pair a legal inverse path
from that endpoint.

The proof concerns fixed continuous tests. It supplies no rate at a growing
ternary modulus and no same-limit collision upper bound. These are the
closing boundaries retained in the reviewed note.
