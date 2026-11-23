# Arithmetic construction attack

Read [TRIADIC_CONSTRUCTION_ATTEMPT.md](TRIADIC_CONSTRUCTION_ATTEMPT.md).

The target is the actual small triadic witness needed by the preceding
full-convergence implication. The candidate now uses the correct member
of the standard complementary cycle at its terminal clock, rather than
a zero terminal state. It changes only at failures of parity alternation.
Its exact paired increment identities, and the persistence of any
uncancelled 3-denominator under backward iteration, locate the arithmetic
cancellation that a successful construction must establish.

The attempted p-adic Subspace argument has two independent missing
hypotheses: the unknown dual is not known algebraic, and the actual
fixed-form product has no automatic negative-height-power saving.
The latter failure is explicit even on source 1, where the product tends
to one. Matching the terminal boundary removes this known-cycle artifact
but does not force the needed cancellation for all inputs.

The [Lean module](lean/TriadicBoundary.lean) checks the finite recurrence,
unit-numerator and alternating-source algebra. All infinite arguments
retain written-proof scope. **No universal witness construction or full
Collatz proof was obtained.**
