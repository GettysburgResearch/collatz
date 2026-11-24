# A direct critical-exponent count for separated visits on one orbit

**Status: elementary written reconstruction, independently checked in this
round; not a new literature record and not a convergence proof.** The finite
complete-carry compression step is separately formalized in
`OrbitCounting.lean`. The binomial asymptotics and infinite counting argument
below are written mathematics, not claimed as Lean-checked.

The repository input used in our previous pressure construction was the
explicit estimate `4 X^(39/40)` for all odd states below `X` on an escaping
orbit. PR185's current critical-exponent argument bounds a consecutive
segment that stays below a height. Here a short recursive charging argument
obtains the critical exponent for **all** visits below a height, even when
arbitrarily large excursions separate them. It uses no harmonic flow,
predecessor-population assertion, or distributional premise.

A priority check during this derivation found stronger existing work.
Lyapunov Weaver's [*A power improvement for uniform Collatz interval
compression*, Paper 28, v3, 26 October 2026](https://rstation.ai/problems/collatz/papers/28)
already states an effective full-orbit estimate with a `(log X)^(-3/2)`
factor in equation (24), through a more general translated-interval
compression theorem. The earlier [23 October discussion](https://rstation.ai/r/collatz/posts/36)
has the critical exponent and square-root logarithmic saving. That source
credits Garcia--Tal and Leen for earlier compression mechanisms. We do not
claim priority for the exponent, logarithmic saving, or global orbit sparsity.
We inspected the stronger statements but did not independently audit the
entire paper's analytic chain or import its later ineffective power gain.
The contribution here is a self-contained odd-clock proof and its explicit
connection to the pressure and collision interfaces currently used in this
branch.

## 1. Statement and exact domain

Let

\[
U(n)=(3n+1)/2^{v_2(3n+1)}
\]

on positive odd integers. Let `S` be a set of positive odd integers with
`U(S) subset S`, such that the restriction of `U` to `S` is injective. Put

\[
 F_S(X)=\#\{n\in S:n\le X\},\qquad
 \alpha=\log_3 2,\qquad
 \theta=H_2(\alpha)=0.949955527188\ldots.
\]

**Theorem.** There is an absolute constant `C` such that, uniformly in
every such `S` and every real `X>=1`,

\[
\boxed{F_S(X)\le C\,\frac{X^\theta}{\sqrt{1+\log X}}.}
\tag{1}
\]

An entire injective odd forward orbit satisfies these hypotheses. So does
a positive odd cycle, and even the union of all positive odd periodic
points: each periodic point has exactly one periodic predecessor. A
general predecessor basin does not satisfy injectivity. A truncated orbit
segment is not forward invariant; its missing terminal images must be
paid for separately. We do not silently replace either of these domains
by `S`.

## 2. The full ordered affine identity

For one actual source `n` and its next `m>=1` odd transitions, write the
positive gaps as `g_1,...,g_m`, their partial sums as `A_i`, and
`A=A_m`. The endpoint `q=U^m(n)` satisfies

\[
 2^A q=3^m n+C(g),\qquad
 C(g)=\sum_{i=0}^{m-1}3^{m-1-i}2^{A_i}.
\tag{2}
\]

Every `g_i>=1`, hence `A-A_i>=m-i`. Consequently

\[
0<\frac{C(g)}{2^A}
 \le\sum_{d=1}^m\frac{3^{d-1}}{2^d}
 =(3/2)^m-1.
\tag{3}
\]

No bound on the intermediate ordinary heights was used. The complete
carry is kept; replacing it by zero would be an invalid compression.

A prescribed positive gap composition of total `A` specifies exactly
one odd residue modulo `2^(A+1)`. The first `A` shortcut bits are
`1 0^(g_1-1) ... 1 0^(g_m-1)`, and the final endpoint must also be odd.
The ordinary parity-prefix bijection at length `A+1` gives the asserted
residue and the exact valuations. There are
`binom(A-1,m-1)` positive gap compositions of total `A`.

## 3. Charge large total clocks to a smaller part of the same set

Fix `X>=24`, and choose

\[
 K=\lfloor\log_2 X\rfloor,\qquad
 m=\lfloor\log_3(X/8)\rfloor\ge1.
\tag{4}
\]

For each source in `S intersect [1,X]`, read its actual next **same
number `m` of odd steps**. Its total binary clock `A` is allowed to vary.
If `A>=K`, equations (2)--(4) give

\[
q\le\frac{3^m X}{2^A}+(3/2)^m-1
 <2\,3^m+3^m\le3X/8<X/2.
\tag{5}
\]

The endpoint is in `S` by forward invariance. Moreover `U^m` is
injective on `S`, by iteration of the same injective restriction. Thus
**all** the sources with `A>=K` inject into `S intersect [1,X/2]`.
Their number is at most `F_S(X/2)`.

This is the step that removes the contiguous-window restriction. The
ordinary clocks differ, but the odd clock does not. Neither intermediate
excursions nor the distances between selected visits affect the
injection. Applying different odd-step counts to different sources would
not justify it.

## 4. Count the remaining complete words at the critical slope

For `A<K`, a single residue modulo `2^(A+1)` contributes at most
`X/2^(A+1)+1` positive sources below `X`. Since `A<=K-1`, this is
at most `X/2^A`. Summing the positive compositions gives the exact
finite upper bound

\[
 L(X)\le X\sum_{A=m}^{K-1}
       \binom{A-1}{m-1}2^{-A}
 =\frac{X}{2^{K-1}}
       \sum_{j=m}^{K-1}\binom{K-1}{j}.
\tag{6}
\]

The last identity counts fair binary words by the position of their
`m`th one. It is a finite combinatorial identity, not an assertion that
actual gaps are independent random variables. An empty sum is zero.

For completeness, the asymptotic estimate in (6) can be checked directly.
Put `t=K-1`. Equation (4) gives `m=alpha*t+O(1)`, with an absolute
bounded error. Since `1/2<alpha<1`, for all large `t` the ratio of
successive terms in the upper binomial tail is bounded above by one
fixed `rho<1`:

\[
\frac{\binom t{j+1}}{\binom tj}=
\frac{t-j}{j+1}\le\rho\qquad(j\ge m).
\]

Therefore the tail is at most `binom(t,m)/(1-rho)`. Stirling's factorial
bounds, uniformly with `m/t` in a fixed compact subinterval of `(0,1)`,
give

\[
\binom tm=O\!\left(t^{-1/2}2^{tH_2(m/t)}\right).
\]

The entropy function has bounded derivative near `alpha`, so
`t H_2(m/t)=t H_2(alpha)+O(1)=theta*t+O(1)`.
Finally `2^K<=X<2^(K+1)` and `X/2^(K-1)<4`. Thus (6) yields

\[
 L(X)=O\!\left(\frac{X^\theta}{\sqrt{\log X}}\right),
\tag{7}
\]

with an absolute implied constant. The finitely many smaller `t` are
absorbed into that constant.

## 5. Iterate the scale inequality

Equations (5)--(7) prove

\[
F_S(X)\le F_S(X/2)+
 C_0\frac{X^\theta}{\sqrt{1+\log X}}
\tag{8}
\]

for all sufficiently large `X`. No induction on a conjecturally
convergent source is involved.

Iterate until the height is below a fixed absolute cutoff. In the part
where `X/2^i>=sqrt X`, every denominator is at least a constant times
`sqrt(1+log X)`, and the numerator factors `2^(-theta*i)` have a
convergent geometric sum. The remaining terms sum to `O(X^(theta/2))`
by the same geometric bound with denominator at least one. The final
finite-height count is absolutely bounded. Both contributions are
absorbed by the right side of (1). This proves the theorem uniformly
over `S`.

The finite inequality (6), rather than a floating approximation to
`theta`, is the exact arithmetic interface used in the replay controls.
No explicit optimized value of the absolute constant `C` is claimed.

## 6. Consequences for the present pressure construction

For any `s>theta`, Tonelli gives a uniform moment bound

\[
\sum_{n\in S}n^{-s}
=s\int_1^\infty F_S(t)t^{-s-1}\,dt<\infty.
\tag{9}
\]

This concerns the distinct states in `S`; it is not a sum over repeated
cycle visits or over a whole branching predecessor basin. The endpoint
`s=theta` is not covered: the resulting integral has a
`1/(t sqrt(log t))` upper integrand, which does not converge.

If all elements of `S` are at least `M>=2`, (1) implies

\[
\sum_{n\in S}\frac1n
 \le\frac{C}{1-\theta}
       \frac{M^{\theta-1}}{\sqrt{1+\log M}}.
\tag{10}
\]

Indeed use `sqrt(1+log t)>=sqrt(1+log M)` in the integral from `M`
to infinity. This strengthens the local bound used in
[`SOURCE_CLOSURE.md`](../closure-round2-20261123/SOURCE_CLOSURE.md)
at large component floors, without importing the stronger external
compression theorem.

For an escaping unit component of minimum `M`, every forward path has
that floor, so its correction product obeys

\[
\Lambda(n)\ge
\exp\!\left[-\frac{C}{3(1-\theta)}
\frac{M^{\theta-1}}{\sqrt{1+\log M}}\right].
\tag{11}
\]

The previously proved attained pressure maximum `m` therefore satisfies

\[
1\le\frac mM\le
\exp\!\left[\frac{C}{3(1-\theta)}
\frac{M^{\theta-1}}{\sqrt{1+\log M}}\right].
\tag{12}
\]

This is a sharper quantitative localization of the **same** maximum.
It does not prove `m=M`, eliminate its positive pressure atom, or
construct a triadic dual. Even the prior stronger literature sparsity
statements leave those tasks open.

## 7. Why the new finite collision decomposition still matters

The [companion note](ACTUAL_COLLISION.md) retains the full source and
splits actual windows by total clock, complete carry quotient, and
source quotient. Inside each such box there are no distinct-occurrence
residue collisions. Formula (1) limits the global number of possible
ordinary sources below a height, but it does not bound the number or
mass of boxes contributing to one ternary residue at unbounded heights.
Using the count as if it were a uniform moving-root density estimate
would restore precisely the unproved transfer step.

The unresolved task remains a quantitative bound on those actual
cross-box overlaps, or a source construction that forces an original
orbit to meet a smaller known source. No convergence conclusion is
drawn from (1), (10), or (12).

## 8. Frozen repository inputs and verification boundary

- PR177 at `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
  `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`,
  HE2: the prior coarse cylinder count and positive path product.
- PR185 at `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
  `research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`:
  the critical entropy exponent, same-law collision target, and explicitly
  contiguous-window height bound. Its deeper harmonic-flow hypotheses are
  not premises of the present argument.
- Parent `b78819e95ee7d39f02022de991b42217821e7590`,
  `research/closure-round2-20261123/SOURCE_CLOSURE.md` and
  `TwoSidedPressure.lean`: the attained ordinary maximum used in (12).

The new Lean module proves a full-carry upper bound, the exact high-clock
compression implication, and the finite injection charge. It does not
formalize Stirling, the critical entropy asymptotics, the infinite orbit
set, or the displayed integral consequences. The independent reviews
and actual execution receipts are in the accompanying report directory.
