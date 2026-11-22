# Independent review: Green Dirichlet energy and its forward boundary

Date: 2026-11-22. Reviewer: `global_certificate22`.

## Exact scope and verdict

Reviewed `LITERATURE_DIRICHLET_BOUNDARY.md` at SHA256
`41b4fe328417b3feef665b4de53fff1e94fdccc37bea1e75ce99ee4c3523c504`.
The final source includes the weak-gradient boundary identity, the exact
Cesaro and Abel formulas, the component decomposition, and the explicit
little-o target. I inspected those final statements after the rename.
The final scope clarification explicitly distinguishes the companion's
shortcut, accelerated, and killed accelerated operator counterexamples.
Those last two assertions are now supported by the direct accelerated
construction and complete basin-of-one certificate in Section 5 of
`FIVE_EDGE_TRANSPORT.md`, SHA256
`0ffaa8cc0a361aa1b9ad69c3c55a5ca4009350eaa97aa07262a0195096118c40`.
I checked the clarification and the matching operator domains; the
Dirichlet identities and countermodel arguments are unchanged.

**Verdict: VERIFIED as a written deduction under the displayed frozen
ordinary harmonic construction and canonical forward-limit inputs.**
I independently reconstructed Sections 2--7, including all quantitative
energy coefficients and both versions of the explicit countermodel.
No substantive correction is required at this source version.

This review does not independently establish the upstream analytic
construction, its predecessor-population constant, or the quoted
primary-literature statements in Section 1. Those retain their existing
source qualifications. This is not a Lean build or a proof of Collatz.
The companion five-edge transport arguments have their own frozen file
and independent reviews; they are not needed to validate the operator
identities below.

## 1. The killed-domain operator and legitimate approximants

The definition of `C` includes zero on a forward edge entering a removed
periodic state. Consequently `L nu = nu` gives the exact isometry
identity by summing over every surviving predecessor, even though the
domain is killed. Its adjoint is the displayed inverse kernel `K`, and
`KC=I`. The rows of `K` sum to one, while summing its columns loses the
sources on killed edges. Thus the asserted `L1(nu)` contraction, rather
than an unwarranted mass-preservation assertion, is correct.

The seed `g=d/nu` has finite `L1(nu)` norm `D`. The displayed reference
moment gives `D <= 200A/3` with the correct factor three. The finite
Green sum `R_M=sum_{j=0}^{M-1} K^j g` has `L1` norm at most `MD`, is
bounded between zero and one, and hence belongs to `H=l2(N,nu)`.
This justifies every subsequent Hilbert-space identity applied to it.

The exact truncation equation is `(I-K)R_M=g-K^M g`. The remainder has
the sign used in the estimate. Fatou is applied to the squared edge
differences, which need not be monotone, rather than incorrectly
applying monotone convergence to those differences. The resulting
bound is

`D_U(R) <= 2 sum dR <= 2D <= 400A/3`.

The boundary summands `nu(n) R(n)^2` on killed edges are retained.
Thus the true conclusion is square integrability of the gradient
`a=(I-C)R`; it does not assert square integrability of `R`.

## 2. The quantitative Cesaro and Abel identities

For a general `f` in `H`, the formula

`(I-K) A_N f = (C^(N-1)f-f+(I-K)f)/N`

follows directly from `KC=I`. The inner product of `A_N f` with
`C^(N-1)f-f` is zero: the isometry correlations form the same finite
list in reverse order. This proves the exact coefficient `2/N` in
the energy formula. Applying it to `R_M` and using positivity gives
the stated estimate; Fatou and dominated convergence against the
finite measure `d` then yield

`D_U(A_N R) <= (2/N) sum d A_N R <= 2D/N`.

For the Abel operator, if `u=B_alpha f`, both

`u=(1-alpha)f+alpha C u`

and

`K u=(1-alpha)Kf+alpha u`

hold. Subtracting their inner-product consequences gives exactly

`D_U(u) = 2(1-alpha)/(1+alpha) <u,(I-K)f>`.

The same Green truncations therefore give the displayed estimate for
every `0<=alpha<1`, including zero. There is no invocation of the
separate harmonic-norm geometric bound outside its convergence range.

## 3. Fixed vectors and the exact weak-gradient boundary identity

The proof that the `H` fixed space of `C` is zero is correct. An
eventually killed path forces a fixed value to be zero. Otherwise its
forward vertices are distinct and their `nu` weights are at least the
positive weight of the initial vertex. A nonzero invariant value along
that path would have infinite square norm. The assertion about the
adjoint fixed space follows from isometry as stated.

The qualitative mean-ergodic statement is applied only to the gradient
`a` in `H`. In fact the quantified estimates already prove its asserted
decay, so there is no dependency on an unproved membership of `R`.

For the sharper identity, the gradients `a_M=(I-C)R_M` are uniformly
bounded in `H` and converge at every coordinate to `a`. Finite-support
vectors are dense, so this implies weak convergence to `a`. The
pointwise identity `Ka=-g` is legitimate: `R` and `CR` are bounded,
the inverse rows sum to one, and the same result agrees with the
Hilbert-space operator on the square-integrable gradient.

