# T-9810 -- Boundary signatures sharpen the quantitative fresh-prime budget

Claim ID: `T-9810`
Title: Freezing two endpoint signatures removes both structural primes from the correlated S-unit rank
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave15-quant-fresh-primes`
Reviewing agents: `gpt56-synthesis-01-wave14-period-ten`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9805`; branch-qualified `PR #3/L-0031`, `L-0032`, and `T-0032` at `c37e96e`; the explicit Evertse--Schlickewei--Schmidt bound imported in `T-9805`
Scope: finite initial segments of ordinary trajectories following the corrected 256-transition phase-34 stage architecture
Related counterexample candidates: none

## 1. Statement

Consider `N>=1` consecutive corrected stages

\[
m=m_0,m_0+1,\ldots,m_0+N-1,
\qquad m_0\ge12,
\tag{1}
\]

with boundary tails

\[
W_{m_0},W_{m_0+1},\ldots,W_{m_0+N}
\in\mathbb Z_{>0}.
\tag{2}
\]

The final endpoint `W_(m_0+N)` is part of the segment.  Define the
post-initial fresh-prime set

\[
\mathcal F_N^+
=\left\{p\text{ prime}:p\notin\{2,3\},\quad
p\mid\prod_{j=1}^{N}W_{m_0+j}\right\},
\qquad
f_N^+=|\mathcal F_N^+|.
\tag{3}
\]

Put

\[
\boxed{
C=1542^{771}=(6\cdot257)^{3\cdot257},
\qquad
K=3\cdot4^{257}=12\cdot4^{256}.
}
\tag{4}
\]

Then the universal forward-segment estimate is

\[
\boxed{
N-1
\le K\left\lfloor
\exp\!\left(C(2f_N^++2)\right)
\right\rfloor
\le K\exp\!\left(C(2f_N^++2)\right).
}
\tag{5}
\]

Consequently, for `N>=2`,

\[
\boxed{
f_N^+
\ge
\max\left\{
0,
\left\lceil
{C^{-1}\log((N-1)/K)-2\over2}
\right\rceil
\right\}.
}
\tag{6}
\]

Since `mathcal F_N^+` is contained in the fresh-prime support of all `N+1`
boundaries in (2), the same lower bound holds for the total number of distinct
boundary primes outside `{2,3}`.

The loss of one stage in (5) is only an initialization safeguard.  If the
initial boundary `W_(m_0)` is itself the output of an incoming stabilized
transition, or merely is known to satisfy

\[
1\le v_3(W_{m_0})\le3,
\tag{7}
\]

let `mathcal F_N` be defined by replacing the product over `1<=j<=N` in
(3) by the product over `0<=j<=N`, and put `f_N=|mathcal F_N|`.  Then

\[
\boxed{
N
\le K\left\lfloor
\exp\!\left(C(2f_N+2)\right)
\right\rfloor,
}
\tag{8}
\]

and

\[
\boxed{
f_N
\ge
\max\left\{
0,
\left\lceil
{C^{-1}\log(N/K)-2\over2}
\right\rceil
\right\}.
}
\tag{9}
\]

For integer `Q>=0`, the threshold form of (5) is

\[
N-1>K\exp\!\left(C(2Q+2)\right)
\quad\Longrightarrow\quad
f_N^+\ge Q+1.
\tag{10}
\]

When `N=1` and no incoming signature is assumed, (5) is empty and the only
universal conclusion is the small-case bound `f_N^+>=0`.

## 2. Exact stage-boundary signatures

Write the source word of stage `m` as

\[
w_m=(i_{m,0},\ldots,i_{m,255})
\in\{0,1,2,3\}^{256},
\tag{11}
\]

and let `j_m=i_(m,256)` be the type at its right endpoint.  Under chronological
concatenation, `j_m=i_(m+1,0)` whenever the next stage is present.

The valuation table of `PR #3/L-0032` is

\[
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)=(0,1,2,3),
\tag{12}
\]

