# Four construction attacks: all templates, actual sources, witness charge, and arithmetic germs

23 November 2026. **Full Collatz, the original residue-512 witness
implication, and a universally successful ordinary certificate constructor
remain OPEN.** This packet continues PR177 at
`3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`.

The work targets the missing constructions in the previous checkpoint.
Three parallel lanes examined rational-template selection, finite ordinary
predecessor sets, and complete-witness transformations. A fourth argument
uses the latest peer arithmetic-germ obstruction and a primary multipoint
rationality theorem. The results below are unrestricted where stated;
finite experiments are separately identified.

| Attack | New result | Construction still required |
| --- | --- | --- |
| [All rational templates](descent/TEMPLATE_SELECTION.md) | Every nonintegral actual prefix template has displacement greater than its positive integer source; all nonzero template scores admit a complete finite minimization | An actual universally successful paid macro or ordinary descent |
| [Full ordinary predecessor sets](transport/FULL_SOURCE_FINITE_CERTIFICATE.md) | Every finite full-source set projects to the same unit root with explicit bounded loss in inverse-power mass; exact pressure fibers are computed | Moving ordinary source sets with the absolute lower mass required by the transport argument |
| [Complete-witness charge](witness/WITNESS_CHARGE_AND_POWER_INDUCTION.md) | Complete affine-merger classifications; an infinite four-odd-step family excludes every half-germ and requires an unbounded joint-edit budget | A source-dependent transformation that pays the changing charge and constructs the target witness |
| [Density-free arithmetic germ](germ/DENSITY_FREE_DEFLATED_GERM.md) | A quantitative criterion for reaching one, without a parity-density limit | The full actual arithmetic germ and its required complex and ternary radii |

There are **46 new audited Lean declarations** in four modules. The
external Matveev and Chambert-Loir--Nous theorems enter written arguments;
they are not represented by new Lean axioms. The complete analytic and
number-theoretic arguments are not claimed as kernel-checked theorems.
The [execution and review report](../../../reports/lean-exact-witness-global-20261121/construction-attacks-20261123/README.md)
records the exact boundaries, hashes, commands and independent reviews.

## 1. Nonintegral templates cannot lower the ordinary source height

Use the ordinary shortcut map `T(n)=n/2` for even n and `(3n+1)/2`
for odd n. For any nonempty actual parity prefix at a positive integer x,
write its full affine action as

\[
T^L(x)=\frac{Px+C}{Q},\qquad P=3^p,\quad Q=2^L.
\]

Reduce its rational fixed center to `c/d=C/(Q-P)`, with positive
denominator d. The new all-length theorem is

\[
\boxed{d>1\quad\Longrightarrow\quad |dx-c|>x.}
\]

The ordinary source lattice supplies `Q | dx-c`. A nonintegral reduced
center has odd denominator at least three and cannot have zero displacement
at an integer x. Thus x<Q is immediate. The x>=Q case follows from the
uniform contracting-center bound `c/d<2Q/3`; expanding centers are negative.

The center bound uses the complete carry, not a selected factor of a cycle
denominator. Sorting the zeros before the ones maximizes the carry and gives

\[
C\le Q((3/2)^p-1).
\]

The needed power separation is proved for every p,L>=1:

\[
3^p<2^L\quad\Longrightarrow\quad
2^L-3^p>\frac32((3/2)^p-1).
\]

Matveev's published explicit logarithmic-form bound handles p>=10^12.
Below that threshold, failure would force the reduced fraction L/p to be
a continued-fraction convergent of log_2(3). Exact rational logarithm
enclosures certify every relevant convergent and every multiple of a
reduced convergent. The small exceptional convergent 2/1 is handled by
an exact power-lifting argument. An independent reviewer implemented a
separate finite continued-fraction certificate and checked the original
Matveev statement.

A direct positive corollary is the contracting-prefix descent window

\[
P<Q,\qquad x\ge\frac{2^{L+1}}3
\quad\Longrightarrow\quad T^L(x)<x.
\]

It retains the full carry and makes no average-parity approximation.
The existence of a contracting prefix inside this window is not proved.

### The exact minimum identifies the integral-cycle obligation

Minimize the nonzero scores `|d_u x-c_u|` over every actual nonempty
prefix u. The one-step score is at most x+1, whereas each nonzero score
is at least `2^|u|`. Consequently the entire infinite minimization is
decided by the actual prefixes of lengths

