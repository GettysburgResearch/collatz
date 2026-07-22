# L-9891 -- Exact rank of adjacent equal-allocation Pade tails

Claim ID: `L-9891`
Title: Every finite adjacent-order Casoratian is nonzero, and q neighboring tails cancel exactly q-1 further blocks
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: none
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR20/L-9408`, `PR20/L-9410`, `L-9884`
Scope: scalar combinations of monomial-aligned, equal-allocation periodic block-Pade errors
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Use the equal-allocation periodic Pade family of `PR20/L-9410` and `L-9884`.
Thus the displayed positive word has length `r`,

\[
T={64\over81},\qquad S=S(W)>0,
\qquad Z=T^\zeta,
\tag{1}
\]

and the order-`t` error is

\[
E_t(Y)
=B_t(Y)F(Y)-A_t(Y).
\tag{2}
\]

Put

\[
N_t=(r+1)t
\tag{3}
\]

and expand the completed-window tail as

\[
E_t(Y)
=Y^{N_t}\sum_{\ell\ge0}g_{t,\ell}Y^\ell.
\tag{4}
\]

The coefficient `g_(t,ell)` is the combined phase coefficient called
`a_(N_t+ell)` in `L-9884`, with the root set belonging to order `t`.
In particular it is nonzero. Write

\[
V(t,\ell)=v_2(g_{t,\ell}).
\tag{5}
\]

If

\[
L_{r,t}
={t[tr(r^2+r+1)-r^2-2r]\over2},
\tag{6}
\]

then `L-9884/(21)` gives

\[
\boxed{
V(t,\ell)
=6\left\{
 \zeta((r+1)t+\ell)
 +9S\left[
 L_{r,t}+rt\ell+{r\ell(\ell-1)\over2}
 \right]
 \right\}.
}
\tag{7}
\]

## Statement 1 -- a strict valuation anti-Monge law

There are functions of one variable `U(t)` and `W(ell)` such that

\[
\boxed{
V(t,\ell)=U(t)+W(\ell)+54Sr\,t\ell.
}
\tag{8}
\]

Consequently every adjacent valuation square has the exact positive mixed
difference

\[
\boxed{
V(t,\ell)+V(t+1,\ell+1)
-V(t,\ell+1)-V(t+1,\ell)
=54Sr>0.
}
\tag{9}
\]

In particular, the first adjacent Casoratian is always nonzero:

\[
\mathcal C_{t,\ell}
=
\det\begin{pmatrix}
g_{t,\ell}&g_{t,\ell+1}\\
g_{t+1,\ell}&g_{t+1,\ell+1}
\end{pmatrix}
\ne0,
\tag{10}
\]

and its exact valuation is the valuation of its antidiagonal term,

\[
\boxed{
v_2(\mathcal C_{t,\ell})
=V(t,\ell+1)+V(t+1,\ell).
}
\tag{11}
\]

## Statement 2 -- every finite adjacent Casoratian

Fix integers `q>=2`, `n>=1`, and `ell>=0`. Define

\[
\Delta_{q,n}(\ell)
=
\det
\begin{pmatrix}
g_{n,0}&g_{n,1}&\cdots&g_{n,q-2}&g_{n,\ell}\\
g_{n+1,0}&g_{n+1,1}&\cdots&g_{n+1,q-2}&g_{n+1,\ell}\\
\vdots&\vdots&&\vdots&\vdots\\
g_{n+q-1,0}&g_{n+q-1,1}&\cdots&g_{n+q-1,q-2}&g_{n+q-1,\ell}
\end{pmatrix}.
\tag{12}
\]

For `0<=ell<q-1`, this determinant is zero because its last column repeats an
earlier column. For every `ell>=q-1`, it is nonzero, with exact valuation

\[
\boxed{
v_2(\Delta_{q,n}(\ell))
=V(n,\ell)
 +\sum_{i=1}^{q-1}V(n+i,q-1-i).
}
\tag{13}
\]

The determinant valuations strictly increase with the last column:

\[
\boxed{
v_2(\Delta_{q,n}(\ell+1))
-v_2(\Delta_{q,n}(\ell))
=6\{\zeta+9Sr(n+\ell)\}>0.
}
\tag{14}
\]

Thus the whole infinite adjacent coefficient matrix `(g_(t,ell))` has full
rank on every finite block of consecutive rows and initial consecutive
columns.

## Proof of Statements 1 and 2

Equation (7) separates as (8) with

\[
U(t)=6\{\zeta(r+1)t+9S L_{r,t}\},
\tag{15}
\]

\[
W(\ell)=6\left\{\zeta\ell
+9S{r\ell(\ell-1)\over2}\right\}.
\tag{16}
\]

This proves (9). In (10), the diagonal product has valuation exactly `54Sr`
larger than the antidiagonal product. The ultrametric inequality with a unique
minimum therefore proves (11), including nonvanishing.

For `ell>=q-1`, list the distinct column indices in (12) in increasing order
as

\[
c_0=0,c_1=1,\ldots,c_{q-2}=q-2,c_{q-1}=\ell.
\tag{17}
\]

The term indexed by a permutation `pi` has valuation

\[
\sum_{i=0}^{q-1}U(n+i)
+\sum_{j=0}^{q-1}W(c_j)
+54Sr\sum_{i=0}^{q-1}(n+i)c_{\pi(i)}.
\tag{18}
\]

The first two sums and the part containing `n` do not depend on `pi`.
Because both `i` and `c_i` are strictly increasing, the rearrangement
inequality says that

\[
\sum_i i c_{\pi(i)}
\tag{19}
\]

has a unique minimum at the reverse permutation. Therefore the determinant
expansion has one term of uniquely least 2-adic valuation. It cannot cancel.
The reverse assignment sends row zero to column `ell` and row `i>=1` to
column `q-1-i`, which proves (13).

Only the row-zero term changes when `ell` is increased by one in (13).
Equation (7) gives

\[
V(n,\ell+1)-V(n,\ell)
=6\{\zeta+9Sr(n+\ell)\},
\tag{20}
\]

proving (14). **QED**

## Statement 3 -- exact rank of the aligned adjacent-order repair

Align the first errors of orders `n,...,n+q-1` at the leading degree

\[
N_*=(r+1)(n+q-1).
\tag{21}
\]

For `0<=i<q`, put

\[
s_i=(r+1)(q-1-i),
\qquad
\widetilde E_i(Y)=Y^{s_i}E_{n+i}(Y).
\tag{22}
\]

Thus

\[
\widetilde E_i(Y)
=Y^{N_*}\sum_{\ell\ge0}g_{n+i,\ell}Y^\ell.
\tag{23}
\]

Let `M_i` be the `(q-1)`-square minor obtained from the first `q-1`
coefficient columns `0,...,q-2` by deleting row `i`, and set

\[
d_i=(-1)^{i+q-1}\det M_i.
\tag{24}
\]

The canonical coupled error

\[
\mathcal E_{q,n}(Y)
=\sum_{i=0}^{q-1}d_i\widetilde E_i(Y)
\tag{25}
\]

has the exact expansion

\[
\boxed{
\mathcal E_{q,n}(Y)
=Y^{N_*}\sum_{\ell\ge q-1}\Delta_{q,n}(\ell)Y^\ell.
}
\tag{26}
\]

In particular, it cancels exactly `q-1` additional block coefficients and no
more. After evaluation at `Y=1`, its first remaining term is still uniquely
minimal:

\[
\boxed{
v_2(\mathcal E_{q,n}(1))
=v_2(\Delta_{q,n}(q-1)).
}
\tag{27}
\]

The coupling is a genuine rational approximant, not merely a formal error
identity. Put

\[
\mathcal B_{q,n}
=\sum_{i=0}^{q-1}d_iB_{n+i}(1),
\qquad
\mathcal A_{q,n}
=\sum_{i=0}^{q-1}d_iA_{n+i}(1).
\tag{27a}
\]

Then

\[
\boxed{
\mathcal B_{q,n}\ne0,
\qquad
v_2(\mathcal B_{q,n})=v_2(d_{q-1}).
}
\tag{27b}
\]

The normalized coupled approximant has exact error valuation

\[
\boxed{
v_2\!\left(
F(1)-{\mathcal A_{q,n}\over\mathcal B_{q,n}}
\right)
=V(n+q-1,0)
+6(q-1)\{\zeta+9Sr(n+q-2)\}.
}
\tag{27c}
\]

This order is optimal among all scalar combinations of the `q` aligned
errors. If rational scalars `x_0,...,x_(q-1)` satisfy

\[
\sum_i x_i\widetilde E_i(Y)
=O(Y^{N_*+q}),
\tag{28}
\]

then every `x_i=0`.

### Proof

Laplace expansion of (12) along its last column gives

\[
\sum_i d_i g_{n+i,\ell}=\Delta_{q,n}(\ell).
\tag{29}
\]

For `0<=ell<q-1`, the last column repeats one of the first `q-1` columns,
so the right side is zero. At `ell=q-1`, Statement 2 says it is nonzero.
This proves (26) and exact cancellation order.

Equation (14) makes the valuations of all coefficients on the right of (26)
strictly increasing. The series converges 2-adically, so its value at `Y=1`
has the valuation of its first term, proving (27).

Every cofactor `d_i` is itself a determinant with strictly increasing row and
column indices, so the reverse permutation is again its unique
least-valuation term. Comparing the minors that omit consecutive rows gives

\[
v_2(d_{i+1})-v_2(d_i)
=U(n+i)-U(n+i+1)-54Sr(q-2-i)<0.
\tag{29a}
\]

Indeed, the reverse matchings differ only in whether the common column
`q-2-i` is assigned to row `n+i` or `n+i+1`, while

\[
U(t+1)-U(t)
=6\left\{
\zeta(r+1)
+9S\left[
r(r^2+r+1)t+{r(r^2-1)\over2}
\right]
\right\}>0.
\tag{29b}
\]

Thus `d_(q-1)` is the unique cofactor of least valuation. Each `B_t(1)` is a
2-adic unit by `PR20/L-9410`, so the ultrametric inequality proves (27b).
At `Y=1`, equation (25) is

\[
\mathcal E_{q,n}(1)
=\mathcal B_{q,n}F(1)-\mathcal A_{q,n}.
\tag{29c}
\]

The reverse term in `Delta_(q,n)(q-1)` has valuation

\[
\sum_{i=0}^{q-1}V(n+i,q-1-i),
\tag{29d}
\]

whereas `d_(q-1)` has valuation

\[
\sum_{i=0}^{q-2}V(n+i,q-2-i).
\tag{29e}
\]

For every `0<=i<=q-2`, the difference between the corresponding summands is

\[
V(n+i,q-1-i)-V(n+i,q-2-i)
=6\{\zeta+9Sr(n+q-2)\}.
\tag{29f}
\]

Subtracting (29e) from (29d), retaining the final term `V(n+q-1,0)`, and
using (27) and (27b) proves (27c).

Finally, (28) says that the vector `(x_i)` lies in the left kernel of the
`q`-square matrix with columns `0,...,q-1`. Its determinant is
`Delta_(q,n)(q-1)`, which is nonzero by Statement 2. Hence the kernel is
trivial. **QED**

## Statement 4 -- the normalized period-four width benchmark

Fix the word `W` and starting height `m`, hence also `r,S,zeta`, while `n`
and `q` grow.

The best constituent in (25) is the order `n+q-1` Pade error. Statement 3
shows that `q` scalar-coupled adjacent orders buy exactly

\[
\ell=q-1
\tag{30}
\]

additional zero blocks beyond that constituent, before any height analysis.
After cofactor normalization, (27c) gives the exact valuation gain rather
than merely the formal cancellation order.

Put

\[
t=n+q-1,
\qquad
{q-1\over t}\longrightarrow\theta.
\tag{31}
\]

Grant optimistically that the cofactor coupling has zero quadratic height
cost and retains the raw order-`t` height coefficient of `PR20/L-9410`. Then
the exact normalized-error benchmark is

\[
\boxed{
\mu_r^{\rm adj}(\theta)
={6\over\log_2 81}
 {r^2+r+1+2\theta\over r(r+1)}.
}
\tag{32}
\]

In particular, fixed `q`, logarithmic `q`, and every `q=o(n)` leave the old
quadratic exponent unchanged. At period four, even this deliberately
cost-free unchanged-height model requires

\[
\boxed{
\theta>\theta_4^{\rm adj}
={{10\over3}\log_2 81-21\over2}
=0.066416671474\ldots .
}
\tag{33}
\]

If `q/n -> rho`, then `theta=rho/(1+rho)`, so equivalently

\[
\boxed{
\rho>{\theta_4^{\rm adj}\over1-\theta_4^{\rm adj}}
=0.071141664000\ldots .
}
\tag{34}
\]

Equations (33)--(34) are the exact width boundary only inside this stipulated
unchanged-height benchmark. They are neither necessary nor sufficient for the
actual reduced coupled approximants: an unknown quadratic height saving could
win below the boundary, while cofactor height cost could lose above it.

### Proof

After removing the common factor `9S`, the quadratic part of the leading
order-`t` valuation is

\[
{r\over2}(r^2+r+1)t^2.
\tag{35}
\]

Equation (27c) adds

\[
r(q-1)(t-1)=r\theta t^2+o(t^2).
\tag{36}
\]

The unchanged raw height has quadratic coefficient

\[
{r^2(r+1)\over2}t^2.
\tag{37}
\]

Their ratio, with the place-conversion factor `6/log_2(81)`, is (32).
Solving `mu_4^(adj)(theta)>1` gives (33), and substituting
`theta=rho/(1+rho)` gives (34). **QED**

## What this advances

- It proves exact nonvanishing of every finite adjacent-order error
  Casoratian, including the first 2-by-2 construction proposed in
  `PR20/Q-9412`.
- It constructs the canonical `q`-order coupled linear form, locates its first
  nonzero coefficient, and proves the exact 2-adic valuation of its evaluated
  error.
- It shows that two adjacent orders cancel exactly one extra block. Any
  bounded-width adjacent-order determinant is therefore quadratically
  invisible as a cancellation-and-normalized-valuation mechanism at the
  period-four frontier.
- It converts the vague requirement of "linearly many neighboring pairs" into
  the explicit unchanged-height target `q>0.07114166n` asymptotically.

## Dependency audit

- `PR20/L-9408` and `PR20/L-9410` supply the rational periodic Pade errors.
- `L-9884/(21)` supplies the exact valuation (7), including combined-phase
  noncancellation at every tail coefficient.
- `PR20/L-9410` supplies the raw height coefficient used in the deliberately
  optimistic comparison of Statement 4.
- The remaining proof is finite determinant algebra, the rearrangement
  inequality, and the ultrametric inequality.

## Gap audit

- The claim treats equal allocation and scalar combinations after the unique
  monomial shifts that align their first errors. General polynomial
  multipliers in `Y` and phase-sensitive Hermite-Pade systems are outside it.
- Cofactor denominators and reduced global height are not bounded. When `q`
  grows linearly, their cost can itself be quadratic or worse.
- Extra 2-adic factors shared by the coupled numerator and denominator could
  change the reduced height. No such factor is proved or excluded.
- Statement 4 grants zero cofactor-height cost and is not an irrationality
  exponent for the coupled form.
- No period-four value theorem or Collatz conclusion is claimed.

## Adversarial checks

- The entries `g_(t,ell)` are the combined phase coefficients, not their
  phase-zero summands. Their exact valuations are available only because
  `L-9884` first excluded all post-window phase cancellation.
- The last column in (12) is distinct precisely because `ell>=q-1`.
- The reverse permutation is uniquely minimizing; equal valuations cannot
  cancel the claimed determinant term.
- The `Y` shifts in (22) are essential for formal coefficient alignment even
  though they all become one at `Y=1`.
- For `q=2`, the diagonal product exceeds the antidiagonal product by exactly
  `54Sr`, agreeing with (9).
- The width ratio in (31) is measured against the highest constituent order
  `n+q-1`, not the lowest order `n`.

## Remaining uncertainty

What is the reduced global height of the cofactor vector `(d_i)` when
`q=rho*n`? Exact nonvanishing and exact cancellation depth are now closed; the
period-four question has moved to a determinant-height problem.

## Suggested next attack

Use the same reverse-permutation valuation structure to factor the predictable
power of `T` from every cofactor, then bound the common odd denominator and
archimedean size of the normalized `q`-order determinant. Compare the resulting
quadratic height coefficient with the width threshold (31).
