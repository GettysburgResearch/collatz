# Scoped review of the odd-count return theorem and channel composition

Date: 2026-11-22. Verdict: **VERIFIED at the stated arithmetic and composition scope.**

Reviewed new Lean source:
`CollatzGlobalClosure/OddReturnClock.lean`, SHA256
`f532f89fb9042e7073e992bf26e0049f28829171075e23e87edfa50fd66439ac`.

Reviewed written composition:
`LATE_CHANNEL_FIVE_TRACE.md`, original supplied SHA256
`29340c0d6dec69e6e4505f98849db1106be47d4ff986d1659d281cb9da820915`.
Publication only changes its receipt reference to a working relative link.

## Finite arithmetic

The integrating reviewer independently reconstructed the argument:
if an actual return sends `m*n` to positive `n`, let `a` be its
actual odd count and `v=floor(n/3^a)`. The existing exact quotient
identity makes `v=floor(m*n/2^h)`. Nonnegative affine correction and
nonresonance give `2^h>=m*3^a+1`; hence
`(m*3^a+1)*v<=m*n<m*3^a*(v+1)`. Thus `v<m*3^a` and
`n<m*9^a`. A nontrivial odd divisor of `m` rules out resonance with
the power of two, with no coprimality-to-three requirement.

The four public statements retain actual source, endpoint, odd count,
and positive-source hypotheses. The multiplier-five corollary concerns
a return to `n`, not arbitrary downstream mergers. It does not assert
existence of such a return.

## Written channel deduction

With the explicitly imported ordinary harmonic and channel inputs,
a signed pair in one escaping component has two diagonal Abel residues
and one asynchronous cross term. Retaining that term gives the required
cancellation even for unequal meeting clocks. The component-indicator
trace therefore equals the displayed five-energy divided by the
component capacity. Taking the boundary source by source is essential.

The cycle-sensitive fixed-radius lower bound correctly considers both
periodic and nonperiodic starting points. At coordinate `n`, an
unmatched source or a delayed hit from `5*n` leaves at least
`1-r^(J+1)` when `n>=5*9^J`. On a cycle the additional denominator
`1-r^p` only increases this lower bound. The bounded reference then
gives harmonic divergence over all odd ternary units at every fixed
`0<r<1`. No density assumption for the nonperiodic subset is inserted.

The source notes are pinned at PR183
`68345f60a4f757acb42a69a4ac95910f8ce26163`, with the explicit inherited
PR185 and finite-five-energy rigidity dependencies retained. This review
checks the new deductions from those interfaces, not every upstream
analytic proof. The pointwise finite-boundary estimate remains open.

The author's [development receipt](ODD_RETURN_CLOCK_REPLAY.json) and the
integrating fresh complete-checkout compilation are distinct evidence.
No fresh integrating execution is asserted by this semantic review.
