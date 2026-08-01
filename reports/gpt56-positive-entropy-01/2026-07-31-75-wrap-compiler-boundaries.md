# Session addendum — exact wrap compiler and two boundary-departure theorems

**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**PR:** #81  
**Date:** 2026-07-31

## Purpose

After closing the upper-mechanical and no-wrap sectors, this addendum freezes
the exact remaining acyclic first-crossing object rather than adding another
bounded scan.

## 1. Lossless near-cycle compiler

`L-6809` transports PR #34's prime-power excess-path method from the cycle
equation

```text
D | A
```

to the first-crossing near-cycle equation

```text
D | A-2^j Delta,
0 <= Delta < j/2.
```

For

```text
D=2^j-3^q=product_s Q_s,
h_s=ord_(Q_s)(2),
```

one exact ordinary first-crossing near-return is equivalent to:

```text
- generalized CRT compatibility of all local excess coordinates;
- the unique monotone physical path in the source-qualified full-order window;
- explicit first-crossing inequalities at every proper prefix;
- one common ordinary Delta;
- all complete prime-power shifted-numerator congruences;
- the canonical positive source range.
```

A source tuple omitting any of these gates is not a certificate.

### Adversarial correction

The first draft recognized a monotone parity word but did not separately
require the coefficient-first-crossing prefix barrier.  This was caught in the
same session and repaired before integration.  The current theorem explicitly
requires

```text
3^(prefix ones) >= 2^(prefix length)
```

at every proper prefix.

## 2. Logarithmic departure from the extremizer

`T-6809` studies the initial common prefix `ell` between a target-failure word
and the upper-mechanical extremizer.

The shared prefix itself has bank below one and Sturmian factor complexity.
Its canonical root therefore has an exponential lower bound, while the full
no-descent word has the harmonic/Baker polynomial upper bound.

Exact candidate-dependent gate:

\[
\frac{2^{\lfloor(\ell-1)/3\rfloor}+1}{3}
-\frac\ell2
<
\frac{1}{2^{j/q}-3}.
\]

Source-qualified asymptotic conclusion:

\[
\limsup\frac{\ell}{\log_2j}\le42.9.
\]

Thus every unbounded acyclic obstruction leaves the maximum-remainder path
within logarithmic depth.

## 3. Logarithmic self-departure after the near-return

`L-6810` compares the parity tails from the canonical source `r` and its
near-return endpoint `r+Delta`.

If they agree for `u` steps, exact dyadic factor separation gives

```text
2^u | Delta.
```

Therefore

```text
Delta>0 -> u <= v_2(Delta) < log_2(j/2).
```

At the end of the common factor, the two physical states differ exactly by

\[
3^s\frac{\Delta}{2^u}.
\]

The equality case `Delta=0` is precisely a positive cycle.

## 4. Combined residual object

Every unbounded acyclic first-crossing obstruction must now be:

```text
nonmechanical;
a genuine dyadic wrap;
departing from mechanical within O(log j) bits;
departing from its own old parity tail within <log_2(j/2) bits after return;
Omega(j^(2/3)) in integrated mechanical displacement;
Omega(j^(1/3)) in displaced odd support;
accepted by one of fewer than j/2 full-denominator levels;
and compatible at every complete prime-power factor with one common Delta.
```

This is the exact object frozen in the revised `Q-6802` as `(FC*)`.

## 5. Box 1 boundary

No source-coordinate theorem was found in this pass.  PR #80's stronger
ordinary product/packing estimates deepen the necessary high-surplus profile,
but the canonical source may still remain one fixed integer in all those
statements.

The exact unresolved target remains

```text
min_{w in W_N^sup} r_w -> infinity.
```

## 6. Honest status

The addendum proves no full-denominator avoidance, no absence of positive
cycles, no Box-1 source escape, and no proof of Collatz.

It narrows the remaining finite-crossing language and supplies a lossless
factorwise certificate interface on which a future negative or positive result
would be immediately decisive.
