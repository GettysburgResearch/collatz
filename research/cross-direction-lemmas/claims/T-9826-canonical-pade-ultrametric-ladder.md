# T-9826 -- Canonical combined Pade approximants form an exact ultrametric ladder

Claim ID: `T-9826`
Title: The combined-moment Pade coefficients have checkerboard sign, their real errors have one sign, and their rational values have exact pairwise 2-adic distances
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-period-ten`
Reviewing agents: `gpt56-synthesis-01`; `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `T-9821`
Scope: every positive periodic stack word and every canonical combined-moment Pade order
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup and exact source assumptions

Use `T-9821/(1)--(3)`.  Thus `r,S,zeta` are positive integers,
the rational moments

\[
 u_N=R^{N(N-1)/2}Z^NP_W(X\lambda^N)               \tag{1}
\]

are positive in the real embedding, and

\[
 H_v=\sum_{N\ge0}u_N                                \tag{2}
\]

converges separately for `v=infinity` and `v=2`.  These two limits are not
identified.

For increasing nonnegative index tuples `mathbf s,mathbf t` of common length
`d`, put

\[
 \Delta(\mathbf s,\mathbf t)
 =\det(u_{s_i+t_j})_{0\le i,j<d}.                   \tag{3}
\]

The exact input from `T-9821/Theorem 1` is

\[
 \Delta(\mathbf s,\mathbf t)\ne0,
 \qquad
 \operatorname{sgn}_\infty\Delta(\mathbf s,\mathbf t)
 =(-1)^{d(d-1)/2}.                                  \tag{4}
\]

For `n>=1`, let

\[
 B_n(Y)=\sum_{k=0}^n b_{n,k}Y^k,qquad b_{n,0}=1,   \tag{5}
\]

be the unique denominator for which the coefficients of `B_n(Y)H(Y)` in
degrees `n,...,2n-1` vanish, and let `A_n(Y)` remove the coefficients below
degree `n`.  Write

\[
 B_n(Y)H(Y)-A_n(Y)
 =\sum_{\ell\ge0}\varepsilon_{n,\ell}Y^{2n+\ell}.  \tag{6}
\]

Finally put

\[
 R_n={A_n(1)\over B_n(1)}\in\mathbf Q,qquad
 E_n=6\left\{2\zeta n+{27Sr\over2}n(n-1)\right\}. \tag{7}
\]

`T-9821/(17),(19)--(21)` supplies

\[
 v_2(B_n(1))=0,qquad
 v_2(H_2-R_n)=E_n.                                  \tag{8}
\]

## Theorem 1 -- checkerboard denominator and one-signed real error

For every `0<=k<=n`,

\[
 \boxed{\operatorname{sgn}_\infty(b_{n,k})=(-1)^k.}\tag{9}
\]

For every `ell>=0`,

\[
 \boxed{
 \operatorname{sgn}_\infty(\varepsilon_{n,\ell})=(-1)^n.
 }                                                   \tag{10}
\]

Consequently the convergent real linear form has the same strict sign:

\[
 \boxed{
 \operatorname{sgn}_\infty
 \{B_n(1)H_\infty-A_n(1)\}=(-1)^n.
 }                                                   \tag{11}
\]

### Proof

Put `c_j=b_(n,n-j)`, so `c_n=1`.  The first `n` cancellation equations are

\[
 \sum_{j=0}^{n-1}u_{i+j}c_j=-u_{i+n}
 \qquad(0\le i<n).                                  \tag{12}
\]

Let `D_n=det(u_(i+j))_(0<=i,j<n)`.  For `0<=j<n`, let `D_(n,j)` be the
minor with the same rows and with its columns written in increasing order as

\[
 \{0,1,\ldots,n\}\setminus\{j\}.                   \tag{13}
\]

Cramer's rule gives

\[
 c_j=(-1)^{n-j}{D_{n,j}\over D_n}.                  \tag{14}
\]

Indeed, the replacement column carries the minus sign in (12), and moving
column `n` from position `j` to its sorted final position uses `n-1-j`
transpositions.  Both determinants in (14) have size `n`, so (4) gives their
ratio positive.  Therefore `sgn(c_j)=(-1)^(n-j)`, and substituting
`j=n-k` proves (9), including `b_(n,0)=1`.

By the Schur-complement identity used in `T-9821`, `epsilon_(n,ell)` is the
quotient of the determinant with row set

\[
 (0,1,\ldots,n-1,n+\ell)                            \tag{15}
\]

