# Independent review: divergent-orbit phases

**Reviewed source:** the root repository version at
`collatz-lean/research/lean-forward-band-20261121/DIVERGENT_ORBIT_PHASES.md`,
including its final sweep-out section. I also checked the `15(d+1)` clock
interface in the root population note. No compiler or test work was run.

## Verdict

**No mathematical gap found, conditional on the uniform predecessor-density
statement (P).** In particular, there is no unjustified exchange of an
infinite sum with a density limit.

## Graph and density checks

- Among the three legal exponents in `{1,...,6}`, exactly two produce odd
  unit parents. Each parent satisfies `b < (64/3)q < 22q`. In a forward
  odd orbit with all entries distinct, at most one such parent can be an
  orbit member: its index must be `i-1`. The off-orbit choice therefore
  exists for every index, including index zero.
- The ordinary path from an off-orbit parent has no subsequent odd points
  outside the specified forward odd orbit. A shared ordinary predecessor
  of two chosen parents would put one parent later on the other's
  deterministic trajectory. Its oddness then contradicts the off-orbit
  choice. Equal encounter clocks would make the parents, and hence their
  distinct children, equal. Thus the *full ordinary* predecessor sets are
  pairwise disjoint.
- For each fixed finite number of branches, their harmonic counts sum to
  at most the full harmonic count. Finite liminf superadditivity and (P)
  give `c_0 sum_(i<m) 1/b_i <= 1`; no common target-independent onset is
  required. The inequality `b_i < 22q_i` then bounds every finite partial
  sum of `sum 1/q_i`. Passing to increasing partial sums is valid and is
  separate from the density limit.

## Phase and return checks

- The exact logarithmic recursion gives positive errors bounded by
  `1/(3 log(2) q_i)`. Reciprocal summability therefore yields the stated
  convergent correction and exact identity
  `log_2 q_n = n alpha - A_n + theta - r_n`, with `r_n -> 0`.
- A vanishing phase perturbation preserves irrational-rotation
  equidistribution, first for continuous periodic test functions and then
  for intervals whose boundaries have zero Lebesgue measure. Thus the
  stated base-2 Benford conclusion holds in **odd accelerated time**.
  No claim about variable ordinary-clock weights is used.
- Distinct positive integer values tend to infinity, even though they
  need not increase monotonically. Hence the marked window width tends
  to zero. Bounding late marked visits by any fixed interval `[0,eta]`
  proves zero asymptotic frequency without requiring a shrinking-target
  discrepancy estimate.
- PR173's future visit theorem applied after any proposed last marked
  visit proves there are infinitely many visits. Zero frequency then
  gives `i_j/j -> infinity`; telescoping gives divergence of the mean
  return gap. This does not imply that individual gaps tend to infinity.
  Ordinary gaps are at least their odd-time counterparts.

## Sweep-out check and one wording suggestion

The root population theorem supplies the required clock bound. Each
successful octave contributes at least `gamma/2` to the squared-logarithmic
harmonic weight, and unbounded octaves are disjoint. This proves the
weighted divergence in (5.1). The ordinary harmonic lower guarantees form
a convergent series; the manuscript correctly does not infer convergence
or divergence of the actual harmonic sum from that fact.

The final disjointness statement for equal-clock predecessors of a
nonperiodic target is valid: a forward relation between two such sources
would make the target periodic. For clarity, explicitly say **unit
equal-clock predecessors** when subsequently invoking their lower density
coefficients from (P). Disjointness itself does not require the unit
restriction, but (P) does. The available unit-source appendix supplies the
needed restricted families, so this is a wording clarification rather than
a gap in the stated main result.

The argument excludes divergent orbits with divergent reciprocal sum.
It does not exclude all divergent orbits or additional cycles; the final
closure status accurately retains those unresolved cases.
