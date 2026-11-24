# Independent review of the actual Taylor-jet transport

23 November 2026. Reviewer: the separate `source_transfer7` research lane.
Parent checkpoint: `e4367dd2c4406c1041e66d82dfba822908747fa3`.

**Verdict: VERIFIED at the written finite-arithmetic claim level, with
the formalization boundary stated correctly. No mathematical correction
was required. Universal rationality of the actual germ remains OPEN.**

This review reconstructs the arguments rather than extending a verdict
from the preceding round. It covers the exact files below, whose author
confirmed they were frozen. It is not a review of later edits, the entire
PR182 branch, or the analytic rationality consumers on PR178.

## 1. Frozen inputs and evidence

All three file hashes were recomputed from the actual local bytes.
Paths in this table are relative to
`research/closure-round7-20261123/`.

| File | Git blob | SHA256 |
| --- | --- | --- |
| `GERM_CONSTRUCTION.md` | `6a92d7c329c0b6e782e78f2bb3abaace3fcc5a64` | `90a1decd0e248788bb04ead0769e5ab17bf1d4e2b20f92ec44fb5fea99048e83` |
| `GermConstruction.lean` | `b62dd1a5a6f5b8d818b86721d430b06e3f3bae75` | `e57b0ebd48825e5cf214dc458e697d957f86affeb064f46a2e49b52420ab698a` |
| `germ_controls.py` | `14e45e40bc798594a1e201f82952aa0c6da10a8c` | `58af0296144179eecf5a98b15c45f5af9f0b8834deedd58dffb9630b45c26dec` |

The inherited actual-germ definition and the definition of `J3` were
checked in
`research/profound-round6-20261123/RATIONAL_SELECTION.md`, Git blob
`54d7949ac80ec6b8286f0d03d579f9f6e0efe95f`, at the parent checkpoint.
No external analytic consumer is needed for the reviewed deductions.

Evidence consists of a complete reading of the note and Lean source,
independent algebraic reconstruction below, complete inspection of the
finite control script, and an independent execution of that script under
`python -O`. This reviewer did not invoke the Lean compiler; a separate
packet-level build receipt must supply execution and axiom-audit evidence.
The Lean assessment here is a semantic source review, not a fabricated
compilation receipt.

## 2. Actual binary coefficients and all-order prefix identity

**VERIFIED:** the coefficients in equations (1)--(2) concern one fixed
positive ordinary source and its literal shortcut itinerary. Each term
of

\[
c_j(n)=\sum_{k\ge j}e_k\binom{k}{j}2^{k-j}3^{-p_{k+1}}
\]

has binary valuation at least `k-j`. The series therefore converges in
`Z_2`. This establishes binary integrality, without establishing
rationality. Translation of the original binary analytic function on
a closed disc of radius less than one is legitimate. The complete affine
identity gives `c_0(n)=-n` because `2^N x_N/3^(p_N)` tends to zero
binary-adically for ordinary integer `x_N`.

The prefix split retains the complete chronological carry and the actual
tail `x_N`. Coefficient extraction from

\[
J_n(t)=\sum_{k<N}e_k3^{-p_{k+1}}(2+t)^k
       +3^{-p_N}(2+t)^N J_{x_N}(t)
\]

and multiplication by `2^j 3^(p_N)` yield exactly

\[
2^j3^{p_N}c_j(n)-C_j(N)
=2^N\sum_{i=0}^j\binom N{j-i}2^i c_i(x_N).
\]

The coefficients with `j-i>N` vanish by the binomial convention. The
integer carry recursion has factor `3^(e_N)` and new term
`e_N binom(N,j) 2^N`, as stated. There is no discarded tail or unexplained
exchange of a changing finite witness for the fixed source. Guaranteed
binary divisibility of the right side by `2^N` supplies no archimedean
height bound or ternary cancellation bound.

## 3. Exact finite denominator clock

**VERIFIED:** R7-GERM-2 and equation (10), as written mathematics under
the explicit hypothesis that the first `r+1` actual coefficients lie in
`Z[1/3]`.

The one-step relation is

\[
(2+t)J_{Tx}(t)=3^eJ_x(t)-e,
\qquad e\in\{0,1\}.
\]

Its finite triangular equations first put the tail jet in `Q`, with
denominators involving only two and three. The independently established
binary integrality of the actual tail excludes the factor two in every
reduced denominator. Thus the tail finite jet remains in `Z[1/3]`.

For the exact exponent, represent a truncated jet by a vector of length
`r+1`. Multiplication by `2+t` is a triangular matrix with diagonal two;
both this matrix and its inverse have entries in `Z_3`. It therefore
preserves the minimum ternary valuation of the vector. The maximum
reduced-denominator exponent is that negative minimum clipped at zero.

An even step does not change it. For an odd step, write its initial
value as S. If `S>=2`, multiplication by three changes the negative
minimum from `-S` to `1-S`; subtracting the integer constant term cannot
cancel a coefficient of negative valuation. The subsequent unit
triangular map preserves that minimum, so the new exponent is `S-1`.
If `S=0` or `S=1`, the right-hand vector is ternary integral, hence the
new exponent is zero. This proves the exact one-step law

\[
S_r(Tx)=\max\{S_r(x)-e,0\},
\]

and iteration gives `S_r(x_N)=max(S_r(n)-p_N,0)`.

