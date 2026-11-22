# Independent arithmetic review

**Verdict: VERIFIED for the stated written arithmetic claims, using the
explicitly identified external Matveev theorem.** This is an internal
independent mathematical reconstruction, not acceptance of a full Collatz
proof or a formalization of the external theorem.

Reviewed file:
`research/global-synthesis-20261122/ARITHMETIC_CLOSURE.md`

SHA256: `b40923eb93eb7984a62616dae756a467331beee02e41d4a290105bce39c602e6`.

The independent renewal researcher reconstructed Sections 2–6 and extended
the review to this final file after the empty-list clarification and Lean
evidence paragraphs. The lead researcher separately reconstructed the same
central arguments and inspected the two arithmetic Lean files and exact
Python checker.

## Checked mathematical obligations

- Rotation at a minimum proper prefix makes every suffix multiplier at most
  one; it supplies a small real translation at an actual cycle boundary.
- Repeated-block integrality gives divisibility of the same incoming
  ordinary defect by the entire binary repetition factor. Nonzero defects
  bound each clock; actual forward heights propagate the common source
  budget through every block.
- Zero exponents, the empty list/word, all-zero parity words, and block
  fixed points are kept separate. A fixed block identifies a cycle that is
  explicitly replayed, not assumed trivial.
- Matveev Corollary 2.3 was independently retrieved from the indexed primary
  paper. With two positive rational logarithms, degree one, coefficient
  maximum `L`, and `log(2)log(3)<1`, its bound `C1<=2^32` gives the displayed
  specialization. The passage from the denominator estimate to the integer
  cutoff is valid.
- The finite cycle list is complete for the supplied block product. For
  each listed cycle state, the divisibility criterion gives the finite
  allowed exponents or the exactly fixed-block free coordinate. This
  justifies the stated effective semilinear realization description.
- For `P^aQ^b`, neither executed boundary has zero defect. The `b>=a`
  inequality, Farey obstruction for every `a>=16`, and remaining 105 pairs
  exhaust all independent positive exponents. The Farey argument works for
  unreduced fractions and keeps the full denominator.

Independent exact calculations give
`H=4722397970736130105600`, Farey determinant one, and denominator-sum margin
`135083164865499615141`. The log enclosures and remainders are exact rational
objects; the executable checker composes each finite parity word separately
from the generator's closed formula.

The concrete Lean file was reviewed at SHA256
`9e24fdb7e8a6b9890cd8ddda476ac248c5f52f71108f905b64f9e6e385bcd435`.
Its predicates match the arbitrary-denominator Farey obstruction and all
finite whole-denominator exclusions. Fresh compiler execution is recorded
separately; a written semantic review is not a compiler receipt.

## Limits

The original proof of Matveev's theorem was not audited in its entirety.
The logarithmic-form application, real logarithm series remainder, and
infinite parameter coverage are written proofs. The generic large-cutoff
classification algorithm was not executed exhaustively. There is no
universal bound on the number or contents of blocks of an arbitrary cycle,
and this packet supplies no exclusion of all escaping ordinary orbits.
