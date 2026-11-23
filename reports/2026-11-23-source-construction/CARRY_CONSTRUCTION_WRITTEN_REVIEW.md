# Independent written review of the carry construction attempt

23 November 2026. Reviewer: checkpoint17 cycle arithmetic lane.

**Result: PASS for the written elementary arguments, with the clock/equality
paragraph read under Theorem D's explicit hypothesis `n>2`.** The source's
open conclusion is appropriate: it establishes scope and exact identities,
but does not construct a candidate for every unchanged ordinary source.

## Frozen source and review boundary

Reviewed file:
`checkpoint17_carry/CARRY_CONSTRUCTION_ATTACK.md`.

SHA256:
`9e7f08c17362d2163f5020661dad6d012f987e94b62aa1754605ef6ef1e6dcd3`.

I independently reconstructed Sections 1–5, concentrating on Theorem L,
Theorem D, the negative-sector estimate, and the full reset identity. I did
not edit the author file or shared repository. This review does not certify
the external literature's statements or provenance, and it does not review
or replay any Lean module. The finite controls below supplement the written
proofs; they are not the justification of their universal quantifiers.

## 1. Terminal lattice and all-target sign crossing

The terminal pullback is

\[
y=\frac{2^K u-D}{3^b}.
\]

For `r<=b`, its denominator divides `3^r` exactly when
`2^K u = D mod 3^(b-r)`. Since 2 is invertible modulo powers of 3, the
terminal values form one progression of spacing `3^(b-r)`. On writing
`y=a/3^r`, its numerators have spacing `2^K`. The proposed freedom in the
terminal integer therefore retains the original carry congruence.

For Theorem L, the least positive `R` with `2^R(u+1)<3^R` exists. For
`u>=1`, `R=1` is impossible, so `R>=2`. Minimality gives
`2^(R-1)(u+1)>=3^(R-1)`; equality is impossible because the left side is
even and the right side odd. Dividing these two strict bounds proves

\[
-\frac13<y_0<0,\qquad 0<y_1<\frac12.
\]

For `j<R`, the displayed numerator of `y_j` is odd and its denominator is
odd. Cancellation of factors of 3 does not change that parity. The original
`x_j=2^(R-j)N` is even. Direct application of the two specified branches
therefore proves every step of the formula, and its terminal pair is
exactly `(N,u)`. Subsequent `y_j` remain positive by the formula or by
positivity of the odd branch.

The assertion about an additional finite complementary prefix uses the
unique ordinary parity residue modulo `2^L`; triangular bit lifting, or the
odd coefficient `3^b` in the affine numerator, supplies that residue. A
positive representative can always be chosen. This keeps the terminal
ordinary target `N` fixed while changing the initial source `2^R N` when
`u` changes. The source explicitly retains that distinction and makes no
claim that these examples satisfy their own required certificate horizon.

The short sequence
`(16,-1/9) -> (8,1/3) -> (4,1) -> (2,2)` is exact: the first three steps
are complementary and the last displayed pair has equal parity. It does
not extend to an additional legal paired step.

## 2. True-dual denominator and first-hit clock

Assuming an actual first hit of 1 from `n>2`, the terminal segment must be
`4,2,1`: an odd preimage of 2 would be 1 and violate first hitting, and 4
has no positive integral odd preimage. Pulling terminal dual 2 backward
gives respectively `1/3,1,2` at those three states.

From a reduced `u/3^j`, `j>0`, an original odd inverse doubles the numerator
and preserves the exact denominator exponent. An original even inverse
gives `(2u-3^j)/3^(j+1)`, whose numerator is a unit modulo 3. Thus each
earlier even input adds exactly one to the reduced exponent. The base at
4 has exponent 1 and two remaining even inputs, proving `r=b_tau-1`.

If the start is outside `{1,2,4}`, the state before that terminal segment
is 8, with dual `-1/9`. Both inverse branches preserve negativity, proving
the claimed sign classification. The separate values at 1, 2, and 4 are
consistent with the pullback.

The ordinary affine formula has

\[
2^\tau=n3^{o_\tau}+C,\qquad C\ge0,
\qquad o_\tau=\tau-r-1.
\]

Each odd input contributes a strictly positive summand to `C`, so equality
holds exactly when there are no odd inputs, equivalently `n=2^tau`.
Rearrangement gives the displayed logarithmic clock bound. This proves a
statement about a known true dual of a known finite path, as the source
expressly says.

**Scope clarification requested:** this clock/equality paragraph uses
`n>2`. If it were instead read over every positive `n`, its equality
characterization would fail at `n=1`: there `tau=r=0`, and its first
display is `1/3<1`, although `n=2^tau`. The assertion is correct in its
inherited domain, and also works separately at `n=2`. I recommended that
the author explicitly repeat `n>2` in the clock paragraph.

