# T-9835 -- Every evaluated Padé gcd is trapped between adjacent Schur cores

Claim ID: `T-9835`
Title: The prime-to-six gcd of a canonical combined-moment approximant divides one quadratic cyclotomic step times the square of an adjacent Schur-core gcd
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave22-completion-master`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9821`, `T-9824`, `T-9826`, `T-9830`; branch-qualified `PR20/Q-9413` at `82ca2f932438a9fe0897704ba62959ca23ec830f`
Scope: canonical combined-moment Padé approximants for every fixed positive periodic stack word; especially primitive period ten
Related counterexample candidates: issue #4 periodic stack frontier; PR #38 atom `ACL-N024`; no `K-####` candidate

## Motivation

`T-9830` proves that a quadratic primitive-height bound would require an
almost-total cubic gcd

\[
 g_n=\gcd(|\widehat A_n|,|\widehat B_n|)
\tag{1}
\]

supported only at primes at least five.  That formulation still leaves the
gcd hidden inside two evaluated sums.  The consecutive Padé determinant
identity and the exact Hankel factorization localize it much further: apart
from one explicitly quadratic cyclotomic step, all of its cubic mass must
already occur in the gcd of two *adjacent base Schur cores*.

This is a localization theorem, not an upper bound for that adjacent gcd.

## Setup

Retain all notation of `T-9830`.  In particular,

\[
 T={64\over81},\qquad \lambda=T^{9S},\qquad r\ge1,
\tag{2}
\]

and

\[
 H(Y)=\sum_{N\ge0}u_NY^N.
\tag{3}
\]

Let

\[
 \Delta_n=\det(u_{i+j})_{0\le i,j<n},\qquad \Delta_0=1,
\tag{4}
\]

and let `B_n`, `A_n`, and `R_n=A_n(1)/B_n(1)` be the canonical Padé
objects of `T-9821` and `T-9830`.  Thus

\[
 B_n(Y)H(Y)-A_n(Y)
 =\varepsilon_{n,0}Y^{2n}+O(Y^{2n+1}).
\tag{5}
\]

Write

\[
 G_n=G_{n,0}
 =81^{d_n}F_{n,0}(64/81)\in\mathbf Z_{>0},
 \qquad \gcd(G_n,6)=1,
\tag{6}
\]

for the base Schur core of `T-9830`.

The raw clearing used there is

\[
 \mathcal D_n=3^{4\beta_n}G_n,
\tag{7}
\]

and

\[
 \widehat A_n=\mathcal D_nA_n(1),\qquad
 \widehat B_n=\mathcal D_nB_n(1).
\tag{8}
\]

Both quantities in (8) are integers and

\[
 \gcd(\widehat A_n,\widehat B_n)=g_n,
 \qquad \gcd(g_n,6)=1.
\tag{9}
\]

For `n>=0`, define the positive prime-to-six integer

\[
 \boxed{
 \mathcal C_n
 =\prod_{j=1}^{n}
 \left(81^{9Sj}-64^{9Sj}\right),
 \qquad \mathcal C_0=1.}
\tag{10}
\]

## Statement 1 -- exact prime-to-six part of the base Hankel determinant

Put

\[
 \mathcal V_n
 =\prod_{j=1}^{n-1}
 \left(81^{9Sj}-64^{9Sj}\right)^{n-j},
 \qquad \mathcal V_0=\mathcal V_1=1.
\tag{11}
\]

For every prime `p>=5`,

\[
 \boxed{
 v_p(\Delta_n)=v_p(\mathcal V_n)+v_p(G_n).}
\tag{12}
\]

Consequently,

\[
 \boxed{
 v_p(\varepsilon_{n,0})
 =v_p(\mathcal C_n)+v_p(G_{n+1})-v_p(G_n).}
\tag{13}
\]

Here the valuations in (12)--(13) are valuations on nonzero rational
numbers, so the right side of (13) is allowed to be negative.

### Proof

Factor rows and columns in the base determinant exactly as in
`T-9821/(6)`.  For the index sets `0,1,...,n-1`, this gives

\[
 \Delta_n
 =R^{2K_n}Z^{n(n-1)}
 \mathcal A_n(1,\lambda,\ldots,\lambda^{n-1}),
\tag{14}
\]

where `K_n=n(n-1)(n-2)/6` and `mathcal A_n` is the alternant of
`T-9824`.  Its exact factorization is

\[
 \mathcal A_n(1,\lambda,\ldots,\lambda^{n-1})
 =V_n(1,\lambda,\ldots,\lambda^{n-1})
 T^{a_n}F_{n,0}(T).
\tag{15}
\]

All factors outside the Vandermonde and `F_(n,0)` in (14)--(15) are
powers of `T=64/81`, so they have no valuation at a prime `p>=5`.

