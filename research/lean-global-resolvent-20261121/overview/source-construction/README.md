# An accepted finite candidate is the exact all-time candidate

Checkpoint 17, 23 November 2026. **Full Collatz remains OPEN.** The new
Lean theorem strengthens checkpoint 16 without enlarging its premise:
one candidate that passes its prescribed finite horizon reaches the
exact complementary cycle and stays compatible forever. The universal
construction of such a candidate remains the central missing theorem.

Three agents pursued candidate construction, an infinite pressure-optimal
ray, and complete cycle cancellation in parallel. The coordinator pursued
the actual-boundary rigidity route. The results below distinguish a new
formal theorem, written universal controls, and attempted closing arguments.

## 1. The same finite premise now forces exactness

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Fix a positive ordinary integer n and one signed rational candidate
`a/3^r`, with a integral and r nonnegative. Use the unchanged literal
paired-state rules and opposite-parity tests from checkpoint 16. Put

\[
 F(r)=\prod_{j<r}(1+3^j),\quad
 B=n\max(1,|a|)F(r),\quad E=\operatorname{bl}(B),\quad H=9E+1.
\]

Here `bl(B)` is the least positive E such that `B<2^E`. The denominator
representation need not be reduced. The horizon is computed from this
same unchanged input and candidate.

**New formal conclusion.** If the first H tests pass, there is a clock
`tau<=8E` at which

\[
                   x_\tau=1,\qquad w_\tau=2\cdot3^{r_\tau}.
\]

Thus the supplied candidate reaches the exact complementary value two
when the original coordinate is one. Every subsequent test passes for
that same candidate. In particular,

\[
 \boxed{\text{first H tests pass}\quad\Longleftrightarrow\quad
        \text{all tests pass}.}
\]

The principal declarations in
[TriadicCertificateRigidity.lean](lean/TriadicCertificateRigidity.lean) are
`finite_triadic_exact_pair`, `finite_certificate_alltime`, and
`finite_certificate_iff_alltime`, in namespace `CollatzTriadicRigidity`.
The [complete proof](EXACT_CANDIDATE_RIGIDITY.md) and
[formal scope](FORMAL_SCOPE.md) specify which further consequences remain
written mathematics.

### Why the remaining finite tail forces equality

The previous integer potential gives an original hit of one or a zero
numerator by `8E`. A zero before that hit is impossible: the available
following `E+1` tests force a positive integer no larger than `2^E` to
be divisible by `2^(E+1)`. Hence an original hit occurs by `8E`.

At its first hit, the same potential bounds the terminal defect

\[
             d=w_\tau-2\cdot3^{r_\tau},\qquad |d|<2^{E+1}.
\]

On the original `1,2` cycle, each compatible step removes a required
factor of two from this defect, with a possible multiplication by three.
The remaining `E+1` tests therefore force `2^(E+1)` to divide d. The size
bound makes d zero. The exact paired cycle is then invariant under the
literal deterministic rules. The proof includes initially zero candidates,
zero entry, n=1, and deliberately unreduced representations.

### Written arithmetic consequences

For n>2, reduce an accepted value to `a_*/3^r_*`, and let `b_tau` count
the original even inputs before its first hit. Backward reconstruction
from the forced final segment `4,2,1` gives

\[
 r_*=b_\tau-1,\qquad
 n3^{\tau-r_*-1}\le2^\tau,
 \qquad
 \tau\le\frac{(r_*+1)\log3-\log n}{\log(3/2)}.
\]

Equality in the clock bound occurs for powers of two; it is strict when
the first-hit path has an odd input. Outside `{1,2,4}`, every accepted
candidate is negative, with first sign crossing exactly
`(8,-1/9)->(4,1/3)`. These are proved written corollaries, independently
reconstructed, rather than additional Lean declarations.

This narrows what a construction must achieve. A candidate accepted at
its own prescribed height cannot merely imitate the complementary word
and depart later. It is already the exact all-time candidate. The result
does not produce that candidate for an arbitrary n.

## 2. The direct construction attempt

Let `e_i` be the actual first K shortcut bits, `b_K` the number of even
inputs, and retain the complete complementary carry

\[
 D_0=0,\qquad D_{i+1}=3^{1-e_i}D_i+(1-e_i)2^i.
\]

The unresolved target is still to construct a, r, K for **every fixed
positive ordinary n** such that