\[
1,\ldots,\lfloor\log_2(x+1)\rfloor.
\]

This is a complete finite evaluator. Its sublevel sets have an explicit
finite height bound. The elementary centers -1,0,1,2 supply

\[
\phi(1)=\phi(2)=2,\qquad
\phi(x)=4\left\lfloor\frac{x+1}{4}\right\rfloor\quad(x\ge3).
\]

The minimum equals phi for every x **if and only if** there is no
nonstandard positive ordinary cycle. A strict improvement supplies a
positive integral cycle center; conversely a nonstandard cycle at c
supplies a strict improvement at `c+2^L`. This equivalence identifies the
remaining cycle statement and does not prove either side. Escape is a
separate obligation.

The same lane proves that every supplied complete ordinary termination
word fits the previously defined paid changing-center macro format,
after padding the exceptional word from two to one. Thus this format
does not discard known complete witnesses; its successful universal
selection is still absent.

## 2. Full ordinary sources can be used without losing the required root

The previous finite-source transport certificate worked on odd integers
prime to three. The new projection accepts every positive ordinary
predecessor of the same root v. Write n=2^a m with m odd, and set

\[
\pi(n)=
\begin{cases}
m,&3\nmid m,\\
U(m),&3\mid m,
\end{cases}
\]

where U is the accelerated odd map. If v is an odd unit and n reaches v,
the actual prefix defining pi(n) occurs before v. Hence pi(n) remains a
unit predecessor of **that same v**. Its height is at most 5n/3.

For each s>0, every complete projection fiber has the explicit bound

\[
\sum_{\pi(n)=u}n^{-s}\le C_su^{-s},\qquad
C_s=\frac{1+(5/3)^s/(1-64^{-s})}{1-2^{-s}}.
\]

In particular C_2<6. Deduplicating any finite source set G into H=pi(G)
therefore gives

\[
\sum_{u\in H}u^{-s}\ge C_s^{-1}\sum_{n\in G}n^{-s}.
\]

The proof enumerates the entire fiber, including all dyadic multiples
and all odd multiples of three. It also computes the exact fiber factor
for the ordinary pressure weight: this factor depends only on u mod9,
and it gives two-sided comparisons of full and unit Green ratios.

Applied to the unchanged sibling root `v=64q+21`, the retained balanced
transport and finite trial certificate now accept arbitrary nonempty
verified ordinary predecessor sets G. If G has N>=1 distinct elements at most X,
its inverse-power mass is at least N/X^s. What is missing is a sequence
of actual finite sets at the required moving roots with a sufficiently
large **absolute** lower bound. A count normalized by the target scale
does not supply that bound.

## 3. Complete witnesses expose an unbounded transformation cost

A complete ordinary witness n to one with L shortcut steps and r odd
steps has the integer charge

\[
\chi(n)=2r-L.
\]

This is independent of the complete witnessing clock: every appended
standard cycle contributes one odd step and two shortcut steps. The
charge is defined only when a complete witness is supplied.

For y=(x+1)/2, the complete classification is

\[
\boxed{\text{a fixed-word affine half-merger at }(x,y)
\quad\Longleftrightarrow\quad \chi(y)=\chi(x)+1,}
\]

when both complete profiles are supplied. The forward implication can
also transport a supplied source witness to the target. The reverse
implication constructively pads terminal cycles and lifts the resulting
actual words to an infinite ordinary arithmetic progression. The more
general slope `2^u3^v` has charge difference `u+2v`.

The retained source family gives a global obstruction to this architecture.
For k>=1, let m=27k and

\[
K=(4^m-1)/81,\qquad x=256K+1,\qquad y=128K+1.
\]

Here x mod512=257, and the complete input tuple is
`[0,2,4,6,2m+8]`. This family and its forced target prefix were already
proved in the earlier `WitnessLengthSeparation.lean`; they are credited
inputs. The new charge argument proves that **none** of these pairs
admits an affine half-merger, at any clocks or with any terminal padding.
It does not assume convergence of the target: an alleged merger would
construct that witness and then contradict the height/charge bound.

For the power family n_m=3^m+1, homogeneous power mergers preserve
`J(m)=2m+chi(n_m)`. Such a merger exists exactly when the two witnessed
signatures coincide. But every complete witness satisfies

