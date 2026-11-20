# Signed summable clock filters cannot supply the missing smoothing

**PROPOSED elementary extension of SM3.** The previously frozen
[smoothing note](SMOOTHING_BOUNDARY.md) deliberately leaves signed clock
cancellations outside its positive-averaging theorem. This annex checks
that possibility. It classifies every fixed absolutely summable linear
filter of the ordinary finite products. It does not establish anything
new about the pointwise infinite product's regularity, and it does not
prove Collatz.

Use `U(n)=(3n+1)/2^{v_2(3n+1)}` on positive odd ordinary integers, and
put

\[
c(n)=\frac{3n}{3n+1},\quad
r_q(n)=\prod_{j<q}c(U^j n),\quad r_0(n)=1,\qquad c_* =3/4.
\]

No packing theorem, unknown orbit, or external approximation theorem is
needed below.

## SF1. Adjacent ordinary witnesses for every finite landing time

Fix an integer `ell>=1`. Choose arbitrarily large even integers `H` with
`3^{ell-1}` dividing `H-1`; for example

\[
H=1+(2v+1)3^{\ell-1}\quad(v=0,1,2,\ldots).
\]

Define

\[
m_{\ell,H}=\frac{2^{H-1}+1}{3^\ell},\qquad
n_{\ell,H}=2^\ell m_{\ell,H}-1,
\qquad t_H=\frac{2^H-1}{3}.
\]

The lifting identity
`v_3(2^d+1)=1+v_3(d)` for positive odd `d` proves that `m` is a
positive odd integer. This identity also follows directly by factoring
`x^3+1` successively, as in OE2. The states

\[
x_j=2^{\ell-j}3^j m_{\ell,H}-1
\quad(0\le j\le\ell-1)
\]

have exact gap one for `j<ell-1`, end at `t_H`, and then reach 1.
For fixed `ell` and `H` tending to infinity, all these pre-landing
states tend to infinity. Hence, at every fixed finite clock `q`,

\[
\lim_H r_q(n_{\ell,H})
=\begin{cases}
1,&q\le\ell,\\
c_*^{q-\ell},&q>\ell.
\end{cases}                                             \tag{1}
\]

The adjacent ordinary source also has an explicit description:

\[
n_{\ell,H}+2
=\frac{2^{H+\ell-1}}{3^\ell}+\rho_\ell,
\qquad \rho_\ell=1+(2/3)^\ell>0.                        \tag{2}
\]

Here `rho_ell` is an odd 2-adic rational with odd denominator. Apply the
same odd map to this positive rational using numerator parity. At each
finite step `3x+1` is positive and nonzero, so its 2-adic valuation is
finite, and the next odd rational is again positive. In particular its
first `q` odd valuations have a finite sum for every fixed `q`.

The difference in (2) has 2-adic valuation `H+ell-1`, which tends to
infinity. For all sufficiently large admissible `H`, the adjacent ordinary
source therefore has exactly that finite valuation word: at each step,
a difference of valuation larger than the current gap preserves the
gap, and the forward affine map reduces the remaining precision by
that gap. This is a finite induction, not an assertion of equality of
infinite trajectories.

If `A_j` is the sum of the first `j` gaps of the rational source, the
actual ordinary iterate is then

\[
U^j(n_{\ell,H}+2)
=U^j(\rho_\ell)
 +\frac{3^j}{2^{A_j}}\frac{2^{H+\ell-1}}{3^\ell}.
\]

For fixed `j` its second summand tends to positive infinity. Consequently

\[
\lim_H r_q(n_{\ell,H}+2)=1\qquad(q\text{ fixed}).        \tag{3}
\]

The rational source in this proof only certifies a finite valuation
prefix of each changing adjacent ordinary witness. Neither its limit
nor this argument supplies a positive ordinary escaping source.

## SF2. Complete classification of fixed summable clock filters

Let `(alpha_q)_{q>=0}` be real or complex coefficients with
`sum_q |alpha_q|<infinity`, independent of the ordinary source. Define

\[
R_\alpha(n)=\sum_{q\ge0}\alpha_q r_q(n),
\qquad A=\sum_{q\ge0}\alpha_q.
\]

The series defines a bounded function, since `0<r_q<=1`.

**Theorem.** The adjacent-smoothing condition

\[
R_\alpha(n+2)-R_\alpha(n)\longrightarrow0
\quad(n\text{ positive odd},\ n\to\infty)               \tag{4}
\]

holds if and only if `alpha_q=0` for every `q>=2`.

**Proof.** Absolute summability permits dominated summation in (1)--(3).
For each fixed `ell>=1`, it gives the exact adjacent limit

\[
\lim_H\{R_\alpha(n_{\ell,H}+2)-R_\alpha(n_{\ell,H})\}
=A-G_\ell,
\]

where

\[
G_\ell=\sum_{q\le\ell}\alpha_q
       +\sum_{q>\ell}\alpha_q c_*^{q-\ell}.             \tag{5}
\]

If (4) holds, `G_ell=A` for every `ell>=1`. Subtracting two consecutive
equalities yields

\[
0=G_{\ell+1}-G_\ell
 =(1-c_*)\sum_{q\ge\ell+1}\alpha_q c_*^{q-\ell-1}.
\]

Call the last sum `H_ell`. It is zero for every `ell>=1`, and
`H_ell=alpha_{ell+1}+c_* H_{ell+1}`. Thus every `alpha_{ell+1}` is zero.
Conversely, support on `{0,1}` gives
`R_alpha(n)=alpha_0+alpha_1 c(n)`, whose adjacent differences tend to
zero. This proves both directions. No positivity of the coefficients
was used. ∎

## SF3. Bounded signed averaging families also retain the large jump

Suppose a family of summable filters satisfies

\[
\sum_q\alpha^{(v)}_q=1,\qquad
\sup_v\sum_q|\alpha^{(v)}_q|<\infty,\qquad
\alpha^{(v)}_q\to0\text{ for every fixed }q.
\]

These are bounded total variation, normalized filters whose coefficients
leave every fixed clock. Formula (5) for `ell=1` gives

\[
G^{(v)}_1=\alpha^{(v)}_0+\alpha^{(v)}_1
 +\sum_{q\ge2}\alpha^{(v)}_q c_*^{q-1}\longrightarrow0.
\]

To justify the limit, first split at a fixed finite clock. The finite
part tends to zero term by term; the remaining part is bounded in
absolute value by the common total-variation bound times a geometric
tail maximum, which can be made arbitrarily small. Therefore

\[
\liminf_v\ \limsup_{n\to\infty\atop n\ {\rm odd}}
|R_{\alpha^{(v)}}(n+2)-R_{\alpha^{(v)}}(n)|\ge1.          \tag{6}
\]

Thus bounded signed averaging families cannot restore uniform adjacent
smoothing while passing to arbitrarily late clocks. This extends the
positive-law statement, without making a claim about arbitrary
unbounded-total-variation regularizations.

## Scope of the obstruction

The classification covers fixed absolutely summable source-independent
linear filters. The family statement requires the three displayed
uniform hypotheses. Source-dependent stopping rules, non-linear
procedures, unbounded-total-variation schemes, or a separate theorem
about the actual pointwise limit are outside these claims.

In particular the infinite product can still vanish everywhere even
though every nontrivial summable finite-clock filter fails (4). The two
limits, changing ordinary source and increasing clock, cannot be
interchanged. This annex closes a specified signed-filter possibility;
it supplies no new escape or cycle exclusion.
