# Every valuation-one psi query returns

This result uses the original complete-source multiset induction. It removes
an entire initial-valuation branch, with no restriction on the supplied odd
source word. It does not assert the remaining universal interval selector.

Let `Certificate q gaps` be supplied, let the known source be `S = 2q`, and
assume the interval induction hypothesis below `grades 1 gaps`. The initial
even grade is `3`; deleting just this grade leaves `grades 0 gaps`. Thus the
same complete odd certificate `q, gaps` can be used with a strictly lower
interval induction hypothesis. No newly obtained convergence certificate is
substituted into the rank comparison.

The exact two-odd-step target identity is

\[
9(4q-1)+5=4(9q-1).
\]

It gives the legal positive-gap prefix `[1,1]` from `psi(S) = 4q-1` to
`9q-1`. The theorem `CollatzLowGapGlobal.negative_nine_return` returns the
latter carry for every complete odd source certificate. This proves the
whole valuation-one psi step, including the empty source word.

The formal theorem actually proves the larger lattice. If `k >= 0`,
`t > 0`, and

\[
t+16k=4q-1,
\]

then the same target prefix ends at

\[
v=9q-1-36k>0.
\]

Here `v <= 9q+3` and `v mod 4 = (q+3) mod 4`, so the entire target lattice
falls under `nine_lattice_return`. The boundary `k=0` is the psi theorem.
All odd source gaps, their count, and the target offset are unbounded.

## Lean interface

`lean/Collatz/PsiValuationOne.lean` exports:

- `erase_initial_even`: the complete-source rank comparison.
- `lattice_rule`: the unbounded target lattice under the original lower-rank
  interval hypothesis.
- `psi_rule`: every valuation-one psi query, with the complete odd source
  certificate unchanged.

These results are conditional step rules for the existing well-founded
induction. They do not replace its interval hypothesis by a psi-only
hypothesis. In particular, valuation-two and valuation-three psi queries,
and other uncovered low-gap interval queries, are not silently discharged.

The proof is original composition of the current branch's carry return and
complete-source rank rules. No numerical verification threshold or external
analytic result is used.
