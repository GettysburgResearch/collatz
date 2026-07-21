# Open questions — p-adic repetition program

**Agent:** `gpt56-complexity-01`
**Issue:** #18

## Q-9401 — Directive-to-output complexity transfer

**Status:** IDEA

For the exact stack, skeleton, or marked-rewrite grammars in issue #4 and
PR #3, bound the factor complexity of the emitted survivor code in terms of

- directive factor complexity;
- finite control-state count;
- carry-memory radius;
- number of genuinely fresh arithmetic bits injected per level.

A bound with lower slope below

```text
1/(log_64(81)-1) = 17.654847...
```

would combine with T-9402 to exclude that grammar as an ordinary M1
certificate.

## Q-9402 — Denominator cancellation and chart sharpening

**Status:** IDEA

L-9401 uses the universal denominator

```text
81^r * (81^s - 64^s).
```

Determine whether chart classes modulo `17`, balanced block counts, or exact
carry constraints force a uniform cancellation factor.  Even an exponential
saving `c^t` would raise the complexity threshold in T-9402.

## Q-9403 — Fourier-cylinder connection

**Status:** IDEA

PR #16 isolates sparse low-energy carry cylinders.  Determine whether a
low-energy prefix necessarily contains a repeated factor whose parameters
violate T-9401, or conversely whether repetition-free codes force a uniform
energy contribution.  This could connect the ordinary-integer obstruction
to the all-depth EQ frontier.

## Q-9404 — Wider collision alphabets

**Status:** IDEA

Generalize L-9402 and T-9401 to maps

```text
H_D(MB+d) = NB+d
```

with a finite digit set `D`.  The first-difference valuation then depends on
`v_2(d-d')`, while the rational approximant height depends on `N^s-M^s`.
A general theorem could compare the information-growth demand across the
entire collision-fiber ladder rather than only the `{0,1}` chart.

## Q-9405 — Near-saturation structure

**Status:** IDEA

Classify codes with repeated factors close to

```text
ell = (log_64(81)-1)t + log_64(A).
```

Near-saturation requires the cross-multiplied rational difference to be a
small multiple of `64^(t+ell)` while the denominator is near its maximum.
Such configurations may have rigid modular structure exploitable by the
conditioned `3`-adic resonance program in issue #8.
