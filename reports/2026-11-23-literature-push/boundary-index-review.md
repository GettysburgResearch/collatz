# Scope check of the checkpoint index, Section 4

23 November 2026. Reviewer: `/root/actual_collision`, author of the
underlying boundary note. This is an accuracy check of the root-authored
summary, not a second independent review of the reviewer's own theorem.

**Verdict: VERIFIED WITH PRECISION FIXES APPLIED.**

- Target: `research/literature-push-20261123/README.md`, Section 4 only.
- Frozen target SHA256:
  `4ba8cf99b8f850ba80f4abcaad91eedfe5e957ad3bd7ec511b255c5d587b5b66`.
- Underlying note:
  `research/literature-push-20261123/boundary/CANONICAL_FIBRE_DEPTH.md`,
  SHA256 `118ce0a322d68ae683789d1647060c4bc16e39086ee96ae443f68d877c2b1999`.

The summary preserves the specified iid affine model, exact renewal-tail
constant, trace-weighted Cesaro measures, unchanged original ordinary
source, and reversed prefix. It keeps the full finite factor `Lambda_j`
and explicitly imports `inf_j Lambda_j>0` for the uniform square-height
conclusion. The extra trace upper bound is confined to the normalized-law
corollary.

Two requested precision fixes are present in the frozen text. First, the
accuracy requirement is explicitly an `o(q_j)` discrepancy between
`h(q_j) mu_(q_j)` and `bar eta_M^(q_j)` in the one specified scaled
bounded test `f(R/q_j)`. Second, arbitrary positive weights use
`sum_m w_m 3^m >= c q_j^2`; the additional Cesaro factor `1/M` is not
assigned to those general weights.

The necessary budget is not described as a sufficient construction or
as a convergence-rate theorem. Fixed-root weak convergence is not
upgraded to a moving-root Fourier comparison. The same-source collision
upper and escape contradiction remain explicitly open. No further
change to this section is requested. This verdict does not review the
other sections, release checks, or later edits of the index.
