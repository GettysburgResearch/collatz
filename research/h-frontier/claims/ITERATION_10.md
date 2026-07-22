# Iteration 10: macro-growth, sharp deficit, and quantitative fresh-prime barriers

All theorem-level claims remain `PROPOSED` pending independent review.  This
iteration incorporates three useful interfaces from neighboring repository
programs:

1. the finite-control / one-unbounded-state discipline of PR #49;
2. the countable-IFS ordinary survivor bound and completion-height viewpoint;
3. the explicit Evertse--Schlickewei--Schmidt fresh-prime counting pattern used
   in PR #34.

No positive H counterexample and no proof of H termination is claimed.

Retain the exact normalized block system

\[
 x_{n+1}=m_{r_n}x_n+\frac14,
 \qquad
 m_r=\frac{3^{2r+1}}{2^{3r+2}},
 \qquad x_n=p_n/4\in\mathbb Z_{>0},
\tag{1}
\]

and the exact cores

\[
 p_n=2^{3r_n+2}u_n,
 \qquad
 2^{3r_{n+1}+2}u_{n+1}-3^{2r_n+1}u_n=1.
\tag{2}
\]

Let `rho` be the plastic constant, `rho^3=rho+1`, and put

\[
 \sigma=\log_2\rho=0.405685231\ldots .
\tag{3}
\]

The ordinary infinite-survivor count from `T-9506` is

\[
 A_{\mathcal I}(X)=O(X^\sigma).
\tag{4}
\]

---

## L-9526: polynomial macro-growth barrier

**Claim ID:** `L-9526`  
**Title:** A physical finite-macro construction needs sufficiently fast positive-cycle growth  
**Status:** `PROPOSED`  
**Dependencies:** `T-9506`; exact affine macro composition  
**Scope:** actual positive exact H orbits sampled at macro boundaries

### Statement

Let an actual exact orbit be sampled at times

\[
 0=n_0<n_1<n_2<\cdots,
\]

and suppose the segment from `n_k` to `n_(k+1)` is one of a finite family of
nonempty exact macro words.  Write the induced recurrence

\[
 x_{k+1}=a_kx_k+b_k,
 \qquad a_k>0,\quad b_k>0,
\tag{5}
\]

where the pairs `(a_k,b_k)` range over a finite set.  For `j<k`, put

\[
 A_{j,k}=\prod_{i=j}^{k-1}a_i.
\tag{6}
\]

Assume that for some constants `C>=1` and `gamma>=0`, every suffix multiplier
obeys

\[
 \boxed{
 A_{j,k}\le C(1+k-j)^\gamma
 \qquad(0\le j<k).
 }
\tag{7}
\]

If the orbit is nonperiodic, then necessarily

\[
 \boxed{
 \gamma\ge\frac1\sigma-1
 =1.464965255\ldots .
 }
\tag{8}
\]

In particular, a finite directed macro grammar in which every directed cycle
has multiplier product at most one cannot carry a nonperiodic positive exact
H orbit.

More generally, every physical finite-macro counterexample must exploit
positive-multiplier cycles often enough that its suffix products violate every
bound (7) with `gamma<1/sigma-1`.

### Proof

Unrolling (5) gives

\[
 x_k=A_{0,k}x_0+
 \sum_{j=0}^{k-1}b_jA_{j+1,k}.
\tag{9}
\]

Let `b_*` be the maximum macro intercept.  Equation (7) implies

\[
 x_k
 \le C(1+k)^\gamma x_0
 +Cb_*\sum_{m=0}^{k-1}(1+m)^\gamma
 =O(k^{\gamma+1}).
\tag{10}
\]

If two sampled states were equal, determinism of the exact map would make the
orbit eventually periodic.  Hence a nonperiodic orbit gives `k+1` distinct
members of the infinite-survivor set below `O(k^(gamma+1))`.  By (4),

\[
 k+1
 \le O\!\left(k^{\sigma(\gamma+1)}\right).
\tag{11}
\]

This is impossible when `sigma(gamma+1)<1`, proving (8).

For the graph corollary, take any finite path segment and delete directed
cycles until a simple path remains.  Every deleted cycle has multiplier at
most one, while the products of the finitely many simple paths have a common
upper bound.  Thus (7) holds with `gamma=0`, contradicting (8).  QED.

### Significance for construction

This theorem is the exact H analogue of the repository's finite-control
warnings.  A finite macro grammar is not automatically impossible, but it must
contain a positive multiplier cycle and the physical path must use positive
cycles with quantitatively unbounded frequency.  A bounded phase rotation,
a neutral compiler, or a finite graph with only nonpositive cycle means cannot
be repaired by abstract 2-adic tail freedom.

---

## T-9516: quantitative renewal prime budget

**Claim ID:** `T-9516`  
**Title:** A nonperiodic H survivor needs logarithmically many distinct bridge primes  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Dependencies:** `L-9520`, `T-9513`; quantitative Evertse--Schlickewei--Schmidt Theorem 1.1  
**Scope:** finite initial segments of the renewal sequence of a hypothetical nonperiodic survivor

