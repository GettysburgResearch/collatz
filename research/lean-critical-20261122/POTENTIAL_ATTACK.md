# A compact ordinary Green map, and the norm it cannot preserve

**Status: SOURCE-QUALIFIED written deductions, with the explicit ordinary
obstruction checked in Lean. No full Collatz closure is claimed.**

This attack starts from the latest global canonical-potential bounds and
ordinary harmonic flow, rather than reconstructing the earlier local
potential criteria. It obtains a quantitative compactness theorem for the
**full actual Green map**, a stable finite-source approximation to the
canonical immigration correction, and two precise restrictions on using
those estimates in a critical operator argument.

The restrictions are witnessed entirely inside a certified convergent
basin. They do not assume a divergent orbit or a nontrivial cycle.

## 1. Exact source inputs and map

The pinned sources are:

| Source | Full head | Statement used |
|---|---|---|
| PR175 | `2bc2ad37b490a5aea63658eaf657bc048da4532e` | `research/lean-global-closure-20261121/CANONICAL_POTENTIAL_SUPERLEVELS.md`, equations (M), (O), and Sections 4--5: a uniform actual-path count with exponent `39/40`, including nonperiodic preperiods, and the global canonical first-moment bound. |
| PR185 | `276be8154f4e867acc0230466b34d9cb224aacf5` | `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`, equations (7)--(15), (33)--(36): the ordinary harmonic correction, its finite immigration, and the exact energy retained by a hypothetical escaping atom. |
| PR180 baseline | `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | `research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md`: canonical normalization, ordinary-point comparisons, and the distinction between a finite-resolution estimate and the critical ordinary upper bound. |
| PR186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | `literature/deep-machinery-20261122/04_returns_operators_and_termination.md`: motivation to specify the operator, state space, retained mass, and missing tail before importing renewal or spectral machinery. This guide is not an additional theorem hypothesis. |

The analytic dependencies of the potential and population statements remain
source-qualified. The actual-path count used in Section 2 is the elementary
cylinder estimate in the pinned PR175 packet. Neither it nor the new Green
argument assumes convergence of every positive source.

Use

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd integers. Let `N` be the positive odd ternary units that
are **not themselves periodic** under `U`. A member of `N` may later enter
a cycle. Forward transport is killed on first exit from `N`; consequently
all states of a retained path are distinct. This is a mathematical domain
separation, not an algorithm for detecting a nontrivial cycle.

For an absolutely summable original source mass `a`, define

\[
(La)(q)=\sum_{\substack{n\in N\\U(n)=q}}a(n),
\qquad
(Sa)(q)=\sum_{j\ge0}(L^ja)(q),\qquad q\in N.
\tag{P1}
\]

The original atom is unchanged at every retained time. Endpoint collisions
are summed. For `a>=0`, nonnegative summation gives the exact identity

\[
(Sa)(q)=\sum_{n\in\operatorname{Pred}(q)}a(n)
\le\|a\|_1.
\tag{P2}
\]

A fixed source can hit a nonperiodic target at most once, which is why
the time sum in (P1) becomes the single predecessor sum in (P2).
For signed or complex masses, absolute convergence follows by domination
with `S|a|`. The same construction therefore defines a linear map.

## 2. A uniform all-time occupation estimate

Put

\[
\theta=\frac{39}{40},\qquad C_s=\frac{5s}{s-\theta}
\quad(s>\theta).
\]

The pinned actual-path count says that, for every source and every finite
subset of its retained path,

\[
\#\{q\text{ in that subset}:q\le X\}\le5X^\theta,
\qquad X\ge1.
\tag{P3}
\]

Taking increasing finite subsets gives the same bound for the entire
retained path. In particular, all the following bounds are uniform in
the starting source and in its duration before killing.

### Theorem P1: a tail estimate retaining the whole path

For every retained ordinary path `q_j` and every `X>=1`,

\[
\boxed{
\sum_{j:q_j>X}q_j^{-s}\le C_sX^{\theta-s}.}
\tag{P4}
\]

Also `sum_j q_j^(-s)<=C_s`.

**Proof.** Write `N(t)` for the number of retained path states at most
`t`. Use the nonnegative integral identity

\[
q^{-s}=s\int_q^\infty t^{-s-1}\,dt.
\]

Summing first over a finite path subset, then increasing that subset, gives

\[
\begin{aligned}
\sum_{j:q_j>X}q_j^{-s}
&=s\int_X^\infty\#\{j:X<q_j\le t\}\,t^{-s-1}\,dt\\
&\le5s\int_X^\infty t^{\theta-s-1}\,dt
=C_sX^{\theta-s}.
\end{aligned}
\]

For the full sum, integrate from 1. The state 1 is periodic and absent
from `N`, so no omitted endpoint term arises. QED.

## 3. Quantitative compactness of the actual Green map

Define the weighted sequence norm

\[
\|b\|_{1,s}=\sum_{q\in N}\frac{|b(q)|}{q^s},
\qquad \ell^1_s=\{b:\|b\|_{1,s}<\infty\}.
\tag{P5}
\]

Let `Q_X` retain only output states at most `X`.

### Theorem P2: full Green transport with an explicit output tail

For every `a` in ordinary, unweighted `ell^1(N)`,

\[
\boxed{\|Sa\|_{1,s}\le C_s\|a\|_1,}
\tag{P6}
\]

\[
\boxed{
\|(I-Q_X)Sa\|_{1,s}\le
C_sX^{\theta-s}\|a\|_1.}
\tag{P7}
\]

Consequently

\[
\boxed{S:\ell^1(N)\longrightarrow\ell^1_s(N)
\text{ is compact for every }s>39/40.}
\tag{P8}
\]

**Proof.** For positive `a`, interchange the two nonnegative sums in
`sum_q q^(-s) sum_j L^j a(q)`. The contribution from an original source
`n` is its unchanged mass `a(n)` times the reciprocal-power occupation
sum of its actual retained path. Apply (P4). General `a` follows from
`|Sa|<=S|a|`.

The same argument restricted to `q>X` proves (P7). Thus

\[
\|S-Q_XS\|_{\ell^1\to\ell^1_s}
\le C_sX^{\theta-s}\longrightarrow0.
\]

Each `Q_XS` has finite-dimensional range. Its image of the unit ball is
bounded in that finite-dimensional space. Approximating that image by
finitely many small balls and then using the displayed uniform tail
proves total boundedness of the image under `S`. The target is complete:
`b(q) -> q^(-s)b(q)` is an isometry onto ordinary `ell^1`. This proves
compactness directly. QED.

At the harmonic spatial weight the constants become

\[
\boxed{
\|Sa\|_{1,1}\le200\|a\|_1,
\qquad
\|(I-Q_X)Sa\|_{1,1}\le200X^{-1/40}\|a\|_1.}
\tag{P9}
\]

This is an all-time estimate for original ordinary source atoms. It does
not require a new independent source sample after a return.

## 4. Stable finite-source approximation of the harmonic correction

Use PR185's notation

\[
h(q)=G(q)/q,\qquad
d(q)=\frac{h(q)}{3q+1},\qquad
D=\sum_{q\in N}d(q)\le\frac{200}{3c},
\]

where `c>0` is the pinned uniform unit-predecessor constant. Its corrected
ordinary harmonic flow satisfies

\[
\nu=h+SLd,\qquad L\nu=\nu.
\tag{P10}
\]

Here `L` is a contraction on unweighted source `ell^1`: each source has
one forward image or is killed. The correction is therefore an exact
application of the Green map above to a finite source mass.

### Corollary P3: quantitative stability under immigration truncation

Let `s>theta` and `X,Y>=1`, and put `d_Y=d 1_[1,Y]`. Then

\[
\boxed{
\|\nu-h-SLd_Y\|_{1,s}
\le C_s\sum_{n>Y}d(n)
\le C_s\frac{200}{3c}Y^{-1/40}.}
\tag{P11}
\]

Moreover

\[
\boxed{
\|\nu-h-Q_XSLd_Y\|_{1,s}
\le C_sD X^{\theta-s}
+C_s\frac{200}{3c}Y^{-1/40}.}
\tag{P12}
\]

**Proof.** The global canonical count in PR175, and `h<=V/q`, give

\[
\sum_{n\le t}h(n)\le\frac5c t^\theta.
\]

The same nonnegative integral argument as in (P4), applied to this
weighted count with exponent 1, gives

\[
\sum_{n>Y}d(n)
\le\frac13\sum_{n>Y}\frac{h(n)}n
\le\frac{200}{3c}Y^{-1/40}.
\]

Apply (P6) to `L(d-d_Y)` for (P11). For (P12), split the error into
the output tail `(I-Q_X)SLd` and the retained outputs of `SL(d-d_Y)`.
Use (P7) and (P11). All quantities are nonnegative, so no conditionally
convergent rearrangement occurs. QED.

Thus the immigration correction admits a global quantitative
approximation using a finite source set and a finite output set. The
matrix entries still involve **actual all-time hitting**. This is not
an effective clock cutoff or a decision procedure for those entries.
The uncorrected critical term `h` has not disappeared.

## 5. An explicit convergent ladder tests the operator domain

Define

\[
n_j=\frac{40\,64^j-1}{3},\qquad e_j=6j+3.
\tag{P13}
\]

Equivalently `n_0=13`, `n_(j+1)=64 n_j+21`. Every `n_j` is a positive
odd ternary unit, `n_j>=j+13`, and

\[
3n_j+1=5\,2^{e_j},\qquad
\boxed{U(n_j)=5,\qquad U^2(n_j)=1.}
\tag{P14}
\]

All `n_j` and 5 are nonperiodic. Their orbits are explicitly known, so
this family lies in the retained domain until it reaches 1 and is killed.
For finite source point masses,

\[
\boxed{L\delta_{n_j}=\delta_5.}
\tag{P15}
\]

The new `lean/PotentialCritical.lean` checks the recursive ladder,
its exact power identity, positivity/oddness/unit conditions, cofinality,
one-step image, two-step convergence, nonperiodicity, and the exact
finite-support pushforward. The following norm obstruction is also
checked there as a vanishing-input/fixed-output graph witness and a
failure of every uniform boundedness inequality.

The finite-support Lean pushforward is defined on `Nat`. For the ladder
atoms, both the source and its first image lie in `N`, so that formal
pushforward agrees exactly with the killed operator in (P1).

### Theorem P4: the forward operator is not closable in the compactness norm

For every `s>0`, the operator `L`, initially defined on finite-support
functions in `ell^1_s(N)`, is **not closable** as an operator from
`ell^1_s(N)` to itself.

**Proof.** The inputs `a_j=delta_(n_j)` satisfy

\[
\|a_j\|_{1,s}=n_j^{-s}\longrightarrow0,
\]

while `La_j=delta_5` for every `j`. The latter sequence converges to a
nonzero vector of norm `5^(-s)`. The graph closure therefore contains
`(0,delta_5)`. It cannot be the graph of a linear operator, since such
an operator sends zero to zero. QED.

The same proof works for any positive spatial weight `w` for which
`w(n_j)->0`, in the norm `sum_n w(n)|a(n)|`. In particular, it works
for every positive summable weight on `N`. Its failure is already
visible on single source atoms, without an infinite input sum.

**This norm is not the finite-reference collision norm.** The latter
is `sum a(n)^2/lambda(n)` and has the reference in the denominator.
The theorem above concerns spatially weighted mass norms with the weight
in the numerator. It does not refute PR185's collision contraction or
claim that every finite-reference operator is unbounded. It rules out
using (P8) as if it were a compact resolvent of a closed forward operator
on that same spatially weighted sequence space.

## 6. Compact output approximation does not give a uniform source or clock cutoff

The distinctions can be quantified on the same convergent ladder.

### Source height cutoff

Let `P_Y` truncate the **input** to sources at most `Y`. Choose `j`
with `n_j>Y`. Then `P_Y delta_(n_j)=0`, but
`S delta_(n_j)(5)=1`. Consequently

\[
\boxed{
\|S-SP_Y\|_{\ell^1\to\ell^1_s}\ge5^{-s}
\quad\text{for every finite }Y.}
\tag{P16}
\]

This does not contradict (P11): that result controls the discarded mass
of **one specified finite source measure**. Formula (P16) takes the
supremum over all unit source masses and is a different quantifier.

### Literal ordinary-clock cutoff

Let `S^[K]` count retained odd target visits occurring within `K` steps
of the ordinary shortcut map `T`. Its full-time limit is `S`, because
the odd subsequence of a shortcut orbit is exactly the `U` orbit.
The killing rule is applied to that odd subsequence on entry into a
periodic odd orbit; intervening even shortcut states are skipped.

For the ladder (P13),

\[
T^t(n_j)=5\,2^{e_j-t}\qquad(1\le t\le e_j).
\]

Thus the **first** ordinary hit of 5 occurs at time `e_j=6j+3`.
For `e_j>K`, `S^[K] delta_(n_j)(5)=0`, while the full Green value is
one. Hence

\[
\boxed{
\|S-S^{[K]}\|_{\ell^1\to\ell^1_s}\ge5^{-s}
\quad\text{for every finite ordinary-clock cutoff }K.}
\tag{P17}
\]

The claim in (P17) is about the literal shortcut clock. All ladder
sources hit 5 after one **odd** step, so this family is not offered as
an odd-depth delay example.

For every fixed `a` in `ell^1`, both source truncations and increasing
ordinary-clock truncations do converge after applying `S` in the weighted
output norm. For input truncation this follows from (P6) and the `ell^1`
tail of `a`; for clock truncation it follows by dominated convergence
under the integrable majorant `S|a|`. Statements (P16)--(P17) show that
this strong convergence is not convergence in operator norm.

## 7. What this says about the missing critical estimate

The positive result is an explicit infinite-tail bound for actual
ordinary Green transport, including quantitative stability of the
canonical immigration correction. It provides a legitimate setting for
finite-output approximations while preserving source atoms and every
collision.

Three tempting upgrades fail at precisely stated points:

1. The compact Green map has **different input and output norms**.
   The forward counting operator is not closable on its weighted output
   space, by (P13)--(P15). A compact-resolvent or analytic-Fredholm
   argument on one space cannot start from (P8).
2. Output truncation has the uniform error (P7); input truncation and
   ordinary-clock truncation have the nonvanishing operator-norm lower
   bounds (P16)--(P17). A finite matrix has not captured its missing
   incoming histories merely because its output set is finite.
3. Weighted compactness permits escape to lose norm. If an original atom
   follows an injective orbit `q_k`, then `q_k->infinity` and
   `||delta_(q_k)||_(1,s)->0`, although its original mass is still one.
   Thus compactness or decay in this norm does not prove killing.

The latest harmonic-flow packet has the complementary feature: its
collision norm retains a strictly positive energy from each hypothetical
escaping atom. That reference is infinite. Passing to its finite
reference costs a height factor, which (P6)--(P12) do not pay.

The remaining potential target is still a critical ordinary upper bound
at moving marked sources, or a genuine finite-reference bound that
retains their mass. This packet supplies no such bound, excludes no
nontrivial cycle, and does not replace the missing statement by an axiom.

## 8. Formal evidence

`lean/PotentialCritical.lean` has 13 public theorem audits. The isolated
replay uses Lean 4.34.1, `-j1 -DwarningAsError=true`, and the pinned
baseline dependency `MarkedDensityPotential`. Its successful compiler
log contains only `propext`, `Classical.choice`, and `Quot.sound` in the
printed axiom dependencies.

The compactness theorem, infinite-source Green estimates, immigration
tail estimates, and operator-norm cutoff conclusions are written proofs.
The Lean module checks their explicit ordinary arithmetic counterexample
and the corresponding finite-support weighted inequalities; it does not
claim to formalize Banach-space compactness or closability itself.
