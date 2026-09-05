# T-9815 -- Period-one native stack values have an explicit 2-adic linear-independence measure

Claim ID: `T-9815`
Title: Every one-letter periodic stack tail and its first q-shift are Q-linearly independent, with an explicit finite-place measure
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-period-ten`
Reviewing agents: `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `T-9812`; branch-qualified `PR20/L-9408` (blob `b3e09ca76b5edea808b4c7b6c10730f7e48cb183`) and `L-9415` (blob `c53fb954c5b8a7ac111d11aff4737bd886797b98`) at `14f06d252c3ef56fb9a69ea34c61edaa578d02a1`
Scope: every one-letter positive periodic stack word and every physical starting height
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Let the periodic increment word be the single letter

\[
 W=(d),\qquad d\geq 1,
\tag{1}
\]

and put

\[
 T={64\over81},\qquad
 q=T^{9d},\qquad
 c=T^{1+9d}.
\tag{2}
\]

The one-letter case of `PR20/L-9408` has `P_W(X)=1`.  Hence the native
function of `PR20/L-9415` satisfies

\[
 \boxed{F(X)=1+cX F(qX)}.
\tag{3}
\]

At every physical starting height `h>=0`, set

\[
 x=T^{9h}\in\mathbf Q^*.
\tag{4}
\]

`T-9812` proves the relevant formal nonrationality/rank statement and also the
nonvanishing of the physical solution Casoratian.  The value theorem used
below needs the former; its approximation determinant is not the Casoratian
from `T-9812`.

## Exact source theorem

We use Theorem 5.1 of

