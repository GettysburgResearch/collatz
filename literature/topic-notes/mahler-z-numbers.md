# Mahler Z-numbers and the repository's `2`-adic survivor problem

## Classical problem

Mahler studies real numbers `ξ>0` for which the fractional parts of `ξ(3/2)^n` remain in the lower half of the unit interval for every `n`. Such numbers are traditionally called Z-numbers; their existence remains unresolved. [@Mahler1968]

Flatto, Lagarias, and Pollington prove lower bounds on the range of fractional parts of `ξ(p/q)^n` for rational `p/q>1`. Their theorem is archimedean: it concerns real fractional parts and interval diameter. [@FlattoLagariasPollington1995]

## Repository analogue

`CLAUDE/Q-0002` asks whether a `2`-adic coded set for the induced ratio `81/64` contains an ordinary positive integer in a lifting class. The orbit restriction is expressed by base-64 digits and a carry-preserving map.

The shared pattern is a multiplicative orbit constrained to a proper digit/interval set. The differences are decisive:

- real topology versus `2`-adic topology;
- fractional-part reduction versus an integral carry map;
- a fixed interval condition versus a digit-cylinder condition;
- existence in `R` versus intersection of a `2`-adic attractor with `Z_{>0}`.

## Verdict

`PARTIAL OVERLAP / ANALOGY`. “A `2`-adic analogue of Mahler's problem” is accurate. “Equivalent to Mahler's Z-number problem” is not supported by any located source.

A comparison of Haar measure `1/32` with an FLP real interval threshold does not transfer the theorem. It can be recorded only as a heuristic reason the most naive interval obstruction has no evident analogue.