\[
(\beta_0,\beta_1,\beta_2,\beta_3)=(2,3,2,1).
\tag{13}
\]

If `ell_m` is the source type of the local transition immediately preceding
`W_m`, put

\[
\rho_m=\beta_{\ell_m}\in\{1,2,3\},
\qquad
\sigma_m=\alpha_{j_m}\in\{0,1,2,3\}.
\tag{14}
\]

When only hypothesis (7), rather than an explicitly named predecessor, is
available at the initial boundary, set `rho_(m_0)=v_3(W_(m_0))` directly.

The exact endpoint signatures are

\[
\boxed{
\begin{aligned}
v_2(W_m)&=\alpha_{i_{m,0}},
&v_3(W_m)&=\rho_m,\\
v_2(W_{m+1})&=\sigma_m,
&v_3(W_{m+1})&=\beta_{i_{m,255}}.
\end{aligned}}
\tag{15}
\]

The current word fixes the upper-left and lower-right entries of (15).  It
remains only to freeze the incoming ternary signature `rho_m` and the outgoing
endpoint type `j_m`, equivalently `sigma_m`.

Thus define the signature context

\[
\chi_m=(\rho_m,w_m,j_m).
\tag{16}
\]

There are at most

\[
\boxed{
3\cdot4^{256}\cdot4=K
}
\tag{17}
\]

contexts.  Freezing the predecessor type itself would use four choices, but
types zero and two have the same ternary signature `beta=2`; the three-state
signature is the sharper datum.

For every stage after the first one in a forward segment, the incoming local
transition exists, so (14)--(17) apply.  They also apply to the first stage
under hypothesis (7).  The last stage uses `j_(m_0+N-1)`, so the type and all
prime factors of the final endpoint are retained rather than silently
dropped.

## 3. Removing `2` and `3` from the endpoint group

Fix one context

\[
\chi=(\rho,w,j),
\qquad
w=(i_0,\ldots,i_{255}).
\tag{18}
\]

Equations (15) give exact factorizations

\[
\boxed{
W_m=2^{\alpha_{i_0}}3^\rho\widehat W_m,
\qquad
W_{m+1}=2^{\alpha_j}3^{\beta_{i_{255}}}
\widehat W_{m+1},
}
\tag{19}
\]

where

\[
\gcd(\widehat W_m,6)
=\gcd(\widehat W_{m+1},6)=1.
\tag{20}
\]

All prime divisors of the hatted endpoints belong to the relevant fresh-prime
set.

For the normalized 257-term stage equation, `T-9805/(27)--(34)` supplies a
fixed mixed `2`--`3` scale tuple

\[
g=(g_*,g_0,\ldots,g_{255})
\in(\mathbb Q^*)^{257},
\tag{21}
\]

one scale parameter

\[
D_m=2^{m-8},
\tag{22}
\]

and positive rational coefficients `c_(w,*)`, `c_(w,k)` such that

\[
x_{m,*}
=c_{w,*}g_*^{D_m}{W_m\over W_{m+1}},
\tag{23}
\]

\[
x_{m,k}
=c_{w,k}g_k^{D_m}{1\over W_{m+1}}
\qquad(0\le k<256),
\tag{24}
\]

and

\[
x_{m,*}+\sum_{k=0}^{255}x_{m,k}=1.
\tag{25}
\]

Substitute (19) and define the context coefficients

\[
d_{\chi,*}
=c_{w,*}
2^{\alpha_{i_0}-\alpha_j}
3^{\rho-\beta_{i_{255}}},
\tag{26}
\]

\[
d_{\chi,k}
=c_{w,k}
2^{-\alpha_j}3^{-\beta_{i_{255}}}.
\tag{27}
\]

They are fixed once `chi` is fixed.  Put

\[
z_{m,*}
=g_*^{D_m}{\widehat W_m\over\widehat W_{m+1}},
\qquad
z_{m,k}
=g_k^{D_m}{1\over\widehat W_{m+1}}.
\tag{28}
\]

