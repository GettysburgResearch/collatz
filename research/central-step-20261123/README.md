# Direct construction attacks: finite rational witnesses and fast ordinary flows

23 November 2026. Base: `e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`.

Four parallel attacks produced two constructive interfaces and two
arithmetic constraints. The finite rational certificate now allows every
positive odd denominator, and the ordinary-flow construction supplies a
uniform collision comparison at arbitrary precision. The new Lean files
check twelve finite lemmas; the larger theorems have independently reviewed
written proofs. **Universal witness construction, the needed actual-orbit
collision upper bound, and full Collatz remain open.**

## Results and their exact scope

| Attack | New result | Verification | Remaining central obligation |
| --- | --- | --- | --- |
| [Arbitrary odd denominators](rational/FINITE_RATIONAL_CERTIFICATE.md) | An explicit finite number of complementary parity tests forces eventual periodicity, with primitive period at most `2q` | Seven numerical Lean lemmas, separate fresh build, independent review of the complete written certificate | Construct a candidate that satisfies its own horizon for each actual positive input; control nontrivial cycles |
| [Fast equivalent ordinary flow](stationary/FAST_EQUIVALENT_FLOW.md) | One positive harmonic reweighting preserves the original root's entire inverse law and makes inverse and original collision probabilities agree relatively, uniformly over all moduli and inverse clocks | Independent written proof review under the stated component hypotheses | Bound the actual residue collisions or the full effective number of source boxes |
| [Complementary cycle capacity](cycles/COMPLEMENTARY_DENOMINATOR_CAPACITY.md) | A nontrivial positive integer cycle of primitive shortcut length `K` has full reduced complementary denominator `q>K/2` | Independent written proof review; exact integer comparisons | Prove an incompatible upper bound on that denominator, or construct a sufficiently restricted dual |
| [Complete triadic selection](triadic/OPTIMAL_SELECTOR_AND_HEIGHT.md) | All-candidate rational-target cost and a necessary quadratic denominator cost throughout the specified separable potential class | Five finite Lean lemmas, separate fresh build, independent written review | Find source-specific arithmetic beyond those universal potential and approximation mechanisms |

No packet imports an unproved universal selector or a new collision upper
bound as an axiom. The formal and written scopes are separate throughout.

## 1. A finite certificate on the larger rational search space

For the shortcut map `T`, start at a literal positive integer `n`. Supply
an integer numerator `a` and an odd positive denominator `q`. Iterate

\[
x_k=T^k(n),\qquad w_k=S_q^k(a),\qquad
S_q(w)=\begin{cases}w/2,&w\text{ even},\\(3w+q)/2,&w\text{ odd}.
\end{cases}
\]

The finite test is that `x_k` and `w_k` have opposite parity. Put

\[
\begin{aligned}
J&=2q+2,&M&=n\max(1,|a|)(4q)^J,\\
L&=\operatorname{bl}(M),&H&=[J(4q+3)+1]L+J,
\end{aligned}
\]

where `bl(M)` is the least positive integer with `M<2^L`.
**Passing the first `H` tests forces the original orbit into a positive
integer cycle before `H`; its primitive period is at most `2q`.**

The mechanism uses the positive integer potential `x max(1,|w|)`.
Outside `[-q,q]` each tested step contracts it by at least the fixed
factor `(4q+3)/(4q+4)`. Inside that interval the potential can grow by at
most `4q`. This forces sufficiently many small-numerator visits within
the explicit horizon. A repeated numerator gives equal future dual
parities; the reserved final `L` bits then force two bounded original
states to be equal. Negative numerators and zero are included.

Equivalently, a candidate passes precisely when

\[
2^H\mid 3^{b_H}a+qD_H,
\]

where `b_H` and the complete carry `D_H` come from the complementary
word of the actual first `H` steps. This is a concrete finite arithmetic
target whose clock depends on the candidate itself. Its universal
solvability has not been proved. For `q=3^r`, the eventual complementary
denominator must be one, so the certificate gives convergence to the
standard cycle. The specialized triadic horizon from PR176 is much
smaller in that case.

Monks--Yazinski already proved the qualitative relation between rational
autoconjugacy of positive integers and nondivergence. The packet credits
that primary result. The work here is the explicit finite certificate
and its excursion proof; no historical priority claim is made.

## 2. Constructing the rate needed for the actual collision comparison

