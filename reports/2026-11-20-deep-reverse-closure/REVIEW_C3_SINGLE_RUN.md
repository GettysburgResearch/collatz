# Independent reconstruction of the adaptive c=3 single-run exclusion

Reviewer: `/root/deep_reverse_proof`.
Reviewed mathematical source: `C3_SINGLE_RUN_CERTIFICATES.md`, SHA-256
`d9101068f5180413b5a1ef142fe25f0dc8881e0651ed8addf21ea28ab569257d`.

**Verdict: VERIFIED at C3S1--C3S2 as a deduction using H2's fixed
globally least-failure hypothesis.** This is a complete exclusion of
the stated unbounded-rank certificate family from being that global
minimum. It is not a proof of every c=3 reverse implication. The
general first-block removal identities are also verified, with the
remaining residual closure explicitly open. C3S3's exact rank-six
Mersenne reduction and its same-clock inequality are also verified;
they identify a concrete remaining family and do not establish its
convergence or an obstruction to every adaptive construction.

## Certificate and first-hit reconstruction

Since `z=41 (mod81)`, `v3(z+1)=1`. The identity
`z+1=2^a(2^e+1)/3^a` therefore forces
`v3(2^e+1)=a+1`. In particular `e` is odd, and elementary lifting
gives `v3(e)=a`, so `e>=3^a`. The quotient
`q=(2^e+1)/3^a` is a positive odd integer.

The actual first `a-1` odd iterates are
`3^i*2^(a-i)*q-1`, and their division exponents are one.
The following odd input has `3n+1=2^(e+1)`, yielding the terminal
division exponent `e+1`. All earlier odd inputs exceed 1 because
`e>=3` and `z>1`. Thus this is a first-hit certificate, rather than
a word padded with a cycle at 1.

The four initial gaps of the upper are `(2,2,2,3)`, as in K1.
Its total first-hit odd rank is exactly `a+4` and its native clock
is `9+(a-1)+(e+1)=a+e+9`. On the lower side,
`T^7(Y)=2z+1`; the next `a` inputs are odd and produce
`2^(e+1)+1`. The even-exponent cycle-shadow identity then yields
`T^(a+e+9)(Y)=T(3^((e-1)/2))`. The endpoint clocks match exactly.

## Uniform source comparison

Multiplying `X-176106*P` by `81*3^a` gives the four terms printed
in the source. Dropping the positive term `2^(a+9)` is legitimate.
The remaining `S(a,e)` has the exact increment identity
`S(a,e+2)=3S(a,e)+2^(a+e+9)+2*687*3^a`.

For the joint step `(a,e)->(a+1,3e)`, the positive exponential
multiplier is `2^(2e+1)`, larger than both negative multipliers
`3^(e+1)` and 3 for `e>=2`. Consequently positivity at `(4,81)`
propagates to every `(a,3^a)`, `a>=4`, and then to every larger
odd `e`. Both the base integer and the recurrence were independently
computed. This handles arbitrarily large `a` and `e`; the finite
replay is not being extrapolated to obtain that quantifier.

For `a=1,2,3`, I independently enumerated the complete exponent
periods modulo `3^(a+4)` and obtained exactly
`21 (mod162)`, `315 (mod486)`, and `837 (mod1458)`. The normalized
quantity `S(a,81)/2^a` is decreasing in `a`, so the printed positive
base at `a=3` does imply positivity for `a=1,2`. This leaves only
`(a,e)=(1,21)`, whose residual `3^10` has the stated complete finite
ordinary certificate. The small-rank exception has not been silently
included in the uniform inequality.

If such an `X` is the globally least failure, the established
comparison `176106*P<X` invokes H2 for that same fixed `X`, hence
places `P` in the basin and contradicts failure. Equivalently the
argument can be run assuming the validity of all eligible reverse
implications below this `X`. No separate minimum within the
single-run family is used; that would be insufficient.

## Ordinary construction in every obstruction cylinder

With `a=L-2` and `m=2L-1=a+L+1`, the proposed exponent congruence
does give
`2^a(2^e+1)=3^(a+1)/2 (mod3^(a+L+1))`.
Division by `3^a` is justified and gives
`z+1=3/2 (mod3^(L+1))`. Together with exact
`v2(z+1)=a=L-2`, this yields the required two congruences for
`N=(4z+1)/3`. The modulus exponents and the one extra ternary
division are correct.

