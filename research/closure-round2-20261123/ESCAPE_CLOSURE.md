# Pressure poles: a complete ordinary-source summation and its boundary

Date: 2026-11-23. **Written deductions; escape exclusion remains OPEN.**
This attack tried to construct a positive pressure barrier integrable
against an escaping component's atomic measure. It identifies a genuine
range in which each rational pole is integrable and evaluates the entire
propagated pole family under two different reference measures. Neither
estimate is an upper bound for the retained escaping measure.

The new ordinary excessive-measure identity in Section 2 was supplied by
the principal research agent during this pass. The rational-pole estimates,
their complete Green consumer, and the pressure-window calculation below
were developed in this lane. These are written proofs, not additional Lean
declarations or assertions of external peer review.

## 1. Exact operator and the attempted completion

Let `O` be the positive odd integers prime to three, embedded in
`X=Z_3^times`. Use

\[
 U(n)=\frac{3n+1}{2^{a(n)}},\quad a(n)=v_2(3n+1),\quad
 \lambda(n)=\frac{3n}{3n+1},\qquad
 (P_s f)(q)=\sum_{\substack{e\ge1\\I_e(q)\in X}}
       (3/2^e)^s f(I_e(q)),\quad I_e(q)=\frac{2^eq-1}{3}.
 \tag{1}
\]

At a root in `O`, every displayed child is an actual positive odd unit,
and its exponent is the exact odd-map valuation. The sum is nonnegative
throughout this note. Periodic roots are retained here.

