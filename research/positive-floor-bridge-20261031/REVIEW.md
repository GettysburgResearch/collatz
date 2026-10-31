# Adversarial self-check of the positive-floor bridge

**Scope:** PFB-001--005 in the adjacent README, by the same assistant that
wrote the proof. This is not an independent-agent or external review.

| Check | Outcome and retained guard |
|---|---|
| Direction of the inverse operator | L takes source values to their actual Syracuse endpoint with weight 3/2^a; it is not the unweighted contact operator. |
| First-step law | The full even/odd exponent geometric sums are exactly 1 and 2; multiples of three have no predecessors. |
| Uniformity | alpha must work for every positive unit target. A target-dependent positive lower bound does not imply the theorem. |
| Prefix-free budget | Finite tree induction, then finite-subfamily supremum; no finite expected stopping time is assumed. Repeated endpoint states remain different word positions. |
| Arbitrary clocks | Leaf clocks are positive integers and may vary independently. They are not a hidden common total clock. |
| Infinite-branch limit | The tail is dominated by 3*2^-m plus the summable inverse tail of h. Pointwise convergence alone was not used to exchange the infinite sum. |
| Bootstrap direction | Fatou gives Lg<=g before the new domination argument proves equality. Harmonicity is not a premise disguised as a conclusion. |
| Source normalization | Canonical g refers to stationary rho, not the different weighted-construction varrho. Delta is log(4/3)/2. |
| Scalar priority | The pinned external manuscript already gives first-hit depth bounds and canonical trace results. These are credited, not relabeled as new discoveries. |
| Contact pairing | The second height moment pays the explicit polynomial root charge. The statement remains about weighted inverse transport; no unweighted contraction is inferred. |
| Zero-clock counterexample | At root 3 the exact Abel residue is zero while rho_0=1. Positive clocks cannot be removed. |
| Infinite dead frontier | Ld>=rho_1/21, hence L^q d>=rho_q/21; every dead leaf has no extension. Divergence uses a positive Abel-residue premise, not an unconditional claim of it. |
| Cycle treatment | U(1)=1 is unabsorbed and cycle weights are retained. The result neither excludes the trivial cycle nor silently rules out other cycles. |
| Evidence ceiling | Finite-model h is a killed Green function, not an approximation certified to equal the external canonical trace. No external Lean chain is executed. |

## Failed strengthenings retained

1. Dropping prefix-freeness double-counts full words. The verifier retains
   the empty word and one copy of the inverse 1->1 loop as an exact control.
2. Allowing arbitrary zero residual clocks defeats a root-only charge, as
   PFB-005 shows; assigning synchronized *total* clocks is a different theorem.
3. Replacing the uniform floor with the earlier polynomially decaying floor
   leaves endpoint growth in the bound and does not yield the new uniform tail.
4. Calling (15) a proof of Collatz would confuse Jacobian-weighted inverse
   mass with unweighted survivor mass and ignore cycle exclusion.

## Review priority

An independent reader should first check the two external input statements
at their pinned source and audit the uniform inverse-linear density argument's
coalescence and predecessor dependencies. For the new local algebra, the
most sensitive points are the clock-zero guard, the Fatou direction, and
word-level rather than endpoint-level prefix-free counting.
