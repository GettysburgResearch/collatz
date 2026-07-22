# T-9421 — The ordinary binary survivor section is trivial

Claim ID: `T-9421`  
Title: The only ordinary nonnegative integers in the binary `64 -> 81` survivor attractor are `0` and `1`  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `D-9401`, `T-9420`  
Scope: the full M1 ordinary-integer section of the binary survivor attractor  
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Theorem

For the binary code map

```text
Phi(epsilon)
 =(17/81)sum_(n>=0)epsilon_n(64/81)^n,
epsilon in {0,1}^N,
```

one has

```text
boxed:
Phi({0,1}^N) intersect Z_(>=0)={0,1}.                 (1)
```

Moreover:

```text
Phi(epsilon)=0 iff epsilon=000...,
Phi(epsilon)=1 iff epsilon=111... .                   (2)
```

Hence there is no nontrivial ordinary survivor code in the sense of `D-9401`.
In particular, issue #4's M1 question has a negative answer for this exact binary attractor.

## Proof

Suppose

```text
A=Phi(epsilon) in Z_(>=0).                             (3)
```

Then `A` is rational, so `T-9420` makes `epsilon` eventually periodic. For an
eventually periodic code, the geometric expression of `T-9420(2)` is one fixed
rational number. The same rational expression evaluates to `A` in `Q_2` and in
the real completion because all relevant geometric series converge in both.

In the real embedding all summands are nonnegative and

```text
0<=Phi(epsilon)
 <=(17/81)sum_(n>=0)(64/81)^n
 =(17/81)/(1-64/81)
 =1.                                                   (4)
```

Therefore the ordinary integer `A` lies in

```text
Z_(>=0) intersect [0,1]={0,1}.                        (5)
```

If `A=0`, equation (4) is a sum of nonnegative real terms equal to zero, so
every digit is zero.

If `A=1`, subtracting from the all-one geometric series gives

```text
0
 =1-Phi(epsilon)
 =(17/81)sum_(n>=0)(1-epsilon_n)(64/81)^n.             (6)
```

Again every summand is nonnegative, so every digit is one. This proves
(1)--(2). **QED**

## M1 consequence

`D-9401` defines an ordinary survivor code as a binary code whose `2`-adic value
is an ordinary nonnegative integer, with `1` declared trivial. The theorem
therefore gives

```text
boxed:
there is no nontrivial ordinary point in the binary survivor attractor.       (7)
```

Any chart-class or modulo-`17` requirement imposed downstream can only shrink
this empty nontrivial section.

This closes the exact M1 existential question for the `64 -> 81` binary
subsystem. A positive M1 witness cannot be used to construct a Collatz
counterexample because no such witness exists.

## Why the real bound is legitimate here

For a general nonperiodic rational sequence of partial sums, the real and
`2`-adic limits can differ. The proof does **not** equate those limits directly.
It first uses `T-9420` to prove eventual periodicity. Only then is the infinite
sum replaced by the finite rational expression

```text
finite prefix + periodic polynomial/(1-T^s),          (8)
```

which is the same rational element in every completion where it is defined.
This order of argument is load-bearing.

## Relationship to previous programs

- `T-9401`--`T-9402` gave strong complexity requirements conditional on a nontrivial ordinary point.
- PR #16 reformulated the same ordinary section as a critical centered rational-power orbit and appended block stabilization.
- The present theorem makes the conditional point nonexistent in the binary subsystem.
- The independently reviewed all-depth EQ theorem remains a substantive finite-set result, but it is no longer needed to exclude one ordinary binary point.

The theorem does not alter claims outside this exact attractor.

## What this does not prove

- It does not prove the Collatz conjecture.
- It does not exclude counterexamples arising outside the `64 -> 81` induced subsystem.
- It does not close PR #3's negative-cycle tower/cap-stitch architecture.
- It does not prove termination of the H subsystem.
- It does not classify algebraic nonrational points of the attractor.

## Dependency audit

- `T-9420` supplies eventual periodicity from rationality.
- The real estimate is the elementary full-geometric-series bound.
- No external theorem, computation, Fourier estimate, or Padé approximation is used.

## Gap audit

- The inference from rationality to eventual periodicity is the sole load-bearing theorem and requires independent reconstruction.
- The binary digit alphabet and positive coefficients are essential for the endpoint classification.
- The result is branch-qualified to the exact `Phi` of `D-9401`; it must not be advertised as a universal Collatz theorem.

## Adversarial tests

`X-9413` verifies the finite periodic rational formula and the endpoint codes.
A reviewer should additionally reconstruct `T-9420` without reading its proof,
especially the denominator-divisor chain and the completion-independent use of
the periodic formula.

## Suggested next attack

Integrate the negative M1 result into issue #4 and move the counterexample search
to the remaining architectures. The most promising cross-program frontier is
the exact late cap-to-correction stitch system of PR #3 / PR #33, where the
binary-attractor rationality classification does not apply.
