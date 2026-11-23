# Integration review: analytic claims and Lean scope

23 November 2026. Reviewer: `/root/source_construction`.

**Verdict: VERIFIED for Section 3 and the stated Lean scope.** This review
binds `research/literature-push-20261123/README.md`, SHA-256
`4ba8cf99b8f850ba80f4abcaad91eedfe5e957ad3bd7ec511b255c5d587b5b66`.
It is an author integration check: the reviewer authored the original
rigidity packet and both arithmetic Lean modules, and contributed the
initial small-hole estimate used by the root-owned addendum. It is not
an independent mathematical review of those authored results.

Section 3 accurately states the scalar rational-or-natural-boundary
alternative under a limiting parity density. It distinguishes the actual
binary value at two from the full arithmetic Taylor germ required by J.
The general-density equivalence is conditional on the existence of that
density. The removed-hole estimate and its displayed logarithmic bound
are scoped to complex radius above two; the smaller-radius cases use
the separate disc arguments. J is explicitly unproved, and eventual
periodicity is not presented as exclusion of nontrivial cycles. The
deflation and finite-filter statements match their frozen proofs.

The Lean scope matches the compiled declarations. The first module
proves strong divisibility for the actual homogeneous sum, and the
second derives the finite-pattern numerator coprimality from the base
and index hypotheses. `full_numerical_gcd_dvd` proves the complete
numerical gcd divisibility for an arbitrary finite index set, retaining
prime-power multiplicities. The index correctly leaves word legality,
primitive period, exact cyclotomic polynomial gcd, and the reduced
denominator magnitude estimate in written mathematics. The count of
22 new theorem declarations and the stated compiler, mathlib, strict
build settings, and axiom scope agree with the author receipts and
root's separate fresh build report. No correction is requested.

The separate reconstruction review of the root-owned general-density
proof is `rigidity-general-density-review.md`, SHA-256
`ec73b514ae472153ddb27086f924843aa5c11d29dda6f9d1e4562bdf1c5ead1c`.
This integration check adds no Collatz closure claim.

Final metadata refresh: after precision edits confined to Section 4,
the reviewer reread Section 3 and the Lean-scope subsection against the
earlier reviewed text and confirmed that both were unchanged. The
full-artifact hash above now binds the final index. The review scope and
mathematical verdict are unchanged; no new proof or test is claimed.

Release normalization refresh: hashing the current index bytes plus one
newline reproduces the previously bound index hash. Its sole subsequent
change removed that redundant final newline. The full-artifact binding
and the separately refreshed general-density review hash above are
updated; no mathematical content or review conclusion changed.
