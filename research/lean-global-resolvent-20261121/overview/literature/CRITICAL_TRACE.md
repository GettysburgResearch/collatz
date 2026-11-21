# A critical ordinary trace can control escape and all cycle heights

**Status:** the finite propagation and finite-cycle minimum arguments are
proved in Lean. Construction of the positive profile is a separate written
argument conditional on frozen PR180 CFJ. The required sublinear estimate is
OPEN. No full Collatz conclusion is asserted.

**Priority and integration update:** PR180 at
`d0349de2108abb7c8fb8393c086610e3372df116` already proves a stronger
closing interface in `MarkedDensityPotential.lean`: sublinearity is needed
only on the forced marked section. Its short-parent and additive-transfer
theorems also subsume the mechanism behind the cycle calculation below.
This note records an independently compiled general trace interface, not
a stronger new reduction. The [canonical Abel comparison](ABEL_CANONICAL_COMPARISON.md)
now upgrades the constructed critical profile to a harmonic one. The
[latest reconciliation](LATEST_REPO_RECONCILIATION.md) gives the current
remaining obligation and exact source pins.

## 1. The operator and the profile

For positive odd integers put

\[
U(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
\]

Restrict to ternary units; this domain is forward invariant. Consider a
finite real-valued function `h`, nonnegative everywhere on this domain, with
`h(q)>=alpha>0` and the full inverse excessiveness inequality

\[
\sum_{U(x)=q}\frac3{2^{v_2(3x+1)}}h(x)\le h(q). \tag{1}
\]

The word *full* matters: separate one-parent inequalities suffice for
propagation along an escaping path, but the cycle argument needs the sum
of two distinct parents. Existence of such an `h` is supplied conditionally
in [the Green note](ANCHORED_INVERSE_GREEN.md), with finite positive values at
every stated ordinary integer. No almost-everywhere representative is
substituted for those values.

## 2. One fixed escaping source cannot lose its trace ratio

For an actual odd trajectory `q_0,q_1,...`, write

\[
3q_k+1=2^{a_k}q_{k+1},\qquad
P_k=\prod_{j<k}\left(1+\frac1{3q_j}\right).
\]

Taking one nonnegative term in (1), and retaining the affine correction,
gives

\[
\boxed{
\frac{h(q_k)}{q_k}P_k\ge\frac{h(q_0)}{q_0}.
} \tag{2}
\]

If `P_k<=K` for all `k`, the same initial source therefore gives

\[
\frac{h(q_k)}{q_k}\ge\frac{h(q_0)}{Kq_0}>0. \tag{3}
\]

The finite-distinct-segment packing argument in the Green note bounds
reciprocal occupation and hence these products on every escaping positive
orbit. Therefore an ordinary pointwise estimate `h(q)/q -> 0` excludes
escape. This implication retains the same `q_0`, every actual exponent,
and the actual correction product. A discounted trace loses an additional
factor at each step and cannot be substituted in (2).

[`CriticalTrace.lean`](../lean/CriticalTrace.lean) proves `edge_trace`,
`propagated_trace`, `trace_ratio_lower`, and `no_arbitrarily_small_trace` for
general positive real paths satisfying the exact edge relation. The theorem
`ordinary_edge` derives that relation from the natural-number identity above.
`bounded_of_sublinear_trace` then proves boundedness of any supplied ordinary
path under the explicit sublinear and correction-product hypotheses. It
does not assume the open estimate as a global axiom.

## 3. A cycle has a uniform positive trace ratio at every vertex

For every positive odd unit `q`, at least two exponents in `{1,...,6}` give
distinct positive odd unit parents `(2^e q-1)/3`. The residue choices modulo
nine are

| `q mod 9` | Two exponents |
|---|---|
| 1 | 2, 4 |
| 2 | 1, 3 |
| 4 | 2, 6 |
| 5 | 3, 5 |
| 7 | 4, 6 |
| 8 | 1, 5 |

On a positive odd cycle, one parent is the preceding cycle vertex. At least
one of the two displayed parents is different. Its contribution to (1) is
at least

\[
\kappa=\frac{3\alpha}{64}. \tag{4}
\]

Choose a cycle vertex `q` minimizing `g=h/q`, and let its cycle parent be
`x`, with `3x+1=2^e q`. Then

\[
g(q)\ge\frac{3x}{3x+1}g(x)+\frac\kappa q
\ge\frac{3x}{3x+1}g(q)+\frac\kappa q.
\]

Hence

\[
\boxed{g(q)\ge\kappa 2^e\ge2\kappa
=\frac{3\alpha}{32}.} \tag{5}
\]

Every other cycle vertex has at least this ratio by minimality. No cycle
length estimate or bound on its largest exponent enters this proof.

The Lean theorems `cycle_minimum_ratio`, `finite_closed_trace_floor`, and
`finite_closed_below_cutoff` prove the minimum argument for an arbitrary
finite closed predecessor family, keeping the positive side-parent
contribution as an explicit hypothesis. The elementary modulo-nine table
and the deduction of that contribution from the full infinite operator are
written bridges, not additional hidden Lean premises.

## 4. The resulting full closing criterion

Suppose (1) and the positive floor are established, and suppose one proves
an effective ordinary sublinear estimate with a specified `M` such that

\[
q\ge M\quad\Longrightarrow\quad
\frac{h(q)}q<\frac{3\alpha}{32}. \tag{6}
\]

Sublinearity and (2)--(3) exclude every escaping orbit. Every bounded
ordinary orbit eventually enters a finite cycle. Equation (5) then places
**all vertices** of every positive odd cycle below `M`. An actual convergence
certificate for every positive odd integer below `M` rules out all remaining
cycles except the one at `1`. Initial even states reduce to odd states by
halving, and an odd multiple of three maps into the unit domain in one odd
step. These statements give full convergence.

This is a conditional route to the full theorem. A tail bound merely below
`3 alpha/32`, without sublinearity, does not exclude escape. An ineffective
existence statement for `M` does not furnish the required finite-core
verification. The critical sublinear estimate and a usable verified cutoff
remain the first unsupported steps.
