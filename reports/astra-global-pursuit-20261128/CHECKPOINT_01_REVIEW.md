# Checkpoint 1: independent mathematical reconstruction

28 November 2026. **The research pass continues; Collatz is unresolved.**
The coordinator reconstructed the arguments below from the stated equations,
rather than treating agreement among agents or successful scripts as proof.
This review applies to the specified source bodies. External analytic inputs
retain their own provenance and are not promoted to locally formalized results.

## 1. Logarithmic capacity of an entire block

Source: author commit `9b894a0efc2b5fc2f9089d4f040cfe62dce2e8a8`,
`research/astra-global-pursuit-20261128/dynamics/GROWING_BLOCKS.md`,
Theorem 1 and equations (3)–(8).

**Verdict: VERIFIED written deduction, source-qualified at its scalar input.**
For Haar two-adic anchors and D consecutive arms, the probability that
simultaneous equality of values and odd counts has not occurred by date t is
at most C(1+log D)/sqrt(t+1), capped at one. This matches the order of the
previously published logarithmic capacity lower bound. The corresponding
whole-block time scale is (log D)^2. Ordinary integer windows inherit the
estimate with the explicitly retained residue-counting error 2^t/X.

The crucial new mechanism is the following. Conditional on one common source
prefix r modulo 2^j, each remaining label is an affine function 3^q z+c of the
same unread Haar input. Its residual R=c−3^q r/2^j is nonnegative and obeys
R'=(3^b R+b)/2. Each individual b is fair over the two refinements, even
though the arms are correlated. At a fixed q, different labels have residuals
spaced by an integer. This gives a packing bound on their number. A fractional
moment contracts strictly; deleting duplicate labels only decreases its
positive mass. After C log D dates, the expected total weighted number of
labels is O(log D).

Sorting the remaining labels by q is essential. Consecutive grade differences
telescope to at most j, while the normalized pair offset is
|R_next/3^gap−R_current|. Each residual enters at most two comparisons.
The imported scalar tail can therefore be summed without a factor D.
The conditioning date is deterministic, all subsequent bits are still fresh,
and transitivity gives whole-family agreement at the one final deadline.