### Setup

At an interior renewal use

\[
 a=L_{k-1},\qquad b=L_k,\qquad R=R_k,
 \qquad X=W_{k-1},\qquad Y=W_k.
\]

The exact normalized compatibility equation is

\[
 \boxed{
 -4^bY+3^a(9/8)^RX+(9/8)^R=1.
 }
\tag{12}
\]

All `X,Y` are positive and coprime to six.  For the first `N` interior
renewals, let

\[
 \mathcal S_N
 =\{q\ge5\text{ prime}:q\mid X_kY_k\text{ for some }1\le k\le N\},
 \qquad s_N=|\mathcal S_N|.
\tag{13}
\]

### Statement

Put

\[
 C_3=18^9.
\tag{14}
\]

Then

\[
 \boxed{
 N\le\exp\!\left(C_3(2s_N+4)\right).
 }
\tag{15}
\]

Consequently

\[
 \boxed{
 s_N\ge
 \max\left\{0,
 \left\lceil\frac{C_3^{-1}\log N-4}{2}\right\rceil
 \right\}.
 }
\tag{16}
\]

In threshold form, for every integer `Q>=0`,

\[
 N>\exp(C_3(2Q+4))
 \quad\Longrightarrow\quad s_N\ge Q+1.
\tag{17}
\]

Thus the qualitative infinite-prime-support theorem has an explicit, although
extremely weak, logarithmic rate.

### Proof

For each renewal define

\[
 z_1=-4^bY,
 \qquad z_2=3^a(9/8)^RX,
 \qquad z_3=(9/8)^R.
\tag{18}
\]

These solve `z_1+z_2+z_3=1`.  They lie in the subgroup of
`(Q^*)^3` generated by

\[
 (4,1,1),\quad(1,3,1),\quad(1,9/8,9/8),
\tag{19}
\]

and, for each `q in S_N`,

\[
 (q,1,1),\qquad(1,q,1),
\tag{20}
\]

plus the torsion sign.  Hence the group rank is at most

\[
 2s_N+3.
\tag{21}
\]

The solution is nondegenerate.  The two positive coordinates cannot cancel.
Equality of the negative coordinate with either positive coordinate would
contradict their 2-adic valuations: the negative term has valuation `2b>0`,
whereas each term containing `(9/8)^R` has valuation `-3R<0`.

Different interior renewals on a nonperiodic chain give different solutions:
`z_3` recovers `R`; the 2-adic valuation and value of `z_1` recover `b,Y`; the
3-adic valuation and value of `z_2` recover `a,X`; the central equation then
recovers `U` and the exact state.  Repetition would make the deterministic
orbit periodic.

The quantitative Evertse--Schlickewei--Schmidt bound for a nondegenerate
three-term equation in a rank-`r` subgroup is

\[
 \exp\!\left((6\cdot3)^{3\cdot3}(r+1)\right)
 =\exp(18^9(r+1)).
\tag{22}
\]

Insert `r<=2s_N+3` to obtain (15), and rearrange for (16)--(17).  QED.

### Source audit

The numerical constant in (22) is the explicit form of Theorem 1.1 of
Evertse--Schlickewei--Schmidt (Annals of Mathematics 155 (2002), 807--836),
already imported and source-audited in the repository literature / PR #34
layer.  Independent review should verify that the native rank and distinctness
arguments above match that source's exact group convention.

---

## T-9517: asymptotically sharp rounded-deficit pressure

**Claim ID:** `T-9517`  
**Title:** Harmonic summability raises the deficit baseline to the exact critical constant  
**Status:** `PROPOSED`  
**Dependencies:** `T-9502`, `L-9504`, `L-9519`  
**Scope:** hypothetical nonperiodic infinite exact positive H orbit

### Definitions

Put

\[
 c=\log_8 9,
 \qquad
 \delta_0=\log_8(4/3),
 \qquad
 \kappa=\frac{\log(4/3)}{\log(9/8)}.
\tag{23}
\]

Then

\[
 \boxed{\delta_0=(c-1)\kappa.}
\tag{24}
\]

Let

\[
 \theta_n=\lceil cr_n\rceil-cr_n,
 \qquad
 s_n=\lceil cr_n\rceil-r_{n+1}=d_n-o_n,
\tag{25}
\]

with `d_n=(s_n)^+`, `o_n=(-s_n)^+`, and put

\[
 h_n=\log_8u_n,
 \qquad
 \beta_n=\log_8\left(1+\frac1{p_{n+1}-1}\right)>0.
\tag{26}
\]

For `N>=1`, write

\[
 D_N=\sum_{n<N}d_n,
 \quad O_N=\sum_{n<N}o_n,
 \quad \Theta_N=\sum_{n<N}\theta_n,
 \quad B_N=\sum_{n<N}\beta_n.
\tag{27}
\]

