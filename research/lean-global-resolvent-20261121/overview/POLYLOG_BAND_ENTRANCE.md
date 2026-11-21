# A polylogarithmic clock for the mandatory dyadic band

## Scope and status

This note develops the analytic corollary of the new finite-denominator
entrance argument. The finite argument is elementary; its Lean implementation is
[FastForward.lean](../section/lean/FastForward.lean). The passage from a supplied denominator to the uniform exponent
`4.117` uses a published two-logarithm estimate; that estimate is not installed
as a Lean axiom. All clocks below count the ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

For a positive odd integer `x`, write `d(x)=floor(log_2 x)`. The mandatory
band is the existing, unchanged condition

\[
\operatorname{Mark}(x)\quad\Longleftrightarrow\quad
x\text{ is odd},\qquad
(d(x)+1)(x-2^{d(x)})\le70\,2^{d(x)}.
\]

The new bound concerns the time needed to reach this same band, including
from a trajectory that is not assumed injective. It does not establish
descent between successive visits.

## 1. The finite denominator statement

Put `alpha=log_2 3`. A convenient version of the finite statement is:

> Suppose `q>=16`, `gcd(a,q)=1`, `|q alpha-a|<=1/q`, and
> `d(n)<=q`. Every positive integer `n` has a marked ordinary iterate at a
> clock strictly below `8q+d(n)`.

In particular, for every supplied good denominator `Q`, simultaneously for
all `1<=n<=2^Q`, one has

\[
\boxed{\exists t<9Q:\quad
\operatorname{Mark}(T^t n),\qquad T^t n<2^{10Q}.}
\tag{1}
\]

The second bound uses only `T(v)<=2v`. The Lean statement uses exactly
these constants.

### Why the clock is linear in the supplied denominator

First take an odd source `n`. Set the floor to `m=q^2`. The existing rational
grid argument supplies an odd clock `j<q`. If every state up to the selected
clock remains at least `m`, its phase error is bounded by

\[
0\le\Delta\le \frac3q+\frac j{q^2}\le\frac4q.
\tag{2}
\]

The three units in the first numerator account for the rational grid and the
approximation error of the rotation. The second term is the actual
one-sided accumulated logarithmic perturbation, using
`log_2(1+1/(3x))<=1/x` at each odd state.

The endpoint satisfies `x_j<=2^j n`. Since `d(n)<=q` and `j<q`, its integer
binary height obeys `d(x_j)+1<=2q`. Thus

\[
(d(x_j)+1)\Delta\le8.
\]

The existing logarithmic-to-band comparison accepts any integer below
the endpoint height and therefore gives the original constant-70 mark.
Identifying that integer with the actual binary height is unnecessary;
the finite theorem in Lean in fact needs only `q>0`. Keeping the *actual denominator* in (2) is
essential: replacing `3/q` by a bound involving only an external clock
budget loses this useful cancellation with the endpoint height.

If the orbit instead crosses below `q^2`, stop at such an actual odd state
`x`. The earlier square-root entrance theorem takes fewer than

\[
4\lfloor\sqrt x\rfloor+\lfloor\log_2 x\rfloor<6q
\]

additional shortcut clocks to reach a mark. This use of the earlier theorem
is at the new, much smaller state `x`, not at the original source.

For either branch, the clock spent before that endpoint must be counted
correctly. If `A_j` is the total number of removed factors of two in the
first `j` accelerated odd steps, the exact weight estimate gives

\[
2^{A_j}x_j\le4^j n.
\]

Because `x_j>=1`, it follows that `A_j<=2j+d(n)`. The stronger estimate
`A_j<=2j` would require the extra premise `x_j>=n` and is not available in
the floor-crossing branch. Combining the valid clock bound with the less
than `6q` fallback gives the less than `8q+d(n)` total.

For an even source write `n=2^r n_odd` with `n_odd` odd. The initial `r`
halvings and the odd-source height account add exactly:
`r+d(n_odd)=d(n)`. Thus the same statement holds for every positive source.

No orbit-packing theorem, predecessor-density theorem, probabilistic
valuation model, or injectivity premise is used in this finite proof.

## 2. The external number-theory input, checked at its actual scope

