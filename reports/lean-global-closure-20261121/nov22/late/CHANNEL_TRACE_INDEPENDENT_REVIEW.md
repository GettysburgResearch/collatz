# Independent review: sourcewise five trace and fixed-radius divergence

Date: 2026-11-22. Reviewer: global_analytic22.

**Verdict: VERIFIED under the displayed imported inputs, for Sections
3–4 of LATE_CHANNEL_FIVE_TRACE.md.**

Reviewed source: agent22_merger/LATE_CHANNEL_FIVE_TRACE.md.

SHA256: 29340c0d6dec69e6e4505f98849db1106be47d4ff986d1659d281cb9da820915.

This review covers the new deductions from the signed-source boundary
formula, the finite-five-energy rigidity statement, and the odd-clock
return exclusion supplied in the note. It does not upgrade the imported
analytic hypotheses, independently replay a Lean unit, or certify the
entire PR183 channel construction.

## Sourcewise boundary trace

The first odd ternary-unit projection is an actual orbit point and
preserves the ordinary component. On the specified odd-unit domain of
the five-energy, both projections reduce exactly to the original
sources \(n\) and \(5n\). The definition omits zero-coefficient atoms,
so it does not introduce a Dirac mass outside the killed domain.

For a fixed escaping component, applying the stated two-source boundary
formula gives its squared Boolean mismatch divided by the positive
component mass. The equality between squared and absolute Boolean
mismatches gives exactly the displayed sourcewise trace. The limit is
taken before the nonnegative sum. The source labels are preserved until
after the separate quadratic energies are computed. Thus asynchronous
mergers cancel within the same original source pair; unrelated pairs
cannot spuriously cancel each other.

The deduction that this trace is infinite for an escaping-component
indicator uses the separately displayed rigidity theorem. The source
explicitly retains that theorem's analytic assumptions.

## Cycle-sensitive extension

In a periodic component the two tails at a fixed cycle coordinate have
the same denominator \(1-r^p\). If both atoms lie in that component,
their numerator is a difference of two fixed powers of \(r\), so the
resolvent difference stays bounded as \(r\uparrow1\). Its normalized
energy therefore tends to zero. An unmatched nontrivial periodic tail
has the uncancelled energy pole and yields infinite normalized residue.
The basin of the killed point contributes zero. This proves the stated
case division and its lower bound by the basin-of-one mismatch.

Under the stated rigidity input, finiteness of the exact sourcewise
trace would force the basin indicator to be constant. Since it takes
value one at one, this would prove universal entry into that basin.
The note correctly presents this as a missing estimate, not a theorem
of finiteness.

## Fixed-radius whole-source divergence

For \(n\ge5\,9^J\), the supplied odd-clock return bound excludes a visit
from \(5n\) to \(n\) by time \(J\). At coordinate \(n\), the source atom
contributes one if \(n\) is nonperiodic, or \(1/(1-r^p)\) if periodic.
The second atom contributes either zero, one later discounted visit,
or the corresponding discounted periodic tail. In all cases the
difference is at least \(1-r^{J+1}\).

The common pointwise reference upper bound, including periodic states,
then yields the claimed per-source quadratic lower bound. Summing
against \(1/n\) over the two odd-unit arithmetic progressions diverges.
Every sufficiently large positive odd ternary unit is included,
regardless of whether it is periodic or nonperiodic. No unproved density
claim about the nonperiodic domain is used.

The weaker lower bound from \(5n\ne n\) also checks. The new return
theorem supplies the quantitative arbitrary-window cutoff, while the
basic fixed-radius divergence does not depend on it.

## Scope conclusion

The distinction between a sourcewise boundary limit and a fixed-radius
whole-source sum is mathematically necessary, and the note preserves it
throughout these sections. No substantive correction was found.
