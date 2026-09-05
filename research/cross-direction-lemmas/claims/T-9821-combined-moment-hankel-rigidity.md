# T-9821 -- The native combined-moment Pade system has exact opposite tropical endpoints

Claim ID: `T-9821`
Title: Every combined periodic-tail Hankel minor is nonzero, but irrationality is reduced to a global height bound for its normalized minors
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-period-ten`
Reviewing agents: `gpt56-synthesis-01`; `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `T-9818`; branch-qualified `PR20/L-9408`, `L-9410`, and `Q-9413` at `14f06d252c3ef56fb9a69ea34c61edaa578d02a1`
Scope: every positive periodic stack word; in particular the first uncovered minimal period ten
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Use the notation of `T-9818`, but write

\[
 \lambda=T^{9S},\quad R=\lambda^r,\quad X=T^{9m},
 \quad Z=T^eX^r=T^\zeta,
 \quad C_h=p_hX^h=T^{\gamma_h},                    \tag{1}
\]

where `T=64/81`, `0<=h<r`, `gamma_0=0`, and

\[
 0=\gamma_0<\gamma_1<\cdots<\gamma_{r-1}.          \tag{2}
\]

The native block moments proposed in `PR20/Q-9413` are

\[
 u_N=R^{N(N-1)/2}Z^NP_W(X\lambda^N)
 =\sum_{h=0}^{r-1}C_hR^{N(N-1)/2}(Z\lambda^h)^N.   \tag{3}
\]

Thus `H(Y)=sum_(N>=0)u_NY^N` satisfies `H(1)=F_W(X)`, the prescribed
phase combination.  This is one scalar combined-moment series, not a claim
that its `r` individual phase values specialize independently.

## Theorem 1 -- every square combined-moment minor is nonzero

Let `d>=1`, and let

\[
 0\le s_0<\cdots<s_{d-1},\qquad
 0\le t_0<\cdots<t_{d-1}.                           \tag{4}
\]

Put

\[
 \Delta(\mathbf s,\mathbf t)
 =\det(u_{s_i+t_j})_{0\le i,j<d}.                   \tag{5}
\]

For `A(v)=sum_i binom(v_i,2)`, direct expansion gives

\[
\begin{aligned}
 \Delta(\mathbf s,\mathbf t)
={}&R^{A(\mathbf s)+A(\mathbf t)}
 Z^{\sum_i(s_i+t_i)}                                  \\
 &\times\sum_{0\le h_i<r}
 \left(\prod_i C_{h_i}\lambda^{h_is_i}\right)
 \det\left((\lambda^{rs_i+h_i})^{t_j}\right)_{i,j}.
                                                               \tag{6}
\end{aligned}
\]

The exponents `rs_i+h_i` are strictly increasing in `i`.  Hence all
generalized Vandermonde determinants in (6) have the same real sign
`(-1)^(d(d-1)/2)`.  In particular,

\[
 \boxed{\Delta(\mathbf s,\mathbf t)\ne0}.            \tag{7}
\]

More precisely, define

\[
\begin{aligned}
 E_2(\mathbf s,\mathbf t)
={}&\zeta\sum_i(s_i+t_i)\\
 &+9Sr\left\{A(\mathbf s)+A(\mathbf t)
             +\sum_i s_it_{d-1-i}\right\},          \tag{8}
\end{aligned}
\]

and, with `gamma_*=gamma_(r-1)`,

\[
\begin{aligned}
 E_3(\mathbf s,\mathbf t)
={}&\zeta\sum_i(s_i+t_i)
 +9Sr\{A(\mathbf s)+A(\mathbf t)}+d\gamma_*\\
 &+9S\left\{(r-1)\sum_i(s_i+t_i)
             +r\sum_i s_it_i\right\}.              \tag{9}
\end{aligned}
\]

Then

\[
 \boxed{v_2(\Delta)=6E_2,\qquad v_3(\Delta)=-4E_3.} \tag{10}
\]

The selecting determinant term at `2` is uniquely the reverse permutation
with `h_i=0` in every row.  The selecting term at `3` is uniquely the identity
permutation with `h_i=r-1` in every row.

