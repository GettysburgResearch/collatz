# Lean global attack: a common rank and the uncovered ordinary family

**Full Collatz convergence remains OPEN.** This pass develops an actual
Lean 4.34.1 project with no Mathlib dependency, a common well-founded rank
for guarded certificate transformations, and a kernel-checked infinite
family on which the present move catalog has no applicable step. No open
Collatz statement is introduced as an axiom or filled with `sorry`.

The subsequent [repository-wide reframe](../reframe-20261121/README.md)
compares the complete-word and marked-section work with the ordinary mass
and spectral routes, and adds a checked fixed-block canonical-pump theorem.

All clocks use the positive shortcut map `T(n)=n/2` for even `n` and
`T(n)=(3n+1)/2` for odd `n`. Every input and orbit here is an ordinary
natural integer.

The main positive result is **termination of every sequence passing the
proved common-rank guards**. The missing result is **a successful rule or
a complete target certificate for every eligible ordinary input**. These
are separate statements; the second is not inferred from the first.

## 1. A proved common rank, including source-clock growth

For a convergent ordinary source `n` with its exact supplied hit clock `d`,
put

\[
\boxed{P(n,d)=(n+1)(201/200)^d.}
\]

[`CommonRank.lean`](lean/CollatzGlobal/CommonRank.lean) proves the strict
order well-founded on **all** natural source/clock pairs. The proof is
entirely in core Lean using integer cross multiplication. It does not
assume that decreasing positive rationals are well ordered. Bernoulli's
inequality bounds a score sublevel by `n+1<=B`, `d<=200B`; a fixed common
denominator then gives strict natural-number descent.

[`RankMoves.lean`](lean/CollatzGlobal/RankMoves.lean) proves the exact
admission guards. A forward move consuming `t` clocks is accepted if

\[
(q+1)200^t<(n+1)201^t.
\]

It can increase ordinary size. The new
[`PsiExpansion.lean`](lean/CollatzGlobal/PsiExpansion.lean) proves the
whole same-goal affine family

\[
m_h=106495+2^{52}h,\qquad r_h=131455+3^{33}h,
\]

\[
T^{52}(m_h)=r_h>m_h,\qquad
T^{52}(3m_h-1)=3r_h-1,\qquad
r_h200^{52}<m_h201^{52}.
\]

These identities and the strict guard hold for **every** natural `h`.
Thus the actual known source grows while its certificate clock decreases
by 52, and the common rank strictly decreases. The ternary-unit restriction
on the input is exactly `h mod3 != 2`. General source convergence is a
supplied hypothesis, not a consequence of lifting the seed: for `h=0`,
Lean separately checks the complete source certificate
`T^196(319484)=1`, which becomes `T^144(394364)=1`.

The separate five-return example `19483 -> 21091` in thirty clocks also
passes, with its supplied source clock shrinking from 127 to 97.

A height contraction may instead add `a` clocks. The exact sufficient
conditions are

