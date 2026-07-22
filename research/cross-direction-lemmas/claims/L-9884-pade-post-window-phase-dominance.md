# L-9884 -- Post-window phase dominance for periodic block Pade tails

Claim ID: `L-9884`
Title: Every completed root-product tail is phase-zero dominated, and period four needs linear extra cancellation
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-b`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR20/L-9408`, `PR20/L-9410`, `PR20/L-9411`, `PR20/T-9416`
Scope: the periodic phasewise root-product Pade family, after every allocated cancellation window has closed
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Use the notation of `PR20/L-9411`. Thus `W` is a positive word of displayed
length `r`,

\[
T={64\over81},\qquad S=S(W),\qquad
\lambda=T^{9S},\qquad R=\lambda^r,
\tag{1}
\]

and, at starting height `m`,

\[
Z=T^\zeta,\qquad \zeta=e(W)+9mr.
\tag{2}
\]

The phase constants from `PR20/L-9408` are

\[
C_j=T^{\gamma_j},\qquad
\gamma_j=j+9A_j(W)+9mj,
\tag{3}
\]

so `gamma_0=0` and `gamma_j>0` for `j>0`.

Choose allocations `n_0,...,n_(r-1)>=0`, put

\[
D=\sum_jn_j\ge1,
\qquad n_{\max}=\max_jn_j,
\tag{4}
\]

and let

\[
\mathcal C
=\bigcup_{j=0}^{r-1}
 \{r(D+t)+j:0\le t<n_j\}
\tag{5}
\]

be the root set. For `N>=D`, the phase coefficient supplied by
`PR20/L-9411` is

\[
\Gamma_{j,N}
=C_jR^{N(N-1)/2}(Z\lambda^j)^N
 \prod_{c\in\mathcal C}(1-\lambda^{c-rN-j}).
\tag{6}
\]

Write

\[
a_N=\sum_{j=0}^{r-1}\Gamma_{j,N},
\qquad
E_{\mathcal C}(N)
={rN(N-1)\over2}-rDN+\sum_{c\in\mathcal C}c.
\tag{7}
\]

## Statement 1 -- exact post-window valuation

For every

\[
N\ge D+n_{\max}
\tag{8}
\]

all factors in (6) are nonzero, and

\[
\boxed{
v_2(\Gamma_{j,N})
=6\{\gamma_j+\zeta N
 +9S[E_{\mathcal C}(N)+j(N-D)]\}.
}
\tag{9}
\]

In particular, for every `j>0`,

\[
\boxed{
v_2(\Gamma_{j,N})-v_2(\Gamma_{0,N})
=6\{\gamma_j+9Sj(N-D)\}>0.
}
\tag{10}
\]

Hence phase zero is the unique term of least `2`-adic valuation in every
completed-window coefficient:

\[
\boxed{
a_N\ne0,
\qquad
v_2(a_N)=6\{\zeta N+9S E_{\mathcal C}(N)\}.
}
\tag{11}
\]

These valuations strictly increase with `N`:

\[
\boxed{
v_2(a_{N+1})-v_2(a_N)
=6\{\zeta+9Sr(N-D)\}>0.
}
\tag{12}
\]

Consequently, for every `M>=D+n_max`, the convergent evaluated tail satisfies

\[
\boxed{
v_2\!\left(\sum_{N\ge M}a_N\right)=v_2(a_M).
}
\tag{13}
\]

Thus neither cross-phase cancellation inside a coefficient nor cross-block
cancellation after setting `Y=1` can occur once all allocated phase windows
have closed.

## Proof of Statement 1

The largest possible root in (5) is at most

\[
r(D+n_{\max})-1.
\tag{14}
\]

Therefore (8) implies

\[
c-rN-j<0
\tag{15}
\]

for every root `c` and phase `j`. Put `d=rN+j-c>0`. Extract

\[
1-\lambda^{-d}=-\lambda^{-d}(1-\lambda^d).
\tag{16}
\]

Because `v_2(lambda)>0`, every remaining factor `1-lambda^d` is a `2`-adic
unit. The extracted total `lambda` exponent in (6) is

\[
{rN(N-1)\over2}+jN-D(rN+j)+\sum_{c\in\mathcal C}c
=E_{\mathcal C}(N)+j(N-D).
\tag{17}
\]

Equations (1)--(3) now give (9). Subtracting the phase-zero value proves
(10); the term `gamma_j` is already positive for `j>0`. The ultrametric
inequality with a unique minimum proves (11).

Finally,

\[
E_{\mathcal C}(N+1)-E_{\mathcal C}(N)=r(N-D),
\tag{18}
\]

which proves (12). The valuations tend quadratically to infinity, so the
tail converges `2`-adically; its first term is uniquely minimal by (12),
giving (13). **QED**

## Statement 2 -- the equal-allocation coefficient law

Specialize to

\[
n_0=\cdots=n_{r-1}=n,
\qquad D=rn,
\qquad N_0=(r+1)n.
\tag{19}
\]

Put, as in `PR20/L-9410`,

\[
L_{r,n}
={n[nr(r^2+r+1)-r^2-2r]\over2}.
\tag{20}
\]

Then for every integer `ell>=0`,

\[
\boxed{
v_2(a_{N_0+\ell})
=6\left\{
 \zeta(N_0+\ell)
 +9S\left[L_{r,n}+rn\ell+{r\ell(\ell-1)\over2}\right]
 \right\}.
}
\tag{21}
\]

