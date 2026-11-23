# Every finite ordinary ancestor set gives a unit-pressure certificate

23 November 2026. **Written all-parameter construction; the required
moving-target mass lower bound remains OPEN.** This closes the source-pool
projection left explicit in CF7-F of the preceding checkpoint. It does not
claim to produce sufficiently many small ancestors of every moving sibling.

The map is the shortcut map `T(n)=n/2` for even `n` and
`T(n)=(3n+1)/2` for odd `n`. Its odd acceleration is `U`. A unit below means
a positive odd integer not divisible by three. All ancestors in this note
are actual positive ordinary ancestors, not congruence-compatible words.

The retained parent is PR177, commit
`3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`.
Dependencies are its [finite trial certificate](../../profound-step-20261123/COMMON_DISPLACEMENT_AND_FREE_ENERGY.md),
CF5--CF9, and [ordinary pressure identities](../../repo-synthesis-20261123/escape/BASIN_PRESSURE_PACKING.md),
BP1--BP3. The pointwise construction and its inverse-power inequality below
do not require an escaping orbit.

## 1. The actual projection and its endpoint

For `n>=1`, write `n=2^a m` with `m` odd. Define

\[
\pi(n)=
\begin{cases}
m,&3\nmid m,\\
U(m),&3\mid m.
\end{cases} \tag{FP1}
\]

This is a terminating, explicit integer computation. If `3|m`, then
`3m+1=2^e u` has odd `u` with `3` not dividing `u`; thus FP1 always
returns a unit. The shortcut clock to the projection is `a` in the first
case and `a+e` in the second.

**FP2. Same endpoint.** If `v` is a unit and `T^k n=v`, then
`pi(n)` is an actual ancestor of `v`.

Indeed all states before reaching `m` are even, so they cannot equal the
odd target `v`. If `3|m`, that state also cannot be `v`; the intermediate
states after its first odd step and before `U(m)` are even. The actual
hitting path therefore contains the complete projection prefix. Removing
that prefix leaves the required actual suffix to the same `v`.

The height increase is uniformly bounded:

\[
\boxed{3\pi(n)\le5n.} \tag{FP3}
\]

For a unit odd part this follows from `m<=n`. Otherwise `m>=3` and
`2u<=3m+1`, hence `3u<=5m<=5n`. The constant `5/3` is attained by
the actual source `n=3`, whose projection is `5`.

## 2. Every fiber is explicit, including all collisions

For a unit `u`, there is exactly one `e_0(u)` in `{1,...,6}` such that

\[
2^{e_0(u)}u\equiv1\pmod9.
\]

The six values, indexed by `u mod9 = 1,2,4,5,7,8`, are respectively
`6,5,4,1,2,3`. This is the order-six cycle of powers of two modulo nine.
Put

\[
m_b(u)=\frac{2^{e_0(u)+6b}u-1}{3},\qquad b\ge0.
\]

These are exactly the positive odd multiples of three with odd successor
`u`. They satisfy

\[
m_b=64^b m_0+\frac{64^b-1}{3}\ge64^b m_0,
\qquad m_0\ge\frac35u. \tag{FP4}
\]

The complete disjoint fiber is

\[
\boxed{
\pi^{-1}\{u\}
=\{2^a u:a\ge0\}
\ \sqcup\ \{2^a m_b(u):a,b\ge0\}.
} \tag{FP5}
\]

Uniqueness of the odd part separates the two families and identifies `a`.
In the second family the exact valuation identifies `e_0+6b`, hence `b`.
There is no uncounted source multiplicity in FP5.

For every real `s>0`, its full inverse-power sum therefore obeys

\[
\sum_{\pi(n)=u}n^{-s}
\le C_s u^{-s},\qquad
\boxed{
C_s=\frac{1+(5/3)^s/(1-64^{-s})}{1-2^{-s}}.
} \tag{FP6}
\]

This follows from FP4 and the two convergent geometric series in `a` and
`b`. No source cutoff is needed for the bound. In particular `C_2<6`.

For a finite set `G` of full positive shortcut ancestors of one unit
target `v`, compute `H=pi(G)` and remove duplicate images. Group the finite
sum by its actual fibers and apply FP6:

\[
\boxed{
\sum_{u\in H}u^{-s}\ge C_s^{-1}\sum_{n\in G}n^{-s}.
} \tag{FP7}
\]

FP2 supplies a literal ancestor witness for every member of `H`.
Multiplicity is paid by a fixed weighted constant, not by a logarithmic
counting loss. Counts alone do not have this property: the distinct
ancestors `u,2u,...,2^a u` all project to the one unit `u`.

## 3. A finite certificate from unrestricted ordinary predecessor data

Return to one unchanged hypothetical escaping component, fix the same
unit sibling `v=Sq=64q+21`, and retain the complete balanced bijection
`Phi:D(q)->D(v)`. Given any nonempty finite full shortcut ancestor set
`G` of `v` with its actual paths, construct

\[
H=\pi(G),\qquad F=\Phi^{-1}(H).
\]

