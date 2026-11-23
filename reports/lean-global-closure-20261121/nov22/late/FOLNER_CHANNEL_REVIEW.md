# Focused independent review: normalized clock filters and five cutoffs

Date: 2026-11-22. Reviewer: `global_certificate22`.

Reviewed `FOLNER_FIVE_CHANNELS.md` at SHA256
`c539067d4cb4a0bb3ceaca062389940865dfa74f0ef0c1fd532961cee7de16eb`.

**Verdict: VERIFIED as a written deduction conditional on the displayed
frozen PR183 Wold-channel and component-mass statements.** This review
does not re-establish those upstream analytic inputs or perform a Lean
build.

Two precision corrections requested during review are present in this
final version: the complete cross-term formula uses the first common
endpoint, and the explicit merger family is restricted to its ternary
unit subfamily when it is used inside the odd-unit energy domain.

## Clock filters and their surviving term

For one physical source, all surviving forward vertices are distinct.
The squared collision norm is therefore the displayed weighted square
sum of the filter values. The lower bound on the forward reference
weights proves convergence for every normalized `l2` filter, even
without `l1` summability. Finite source sums follow by the norm triangle
inequality; the note does not infer boundedness for arbitrary source
vectors from this finite-source assertion.

Given the pinned Wold projection, a projected unit atom has density
`1/C_C` on its synchronous class and squared norm `1/C_C`. Translating
the clock profile proves (F2) with its precise normalization. The
unmatched component source contributes `1/C_C` for every normalized
filter, independent of its time profile. The orthogonal remainder
has nonnegative energy, so (F3) follows.

The flat and geometric filter lag costs are the stated exact overlaps:
`2 min(1,|d|/J)` and `2(1-r^|d|)`. For general normalized Følner
filters, approximate invariance under one shift implies approximate
invariance under each fixed integer shift and vanishing mass on every
fixed finite set of clock indices. Splitting the orbit norm into a
finite initial segment and a tail where the reference tends to `C_C`
then gives the atom limit. The corrected first-common-endpoint choice
makes (F6) the entire pair cross term. The same split and
Cauchy--Schwarz give its limit `1/C_C`. Thus the full physical norm
limit (F7), rather than only its projected contribution, is justified.

## The exact finite five-ray cutoff

The factorization `n=5^k m` with `gcd(m,30)=1` is unique on positive
odd ternary units. Summing its geometric weights gives exactly the
mass formula in (F8). Only the top edge of each retained ray crosses
the cutoff, giving exactly `5^(-K) H_M` for the absolute-value
five-boundary cost. The displayed choice of `K(M)` makes that cost
at most `H_M/(1+H_M)^2`, tending to zero, while the retained harmonic
mass diverges and the cutoff tends pointwise to one.

The product inequality (F9) uses the correct endpoint `eta(5n)` in
its first term. Formula (F10) is the exact ordinary transport
commutator. A small boundary on the five graph supplies no estimate
for that different commutator, as the note states.

For finite source cutoffs, every quantity in (F11) is finite. Applying
the per-source unmatched lower bound and then nonnegative Fatou gives
(F12) without requiring monotonic cutoffs or a comparison between
source and clock growth rates. If the source-qualified rigidity input
makes the limiting component five-energy infinite, the diagonal sums
must diverge. The note does not present their finiteness as proved.

## Distinct meanings of an odd return and a downstream merger

For `h=6k+4`, direct substitution gives the exact first halving
exponents two and five in (F13); the next exponents are `h-2` and
`h-5`. This proves the displayed merger after two and three odd steps
for arbitrarily large sources. The example is therefore a valid
counterexample to replacing a return-to-source bound by a bound on
arbitrary downstream merger clocks.

The final version correctly retains the necessary domain restriction:
`n_k` is a ternary unit precisely for `k=0 or 1 mod 3`, as follows
by evaluating `2^(6k+4)` modulo 27. The infinite subfamily `k=3j+1`
includes the first example `n=113` and makes the subsequent killed
clock-filter statement apply on the stated domain.

These results identify exact surviving mismatch terms and exact cutoff
costs. They do not supply a global upper bound for the mismatch sum,
or eliminate escaping or periodic Collatz components.