and column set `(0,1,...,n)` by `D_n`.  The numerator has size `n+1`, so
its sign divided by that of `D_n` is

\[
 (-1)^{n(n+1)/2-n(n-1)/2}=(-1)^n.                  \tag{16}
\]

This proves (10).  The real error series converges and all of its nonzero
terms have the same sign, so no archimedean cancellation is possible; (11)
follows. **QED**

## Theorem 2 -- exact ultrametric distance ladder

The error radii increase strictly:

\[
 \boxed{
 E_{n+1}-E_n=6\{2\zeta+27Sr\,n\}>0.
 }                                                   \tag{17}
\]

For every `m>n>=1`,

\[
 \boxed{v_2(R_m-R_n)=E_n.}                          \tag{18}
\]

In particular all rational approximants `R_n` are pairwise distinct, so all
projective pairs `(A_n(1):B_n(1))` are pairwise nonproportional.  Moreover,
with the usual reduced rational height,

\[
 \boxed{H(R_m-R_n)\ge2^{E_n}\qquad(m>n).}           \tag{19}
\]

### Proof

Equation (17) is direct subtraction in (7).  For `m>n`, equation (8) and
(17) give

\[
 v_2(H_2-R_n)=E_n<E_m=v_2(H_2-R_m).                 \tag{20}
\]

The ultrametric equality for two terms of unequal valuation, applied to

\[
 R_m-R_n=(H_2-R_n)-(H_2-R_m),                       \tag{21}
\]

proves (18).  Thus the values are distinct, and nonzero rational multiples
of their projective pairs cannot represent the same value.  If a reduced
rational number has positive 2-adic valuation `E_n`, its numerator is
divisible by `2^(E_n)` and its denominator is odd.  This proves (19).
**QED**

## What this closes

The height target in `T-9821/(23)` asked for an infinite subsequence with
nonproportional Pade pairs.  Theorem 2 proves that this auxiliary condition is
automatic for the entire canonical sequence: no order extraction is needed
to ensure distinctness.  It also gives the exact mutual distance, rather than
only convergence to the unknown limit.

Theorem 1 supplies an independent real-place orientation.  It is useful for
future two-place determinant estimates, but it is deliberately stated for
the real series value `H_infinity`; it is not transferred to `H_2`.

## Dependency, novelty, and source audit

- `T-9821` proves arbitrary-minor nonvanishing and common real sign, exact
  coefficient valuations, the denominator-unit property, and the exact first
  evaluated error valuation.  Those are the only inputs here.
- The new conclusions are the checkerboard coefficient signs (9), the
  one-signed full real error (10)--(11), and the exact pairwise distance and
  height ladder (18)--(19).
- `T-9824` gives a positive Schur expansion of one normalized alternant.  It
  is compatible with (4) but is not needed for this proof.
- Live `PR20/L-9418`, `R-9410`, and `T-9422` now optimize and close the
  delayed equal-phase family: it proves periods through nine and still misses
  ten.  The refreshed `PR20/Q-9413` retains direct combined-moment Pade as a
  live route.  Local `T-9821` supplies its cancellation window, nonzero first
  survivor, and odd evaluated denominator; the present theorem makes
  nonproportionality automatic.  Neither result supplies `Q-9413`'s remaining
  reduced-height bound or exponent greater than one.
- No external theorem, finite computation, or unstated specialization result
  is used.

## Gap and scope audit

- Pairwise nonproportionality is not the missing global upper-height estimate
  in `T-9821/(23)`.  Equation (19) is a lower bound and does not prove that
  any approximation exponent exceeds one.
- The real sign (11) concerns `H_infinity`, while (8) concerns `H_2`.
  Equality of these two completion limits is neither assumed nor inferred.
- Alternating coefficient signs do not imply real-rootedness of `B_n`, and no
  root-location claim is made.
- The result is fixed-period.  It does not give period-uniform S-adic bounds,
  period-ten irrationality, or a Collatz conclusion.

## Adversarial checks

- The minus sign in (12) and the `n-1-j` column moves combine to
  `(-1)^(n-j)` in (14).  Omitting either reverses (9).
- A bordered determinant has size `n+1`, not `n`; its sign quotient is exactly
  `(-1)^n`.
- The `+27Sr*n` term in (17) comes from
  `(n+1)n-n(n-1)=2n` and has no half remaining.
- In (21), unequal valuations force equality with the smaller value `E_n`;
  the ultrametric inequality alone would give only a lower bound.
- Reduction of `A_n(1)/B_n(1)` cannot merge two orders, because (18) concerns
  the reduced rational values themselves.