### Proof

Factor the row and column powers in (3), and expand `P_W` once in every row;
this is (6).  Since

\[
 rs_i+h_i<rs_{i+1}+h_{i+1},                         \tag{11}
\]

generalized Vandermonde positivity proves the common real sign.  At `2`,
strict rearrangement pairs the increasing exponent list with `t_j` in reverse
order.  Its phase-dependent `T`-exponent is

\[
 \sum_i\{\gamma_{h_i}+9Sh_i(s_i+t_{d-1-i})\},       \tag{12}
\]

uniquely minimized by every `h_i=0`.  At `3`, because `v_3(T)=-4`, strict
rearrangement selects the identity permutation and the relevant exponent

\[
 \sum_i\{\gamma_{h_i}+9Sh_i(s_i+t_i)\}              \tag{13}
\]

is uniquely maximized by every `h_i=r-1`.  Substitution gives (8)--(10).
**QED**

## Theorem 2 -- the canonical combined Pade system and its exact error

For `n>=1`, there is a unique polynomial

\[
 B_n(Y)=\sum_{k=0}^n b_{n,k}Y^k,\qquad b_{n,0}=1,   \tag{14}
\]

for which the coefficients of `B_nH` at degrees `n,...,2n-1` vanish.
Indeed, after putting `c_j=b_(n,n-j)`, its coefficient matrix is
`(u_(i+j))_(0<=i,j<n)`, nonzero by Theorem 1.

Cramer's rule and (10), applied to the column set
`{0,...,n}\setminus{n-k}`, give, for `1<=k<=n`,

\[
 \boxed{v_2(b_{n,k})=6k\{\zeta+9Sr(n-1)\},}         \tag{15}
\]

\[
 \boxed{
 v_3(b_{n,k})
 =-4k\{\zeta+9Sr(2n-k-1)+9S(r-1)\}.
 }                                                   \tag{16}
\]

In particular,

\[
 \boxed{v_2(B_n(1))=0.}                             \tag{17}
\]

Let `A_n` remove the coefficients of `B_nH` below degree `n`.  The imposed
window then gives

\[
 B_n(Y)H(Y)-A_n(Y)
 =\sum_{\ell\ge0}\varepsilon_{n,\ell}Y^{2n+\ell}.  \tag{18}
\]

The bordered determinant with row set
`(0,...,n-1,n+ell)` and column set `(0,...,n)` yields

\[
 \boxed{
 v_2(\varepsilon_{n,\ell})=6\left[
 \zeta(2n+\ell)+{9Sr\over2}
 \{\ell^2+(2n-1)\ell+3n(n-1)\}
 \right].}                                         \tag{19}
\]

Successive bracketed exponents differ by

\[
 \zeta+9Sr(n+\ell)>0.                               \tag{20}
\]

Consequently the evaluated linear form has no hidden phase cancellation:

\[
\boxed{
 v_2(B_n(1)H(1)-A_n(1))
 =6\{2\zeta n+27Sr\,n(n-1)/2\}.
}                                                    \tag{21}
\]

### Proof

The Cramer minors are precisely the minors covered by Theorem 1.  Subtracting
their (8) and (9) from those of the base Hankel determinant gives (15)--(16).
Equation (15) makes every nonconstant coefficient of `B_n(1)` 2-adically
smaller than its constant term, proving (17).

By the Schur-complement determinant identity,
`epsilon_(n,ell)` is the bordered determinant just stated divided by the base
Hankel determinant.  Subtraction in (8) gives (19).  The error series converges
2-adically, and (20) makes its first term uniquely least, proving (21).
**QED**

## Exact period-ten reduction and height boundary

For `r=10`, (7) closes the determinant/nonvanishing part of the direct
combined-moment proposal in `PR20/Q-9413`: no finite Pade order is lost to a
rank defect, and (21) proves that summing the ten prescribed phases creates
no 2-adic cancellation of the first error.  Its quadratic leading gain is

\[
 v_2(B_n(1)H(1)-A_n(1))=81Sr\,n^2+O(n),             \tag{22}
\]

