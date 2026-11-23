# Complete triadic selection and the cost of denominator freedom

23 November 2026. **Universal witness construction and full Collatz remain
OPEN.**

[The main note](OPTIMAL_SELECTOR_AND_HEIGHT.md) optimizes over every signed
triadic candidate at the unchanged ordinary source, using PR176's improved
weighted horizon. Its two main deductions are:

- Every nonincreasing separable product `x |w| G(r)` on all legal
  nonterminal paired steps requires `F(r) G(0) <= 4^r G(r)`. Its logarithmic
  denominator cost must therefore have the same leading quadratic order
  as `F(r)=prod_(j<r)(1+3^j)`. This conclusion concerns that entire
  potential class, not every possible source-specific argument.
- A fixed reduced nontriadic rational target `u/d` forces every matching
  triadic candidate to satisfy
  `2^(K+1) <= (2d+3|u|) F(r) max(1,|a|)`. Consequently its optimized
  cost has logarithmic growth rate one, even when terminal numerators,
  terminal denominators, and the initial triadic exponent all vary.

The exact optimized selector and its success criterion are an organization
of the pinned prior arithmetic and budget, not an unconditional new
small-residue estimate. The note also checks the loss of precision when
normalizing even denominators in rational approximation, gives an explicit
generic obstruction to a same-clock odd-denominator guarantee, and retains
the source-height qualification that prevents that obstruction from being
misread as a Collatz counterexample.

[WeightedSelector.lean](lean/WeightedSelector.lean) checks five finite
arithmetic lemmas. [Its audit](lean/WeightedSelectorAudit.lean) prints the
axioms of every authored theorem. The selector interpretation, real-weight
extension, asymptotic statements, and attempted construction have written
proof scope. No universal candidate assertion is introduced as an axiom.

The exact pinned peer inputs are recorded in
[`triadic-sources.json`](../../../reports/2026-11-23-central-step/triadic-sources.json).
The strict Lean invocation and source/log hashes are recorded in
[`triadic-lean-receipt.json`](../../../reports/2026-11-23-central-step/triadic-lean-receipt.json).
