# Review of the final backward-failure closing attempt

Reviewer: `/root`. Author: `cycle_arithmetic`. Date: 23 November 2026.
Independent project-agent review; not external peer review.

**Verdict: VERIFIED written consequences and finite controls. No
universal horizon inequality or Collatz closure is established.**

Frozen target:
`research/profound-step-20261123/arithmetic/FAILURE_POSITION_RESETS.md`.
SHA-256:
`28406b5165f1cba6d8317456920654d13f3204846104f289d68e13b1978c825a`.

I independently reconstructed the four cases from the already reviewed
boundary recurrence. At 01, both raw numerator and denominator gain a
factor of three. At 10, neither changes. Thus both alternating cases
preserve the rational candidate and its reduced denominator.

At 00 the new numerator is `3A_K-2^(K+1)`, a unit modulo three,
and the new terminal inverse step is literally `1 -> 1/3`.
The full exponent and immediate failure position in (2) follow.
At 11, existing cancellation means `b_K>0` and `3 | A_K`.
Adding `2^(K+1)` makes the new numerator a unit, while the raw
denominator is unchanged. In the full-denominator case the displayed
valuation identity is exact, and the quantified congruence correctly
has an empty range when `b_K=0`.

The source-3 table follows from the literal shortcut prefix
`3,5,8,4,2,1,2` and complementary carries `D_2=0`, `D_3=4`,
`D_4=20`. The new even terminal step immediately fails at indices
2 and 3, respectively. This refutes monotone decrease of this
particular failure index; it does not exclude eventual convergence.

The source-27 states at clocks 5 and 7 are 71 and 161. Both have
one preceding even step and carry four. Their numerators are
`64-4=60` and `256-4=252`, which reduce to 20 and 84. With
`bl(27)=5`, the horizons are exactly 82 and 98. A separate exact
Python evaluation using integer shortcut steps and `fractions.Fraction`
reproduced all five table rows and these horizons. The execution was
limited to those displayed controls; no large numerical census was run.

Finally `3^r < 2^L` gives `L > r log_2(3)`. Inserting it in the
positive horizon formula proves `H > 9 log_2(3) r^2`, including the
trivial strict inequality at `r=0`. Thus `H<=K` implies the stated
strict square-root bound for `r`. This is necessary, not sufficient,
and imposes no unproved growth law on the actual even count.

The closing attempt correctly leaves simultaneous numerator and
denominator saving open. No new external theorem, Lean result, or
asymptotic obstruction is claimed. No repair was needed.
