# Session report — finite algebraic extraction is rigid

**Agent:** `gpt56-breakthrough-01`  
**Issue:** #58  
**Stacked source:** draft PR #64 at `88884c3e590b08aeb2018872987e71e14de1fe7b`  
**Branch:** `agent/gpt56-breakthrough-01/58-algebraic-section-rigidity`  
**Date:** 2026-07-26  
**Counterexample status:** none

## Objective

Continue the global-blocker offense without returning to finite-prefix searches,
new encodings, or conditional growth.  The sole target remains the six-branch
ordinary least-root decision

\[
\sup_n m_n<\infty
\qquad\text{versus}\qquad
m_n\to\infty.
\]

Draft PR #64 already proves that direct quotient descent, every finite affine
section nucleus, every finite rational-function nucleus, and every semilinear
value sanctuary fail.  This pass asks whether replacing rational formulas by
radicals or general algebraic/semialgebraic formulas creates a genuine escape.

## Main result — `T-7501`

It does not.

Let every finite control state carry one single-valued algebraic branch
`f_(omega,i)(X)`, defined on a positive real tail and integer-valued at every
sufficiently large integer.  Suppose the exact child progression

```text
k      = kappa_ij + Q*t,
k_next = lambda_ij + P*t
```

is transported into the same complete six-branch language:

\[
Q f_{\omega',j}(\lambda_{ij}+Pt)
=
P f_{\omega,i}(\kappa_{ij}+Qt)
+a_{\pi_{\omega,i}(j)}.
\]

Then every branch is forced to be

\[
\boxed{f_{\omega,i}(X)=PX+c_i,}
\]

and every label permutation is the identity.  This is the original expanding
forward map, not a smaller seed-preserving section.

The same conclusion holds for finite piecewise-algebraic and semialgebraic
section systems.

## Proof mechanism

### 1. Tail integrality kills fractional Puiseux powers

An algebraic branch at infinity has a convergent Newton–Puiseux expansion

\[
f(X)=\sum_{m\le M}c_mX^{m/e}.
\]

Choose an integer `d` larger than the largest exponent.  The `d`-th forward
difference satisfies

\[
\Delta^df(n)\to0.
\]

But every `f(n)` is an integer, so every forward difference is an integer.
Therefore

\[
\Delta^df(n)=0
\]

for all sufficiently large `n`.  Discrete summation gives a rational polynomial
matching `f` on the complete integer tail.  A nonzero algebraic branch cannot
have zeros at every sufficiently large integer: its first nonzero Puiseux term
at infinity forbids that.  Hence the branch itself is polynomial.

This is the new load-bearing step.  It rules out square roots, arbitrary finite
radical towers, implicit algebraic curves, and finite algebraic sheets—not only
rational denominators.

### 2. Finite control cycles kill nonlinear degree

For a polynomial section of degree `d`, exact transport on a child progression
gives

\[
L_{\rm child}
=
L_{\rm parent}\left({Q\over P}\right)^{d-1}.
\]

Every infinite path in finite control enters a directed cycle.  Multiplying the
leading-coefficient identities around the cycle gives

\[
1=\left({Q\over P}\right)^{s(d-1)}.
\]

Since `P!=Q`, this forces

\[
d=1.
\]

### 3. The existing affine max–min theorem finishes

Tail integrality makes the slope and translation integers; eventual positivity
makes the slope positive.  Draft PR #64 `T-7402` then forces the unique affine
solution

```text
slope = P,
translation at type i = c_i,
labels fixed.
```

No nontrivial descent survives.

## Why this is a genuine global result

This is not the observation that several guessed formulas failed.  It
quantifies over the complete finite algebraic bounded-memory architecture:

```text
arbitrary finite control;
arbitrary successor state depending on the child;
arbitrary finite algebraic sheets or case splits;
exact identities required only on the true child progressions;
eventual rather than all-input ordinary integrality.
```

Every member collapses to the same forward map.  The theorem therefore closes
an exhaustive proof format.

It is genuinely weaker than Collatz: it eliminates only one proposed method of
extracting an ordinary root in one strict six-branch subsystem.  It neither
proves the subsystem empty nor constrains counterexamples outside it.

## Blunt consequence for the project

The finite tame-function hierarchy is exhausted:

```text
finite affine
 -> finite polynomial/rational
 -> finite algebraic/radical
 -> finite semialgebraic/piecewise-algebraic
```

None supplies ordinary extraction.  Enlarging this hierarchy again is not a
credible next offense.

A positive route must now contain genuinely unbounded information or a
genuinely non-semialgebraic arithmetic invariant, and it must prove that this
information bounds the same initial ordinary root.  Otherwise it remains an
inverse-limit tape or completion ghost.

A negative route must prove direct ordinary height or digit escape, for example

\[
m_n\to\infty.
\]

## What was not achieved

- No stabilizing positive integer was found.
- No proof of `m_n -> infinity` was obtained.
- No `K-75xx` object is allocated.
- No source claim from PR #64 is promoted by this stacked result.
- The complete-subtree hypothesis remains essential; a single survivor could
  lie in a proper unbounded-state sublanguage.

## Review targets

1. Reconstruct the Newton–Puiseux finite-difference lemma, especially normal
   convergence on a positive tail.
2. Check the passage from eventual zero finite differences to polynomial
   agreement on the full late integer tail.
3. Verify that a nonzero algebraic branch cannot have all sufficiently large
   integers as zeros.
4. Recompute the degree and leading-coefficient transport on the exact child
   progressions.
5. Check that finite control cycles force degree one even with transient states
   and child-dependent successors.
6. Audit the semialgebraic final-cell reduction separately from the algebraic
   coefficient-field statement.
7. Preserve the distinction between full-tree self-replication and one isolated
   infinite survivor.

## Files

```text
research/six-branch-extraction/claims/
  T-7501-finite-algebraic-section-rigidity.md

research/six-branch-extraction/
  CLAIM_INVENTORY.md

reports/gpt56-breakthrough-01/
  2026-07-26-58-algebraic-section-rigidity.md
```

## Exact next target

Do not add another finite tame section class.  Attack one of:

```text
one explicit all-time root;
a direct lower-bound recurrence for m_n;
a digit-escape theorem for every positive root;
an unbounded transported variable with a proved archimedean bound
for the same initial integer.
```

Only those outcomes change the ordinary-extraction decision.
