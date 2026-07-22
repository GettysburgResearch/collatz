# R-9304 — Constant-word counterexamples to T-9318

**Claim ID:** R-9304  
**Title:** The unrestricted low-factor-complexity nonstabilization criterion in `T-9318` is false  
**Status:** PROVED  
**Authoring agent:** `gpt56-review-9315-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** definitions of factor complexity and nearest-integer cylinder blocks  
**Scope:** `T-9318`, Section 3  
**Related counterexample candidates:** none

## Statement

The statement

> every infinite binary word `v` satisfying
> \[
> \liminf_{n\to\infty}p_v(n)/n<1/\log_{64}(81/64)
> \]
> cannot have an eventual-zero nearest-integer cylinder tail

is false as written.

The two smallest exact counterexamples are

\[
v=0^\infty,
\qquad
v=1^\infty.
\]

For either word,

\[
p_v(n)=1\quad(n\ge1),
\qquad
\liminf_{n\to\infty}\frac{p_v(n)}n=0,
\]

while its nearest-integer cylinder is already stationary and

\[
q_K=0\quad\text{for every }K.
\]

## Independent derivation

For a constant word, every length-`n` factor is the same, so `p_v(n)=1`.

In the nearest-integer recurrence

\[
64B_{K+1}=81B_K+e_K-e_{K+1},
\]

the digit difference is always zero. Taking `B_K=0` for every `K` gives the selected completion point `B_0^*=0`. Hence every least representative is zero and every appended digit is zero.

The same conclusion follows from the completion series

\[
B_0^*(e)
=-\sum_{n\ge0}(e_n-e_{n+1})64^n81^{-(n+1)}=0.
\]

Thus both constant words satisfy the antecedent of `T-9318(7)` and contradict its conclusion.

## First invalid inference

The proof of `T-9318`, Section 3, silently inserts the sentence

> “A nonconstant word cannot stabilize at zero.”

That sentence is correct, but `nonconstant` is absent from the quantified theorem statement. The missing hypothesis is therefore statement-level, not a failure of the factor-complexity lower bound for nontrivial ordinary orbits.

## Smallest repair

Add the explicit hypothesis that `v` is nonconstant. The corrected theorem is recorded separately as `T-9319`; the false `T-9318` statement and proof history are preserved.

## Downstream audit

- The lower bound for an already nontrivial ordinary itinerary in `T-9318(3)--(4)` remains correct.
- The unrestricted screening statement `T-9318(7)` must not be used.
- Source-equality applications normally concern nonconstant languages, but they must cite `T-9319` and state that condition explicitly.
- No other claim is refuted by these counterexamples.

## Computational corroboration

The independent checker verifies the exact block sequence for both constant words and scans `2,794` nonconstant periodic words through cylinder depth `4,096`. The finite scan is corroboration only; the two displayed counterexamples are exact proofs.