### Statement

The positive toll series converges:

\[
 \boxed{
 B_\infty=\sum_{n\ge0}\beta_n<\infty.
 }
\tag{28}
\]

For every `N`, one has the exact identity

\[
 \boxed{
 D_N-O_N-\Theta_N
 =\delta_0N+h_N-h_0-B_N.
 }
\tag{29}
\]

Consequently

\[
 \boxed{
 D_N\ge
 O_N+\Theta_N+\delta_0N-h_0-B_\infty,
 }
\tag{30}
\]

and therefore

\[
 \boxed{
 \liminf_{N\to\infty}\frac{D_N}{N}
 \ge\delta_0
 =0.138345833\ldots .
 }
\tag{31}
\]

This improves the universal finite-chain baseline
`log_8(49/37)=0.13508549...` from `L-9519` to the exact critical constant on
an actual nonperiodic survivor.

There are two equivalent exact forms.  If

\[
 K_N=\sum_{n<N}(r_n-\kappa),
 \qquad Q_N=p_N/M_N,
\]

then

\[
 \boxed{
 h_N=(c-1)K_N-r_N+\log_8(Q_N/4),
 }
\tag{32}
\]

and

\[
 \boxed{
 D_N-O_N-\Theta_N-\delta_0N
 =(c-1)K_N+r_0-r_N.
 }
\tag{33}
\]

If the letters are bounded by `R`, and `N_+(N)` counts indices `n<N` with
`d_n>0`, then

\[
 \boxed{
 \liminf_{N\to\infty}\frac{N_+(N)}N
 \ge\frac{\delta_0}{\lceil cR\rceil}.
 }
\tag{34}
\]

### Proof

The core recurrence gives

\[
 \begin{aligned}
 h_{n+1}-h_n
 &=cr_n-r_{n+1}-\delta_0+\beta_n\\
 &=s_n-\theta_n-\delta_0+\beta_n.
 \end{aligned}
\tag{35}
\]

Moreover

\[
 \beta_n
 =\log_8\frac{p_{n+1}}{p_{n+1}-1}.
\tag{36}
\]

The Toll--Euler identity therefore gives

\[
 B_N=\log_8(Q_N/p_0).
\tag{37}
\]

`T-9502` gives `Q_N -> Q_infinity in (0,infinity)`, proving (28).  Summing
(35) proves (29), and `h_N>=0` proves (30)--(31).

Since

\[
 p_N=4\,8^{r_N}u_N=M_NQ_N,
 \qquad M_N=(9/8)^{K_N},
\]

base-eight logarithms prove (32).  Substitute (32) and (37) in (29), using
`p_0=4*8^(r_0)u_0`, to prove (33).

Finally, bounded letters give

\[
 d_n\le\lceil cR\rceil,
 \qquad
 D_N\le\lceil cR\rceil N_+(N).
\]

Combine this with (31) to obtain (34).  QED.

---

## R-9508: finite control and qualitative fresh primes are not yet a counterexample

**Claim ID:** `R-9508`  
**Title:** The remaining construction needs positive-cycle exploitation and quantitative ordinary closure  
**Status:** `PROPOSED`  
**Dependencies:** `L-9526`, `T-9516`, `T-9517`

The neighboring one-counter construction program is useful as a design
principle but does not directly supply an H orbit.  In H coordinates:

1. a physical finite macro grammar whose cycle products are all at most one is
   excluded by `L-9526`;
2. an actual nonperiodic survivor must inject distinct bridge primes at the
   explicit rate `T-9516` and must pay the exact critical deficit baseline in
   `T-9517`;
3. the unique ordinary-integer requirement remains eventual stabilization of
   the cylinder representative, not abstract 2-adic tail nonemptiness.

Thus neither a finite neutral compiler nor qualitative infinite prime support
is a counterexample certificate.  A positive construction needs a physical
positive-multiplier cycle or an unbounded macro state, quantitative fresh
arithmetic, and one finite induction proving eventual zero carry.

---

## Q-9512: sharpened counterexample construction interface

**Claim ID:** `Q-9512`  
**Title:** Construct an ordinary positive-cycle-exploiting macro ray or exclude it  
**Status:** `IDEA`

A viable structured H counterexample must now provide one explicit initial
integer and an exact inductive macro decomposition satisfying all of:

1. physical exact legality and eventual zero ordinary carry;
2. suffix multiplier growth faster than the polynomial threshold in `L-9526`,
   or an explicitly unbounded macro state;
3. exact rounded-deficit mass meeting `T-9517`;
4. the quantitative renewal-prime burden of `T-9516`;
5. positive endpoints and nontermination for every macro stage.

Conversely, a proof that every eventual-zero-carry ray has polynomial suffix
multiplier exponent below `1/sigma-1`, or violates the quantitative prime / deficit
burdens above, would settle the remaining ordinary-section problem.