The specialized Vandermonde is

\[
 \begin{aligned}
 V_n(1,\lambda,\ldots,\lambda^{n-1})
 &=\prod_{0\le i<j<n}(\lambda^j-\lambda^i)\\
 &=(-1)^{n(n-1)/2}T^{e_n}
   \prod_{j=1}^{n-1}(1-T^{9Sj})^{n-j}
 \end{aligned}
\tag{16}
\]

for an integer `e_n>=0`.  Since

\[
 1-T^{9Sj}
 ={81^{9Sj}-64^{9Sj}\over81^{9Sj}},
\tag{17}
\]

its prime-to-six numerator is exactly `mathcal V_n`.  Likewise,

\[
 F_{n,0}(64/81)={G_n\over81^{d_n}}.
\tag{18}
\]

Equations (14)--(18) prove (12).

The Schur-complement identity for the leading Padé error gives the exact
rational identity

\[
 \varepsilon_{n,0}={\Delta_{n+1}\over\Delta_n}.
\tag{19}
\]

Finally,

\[
 {\mathcal V_{n+1}\over\mathcal V_n}
 =\prod_{j=1}^{n}(81^{9Sj}-64^{9Sj})
 =\mathcal C_n.
\tag{20}
\]

Subtracting (12) at consecutive orders proves (13). **QED**

## Statement 2 -- exact adjacent cross-determinant content

For `n>=1`, define the nonzero integer

\[
 X_n^+
 =\widehat A_{n+1}\widehat B_n
  -\widehat A_n\widehat B_{n+1}.
\tag{21}
\]

Then, for every prime `p>=5`,

\[
 \boxed{
 v_p(X_n^+)
 =v_p(\mathcal C_n)+2v_p(G_{n+1}).}
\tag{22}
\]

Equivalently, the entire prime-to-six part of `X_n^+` is

\[
 \boxed{\mathcal C_nG_{n+1}^2.}
\tag{23}
\]

### Proof

The consecutive Padé identity from `T-9830/(96)` is

\[
 A_{n+1}(Y)B_n(Y)-A_n(Y)B_{n+1}(Y)
 =\varepsilon_{n,0}Y^{2n}.
\tag{24}
\]

Evaluating at `Y=1` and using (8) gives

\[
 X_n^+=\mathcal D_n\mathcal D_{n+1}\varepsilon_{n,0}.
\tag{25}
\]

At a prime `p>=5`, equation (7) gives

\[
 v_p(\mathcal D_j)=v_p(G_j).
\tag{26}
\]

Substituting (13) and (26) into (25) cancels `v_p(G_n)` and leaves

\[
 v_p(X_n^+)
 =v_p(G_n)+v_p(G_{n+1})
  +v_p(\mathcal C_n)+v_p(G_{n+1})-v_p(G_n),
\tag{27}
\]

which is (22).  Every factor in (23) is prime to six.  Since `X_n^+` is a
nonzero integer, (22) for all `p>=5` proves (23). **QED**

## Statement 3 -- the two-sided adjacent-core trap

For every `n>=2`,

\[
 \boxed{
 g_n\mid
 \gcd\!\left(
   \mathcal C_{n-1}G_n^2,
   \mathcal C_nG_{n+1}^2
 \right).}
\tag{28}
\]

In particular,

\[
 \boxed{
 g_n\mid
 \mathcal C_n\gcd(G_n,G_{n+1})^2.}
\tag{29}
\]

### Proof

Because `g_n` divides both entries in (8), it divides both terms in (21),
and hence

\[
 g_n\mid X_n^+.
\tag{30}
\]

The same argument with orders `n-1,n` gives

\[
 g_n\mid X_{n-1}^+.
\tag{31}
\]

The gcd `g_n` is prime to six by (9).  Applying (23) to (30)--(31) proves
(28).

It remains only to simplify the right side.  Since

\[
 \mathcal C_n=\mathcal C_{n-1}
 (81^{9Sn}-64^{9Sn}),
\tag{32}
\]

the elementary valuation inequality

\[
 \min(c+2a,c+h+2b)
 \le c+h+2\min(a,b)
\tag{33}
\]

for nonnegative integers `a,b,c,h`, applied prime by prime, gives

\[
 \gcd(\mathcal C_{n-1}G_n^2,
      \mathcal C_nG_{n+1}^2)
 \mid \mathcal C_n\gcd(G_n,G_{n+1})^2.
\tag{34}
\]

This proves (29). **QED**

## Statement 4 -- the period-ten problem becomes a half-core adjacency problem

For fixed `S`,

\[
 \boxed{
 \log_2\mathcal C_n
 ={9S\log_2 81\over2}n(n+1)+O_S(1).}
\tag{35}
\]

For `r>=2`, the quadratic primitive-height requirement of `T-9830` forces

