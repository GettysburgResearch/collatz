# Independent review: finite padding funds the signed normalizer

Reviewer: atomic-exclusion lane, separately from the target-note author.
Date: 23 November 2026.

**Verdict: VERIFIED at the written claims TP1--TP14 and TP-F, with their
stated hypotheses and scope. The complete target-entry theorem remains
OPEN.** The padding theorem removes the binary-clock funding obstruction;
it does not assert convergence of the remaining positive endpoint.

## Frozen source and evidence boundary

Reviewed source:
`research/lean-exact-witness-global-20261121/TARGET_PADDING_CONTINUATION.md`
at SHA256
`ea71e2142b4ae3e85f868e92e89fe7786364af90380a17ac06a7bc11e2dc0512`.

I reconstructed the finite argument independently before the note froze,
then checked its final text, formulas, clock conventions, and scope.
The signed-normalizer and six-step-family inputs are TE8--TE16 of the
previously reviewed `TARGET_ENTRY_CONTINUATION.md`, at SHA256
`a1d0142df4803f0091e373dfe749cc02887a4fb0891e95e935c428c91fee9cb0`.
This addendum contains no new Lean module or executable control. This
review claims no new compilation, computational replay, or audit of
the external PR176 files discussed in its final section.

## 1. Padding retains the original ordinary source

Appending L copies of the actual odd edge `1 -> 1` with gap two gives
length `r+L`, total `A+2L`, and correction
`3^L C+2^A(4^L-3^L)`. Substitution in the complete source identity verifies
the new certificate for the same x. The displayed signed numerator
formula follows by subtraction and division by two. Padding changes the
signed input; no old signed trace is reused without justification.

The normalizer decreases its denominator exponent once per odd shortcut
step. Its parity agrees with the actual target while the unused binary
exponent is positive. If it has not completed by `H_L=A+2L-1`, the
coupling remains valid through that clock and its denominator exponent is
`r+L-q_(H_L)>0`. Conversely, the `(r+L)`-th odd step by that clock
completes it. This proves TP4 without assuming that a stopped normalizer
continues running. Completion exactly at `H_L` is allowed: the preceding
high block still has exponent one, hence even parity.

## 2. The finite funding dichotomy

Assuming no hit of one through clock t makes every odd input at least
three. Its shortcut multiplier is then at most `5/3`, while every even
step has multiplier `1/2`. This gives TP5 for the actual target and
actual odd-step count.

For `L=r-1` and `t=A+2r-3`, the contrary count `q_t<=2r-2`, together
with `y<=x` and the strict source inequality `3^r x<2^A`, gives exactly

`0<T^t(y)<(2/3)*(25/27)^(r-1)<1`.

Positive integrality is sufficient for the contradiction. Thus the target
either has already reached one or the padded normalizer is funded by
the stated finite clock. The r=1 case is valid, as A is at least two.
The argument requires no unknown stopping-time bound, escape hypothesis,
or residue-class restriction beyond the displayed source hypotheses.
I also recomputed the general sufficient guard in TP7; its constants and
strict inequality are correct. Every `L>=r-1` satisfies that guard.

## 3. Relative negative carry does not give an absolute descent

Multiplying the exact factors `3n/(3n+1)` at the first `r+L` actual odd
inputs gives TP9, including the factor of two in its numerator. On a
target never reaching one these factors are at least `9/10`, yielding
TP10. Since the physical endpoint is a positive integer, the ratio
tending to zero forces `d_L -> infinity`; the signed carry divided by
`2^d_L` then tends to -1. The moving scale prevents replacing this
relative conclusion by the absolute inequality TP11.

For the six-step control I checked the complete clock count. Its sixth
odd shortcut step finishes at clock nine, with the following even step
reaching `2^b-1` at clock ten. For each `1<=L<=b`, the next L steps are
odd shortcut steps, so the `(6+L)`-th odd step finishes at `10+L`.
This verifies TP12 without mistaking the sixth completion clock or the
final even endpoint at `L=b` for an accelerated odd-gap endpoint.

Subtracting `2^(b+L)` from the displayed ordinary endpoint gives exactly
the stated negative integer carry. I recomputed TP13 and the earlier
clock-ten descent. Thus the control really refutes automatic descent at
the normalization endpoint, including uniform padding L=5, while its
earlier descent makes it unsuitable as a least-counterexample control.
The note states both facts explicitly and does not infer divergence.

## 4. Coefficient transport and the remaining conclusion

Starting from the explicitly stated odd coefficient envelope and edge
equation, its extension to even states preserves `H(n)<=n^(-s)`.
Extension across an odd multiple of three gains the factor
`(3n/(3n+1))^s<=1`, so it preserves the same envelope as well.
Multiplication along the actual target prefix gives TP14 exactly.
For escape, a positive limiting path product and a bounded normalized
endpoint coefficient are compatible with a positive initial coefficient.
No vanishing conclusion follows from this transport alone.

The new result is an unconditional finite, admissible rewrite that funds
the signed normalizer, with an already-converged alternative. The final
endpoint may be even and is only an ordinary positive target with a
known prefix. A complete tail, or a justified earlier descent or merger,
is still required for the original unrestricted target implication.