The main source is PR177 at
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`.
Its elementary counting argument proves that an escaping ordinary orbit
has a positive infinite correction product. Thus, for each escaping
component `E` and `s>1`,

\[
 \mu_{E,s}=\sum_{n\in E}n^{-s}\Lambda_\infty(n)^s\delta_n,
 \qquad \Lambda_k(n)=\prod_{j<k}\lambda(U^jn),
 \tag{2}
\]

is a nonzero finite positive measure with `mu_(E,s) P_s=mu_(E,s)`.
This is an atomic conformal measure; `P_s` is not a Markov kernel.
The same source computes normalized unit-Haar pressure

\[
 mP_s=\rho(s)m,\qquad
 \rho(s)=\frac{3^{s-1}}{2^s-1}<1\quad(1<s<2).
 \tag{3}
\]

One possible closing proof would construct `H>=1` with `P_s H<=H-1`
and `mu_(E,s)(H)<infinity`. Integrating would then contradict (2).
This note does not construct such an `H`.

## 2. The ordinary reference and its actual loss

For `s>1`, put

\[
 \sigma_s=\sum_{n\in O}n^{-s}\delta_n,
 \qquad
 d_s=\sum_{n\in O}n^{-s}(1-\lambda(n)^s)\delta_n.
 \tag{4}
\]

These measures refer to original ordinary integers. The exact identity
is

\[
 \sigma_sP_s=\sigma_s-d_s,\qquad
 (\sigma_sP_s^k)(\{n\})=n^{-s}\Lambda_k(n)^s.
 \tag{5}
\]

For the first equality, an ordinary child `n` has exactly one odd
ordinary parent root, `U(n)`. Its contribution is

\[
 (Un)^{-s}(3/2^{a(n)})^s=n^{-s}\lambda(n)^s.
\]

Induction gives the second equality. Thus these measures decrease to

\[
 \mu_{\infty,s}=\sum_{n\in O}n^{-s}\Lambda_\infty(n)^s\delta_n.
 \tag{6}
\]

An eventual positive cycle has correction product zero; the cited
elementary orbit-count estimate makes the product positive on every
escape. Consequently (6) is precisely the sum of the component measures
in (2), with coefficient one. No canonical-envelope or mixing input is
used to obtain this identity.

For any nonnegative `f` with `sigma_s(f)<infinity`, finite telescoping
and dominated convergence give the **complete original-source identity**

\[
 \boxed{
 \sum_{k\ge0}d_s(P_s^k f)
 =\sigma_s(f)-\mu_{\infty,s}(f)
 \le\sigma_s(f).}
 \tag{7}
\]

The domination is explicit: the atom density `Lambda_k^s` is between
zero and one relative to `sigma_s`. In particular, (7) does not replace
the retained measure by Haar. It is the exact summation law for the
dissipated part of the ordinary reference.

## 3. An integrable class of rational poles

Fix a rational pole `a/b`, with `a` an integer, `b>=1`, `3` not dividing
`b`, and `a/b` not in `O`. Let `0<beta<s-1`, and set

\[
 \varphi_{a/b,\beta}(x)=|x-a/b|_3^{-\beta},
 \quad\varphi_{a/b,\beta}(a/b)=+\infty.
\]

At every `n in O`, the integer `bn-a` is nonzero. Hence

\[
 3^{v_3(bn-a)}\le |bn-a|\le bn+|a|\le(b+|a|)n,
\]

where the middle absolute value is ordinary real absolute value. It
follows that

\[
 \boxed{
 \sigma_s(\varphi_{a/b,\beta})
 \le(b+|a|)^\beta\zeta(s-\beta)<\infty.}
 \tag{8}
\]

Here `zeta(t)=sum_(n>=1) n^(-t)` is only a convergent positive series,
with `zeta(t)<=1+1/(t-1)` for `t>1`. No analytic continuation is used.
The bound applies in particular to negative integers and nonintegral
dyadic rationals, including positive nonintegral ones. It includes the
numerator and denominator heights, so propagation to new rational
locations does not silently leave the constant unchanged.

Since `mu_(E,s)<=sigma_s`, (8) also gives integrability against every
canonical escaping component. For this latter assertion alone a pole
at a positive ordinary integer outside `E` is permitted, using the same
sum restricted to `E`; it is **not** permitted in the global `sigma_s`
version (8).

More generally, let `c_i>=0`, let every `a_i/b_i` satisfy the global
conditions above, and suppose

\[
 A_\beta:=\sum_i c_i(|a_i|+b_i)^\beta<\infty,
 \qquad f=1+\sum_i c_i\varphi_{a_i/b_i,\beta}.
 \tag{9}
\]

Tonelli proves the simultaneous bounds

\[
 f(n)\le1+A_\beta n^\beta\quad(n\in O),\qquad
 \boxed{\sigma_s(f)\le\zeta(s)+A_\beta\zeta(s-\beta).}
 \tag{10}
\]

This is an actual countable-family estimate, with its required weighted
coefficient sum displayed. It is not inferred merely from integrability
of each individual pole.

## 4. The entire propagated family has two finite budgets

Define the pressure Green function of this specified seed by

\[
 \mathcal G_s f(q)=\sum_{k\ge0}P_s^k f(q).
 \tag{11}
\]

Combining (7) and (10) evaluates the whole family, including every
branch, every original source, and every time:

\[
 \boxed{
 d_s(\mathcal G_s f)
 =\sigma_s(f)-\mu_{\infty,s}(f)
 \le\zeta(s)+A_\beta\zeta(s-\beta).}
 \tag{12}
\]

It is also finite at **every positive ordinary root**. If `q` is not
periodic, each original ancestor reaches it at at most one odd depth.
The exact physical product identity gives

\[
 \mathcal G_s f(q)
 =q^s\sum_{n\in\operatorname{Pred}(q)}
        n^{-s}\Lambda(n,q)^s f(n)
 \le q^s\sigma_s(f).
 \tag{13}
\]

If `q` is periodic with least odd period `r`, write
`c_q=prod_(j<r)lambda(U^j q)`, so `0<c_q<1`. Each source that reaches
`q` has one first-hit depth and then hits it at successive multiples
of `r`. Summing these repeated hits, without discarding them, gives

\[
 \boxed{\mathcal G_s f(q)\le
         \frac{q^s\sigma_s(f)}{1-c_q^s}<\infty.}
 \tag{14}
\]

This includes hypothetical nontrivial positive cycles; no classification
of them was used.

For `1<s<2`, the same seed has a separate Haar budget. In that range
`beta<s-1<1`. A unit pole has normalized unit-Haar integral

\[
 J_\beta=\frac12+\sum_{j\ge1}3^{(\beta-1)j}<\infty;
\]

a pole outside the unit class has integral one, at most `J_beta`.
Since `sum_i c_i<=A_beta`, (3) and Tonelli therefore yield

\[
 \boxed{m(\mathcal G_s f)=\frac{m(f)}{1-\rho(s)}
 \le\frac{1+J_\beta A_\beta}{1-\rho(s)}<\infty.}
 \tag{15}
\]

These are two actual finite integrals of the same full Green function.
They are taken against Haar and the ordinary loss measure `d_s`.

## 5. Why the pole approach had a genuine parameter window

The inverse gap-one branch fixes the ternary point `-1`. Near that
point, a pole of order `beta` changes its branch multiplier from
`(3/2)^s` to `(3/2)^s 3^(-beta)`. That one branch contracts if

\[
 \beta>s\log_3(3/2).
\]

This condition and the ordinary integrability condition `beta<s-1`
can hold simultaneously exactly when

\[
 \boxed{s>\log_2 3.}
 \tag{16}
\]

Indeed `1-log_3(3/2)=log_3 2`. Thus the interval
`log_2(3)<s<2` offers a genuine local-pole/integrability margin.

This differs from PR175 at
`8870528daa6a13cc941d602e578e35c8bfa4bf4f`,
`research/lean-global-closure-20261121/risk23/TERNARY_POLE_BARRIER_ATTEMPT.md`.
Its everywhere-superharmonic profile uses an exponent strictly between
zero and one and has Haar multiplier greater than one. That specific
mean obstruction does not apply to (16).

Its finite-pole propagation objection does still apply: the affine maps
`a -> (3a+1)/2^e` generate further pole locations. Starting at `-1`
already generates nonintegral dyadic points, some positive. Local
contraction of the self-return branch is not a global superharmonic
inequality. The factor `(|a|+b)^beta` in (8) must be paid for the new
locations.

## 6. The retained measure is precisely where the proposed closure stops

For every escaping component, invariance and `f>=1` give

\[
 0<\mu_{E,s}(f)<\infty,\qquad
 \boxed{\mu_{E,s}(\mathcal G_s f)
       =\sum_{k\ge0}\mu_{E,s}(f)=\infty.}
 \tag{17}
\]

There is no contradiction with (12)--(15), nor with pointwise finiteness
at every ordinary atom. The same unchanged source contributes at
infinitely many later forward endpoints. The positive component term
in (7) is exactly what the loss-measure summation leaves out.

Explicitly, retain one escaping source `p` and `q_k=U^k(p)`. Its
contribution to the loss-weighted term at the endpoint is

\[
 d_s(\{q_k\})\left(\frac{q_k}{p}\Lambda_k(p)\right)^s f(p)
 =\frac{f(p)}{p^s}\Lambda_k(p)^s(1-\lambda(q_k)^s).
\]

Summing over `k` gives exactly
`f(p)*(1-Lambda_infinity(p)^s)/p^s`, a finite telescope. With the
retained weight `mu_(E,s)({q_k})` instead, the same unchanged source
contributes `f(p)*Lambda_infinity(p)^s/p^s>0` at every `k`.
The distinct endpoints make their sum infinite. Thus the successful
loss budget and the failed retained-mass budget are visible before
any change of variables or limit interchange.

I tried to prove a uniform packing estimate for the propagated rational
poles that would make (17) finite. No such estimate was established.
The exact summation (12) succeeds for the dissipated part and retains
the residual term, rather than removing it by a change of measure.

The new critical collision target in PR185 at
`2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
`research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`, concerns
the specific moving ordinary inverse endpoint laws. Neither (12) nor
(15) supplies their required upper bound
`O(3^(-theta*m))`. Haar contraction, each individual pole's
integrability, and the full loss-measure budget cannot be relabeled as
that same-law estimate.

The complete pressure-pole calculations above are positive finite and
infinite deductions. A superharmonic majorant integrable against the
retained atomic measure, the critical same-law collision upper bound,
and escape exclusion remain unproved.