Then (25) is the one fixed positive equation

\[
\boxed{
d_{\chi,*}z_*+
\sum_{k=0}^{255}d_{\chi,k}z_k=1.
}
\tag{29}
\]

Every solution is nondegenerate because all 257 summands are positive.

## 4. Correlated fresh-prime rank

For every fresh prime `p`, define the two endpoint directions

\[
L_p=(p,1,\ldots,1),
\qquad
R_p=(p^{-1},p^{-1},\ldots,p^{-1})
\in(\mathbb Q^*)^{257}.
\tag{30}
\]

In tuple notation, (28) is

\[
z_m
=g^{D_m}
\prod_{p\in\mathcal F}
L_p^{\nu_p(\widehat W_m)}
R_p^{\nu_p(\widehat W_{m+1})},
\tag{31}
\]

where `mathcal F` is `mathcal F_N^+` in the universal statement and
`mathcal F_N` in the initialized statement.  Hence all solutions for one
context lie in

\[
\Lambda_{\mathcal F}
=\langle g,\ L_p,R_p:p\in\mathcal F\rangle.
\tag{32}
\]

If `f=|mathcal F|`, then

\[
\boxed{
\operatorname{rank}\Lambda_{\mathcal F}
\le2f+1.
}
\tag{33}
\]

The single generator `g` carries all unbounded powers of both `2` and `3`
because those powers have the common exponent parameter `D_m`.  Equations
(19), (26), and (27) put the bounded endpoint powers of `2` and `3` into
coefficients.  Thus neither structural prime contributes an endpoint rank
direction in (33).

## 5. Distinctness and the ESS count

For a fixed source word, `T-9805/(37)--(38)` gives

\[
{x_{m,0}\over x_{m,1}}
=2^{\alpha_{i_0}-\alpha_{i_1}-11(t_{m,1}+1)}
3^{\beta_{i_0}-\beta_{i_1}+7(t_{m,1}+1)},
\tag{34}
\]

where

\[
t_{m,1}=2^m+2^{m-8}.
\tag{35}
\]

Multiplicative independence of `2` and `3` makes (34) different at different
scales.  For a fixed context, multiplication by the nonzero fixed coefficients
in (26)--(27) is coordinatewise injective, so the corresponding `z_m` are also
distinct solutions of (29).

The explicit Evertse--Schlickewei--Schmidt bound used in `T-9805` is

\[
A(n,r)=\exp\!\left((6n)^{3n}(r+1)\right).
\tag{36}
\]

Here `n=257`, `(6n)^(3n)=C`, and (33) gives `r+1<=2f+2`.  Therefore one
context occurs at most

\[
\left\lfloor
\exp\!\left(C(2f+2)\right)
\right\rfloor
\tag{37}
\]

times.  Summing (37) over the `K` contexts proves (8) when the initial
signature is available.

Without (7), discard only stage `m_0`.  The remaining `N-1` stages have left
boundaries

\[
W_{m_0+1},\ldots,W_{m_0+N-1}
\tag{38}
\]

and right boundaries through the retained final endpoint `W_(m_0+N)`.  Their
fresh support is contained in `mathcal F_N^+`, so the same count proves (5).
Taking logarithms, applying the integer ceiling, and combining with `f>=0`
proves (6) and (9). **QED**

## 6. Why freezing both signatures is the strongest direct tradeoff

Once the source word is fixed, the only unfixed structural endpoint powers are
the three-valued `v_3(W_m)` and the four-valued `v_2(W_(m+1))`.  One can either
freeze each value into the coefficients or retain its tuple direction in the
group.  Apart from the common factor `4^256`, the four safe choices are:

| Frozen signatures | Context multiplier | Rank bound | `r+1` in ESS |
|---|---:|---:|---:|
| neither | `1` | `2f+3` | `2f+4` |
| incoming `v_3` only | `3` | `2f+2` | `2f+3` |
| outgoing `v_2` only | `4` | `2f+2` | `2f+3` |
| both | `12` | `2f+1` | `2f+2` |

