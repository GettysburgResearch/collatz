# Session report — critical symmetric `Z_(5/4)` equivalence

Agent: `gpt56-drift-01`  
Issue: #26  
Branch: `agent/gpt56-drift-01/26-5x1-portability`  
Date: 2026-07-22

## Starting hypothesis

The base-`5/4` forbidden-digit frontier might admit a sharper analytic
reformulation than the broad rational-base normality conjecture. In particular,
its two extreme residue classes suggested a critical nearest-integer condition.

## Approach

1. Started from the general `p=q+1`, `S={0,q-1}` approximate-multiplication
   map singled out by Dubickas--Mossinghoff.
2. Encoded its two branches by digits `d_n in {0,1}`.
3. Constructed a convergent real parameter from an infinite integer orbit.
4. Identified the exact two outer fractional-part intervals.
5. Proved the converse by taking integer parts of `q*xi*(p/q)^n`.
6. Audited the strict boundary cases, which correspond only to zero or negative
   constant-tail states.

## New result

`T-8810` proves, for every `q>=2` and `p=q+1`, that a positive infinite orbit of

```text
x -> ceil(p*x/q)
```

restricted to residues `{0,q-1}` exists if and only if there is `xi>0` with

```text
||xi*(p/q)^n|| < 1/p
```

for every `n>=0`.

For the PR #35 chart this becomes

```text
||xi*(5/4)^n|| < 1/5   for all n>=0.
```

The threshold `1/5` is exact: the permissible residues correspond precisely to
fractional parts in `[0,1/5)` and `(4/5,1)`.

## What this completes

The same global existence question now has four proved equivalent forms:

1. a divergent positive orbit trapped in the exact `5x+1` chart;
2. an all-`{0,1}` base-`5/4` bottom word from a nonempty ordinary seed;
3. nontermination of the `p=5,q=4,S={0,3}` approximate-multiplication map;
4. a critical symmetric nearest-integer orbit below `1/5`.

This is a conceptual completion of the reduction. It also gives a precise test
for external range theorems: a strict universal lower bound above `1/5` would
settle the chart negatively, while a bound merely equal to `1/5` requires an
equality-classification argument.

## Candidate counterexamples

None. No parameter `xi` satisfying the infinite condition is constructed.

## Failed shortcut

Known broad distribution and range statements cannot be cited from their
abstracts as exceeding the exact `1/5` threshold. The 2009 source explicitly
marks the two-residue `p=q+1` family as a target beyond its singleton theorem.
No external theorem was promoted without checking the constant and strictness.

## Files changed

```text
research/drift-isolation/claims/T-8810-critical-nearest-integer-equivalence.md
reports/gpt56-drift-01/2026-07-22-26-critical-symmetric-z-equivalence.md
```

## Claims affected

New: `T-8810`.

## Potential errors / review targets

1. Verify the real parameter construction and tail identity.
2. Check that the constant-one and constant-zero tails are the only equality
   cases and that they force nonpositive states.
3. Reconstruct the converse independently, including the floor calculations in
   both outer intervals.
4. Keep the symmetric condition distinct from the standard one-sided
   `Z_(p/q)` definition.

## Recommended next action

Compute or locate the sharp Dubickas nearest-integer constant for `p=5,q=4`
and compare it with `1/5`, including equality cases rather than decimals alone.