exactly the scalar Tschakaloff gain, rather than a ten-phase allocation loss.

This still does **not** prove `H(1)` irrational.  The raw Hankel and bordered
determinants have `2`- and `3`-adic sizes of order `exp(Theta(n^3))`.  Their
ratios have the quadratic endpoint differences (15)--(16), but local
valuation cancellation does not bound their global reduced rational height:
the integer unit parts may contain other primes of cubic size.

Equivalently, the remaining deliverable is the explicit global estimate

\[
 \boxed{
 \log_2 H\bigl(A_n(1):B_n(1)\bigr)
 \le (81Sr-\eta)n^2+o(n^2)
 \quad\hbox{for some }\eta>0,
 }                                                   \tag{23}
\]

along an infinite subsequence (with nonproportional pairs).  Then (21), the
product formula, and (17) would prove irrationality of the prescribed value.
Theorem 1 reduces the period-ten problem to (23); it does not assert (23).

There is one visible common factor.  With independent variables `z_i`, the
base core alternant after removing the standard row factors is

\[
 \mathcal A_n(\mathbf z)
 =\det\!\left[z_i^{rj}P_W(X\lambda^jz_i)\right]_{0\le i,j<n}.
\]

It is divisible by the ordinary Vandermonde in the `z_i`, later specialized
to `z_i=lambda^i`.  Its top-degree term chooses degree `rj+r-1` in every
column and is nonzero, so its degree is
`r n(n-1)/2+n(r-1)`.  Subtracting the Vandermonde degree `n(n-1)/2` proves
that the quotient has exact total degree

\[
 (r-1)n(n+1)/2                                      \tag{24}
\]

for the base column set, so its principal specialization can still carry
cubic global height.  A useful continuation must prove additional common
factor/content cancellation among these normalized alternants, not merely
repeat their endpoint valuations.

## Dependency, novelty, and gap audit

- `T-9818` supplies the phase decomposition and distinguishes formal rank,
  scalar irrationality measures, and arithmetic specialization.  None of
  those statements implies (7) or irrationality of `H(1)`.
- `PR20/L-9410` uses one phasewise root product.  The present denominator is
  the unique solution of the genuinely combined moment equations and is not
  assumed to factor phasewise.
- At live `PR20` head `82ca2f932438a9fe0897704ba62959ca23ec830f`,
  refreshed `Q-9413` lists five deliverables for its direct combined-moment
  route.  Theorem 2 supplies its combined zero window, proved nonzero first
  survivor, and odd evaluated denominator (deliverables 1--3).  The global
  reduced-height bound and exponent greater than one (deliverables 4--5)
  remain open exactly as stated here.
- Live `PR20/L-9418`, `R-9410`, and `T-9422` concern a different delayed
  phasewise denominator family.  They prove the native result through period
  nine and close that delayed family below threshold at period ten; they do
  not subsume the genuinely combined Hankel system (3)--(6).
- Local `R-9807` and `T-9804` close phase allocation and sparse scalar-order
  shortcuts.  They do not contain the arbitrary combined Hankel formula (6).
- Opposite endpoint uniqueness proves nonvanishing and exact local
  valuations.  It does not control primitive global height or rule out the
  prescribed arithmetic relation by itself.
- Full-period `Q`-shift propagation only rescales the same native coefficient
  relation; it cannot manufacture ten independent relations from one assumed
  rational value.  The square system here comes instead from independent
  combined moment conditions.
- The result is fixed-period and gives no period-uniform S-adic conclusion.

## Adversarial checks

- The reverse permutation belongs to `p=2`; the identity permutation belongs
  to `p=3`.  Interchanging them reverses (8) and (9).
- The phase minimizer at `2` is `h=0`, while the phase maximizer at `3` is
  `h=r-1`; positivity alone would not establish either local assertion.
- At `ell=0`, (19) is the determinant quotient
  `det(u_(i+j))_(0<=i,j<=n)/det(u_(i+j))_(0<=i,j<n)`.
- For `r=1`, (15), (19), and (21) reduce to the scalar Gaussian-binomial
  Pade valuations, providing an indexing check.
