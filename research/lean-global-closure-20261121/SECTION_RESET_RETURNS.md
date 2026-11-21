# A cofinal reset at the first dyadic-section return

## Status

**Proved in Lean; not a proof or disproof of Collatz.** This result builds on the actual forward-section theorem of PR #173, frozen at `fa0c9e2a2851e6324391e39c17afcb5913185aec`. It concerns ordinary positive integers and the first strictly positive return on their actual shortcut trajectories.

The motivating full-proof attempt was to turn the new forced band visit into a well-founded return rank. Ordinary size alone fails by the source's increasing-return family. A natural repair is to charge a long run of trailing binary ones: during an odd shortcut step, `v₂(n+1)` falls by one. The result here shows that this proposed resource can be reset upward before the next marked return, while ordinary size also increases arbitrarily.

## Exact result

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2.\end{cases}
\]

For odd `n`, put `d=floor(log₂ n)` and mark it when

\[
(d+1)(n-2^d)\le70\,2^d.
\]

Write `R(n)` for the first marked point at a **strictly positive** shortcut clock, as defined and proved total in the frozen source. Write `κ(n)=v₂(n+1)`.

`cofinal_expanding_reset` proves

\[
\boxed{\forall C,L\in\mathbb N\;\exists n>L:\quad
n>1,\quad n\text{ is marked},\quad\kappa(n)=1,
\quad R(n)>Cn,\quad\kappa(R(n))>C.}
\]

Thus a finite initial exception range cannot remove the phenomenon. The conclusion concerns the first return itself, not a selected later return or a changing family of incompatible prefixes.

The second theorem, `no_eventual_coordinate_rank`, permits any preorder `A` and any coordinatewise monotone function

\[
F:\mathbb N\times\mathbb N\to A.
\]

There is no cutoff `L` above which every marked `n>1` satisfies

\[
F(R(n),\kappa(R(n)))<F(n,\kappa(n)).
\]

The function need not be linear, real-valued, or computable. This covers monotone functions of binary length and trailing-one depth as well, by composition with `floor(log₂ n)`.

## Construction and ordinary trajectory

Given the desired factor `C` and cutoff `L`, take

\[
H=4C+4,\qquad h=2H+2L+10,\qquad d=2^h,
\]

and define

\[
B=d-h-2,\qquad u=3d+23,\qquad
n=\frac{2^{B+2}u-5}{3}.
\]

Here `h`, `d`, and `B` are even. Therefore the displayed numerator is divisible by three; the natural-number division in the Lean definition is exact. The key identities are

\[
3n+5=2^{B+2}u,
\qquad
n=2^d+\frac{23\,2^{d-h}-5}{3},
\qquad n\equiv1\pmod4.
\]

The source is marked, lies above `L`, and has `κ(n)=1`. Its first two actual shortcut steps are

\[
T(n)=2(2^Bu-1),\qquad T^2(n)=2^Bu-1.
\]

The first state is even and hence is not marked. The second state starts a long rising odd run. For `1≤j≤B+1`, put

\[
x_j=T^{j+1}(n)
   =3^{j-1}2^{B-j+1}u-1.
\]

For `j≤B`, this state is odd, and its trailing-one depth is `B-j+1`. The Lean proof needs only the directly proved divisibility lower bound

\[
2^{B-j+1}\mid x_j+1.
\]

The division-by-four entry into this run is essential: it permits the initial marked source to have depth one, while later marked points in the run still have enormous trailing-one depth.

## Why the first marked return is late but remains inside that run

Let `α=log₂ 3`. For the displayed prefix,

\[
\log_2 x_j=d-1+j(\alpha-1)+e_j,
\qquad \frac2d\le e_j\le\frac{16}d.
\]

To verify the indexing, `j=1` is `T²(n)`, whose leading size is approximately `(3/4)2^d`; its leading logarithm is `d+α−2`, exactly the expression above at `j=1`.

The proof obtains the error interval by writing

\[
F_j=2^{d-1}(3/2)^j,
\qquad
\frac{x_j}{F_j}=1+\frac{23}{3d}-\frac1{F_j}
\in[1+7/d,1+8/d].
\]

The same rational-grid argument used in the frozen source provides a positive `q≤d/2` for which `x_q` is marked. Since `h+2<d/2`, this witness occurs within the rising prefix.

Conversely, if an `x_j` in this prefix is marked, then for a natural integer `a`

\[
|j\alpha-a|\le156/d.
\]

The frozen source's elementary separation theorem for `3^j` and `2^a`, together with

\[
156(4^H+1)\le d,
\]

forces `j>H`. This is an exact integer-power argument, not an equidistribution assumption.

Let the first positive return clock be `r`. Its totality and the marked witness give `r≤q+1`; the first state is even, so `r≥2`. Therefore `j=r−1` is an actual marked state of the displayed prefix and satisfies

\[
H<j\le d/2.
\]

A direct induction along the rising run gives

\[
(j+1)n\le4x_j.
\]

Since `H=4C+4`, this yields `R(n)>Cn`. Meanwhile

\[
\kappa(R(n))\ge d-h-j-1
\ge d/2-h-1>C.
\]

Every statement refers to the same constructed ordinary source `n` and its first actual positive return.

## What was attempted toward full convergence

The section proof controls the leading phase, but the integer amount removed at each accelerated odd step disappears modulo one. Its phase recurrence is

\[
\log_2 U(x)=\log_2 x+\log_2 3-v_2(3x+1)
 +\log_2(1+1/(3x)).
\]

A rational grid produces phase precision of order `1/q`. The integer reached after `q` odd steps can have binary length proportional to `q`, so simply improving the irrationality bound for `log₂ 3` does not convert this into unit-scale proximity to a power of two. To identify a one-odd-step predecessor of a power of two, that approach would need phase precision of order `1/x`, or an additional exact congruence mechanism.

The attempted resource repair charged the trailing-one depth, which correctly decreases during an already active rising run. The construction above pinpoints the missing transition: one legitimate division-by-four step can reset that depth from one to a large value. The ensuing first marked return increases both recorded coordinates. A complete proof needs an additional mechanism that handles these resets, a rank with different monotonicity, or eventual descent across a variable number of returns. The universal eventual-descent assertion remains open.

## Provenance and checks

The imported modules `ShellCover.lean`, `ForwardSection.lean`, and `SectionDynamics.lean` are exact copies from the frozen PR #173 head. The private logarithmic estimates named `buffer` and `marked_height` are reproduced from that head's `RisingReturns.lean`. The source definition, ordinary reset identities, shifted-phase argument, first-return analysis, and rank corollary are in `ResetReturns.lean`.

Lean: `4.34.1`, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`.

Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.

All three imported source modules were compiled locally with warnings treated as errors, followed by the new module. The final receipt records exact source hashes and the actual command. Both exported theorems depend only on `propext`, `Classical.choice`, and `Quot.sound`. No conjectural axiom, `sorry`, unsafe evaluation, or `native_decide` supplies a closing assertion.
