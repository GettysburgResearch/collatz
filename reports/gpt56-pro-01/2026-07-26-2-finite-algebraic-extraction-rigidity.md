# Session report — finite algebraic extraction rigidity

**Agent:** `gpt56-pro-01`  
**Issue:** #2  
**Branch:** `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
**Date:** 2026-07-26  
**Status:** theorem-level method closure; no counterexample claim

## Objective

Continue only on the ordinary-extraction blocker. The target was not another finite prefix, amplifier, or conditional growth statement, but a proof that a broad proposed class of recursive extraction mechanisms either produces a genuine smaller ordinary root or cannot exist.

The strict test system was the stationary six-branch chart

```text
P=3^12,
Q=2^19,
A={229376,258048,290304,326592,367416,413343}.
```

For this chart, bounded least roots would write a restricted ordinary survivor and therefore a counterexample candidate after physical replay; divergent least roots eliminate the whole chart.

## Repository inputs inspected

- PR #64: six-branch least-root decision, direct quotient exit, finite affine/rational nucleus rigidity, and semilinear obstruction;
- PR #61/#62: eventual-periodicity/full-denominator firewall and independent ordinary-extraction reconstruction;
- PR #49: strongest integer-first intrinsic primitive-core machine and its exact all-time routing target;
- PR #51: negative-three-cycle run-core highway and its changing-modulus quotient;
- PR #38: convergence of the portfolio onto ordinary top-boundary extraction and full-denominator cycles.

## New lemma `L-0040`

A real algebraic branch on a positive ray which takes integer values at every sufficiently large integer is a polynomial.

The proof is direct:

1. Newton--Puiseux at infinity gives polynomial growth and derivative decay;
2. a sufficiently high forward difference tends to zero;
3. that difference is an integer, hence is eventually exactly zero;
4. Newton interpolation gives a polynomial on the integer tail;
5. an algebraic branch agreeing with the polynomial at infinitely many points is the polynomial branch identically.

The same conclusion applies to eventually integral semialgebraic/Nash branches.

## New theorem `T-0044`

Allow an arbitrary finite control graph. At every state/type, allow a nonconstant algebraic section formula which:

- is defined on every sufficiently large ordinary tail;
- takes positive integer values there;
- carries all six child cylinders;
- and replays the complete six-branch law exactly, with state-dependent successor control and initially arbitrary symbol permutations.

Then every section formula is forced to be

```text
f_(omega,i)(X)=P*X+c_i,
```

with the physical symbol labels unchanged.

The proof has three independent rigidity layers:

1. `L-0040` turns every algebraic branch into a polynomial;
2. leading coefficients around a finite control cycle force polynomial degree one;
3. the six-digit alphabet has trivial affine automorphism group, and a max--min argument on the finite normalized carry set forces the only affine nucleus to be the original forward image.

Thus finite algebraic, Nash, semialgebraic, polynomial, rational, and affine complete-tree nuclei all collapse to the same expanding map. None provides a bounded or seed-preserving ordinary extraction.

## Why this is a genuine exhaustive result

The theorem eliminates the full class

```text
finite control
+ one tame algebraic section per state/type
+ tail-integral ordinary values
+ exact complete-tree self-replication
+ no unbounded top register.
```

It is not a sampled-controller result. It is all-depth and formula-independent within that class.

It is genuinely weaker than Collatz because:

- it concerns one strict six-branch subsystem;
- it concerns uniform recursion of the complete subtree;
- a survivor in a proper infinite-state sublanguage remains possible;
- unbounded quotient/stack machines remain possible.

## Blunt consequence

A positive extraction proof cannot be hiding in a more complicated finite algebraic coordinate change. Any remaining successful mechanism must use genuinely unbounded arithmetic information, a source-specific global height relation, direct digit escape, or a finite full-denominator cycle.

This removes a broad family of plausible but ultimately circular attempts to repackage the same expanding tree as a smaller copy of itself.

## What remains unresolved

The theorem does not decide the least-root sequence of the six-branch chart. It does not provide one forever-defined intrinsic refund state. It does not prove full-denominator divisibility for a positive cycle.

The load-bearing targets remain exactly:

```text
positive:
  write one explicit all-time ordinary state;

negative:
  prove least roots escape / every ordinary state exits;

finite alternative:
  cross one complete positive-cycle denominator and replay it.
```

## Files added

- `claims/lemmas/L-0040-eventually-integral-algebraic-branches.md`
- `claims/theorems/T-0044-finite-algebraic-nucleus-rigidity.md`
- this report

## Verification boundary

No numerical experiment is load-bearing. Independent review should focus on:

1. the Newton--Puiseux derivative estimate in `L-0040`;
2. eventual-zero finite differences implying an integer-valued polynomial;
3. degree/leading-coefficient transport around finite graph cycles;
4. the affine automorphism calculation for the six digits;
5. the finite normalized-carry max--min argument.
