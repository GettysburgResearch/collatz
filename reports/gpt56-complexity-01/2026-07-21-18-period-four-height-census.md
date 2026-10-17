# Session report — primitive period-four height census

Agent: `gpt56-complexity-01`  
Issue: #18  
Branch: `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
Date: 2026-07-21

## Starting hypothesis

The small universal deficit at period four might be repaired automatically by
large gcds between the cleared numerator and denominator of the L-9410
approximants.

## Approaches attempted

1. Replaced repeated `Fraction` normalization by sparse integer polynomials in
   `T=64/81`.
2. Classified primitive binary length-four words up to cyclic rotation and
   complement.
3. Excluded the alternating word because it has true period two.
4. Evaluated the three primitive classes through Padé order three.
5. Cleared the exact universal odd denominator.
6. Computed the exact integer gcd and final reduced rational height.
7. Compared the exact error valuation with reduced height bit length.

## New results

### Empirical observation O-9401

For all three primitive cyclic representatives, the reduced exponent is below
one by order three. At order two it is already within roughly `1.5e-4` of one.

The observed gcd bit lengths are tiny compared with the million-bit rational
heights. No immediate large common-factor rescue appears in the frozen range.

### Exact experiment X-9409

The experiment covers

```text
(17,17,17,18),
(17,17,18,18),
(17,18,18,18)
```

at orders `1,2,3`.

Canonical SHA-256:

```text
bf85a00cc1b34aef1d85f5b7e483547b1200ac10e53c02375333447bb1c31546
```

## Candidate counterexamples

None. No period-four word is claimed rational, irrational, ordinary, positive,
or Collatz-valid from this computation.

## Failed approaches

### Easy-gcd rescue

The bounded data do not show a common factor remotely near the quadratic-scale
saving required by Q-9411. This is a failed finite heuristic, not a refutation
of asymptotic gcd growth.

### Nonprimitive control word

The first tested length-four word `(17,18,17,18)` was recognized as period two.
Its larger gcd structure is therefore irrelevant to the primitive period-four
question and was removed from the canonical census.

## Potential errors

1. Primitive cyclic-class enumeration should be checked independently.
2. Sparse polynomial exponent formulas must match L-9410 exactly.
3. Cleared gcd bit length is not itself logarithmic saving unless compared to
   the same cleared height.
4. Order-three behavior must not be extrapolated to infinity.

## Files changed

```text
experiments/X-9409-period-four-height/README.md
experiments/X-9409-period-four-height/run.py
experiments/X-9409-period-four-height/results/canonical.json
research/padic-repetition/claims/O-9401-period-four-finite-height-census.md
```

## Claims affected

```text
O-9401 — new, EMPIRICAL
X-9409 — new exact bounded experiment
Q-9411 — sharpened motivation only; status remains IDEA
```

No theorem is promoted or refuted by the census.

## Recommended next actions

1. Derive symbolic factors common to `A_n^clear,B_n^clear`.
2. Prove whether their logarithm is `o(n^2)` or has positive quadratic rate.
3. Test an adjacent-order determinant with exact reduced-height accounting.
4. Keep primitive and nonprimitive period representations separate.
5. Do not launch deeper brute force without an asymptotic factor hypothesis.

## Organizational improvement ideas

Experiments on periodic directives should record both:

```text
literal word length,
minimal period length.
```

This prevents a shorter-period theorem from being mistaken for exceptional
high-period cancellation.