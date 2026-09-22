# Issue #46 — single-pulse counterexample offense

**Agent:** `gpt56-pro-04`  
**Date:** 2026-07-22  
**Status:** partial exact negative result; counterexample search continues

## Objective

Move from address-first compatible cylinders to an integer-first certificate. The shortest target is a positive accelerated Collatz cycle, because a finite valuation word and one exact replay would disprove the conjecture without any inverse-limit stabilization argument.

## Structural idea

Use the known negative cycles as near-critical templates. Repeat one negative-cycle valuation block `r` times and increase one valuation by `delta`, chosen just large enough that

\[
2^{Ar+\delta}>3^{kr}.
\]

At first this appears to require scanning every pulse position. Cyclic rotation and the affine numerator formula collapse it completely.

If `z<0` is the rotated negative state, the perturbed fixed point is

\[
n=z-
\frac{(2^\delta-1)(3z+1)3^{kr-1}}
     {2^{Ar+\delta}-3^{kr}}.
\]

Therefore integrality requires

\[
2^{Ar+\delta}-3^{kr}
\mid
(2^\delta-1)(3z+1).
\]

This is `L-9601`.

## Exact computation

`X-9601` evaluates the reduced divisibility condition and then replays every hit.

```text
negative three-cycle rotations:  2 states
negative eleven-cycle rotations: 7 states
repetition counts:                1..20,000
pulse schedule:                   threshold, +1, +2, +3
reduced candidates:               720,000
nontrivial exact cycles:          0
```

The sole hit is the trivial cycle:

```text
(1,2) -> pulse first valuation -> (2,2), start 1.
```

Frozen result digest:

```text
cb97c4b0fcc5e2557b3e22ce83483d9e86f8ed4d825032925c90c4e0f6ee2ae8
```

## Collaborator handoffs

- Issue #9 received the exact scope and digest so the compressed-cycle agent can treat the single-pulse family as closed and reuse the reduction.
- Issue #39 received the exact observation that phase `1` with `q=n+1` is an invariant copy of the original shortcut map. A permanent phase-1 tail is not a new amplifier.

## Next offense

The negative result localizes the next cycle search to distributed pulses. The intended exact object is the upper-triangular affine monoid

\[
M_a=
\begin{pmatrix}
3&1\\
0&2^a
\end{pmatrix},
\]

whose products encode both the cycle numerator and total dyadic exponent. A meet-in-the-middle search can combine several pulse locations while retaining a tiny exact replay certificate.

No positive integer counterexample, nontrivial cycle, or divergent ordinary orbit is claimed in this report.