At the same block, the exact gap from phase zero to phase `j>0` is

\[
\boxed{
6\{\gamma_j+9Sj(n+\ell)\}.
}
\tag{22}
\]

### Proof

For equal allocation the root set is the consecutive interval

\[
\{r^2n,r^2n+1,\ldots,r^2n+D-1\}.
\tag{23}
\]

Direct substitution at `N_0` gives

\[
E_{\mathcal C}(N_0)=L_{r,n}.
\tag{24}
\]

Summing (18) from `N_0` to `N_0+ell` yields

\[
E_{\mathcal C}(N_0+\ell)
=L_{r,n}+rn\ell+{r\ell(\ell-1)\over2}.
\tag{25}
\]

Equations (11) and (10) give (21) and (22). **QED**

## Statement 3 -- an optimistic cancellation-depth barrier

This part is a benchmark for proposed coupled repairs, not an assertion that
such a repair exists. Grant, at zero quadratic height cost, an auxiliary
mechanism that deletes the first `ell_n` equal-allocation tail blocks and
leaves (21) as the next error. Assume the raw quadratic height coefficient of
`PR20/L-9410` is unchanged up to `o(n^2)`.

If

\[
{\ell_n\over n}\longrightarrow\theta\ge0,
\tag{26}
\]

then its valuation-to-height benchmark is

\[
\boxed{
\mu_r(\theta)
={6\over\log_2 81}
 {r^2+r+1+2\theta+\theta^2\over r(r+1)}.
}
\tag{27}
\]

In particular, any sublinear delay `ell_n=o(n)` leaves the original exponent
`mu_r` unchanged. If the quotient in (26) does not converge, applying (27)
along each convergent subsequence gives the corresponding liminf statement.
For period four, a liminf benchmark strictly above one in this deliberately
optimistic unchanged-height model therefore requires

\[
\boxed{
\liminf_{n\to\infty}{\ell_n\over n}
>
\theta_4
=-1+\sqrt{{10\over3}\log_2 81-20}
=0.064346439346\ldots .
}
\tag{28}
\]

Thus bounded cancellation, logarithmic cancellation, and every other
`o(n)` postponement are quadratically invisible at the period-four frontier.
Even a cost-free cancellation-only repair needs more than `6.4346%` of `n`
additional blocks asymptotically.

### Proof

If `ell_n=theta*n+o(n)`, then after removing the common factor `9S`, the
quadratic part of the bracket in (21) is

\[
{r\over2}
 [r^2+r+1+2\theta+\theta^2]n^2.
\tag{29}
\]

After removing the same common factor `9S`, the raw height exponent of
`PR20/L-9410` has quadratic part

\[
{r^2(r+1)\over2}n^2.
\tag{30}
\]

Multiplication by the place-conversion factor `6/log_2(81)` proves (27).
For `r=4`, solving `mu_4(theta)>1` gives (28). **QED**

## What this closes

- `PR20/L-9411` left cross-phase cancellation after the allocated windows
  open. Equations (9)--(13) exclude it throughout the complete post-window
  tail.
- For equal allocation there is no staggered transition strip, so every
  surviving coefficient is phase-zero dominated.
- A proposed period-four repair based only on cancelling finitely or
  sublinearly many further equal-allocation errors cannot change the
  quadratic approximation exponent.

## Dependency audit

- `PR20/L-9408` supplies the exact exponents `zeta` and `gamma_j`.
- `PR20/L-9411` supplies the root set and product formula (6).
- `PR20/L-9410` supplies the equal-allocation height normalization and
  `L_(r,n)`.
- `PR20/T-9416` supplies the context that equal allocation is already optimal
  inside the whole root-product class; it is not needed for the algebraic
  proof of Statements 1 and 2.
- Only exact factor extraction and the ultrametric inequality are used.

## Gap audit

- Unequal allocation can have a staggered strip
  `D+min_j(n_j)<=N<D+n_max`; cancellations there are not excluded.
- Statement 3 is explicitly conditional on retaining the old quadratic
  height coefficient while only delaying the first surviving block. A common
  factor that lowers height quadratically, or a determinant with a different
  height law, lies outside it.
- A genuinely coupled Hermite--Pade or Casoratian construction can alter the
  coefficient profile and is not reduced to (6).
- The lemma does not prove period-four irrationality.

## Adversarial checks

- The endpoint in (8) is inclusive: at `N=D+n_max`, (14) makes every exponent
  at most `-1`, so no product factor vanishes.
- Allocations with `n_0=0` are allowed; phase zero is still nonzero after the
  common endpoint and remains the unique valuation minimum.
- The phase gap includes both the fixed positive exponent `gamma_j` and the
  growing term `j(N-D)`; neither was discarded.
- Cross-block noncancellation uses the positive `Z` increment in addition to
  (18).
- The constant in (28) is the positive root of
  `21+2 theta+theta^2=(20/6)log_2(81)`.

## Remaining uncertainty

Can a coupled adjacent-order determinant cancel a linear fraction of the
equal-allocation tail while paying less than a quadratic height penalty? The
minimum optimistic target at period four is now the explicit depth
`theta_4 n` from (28).

## Suggested next attack

Build the first adjacent-order Casoratian symbolically and compare its exact
height increase with the linear-depth target (28). Any successful construction
must either reach that depth, lower the height quadratically, or leave the
root-product coefficient profile altogether.