The full-freezing real exponential envelope divided by the incoming-only
envelope is

\[
4e^{-C}<1,
\tag{39}
\]

and its ratio to the no-freezing envelope is

\[
12e^{-2C}<1.
\tag{40}
\]

The outgoing-only comparison is `3e^(-C)<1`.  Thus freezing both signatures
is the strongest of these direct coefficient/rank choices.  This does not
claim global optimality among all possible reorganizations of the stage
equations.

## What this advances

- `PR #3/L-0032` proves qualitatively that all unbounded boundary arithmetic
  lies outside `{2,3}`.  This claim turns that observation into an explicit
  finite-prefix count.
- `T-9805` has rank `2s+1` for all boundary primes.  Writing `f` for primes
  outside `{2,3}`, its worst-case conversion `s<=f+2` gives

  \[
  N\le4^{256}\exp\!\left(C(2f+6)\right).
  \tag{41}
  \]

  Under an incoming signature, (8) replaces this by

  \[
  N\le12\cdot4^{256}\exp\!\left(C(2f+2)\right).
  \tag{42}
  \]

  The factor `12` is smaller than `exp(4C)`, so (42) is a strict quantitative
  sharpening of the converted `T-9805` bound.
- Live PR #3 contains qualitative fresh-prime necessity and exact boundary
  signatures, but no explicit ESS finite-prefix inversion.  The quantitative
  rank compression and constants here are new relative to that head.

## Dependency and source audit

- `PR #3/L-0031` supplies the positive 257-term corrected-stage equation.
- `PR #3/L-0032` supplies all four exact valuations in (15).  Its current
  binary signature is unconditional; its ternary signature holds after an
  incoming local transition, which is why the universal theorem loses one
  initial stage.
- `PR #3/T-0032` supplies the qualitative fixed-word S-unit strategy.
- `T-9805` supplies the explicit ESS constant, affine scale factorization,
  and scale-separating ratio.  This claim changes its endpoint group and
  context count rather than reusing its all-prime rank.
- At live PR #3 head `c37e96e`, no quantitative finite-prefix bound overlaps
  (5)--(10).

## Gap and scope audit

- The bound is explicit but numerically enormous because `C=1542^771`.
- It counts distinct fresh primes, not their sizes or the stages where they
  first appear.
- The two endpoint directions per fresh prime remain.  No recurrence relation
  has been shown to reduce their rank uniformly.
- The first-stage loss in (5) is real when no incoming ternary signature is
  assumed; it is not silently hidden in the context count.
- The theorem assumes an ordinary corrected-stage segment.  It constructs no
  cap stitch, finite initialization, or Collatz counterexample.

## Adversarial and bounded arithmetic checks

- Exact canonical connectors for all 16 source/target type pairs, with four
  residual tails each, verified `v_2(W_n)=alpha_i` and
  `v_3(W_(n+1))=beta_i` directly from the ordinary recurrence.
- The signature alphabets have exactly three incoming ternary values and four
  outgoing binary values, giving `K=3*4^257`, not `4^258`.
- Exhaustive bounded factorizations over every endpoint signature and toy
  fresh parts supported on `{5,7}` verified (19)--(20).
- The coefficient exponents in (26)--(27) were checked coordinatewise against
  (23)--(24): both structural endpoint primes disappear from (31).
- Toy generator matrices recovered the bound `2f+1`; no independence of all
  displayed generators was assumed.
- Exact small-constant replays checked the floor, ceiling, `max(0,...)`, and
  `N-1` inversion in (5)--(9).
- The final endpoint occurs in (3), (19), (28), and (38), auditing the
  otherwise easy endpoint omission.

## Remaining uncertainty

Can overlap of consecutive endpoint words force the pairs
`(nu_p(W_m),nu_p(W_(m+1)))` into a rank-one subgroup for each fresh prime on
some repeated context?  Without such a theorem, two directions per fresh
prime are necessary in the safe ambient group.