\[
 K\ge9\operatorname{bl}\bigl(n\max(1,|a|)F(r)\bigr)+1,
 \qquad 2^K\mid3^{b_K}a+3^rD_K.
\]

The complete-carry implication to literal finite compatibility is the
reviewed written bridge from checkpoint 16. The
[standalone finite arithmetic question](../triadic-height/TWO_CARRY_CONSTRUCTION_QUESTION.txt)
retains both the original and complementary carries.

The [construction attempt](CARRY_CONSTRUCTION_ATTACK.md) tested terminal
interpolation and denominator resets. It proves an all-target lifting:
given N>0 and a positive integer u, let R be the least positive integer
with `2^R(u+1)<3^R`. Then

\[
 x_0=2^RN,\qquad y_0=\frac{2^R(u+1)-3^R}{3^R}
\]

is initially negative, crosses positive at the first step, and reaches
`(N,u)` after R legal paired steps. Choosing u in a complementary residue
class supplies any prescribed finite continuation. The starting source
and candidate change with u, so this does not satisfy the fixed-source,
own-height construction target. The exact denominator-reset normalization
is also derived; a sufficient global estimate for the original-n-selected
chain was not obtained.

## 3. Three other attacks on the closing step

| Attack | What this pass established | Missing inference |
|---|---|---|
| [Infinite optimal ray](INFINITE_OPTIMAL_RAY_ATTEMPT.md) | A fixed-source simultaneous real/2-adic/3-adic Subspace-Theorem attempt has exact linear-form product `S(q_k)>=1`. The negative rational cycle anchors give exact congruences to the actual endpoints. | Obtain a height saving or an admissible better ancestor. The inspected terminal-word theorem has fixed-anchor, nonuniform onset; the anchors here change with k. |
| [Actual boundary and ordinary labels](HAAR_AND_ORDINARY_LABELS.md) | An exact finite total-variation bound removes the valuation clock from the long averaging shape. Under an explicit additional Rajchman hypothesis, the unthickened joint limit is `Haar x nu`, where nu is the actual endpoint law. An exact mixed-phase identity recovers the endpoint. | Estimate that same mixed phase, or the equivalent actual cross-box collision terms. Compact Haar convergence alone does not estimate the endpoint marginal. |
| [Complete cycle/product transfer](CYCLE_PRODUCT_TRANSFER_ATTEMPT.md) | Every positive rational one-rise cycle has a multiplicatively Sidon odd-state set. There are such primitive nonintegral cycles above any prescribed floor and with arbitrarily large period. | Supply a consequence of full ordinary integrality that contradicts product growth, or a transfer to the same complete carry zero fibre. |

The cycle result is uniform, not a bounded search. For `p>=2`, `A>p`,
and `2^A>3^p`, the shortcut word `1^p0^(A-p)` has

\[
 D=2^A-3^p,\quad C=3^p-2^p,\quad t=C/D.
\]

If B is its entire set of p odd states, then

\[
                   |BB|=p(p+1)/2,\qquad E_\times(B)=2p^2-p.
\]

The proof uses strictly decreasing shifted two-adic valuations after
clearing the same full denominator. Irrational-rotation density produces
arbitrarily long examples with `H<t<4H` for any H>=1; a separate valuation
argument proves their reduced denominator is nontrivial. These are rational
controls, not positive integer counterexamples. The inspected incidence
and energy results remain credited to their primary manuscript.

## 4. Evidence and continuation

All 15 new theorem declarations and two definitions have a complete axiom
audit. Fresh strict compilation was performed by the author, a separate
reviewer, and the integration runner; the axiom union is only `propext`,
`Classical.choice`, and `Quot.sound`. The two inherited Lean dependencies
are copied unchanged and pinned by hash. The written cycle and boundary
results have separate reconstructions, with qualifications retained.

The [report](../../../../reports/2026-11-23-source-construction/README.md)
records exact controls, commands, reviews, and evidence scope.
[SOURCES.json](SOURCES.json) freezes the advancing peer files. No historical
Lean corpus or old census is required by the scoped runner.

The next constructive obligation is the displayed complete-carry
divisibility **at the candidate's own horizon**, for one fixed ordinary
source. The other routes retain equally explicit original-law or
full-denominator consumers. This checkpoint proves candidate exactness;
it supplies no universal existence theorem, escape exclusion, or complete
integer-cycle exclusion.
