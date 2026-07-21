# KTHM-0010 — Tao's almost-bounded-orbit theorem

**Source:** Tao, Theorem 1.3 in the published paper. [@Tao2022]  
**Proof status:** black-box import; proof not reproduced  
**Maps to:** modern almost-all context for both branches

## Statement

Let `Col_min(N)` be the minimum value attained by the Collatz orbit of `N`. For every function `f:N→R` with `f(N)→∞`,

\[
Col_{\min}(N)<f(N)
\]

for almost all positive integers `N` in the sense of logarithmic density.

## What this says

The exceptional set of starting values whose orbit never drops below an arbitrarily slowly growing threshold has logarithmic density zero.

## What this does not say

- It does not prove convergence for every starting value.
- It does not rule out an individual divergent orbit or nontrivial cycle.
- It does not show that a repository survivor set is empty.
- It does not promote any finite computation or `2`-adic construction to an ordinary-integer theorem.
