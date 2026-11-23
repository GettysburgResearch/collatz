# An ordinary cylinder makes the mixing horizon intrinsic

**Status: finite written theorem and eight Lean-checked supporting statements.**
The asymptotic growth conclusion uses the explicitly cited marginal mixing
input in [FINITE_SPIKE_CLOSURE.md](FINITE_SPIKE_CLOSURE.md). Neither the
finite theorem nor that input proves an all-depth Collatz estimate.

The finite-spike attack calibrated its horizon from an exact rational
mixing error plus a positive regularizer. An actual positive-integer
inverse cylinder proves that the error itself is positive. This removes
the regularizer, gives a larger computable horizon, and also places an
intrinsic upper bound on that particular calibration.

## 1. Exact domain and normalization

Use the ordinary accelerated map

\[
U(n)=(3n+1)/2^{v_2(3n+1)}
\]

on positive odd integers. The inverse transfer operator and its finite
densities are exactly those of the companion note:

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\pmod3}}
\frac3{2^e} f\!\left(\frac{2^e q-1}{3}\right),
\qquad D_r=P^r\mathbf1.
\tag{C1}
\]

For a positive odd ternary unit `q`, every summand is an actual positive
odd predecessor. As a periodic density, `D_r` is defined on residues
modulo `3^r`. For `r>=1` it vanishes on nonunits, has normalized mean one,
and satisfies `0<=D_r<=2^r`. These elementary finite transfer facts,
including the exact geometric grouping of all valuation exponents, are
proved in the companion note. There is no valuation cutoff in (C1).

For integer `m>=1` let

\[
\epsilon_m=3^{-2m}\sum_{a\bmod3^{2m}}
\left|D_{2m}(a)-D_m(a\bmod3^m)\right|.
\tag{C2}
\]

The coarse density is lifted to the same fine residue space. Both terms
therefore have total mass `3^(2m)`. The normalization in (C2) is essential.

## 2. One fully ordinary cylinder gives a two-sided L1 discrepancy

Set

\[
q_m=2\cdot3^{2m}-1,\qquad
x_j=2^{j+1}3^{2m-j}-1\quad(0\le j\le2m).
\tag{C3}
\]

Every `x_j` is a positive odd ternary unit. Direct arithmetic gives

\[
3x_j+1=2x_{j-1}\quad(1\le j\le2m).
\]

Consequently all `2m` actual odd gaps are one, from the source
`x_(2m)=2^(2m+1)-1` to the target `x_0=q_m`. Their shortcut clock is also
`2m`; this is not a completion-only word or a changing-target limit.
The word's single contribution to (C1) gives

\[
D_{2m}(q_m)\ge(3/2)^{2m}=(9/4)^m,
\qquad D_m(q_m)\le2^m.
\tag{C4}
\]

If a finite real vector `f` has sum zero, then
`sum |f| = 2 sum max(f,0)`, and hence `sum |f|>=2f(a)` at every cell.
Apply this to the difference of the two equal-mass densities. Dividing
the discrepancy in (C4) by the size of the fine residue space proves

\[
\boxed{
\epsilon_m\ge2\left(4^{-m}-(2/9)^m\right)
\ge\frac29\,4^{-m}>0.}
\tag{C5}
\]

For the last inequality, factor out `2*4^(-m)` and use
`(8/9)^m<=8/9`, valid for every `m>=1`. The factor two in (C5) comes
from the equal total masses, not from counting the cylinder twice.

The Lean file [MixingCylinder.lean](lean/MixingCylinder.lean) proves the
arbitrary-length actual gap trace and its shortcut clock; the elementary
ternary exponent period; the zero-mass L1 inequality; and the two scalar
error bounds. The analytic interpretation of `D_r`, its periodicity,
and its equal-mass normalization remain explicit written inputs to the
finite inequality. They are not asserted as unexplained Lean axioms.

## 3. A larger horizon without an artificial positive term

Define the intrinsic integer calibration

\[
\boxed{H_m^*=\max\{H\in\mathbb N:H^4\epsilon_m\le1\}.}
\tag{C6}
\]

The exact rational (C2) and strict positivity (C5) make this a finite,
computable maximum. Zero is always admitted. Every use of a reciprocal
of `H_m^*` below assumes `H_m^*>=1`, which holds eventually by the
mixing input. If `H_m` is the companion note's regularized maximum,
then `H_m^*>=H_m`.