Both `H` and `F` are nonempty, so their positive inverse-power masses
define the normalized trial and the logarithms below. This is an actual
finite source set for the preceding CF7-F certificate.
The inverse address bijection computes every member of `F` from the
supplied path of its member of `H`. With `c_*=exp(-160/3)` and `s>1`,

\[
\boxed{
\mathcal F_q(\sigma_F)
\le\log\frac{s}{s-1}-s\log(64c_*)
 +\log C_s-\log\sum_{n\in G}n^{-s},
} \tag{FP8}
\]

where `sigma_F(n)=Phi(n)^(-s)/sum_(F)Phi(n)^(-s)` is the same explicit
finite trial as CF7-F. Neither `r`, `Z_s`, nor an infinite probability
normalizer has to be evaluated in the certificate.

If `G` has `N>=1` distinct sources at most `X` (hence `X>=1`), this gives

\[
\boxed{
\mathcal F_q(\sigma_F)
\le\log\frac{s}{s-1}-s\log(64c_*)+\log C_s+s\log X-\log N.
} \tag{FP9}
\]

Thus an ordinary predecessor-population theorem can now enter the
certificate without a hidden odd/unit projection. To exclude escape
using the preceding root-summability theorem, one still needs actual
finite sets `G_j` with

\[
N_j/X_j^s\ge c/g(j)^s,
\qquad \sum_j1/g(j)=\infty.
\tag{FP10}
\]

No such moving-target construction is supplied here. For example, a
relative-scale count `N_v(X)>=c(X/v)^gamma`, valid only for `X>=Bv` with
`0<gamma<s`, gives its best bound of this form at `X=Bv`, of order
`v^(-s)`. Sending `X` farther out worsens `X^(gamma-s)`. The projection
now works, but that count by itself still does not reach FP10. This is
an algebraic assessment of the displayed count, not an assertion that a
specific external theorem has uniform constants of that form.

## 4. Exact pressure projection on the full ordinary component

Extend the escaping-component weight to all positive ordinary integers
in the same eventual-meeting component by

\[
r(2^a m)=2^{-a}r(m)
\]

for odd `m`; for a multiple of three with `Um=u`, use the exact odd-edge
identity `r(m)=(3/2^e)r(u)`. This agrees with the product definition on
odd sources. FP5 gives the exact fiber mass

\[
\boxed{
\sum_{\pi(n)=u}r(n)^s
=J_s(u)r(u)^s,
\quad
J_s(u)=\frac{1+D_s(u)}{1-2^{-s}},
\quad
D_s(u)=\frac{(3/2^{e_0(u)})^s}{1-64^{-s}}.
} \tag{FP11}
\]

The multiplier `J_s(u)` depends only on the actual residue `u mod9`.
In particular it lies between the explicit positive constants

\[
J_s^-=
\frac{1+(3/64)^s/(1-64^{-s})}{1-2^{-s}},\qquad
J_s^+=
\frac{1+(3/2)^s/(1-64^{-s})}{1-2^{-s}}.
\tag{FP12}
\]

Every member of a fiber of a unit ancestor `u` is itself an ancestor of
`v`. FP2 proves the reverse implication. Thus, writing `A_s^T(v)` for
the full shortcut basin mass and `A_s(v)` for the unit-odd basin mass,

\[
A_s^T(v)=\sum_{u\in D(v)}J_s(u)r(u)^s,
\qquad
J_s^-A_s(v)\le A_s^T(v)\le J_s^+A_s(v). \tag{FP13}
\]

At a nonperiodic root, the corresponding complete shortcut Green sum
uses edge weights `1/2` at an even source and `3/2` at an odd source,
each raised to `s`. Unique hitting depths give
`A_s^T(v)=r(v)^s Z_s^T(v)`. Consequently the full-source and unit-source
sibling ratios are comparable:

\[
\boxed{
\frac{J_s^-}{J_s^+}\frac{Z_s(Sq)}{Z_s(q)}
\le\frac{Z_s^T(Sq)}{Z_s^T(q)}
\le\frac{J_s^+}{J_s^-}\frac{Z_s(Sq)}{Z_s(q)}.
} \tag{FP14}
\]

Adding even sources and initial multiples of three therefore preserves
the absolute lower-comparison question up to explicit constants. It
does supply more convenient finite ordinary certificates through FP8;
it does not by itself manufacture the missing mass.

## 5. Formal and computational boundary

`UnitProjection.lean` proves the finite ordinary path projection,
the sharp `3u<=5n` height bound, and the finite fiber aggregation consumer.
The complete countable fiber sums, real powers, and pressure comparison
FP6 and FP11--FP14 are written proofs. They are not claimed as additional
Lean declarations.

The exact checker constructs finite full shortcut predecessor pools,
computes the actual projection clocks and suffix paths, deduplicates the
unit images, and checks rational inverse-square mass. Separate complete
finite fiber rectangles check every source form and reject omitted
dyadic multiplicity, lost odd multiples of three, and an incorrect claim
that projection never increases height. The examples include convergent
roots; no simulated escaping component is asserted.

The direct construction FP1--FP8 is new here. The full Collatz conjecture,
the residue-512 implication, and the finite mass lower bound FP10 remain
open.