The coordinator read the primary [Weaver paper 124/v1](https://rstation.ai/problems/collatz/papers/124/v1),
especially its scalar equation (3), its deterministic lower comparison, and
the ordinary transport statement. It explicitly states the needed uniform
Leen estimate with U=|c|/3^k, not an unnormalized offset. The direct Zenodo
Leen page could not be retrieved by the coordinator's browser tool. This
review uses Weaver's stated scalar input; it does not claim to have rebuilt
Leen's proof or a formalization. The prior fourth-power logarithmic upper
bound and lower capacity comparison are credited to the named sources.

**Local Lean:** the five roots of `BlockResidual.lean` were freshly compiled
by the coordinator with Lean 4.34.1 and warnings as errors. They prove the
integer residual transport, distinct digit parities, normalized offset
cancellation, and within-grade spacing. The printed axioms are only
`propext`, `Classical.choice`, and `Quot.sound`. The probability argument,
fractional moment estimate and all-time tail theorem are written proofs.

**Independent finite replay:** the coordinator's separate implementation
recomputed literal integer paths on 8,184 source-prefix/block combinations,
including 395,901 positive lifts and 263,934 exact residual refinements.
It checked packing and sorted offsets without floating arithmetic. Both
normal and optimized Python produced identical output. These are bounded
interface checks, not a numerical verification of the asymptotic theorem.

The theorem still allows a prescribed positive source to be exceptional.
Its density-one block guarantee does not put an ancestor of 1 inside every
block. The full-proof consumer is therefore still under investigation.

## 2. A complete finite skeleton at every bounded even grade

Source: author science commit `ae57f567d574be8e430bc716c8bf8735ab78709e`,
with rendering correction `f947c81ee4373c7181de56b3a2179ab83a1ba51e`,
`research/astra-global-pursuit-20261128/arithmetic/CENTERED_ADJACENT_RETURNS.md`,
Sections 1–3. The rendering correction does not change the mathematics.

**Verdict: VERIFIED written determinant/skeleton argument; finite exact
enumeration supports the displayed grade tables.**
For centered adjacent trajectories U=x+1, V=x+2 and even counts a,b,
the determinant D=3^b V−3^a U satisfies the stated two-arm recurrence.
If the terminal even counts both equal e and the terminal gap is ±1,
backward propagation gives |D_i|≤3^e at every earlier date: the correction
difference has magnitude at most 3^e. In a nonzero shared-odd run,
the final integer determinant is divisible by 3^r, so r≤e.

Only the exact proportionality D=0 permits unbounded shared-odd repetitions.
After their removal, the count sum increases on every active edge and the
absolute determinant increases on every other edge. There is no remaining
directed cycle. The skeleton length is at most 2e^2+3e. Reinserted loops
are independently legal on the uniquely reconstructed positive binary
cylinder. Thus a finite rational generating sum counts all clocks at each
fixed even grade; this is stronger than a bounded time census.

The complete grade-four graph has two unbounded negative-gap skeletons and
no unbounded positive-gap skeleton. At t≥9 the maximal common odd count is
t−4 and exactly two source residues attain it. The two inverse formulas are
obtained by evaluating the fixed suffixes at the formal centered origin,
then restoring the full positive ordinary source. The ternary divisibility,
the binary parity cylinder and positivity are all retained.

The least-failure exclusions use t=12 and the strict inverse slope
2^12/3^8<2/3. The coordinator checked both affine constants and the
substitution y=(3n−1)/2. These exclude two specified ternary residue
families only. They do not cover every possible least failure.

The exact graph script was inspected and rerun normally and with Python -O.
It matched 288 signed coefficients against 65,535 canonical native starts
and replayed 672 complete ordinary inverse pairs through clock 120.
No Lean claim is made for this packet at this checkpoint.

## 3. One explicit predecessor family in every large translated window

Source: author commit `2dde14dc80d7c5ead6b684d5a1e884e23cd64207`,
`research/astra-global-pursuit-20261128/wild/ORDINARY_WINDOW_RAYS.md`.

**Verdict: VERIFIED written construction and exact convergent-denominator
window; source-qualified power-log simplification.**
For any fixed positive odd unit target, fixed initial binary word and fixed
ternary residue, the same explicit two-parameter family visits the target
and meets every sufficiently high interval of the stated width. It also
provides an actual chronological path with O(log n) shortcut steps.

The exponent interval contains exactly one period of powers of two modulo
the specified power of three. Every resulting inverse vertex is a unit,
and the spine grows at least geometrically. The accumulated logarithmic
correction converges with exponentially small remaining tail, giving a
fixed irrational mantissa rotation modulo the congruence period. One final
free inverse exponent fits the required real window while preserving the
exact residue. The prescribed initial parity word is recovered by full
divisibility and backward parity, not by assuming a real affine path is legal.

A consecutive convergent-denominator block of phases is a controlled net.
Its positive buffer exceeds both affine errors, and the chosen last
exponent is positive. The passage from the exact denominator q(X) to a
power of log X uses a classical two-logarithm lower bound. The latter
external theorem is named in the source; the elementary window proof does
not require its numerical constant. Historical priority for this rotation
construction has not been established.

The sparse family's own octave count gives a lower gap of order X/log X.
This is a limitation of that family, not an empty interval in the full
predecessor basin. The width is too large for the current block-merger
consumer. The agent is pursuing multiple spines and a separate cycle trace.

The exact finite replay checks ordinary paths, complete prescribed prefixes
and congruences, and selected large translated windows. It does not prove
the all-location asymptotic by testing finitely many windows.

## Continuing research

The all-time ordinary quantifier remains unresolved. Work continues on
unrestricted adjacent inverse returns, positive-anchor multigrade estimates,
and actual fixed-root trace/short-interval mechanisms. These are attempts
to discharge the missing global inference, with freedom to change course.