> M. Amou, T. Matala-aho and K. Vaananen, "On Siegel-Shidlovskii's theory
> for q-difference equations," *Acta Arith.* **127** (2007), 309--335,
> DOI: [10.4064/aa127-4-2](https://doi.org/10.4064/aa127-4-2).

The source studies the vector equation

\[
 z^s\mathbf f(qz)=a(z)C\mathbf f(z)+\mathbf b(z),
\tag{5}
\]

where `a(0)!=0`, `deg a<=s`, `deg b<=s`, and `C` is an invertible constant
matrix.  For a number field `K`, a place `v`, and `|q|_v<1`, it defines

\[
 \lambda={\log H(q)\over\log\lVert q\rVert_v}\leq-1.
\tag{6}
\]

Choose `0<delta<1`.  If the source vector dimension is `m`, define

\[
 \begin{aligned}
 K_\delta&={m^2\over2}+{(m+1-\delta)^3-m^3\over6\delta},\\
 A(\rho)&={s\rho^2\over2}+m\rho+K_\delta,\\
 B(\rho)&={s\rho^2\over2}+(m+1-\delta)\rho,
 \end{aligned}
\tag{7}
\]

and let `rho_0` be the positive root of

\[
 s(1-\delta)\rho^2+
 \{s(1-\delta)\delta m-2sK_\delta\}\rho
 -\{s\delta m+2(m+1-\delta)\}K_\delta=0.
\tag{8}
\]

If `1,f_1,...,f_m` are independent over `K(z)`, the evaluation orbit is
nonsingular, and

\[
 -{B(\rho_0)\over A(\rho_0)}<\lambda\leq-1,
\tag{9}
\]

then `1,f_1(alpha),...,f_m(alpha)` are independent over `K`.  More precisely,
with

\[
 \mu={B(\rho_0)\over B(\rho_0)+\lambda A(\rho_0)},
\tag{10}
\]

the source gives constants `C_0,D,H_0>0` such that every nonzero coefficient
vector obeys its displayed lower bound (5.5).  Over `K=Q` at `v=2`, this is

\[
 |u_0+u_1f_1(\alpha)|_2
 > C_0 H^{-\mu-D/\sqrt{\log H}},
 \qquad
 H=\max\{H(u_0,u_1),H_0\}.
\tag{11}
\]

Here the source uses the affine multiplicative height; over `Q`,

\[
 H(u_0,u_1)=\prod_w\max\{1,|u_0|_w,|u_1|_w\}.
\tag{11a}
\]

The official source PDF was checked at printed pages 318--320, including the
definitions (5.2)--(5.4) and the lower bound (5.5).

## Theorem 1 -- exact hypothesis audit at period one

Equation (3) is exactly (5) with

\[
 \mathbf K=\mathbf Q,\quad v=2,\quad m=1,\quad s=1,
 \quad a(z)=1,\quad C=(c^{-1}),\quad b(z)=(-c^{-1}).
\tag{12}
\]

Every source hypothesis holds.

1. **Coefficient restrictions.**  The polynomial `a(z)=1` has nonzero
   constant term and degree zero, `b(z)` has degree zero, and `C` is
   invertible.
2. **Analytic solution.**  Iterating (3) gives
   \[
   F(X)=\sum_{n\geq0}c^nq^{n(n-1)/2}X^n.
   \tag{13}
   \]
   Since `v_2(c)>0` and `v_2(q)>0`, its coefficients tend to zero
   quadratically in valuation; it is analytic in a neighbourhood of zero in
   `Q_2` (indeed, it is 2-adically entire).
3. **Functional independence.**  `F` is not in `Q(X)` by `PR20/L-9415`
   (and is used in the formal-rank proof of `T-9812`).  Thus `1,F(X)` are
   independent over `Q(X)`.
4. **Evaluation orbit.**  The source singularity condition is
   `a(xq^k)!=0`; here it is identically one.  Also `x` is nonzero rational.
5. **Finite place and exact height ratio.**  In lowest terms,
   \[
   q={2^{54d}\over3^{36d}},\qquad
   H(q)=3^{36d},\qquad |q|_2=2^{-54d}.
   \tag{14}
   \]
   Therefore
   \[
   \lambda=-\gamma,
   \qquad
   \gamma={2\over3}\log_2 3.
   \tag{15}
   \]

It remains only to check (9).  Take `delta=1/2`.  Equations (7)--(8) give

\[
 K_\delta={31\over24},\qquad
 24\rho_0^2-112\rho_0-217=0,
 \qquad
 \rho_0={28+\sqrt{2086}\over12}.
\tag{16}
\]

Writing

\[
 \beta={B(\rho_0)\over A(\rho_0)},
\tag{17}
\]

exact simplification gives

\[
 \boxed{\beta={2\sqrt{2086}-7\over79}}.
\tag{18}
\]

The comparison with the height ratio is exact:

\[
 \beta>{16\over15}>\gamma.
\tag{19}
\]

For the first inequality, after clearing positive denominators it is enough
that `30*sqrt(2086)>1369`, whose square is
`1,877,400>1,874,161`.  For the second,

\[
 3^5=243<256=2^8
 \quad\Longrightarrow\quad
 {2\over3}\log_2 3<{16\over15}.
\tag{20}
\]

Also `gamma>1` (equivalently `9>8`).  Hence

\[
 -\beta<\lambda=-\gamma\leq-1,
\tag{21}
\]

which proves the final source hypothesis. **QED**

## Theorem 2 -- value independence and explicit measure

For every `d>=1` and `h>=0`,

\[
 \boxed{1,F(x)\text{ are linearly independent over }\mathbf Q.}
\tag{22}
\]

The source exponent can be written explicitly as

\[
 \boxed{
 \mu={\beta\over\beta-\gamma},\qquad
 \beta={2\sqrt{2086}-7\over79},\qquad
 \gamma={2\over3}\log_2 3,
 }
\tag{23}
\]

so `mu=96.8590845...`.  In particular, constants depending on `d` and `h`
exist for which (11) holds with `f_1(alpha)=F(x)` and this explicit `mu`.

Moreover, (3) gives

\[
 F(qx)={F(x)-1\over cx}.
\tag{24}
\]

For rational `u,v`,

\[
 uF(x)+vF(qx)
 =-{v\over cx}+\left(u+{v\over cx}\right)F(x).
\tag{25}
\]

The map

\[
 (u,v)\longmapsto
 \left(-{v\over cx},\ u+{v\over cx}\right)
\tag{26}
\]

is an invertible rational linear map.  Therefore (22) and the source height
bound imply

\[
 \boxed{
 \dim_{\mathbf Q}\operatorname{span}_{\mathbf Q}
 \{F(x),F(qx)\}=2.
 }
\tag{27}
\]

Here is the height transfer explicitly.  Let `M_x` denote the fixed invertible
rational matrix in (26).  The local triangle inequality and the product
formula give a constant `C_x>=1` such that

\[
 H(M_x(u,v)^t)\leq C_x H(u,v)
\tag{28}
\]

for every rational pair.  After increasing the height cutoff, put
`H=max{H(u,v),H_1}`.  The height used on the right side of the source bound is
at most `C_x H`.  Since

\[
 Y^\mu Y^{D/\sqrt{\log Y}}
 =\exp\{\mu\log Y+D\sqrt{\log Y}\},
\tag{29}
\]

substituting `Y<=C_x H` changes this expression by at most a multiplicative
constant times `H^mu H^(D/sqrt(log H))`; use
`sqrt(log H+log C_x)<=sqrt(log H)+sqrt(log C_x)`.  Absorbing the fixed factor
into `C_0` transfers (11) to `uF(x)+vF(qx)` with the same `mu` (and even the
same secondary `D`, after changing the cutoff and leading constant).  Thus
(27) is quantitative, not merely qualitative. **QED**

## Why the same published criteria stop at longer period

The first-order equation remains useful for a word of length `r`:

\[
 z^rF(qz)=c^{-1}F(z)-c^{-1}P_W(z).
\tag{30}
\]

It has source vector dimension `m=1` and source singular exponent `s=r`.
However, Theorem 5.1's height window fails for every `r>=2`, for every choice
of `0<delta<1`.

Indeed, put `w=1-delta`.  For source dimension one,

\[
 K_\delta={w^3+3w^2+3\over6(1-w)}.
\tag{31}
\]

At the source root `rho_0`, the paper notes `B(rho_0)>A(rho_0)`.  Put

\[
 D=B(\rho_0)-A(\rho_0)=w\rho_0-K_\delta>0.
\tag{32}
\]

Since `A(rho_0)>=r*rho_0^2/2` and
`rho_0=(D+K_delta)/w`, AM--GM gives

\[
 {D\over A(\rho_0)}
 \leq {2Dw^2\over r(D+K_\delta)^2}
 \leq {w^2\over2rK_\delta}
 \leq {w^2\over4K_\delta}
 <{1\over18}.
\tag{33}
\]

The last strict inequality is equivalent to

\[
 28w^3-24w^2+3>0.
\tag{34}
\]

On `[0,1]` the polynomial has its interior minimum at `w=4/7`, where it is
`133/343>0`.  Consequently

\[
 {B(\rho_0)\over A(\rho_0)}<{19\over18}.
\tag{35}
\]

But

\[
 3^{12}=531441>524288=2^{19}
 \quad\Longrightarrow\quad
 \gamma={2\over3}\log_2 3>{19\over18}.
\tag{36}
\]

Thus `-B/A<lambda=-gamma` is false.  This is a rigorous obstruction to the
direct first-order application at every longer period; it is not a numerical
near miss.

The older homogeneous theorem advertised by `PR20/L-9415` also fails before
reaching a determinant hypothesis.  Theorem 4.1 of

> T. Matala-aho, "On Diophantine approximations of the solutions of
> q-functional equations," *Proc. Roy. Soc. Edinburgh Sect. A* **132**
> (2002), 639--659,
> DOI: [10.1017/S0308210500001827](https://doi.org/10.1017/S0308210500001827)

requires `B>A`, with `B=s/2`.  Mapping the homogeneous order-two equation of
`L-9415` gives

\[
 s=r,\quad
 M=cq^rP_W(z),\quad
 P_{0,1}=P_W(z)+cz^rP_W(qz),\quad
 P_{0,2}=-P_W(qz).
\tag{37}
\]

Before primitive-content cancellation the source degrees give

\[
 A=2r-1,\qquad B={r\over2},
\tag{38}
\]

so `B>A` is impossible.  This does not arise from an avoidable common factor.
Any common polynomial divisor is a divisor of both `P_W(z)` and `P_W(qz)`.
Its degree is at most `r-2` for `r>=2`: equality `r-1` would make the two
degree-`r-1` polynomials scalar multiples, and their common constant term one
would force equality, contrary to `q!=1` and the nonzero coefficients of
`P_W`.  After cancelling the maximal content, the source degree `r_1` is
therefore at least `r+1`; it still exceeds `B=r/2`.  At `r=1`, it is one and
again exceeds `B=1/2`.

Hence the 2002 homogeneous theorem yields neither qualitative independence
nor a measure here.  Its iterated approximation determinant is also a
different object from the physical solution Casoratian in `T-9812`; the latter
cannot repair the failed degree/height inequalities.

For completeness, the degree inequality is the first failed hypothesis, not
a proxy for several hidden failures:

- `T-9812` proves that `F(z),F(qz)` are independent over `Q(z)`, so the
  homogeneous equation really is of lowest order two.
- The fixed parameters `q,x` and all coefficient-polynomial entries are
  rational, and `|q|_2<1`.
- On the physical orbit, both source endpoint coefficients are nonzero:
  `M(q,q^kx)=cq^rP_W(q^kx)` and
  `P_(0,2)(q,q^kx)=-P_W(q^(k+1)x)`.  Positivity of every coefficient of
  `P_W` proves this in the real embedding, hence as rational nonvanishing.
- Every `F(q^n x)` is a 2-adic unit: its constant term is one and every
  remaining term has positive 2-adic valuation.  Thus the source exponential
  growth condition holds.  If the source convention for `N` includes zero
  and its strict inequality is read at `n=0`, replace the solution by `2F`;
  this preserves all independence questions and makes the strict bound hold
  there as well.
- The sampled values are therefore not all zero.

Even apart from the required global condition `B>A`, (15) and `lambda<-1`
give `B+lambda*A < B-A < 0`, so the source's second positivity condition also
fails.

## Dependency and novelty audit

- `PR20/L-9408` supplies `P_W`, and in particular `P_(d)=1`, `e(d)=1+9d`.
- `PR20/L-9415` supplies the native functional equation and formal
  nonrationality.  `T-9812` supplies the formal two-shift rank and exact
  physical Casoratian; no external value theorem was used there.
- The 2007 primary source supplies the new specialization theorem and lower
  bound.  Its hypotheses and constants are reproduced above rather than
  inferred from an abstract or secondary citation.
- At live `PR20` head `14f06d2`, new `R-9409` records the completion-limit
  mismatch and the source branch explicitly withdraws `T-9418`--`T-9421`.
  Those withdrawn claims are neither dependencies nor novelty blockers for
  (22)--(27).  The dependency blobs `L-9408` and `L-9415` are unchanged at the
  hashes recorded in the header.

## Gap and scope audit

- The theorem proved here is exactly period one.  Equations (33)--(36) show
  why this particular source theorem does not extend directly to `r>=2`.
- Splitting a longer-period series into residue classes produces several
  scalar Tschakaloff-type functions.  Separate irrationality of components
  would not rule out cancellation in their rational linear combination; a
  joint theorem is still required.
- No claim is made that every possible gauge transformation of the order-two
  system fails.  The direct primitive homogeneous presentation and the native
  first-order presentation are the two exact source audits above.
- The constants in the source bound depend on the fixed word and physical
  point.  Nothing here is uniform in a growing S-adic period.
- This is a value theorem for the periodic stack model, not an ordinary M1
  witness or a Collatz conclusion.

## Reproducibility record

The primary PDFs audited were the official journal copies:

- 2007 Acta Arithmetica PDF, SHA-256
  `71B1F76747DCCA9A10F334D25416766936C58D1A767690B62D5ABF0A7130207A`;
- 2002 Cambridge PDF, SHA-256
  `F93302E363110B188DCBAFB24E9970A52B855786741CE66130E59D54DBE15703`.

The decisive 2007 formulas occur on printed pages 318--320; the decisive
2002 degree condition and theorem occur on printed page 648.

## Suggested next attack

For `r>=2`, build a joint approximation family for the residue-class
components whose height/vanishing ratio beats the exact obstruction
`gamma=(2/3)log_2 3`.  The target is not another solution Casoratian -- that is
already nonzero by `T-9812` -- but a sequence of arithmetic approximation
determinants with a positive product-formula exponent.