Tao's marginal mixing estimate, through the exact identification given
in the companion note, implies `epsilon_m=O_A(m^(-A))` for every fixed
`A>0`. Thus this one sequence `H_m^*` exceeds every fixed polynomial
in `m` by every fixed factor. The sequence is chosen once from (C2);
it is not reselected when the polynomial changes. No effective global
mixing constant is needed to compute a particular finite `H_m^*`.

Conversely (C5) and (C6) imply

\[
\boxed{2(H_m^*)^4\le9\cdot4^m,\qquad
H_m^*\le(9/2)^{1/4}\,2^{m/2}.}
\tag{C7}
\]

This upper bound concerns this quartic calibration, not a universal
upper bound for Collatz stopping times or inverse witnesses. Both the
superpolynomial lower growth and the exponential upper budget can hold
at once. The Lean theorem `calibration_ceiling` proves (C7)'s polynomial
form and also covers the regularized calibration.

## 4. Consequences for finite obstacle iterates

Suppose `q>=b>=9^m`, and every ordinary unit predecessor of `q` through
the finite depth actually used is at least `b`. Let `V_k` be the
companion note's finite obstacle iteration, starting from a bounded obstacle
`0<=g<=1`. Its finite positivity argument gives
`V_k<=sum_(j=0)^k D_j`. For `k+1<=H_m^*`, the same finite theorem gives

\[
\boxed{\frac{V_k(q)}q\le
H_m^*\frac{4^m}{b}+\frac9{mH_m^*}.}
\tag{C8}
\]

Only the actual depth `k` needs the predecessor floor. No stationary
normalization or infinite majorant is used in this finite conclusion.
A violation, with `q>=b`, yields an actual unit predecessor below `b`
at a positive depth at most `k`.

The first term in (C8) is small without choosing an extra truncation of
the calibrated horizon. Indeed, by `b>=9^m` and (C7),

\[
H_m^*4^m/b\le(9/2)^{1/4}(4\sqrt2/9)^m,
\qquad 4\sqrt2/9<1.
\tag{C9}
\]

Together with superpolynomial growth of `H_m^*`, both terms in (C8)
decay faster than any fixed inverse polynomial in `m`.

The exact certificate in this packet checks (C5), maximality of both
quartic calibrations, their ordering, and (C7) for `m=1,2,3`, using
integer arithmetic. All six maxima in that small check equal one.
Those cases test the interface; they do not supply a useful numerical
large-scale cutoff.

## 5. The remaining global step

At a fixed predecessor floor `b`, the condition `9^m<=b` bounds `m`.
It does not permit sending `m` to infinity while retaining that floor.
The finite theorem therefore cannot be passed directly to
`V(q)=sup_k V_k(q)`. The missing inference is still an appropriate
finite witness or contact statement inside the calibrated horizon.

The scale mismatch can also be stated explicitly. With
`m=floor(log_9 b)`, (C7) gives

\[
H_m^*\le(9/2)^{1/4}b^{\log2/(2\log9)}.
\tag{C10}
\]

Propagating obstacle value one from a component minimum `b` gives
normalized amplitude of order `1/b`. That mechanism alone reaches the
critical size of order `1/log q` only once `log q` is of order `b`.
At that scale the term `log(q)/(mH_m^*)` in the companion contact
estimate is too large to certify capture or vanishing. An earlier
critical spike or a different all-time control is needed. This is a
boundary of these displayed estimates, not a refutation of another
route to Collatz.

## Dependency and evidence record

- The finite density, full-clock recurrence, obstacle iteration, and
  exact source pins are in [FINITE_SPIKE_CLOSURE.md](FINITE_SPIKE_CLOSURE.md).
- The sole external asymptotic input is Tao, *Almost all orbits of the
  Collatz map attain almost bounded values*, Proposition 1.14 and
  equations (1.26)--(1.27), [arXiv:1909.03562v7](https://arxiv.org/html/1909.03562v7).
- The actual trace uses the unchanged `WitnessGlobal` map convention at
  PR180 head `cfe70e02f246119a55fb5bf8fd573f148d746beb`.
- The packet's fresh replay checks all eight new public Lean statements
  and their standard-axiom audit; the companion integer certificate
  records its exact finite coverage separately.