\[
3^b(n'+1)\le2^a(n+1),\qquad402^a<200^a3^b.
\]

All eight frozen negative-reference templates pass the relevant coefficient
and source-coordinate tests. Their old ordinary-legality and witness
transformations remain precisely named **paper-level dependencies**; this
pass does not claim to have formalized every old template proof. The new
rank arithmetic, fixed-prefix conjugation, and generic clock transport
are kernel checked. The accompanying independent affine checker verifies
that these eight guarded rows need no terminal padding, so their actual
source clock changes by exactly `+a`.

The [common-rank note](COMMON_RANK.md) gives all constants, guards,
dependencies, and the no-padding proof. The [independent rank review](COMMON_RANK_REVIEW.md)
checks the finite-sublevel argument. A smaller ordinary source is not
automatically smaller in this rank; old least-ordinary-counterexample
floor queries must still be justified separately.

## 2. Same-goal witness transport

A binary reverse template originally acts on
`Basin(128M+1) -> Basin(64M+1)`. It cannot be silently treated as a five
comparison. The new [formal bridge](lean/CollatzGlobal/PsiTemplateBridge.lean)
uses the exact ordinary identities

\[
T^7(128M+1)=81M+2=3(27M+1)-1,
\qquad T^6(64M+1)=27M+1.
\]

They conjugate the templates into the **same psi goal type**
`Basin(3m-1) -> Basin(m)`, with `m=27M+1`. The fixed source overhead
cancels, preserving the precise clock increment `+a`. In that chart the
rank is charged to the known source `3m-1`, and its offset guard is
`27c+3^b<2^a`.

Guarded psi returns and these conjugated rules can therefore share one
termination argument. Every bridge must still supply its actual source
certificate, its target implication in the correct direction, and its
rank guard. The expanding psi family above and the translated negative
templates act on that same psi obligation, so this combination needs no
conversion between five and psi goals.

## 3. Total finite normalization and the full global interface

The [five normalizer](lean/CollatzGlobal/AdaptiveDescent.lean) and
[psi normalizer](lean/CollatzGlobal/PsiNormalization.lean) scan **any
supplied finite source hit certificate** and select the last return in
that window. They prove the remaining source certificate, exact target
certificate transport, and a finite no-return residual. No first-hit
minimality or all-time membership oracle is needed.

Lean proves

\[
\mathrm{Collatz}\quad\Longleftrightarrow\quad
\mathrm{ResidualPsiClosure}.
\]

The right side says that every positive ternary unit `m`, with a supplied
certificate `T^d(3m-1)=1` and no positive psi return through clock `d`,
has `Basin m`. **The development does not prove that right-hand statement.**
The global reverse implication uses the credited PR146/PR174 core theorem.

These total finite normalizers and the common-rank guards are separate
tools. Unrestricted last-return normalization is not asserted to decrease
`P`; a ranked compiler must check the complete move it actually uses.

The [closure note](CLOSURE_ROUTE.md) also records a positive first-layer
result: Jacobsthal source goals close under a genuine least-ordinary-failure
floor. That floor is not automatically available from minimum score.

## 4. A whole infinite family still has no available move

[`PsiCoverage.lean`](lean/CollatzGlobal/PsiCoverage.lean) constructs an
integral, cofinal sequence `M_j` with

\[
243M_j+22=8\,2^{119+162j},\qquad j<M_j,\qquad M_j\equiv2\pmod4.
\]

For `e=119+162j`, `m=27M_j+1`, and `d=e+3`, Lean proves

\[
T^d(3m-1)=1,
\qquad\mathrm{FinitePsiResidual}(m,d),
\qquad M_j\not\equiv-1\pmod{2048}.
\]

Thus there is **no psi return anywhere inside the supplied witness**, and
**none of the eight negative-reference template guards holds**. This
checks the coverage question on every member of an infinite ordinary
family, after the same-goal conjugation, rather than on one numerical
fixture. These are not claimed counterexamples to Collatz. They are an
uncovered family for the present move catalog; an additional asymmetric,
failure-sensitive, or directly certifying rule is needed.

The [coverage attempt](COVERAGE_ATTEMPT.md) gives the full ordinary orbit
formulas and the exact remaining inference.

## 5. Global alternatives tested and ruled out at their precise scopes

The [inverse-expansion route](GLOBAL_FORCING.md) was pursued as a complete
selector, not merely as a source of another isolated return. Lean proves
that any actual expanding word with `p` odd steps excludes the endpoint
class `1 mod3^p`. More strongly, there are arbitrarily large certified odd
ternary units with no smaller certified odd ternary-unit ancestor at any
ordinary clock. Hence a complete inverse-only descent on all certified
units cannot work from finitely many bases. A selector restricted to
actual failures or using other kinds of moves is outside that conclusion.

The [mixed-return attempt](MIXED_RETURN_ATTEMPT.md) proves an exact
retraction: every balanced inverse extension of a finite residual
normalizes back to that same source/clock pair. No rank of that pair,
valued in any well-founded relation, can strictly decrease on both
operations. The new guarded rank avoids the loop by rejecting the inverse
of an admitted strict return. Additional history or asymmetric moves are
not ruled out.

## Formal scope, reuse, and actual execution

The ordinary map and reverse-basin foundation are copied with exact
attribution from PR174, which credits PR146. Whole-cylinder high-bit
lifting and PR166's unbounded ladder are formalized here and credited as
existing mathematical inputs. [SOURCES.md](SOURCES.md) separates those
formal imports from recent research statements inspected for the attack.

From the `lean` subdirectory:

```sh
lake build
lake env lean -DwarningAsError=true FinalAudit.lean
```

The audit lists the logical dependencies of every new public theorem.
The [execution and review index](../../reports/2026-11-21-lean-global/README.md)
records the checkpoint identities and actual checks. Kernel checking
establishes the exact formal statements, including the visible hypotheses
of conditional theorems. It does not fill the residual coverage obligation
or confer external acceptance on neighboring informal source claims.