Every exponent constructed is a positive ordinary integer, and
the displayed stopping word is a finite certificate for its upper
source. The construction does not assert that a limit of these
sources is ordinary, or that an arbitrary pre-existing member of
the same cylinder has that certificate. This distinction is
particularly important when combining the result with the bounded
clock obstruction.

## General block and remaining gap

For arbitrary positive odd `z`, write `z=2^a q-1` with `q` odd.
The exact block removal gives
`T^a(2z+1)=2^(e+1)w+1`, where
`3^a q-1=2^e w`. If `z` is certified, its actual prefix certifies
`w`. The subsequent ordinary identities yield the residuals in
the source table. For `e=1`, the residual is the already certified
`w`, so that branch is complete without H2. For other `e`, the
shorter certificate for `w` does not by itself certify the new
multiplied or shifted residual. Neither the height guard nor a
well-founded global rank has been proved for those new states.

## Remaining rank-six family and its ordinary clocks

The formula `z=(2^(A+3)-11)/9` gives
`3z+1=8w`, where `w=(2^A-1)/3`. For positive even `A`, this
`w` is an odd integer and `3w+1=2^A`. At the eligible exponents
below, `z>w>1`. Thus the exact odd stopping word of `z` is `(3,A)`.

The eligibility equation `z=41 (mod81)` is equivalent to
`2^(A+3)=380 (mod729)`. I independently obtained order 486 for
2 modulo 729: its 486th power is 1, whereas its powers at
486/2 and 486/3 are not 1. These two prime divisors suffice
to exclude every proper divisor of 486. The sole solution in
the complete period is `A=340`; hence all and only the positive
eligible exponents in this family are `A=340+486j`, `j>=0`.

Substituting in the upper formula gives
`X=(2048*2^e-7207)/729`, `e=A+1=341+486j`.
The eligible upper prefix `(2,2,2,3)` followed by the certified
word `(3,A)` is the first-hit word `(2,2,2,3,3,A)`.
Its exact odd rank is six and its native clock is `A+12=e+11`.

For the lower, `T^7(Y)=R=2z+1`. Direct arithmetic gives
`T(R)=(2^(A+3)-5)/3`, an odd integer, followed by
`T^2(R)=2^(A+2)-2` and `T^3(R)=2^(A+1)-1`.
The exact odd division exponents are 1 and 2, and therefore
`T^10(Y)=M_e` as claimed. This progression of `e` is distinct
from the earlier rank-five progression `119 (mod162)`.

Starting at `M_e`, the first `e` inputs are odd: the state
after `i<e` steps is `3^i*2^(e-i)-1`, and after `e` steps
it is `3^e-1`. One additional halving therefore gives
`T^(e+11)(Y)=(3^e-1)/2`. Comparison with the printed `X`
is equivalent to
`729*3^e-4096*2^e+13685>0`. The first two terms already have
positive difference at `e=5`, and their ratio increases by
`3/2` at each increment. This proves the claimed strict
inequality for every eligible `e>=341`, without extrapolating
from the four literal controls.

Consequently, this supplied upper certificate does not force the
lower to be below its upper source by the same ordinary stopping
clock. The argument leaves open further source-dependent work.
It supplies neither a nonconvergent integer nor a universal
impossibility result for certificate-based proofs.

## Independent finite execution

`check_c3_single_run_review.py` imports no author implementation.
Its SHA-256 is
`a5f0ec8b216c76b048a7699b26716653ba47541ba9ba9ead65faf205da5496e5`.
Normal and `-OO` runs returned identical reports. They reconstruct:

* all three finite exponent progressions;
* six literal single-run sources, totaling 4,573 upper native clocks;
* 36 exact recurrence controls alongside the written uniform induction;
* eleven compressed cylinder sources for `H=0,...,10`, by an
  independently implemented ternary discrete-log lift;
* 124 literal general-block identities, including 61 directly solved
  first-block cases with `e=1`;
* the complete rank-six exponent period modulo 729, together with
  four literal rank-six sources totaling 4,324 upper native clocks,
  their lower Mersenne checkpoints, and their exact same-clock
  lower heights.

Large compressed sources were verified by exact modular arithmetic
and the proven formulas. Their huge binary integers were not expanded,
and their full ordinary paths were not claimed to have been executed.
This is an AI reconstruction of the stated proof and an exact finite
replay, not proof-assistant certification or human referee acceptance.