A positive integer trajectory has infinitely many odd steps: after a
last odd step a fixed positive integer could not remain an integer under
indefinite repeated halving. Consequently the required finite clearing
time exists under the coefficient hypothesis. This does not bound the
shortcut time needed to accumulate those odd steps, establish the
coefficient hypothesis, or give one common clearing time for all orders.

## 4. Positive ternary radius and the quantifiers it supports

**VERIFIED:** equation (11) and the distinctions made in Section 4.

To make the constants explicit, let `R_3>0` be the ternary convergence
radius and choose `0<rho<min(R_3,1)`. There is a finite `M>=1` with

\[
|c_j(n)|_3\rho^j\le M\qquad(j\ge0).
\]

For rational coefficients in `Z[1/3]`, their denominator exponents are
`max(0,log_3|c_j(n)|_3)`. Hence with

\[
A=-\log_3\rho>0,\qquad B=\log_3M\ge0,
\]

every coefficient through order r has denominator exponent at most
`Ar+B`, giving the claimed bound on `S_r`. Both constants depend on the
source and the assumed germ. No radius or constants have been constructed
from an arbitrary ordinary orbit.

This gives a sufficient number of odd steps growing linearly in the jet
order. It gives neither a common denominator for every coefficient nor a
bound on the ordinary orbit. Radius one alone permits unbounded
sublinear denominator exponents. Conversely, if `R_3>1`, choosing
`1<rho<R_3` makes the coefficient norms tend to zero; the sufficiently
high coefficients are then ternary integral, and the finitely many early
coefficients supply a common bound. This stronger conclusion is correctly
conditional on a radius strictly greater than one. The complex radius
is part of the inherited `J3` definition but is not used for these local
ternary deductions.

## 5. Other denominator primes and the formal boundary

**VERIFIED:** finite-jet membership in `Z_(ell)` is invariant under an
actual step for every prime `ell` other than two and three. In this ring,
both the truncated factor `2+t` and the scale three are units, and the
prefix correction is integral. Rationality of the jet transports in
both directions through the same finite equations. Thus an excluded
denominator prime cannot disappear from every coefficient through a
fixed order merely by moving along an actual preperiod.

The Lean source has exactly the seven public theorems listed in the
note. Its definitions represent rational binary integrality by an odd
reduced denominator, ordinary integrality by an integer representative,
and common ternary denominator clearing by the predicate `Cleared`.

| Formal theorem(s) | Reviewed scope |
| --- | --- |
| `binaryIntegral_int_mul`, `integral_of_double` | Elementary rational denominator facts; the latter requires binary integrality to remove a possible factor two. |
| `triangular_integrality` | Finite induction through division by `2+t`, with binary-integral output coefficients explicitly assumed. |
| `even_step_cleared` | Sufficient preservation of a common ternary denominator, given the finite coefficient equations. |
| `odd_step_cleared`, `odd_step_integral` | Sufficient removal of one positive denominator layer, and preservation after clearing. They do not assert minimality of that exponent. |
| `jet_subring_iff` | Exact finite-jet membership equivalence for a rational subring containing the inverses of two and three. Its general natural exponent includes the two actual parity cases. |

The formal proofs do not define the actual analytic Taylor series, prove
that its coefficients are rational, or formalize the exact valuation
minimum argument in Section 3 of this review. The note explicitly marks
these limits: the exact recurrence for the minimal exponent is a written
proof, while the Lean module proves the sufficient arithmetic clearing
direction. No hidden premise asserts universal rationality or universal
Collatz convergence. Source inspection found no added axiom, `sorry`,
or unsafe computational proof in the module; the packet-level axiom
audit is still a separate execution event.

## 6. Independent finite execution

Executed successfully at the frozen control-script hash:

```text
python -O -X utf8 -B research/closure-round7-20261123/germ_controls.py
```

The script reported `status: pass` and the following counts:

| Control | Count |
| --- | ---: |
| Explicitly convergent ordinary sources | 68 |
| Maximum tested jet order | 11 |
| Actual prefixes | 1,950 |
| Coefficient prefix identities | 23,400 |
| Direct carry identities | 3,180 |
| Coefficient step identities | 22,584 |
| Exact denominator-clock checks | 23,400 |
| Integral tail coefficients checked | 23,515 |
| Maximum shortcut steps | 329 |
| Maximum initial ternary denominator exponent | 195 |

The actual source 85 has `c_1=0`. Independently, its itinerary reaches
one after eight shortcut steps with one odd step, so

\[
J_{85}(t)=\frac13+\frac{(2+t)^8}{3}J_1(t),\qquad
J_1(t)=-\frac1{1+4t+t^2}.
\]

The linear coefficient is `(-8*2^7+4*2^8)/3=0`, confirming the stated
countercontrol without relying on an approximate calculation.

The script constructs jets backward from the known standard tail after
explicitly evaluating each selected orbit to one. Its step checks are
arithmetic regressions, and its direct carry sum supplies a separate
finite calculation of the chronological carries. These runs do not
test the unconstructed rationality assertion on an arbitrary source,
the existence of a common denominator, or an all-time analytic radius.

## 7. Closing boundary

The new output is a correctly scoped arithmetic transport theorem for
actual finite jets, not a construction of the initial rational jet.
Even rationality of the first derivative for an arbitrary fixed positive
integer is still unsupported. The reviewed recurrence retains that
obligation, and neither finite denominator clearing nor positive radius
under an assumed germ converts it into a proof of full Collatz.
