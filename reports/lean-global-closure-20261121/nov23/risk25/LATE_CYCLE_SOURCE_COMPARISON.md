# Late arithmetic-source comparison at the integer-cycle boundary

Date: 2026-11-23. **Status: narrow source comparison and exact interface
check. No new numerical-gcd bound or unrestricted cycle exclusion.**
This note leaves the frozen residual-degree, recurrence-lattice, and
cyclotomic-value files unchanged. It records the three newly supplied
repository heads and checks whether their integral consequences close
the remaining distinguished-fiber step.

## 1. Exact sources read

| PR | Full head | Complete path read |
|---|---|---|
| 182 | `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c` | `research/literature-round4-20261123/CYCLE_RIGIDITY.md` |
| 178 | `c91b80a3156e640ad471cf30c47721145ae21eb1` | `research/central-step-20261123/cycles/COMPLEMENTARY_DENOMINATOR_CAPACITY.md` |
| 180 | `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161` | `research/profound-step-20261123/ARITHMETIC_CLOSURE.md` |

All three complete notes were read from their pinned git objects. The
comparison below checks the displayed finite arguments and their
connection to this lane. It does not claim a replay of the referenced
Lean modules, a fresh audit of their external literature, or additional
control enumeration.

## 2. The boundary supplied by this lane

For an odd-gap word of period `p` and total clock `A`, use

\[
 F=X^p-2^A,\quad Q=\sum_{j=0}^{p-1}2^{s_j}X^{p-1-j},\quad
 G=\gcd(F,Q),\quad F_0=F/G,\quad Q_0=Q/G,
\]

with monic gcd, and write `d=deg F_0`, `D_pol=|F_0(3)|`.
For an actual primitive positive integer cycle with minimum `m` and
maximum odd state `M`, the reviewed written packet gives

\[
 d\ge c p^\varepsilon,\qquad m\le C_m d^K,\qquad
 M\le C_1d^K(3/2)^{d-1}.
\]

The separately reviewed cyclotomic continuation gives

\[
 D_{\rm pol}\ge c_0\beta^d d^{-K_0},\qquad
 \beta=\frac3{\sqrt{1+\sqrt2}}>\frac32.
\]

Consequently

\[
 \frac{D_{\rm pol}}M
 \ge c_1\frac{(\beta/(3/2))^d}{d^{K+K_0}}\longrightarrow\infty
\]

along any hypothetical sequence with unbounded primitive periods.
The constants retain the large, explicit Matveev exponent and the
qualified ordinary-state-count input of the core file. This is an
asymptotic necessary condition, not a practical remaining search bound.

The exact integral condition is still

\[
 D_{\rm pol}\mid Q_0(3),\qquad
 J=\frac{Q_0+mF_0}{X-3}\in\mathbb Z[X].
\]

Here `J` is primitive and its roots obey the bounds proved in the core
file. A large value of `D_pol/M` alone supplies no upper bound on
`gcd(D_pol,Q_0(3))`.

## 3. What the new minimum-root gap theorem supplies

PR182 works with the complete shortcut word, of length `A` and weight
`p`, and its full denominator `D=2^A-3^p`. For a cut `w=uv`, with
block denominators `d_u,d_v` and complete block carries `C(u),C(v)`,
it proves the exact identity

\[
 C(vu)-C(uv)=d_vC(u)-d_uC(v).
\]

At the least root of a primitive integer word, each proper rotation
has a positive carry gap which is a multiple of the **full** `D`.
It is at least `D`; when both endpoint states are odd it is at least
`2D`. The same source proves the necessary suffix coefficient barrier
for every positive rational least root. The latter therefore does not
provide an additional integral constraint.

The exact dependence among the gap congruences is especially relevant:
over all shortcut rotations,

\[
 \gcd_i\{C_i-C_0\}=\gcd(D,C_0).
\]

Thus imposing all these congruences recovers the existing cancellation
condition. The source also shows exactly that selecting the unique
least root leaves the fraction of integral words unchanged. Neither
selection can be charged as an independent rarity factor.

At odd rotations the monic polynomial gcd `G` is unchanged. Under
integrality, dividing the complete carry gap by `G(3)>0` gives

\[
 Q_{0,i}(3)-Q_{0,0}(3)=D_{\rm pol}(x_i-m)\ge2D_{\rm pol}
 \quad (x_i\ne m).
\]

Its upper bound is `(M-m)D_pol`. Hence `D_pol>M` does not contradict
the gap theorem: both the lower and upper carry-gap bounds contain
the same factor `D_pol`. An upper bound on an ordinary state is not
an upper bound on its complete or residual carry.

The new note therefore gives exact word-rejection certificates and
retains the full numerical arithmetic, but supplies no upper bound on
our distinguished gcd and no extra restriction on `J` beyond those
already implied by the same integral cycle.

## 4. What the two companion-denominator theorems supply

Let the original primitive shortcut cycle have length `A` and `p`
odd states. Its complemented word has `A-p` odd states and its own
complete carry `C_c`. Both new notes retain the completely reduced
companion denominator

\[
 B_c=\frac{2^A-3^{A-p}}{\gcd(2^A-3^{A-p},C_c)}.
\]

PR178 proves `B_c>A/2` for a nontrivial positive integer cycle, and
the non-strict `A<=2B_c` including the core. Its more precise capacity
inequality gives a minimum-sensitive continuous envelope, and an
asymptotic lower ratio about `0.7864098721` along hypothetical
unbounded-period families. The decimal is illustrative; the source's
exact implicit expression defines the bound.

PR180 proves the different explicit inequality

\[
 B_c>3(2p-A)
\]

and a sharper finite product over distinct positive odd numerators
below `B_c`, retaining their coprimality with `B_c`. Both proofs use
actual distinct numerator values in the complete companion cycle;
they do not multiply independent rotation probabilities.

These are substantive lower bounds on a fully reduced numerical
denominator. But `B_c` concerns the **complemented** word, whose
denominator and carry differ from `D_pol,Q_0(3)`. Neither theorem
supplies an upper bound on `B_c` from original positive integrality,
or converts its required lack of companion cancellation into a
failure of the original cancellation.

Both sources explicitly expose this missing direction and include
negative-integer-cycle controls against a sign-independent inference
that original integrality forces companion integrality. Such controls
do not disprove a positive-source theorem; they show why that theorem
would need a further use of positivity. The lower bounds proved here
are consistent with `D_pol/M` tending to infinity.

## 5. Remaining arithmetic step

No new integer-specific estimate on the numerical gcd or on the height
of the primitive polynomial `J` was obtained from this late refresh.
In particular, none of the three notes proves

\[
 \gcd(D_{\rm pol},Q_0(3))<D_{\rm pol},
 \qquad\text{or}\qquad
 \log m\ge c d\quad(c>0).
\]

The latter, if proved with adequate quantitative control, would bound
the possible residual degrees and periods when combined with the
core polynomial minimum bound; exclusion of the remaining finite
range would still be required. It is not supplied by a comparison of
the sizes of the residual denominator and the orbit states.

The fresh gap and companion results therefore leave **full original
numerical cancellation open**. This note makes no broader claim that
these tools cannot participate in a future proof.
