# A proper common rank for guarded witness rewrites

**Status.** The common strict order is well-founded in Lean 4.34.1 core:
[`CommonRank.lean`](lean/CollatzGlobal/CommonRank.lean), theorem
`scoreLT_wellFounded`. The source-clock conjugation of binary reverse
transformations into the psi relation is formalized in
[`PsiTemplateBridge.lean`](lean/CollatzGlobal/PsiTemplateBridge.lean).
The eight older negative-reference witness transformations below retain
their frozen paper-level proof dependency; this note does not silently
formalize their ordinary-legality guards. **Universal rule coverage is OPEN.**

This addresses a real mismatch between two previously usable moves. A
forward paired return can increase the ordinary source while consuming
its certificate clock. A negative-reference transformation decreases its
ordinary parameter while lengthening that source certificate. Neither
lexicographic order of just size and clock handles both. A slowly increasing
exponential weight does handle a guarded subset of both types.

## CR1. The rank and its properness

A goal carries an ordinary **convergent source** `n` and its exact supplied
hit clock `d`. Its target and relation kind must also be tracked by the
compiler; the rank does not erase those semantics. Put

\[
\lambda=\frac{201}{200},\qquad
P(n,d)=(n+1)\lambda^d.
\tag{1}
\]

Only exact natural-number comparisons are needed. The strict move from
`(n,d)` to `(n',d')` is

