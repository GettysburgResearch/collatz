# The fast edge of the first-hit clock distribution

[FLAT_EDGE_PRESSURE.md](FLAT_EDGE_PRESSURE.md) gives matching upper and lower estimates for the largest number of ordinary inputs in a fixed clock window around the fastest possible speed plus a small relative excess. The exponent agrees to all algebraic orders with binary entropy minus the ternary congruence cost, uniformly over every positive odd target prime to three. The proof bounds each true inverse tree using finite ternary cylinder corrections and converts its counted words into first-hit sources in the same dyadic shell. The scale limit precedes the small-excess limit.

[DyadicClock.lean](DyadicClock.lean) proves exact ordinary transport for inverse words with exponents at least two, the integer height footprint, the physical hit after lifting to a dyadic shell and the difference-at-most-one bound on the resulting clocks. Its import is the phase-one FiniteTrace module. The analytic pressure estimate and the positive-prefix variant allowing exponent one remain written proofs.

[pressure_controls.py](pressure_controls.py) checks the finite ternary action in exact rational arithmetic and in its truncated Taylor series at geometric parameter zero. It checks Haar preservation at each coefficient, the first four orders of cancellation, explicit positive upper and lower barriers at parameter 1/100, and propagation of those barriers over a further two levels.

```sh
python pressure_controls.py --check
python -O pressure_controls.py --check
```

Both commands reproduce [PRESSURE_CONTROLS.json](PRESSURE_CONTROLS.json). The Lean file was built with Lean 4.34.1, strict warnings, and the project's pinned mathlib. Its four displayed axiom inventories contain only standard axioms. These results do not determine the future of the target.