Wu and Wang's original published Theorem 1 states a lower bound for a
linear form in **all three of `1`, `log 2`, and `log 3`**. Its exponent is
`4.1163051+epsilon`, for every positive `epsilon`, above an effectively
computable coefficient threshold. In their notation the coefficient height
is `H=max(|q_1|,|q_2|)`. Set the constant coefficient to zero, take
`q_1=-a` and `q_2=q`, and divide the resulting bound by `log 2`.

Choose `epsilon=0.0006949`. For the numerators relevant to rational
approximation of `alpha`, one has `|a|=O(q)`. Absorbing the finitely many
smaller coefficient heights into a positive constant gives

\[
\boxed{|q\alpha-a|\ge c q^{-\tau}
\quad(q\ge1,\ a\in\mathbb Z),\qquad \tau=4.117.}
\tag{3}
\]

For numerators far from `q alpha`, the estimate follows immediately after
decreasing `c`, so it holds for every integer `a`. The constant is not
numerically extracted in this checkpoint. In particular no numerical
finite-verification threshold is claimed.

This is also stated in the form needed here in Fan, Queffelec and
Queffelec, Theorem 2.1. Their definition immediately before that theorem
uses `||q beta||>=c q^{-rho}`, with `beta=log_3 2`, and gives
`rho=4.117`. The reciprocal has the same exponent: for the nearest integer
`a` to `q alpha`,

\[
|q\alpha-a|=\alpha|a\beta-q|
\ge\alpha\,\|a\beta\|\gg a^{-\tau}\gg q^{-\tau}.
\]

The distinction between a bound for a single logarithm and a bound for a
ratio of logarithms matters. The justification here is Wu--Wang's actual
linear-form theorem, corroborated by the explicit ratio formulation in
Fan--Queffelec--Queffelec; it does not infer a ratio estimate merely from
the title or the corollary about `log 3`.

Sources:

