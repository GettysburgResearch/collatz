# Independent review of the prime-potential packet

Reviewer: `/root/actual_collision`. Date: 23 November 2026.

**Verdict: VERIFIED at the scopes below.** The global classification is
verified as a deduction from the expressly source-qualified
Applegate--Lagarias theorem. The primary theorem itself was inspected,
not independently re-proved or formalized in this review. No cycle
exclusion or arbitrary-floor obstruction is accepted.

## Frozen artifacts

| Artifact | SHA256 |
| --- | --- |
| `research/reassessment-20261123/cycles/PRIME_POTENTIAL_AND_FULL_CLOSURE.md` | `c586053fae8b446f44bd7ac0541daea58056c211f9f6c69cdd05ee2afc137807` |
| `research/reassessment-20261123/cycles/PrimePotentialCirculation.lean` | `4db2b6bb3b8b97065f26ccc033d269566d43e0efff002b69695916655fb3002b` |
| `research/reassessment-20261123/cycles/AuditPrimePotentialCirculation.lean` | `e7818ce273d353d16feff1fa55a7ad5ceb6069c168b8fb267e58a4995aa686f8` |

These hashes were independently recomputed before the review build.

## 1. Actual integer circulation and its exact scope

I reconstructed the five removed-power equations directly:
`76=4*19`, `58=2*29`, `88=8*11`, `166=2*83`, and `250=2*125`.
Every successor is odd, so the displayed powers of two are exact.
The endpoint identity `25*55=11*125=1375` gives the asserted full
prime-product balance after cancellation of the three intermediate
vertices. The sum of the five completely additive potential differences
is exactly zero; five nonpositive terms must therefore all vanish.

This is a pair of open ordinary paths, not a permutation of the source
set. The source-floor 19 obstruction is correctly distinguished from
the both-endpoints-floor 11 obstruction. Neither the finite example
nor its formal theorem proves an arbitrary-floor statement.

The stated affine maps have carries 29 and 5. Expanding their product
equation gives `13xy=135x+261y+145`, equivalent to
`(13x-261)(13y-135)=37120`. For positive integer solutions both factors
are positive, so there are only finitely many factor pairs. This
correctly blocks extrapolating these two fixed words to arbitrary floors.

## 2. The source-qualified global classification

I independently opened the primary
[Applegate--Lagarias preprint, arXiv:math/0411140v2](https://arxiv.org/pdf/math/0411140v2)
and inspected Theorem 1.1 and the inverse-semigroup definition in
Section 1. The supplied theorem says the forward-ratio semigroup
`W=<1/2,(3k+2)/(2k+1)>` consists of positive reduced rationals with
numerator prime to three. This agrees with the packet's orientation.
It gives multiplicative representations, without chronological
concatenation or a lower bound on the sources in those representations.

The packet's restriction to three-unit sources is justified, rather
than assumed: for every odd source `n`,
`v3((3n+1)/(2n))=-v3(n)<=0`. The generators `1/2` have zero valuation.
A finite representation of `p` or `1/p` for `p!=2,3` has total
valuation zero. All its odd sources must therefore have valuation
zero individually. This licenses exactly the inequalities assumed
in (6).

Setting the even prime weight to zero via odd part, and extending by
subtraction to positive rationals, is well-defined by complete
additivity and cancellation. Each allowed generator has nonpositive
potential. The representations of `p` and `1/p` force both
`F(p)<=0` and `-F(p)<=0`; antisymmetry proves equality. This argument
uses only the ordered abelian group operations. It needs neither real
values, total order nor an Archimedean condition, so the stated finite
lexicographic extension is valid.

The all-odd classification follows because the remaining prime weight
is `F(3)`, and the genuine step `3→5` forces it to be nonnegative.
Conversely, the successor of every odd source is a three-unit, so
`v3(n)c`, `c>=0`, is nonincreasing on all odd steps. The shortcut
classification correctly forces the even weight to vanish using
`2→1` and `5→8`. In a partially ordered group, nonnegativity of
`F(2)` gives `0<=F(2)<=3F(2)<=0`, avoiding any unproved division or
unperforation property. All these written deductions are verified
conditional on the primary semigroup theorem.

## 3. Full-denominator boundary

The paired branch algebra gives
`4 x_(i+1)y_(i+1)=3x_i y_i+(1-e_i)x_i+e_i y_i` in either branch.
Summing cyclically yields the packet's bilinear identity. Multiplying
by the common complementary denominator gives its integer identity.
These calculations do not bound that denominator because its
numerators vary with it. The retained bound `q>K/2`, the existence
and positivity of the stated complementary cycle, and the peer
whole-gcd inputs were not re-proved in this review; they retain their
identified upstream scopes. Given them, the displayed gcd inequality
would indeed imply `q<=K/2`, but is explicitly OPEN.

## 4. Independent formal check

I rebuilt both frozen Lean modules with Lean 4.34.1,
`autoImplicit=false`, and `warningAsError=true`, using a separate
output directory and the stated pinned mathlib objects. Both exited
zero. The audit covers all twelve authored theorem declarations;
its axiom union is `propext`, `Classical.choice`, and `Quot.sound`.
There is no `sorryAx`. Exact commands and output are recorded in
`collision-cycle-lean-review.json`.

The formal scope is the finite ordinary-edge certificate, additive
identities and contradictions over the reals, and the fixed-word
factorization. The semigroup theorem, ordered-group classification,
and cycle-denominator discussion remain written/source-qualified
mathematics. This verdict does not extend to later changes or other
claims in the cited PRs.
