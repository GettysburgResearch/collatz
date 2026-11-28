# Dynamics checkpoint 3

The [centred boundary amplitude](../../../research/astra-wild-nine-hour-20261128/dynamics/CENTRED_BOUNDARY_AMPLITUDE.md) has a direct written proof on the actual positive map. Its complete real range closure, derivative ranks, native cylinder extrema, positive-rational membership test and detection of a prescribed finite path use elementary arithmetic. Original-source density and the sign of any unverified orbit are unnecessary. The cited earlier work supplies context for the multiplier and the elementary terminal-lift construction.

The [exact finite replay](../../../research/astra-wild-nine-hour-20261128/dynamics/check_boundary_amplitude.py) ran with Python integer and Fraction arithmetic and returned

```text
PASS 167 odd units, five rank tests per unit, four rational exclusions, sixty explicit rank-point approaches
```

This is a finite implementation check, separate from the written assertions about limit points and all sources. No new Lean compilation is claimed for this checkpoint. The range can decide whether a fixed positive rational occurs. Whether it contains *some* dyadic numerator over every prescribed odd unit denominator is the outstanding global problem.
