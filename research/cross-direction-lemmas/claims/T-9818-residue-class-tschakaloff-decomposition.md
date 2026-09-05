# T-9818 -- Residue phases are formally independent, but the 2007 joint height window closes at two

Claim ID: `T-9818`
Title: Every periodic stack tail splits into distinct-orbit scalar Tschakaloff values with an exact multi-value source obstruction
Status: `PROPOSED / SOURCE-DEPENDENT`
Authoring agent: `gpt56-synthesis-01-wave14-period-ten`
Reviewing agents: `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `T-9815`; branch-qualified `PR20/L-9408`, `L-9410`, `L-9412`, `L-9413`, and `L-9415` at `14f06d252c3ef56fb9a69ea34c61edaa578d02a1`
Scope: every positive periodic stack word, every physical starting height, and every subset of its residue phases
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Let

\[
 W=d_1\cdots d_r,\qquad
 r\geq1,\qquad
 S=\sum_{i=1}^r d_i,
\tag{1}
\]

and use the transfer data of `PR20/L-9408`:

\[
 T={64\over81},\qquad
 q=T^{9S},\qquad
 c=T^{e(W)},\qquad
 P(X)=\sum_{j=0}^{r-1}p_jX^j,
\tag{2}
\]

where every `p_j` is a nonzero positive rational number and `p_0=1`.  The
native function of `PR20/L-9415` obeys

\[
 \boxed{F(X)=P(X)+cX^rF(qX)}.
\tag{3}
\]

At a physical starting height `m>=0`, put

\[
 x=T^{9m},\qquad
 y=x^r,\qquad
 Q=q^r.
\tag{4}
\]

Define the standard Tschakaloff function for the common base `Q` by

\[
 E_Q(Z)=\sum_{k\geq0}Q^{k(k-1)/2}Z^k.
\tag{5}
\]

It satisfies

\[
 E_Q(Z)=1+ZE_Q(QZ).
\tag{6}
\]

## Theorem 1 -- exact residue-class decomposition

For `0<=j<r` define

\[
 \lambda_j=cq^j,\qquad
 G_j(Y)=E_Q(\lambda_jY),\qquad
 \beta_j=\lambda_jy=cq^jx^r.
\tag{7}
\]

Then

\[
 \boxed{
 F(X)=\sum_{j=0}^{r-1}p_jX^jG_j(X^r)
 =\sum_{j=0}^{r-1}p_jX^jE_Q(cq^jX^r).
 }
\tag{8}
\]

In particular, with

\[
 a_j=p_jx^j\in\mathbf Q_{>0},
 \qquad
 V_j=E_Q(\beta_j),
\tag{9}
\]

the physical value is

\[
 \boxed{F(x)=\sum_{j=0}^{r-1}a_jV_j.}
\tag{10}
\]

The arguments occupy pairwise distinct multiplicative `Q`-orbits:

\[
 i\ne j
 \quad\Longrightarrow\quad
 {\beta_i\over\beta_j}=q^{i-j}\notin Q^{\mathbf Z}.
\tag{11}
\]

### Proof

Write `F(X)=sum_(n>=0)f_nX^n`.  Equation (3) gives

\[
 f_j=p_j\quad(0\leq j<r),
 \qquad
 f_{n+r}=cq^nf_n\quad(n\geq0).
\tag{12}
\]

Thus

\[
 f_{j+kr}
 =p_jc^kq^{kj+rk(k-1)/2}.
\tag{13}
\]

Grouping the power series by `n mod r` and using `Q=q^r` proves (8).  If the
ratio in (11) were `Q^n=q^{rn}`, then `q^{i-j-rn}=1`.  The rational number
`0<q<1` is not a root of unity, so `i-j=rn`.  Since `|i-j|<r`, this forces
`i=j`, a contradiction. **QED**

## Theorem 2 -- full formal independence of the residue functions

For every nonempty subset \(J\subseteq\{0,\ldots,r-1\}\),

\[
 \boxed{
 1,\quad G_j(Y)\ (j\in J)
 \text{ are linearly independent over }\mathbf Q(Y).
 }
\tag{14}
\]

### Proof

Suppose a rational-function relation exists.  After clearing denominators,
write it as

\[
 A_0(Y)+\sum_{j\in J}A_j(Y)G_j(Y)=0,
 \qquad A_0,A_j\in\mathbf Q[Y].
\tag{15}
\]

Choose `D` at least the degree of every `A_j` and write

\[
 A_j(Y)=\sum_{\ell=0}^D a_{j,\ell}Y^\ell.
\tag{16}
\]

For every sufficiently large `n`, the coefficient of `Y^n` in (15), divided
by the nonzero factor `Q^{n(n-1)/2}`, is

\[
 \sum_{j\in J}\sum_{\ell=0}^D
 a_{j,\ell}\lambda_j^{-\ell}Q^{\ell(\ell+1)/2}
 \left(\lambda_jQ^{-\ell}\right)^n
 =0.
\tag{17}
\]

All exponential bases in (17) are distinct.  Indeed,

\[
 \lambda_jQ^{-\ell}=\lambda_iQ^{-k}
 \quad\Longrightarrow\quad
 q^{j-i-r(\ell-k)}=1,
\tag{18}
\]

and the same residue argument as in (11) gives `j=i` and `ell=k`.  Taking as
many consecutive values of `n` as there are pairs `(j,ell)` produces a
Vandermonde matrix with nonzero determinant.  Hence every coefficient in
(17) vanishes, so every `A_j` vanishes.  Equation (15) then gives `A_0=0`.
**QED**

## Theorem 3 -- every individual physical phase has an explicit measure

Put

\[
 \gamma={2\over3}\log_2 3,\qquad
 \beta_*={2\sqrt{2086}-7\over79},\qquad
 \mu_*={\beta_*\over\beta_*-\gamma}
 =96.8590845\ldots.
\tag{19}
\]

For every `j`, the two numbers

\[
 \boxed{1,\ V_j}
\tag{20}
\]

are linearly independent over \(\mathbf Q\).  More precisely, there are
constants `C_j,D_j,H_j>0` such that every nonzero
\((u_0,u_1)\in\mathbf Q^2\) satisfies

\[
 |u_0+u_1V_j|_2
 >
 C_jH^{-\mu_*-D_j/\sqrt{\log H}},
 \qquad
 H=\max\{H(u_0,u_1),H_j\},
\tag{21}
\]

where `H(u_0,u_1)` is the affine multiplicative Weil height.

### Exact source audit

Theorem 5.1 of

> M. Amou, T. Matala-aho and K. Vaananen, "On Siegel-Shidlovskii's theory
> for q-difference equations," *Acta Arith.* **127** (2007), 309--335,
> DOI: [10.4064/aa127-4-2](https://doi.org/10.4064/aa127-4-2)

applies to the scalar equation

\[
 YG_j(QY)
 =\lambda_j^{-1}G_j(Y)-\lambda_j^{-1}.
\tag{22}
\]

In the source notation this has vector dimension `1`, singular exponent
`s=1`, polynomial `a(Y)=1`, invertible constant matrix
`C=(lambda_j^{-1})`, and constant inhomogeneous term
`b=(-lambda_j^{-1})`.  The orbit condition is automatic because `a=1`, and
formal independence is Theorem 2.  Moreover, the coefficient of `Y^n` in
`G_j` is `Q^{n(n-1)/2}lambda_j^n`.  Its 2-adic valuation tends to positive
infinity quadratically, so `G_j` is analytic near zero (indeed, 2-adically
entire).

The common base has

\[
 Q={2^{54Sr}\over3^{36Sr}},\qquad
 H(Q)=3^{36Sr},\qquad
 |Q|_2=2^{-54Sr}.
\tag{23}
\]

Consequently the source height ratio is

\[
 \lambda_{\rm src}
 ={\log H(Q)\over\log|Q|_2}
 =-\gamma.
\tag{24}
\]

Taking the source parameter `delta=1/2` gives exactly the constants audited in
`T-9815`, including

\[
 \beta_*>{16\over15}>\gamma.
\tag{25}
\]

Thus the source inequality `-beta_*<lambda_src<=-1` holds, and its displayed
lower bound gives (20)--(21). **QED**

## Theorem 4 -- exact obstruction for every joint vector

Let `J` contain `k>=2` residue indices and put

\[
 \mathbf G_J(Y)=(G_j(Y))_{j\in J}.
\tag{26}
\]

The vector satisfies an exact source-form equation

\[
 Y\mathbf G_J(QY)
 =C_J\mathbf G_J(Y)+\mathbf b_J,
\tag{27}
\]

where

\[
 C_J=\operatorname{diag}(\lambda_j^{-1})_{j\in J},
 \qquad
 \mathbf b_J=-C_J\mathbf 1.
\tag{28}
\]

All algebraic, analytic, orbit, and formal-independence hypotheses of the 2007
theorem hold.  Nevertheless, its numerical height window fails for every
`k>=2` and every allowed choice of its auxiliary parameter.

### Proof of the source obstruction

Write the source auxiliary parameter as `epsilon` and put

\[
 0<\epsilon<1,\qquad w=1-\epsilon.
\tag{29}
\]

For source dimension `k` and singular exponent `s=1`, its constant is

\[
 K_\epsilon
 ={k^2\over2}+{(k+w)^3-k^3\over6(1-w)}
 ={3k^2+3kw^2+w^3\over6(1-w)}.
\tag{30}
\]

At the source's positive root `rho_0`, define

\[
 \mathcal A={\rho_0^2\over2}+k\rho_0+K_\epsilon,
 \qquad
 \mathcal B={\rho_0^2\over2}+(k+w)\rho_0.
\tag{31}
\]

The source notes \(\mathcal B>\mathcal A\).  Therefore

\[
 \Delta=\mathcal B-\mathcal A=w\rho_0-K_\epsilon>0,
 \qquad
 \rho_0={\Delta+K_\epsilon\over w}.
\tag{32}
\]

Using \(\mathcal A\geq\rho_0^2/2\) and AM--GM,

\[
 {\Delta\over\mathcal A}
 \leq
 {2\Delta w^2\over(\Delta+K_\epsilon)^2}
 \leq
 {w^2\over2K_\epsilon}.
\tag{33}
\]

For `k>=2`,

\[
 K_\epsilon
 \geq {k^2\over2(1-w)}
 \geq {2\over1-w}
 >9w^2.
\tag{34}
\]

The last inequality is uniform because

\[
 \max_{0\leq w\leq1}w^2(1-w)={4\over27}
 \quad\Longrightarrow\quad
 9w^2(1-w)\leq{4\over3}<2.
\tag{35}
\]

Equations (33)--(35) give

\[
 {\mathcal B\over\mathcal A}
 =1+{\Delta\over\mathcal A}
 <{19\over18}.
\tag{36}
\]

On the other hand,

\[
 3^{12}>2^{19}
 \quad\Longrightarrow\quad
 \gamma={2\over3}\log_2 3>{19\over18}.
\tag{37}
\]

The source condition

\[
 -{\mathcal B\over\mathcal A}
 <\lambda_{\rm src}=-\gamma
\tag{38}
\]

is therefore false.  Thus this theorem gives no joint arithmetic independence
or joint measure for even two residue values.  The failure is solely the
height window: Theorem 2 supplies the formal-independence hypothesis, and all
other hypotheses were verified above. **QED**

## The exact remaining cancellation space

The native equation at the physical point gives

\[
 F(qx)={F(x)-P(x)\over cy}.
\tag{39}
\]

Hence, for rational `u,v`,

\[
 uF(x)+vF(qx)
 =
 \left(u+{v\over cy}\right)F(x)
 -{vP(x)\over cy}.
\tag{40}
\]

Since `c,y,P(x)` are nonzero rationals, the coefficient transformation in
(40) is invertible.  Consequently

\[
 \boxed{
 \{F(x),F(qx)\}\text{ are linearly independent over }\mathbf Q
 \iff
 F(x)\notin\mathbf Q.
 }
\tag{41}
\]

By (10), hypothetical rationality of `F(x)` is exactly the prescribed
cross-phase cancellation

\[
 R+\sum_{j=0}^{r-1}a_jV_j=0
\quad\text{for some }R\in\mathbf Q,
\qquad a_j\ne0\text{ for every }j.
\tag{42}
\]

The scalar measures (21) rule out a cancellation involving only one phase,
but they do not rule out (42).  Formal independence in Theorem 2 cannot be
specialized blindly at `Y=y`.

The existing Vaananen--Wallisser interface in `PR20/L-9412` sharpens the
current repo boundary.  It proves that `1` and any at most nine of the distinct
orbit values `V_j` are arithmetically independent.  Therefore:

\[
 \boxed{
 \text{every nontrivial arithmetic relation among }1,V_0,\ldots,V_{r-1}
 \text{ has at least ten nonzero phase coefficients.}
 }
\tag{43}
\]

For a word of minimal period `r<=9`, no cancellation (42) exists; this is the
already-recorded conclusion of `PR20/T-9417`.  For minimal period `r>=10`,
(43) is the exact present sparse-support boundary.  The 2007 theorem audited
here cannot improve it because its joint condition already fails at two.

## Dependency and novelty audit

- `PR20/L-9410` already records the physical phase decomposition in its
  variables `R=Q`, `Z=cy`, and `lambda=q`.  Equations (8)--(10) rederive it
  directly from the native coefficient recurrence; the decomposition itself
  is not claimed as new.
- `PR20/L-9413` already proves each individual phase irrational using a native
  q-binomial Pade family.  The new source contribution in Theorem 3 is the
  audited 2007 linear-form bound with the explicit exponent `mu_*`.
- `PR20/L-9412` and `T-9417` already give joint arithmetic independence through
  nine phases.  Equation (43) restates their exact implication for the
  cancellation support; it is not a new period-nine theorem.
- The new native result is Theorem 2: formal independence of the full
  arbitrary-period residue vector by an elementary coefficient/Vandermonde
  argument.
- The new source audit is Theorem 4: despite that full formal independence,
  the 2007 theorem's joint numerical condition fails for every subset of two
  or more phases and every auxiliary parameter.
- At `r=1`, the decomposition has one component and recovers `T-9815`.
  `T-9812` concerns the two native shifts and their physical Casoratian, not
  the `r`-component arithmetic phase vector.
- A live-head search at `14f06d2` found neither the formal Vandermonde theorem
  (14) nor the all-parameter 2007 obstruction (29)--(38).

## Gap and scope audit

- Individual irrationality never implies irrationality of their rational
  linear combination.  No such inference is made.
- The physical values may satisfy arithmetic relations even though their
  defining functions are independent over `Q(Y)`.
- Failure of one source theorem is not evidence that a joint relation exists.
  It identifies the first failed hypothesis and the exact missing
  height/vanishing gain.
- If `W` is displayed as a power of a shorter word, reduce it to its minimal
  period before interpreting the dimension of the cancellation space.  The
  displayed-period formulas remain algebraically valid.
- The scalar and joint constants are fixed-period.  They are not uniform in a
  growing S-adic period.
- No conclusion is drawn for the balanced nonperiodic directive, the full M1
  section, or the Collatz conjecture.

## Adversarial checks

- In (13), each recurrence step contributes `q^(j+kr)`.  Summing over
  `k` gives `kj+rk(k-1)/2`; replacing the latter by `rk(k+1)/2` would shift
  every phase incorrectly.
- In (17), multiplying by `Y^ell` produces the base
  `lambda_j Q^(-ell)` and the prefactor `Q^(ell(ell+1)/2)`.  These signs are
  load-bearing for the distinct-base argument.
- Distinct physical arguments are not enough by themselves; (18) checks the
  stronger condition needed by both the Vandermonde proof and the source
  orbit language.
- The source dimension in Theorem 4 is the number `k` of selected phases, not
  the displayed word length `r`.  Thus the obstruction really begins with
  every two-phase subset.
- The auxiliary `epsilon` in (29) belongs to the 2007 theorem and is unrelated
  to the support-gap slope called `delta` in `T-9816`.
- Positivity of the rational weights `a_j` is never used to infer arithmetic
  noncancellation.

## Reproducibility record

The primary 2007 PDF audited in `T-9815` has SHA-256

`71B1F76747DCCA9A10F334D25416766936C58D1A767690B62D5ABF0A7130207A`.

The relevant source formulas are equation (5.1), definitions (5.2)--(5.3),
condition (5.4), and Theorem 5.1 on printed pages 318--320.

## Suggested next attack

For minimal period at least ten, target the prescribed coefficient vector
`(a_0,...,a_(r-1))` rather than full phase independence.  A useful new
construction must couple at least ten phases and beat the height ratio
`gamma=(2/3)log_2 3`; separate scalar approximants cannot prevent (42).
