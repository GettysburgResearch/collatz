# The compact Green function is infinite on a residual null set

**Status: PROPOSED, complete paper proof; not Lean-formalized.** This is a
topological complement to [the fractional-moment theorem](GREEN_FRACTIONAL_MOMENTS.md).
It supplies no divergent positive ordinary orbit and no Collatz closure.

Keep exactly that note's space `X = Z_3^times`, normalized restricted additive
Haar measure, maps

\[
R_a(u)=\frac{3u+1}{2^a}\quad(a\ge1),
\]

and compact Green function `G = sum_(q>=0) P_2^q 1`. At a positive odd
ordinary ternary unit, `G` equals the actual ordinary all-history Green
function and is finite by the fixed-target estimate. By GF1, `G` is also
finite Haar-almost everywhere.

The additional conclusion is

\[
\boxed{\{\zeta\in X:G(\zeta)=\infty\}
\text{ is a dense }G_\delta\text{ of Haar measure zero}.}
\tag{T1}
\]

Thus the finite-Green set is meagre and has full Haar measure. In particular,
every positive odd ordinary unit belongs to that finite-Green set. Topological
genericity, Haar typicality, and assertions at all positive integers are
three different quantifiers in this construction.

## 1. Legal inverse cylinders can be chosen arbitrarily small

For every `zeta in X`, at least one positive exponent `a` has

\[
2^a\zeta\bmod9\in\{4,7\}.
\]

Indeed the powers of two permute the six units modulo nine. The resulting
inverse child `(2^a*zeta-1)/3` is a ternary unit. Repeating this choice gives
a legal inverse prefix `w=(a_1,...,a_r)` of any desired length, with

\[
\zeta\in E_w=R_{a_1}\circ\cdots\circ R_{a_r}(X).
\]

The affine coefficient of `R_w` is `3^r/2^A`, where `A=sum(a_i)`.
Therefore the ternary diameter of `E_w` is at most `3^(-r)`. Given any
neighborhood of `zeta`, choosing `r` large makes the whole cylinder `E_w`
lie inside that neighborhood. This keeps all intermediate inverse values
in the unit space; it is not just a final congruence condition.

## 2. Every such cylinder contains an explosive periodic inverse word

Fix that prefix and append `L` copies of exponent one. Define

\[
S_L=R_w\circ R_1^L.
\]

This is a strict ternary contraction on the complete space `Z_3`, with
affine coefficient `3^(r+L)/2^(A+L)`. Its denominator is a power of two,
so it maps `Z_3` into `Z_3`. Its unique fixed point `zeta_L` is a ternary
unit: every individual `R_a` maps `Z_3` into the units. Moreover,

\[
\zeta_L=R_w(R_1^L(\zeta_L))\in R_w(X)=E_w.
\]

All intermediate values in the fixed word are units. Consequently the word
is a legal periodic inverse history at `zeta_L`, with square-pressure
weight per period

\[
J_L^2=\left(\frac{3^{r+L}}{2^{A+L}}\right)^2.
\]

For sufficiently large `L`, this weight exceeds one, since the extra
factor grows as `(9/4)^L`. Repeating the legal word `k` times contributes
`J_L^(2k)` to `P_2^(k(r+L))1(zeta_L)`. Hence `G(zeta_L)=infinity`.

These witnesses can also be located in the ordinary rational order. The
affine expression for `S_L` is

\[
S_L(u)=\frac{3^{r+L}u+C_L}{2^{A+L}},\qquad C_L>0,
\]

so

\[
\zeta_L=\frac{C_L}{2^{A+L}-3^{r+L}}<0
\]

once `J_L>1`. The denominator is a ternary unit. These are negative
rational points embedded in `Z_3`; no positive ordinary counterexample is
constructed or extracted from them.

Since every neighborhood contains such a cylinder and such a point, the
infinite-Green set is dense.

## 3. Category and measure

Each finite pressure column `P_2^q1` is continuous, as proved from its
uniformly summable clopen word expansion in the fractional-moment note.
The partial Green sums are therefore continuous and increase to `G`.
Thus `G` is lower semicontinuous as an extended nonnegative function.

For every positive integer `M`, the set `{G>M}` is open. It is dense
because it contains the dense infinite-Green witnesses from section 2.
The Baire category theorem, or directly this description of the set, gives

\[
\{G=\infty\}=\bigcap_{M\ge1}\{G>M\}
\]

as a dense `G_delta`. Its complement is a countable union of closed sets
with empty interior. On the other hand, any one of GF1's finite fractional
moments forces the infinite-Green set to have Haar measure zero. This
proves `(T1)`.

In particular, `G` is discontinuous at every finite-valued point: every
neighborhood contains infinite-valued points. This includes **every positive
odd ordinary unit**. This is a discontinuity statement for the canonical
pointwise Green function, not just a limitation of its chosen representative
as a Haar-almost-everywhere class.

## The actual closure boundary

The divergence of this compact Green sum concerns inverse histories at
ternary points. At positive ordinary targets the same sum is finite,
including at unknown positive periodic targets. The theorem neither
rules out such cycles nor produces a nonperiodic positive orbit.

It does show that continuity or topological density cannot transfer the
compact compressed-weight calculation to all positive ordinary targets.
The ordinary sampling assertion `(F11)` in the fractional-moment note
still requires control of the all-depth tails along actual positive
integer samples. No such transfer is asserted here.
