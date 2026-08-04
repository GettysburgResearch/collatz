# LIT-KTHM-0036 — A deterministic one-counter machine has ultimately periodic autonomous output

**Type:** self-contained automata lemma.  
**Maps to:** the next operator-class boundary after `FOUNDRY/T-9603` and `T-9604`.

## Machine model

A deterministic one-counter output machine has:

- a finite control set `S`;
- a counter `c in N`;
- transitions depending only on the control state and on whether `c=0`;
- counter update in `{-1,0,+1}`, with no decrement below zero;
- one output letter on every transition.

Fix the input forever to one autonomous symbol, so the transition is deterministic.

## Statement

Every infinite output word of such a machine is ultimately periodic.

## Proof

Consider an infinite run.

### Case 1: the counter is zero infinitely often

There are only finitely many zero configurations `(s,0)`. Some zero configuration occurs twice. Determinism makes the entire future configuration and output sequence after the second occurrence equal to the future after the first. The run is ultimately periodic.

### Case 2: the counter is zero only finitely often

After the last zero, the positive-counter transition rule is used forever. The control state therefore evolves under one deterministic map of the finite set `S`; after a finite prefix it enters a control cycle.

Let `Delta` be the net counter change over one traversal of that cycle.

- If `Delta<0`, sufficiently many traversals return the counter to zero, contradicting the choice of the last zero.
- If `Delta=0`, the full configuration repeats after every cycle.
- If `Delta>0`, the counter drifts upward, but the control states and emitted output letters repeat with the control cycle.

The output is ultimately periodic in every case. ∎

## Foundry consequence

Suppose a strictly causal Foundry operator is implemented by this machine model and is tail-autonomous on the eventual zero input. If its unique fixed point is an ordinary nonnegative integer, its binary input is eventually zero. The resulting parity output is therefore eventually periodic.

Thus a uniformly supercritical operator in this one-counter class cannot have a positive ordinary fixed point: an ordinary Collatz orbit with eventually periodic parity is eventually periodic and cannot have a strictly supercritical tail.

## Scope boundary

The theorem does not cover:

- access to counter residues or binary digits;
- multiplication, division, or large jumps of the counter;
- two counters;
- a genuine pushdown alphabet;
- nondeterminism;
- scale-dependent transition tables.

In particular, PR #3's padding-address tape is not automatically this one-counter model.