# Q-8802 — Critical symmetric `Z_(5/4)` parameter

Claim ID: Q-8802  
Title: Does a critical symmetric nearest-integer parameter exist at base `5/4`?  
Status: IDEA / OPEN  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-8810  
Scope: real powers of `5/4` and the exact two-residue approximate-multiplication map  
Related counterexample candidates: issue #26; no `K-####` candidate

## Question

Does there exist a real number `xi>0` such that

```text
||xi*(5/4)^n|| < 1/5
```

for every integer `n>=0`?

Here `||x||` is distance to the nearest integer.

## Exact significance

`T-8810` proves constructively that this is equivalent to the existence of a
positive infinite orbit of

```text
x -> ceil(5x/4)
```

restricted to residues `{0,3} modulo 4`, and hence to a strictly increasing
positive orbit trapped in the exact two-branch `5x+1` chart.

Thus:

- a parameter `xi` satisfying the strict inequality produces an unconditional
  divergent positive `5x+1` orbit;
- proving that every `xi>0` reaches distance at least `1/5` closes the chart
  negatively.

## Boundary discipline

- The inequality is strict.
- This is a symmetric nearest-integer condition, not the standard one-sided
  `Z_(p/q)` condition.
- A theorem with lower bound exactly `1/5` requires classification of equality
  cases.
- A solution for `5x+1` is a control-universe result and does not by itself give
  a `3x+1` counterexample.

## Equivalent repository formulations

By `T-8806`, `O-8802`, and `T-8810`, the question is equivalent to:

```text
some X>=2 has only bottom digits 0,1 forever;
some positive root survives every finite frontier;
the least roots m_n eventually stabilize.
```

## Suggested next attack

Either specialize a sharp rational-power nearest-integer theorem at the exact
constant `1/5`, or construct `xi` from a nested sequence of ordinary survivor
cylinders whose representatives stabilize rather than merely converge
`2`-adically.