- Qiang Wu and Lihong Wang, *On the irrationality measure of log 3*,
  Journal of Number Theory 142 (2014), 264--273, Theorem 1.
  [DOI](https://doi.org/10.1016/j.jnt.2014.03.007).
  The publisher-indexed introduction exposes the theorem and its
  `4.1163051+epsilon` exponent. The direct DOI redirect was unavailable
  during this session; the claim is additionally checked against the
  accessible published source below.
- Aihua Fan, Herve Queffelec and Martine Queffelec,
  *The Furstenberg set and its random version*, L'Enseignement Mathematique
  70 (2024), 61--120, definition on p.70 and Theorem 2.1 on p.71.
  [DOI](https://doi.org/10.4171/LEM/1040) and
  [published PDF](https://ems.press/content/serial-article-files/47663).

## 3. Choosing a good denominator without a source-sized clock

Let `D=max(16,d(n))`, and choose the first continued-fraction denominator
`q_k>=D` for `alpha`. Its predecessor satisfies `q_(k-1)<D`. Standard
convergent inequalities and (3) give

\[
cq_{k-1}^{-\tau}
\le |q_{k-1}\alpha-a_{k-1}|
<\frac1{q_k},
\qquad
q_k<c^{-1}D^\tau.
\tag{4}
\]

The new convergent is coprime and satisfies
`|q_k alpha-a_k|<1/q_k`, so it is a valid supplied denominator in Section 1.
Consequently an absolute constant `C` gives

\[
\boxed{\tau_{\rm mark}(n)
\le C(1+\log n)^{4.117}\qquad(n\ge1).}
\tag{5}
\]

Here `tau_mark(n)` is the first nonnegative **ordinary shortcut** clock at
which the orbit is marked. The exponent is uniform in the prescribed
source. All small inputs are covered by enlarging `C`. More generally,
the same proof works with any fixed exponent greater than `4.1163051`,
with a constant depending on that choice.

This argument does not claim bounded partial quotients for `log_2 3`.
The polynomial jump bound (4), rather than a bounded ratio of consecutive
denominators, is exactly what the published estimate supplies.

The height of the entrance is controlled as well:

\[
E(n)=T^{\tau_{\rm mark}(n)}n
\le n\,2^{\tau_{\rm mark}(n)},\qquad
1+\log E(n)\le C'(1+\log n)^{4.117}.
\tag{6}
\]

The bound on the **value** is therefore of the form
`exp(O((log n)^4.117))`; it is the **clock** that is polylogarithmic.

## 4. Consequences that preserve the prescribed source

### Positive marked returns

Apply (5) to `T(n)` and add the initial step. Since `T(n)<=2n`, the first
positive marked return from any marked positive source satisfies

\[
\tau^+_{\rm mark}(n)\le C''(1+\log n)^{4.117}.
\tag{7}
\]

This allows recurrent or periodic trajectories. It also allows the return
value to be larger than the source.

### A larger quantitative merger budget

Suppose an ordinary partner `u>0` has a supplied physical merger
`T^a(u)=T^b(n)`. At a good scale `Q`, assume

\[
u\le2^Q,\qquad 2^{10Q}\le n.
\]

Equation (1) supplies a marked `y=T^t(u)<n` with `t<9Q`. Its common
endpoint with the prescribed source remains explicit:

\[
T^a(y)=T^{b+t}(n).
\tag{8}
\]

This is the ordinary-component version of the lower-mark induction
interface developed in PR184. It replaces its former square-root entrance
cost by a linear cost at compatible good scales. For arbitrary large `n`,
(4) shows that a sufficient partner range is

\[
u\le\exp\!\big(c_1(\log n)^{1/4.117}\big)
\tag{9}
\]

with a sufficiently small absolute `c_1>0`. Indeed the resulting good
denominator has `10Q<=log_2 n`. This is a broader allowable partner range
than a fixed power of `log n`. The existence of such a partner for **each
prescribed marked source** remains unproved.

### Source-weighted entrance moments

For every `s>1` and every finite `p>=0`, (6) gives the convergent series

\[
\sum_{n\ge1}n^{-s}(1+\log E(n))^p<\infty.
\tag{10}
\]

To prove it, majorize by a constant times
`sum n^{-s}(1+log n)^(4.117p)`; any fixed logarithmic power is eventually
smaller than `n^((s-1)/2)`. These are weights on the original source, so
the statement remains valid when many sources share one marked entrance.
It supplies no contraction of the total surviving source mass.

## 5. Relation to earlier work and the remaining full-theorem step

The older ingredients have distinct roles:

- PR173 supplies the actual forced band and the square-root fallback.
- PR184 separates the odd-step clock from the floor and retains the
  integer phase carry. The finite argument here chooses the floor from
  the actual rational denominator and uses the fallback after crossing it.
- PR145 already contains a limiting phase for a divergent ordinary orbit,
  a future-minimum tail estimate, polynomial-clock equidistribution, and
  the numerical discrepancy exponent `1000/5117`, in
  `research/binary-run-occupancy/MELLIN_PHASE.md` at
  `dd245a712f985909f541590e3f6c179b7ba011e4`.
  None of those phase results is claimed as new here.

The novelty check searched all 143 available PR descriptions and the
research/report trees of the 27 PR heads present in the checkout. It found
no earlier stated polylogarithmic entrance clock for the constant-70
mandatory band. This is a repository-scoped comparison, not a claim of
literature priority or a full source audit of every historical head. The
[machine-readable search record](../../../reports/2026-11-21-lean-global-resolvent/checkpoint6-novelty-search.json)
is retained with the execution reports.

The improvement narrows a quantitative interface. It does not recover the
integer valuation cocycle erased by leading-phase rotation. A hypothetical
trajectory can visit this band within the stated clock repeatedly while
its successive marked values increase. The proof also allows a nontrivial
cycle to keep revisiting the band. To finish the full theorem one still
needs a source-preserving descent or smaller-component-partner theorem, or
an all-time fixed-floor survivor estimate that excludes both possibilities.

In particular, the recently inspected manuscript [*Ternary harmonic moments
and Collatz orbit occupation*](https://rstation.ai/problems/collatz/papers/176),
rStation paper 176 (19 November 2026), gives
its finite survival improvements at a clock tied to a **growing floor**
`M`, including a proportional extension of `floor(log_2 M)`. Its stated
estimate is not an all-time estimate at one fixed floor; it cannot simply
be iterated on the conditional distribution of the surviving ordinary
sources. No such iteration is used here.
