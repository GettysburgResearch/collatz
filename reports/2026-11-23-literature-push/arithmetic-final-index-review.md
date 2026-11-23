# Narrow arithmetic integration review

23 November 2026. Reviewer: /root/cycle_closure, author of the arithmetic
lane. **VERIFIED WITH FIXES** at the integration scope below. This is not an
independent scientific review of the reviewer's own theorem.

## Exact reviewed bytes

- Root index: research/literature-push-20261123/README.md,
  SHA256 4ba8cf99b8f850ba80f4abcaad91eedfe5e957ad3bd7ec511b255c5d587b5b66.
- Scope is Section 2 only, from its heading through the blank line before
  Section 3. UTF-8 SHA256:
  ba57ecbff04927d2cadce64f9c8d3be8676ccc4b7767f343568e81274fc6105a.
- Arithmetic theorem: research/literature-push-20261123/arithmetic/FULL_NUMERICAL_SEPARATION.md,
  SHA256 91d0afa1661956f7d5a80a22fe3f731925f33b2dc05516dcf2c844e6c22bf044.
- HomogeneousRepunits.lean:
  b94a7e0ce4223116dced184d4cb08d3b60572e2eac313154513177ff890488dc.
- PacketGCD.lean:
  cabc44a642841ef376734fed131a708897fca3b5e36c1d571d45f191b8ce892e.

## Findings and corrections

The final Section 2 faithfully preserves the actual disjoint-packet
hypotheses, literal word, complete polynomial residual, full numerical gcd
including overlapping prime powers, unbounded packet count, primitive period,
and arbitrary rational-floor statement. The lower bound on the final
denominator and retained polynomial degree fraction match the written theorem.

Three integration corrections were requested and verified in the exact
bytes above:

1. The descending ordinary finite realizer is explicitly chosen above the
   rational fixed point C/D. The summary does not claim that the written proof
   established descent for all possible finite ordinary realizers.
2. Pairwise repunit coprimality carries the necessary index condition i != j.
3. The offsets are the explicit representatives 0 <= s_i < r, preserving the
   exponents in the displayed numerator.

The formal boundary is accurate: the full homogeneous-repunit gcd and the
literal packet numerator's full gcd divisibility are Lean theorems.
The actual Collatz word construction, primitive-period argument, and complete
polynomial gcd remain written mathematics. The index does not represent them
as formalized.

The family conclusion excludes every member from integer closure, and the
missing reduction or comparable bound for arbitrary candidate profiles remains
explicit. No unrestricted nontrivial-cycle exclusion follows. No review verdict
is given here on Sections 1, 3, 4, or the rest of the repository.