The crucial pairing is therefore fully justified:

`<a,a_M> = <a+g,R_M>`

`            = sum d(R-C^M R) + sum d R_M`.

The first equality uses the adjoint; the second uses a finite Green
sum and the telescoping identity `sum_{j<M} C^j a=R-C^M R`.
The left side tends to `||a||^2` by weak convergence. Both sums on
the right pass to their limits against the finite measure `d`.
Consequently the exact formula

`D_U(R) = 2 sum dR - sum dF`

is correct. No difference of two divergent square norms is taken.

## 4. Exact asymptotic coefficients and the little-o target

Let `b_j=sum d C^j R`, so `b_j -> b_inf=sum dF`. For `j>=1`, the
gradient autocorrelation is

`<a,C^j a> = b_j-b_(j-1)`.

Expanding the squared norm of the finite gradient sum and collecting
these correlations gives

`N D_U(A_N R)=2 sum d A_N R-b_inf`.

For Abel averaging, absolute convergence of the correlation series
follows from the geometric weights and the uniform bound on the
gradient correlations. Its diagonal normalization is
`(1-alpha)^2/(1-alpha^2)=(1-alpha)/(1+alpha)`. Telescoping the
remaining correlations proves

`((1+alpha)/(1-alpha)) D_U(B_alpha R)`

`       = 2 sum d B_alpha R-b_inf`.

Dominated convergence against `d` gives the claimed common limit
`b_inf`. Grouping the nonnegative sum by actual escaping components,
using the pinned component limit `F_C=D_C/C_C`, gives precisely

`b_inf=sum_C D_C^2/C_C <= D`.

The strict positivity of the canonical charge makes `D_C>0` for every
nonempty escaping component. Thus the equivalence with the absence of
escaping components is exact. In particular the proved `O(1/N)`
estimate cannot be silently replaced by `o(1/N)`; the latter is
equivalent to vanishing of this boundary coefficient. The corresponding
Abel condition is `o(1-alpha)`. The note correctly keeps nontrivial
periodic cycles as a separate obligation.

## 5. The explicit potential-theory countermodel

I checked the model directly, without any Collatz assumption.

For a nonpower target `q`, its two predecessors are `2q` and `2q+1`,
and the logarithmic weights telescope. For a power target, its
predecessors are `2q+1` and, except at one, `q/2`. These are exactly
the recurrences in the definition of `eta`; the stationary equation
and the bounds `a/n <= eta(n)<1` follow. The prefix estimate follows
by adding the telescoping nonpower sum and the at-most-logarithmic
number of ladder points.

For a nonpower target the stated depth intervals are indeed its entire
predecessor sets at that depth: none contains a power of two. They give
the displayed lower-density bound. A power target inherits the
predecessors of `2q+1`, giving the weaker `1/(6q)` bound. Any one
forward path has only logarithmically many states below a given cutoff.

The point charge at one visits each power once under the forward map.
Therefore its normalized Green potential is exactly the formula on
the ladder, and all positive harmonic moments are at most two. The
inverse pure-potential limit is zero at every target, while every
forward path eventually climbs the ladder and has the same positive
limit. The harmonic pullback bound `5/2` is valid, including the root
exception which only reduces it.

For the three-residue encoding, the two periodic states are exactly
one and three. On the remaining states the same predecessor summation
proves harmonicity, including killing. At an escaping ladder target
the harmonic pullback contribution of its preceding ladder vertex is
at most `5/2`, and the other parent contributes less than `1/2`.
The explicit sums at the two periodic points are less than three.
Thus the global pullback estimate used for finite-time approximants
is correct.

Multiplication by five interchanges the two nonzero residue classes
modulo three. Consequently its energy on the limiting label is
exactly a positive constant times the divergent odd-unit harmonic
series, as stated. The energy here is absolute-value energy, distinct
from the squared ordinary-edge energy throughout the operator proof.

Finally, the strictly-positive-charge extension also checks. Away
from the escaping ladder, inverse coordinates grow at least by a
factor `2^k`, so the added potential is at most `2 epsilon/m`.
At a ladder target its numerator is bounded by `epsilon S`, and its
denominator is at least `a`; the chosen epsilon bounds the added
value by `1/4`. The retained half-atomic potential keeps the full
potential below `3/4`. Off-ladder power moments are controlled by
`sum m^(-1-p)` for every `p>0`, and ladder moments by a geometric
sum. The predecessor sets of successive ladder points exhaust the
whole escaping component, so their total added charge tends to
`epsilon S`. This gives exactly the positive limiting constant in
the note. All-state positive charge therefore does not invalidate
the countermodel.

The countermodel does not satisfy the specific Collatz affine map or
the canonical relation `d=(1-lambda)h`. The note explicitly preserves
that limitation. It rules out the generic functional-analytic
inference being tested, while leaving a more arithmetic estimate for
the actual canonical potential unresolved.
