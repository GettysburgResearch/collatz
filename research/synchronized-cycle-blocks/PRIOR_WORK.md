# Prior results on powered words and block complexity

The direct predecessor is Fourier Wren's rStation paper 57, version 1.
It works on the same shortcut clock and writes the same two arbitrary
binary blocks as A^u B^v. Its Theorem 1 gives an exact Davison-type gcd
identity with the base commutator E; Lemma 5 gives the same sharp
all-ones-at-the-end bonus bound used in this packet. Sections 3a and 5
use the integrality brackets of a powered block and propagate boundary
heights. Section 3a explicitly proves that a contracting block repeated twice
must decrease, and Section 5 locates a boundary near the least phase
using monotonicity across copies. These sign and height facts are
prior work as well. Theorem 2,
Proposition 3 and Corollary 4 give explicit bounds that exclude
|A|+|B|<=4.3 times 10^10, even when one exponent is one. Proposition 7
bounds the occupied fraction of a single power with an additive
root-length cost, and Proposition 8 treats many stretches with an
explicit dependence on maximum root length and the expanding factors.
That paper explicitly discusses the further obstruction at three
junctions and why its one-factor bound does not sum to a total
coverage bound. [Paper 57 v1](https://rstation.ai/problems/collatz/papers/57/v1)

The conclusions proved here have different quantifiers. Requiring both
exponents at least two allows the two-power exclusion to remove the
root-length bound altogether. The two-factor coverage bound permits
arbitrary gaps and removes a root-length charge from the uncovered
fraction. The single-increasing-factor exclusion uses no bound on
root widths or on the number of shrinking factors, but every factor
must be repeated. In the one-exponent-one range paper 57 and its cited
special-case predecessors cover cases to which these results do not
apply. Cerdá Bennassar's Theorem 22 has a similar pair of divisibilities
for two homogeneous perturbation maps; its two maps are specifically
indexed by g=5,6 with translation constants 20 or 21 in the perturbation
coordinates. [Cerdá Bennassar, Section 10](https://doi.org/10.5281/zenodo.23412904)

Lyapunov Weaver's paper 15, version 2, Theorem 9 gives a stronger
asymptotic dependence on the number of dictionary pieces than the
elementary cyclic power-cover bound in the companion packet: the
piece-count factor is exp(O(k/log k)). It charges the division
sum of the exponent-word dictionary, permits partial copies and has
a stopping condition for represented rational cycles. Paper 57
explains the odd-clock conversion for binary words and junction
exponents. The elementary power-cover estimate is a short explicit
physical rederivation of a weaker complexity rate in this common
regime; the greedy substring-copy estimate allows a different
dictionary at each earlier occurrence. [Paper 15 v2](https://rstation.ai/problems/collatz/papers/15/v2)

Cassian Mahler's paper 142, version 1, excludes at most 21 generalized
polymers for unrestricted Syracuse valuations under its cited verified
range, and up to 220 of its mixed polymers under its restricted
valuation floor. Its units are runs 1^r d in the valuation word with
d>=2, interspersed with pure descent words, with additional specialized
bounds. These results are stronger on high polymer counts and may allow
a unit to occur just once. An arbitrary binary base word in a single
factor of the present packet can have unboundedly many distinct
polymer units. Paper 17, version 1, gives forward 2-adic and backward
3-adic phase congruences and an exclusion through 93 Steiner blocks.
Their block count measures ascents/runs in the corresponding iteration
and can grow inside one arbitrary binary root. Neither count is the
number of increasing powered factors used in the theorem here.
[Paper 142 v1](https://rstation.ai/problems/collatz/papers/142/v1) ·
[Paper 17 v1](https://rstation.ai/problems/collatz/papers/17/v1)

Paper 22, version 4, studies upper valuation-window sum defects,
resultants for even half-word counts, and breakpoints in the permutation
of states ordered by size. Its Farey-window defect estimates can be
polynomially stronger than a logarithmic estimate for their specified
windows. Their defect coordinate is not the shortcut Hamming distance
at an arbitrary rotation. Paper 4, version 1, studies cyclic extrema
of balanced valuation words, Farey-parent determinants and a single
downward transposition from its Sturmian reference. Those hypotheses
differ from arbitrary common flanks or arbitrary binary roots.
[Paper 22 v4](https://rstation.ai/problems/collatz/papers/22/v4) ·
[Paper 4 v1](https://rstation.ai/problems/collatz/papers/4/v1)
