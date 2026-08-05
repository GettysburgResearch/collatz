# R-8301 — The reported small ladder quotient is outside every first paired-chart cylinder

**Claim ID:** `R-8301`  
**Status:** `PROPOSED / EXACT REFUTATION`  
**Authoring agent:** `gpt56-cycle-02`  
**Created:** 2026-07-23  
**Dependencies:** `T-8302`  
**Scope:** the small quotient used in the reported recursive Hensel-ladder summary

Write

```text
N_ladder=110,340,992,901,879.
```

This is distinct from the much larger rotated floor denoted `N_*` in `O-8303`.

**Related counterexample candidates:** none; this claim withdraws `N_ladder` as a possible chart-cycle target

## Statement

No finite paired-chart word can have fixed point `N_ladder`. In particular, no amount of lifting at the five known odd denominator factors can force

\[
 C=N_{\rm ladder}D
\]

for a genuine word in the two-branch chart of `T-8302`.

## Proof

The two exact first-branch domains are

\[
 e_0=0:\quad x\equiv0\pmod {16},
\]

and

\[
 e_0=1:\quad x\equiv5\pmod8,
\]

which, modulo `16`, is the union

\[
 \boxed{\{0,5,13\}\pmod {16}.}
\tag{1}
\]

But

\[
 \boxed{N_{\rm ladder}\equiv7\pmod {16}.}
\tag{2}
\]

Thus `N_ladder` lies in neither first branch domain.

If a finite chart word satisfied `C=N_ladder D`, then `T-8302` would identify `N_ladder=C/D` as its positive periodic chart state and would replay the first advertised branch exactly. Equations (1)--(2) make that impossible. **QED**

## Stronger interpretation

The obstruction is independent of:

- the later chart symbols;
- the mechanical-word layout;
- the chosen proper denominator factors;
- the number of odd-prime Hensel levels;
- and the real height estimate.

It is a first-block physical obstruction. Odd-prime quotient matching can coexist with this failure because the known factor product is odd and therefore contains no information about the mandatory dyadic branch cylinder.

## Exact physical corroboration

The physical odd state associated with the proposed chart quotient would be

\[
 n_{\rm ladder}=2N_{\rm ladder}+1=220\,681\,985\,803\,759.
\]

`X-8307` directly replays the shortcut map and obtains

```text
shortcut steps to 1: 208
odd shortcut steps:   101
maximum state:        1,885,279,308,409,466
```

The finite trajectory calculation is not needed for the modular proof, but it supplies an independent adversarial check.

## Consequence for the earlier lifting summary

The reported congruences

\[
 C-N_{\rm ladder}D\equiv0\pmod {M^j}
\]

at several odd-prime levels, even if reconstructed exactly, cannot converge to equality inside this chart. They were proper-place congruences for changing finite words, not a candidate counterexample chain.

Any continuation must first replace `N_ladder` by a quotient in one of the legal classes (1) and carry the complete dyadic physical-prefix obligation alongside the odd-prime lift.

## Gap audit

- This refutes one quotient target, not the paired-chart architecture.
- It does not exclude another chart-compatible integer or an infinite chart path.
- It does not make any inference from the finite orbit beyond the exact displayed seed.
- It does not refute the valid proper-factor identities already committed in `X-8302`.

## Suggested next attack

Use `L-8310` from the beginning of the search. The solver state must include the current dyadic chart cylinder. Reject a real integer target immediately unless its residue belongs to the selected first branch and every subsequently frozen branch replays exactly.