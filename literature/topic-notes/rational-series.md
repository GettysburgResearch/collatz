# Rational integer power series and algebraic-integer growth ratios

## Repository use

`CLAUDE/T-0020` needs the following narrow fact: an integer-valued exponential-polynomial sequence cannot have a rational noninteger as one of the actual characteristic growth ratios if its generating series is rational.

KTHM-0008 proves a stronger, clean version:

> If `F(z)=Σ a_n z^n` has integer coefficients and is rational, every reciprocal pole of `F` is an algebraic integer.

The proof has two parts:

1. rationality plus rational Taylor coefficients gives a rational recurrence over `Q`;
2. evaluation in every nonarchimedean completion excludes poles inside a `p`-adic unit disk, so reciprocal poles are integral at every finite place.

This removes the need to rely on ambiguous “Fatou/Kronecker” shorthand. Fatou and Pólya–Carlson remain useful historical context for rational/transcendental dichotomies of integer power series. [@BorweinCoons2009]

## Scope warning

The imported lemma does not prove that a repository cofactor sequence is exponential-polynomial or rational-recursive. Those hypotheses must come from the definition of the schema being excluded.
