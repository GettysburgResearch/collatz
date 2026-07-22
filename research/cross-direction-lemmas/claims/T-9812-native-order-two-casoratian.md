# T-9812 -- The native order-two stack function has an exact nonzero Casoratian

Claim ID: `T-9812`
Title: The periodic stack function and its first q-shift are formally independent, with a physically nonvanishing two-place Casoratian
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave14-period-ten`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: branch-qualified `PR20/L-9408` and `L-9415` at `aa9cf71c1f252359869ef917955051f340a09df7`; both blobs are unchanged from `93739b4dbc4ac317f660477e7805dabfe484b287`
Scope: every positive periodic stack increment word at every physical starting height
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Let

\[
 W=d_1\cdots d_r,
 \qquad r\ge1,
 \qquad d_j\ge1,
 \qquad S=\sum_{j=1}^r d_j,
\tag{1}
\]

and put

\[
 T={64\over81},
 \qquad q=T^{9S},
 \qquad a=T^{e(W)}.
\tag{2}
\]

Use the transfer polynomial of `PR20/L-9408`,

\[
 P_W(X)=\sum_{j=0}^{r-1}p_jX^j,
 \qquad
 p_j=T^{j+9A_j(W)}>0,
 \qquad p_0=1,
\tag{3}
\]

and the periodic-tail function of `PR20/L-9415`,

\[
 F_W(X)=\sum_{n\ge0}f_nX^n.
\tag{4}
\]

It is entire over the complex numbers, converges on the physical `2`-adic
orbit, is not in `Q(X)`, and obeys

\[
 \boxed{F_W(X)=P_W(X)+aX^rF_W(qX).}
\tag{5}
\]

For a physical starting height `m>=0`, put

\[
 x=T^{9m}.
\tag{6}
\]

Extend the word periodically by `d_(n+r)=d_n`, and define

\[
 C_n=\sum_{h=1}^n d_h,
 \qquad
 E_0=0,
 \qquad
 E_n=\sum_{h=1}^n\{9(m+C_h)+1\}.
\tag{7}
\]

Then the exact transfer identity gives

\[
 s_n:=f_nx^n=T^{E_n},
 \qquad
 F_W(q^\ell x)=\sum_{n\ge0}q^{\ell n}s_n
 \quad(\ell=0,1,2).
\tag{8}
\]

The integers `E_n` are strictly increasing and

\[
 E_1=9(m+d_1)+1.
\tag{9}
\]

## Theorem 1 -- formal two-shift independence

The two functions are linearly independent over the rational-function field:

\[
 \boxed{
 \dim_{\mathbf Q(X)}
 \operatorname{span}_{\mathbf Q(X)}
 \{F_W(X),F_W(qX)\}=2.
 }
\tag{10}
\]

### Proof

Suppose `A,B in Q(X)` satisfy

\[
 A(X)F_W(X)+B(X)F_W(qX)=0.
\tag{11}
\]

Substitute

\[
 F_W(qX)={F_W(X)-P_W(X)\over aX^r}
\tag{12}
\]

from (5).  After clearing the nonzero factor `aX^r`,

\[
 \{aX^rA(X)+B(X)\}F_W(X)=B(X)P_W(X).
\tag{13}
\]

If the coefficient of `F_W` in (13) is nonzero, then (13) makes `F_W`
rational, contrary to `PR20/L-9415`.  If that coefficient is zero, then
`B P_W=0`.  Since `Q(X)` is a field and `P_W` is nonzero, `B=0`, and then
`A=0`.  This proves (10). **QED**

## Theorem 2 -- exact Casoratian expansion

Define the first q-Casoratian

\[
 \Delta_W(X)
 =F_W(X)F_W(q^2X)-F_W(qX)^2.
\tag{14}
\]

It has the exact symmetrized expansion

\[
 \boxed{
 \Delta_W(X)
 =\sum_{0\le i<j}
 f_if_j(q^i-q^j)^2X^{i+j}.
 }
\tag{15}
\]

In particular,

\[
 \boxed{
 \Delta_W(X)
 =f_0f_1(1-q)^2X+O(X^2),
 \qquad f_0f_1>0.
 }
\tag{16}
\]

Thus `Delta_W` is not the zero power series and has a simple zero at the
origin.  In the real embedding,

\[
 \boxed{\Delta_W(X)>0\qquad(X>0).}
\tag{17}
\]

### Proof

Absolute convergence in the real embedding and coefficientwise formal
algebra both permit multiplication of the three series.  The diagonal terms
cancel.  Pairing the `(i,j)` and `(j,i)` terms for `i<j` gives

\[
 q^{2j}+q^{2i}-2q^{i+j}=(q^i-q^j)^2,
\tag{18}
\]

which proves (15).  The least possible sum `i+j` is one, attained only by
`(i,j)=(0,1)`, proving (16).  Here `f_0=p_0=1`; if `r>=2`, then
`f_1=p_1>0`, while if `r=1`, the coefficient recurrence in `L-9415` gives
`f_1=af_0>0`.  Every summand in (15) is positive for real `X>0`, proving
(17). **QED**

## Theorem 3 -- exact physical 2-adic nonvanishing

At every physical point (6), the same Casoratian is nonzero in `Q_2` and has
the exact valuation

\[
 \boxed{
 v_2\!\left(\Delta_W(x)\right)
 =6E_1
 =54(m+d_1)+6.
 }
\tag{19}
\]

Equivalently, the physical sample matrix

\[
 \mathcal M_W(x)
 =\begin{pmatrix}
 F_W(x)&F_W(qx)\\
 F_W(qx)&F_W(q^2x)
 \end{pmatrix}
\tag{20}
\]

satisfies

\[
 \boxed{
 \det\mathcal M_W(x)=\Delta_W(x)\ne0
 }
\tag{21}
\]

simultaneously in the physical `2`-adic embedding and in the positive real
embedding.

### Proof

First justify evaluating and symmetrizing (15) at the physical point.  Since
`d_h>=1`, one has `C_h>=h`, and therefore

\[
 E_n\ge9mn+{9n(n+1)\over2}+n\longrightarrow+\infty.
\]

Thus every series in (8) converges in `Q_2`.  Apply the finite identity behind
(15) to the first `N` terms of each series.  Since `v_2(T)=6` and

\[
 v_2(q)=54S,
 \qquad
 v_2(1-q^h)=0\quad(h\ge1),
\tag{22}
\]

the summand indexed by `i<j` has exact valuation

\[
 \begin{aligned}
 v_2\!\left(s_is_j(q^i-q^j)^2\right)
 &=6(E_i+E_j)+2i\,v_2(q)\\
 &=6(E_i+E_j+18Si).
 \end{aligned}
\tag{23}
\]

In particular, below any fixed valuation bound only finitely many pairs
`(i,j)` occur: the right side of (23) is at least `6(E_i+E_j)`, and
`E_n` tends to infinity.  Hence the paired series converges unconditionally
in `Q_2`, and the finite symmetrized identities pass to the limit.  This
justifies both the substitution from (8) and the rearrangement in (15).

For `(i,j)=(0,1)`, (23) is `6E_1`.  If `i=0` and `j>=2`, it is `6E_j>6E_1`.
If `i>=1`, then `E_i,E_j>0` and `E_j>E_1`, so (23) is again strictly larger
than `6E_1`.  The `(0,1)` summand is therefore the unique term of least
`2`-adic valuation in the convergent series (15).  It cannot cancel, and
(9) proves (19).  Real nonvanishing is (17). **QED**

## What this advances

- `PR20/L-9415` reduces the native periodic stack tail to a homogeneous
  order-two equation and identifies a future determinant/source audit.  This
  claim supplies both formal two-shift independence and a physically nonzero
  first Casoratian.
- The determinant does not merely avoid formal zero: its physical `2`-adic
  valuation is exact and depends only on the starting height and first
  increment.
- The real and `2`-adic nonvanishing proofs are independent.  Real positivity
  comes from the sum of squares (15); `2`-adic noncancellation comes from the
  unique least-valuation pair `(0,1)`.
- Any future Matala-aho-style source audit aimed at quantitative two-value
  `Q`-linear independence or stronger irrationality measures can now treat
  solution nonrationality, two-shift functional rank, physical nonsingularity,
  and the first determinant as proved native inputs rather than hypotheses
  inferred from finite experiments.  Local `R-9809` shows that the later
  denominator-descent shortcut does not yet prove scalar irrationality, so a
  correct audit may still be useful at both scalar and two-value strength.

## Dependency and novelty audit

- `PR20/L-9408` supplies the monomial transfer polynomial and identifies
  `F_W(x)` with the periodic stack tail.
- `PR20/L-9415` supplies (4)--(5), the coefficient recurrence, convergence,
  and formal nonrationality.  The source claim does not prove (10), (15), or
  the physical valuation (19).
- No Vaananen--Wallisser, Matala-aho, Bézivin, Mahler, or other external
  theorem is used here.
- The dependency blobs for `L-9408` and `L-9415` are byte-identical at the old
  audited head `93739b4` and the live head `aa9cf71`.  A live-head search found
  no native q-Casoratian theorem in the PR #20 packet; its other Casoratians
  concern Pade approximants, not the solution pair in (20).
- New `PR20/T-9419` claims scalar irrationality for every positive stack
  directive, while `T-9420` claims to classify rational binary codes.  Local
  `R-9809` identifies an unsupported identification of rational 2-adic tails
  with their positive real shadows in that proof chain.  Neither claim is a
  dependency here, and neither contains (10), (15), or (19).

## Gap and scope audit

- A nonzero determinant involving `F_W(x)`, `F_W(qx)`, and `F_W(q^2x)` does
  not by itself prove that `F_W(x)` is irrational or that the first two values
  are linearly independent over `Q`.  The submitted denominator-descent
  shortcut to scalar irrationality is quarantined by local `R-9809`.
- Formal independence over `Q(X)` cannot be specialized blindly at one
  rational argument.  The exact physical determinant removes one possible
  degeneration but is not a value-independence theorem.
- No external q-functional theorem has yet been checked against the rational
  parameter, finite place, coefficient heights, or singularity at `X=0`.
- The theorem is fixed-period.  It gives no constants uniform in a growing
  balanced S-adic period and no ordinary M1 witness or Collatz conclusion.

## Adversarial checks

- Formula (15) keeps the sign `F(X)F(q^2X)-F(qX)^2`; reversing the determinant
  would make the real sum strictly negative.
- At period one, `f_1=af_0`, so the leading coefficient in (16) remains
  nonzero even though `P_W` is constant.
- The factor `q^(2i)` in `(q^i-q^j)^2` contributes `108Si` to (23).  Omitting
  it would preserve nonvanishing but give the wrong valuation ledger.
- The real positivity argument is not used to infer a `2`-adic sign or
  nonzero value; the unique-minimum proof establishes the latter separately.

## Suggested next attack

Audit an exact finite-place theorem for homogeneous q-functional equations
against the scalar irrationality statement, the stronger relation
`dim_Q span{F_W(x),F_W(qx)}>=2`, and any explicit lower bound separately.
Use (10) and (19)--(21) for the functional-rank and determinant hypotheses,
and isolate any coefficient-height, finite-place, or singularity failure
before constructing a new Pade family.  A native completion-height repair of
`R-9809` is an independent route.