\[
J(3h)>h\qquad(h\ge1).
\]

Thus no finite set of certified powers can cover all powers by arbitrarily
long chains of these homogeneous comparisons. This conclusion allows
unbounded clocks, padding and adaptive choices inside the stated class.
An explicit successful exponent-decreasing cell is retained in the note;
the obstruction explains why adding more such cells cannot complete the
finite-seed architecture.

The same invariant constrains the earlier joint-edit compiler. Matched
same-parity steps have zero cost; a step on only one coordinate costs one.
Any successful t-edit alignment constructs the target witness and obeys
`|chi(x)-chi(y)|<=t`. For the four-step source family above,

\[
\boxed{t\ge9k+2.}
\]

No bound depending only on the source's four odd steps can work. This is
stronger than the earlier output-length separation because terminal
source padding can be matched at zero edit cost but cannot change charge.
It does not exclude pointwise mergers or an unbounded, successfully
constructed edit budget.

## 4. A density-free analytic criterion with explicit radius costs

For the actual positive ordinary orbit of n, let e_k be its parity bit
and p_k its number of odd inputs before time k. Define

\[
B_n(z)=\sum_{k\ge0}e_k3^{-p_{k+1}}z^k,
\qquad K_n(t)=(1+4t+t^2)B_n(2+t).
\]

The translation is the literal full binary analytic germ. It is not a
freely fitted rational series. The new written criterion is

\[
\boxed{
n\longrightarrow1\quad\Longleftrightarrow\quad
K_n\in\mathbb Z[1/3][[t]],\quad
R_\infty(K_n)>\tfrac12,\quad R_3(K_n)\ge1.
}
\]

There is no assumption that p_k/k converges. The unconditional
positive-source inequality `1<=T^k(n)<=n*2^(2p_k-k)` supplies the local
radius at zero. The stated arithmetic and radius bounds at two permit a
two-center application of Chambert-Loir--Nous, *Potentiel et rationalite*,
Theorem4.3. The local domains and the integral model are specified in
the proof.

For the explicit radii 4/3 and 2/3 at infinity, the limiting potential
matrix is

\[
\begin{pmatrix}\log(4/9)&\log2\\\log2&\log(2/3)\end{pmatrix}.
\]

The strategy (2/5,3/5) has strictly positive column payoffs
`log(128/81)/5` and `log(32/27)/5`. These finite inequalities are
checked in Lean. A separate written radius optimization gives the strict
threshold 1/2. Rationality then gives eventual ordinary periodicity.
The frozen PR182 actual-cycle obstruction selects the standard cycle
from the arithmetic coefficient condition.

Conversely a supplied successful ordinary prefix makes K_n a polynomial
with one common power-of-three denominator. Thus all convergent sources
satisfy the criterion. The new result replaces the earlier density
assumption with **explicit stronger analytic bounds**; it does not derive
those bounds from the earlier qualitative germ hypothesis. Constructing
the full actual coefficients and radii for every source is still the
central missing step on this route.

## Evidence, attribution, and next construction

The peer dependency is frozen at PR182
`e4367dd2c4406c1041e66d82dfba822908747fa3`,
`RATIONAL_SELECTION.md`, R6-SEL-4. PR178's two relevant germ/filter
notes were read at `398b3a04da071e96362005792417bd5cf8cc6497`.
The [source ledger](../../../reports/lean-exact-witness-global-20261121/construction-attacks-20261123/SOURCES.json)
distinguishes complete note reads, primary theorem reads, metadata-only
refreshes, and orientation sources. The earlier all-PR inventory remains
historical evidence; it was not rerun or relabeled as this checkpoint.

Each of the four new arguments has a separate source-bound internal
review by an agent who did not author it. The root supplied the carry
maximization idea in the template lane and authored the germ argument;
neither root reconstruction is counted as independent review. Finite
controls include deliberately failing strengthened claims, not just
successful examples.

The next useful construction must supply information not already encoded
in an unknown termination witness: an actual paid descent, absolute
moving-root predecessor mass, a transformation that changes the power
signature with a justified cost, or the full arithmetic germ with its
radii. This checkpoint proves the stated unrestricted consumers and
obstructions and leaves those construction obligations explicit.