\[
(n'+1)201^{d'}200^d
< (n+1)201^d200^{d'}.
\tag{2}
\]

The order is well-founded, although it is a rational-valued order. The
essential fact is that its sublevel sets are finite. Bernoulli's inequality
gives

\[
\lambda^d\ge 1+\frac d{200}.
\]

Thus `P(n,d)<=B`, for an integer `B`, implies `n+1<=B` and `d<=200B`.
Inside this sublevel, set `E=200B` and clear the common denominator:

\[
R_E(n,d)=(n+1)201^d200^{E-d}\in\mathbb N.
\]

Every strict move satisfying (2) stays inside the sublevel and strictly
decreases `R_E`. Every initial state lies in some such integer sublevel.
This proves that no infinite sequence of strictly guarded moves exists.
The Lean proof uses this finite-denominator argument, not an assumed
well-order on the rationals.

## CR2. Forward returns, including increasing ordinary sources

Suppose a supplied ordinary paired return consumes `t` source clocks and
changes its convergent source from `n` to `q`. Its source certificate
changes from `d` to `d-t`. The exact guard is

\[
\boxed{(q+1)200^t<(n+1)201^t.}
\tag{3}
\]

For five goals, the target transport is supplied by the actual balanced
return. For psi goals the convergent source is `n=3m-1`, not the unknown
target `m`. A relation return to target `r` has convergent source `3r-1`,
and (3) becomes `r*200^t<m*201^t`.

An expanding **psi** return is proved in `PsiExpansion.lean`. Its seed is

\[
\begin{aligned}
T^{52}(106495)&=131455>106495,\\
T^{52}(319484)&=394364=3\cdot131455-1,\\
T^{196}(319484)&=1,\\
131455\,200^{52}&<106495\,201^{52}.
\end{aligned}
\]

Here `319484=3*106495-1`. The actual convergent source increases to
`394364` while its supplied certificate clock falls from `196` to `144`.
The common-rank ratio is about `0.95239`. This is the **same psi goal
kind** as the translated negative-reference rules in CR4, so both allowed
coordinate increases occur within one comparison problem.

The result covers an unbounded affine family, not only this seed. Put

\[
m_h=106495+2^{52}h,\qquad r_h=131455+3^{33}h,
\qquad h\in\mathbb N.
\]

The two seed arms each have exactly `33` odd inputs through clock `52`.
The exact high-bit lifting theorem therefore proves, for every `h`,

\[
T^{52}(m_h)=r_h,\qquad
T^{52}(3m_h-1)=3r_h-1,\qquad
m_h<r_h,\qquad r_h200^{52}<m_h201^{52}.
\]

The constant and coefficient inequalities are both verified in Lean; in
particular `3^33*200^52 < 2^52*201^52`. For `h mod 3 != 2`, `m_h` is a
ternary unit, so infinitely many members satisfy the psi closing
domain's ternary-unit restriction.
**Convergence of a general lifted source is not asserted.** If its source
certificate at a clock `d>=52` is supplied, this return transports it to
clock `d-52` and strictly decreases the common rank. The displayed seed
has the actual certificate `d=196` proved by kernel reduction.
Theorems `psi_expanding_family_source`, `psi_expanding_family_target`, and
`psi_expanding_family_rank` connect these identities to the actual
source-witness transport, target Basin equivalence, and `ScoreLT` order.
`psi_expanding_seed_child_certificate` and `psi_expanding_seed_rank`
instantiate the complete seed transition in Lean.

The separate five-goal expanding example from `AdaptiveDescent.lean`
also satisfies (3):

\[
19483\xrightarrow[30\ \mathrm{clocks}]{}21091,\qquad
21092\,200^{30}<19484\,201^{30}.
\]

Its rank ratio is about `0.93209`. Both examples admit moves that a
strictly decreasing ordinary-value rank rejects. Not every paired return
is asserted to pass (3); testing the exact guard is part of the proposed
compiler.

## CR3. Negative-reference transformations

Freeze PR168 at
`e4599b32e4b1a955ac9315d46782d4ad6a5db96c`,
`research/closure-frontier-20261121/NEGATIVE_TEMPLATE_GRAMMAR.md`,
NT2--NT3 and the eight-row catalog. The first two rows there credit PR164
at `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`,
`research/witness-closure-512-2026-11-20/continuation-negative.md`,
W512-070--072. We use precisely the old theorem that each eligible input
has positive ordinary prefix realizations and a complete source witness
is transported with **shortcut-clock increment `a`**. For these eight rows
the retained prefixes end above one, so that statement requires no witness
padding. The increment refers to the total clock, not a final valuation.

For a row `(a,b,c)`, the parameter transformation is

\[
3^bM'=2^aM+c,\qquad 0<M'<M.
\]

The original binary reverse goal has convergent source `n=128M+1` and
unknown target `64M+1`. Its child source is `n'=128M'+1`, with source
clock `d'=d+a`. The exact identity

\[
3^b(n'+1)=2^a(n+1)+2(64c+3^b-2^a)
\tag{4}
\]

shows strict rank descent whenever

\[
64c+3^b<2^a,
\qquad
402^a<200^a3^b.
\tag{5}
\]

Both are exact integer inequalities. The second controls the coefficient
of the unbounded positive parameter; the first makes the additive term
favorable on the entire progression.

| Reference | `a` | `b` | `c` | Ternary class `rho` | Uniform coefficient upper bound |
|---|---:|---:|---:|---:|---:|
| `-197/243`, credited PR164 | 7 | 5 | -69 | 48 | `402^7/(200^7*3^5) < 0.546` |
| `-29/27`, credited PR164 | 9 | 6 | -271 | 674 | `402^9/(200^9*3^6) < 0.735` |
| `-755/729` | 9 | 6 | -243 | 486 | `402^9/(200^9*3^6) < 0.735` |
| `-1039/729` | 11 | 7 | -1069 | 779 | `402^11/(200^11*3^7) < 0.990` |
| `-3125/2187` | 11 | 7 | -1077 | 480 | `402^11/(200^11*3^7) < 0.990` |
| `-3101/2187` | 11 | 7 | -1053 | 1377 | `402^11/(200^11*3^7) < 0.990` |
| `-3011/2187` | 11 | 7 | -963 | 2007 | `402^11/(200^11*3^7) < 0.990` |
| `-1603/2187` | 10 | 7 | -579 | 2100 | `402^10/(200^10*3^7) < 0.493` |

Each row retains its original exact guards `M=-1 mod2048` and
`M=rho mod3^b`, together with the proved positive ordinary realization
conditions. The common rank does not remove those guards or assert that
the rows cover every parameter. The displayed decimal upper bounds are
only readable summaries of rational bounds; the acceptance tests use the
integer comparisons in (5).

### Why these eight rows need no hidden source-witness padding

The generic old compiler allows padding with the `1,2` cycle when a
supplied certificate ends before a retained prefix. That case must not be
silently charged only `a` additional clocks. For these eight instantiated
rows it is excluded on the **entire guarded domain**, as follows.

All eight rows have retained old source word `(2,2,2,1,2,4)` of clock
13 and retained old target word `(2,2,3,1)` of clock 8. Write
`M=2048h-1`, `h>=1`. The exact four retained endpoints are

| Retained arm | Old endpoint | New endpoint |
|---|---|---|
| Source | `23328h-11` | `1458h-1` |
| Target | `41472h-19` | `10368h-5` |

They are respectively at least `23317,1457,41453,10363`, all greater
than one. The source endpoints satisfy `old=16*new+5=J^2(new)`, and
the target endpoints satisfy `old=4*new+1=J(new)`, where `J(v)=4v+1`.
Once ordinary prefix legality from the frozen NT2 proof is imposed, no
prefix can have hit one earlier: an orbit from one stays in `{1,2}`
and cannot subsequently end at these odd endpoints greater than one.
Every complete certificate therefore has a nonempty tail after its
retained prefix.

For the source, the next exact valuation at the old endpoint is four
larger than at the new endpoint, so it is at least five. The new prefix
clock is `17+a`; replacing that first tail valuation by four less gives
the exact net clock change `(17+a)-13-4=a`. For the target the analogous
prefix clock is `10+a`, the valuation difference is two, and the same
calculation gives `+a` forward and `-a` on the child-to-parent witness.
There is no uncounted padding term for any supplied complete certificate
on these progressions.

[`check_common_rank.py`](check_common_rank.py) stores the eight exact
retained word pairs and derives these four formulas by rational affine algebra, verifies
every prefix's positive slope and lower bound for all `h>=1`, and checks
the exact clock and odd-count differences. Its
[`common-rank-data.json`](common-rank-data.json) is the reproducible output.
This verifies the no-padding deduction at the whole-parameter level;
it retains the old ordinary-legality guard theorem as a named dependency.

## CR4. Conjugating these transformations into the psi goal type

This avoids conflating different comparison problems. Put `m=27M+1`.
The exact ordinary identities, now checked in Lean, are

\[
T^7(128M+1)=81M+2=3m-1,
\qquad T^6(64M+1)=m.
\tag{6}
\]

Given a source certificate of clock `d` for `3m-1`, prepend the upper
seven-step prefix, apply the supplied binary negative-reference source
transformation, then remove the new seven-step prefix. Its child source
certificate has clock **`d+a`**. The fixed overhead cancels exactly.
Target certificates transport through the corresponding six-step prefixes.
`conjugate_binary_source_clock` and `conjugate_binary_target` formalize
this construction with the old transformation as an explicit hypothesis.

Thus the old rule gives an actual same-kind psi rewrite from `m=27M+1`
to `m'=27M'+1`. The convergent source rank is now

\[
P(3m-1,d)=3m\lambda^d.
\]

In these coordinates,

\[
3^b(3m')=2^a(3m)+3(27c+3^b-2^a).
\tag{7}
\]

All eight rows also satisfy `27c+3^b<2^a`. Together with the same
coefficient comparison in (5), this proves strict descent in the same
rank (1). Hence guarded psi returns and the translated negative-reference
rows can be interleaved without an infinite chain of successful calls.
The source witness and the target certificate direction are both retained.

For other bridges between goal kinds, one must separately prove actual
source-witness transport, the target implication in the required direction,
and the rank guard. The present theorem grants no unrestricted bridge.

## CR5. What the combined compiler still needs

The root retraction theorem explains why inverting a balanced return and
then normalizing it again cannot create a decreasing loop. In the common
rank, the inverse of an admitted strict return is automatically rejected.
This is compatible with the positive synthesis above: the negative-reference
rules are different guarded transformations, not an unguarded inverse.

For full closure, the compiler still needs a **total successful selector**:
every eligible unresolved psi goal must either have a complete target
certificate or admit one of the sound strict moves. The finite residuals
from `PsiNormalization.lean` need not lie in the translated congruence
classes `m=27M+1`, `M=-1 mod2048`, `M=rho mod3^b`. No coverage theorem is
established here, and the existence of a common rank does not supply one.

This pass therefore closes the termination issue for these explicitly
guarded mixed moves, including some that increase source size and others
that increase source clock. It leaves universal coverage as the decisive
mathematical obligation. The older ordinary-legality and witness-transform
theorems remain precisely sourced dependencies of the instantiated rows.
