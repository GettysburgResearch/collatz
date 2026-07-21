Claim ID: L-9201  
Title: Cofinite-tail obstruction to naive finite-safety SCC widening  
Status: PROPOSED  
Authoring agent: gpt56-sol-01  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9201  
Scope: every finite-horizon shortcut safety language `S_d`  
Related counterexample candidates: none

## Statement

For every `d >= 0`:

1. `F_d` is finite and

   $$
   \max F_d=2^{d+1}.
   $$

   Hence `S_d` is cofinite.

2. The minimal complete binary DFA for the canonical LSD-first encodings of
   `S_d` has exactly one cyclic strongly connected component. It is the
   terminal two-state canonical tail from `D-9201`. Removing it leaves a
   directed acyclic graph.

3. `S_d` is not forward invariant. An exact one-step witness is

   $$
   2^{d+2}\in S_d,\qquad
   T(2^{d+2})=2^{d+1}\notin S_d.
   $$

4. More generally, no cofinite set of positive integers can both exclude
   `{1,2}` and be forward invariant under `T`.

Consequently, SCC learning that retains the canonical tail acceptance of a
finite `S_d` cannot produce a Collatz sanctuary. A viable widening must add a
non-cofinite guard. The sink-stripped boundary DAG is finite-horizon data to
compare across depths; it is not itself a recurrent candidate.

## Definitions

All notation is from `D-9201`. A strongly connected component is called
cyclic if it has at least two states or contains a self-loop.

The claim concerns the minimal DFA language on all finite raw binary words,
with nonempty final-`1` canonicality built into acceptance.

## Motivation

Issue #8's safety-automata path proposes learning candidate inductive
quotients from minimized finite approximants. Raw SCCs appear attractive
because an infinite accepted language needs recurrent input structure.
However, finite avoidance makes every `S_d` cofinite, so it necessarily
contains a universal recurrent tail unrelated to infinite Collatz survival.
This lemma identifies and removes that false signal before synthesis.

## Proof or construction

### 1. Finiteness and maximum

The positive preimages of `y` under `T` are:

$$
2y
$$

always, and

$$
\frac{2y-1}{3}
$$

exactly when `y = 2 mod 3`. The latter, when present, is a positive odd
integer and is strictly smaller than `2y`.

Starting from the finite set `{1,2}`, taking preimages a finite number of
times therefore produces a finite set. This proves finiteness of `F_d`.

At depth zero the maximum is `2`. If the maximum through depth `d` is
`2^(d+1)`, every new preimage is at most twice its target and hence at most
`2^(d+2)`. The even preimage chain contains `2^(d+2)`, so equality holds at
the next depth. Induction proves

$$
\max F_d=2^{d+1}.
$$

Thus every integer greater than `2^(d+1)` belongs to `S_d`.

### 2. Minimal-DFA tail and acyclic boundary

The set of canonical forbidden words encoding `F_d` is finite. Let `h` be
their maximum length. After reading any raw prefix `p` of length greater than
`h`, no forbidden word can extend `p`.

If a further suffix `x` is nonempty, canonicality of `px` depends only on
whether `x` ends in `1`. If `x` is empty, acceptance depends only on whether
`p` itself ends in `1`. Therefore every prefix longer than `h` has one of
exactly two left quotients:

- `R_0`, when `p` ends in `0`, which rejects the empty continuation;
- `R_1`, when `p` ends in `1`, which accepts the empty continuation.

The quotients are distinct because they disagree on the empty continuation.
From either quotient, reading `0` reaches `R_0` and reading `1` reaches
`R_1`. They therefore form a terminal two-state strongly connected component
in the minimal DFA.

Suppose a state outside this component belonged to a directed cycle. Choose a
word reaching the state and a nonempty word labeling the cycle. Repeating the
cycle word would produce arbitrarily long prefixes whose residual state
remained outside `{R_0,R_1}`. Once the prefix length exceeded `h`, the
preceding paragraph says its residual must be `R_0` or `R_1`, a contradiction.
Hence every other component is acyclic, and the canonical tail is the unique
cyclic component.

### 3. Exact nonclosure witness

For `0 <= j <= d`,

$$
T^j(2^{d+2})=2^{d+2-j}\ge4.
$$

Thus `2^(d+2)` belongs to `S_d`. Its one-step image is `2^(d+1)`, and

$$
T^d(2^{d+1})=2,
$$

so the image does not belong to `S_d`.

### 4. No cofinite sanctuary

Let `L` be cofinite. Choose `k` large enough that `2^k` belongs to `L`. If
`T(L)` were contained in `L`, repeated closure would put

$$
2^{k-1},2^{k-2},\ldots,2,1
$$

in `L`. Therefore a cofinite forward-invariant set cannot exclude `{1,2}`.

This also shows why preserving the finite approximant's accepting tail cannot
be a successful widening.

## Dependency audit

- `D-9201` supplies only notation.
- The preimage formula and every automata argument are proved above.
- No theorem or implementation from draft PR #12 is used.

## Gap audit

- The proof does not say that all regular sanctuaries are impossible; a
  sanctuary, if one exists, must be non-cofinite.
- Acyclicity is asserted only after stripping the canonical tail from each
  fixed finite approximant. Inter-depth maps between different boundary DAGs
  may still contain useful recurring structure.
- The finite reverse trees are not extrapolated to their infinite union.
- The result does not imply Collatz convergence.

## Adversarial tests

`experiments/X-9201-sink-stripped-safety/test_run.py`:

- compares direct iteration with exact reverse-tree membership;
- compares both with independently constructed minimal DFAs;
- checks the unique cyclic component through depth 20;
- checks the power-of-two nonclosure witness at every tested depth;
- independently reproduces draft PR #12's state counts through depth 20.

## Remaining uncertainty

The proof is complete-looking but has not been independently reconstructed.
In particular, a reviewer should check that the residual-language argument
correctly handles the empty continuation and noncanonical raw words.

## Suggested next attack

Define state-label-independent embeddings between the boundary DAGs at depths
`d` and `d+1`. Mine recurring *inter-depth* motifs, not within-depth SCCs.
Any inferred guard should then be composed with a fresh recurrent core and
submitted immediately to an exact one-step closure verifier.
