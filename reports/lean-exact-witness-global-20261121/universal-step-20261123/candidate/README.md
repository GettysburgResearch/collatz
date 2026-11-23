# Negative-numerator recognition: execution and scope

23 November 2026. The scientific note is
[`NEGATIVE_NUMERATOR_RECOGNITION.md`](../../../../research/lean-exact-witness-global-20261121/universal-step-20261123/candidate/NEGATIVE_NUMERATOR_RECOGNITION.md).
The new result recognizes a supplied triadic candidate in the binary length
of its negative reduced numerator, with an exact first-crossing check.
Universal candidate construction and full Collatz remain open.

## Executed checks

- [`REPLAY.json`](REPLAY.json) records exact commands, Lean version, source
  hashes, exit codes, and output hashes.
- [`lean-strict-audit.log`](lean-strict-audit.log) contains thirteen public
  declaration audits from strict Lean 4.34.1 compilation. Every transitive
  axiom set is a subset of `propext`, `Classical.choice`, and `Quot.sound`.
- [`normal.json`](normal.json) and [`optimized.json`](optimized.json) are
  byte-identical outputs of the new recognizer's finite controls: sixteen
  true inputs, sixteen unreduced presentations, 64 wrong candidates, two
  wrong first crossings, one giant binary exponent, and sixteen exact
  power-of-two equality cases. No assertion statement is required for the
  checks to execute.
- [`SOURCES.json`](SOURCES.json) pins the inspected peer inputs and their
  exact uses. No historical corpus was replayed.

## Scope boundary

The Lean module proves the integer halving and clock arguments, bounds on
complete backward negative codes, literal first-crossing replay, and the
ordinary-hit soundness of its executable checker. It has no definition of
the infinite 2-adic autoconjugacy and no universal candidate-existence axiom.

The full equality-to-Omega characterization is a written theorem: its
completeness uses the pinned prior triadic rigidity theorem and the forced
standard terminal segment. The equality case of the sharp height bound and
the polynomial bit-complexity interpretation are also written scope.

The finite controls test the new executable and its emitted complete
exponent identity. They are not evidence that every input admits a
successful candidate. Normal and optimized execution are distinct from
the symbolic proofs and from repository integration validation.
