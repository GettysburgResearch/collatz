# Actual scalar formalization and three attacks on repeated returns

23 November 2026. Published parent PR182:
c369ae3c426ec6aaf9a280ec9578b9910c2147d5.

**Collatz remains OPEN.** The main formal advance in this packet is
an actual-map Lean proof that a positive odd source reaches one if
and only if its discounted valuation scalar is triadic rational.
Three parallel attacks then restrict the still-unresolved arithmetic
and return dynamics. Each retains one fixed ordinary source where
that is required; constructions with changing finite sources are
explicitly identified.

The [source pins](SOURCES.json) identify the exact parent claims and
inspected literature. The
[execution and review report](../../reports/2026-11-23-carry-tower-round10/README.md)
separates written proofs, full actual-scalar formalization, finite
Lean arithmetic, ordinary controls, and publication evidence.

## 1. Lean now constructs the actual scalar and proves its criterion

For the positive odd Collatz map, put

\[
q_{i+1}=U(q_i)=\frac{3q_i+1}{2^{g_i}},\qquad
g_i=v_2(3q_i+1),\qquad
h(q)=\sum_{i\ge0}\frac{g_i}{3^{i+1}}.
\]

[ActualScalar.lean](ActualScalar.lean) defines the actual map and
orbit, proves unconditional real summability, and proves

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g(q).
\]

It also proves the exact finite-tail identity and its interval bounds.
An integer scalar makes the actual logarithmic potential
V(q)=log(q)-h(q)log(2) decrease by at least -log(5/6) until one is
reached, while V remains bounded below. Clearing a supplied power
of three along the actual orbit then proves

\[
\boxed{q\longrightarrow1\quad\Longleftrightarrow\quad
h(q)\in\mathbb Z[1/3].}
\]

The full argument is in Lean, including the scalar's existence and
the actual convergence conclusion. It imports Mathlib and defines
the orbit locally; it assumes no repository convergence theorem.
[ACTUAL_SCALAR_FORMALIZATION.md](ACTUAL_SCALAR_FORMALIZATION.md),
R10-G1--G3, explains its proof and exact scope.

**The missing universal assertion is still that every actual h(q)
belongs to Z[1/3].** An equivalence with that assertion does not prove it.

## 2. A finite paid return can be constructed for every rational phase

[GENERAL_PHASE_RETURN.md](GENERAL_PHASE_RETURN.md), R10-P1--P4,
extends the local denominator-eight mechanism to any complete
rational tripling phase. Write h_i=p_i+k_i with the canonical phase
p_i in (1/2,3/2] and integer carry k_i>=0. The complete physical and
scalar equations give

\[
Y_i=q_i/2^{k_i},\qquad
Y_{i+1}=\frac{3Y_i}{2^{b_i+2k_i}}
       +\frac1{2^{b_i+3k_i}}.
\]

The finite necessary scalar guard implies Y_i>=1. Every high step
therefore contracts Y by at least the factor 7/16. The zero-carry
run is computed from the binary distance to the complete canonical
rational cycle: if its word has length L, binary clock A, full affine
constant C, and D=3^L-2^A, the first departure is fixed by

\[
T=v_2(|Dq+C|).
\]

When Dq+C is nonzero, a paid low return or sound rejection is reached
within

\[
\boxed{\operatorname{bl}(q)+2T}
\]

actual odd transitions. The exceptional zero case is checked as a
literal canonical cycle. A returned endpoint preserves the proposed
scalar equality exactly; returning does not accept that equality.

Every arbitrary paid excursion has the entrance comparison

\[
r\le P_2(x)=\frac{9x+5}{32}
\quad\hbox{or}\quad
r\le P_3(x)=\frac{9x+7}{64}.
\]

The complete cost of the preceding expanding zero-carry run stays
in the comparison with the original source.

For the sharp phase 729/1456, the gate is
v_2(7153q+700273) mod19 in {7,9,11,13,15,17,18};
the budget is at most 3bl(q)+26. R10-P5 gives a specific same-phase
word family that descends through 101 canonical repeats and expands
from 102. This threshold is for that exact family.

## 3. Successive arbitrary returns have a growth budget

[RETURN_TOWER.md](RETURN_TOWER.md), R10-T1, considers the actual
denominator-eight level h=7/8. Let q_j be its normalized return
boundaries and m_j the unpaid L=(2,1) blocks before the next paid
excursion. With B=bl(q_0+7), arbitrary paid words obey

\[
\boxed{3\cdot15^j m_j<(B-1)16^j.}
\]

This retains arbitrarily large carries and supplies a fixed-source
restriction on how quickly later unpaid runs can grow. A sharper
bound has exponential base log_8(9), while the cumulative unpaid
mean must be at least 10.7698983756...; the note gives exact formulas.
Slowly changing schedules remain compatible with these inequalities.

For the particular expanding word R=L^11 P, with P=(1,4), define

\[
Z(q)=7551629537q+1478790549031.
\]

R10-T2 proves its **exact** number of consecutive literal repetitions:

\[
\boxed{\left\lfloor\frac{v_2(Z(q))-1}{38}\right\rfloor.}
\]

Each R lowers that integer valuation by 38. Different return types
can change the relevant affine center; controlling these changes is
still open.

R10-T3 constructs arbitrarily long actual finite expanding towers
whose true scalars decrease just below 7/8 while v_2(q_j+7)=34
throughout the selected comparisons. Both q/h(q) and q/2^(h(q))
increase. Corrections depending only additively, or positively
multiplicatively, on that unchanged valuation cannot make these
potentials decrease. The sources change with the requested length;
no positive infinite expanding tower or exact h=7/8 source is claimed.

## 4. Four sparse automatic scripts have irrational physical completions

[ARITHMETIC_TOWER.md](ARITHMETIC_TOWER.md), R10-A1--A4, uses the
literal L/P equation for X=q+7:

\[
8\,4^{s_j}X_{j+1}=9X_j+166s_j.
\]

If the paid positions are t_0<t_1<..., their unique physical
2-adic completion is

\[
q_*=-7-\frac{166}{9}
\sum_{r\ge0}4^r(8/9)^{t_r}.
\]

An elementary numerator-height and binary-valuation argument proves
this value irrational whenever

\[
\limsup_{r\to\infty}\frac{8^{t_{r+1}}}{9^{t_r}}=\infty.
\]

This excludes rational physical sources of either sign for that
script class. In particular, it excludes the four automatic scripts
that select P at positive indices with at most k binary one-bits,
for k=1,2,3,4. Every script still has symbolic scalar 7/8 and every
finite prefix has positive ordinary realizations. A fixed positive
source has an explicit finite mismatch budget linear in its bit length.

The proof keeps real and 2-adic values separate, as suggested by the
directly inspected Mahler paper. It imports no transcendence theorem.
The displayed lacunarity test fails at k=5, and automaticity alone
is not an exclusion criterion.

## The remaining construction task

The actual real scalar and its convergence criterion are formalized.
For any supplied rational phase, a finite equality-preserving return
can be constructed. Fixed return words and sufficiently sparse scripts
have arithmetic obstructions. What is missing is a rank or arithmetic
argument that controls **arbitrary changes of return type at one
unchanged ordinary source**, and ultimately forces its actual scalar
into Z[1/3]. The companion
[handoff](../../reports/2026-11-23-carry-tower-round10/HANDOFF.md)
records that target and the precise limits of each completed attack.