Fix a hypothetical escaping ordinary odd orbit `q_j`, with the supplied
positive harmonic flow `nu` and spine capacity `nu(q_j) -> C`. Weight the
mass first attaching at spine index `k` by `rho^k`, for one fixed
`0<rho<1`, and normalize to capacity `C`. This gives a positive harmonic
flow on exactly the same ordinary graph.

The whole inverse path law at `q_0` is unchanged. The new capacity tail
is exponential, and the inverse endpoint average `zeta_N` satisfies

\[
\|\zeta_N-\pi_N\|_{\rm TV}\le D/N,
\qquad \pi_N=N^{-1}\sum_{j<N}\delta_{q_j},
\]

uniformly over arbitrary finite deterministic inverse depths at the
aligned future roots. Since every residue collision of `pi_N` is at
least `1/N`, this yields

\[
(1-\delta_N)_+^2\operatorname{Col}_Q(\pi_N)
\le\operatorname{Col}_Q(\zeta_N)
\le(1+\delta_N)^2\operatorname{Col}_Q(\pi_N),
\qquad \delta_N=\sqrt2D/\sqrt N,
\]

simultaneously at every modulus `Q`. The earlier comparison-rate
obligation can therefore be met by an explicit choice of flow.

The remaining collision estimate concerns the original orbit. For
`1<=m<N`, with the complete source boxes from PR182, the precise consumer is

\[
\operatorname{Col}_{3^m}(\zeta_N)
\le\left(\frac{\sqrt{(N-m)\mathcal B_{N,m}}+m+D}{N}\right)^2,
\quad
\mathcal B_{N,m}=\left(\sum_B\sqrt{\frac{N_B}{N-m}}\right)^2.
\]

All translated carries, source heights, cross-box terms, and omitted
mass remain. No subexponential estimate for this actual effective box
count was obtained. The fixed-root reciprocal floor is preserved; one
global uniform reciprocal constant on the entire component is not
asserted for the new flow. PR180's finite-deficit and geometric-iid
branches keep their separate orders of limits.

## 3. The arithmetic constraints discovered in parallel

The cycle attack applies an exact product identity to the distinct odd
numerators in the complementary rational cycle. A strict convexity
bound and the ordinary cycle's odd-step proportion imply `K<2q` for a
nontrivial cycle. The core has equality `K=2,q=1`. This controls the
period after the finite certificate proves a cycle; it supplies no
upper bound on the denominator by itself.

For the specialized triadic search, use the newly improved PR176 weight

\[
F(r)=\prod_{0\le j<r}(1+3^j),\qquad
H_{\rm triadic}=9\operatorname{bl}\bigl(nF(r)\max(1,|a|)\bigr)+1.
\]

The new selector optimizes over all signed numerators and all triadic
exponents. Two proved constraints explain what a successful construction
must exploit. For a positive weight `G(r)>0`, every separable product
`x|w|G(r)` that is nonincreasing on
all eligible ordinary paired steps satisfies

\[
F(r)G(0)\le4^rG(r).
\]

Thus this entire potential class retains the leading quadratic cost in
`r`. Separately, if a matching target is the fixed reduced nontriadic
rational `u/d`, every triadic candidate matching `K` bits obeys

\[
2^{K+1}\le(2d+3|u|)F(r)\max(1,|a|).
\]

This includes changing terminal numerators and denominators; the initial
triadic grid still has to be met. Generic rational approximation does
not close the broader construction either: an even denominator loses
bits when normalized, and the note gives an exact odd-denominator
obstruction with its ordinary source-height qualification retained.

## Sources, reviews, and reproducibility

The initial refresh covered the latest 30 updated open PRs. The changed
working set was pinned at PR175 `53ba1e1`, PR176 `fb40240`, PR177
`aaa132e`, PR180 `a436db7`, and PR182 `a7fd3ac`. The source ledgers record
full hashes, exact file paths, and the role of each imported assertion.
This pass inspected the changed dependencies and new proofs rather than
rebuilding the old Lean corpus.

The [report index](../../reports/2026-11-23-central-step/README.md)
links all author and independent Lean receipts, raw logs, independent
written reviews, source pins, and the packet integrity manifest.
Both pairs of new modules passed strict builds with Lean 4.34.1 and
mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.
All twelve authored theorem declarations are covered by the axiom
audits and use only standard Lean axioms. Existing dependency objects
were reused. The repository's required gate is separately run on the
complete clean checkout of the exact publication commit; that gate is
an integrity check, not a proof of the open theorem.
