# Independent ordinary-mass review

**Verdict: VERIFIED AS CONDITIONAL DEDUCTIONS FROM THE STATED PDU INPUT**
for claims Q3–Q10 in
`research/global-synthesis-20261122/ORDINARY_MASS.md`.

Final file SHA256:
`9a37d90dd3de5333b44473cb0df038029dd33adff935ce10db11926dd1fa306d`.

The independent arithmetic researcher reconstructed the ordinary geometry
and finite summations, initially at the earlier byte pin and then at this
final file after the Lean evidence paragraph was added. The lead researcher
separately reconstructed Q1–Q10 and inspected the source-weight accounting
module. These are internal independent reviews.

## Reconstruction

Successive suffix minima exist on an injective positive-integer orbit,
increase strictly, and satisfy the displayed geometric upper bound. Each
odd ternary unit has exactly two unit parents among exponents one through
six. At most one lies on the prescribed orbit; the other is genuinely an
off-spine branch. Different such branches have disjoint predecessor basins.

For the least root `rj` of a selected branch basin, every state before
joining the spine is at least `rj`. The remaining spine has minimum `tj`.
This proves the exact identity `m(n)=min(rj,tj)` throughout `B(rj)`, and
therefore the required floor `m(n)>=3rj/64` without changing source weights.

The geometric root upper bound supplies a single explicit onset for the
first `N` basins at each finite source cutoff. PDU gives the natural moment
bound; nonnegative partial summation gives the harmonic bound. Optimizing
with `N=floor(L/log(3/2))+1` yields the exact nonnegative correction
`L/2 + log(3/2) u(1-u)/2` and the coefficient
`3c/(128 log(3/2))`. The truncated argument fixes `M` before sending the
source cutoff to infinity. No infinite disjoint-sum/density-limit interchange
is used.

## Formal and analytic boundaries

The separate Lean module retains explicit source-disjointness, minimum-floor,
and population premises. It checks finite accounting with identical original
weights in both the population and final moment. It introduces no analytic
population axiom. Its source SHA256 is
`05a2375e5fef1566cd6214cc059fd8d895d901601064b261b03d423896cd10dc`.

This review does not independently establish the imported PDU theorem or
extend the arithmetic researcher's verdict to Q11 and the canonical-flow
discussion. The lead separately checked that this discussion preserves the
pinned source-qualified status and the missing moving-weight comparison.
The required sublogarithmic upper moment is not proved. The deduction
excludes escapes only if that additional upper estimate is established;
positive cycles remain separate.
