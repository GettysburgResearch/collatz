# R-8801 — Phase-only connector regeneration

Claim ID: R-8801  
Title: Two-phase switch scheduling cannot create additional asymptotic connector gain  
Status: REFUTED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-8805  
Scope: connector schemes whose complete state is only the phase label `-2` or `-1`  
Related counterexample candidates: issue #26; no `K-####` candidate

## Refuted proposal

A proposed first connector attack was:

> Choose variable-length transitions between phases `-2` and `-1` so that
> favorable switches contribute a persistent excess of odd steps, thereby
> replenishing more expansion or precision than a stationary `4 -> 5` block.

This proposal is false at the phase-only level.

## Refutation

T-8805 proves that every length-`L` connector from `d_0` to `d_L` has

```text
2s-L = chi(d_0)-chi(d_L).
```

The apparent surplus of a `-1 -> -2` connector is exactly the boundary term
needed to compensate the deficit of the reverse switch. In any concatenation,
all internal phase terms telescope. In every closed phase circuit,

```text
s=L/2.
```

Therefore connector segmentation or phase-switch scheduling cannot improve the
asymptotic odd-step density beyond the fixed alternating baseline.

## What is not refuted

- The baseline `5/4` expansion over two shortcut steps is real.
- A connector automaton with quotient, carry, or deeper residue state may still
  succeed.
- Connectors may leave `{-2,-1}`, visit additional signed phases, and return.
- A non-phase invariant could encode genuine precision replenishment.
- The existence of a positive infinite `5x+1` chart survivor remains open.

## Dependency audit

Only T-8805 is used.

## Gap audit

The scope restriction is essential. This refutation must not be cited as a
no-go theorem for all finite-state connector constructions.

## Adversarial tests

X-8802 exhausts the complete two-phase connector skeleton through length `20`;
the proof in T-8805 covers all lengths.

## Remaining uncertainty

Whether a finite residue refinement of the rational-base bottom orbit can avoid
digits `2,3` forever.

## Suggested next attack

Abandon phase scheduling as the primary state. Use the exact node `X=A+1` in
T-8806, or a rigorously sufficient quotient of it, and search for either an
inductive low-digit sanctuary or an eventual-escape ranking function.
