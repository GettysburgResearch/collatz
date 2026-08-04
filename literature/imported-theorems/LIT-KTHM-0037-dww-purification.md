# LIT-KTHM-0037 — Finite-action purification on an atomless space

**Type:** external black box with an explicit nonapplication boundary.  
**Source:** Dvoretzky--Wald--Wolfowitz, through Khan--Rath--Sun (2006).  
**Maps to:** PR #34 `L-9866` fractional residue allocation.

## Theorem

Let `(X,Sigma,mu)` be an atomless finite measure space, let `A` be a finite action set, and let

```text
p_a(x)>=0,
sum_(a in A)p_a(x)=1
```

be a measurable randomized action. For a finite family of integrable payoff vectors `g_a:X->R^m`, there exists a measurable pure action

```text
rho:X->A
```

such that

```text
int_X g_(rho(x))(x) dmu(x)
 =int_X sum_a p_a(x)g_a(x)dmu(x).                     (1)
```

Thus finitely many aggregate integrals of a randomized finite-action rule can be preserved exactly by a deterministic measurable rule.

This theorem is used as a black box; its proof is not reproduced here.

## Application template for residue allocation

Suppose PR #34 `L-9866` produces a measurable kernel

```text
p_a(x)=0 for a notin D(x),
sum_a p_a(x)=1,
```

with finitely many residue-load inequalities. If the underlying decoder measure is atomless, choose payoff coordinates that record the weighted load sent to each residue. Purification gives a deterministic measurable selector

```text
rho(x) in D(x)
```

with exactly the same finite aggregate residue loads.

## What this removes

Under atomlessness, randomized-versus-deterministic selection is not a **static finite-dimensional** obstruction.

## What it does not remove

Purification supplies none of the following:

1. one residue choice coherent along an individual orbit;
2. a matching to actual positive integers;
3. temporal order or moving size thresholds;
4. compatibility at infinitely many moduli;
5. a causal or finite-state implementation;
6. a pointwise rather than aggregate capacity bound.

A successful native use must prove atomlessness and state exactly which finite integrals are preserved.