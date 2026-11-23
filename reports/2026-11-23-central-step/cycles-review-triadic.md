# Independent review: optimized triadic selection

23 November 2026. Reviewer: `cycle_symmetry`.

**Verdict: VERIFIED at the exact bytes below, with the stated separation
between five finite Lean theorems and the written interpretation.** The
optimized selector, forced weight growth, rational-target separation,
asymptotic classification, and rational-approximation controls follow
from their stated hypotheses. The universal small-candidate construction
remains open. No full Collatz theorem is included in this verdict.

## Frozen source and execution boundary

This is new local work over base commit
`e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`, not yet a committed source
head at review time. The following SHA-256 hashes fix this review; it
does not cover later changes.

| Source | SHA-256 |
| --- | --- |
| `research/central-step-20261123/triadic/OPTIMAL_SELECTOR_AND_HEIGHT.md` | `f75d052b925c7b1bfbf439bb44c9d2770c1865596cebbd095b7dc4575b82fb92` |
| `research/central-step-20261123/triadic/README.md` | `6500c4064b1573e225f92e598e35ad6b81d9987bddc25d740c3cac833849d919` |
| `research/central-step-20261123/triadic/lean/WeightedSelector.lean` | `affb4c0336e5763680ffbb2cc1f17b727d404f225580f2826f5ffac159174fb0` |
| `research/central-step-20261123/triadic/lean/WeightedSelectorAudit.lean` | `7bbbf45e0a34d113cabdcedf3575f577cbbed920743018f08d9e6fae8d42f654` |
| `reports/2026-11-23-central-step/triadic-lean-receipt.json` | `835f8a4b5f286ac53810f36b2b829d83e9cf6af65e1e1f17facc1c6e8680fe8e` |

I checked those hashes before and after independently rebuilding both
new modules with Lean 4.34.1, `autoImplicit=false`, and
`warningAsError=true`. Generated module files went to a fresh reviewer
directory outside the checkout. Both invocations exited zero; the
ordinary compile log is empty. Every one of the five authored theorem
declarations is present in the audit, and their only reported axioms
are `propext`, `Classical.choice`, and `Quot.sound`.

The exact independent invocation, environment, sources, and logs are
recorded in [cycles-selector-lean-receipt.json](cycles-selector-lean-receipt.json),
whose SHA-256 is
`b634977e8fa29f1656bc1ab7d1fe89567ea29acc4204e61f527329023f4a3ee1`.
The compile and audit logs are
[cycles-selector-compile.log](cycles-selector-compile.log) and
[cycles-selector-axioms.log](cycles-selector-axioms.log).

I also directly fetched and read the two mathematical dependencies at
their immutable peer heads:

- PR176, `fb402404deb810bd8e32e596993739bb5a6967d1`,
  `research/lean-global-resolvent-20261121/overview/triadic-height/TRIADIC_AMORTIZED_BUDGET.md`,
  Sections 1--4: the weighted product and the `9 bl(B)+1` sufficient
  clock, including its zero-numerator branch.
- PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
  `research/whole-repo-round3-20261123/TRIADIC_CLOSURE.md`,
  Sections 4 and 6: the full fixed-denominator residue classes, the
  initial-grid restriction, and the source-height qualification.

This review did not rebuild their earlier Lean dependency trees or
assert a new review of the Borel--Dwork literature packet. The latter
is not a dependency of the new mathematical conclusions.

## 1. Exact optimization at the unchanged ordinary source

With the shortcut map and actual parity word as stated, the complete
complementary carry satisfies
`D_(K+1)=3^(1-e_K)D_K+(1-e_K)2^K`. Since powers of three are units
modulo `2^K`, legal initial numerators at denominator `3^r` form exactly
one residue class, `a = 3^r omega_K mod 2^K`. Centering minimizes the
absolute numerator in that class, including the tied endpoints and
the zero case. It therefore minimizes `max(1,|a|)` as well.

For `K>=1`, the exponent-zero candidate has cost at most `2^(K-1)`.
Since `F(r)>=2^r`, the minimum has a finite nonempty search set.
The stronger bound `F(r)>=3^(r(r-1)/2)` gives the claimed square-root
order for the admissible exponent range. Reducing a common factor of
three strictly reduces the cost at positive exponent, so lowest terms
can be assumed without deleting a possible optimum.

The residue classes at clock `K+1` are subsets of those at clock `K`.
Their minimum costs are thus nondecreasing. A candidate matching the
first `K` actual tests has its sufficient clock at most `K` exactly
when `9 bl(n F(r) max(1,|a|))+1<=K`; minimizing this expression gives
equation (5). The equivalence concerns the stated sufficient
certificate, not every possible proof of convergence at that clock.