\[
 \boxed{
 \log_2\gcd(G_n,G_{n+1})
 \ge3S(r-1)\log_2(3)n^3-O_{W,m}(n^2)}
\tag{36}
\]

along every order set on which that requirement holds.

For period ten this becomes

\[
 \boxed{
 \log_2\gcd(G_n,G_{n+1})
 \ge27S\log_2(3)n^3-O_{W,m}(n^2).}
\tag{37}
\]

Conversely, if for some `delta>0` and infinitely many `n`,

\[
 \log_2\gcd(G_n,G_{n+1})
 \le
 \{3S(r-1)\log_2(3)-\delta\}n^3,
\tag{38}
\]

then on those orders

\[
 \boxed{
 \log_2H(R_n)\ge2\delta n^3-O_{W,m}(n^2).}
\tag{39}
\]

In particular, those canonical approximants cannot have quadratic primitive
height.

### Proof

From (10),

\[
 \begin{aligned}
 \log_2\mathcal C_n
 &=\sum_{j=1}^n
   \left\{9Sj\log_2 81+
   \log_2(1-T^{9Sj})\right\}.
 \end{aligned}
\tag{40}
\]

The second sum converges as `n->infinity`, proving (35).

`T-9830/(67)` shows that quadratic primitive height is equivalent to

\[
 \log_2g_n
 =6S(r-1)\log_2(3)n^3+O_{W,m}(n^2).
\tag{41}
\]

Taking logarithms in (29), using (35), and comparing with (41) proves
(36), hence (37).

Under (38), equations (29) and (35) instead give

\[
 \log_2g_n
 \le
 \{6S(r-1)\log_2(3)-2\delta\}n^3
 +O_{W,m}(n^2).
\tag{42}
\]

The raw-height formula `T-9830/(62),(65)` is

\[
 \log_2H(R_n)
 =6S(r-1)\log_2(3)n^3-log_2g_n
 +O_{W,m}(n^2).
\tag{43}
\]

Substitution of (42) proves (39). **QED**

## Consequence for the live period-ten route

The missing cubic cancellation is no longer an arbitrary correlation between
the evaluated sums `widehat A_n` and `widehat B_n`.  Apart from the explicit
quadratic factor `mathcal C_n`, at least half of the base core's cubic
logarithmic mass must be shared by the adjacent integers

\[
 G_{n,0},\qquad G_{n+1,0}.
\tag{44}
\]

This leaves two sharply separated continuations:

1. prove an adjacent-core resultant, primitive-divisor, or specialization-gcd
   upper bound below the half-core threshold, thereby closing the canonical
   combined-moment height route; or
2. find and prove a cross-order factor that accounts for the half-core mass,
   thereby exposing the only remaining source of the required cancellation.

The ordinary Vandermonde contributes only `Theta(n^2)` from one order to the
next and therefore cannot supply the cubic requirement by itself.

## Adversarial audit

- Equation (19) is the leading-error Schur complement.  It uses consecutive
  *normal* canonical Padé systems; arbitrary approximants do not inherit it.
- The cumulative Vandermonde has cubic size, but its consecutive quotient
  `mathcal C_n` has only quadratic logarithmic size.  Confusing these two
  quantities would destroy (36).
- The clearing factor `mathcal D_n` depends on `n`.  Both factors in (25)
  are required; clearing only one order gives the wrong square in (23).
- Statement 3 uses both neighboring cross determinants.  A one-sided identity
  localizes `g_n` only to `mathcal C_nG_(n+1)^2`.
- Equation (29) is an arithmetic specialization statement.  It does not claim
  that the polynomials `F_(n,0)(T)` and `F_(n+1,0)(T)` have a common factor.
- No upper bound for `gcd(G_n,G_(n+1))` is proved.  Hence no period-ten
  irrationality, rationality, or Collatz conclusion is claimed.

## Dependency and source audit

- `T-9821` supplies normality of every Hankel system, the Schur-complement
  error, and the combined moments.
- `T-9824` supplies the exact ordinary-Vandermonde times Schur-quotient
  factorization.
- `T-9826` supplies the consecutive Padé identity and nonproportionality.
- `T-9830` supplies the prime-to-six Schur cores, integral raw clearing,
  exact raw-height formula, and cubic-gcd equivalence.
- Live `PR20/Q-9413` asks for a symbolic maximal-minor, cyclotomic, or
  reduced-height mechanism.  Equations (28)--(37) replace that broad request
  for the canonical family by the exact adjacent-core half-mass target.
- No external theorem or numerical experiment is used.

## Remaining uncertainty

The arithmetic gcd of adjacent specialized Schur cores remains open.  It may
be small, which would close this Padé architecture, or it may contain a new
large cross-order factor.  The present theorem proves that there is nowhere
else for a cubic evaluated gcd to hide.
