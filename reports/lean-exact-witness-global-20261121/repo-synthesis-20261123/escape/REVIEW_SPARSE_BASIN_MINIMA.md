# Reconstruction review: the ordinary first-hit basin-minimum theorem

Reviewer: `/root/global_escape_attack`. Date: 23 November 2026.
Source:
`research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/SPARSE_BASIN_MINIMA.md`.
SHA256: `65f1a0698cb3a17a8eb52ddab42f6b548be5bb921872f71c4d9cb00369ccbeec`.

**Verdict: VERIFIED as written mathematics at these exact bytes.** The
reviewing lane contributed the rational 1/32 tail margin and the horizon
1/25 choice during construction; this is a reconstructed internal proof
review, not an independent discovery or external referee acceptance.

## Reconstructed core

BM1–BM2 retain full positive shortcut predecessor basins. A smaller
positive value before first hitting the root would still reach the root,
contradicting minimality. Therefore actual descent of the minimum at
clock H forces the specified root to have been hit by H. The possible
ternary divisibility of the full minimum is harmless because its role is
source counting; it is not made into a unit-pressure atom.

Upper siblings are off the whole injective odd ray. Any forward path
from a sibling enters that ray at its next odd point; intervening
shortcut states are even. This proves pairwise incomparability and full
basin disjointness, including different sibling depths.

The complete carry satisfies C<=3^H−2^H. If a non-descent source has a
subcritical coefficient, the positive integer denominator 2^H−3^p is
at least one, so that source is strictly below 3^H. All other parity
words have p>=5H/8 by 3^5<2^8. The weighted binomial tail and the exact
integer margin 2^65<3^12·5^20 give BM8 without a random-orbit premise.

The high-root count keeps one fixed odd orbit. The inherited bound
4Y^(39/40) is not applied to a basin. Summing over all sibling depths
costs the convergent geometric factor 1/(64^(39/40)−1)<1.

At H=floor(log_2 X/25), the four exponents are 8/125, 799/800, 31/800,
and 624/625. The latter three comparisons and the floor factor
2^(1/32) are retained. The coefficients total less than twelve. This
proves BM3 for every X>=1 without an omitted small-source cutoff.

## Optional sharper statement and boundaries

For BM14–BM15, the critical binomial tail is of order
2^(theta H)/sqrt(H), and the separately pinned PR182 whole-orbit bound
controls separated visits. The displayed choice of c equates
1−c(1−theta) and theta(1+c log_2(3/2)); both other exponents are strictly
smaller. The sibling-depth split preserves the square-root logarithm.
This checks the deduction conditional on that cited written orbit bound;
it does not supply a fresh audit of all PR182 source files or the stronger
external interval-compression manuscript.

The new theorem counts basin minima, hence how many basins meet a low
source range. It does not bound the population of an individual basin.
The subsequent pressure summability and its positive Green comparison
consumer have their own proof in the companion note. BM3 alone does not
exclude an escaping ray or a nontrivial positive cycle.

The review checked the algebra and quantifiers directly. The separate
finite checker supplies arithmetic examples; it is not the basis for
the universal exponent assertion. Finite Lean formalization includes
the actual first-hit and height interface, but not the real asymptotic
analysis merely by naming it.