The prior weighted-product proof is applicable to signed numerators.
Its nonzero product decreases by a fixed factor over eight steps;
creation of a zero numerator is separately paid for by the same
initial bound and a divisibility argument. The new selector does not
silently drop that branch or change the ordinary input.

## 2. Necessary growth for a separable all-state weight

For denominator exponent `j+1` and numerator one, the original-even
paired step sends the numerator to `(1+3^j)/2` at exponent `j`.
For even `j` this new numerator is odd, and `4 -> 2` supplies the
opposite original parities at both states. For odd `j` the new
numerator is even, and `6 -> 3` supplies them. Every original state
used is positive and greater than one. Thus these are legal
nonterminal tests of the declared all-state condition, rather than
an invented parity cylinder with no ordinary realization.

Nonincrease of `x |w| G(r)` gives

\[
 (1+3^j)G(j)\le4G(j+1).
\]

Multiplying these inequalities yields
`F(r)G(0)<=4^rG(r)`. Taking logarithms and using the preceding lower
bound for `F` gives equation (10), including its leading quadratic
coefficient. The Lean induction checks precisely this finite product
implication for natural weights; the written positive-real extension
uses the same multiplication and cancellation.

The two ordinary sources are separate tests of a uniform proposed
potential. The proof does not identify their pairs as successive
states on a single trajectory or as optimal candidates for a
hypothetical escaping source. The stated restrictions to separable
potentials and one-step nonincrease are therefore necessary scope
conditions and are retained throughout the note and README.

## 3. Uniform rational-target height separation

For a reduced target `u/d` with odd positive `d` having a prime factor
other than three, a `K`-bit matching triadic candidate satisfies
`2^K | d a-u 3^r`. The cross-product is nonzero: equality would imply
`d | 3^r` by coprimality of `u` and `d`. Divisibility and the triangle
inequality then give

\[
 2^K\le d|a|+|u|3^r.
\]

The weight estimate `2 3^r<=3F(r)` holds at zero, is an equality at
one, and is preserved at subsequent exponents because each new
factor is at least three. If `B=F(r)max(1,|a|)`, then `|a|<=B` and
`2 3^r<=3B`. Multiplication and addition yield exactly

\[
 2^{K+1}\le(2d+3|u|)B.
\]

This argument is uniform in both numerator and exponent. It has no
hidden fixed-terminal hypothesis. The Lean statements expose the
nonzero cross-product and divisibility as hypotheses and prove the
finite inequalities with absolute values, so they do not assume
the unknown dual of an arbitrary ordinary source is rational.

The lower bound has a constant independent of `K`, and the
exponent-zero centered candidate gives the upper bound
`2^(K-1)`. Their logarithms, divided by `K`, prove the limit one.
For a triadic target, its own reduced representation is always
available. Any bounded cost level contains only finitely many
different rational candidates; after sufficiently many bits, every
other member of that level is excluded. This proves eventual exact
stabilization at the target's own cost. The same finite-level
argument implies divergence of the optimum for an irrational
target, but provides no rate.

A hypothetical nontrivial positive integer cycle does have a
rational complementary dual. If that dual were triadic, its exact
candidate would pass every test and the pinned sufficient theorem
would make the original cycle reach one. Thus the nontriadic
conditional calculation applies. It describes the cost of all
triadic matches to such a cycle; it supplies no contradiction to
the cycle's existence.

## 4. Odd-denominator approximation and source height

The close-pair pigeonhole argument produces a denominator
`1<=q<=Q` and error at most `ceil(2^K/Q)`, but imposes no oddness
condition on `q`. If `v=v_2(q)<K`, the congruence also makes the
numerator divisible by `2^v`; division preserves precisely a
`K-v` bit congruence. Retaining the original clock after that
division would be invalid.

For `omega_K=2^(K-1)-1` and odd `q<2^(K-1)`, direct reduction modulo
`2^K` gives centered numerator `2^(K-1)-q`, as claimed. The first
`K-1` shortcut steps of `2^(K-1)-1` are odd, with explicit state
`3^j 2^(K-1-j)-1`; its next parity is even. The complementary
original word is therefore `0^(K-1)1`, whose least positive ordinary
source is `2^(K-1)`. Its `K`-bit height prevents this generic
residue control from being an example within a funded small-source
horizon.

The text correctly distinguishes a weak guaranteed approximation
bound from a lower bound on a fortunate actual approximation. It
does not rule out a source-specific construction with arbitrary
odd denominators. Its final unsupported inference is explicit:
construct a candidate for the unchanged ordinary source whose
height fits its own certified clock.

## Review outcome

No mathematical correction was needed at the frozen hashes. Before
freezing, the private positivity helper was made public and added
to the audit; the final all-five-theorem coverage was independently
checked in the fresh build. The full selector construction,
source interpretation, asymptotics, and positive-real weight
extension remain written mathematics. No repository-wide validator
or numerical cycle search was run for this review.