## 3. Negative-sector product estimate

For `n` outside `{1,2,4}`, set `L=tau-3`. Through time `L`, the original
state and negative dual give a positive integer
`P_j=3^r x_j(-y_j)`: legal forward steps keep the triadic denominator
dividing the initial `3^r`. The terminal value in this sector is
`P_L=8*3^r/9`, while `P_0=n|a|`.

An original odd input has `x_j>=3`, hence

\[
\frac{P_{j+1}}{P_j}=\frac{3x_j+1}{4x_j}\le\frac56.
\]

For an original even input whose next dual remains negative,

\[
0<\frac{P_{j+1}}{P_j}
 =\frac{3-1/|y_j|}{4}<\frac34.
\]

Applying the common `5/6` bound for exactly `L` steps gives

\[
8\,3^r6^{\tau-3}\le9n|a|5^{\tau-3}.
\]

The crossing step from `(8,-1/9)` to `(4,1/3)` is excluded from this
contractive interval. At `n=8`, the interval has length zero and the
displayed estimate is equality. The endpoint and off-by-one cases are
therefore consistent.

## 4. Global positive-reset identity

After stripping an initial even numerator, let `w_j/3^j` be reduced,
positive, and odd at a positive denominator level. One odd rational step
gives `(w_j+3^(j-1))/(2*3^(j-1))`. For `j>1`, the numerator is still a
unit modulo 3; the denominator level drops by exactly one. The same
formula at `j=1` reaches an ordinary integer.

Removing all factors of 2, including the one used by that odd step, gives

\[
k_j=v_2(w_j+3^{j-1})\ge1,\qquad
2^{k_j}w_{j-1}=w_j+3^{j-1}.
\]

The block comprises one odd step and `k_j-1` even steps. Summing

\[
k_j=\log_2w_j-\log_2w_{j-1}
 +\log_2(1+3^{j-1}/w_j)
\]

proves the exact displayed telescope, with the sign of
`log_2(w_R/w_0)` as written. Its clock begins after the initial stripping;
that earlier clock is not claimed to be part of `K`.

For `w_j=1`, reduction modulo 8 proves valuation 1 for even `j-1`, and
valuation 2 for odd `j-1`, including the boundary `j=1`. The source does
not turn this local observation into an unproved global estimate. Its
stated remaining gap is precisely a bound for the linked full sum under
the fixed ordinary-source constraint.

## 5. Independent exact controls

The independently written `check_carry_written_review.py` uses exact
`Fraction` arithmetic and explicit exceptions, not Python `assert`.
Normal and `python -O` executions returned the same JSON values. They
cover 168 all-target lifts, 35 lifts with selected extra complementary
prefixes, 12 true-dual examples, 320 complete positive-reset sequences,
and the unit-reset valuations at 40 levels. They also check intermediate
parities, the negative-sector endpoints and bounds, and the complete
multiplicative form of the reset telescope.

| Artifact | SHA256 |
| --- | --- |
| `check_carry_written_review.py` | `6c4e401cf66fbb6c444a30b5e5df0b12066296ad1136a4573b104d168da47e5c` |
| `CARRY_WRITTEN_REVIEW_CONTROLS.json` | `d8e2116f14825acca346d0d524a1485469c004b56b68bef337bc48af2a7c4467` |

These checks are selected controls only. The review's universal conclusions
come from the symbolic arguments above. No convergence construction,
improved global certificate bound, or Lean certification follows from
this review.

## Addendum: final source after the scope clarification

The author changed exactly the clock paragraph's opening sentence to:
“For n>2, the original finite affine formula now gives an exact clock bound:”.
The final source SHA256 is
`cd2edcd77dec25f0d67948a715faf1071cb4dd39c3c2fb003b58ed8cfcdad0b3`.
Reversing only that sentence reproduces the original reviewed SHA256 above,
so the rest of the source is byte-for-byte unchanged. This resolves the
scope clarification: **PASS on the final written source, with no remaining
requested corrections.** All review boundaries above remain in force.

The independent checker is unchanged at SHA256
`6c4e401cf66fbb6c444a30b5e5df0b12066296ad1136a4573b104d168da47e5c`.
It was rerun on this final note under normal and optimized Python; outputs
were byte-identical and all previously listed controls passed. The refreshed
`CARRY_WRITTEN_REVIEW_CONTROLS.json` SHA256 is
`c59782e0ae11df810f2e80adfb5fc5fd9a929d11056755b522ab30f312e4f50a`,
superseding the earlier controls hash in the table.
