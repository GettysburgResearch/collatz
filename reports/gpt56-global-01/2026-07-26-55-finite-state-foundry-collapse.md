# Global-blocker continuation: finite-state foundries collapse to cycles

**Agent:** `gpt56-global-01`  
**Date:** 2026-07-26  
**Issue:** #55  
**Draft PR:** #57  
**New claim:** `R-7602`  
**Counterexample status:** none

## Objective

Continue the ordinary-extraction attack without adding another finite-prefix search, amplifier, prescribed controller, or conditional growth statement.

The preceding result `R-7601` proved that unrestricted strictly causal foundries are surjective onto all `2`-adic points and therefore do not reduce ordinary extraction.  The remaining natural question was whether a genuinely restricted, finite-state foundry could still produce a divergent ordinary point.

## Theorem

Let a finite-state Mealy controller read the binary digits of its own foundry point least-significant-first, outputting the requested Collatz parity bit before reading the current digit.  Strict causality gives one unique `2`-adic foundry point.

If that point is a nonnegative ordinary integer, then its input digits are eventually zero.  The controller's state thereafter follows repeated application of one map on a finite set, hence is eventually periodic.  Its parity output is therefore eventually periodic.

The actual Collatz parity vector equals that output.  If the eventual parity block is `w`, then the orbit state at the beginning of the tail and its image under one full block have the same infinite parity word.  Uniqueness of the `2`-adic realization gives equality of the two states.  Thus the ordinary orbit has entered a finite positive cycle.

Consequently:

```text
finite-state foundry + ordinary nonnegative point
    -> eventual Collatz cycle;

finite-state foundry
    !=> divergent ordinary orbit.
```

If every output of the controller is supercritical in lower one-density, then no positive ordinary point exists.  A supercritical periodic block has affine fixed point

```text
B_w/(2^L-3^a) < 0.
```

## Generalization

The same proof applies to every **zero-tail-tame** strictly causal operator: one whose output on `u 0^infinity` is eventually periodic for every finite input prefix `u`.

Finite state is only the simplest sufficient hypothesis.

## Strategic meaning

The Diagonal Foundry proposal's intended positive mode was a uniformly supercritical feedback operator whose unique point happens to be a positive integer.  `R-7602` proves that no time-homogeneous finite-state implementation can achieve this.

A viable divergent foundry must retain genuinely unbounded state even after an ordinary input has exhausted all of its nonzero binary digits.  This points toward the exact unbounded quotient/carry machines already isolated in the refund and rational-base branches, while leaving their ordinary-extraction problem completely open.

The result is genuinely weaker than Collatz: it excludes a strict controller class.  It does not exclude nontrivial positive cycles, unbounded-state foundries, or arbitrary ordinary counterexamples.

## Files

1. `research/ordinary-extraction/claims/R-7602-finite-state-foundry-cycle-collapse.md`
2. updated `research/ordinary-extraction/README.md`
3. this append-only report

## Review targets

1. Verify that the finite-state output convention is strictly causal.
2. Verify eventual periodicity after the ordinary input becomes all zero.
3. Reconstruct the implication from periodic parity tail to an actual cycle using parity-vector uniqueness.
4. Check the sign of the supercritical affine fixed point.
5. Preserve the distinction between divergent-orbit exclusion and positive-cycle search.
