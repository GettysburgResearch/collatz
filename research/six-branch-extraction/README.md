# Six-branch ordinary-extraction packet

**Agent:** `gpt56-extraction-01`  
**Issue:** #58  
**Namespace:** `74xx`  
**Status:** all theorem-level claims are `PROPOSED`

## Purpose

This packet deliberately stops developing amplifiers, bounded exclusions, new symbolic encodings, and conditional growth theorems. It attacks the repository-wide missing inference:

```text
compatible positive roots at every finite depth
  ?=>
one fixed positive ordinary root at every depth.
```

The answer is not ordinary compactness. Nested residue classes are compact in a `2`-adic completion, but the ordinary positive integers are not compact. The exact additional obligation is a uniform archimedean bound on the same nested representatives.

## Frozen target

The stationary six-branch chart is

\[
P=3^{12},
\qquad
Q=2^{19},
\]

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\},
\]

\[
x_{n+1}=\left\lceil{Px_n\over Q}\right\rceil,
\qquad
\delta_n=Qx_{n+1}-Px_n.
\]

A positive chart path is exactly a positive root with

\[
\delta_n\in\mathcal A
\qquad\text{for every }n.
\]

Let `m_n` be the least positive root legal through depth `n`. The exhaustive decision is

\[
\boxed{(m_n)\text{ stabilizes}}
\]

or

\[
\boxed{m_n\to\infty.}
\]

A stable value is one explicit restricted root and enters `K`-candidate review after branch-qualified physical replay. Divergence eliminates the complete fixed architecture.

## What is genuinely weaker than Collatz

The positive outcome is not a weaker positive theorem. It is already a counterexample construction inside a restrictive chart.

The negative outcome is genuinely weaker:

```text
m_n -> infinity
  => no ordinary survivor in this six-branch chart,
```

while saying nothing about other possible Collatz counterexamples.

## Result 1 — direct quotient extraction fails

Every two-step legal root has the form

\[
x=r_i+Qk,
\]

but `L-7401` proves that the canonical first digit of the high quotient `k` is outside `A` for all 36 ordered transition pairs. Thus

\[
\boxed{x\in S_2\implies\lfloor x/Q\rfloor\notin S_1.}
\]

The simplest recursive root descent fails universally, not just on sampled words.

## Result 2 — the six-state affine self-section is rigid

`T-7401` allows an arbitrary positive scale, six state-dependent integer translations, and a separate permutation of the six outgoing symbols at each state.

If this affine high-quotient coordinate is required to reproduce the six-branch chart for every finite transition, the theorem forces

\[
\boxed{v=P,\qquad s_i=c_i,}
\]

and fixes every symbol. The transformed coordinate is exactly

\[
y=Pk+c_i=F(x),
\]

namely the original expanding forward map.

## Result 3 — no finite affine nucleus can repair it

`T-7402` permits an arbitrary finite control graph, state-dependent affine coordinates, and successor control depending on the chosen next type.

Coefficient comparison first forces one common scale. After the digit alphabet is normalized, the remaining section carries would have to form a finite nonempty integer set closed under all six maps

\[
T_i(h)={Ph-ma_i\over Q}.
\]

A max–min argument excludes `m>0` and `m<0`; for `m=0`, expansion by `P/Q>1` forces the carry set to be `{0}`. Therefore every finite affine nucleus again collapses to

\[
y=F(x).
\]

There is no contracting, bounded, or seed-preserving affine self-replicating subtree at any finite-control size.

## Result 4 — rational and polynomial sections also collapse

`T-7403` allows each finite section state to carry an arbitrary nonconstant rational function of the exact ordinary high quotient.

A rational function that is integer-valued on every sufficiently large ordinary tail must first be a polynomial: a nonconstant denominator would divide one fixed Bezout resultant at infinitely many growing integer arguments.

The exact child-cylinder identity then gives the leading-coefficient transport

\[
L_{\rm child}
=
L_{\rm parent}
\left({Q\over P}\right)^{d-1}.
\]

A directed cycle in the finite nucleus forces `d=1`. Tail integrality makes the linear coefficients integers, reducing the machine to `T-7402`. Hence every finite rational-function nucleus is again

\[
\boxed{y=F(x).}
\]

Nonlinear polynomial and rational recodings do not provide ordinary extraction.

## Result 5 — no semilinear value sanctuary

`T-7404` proves that `S_infinity` contains no infinite arithmetic progression.

At depth `n`, the legal set occupies at most `6^n` residue classes modulo

\[
Q^n=2^{19n}.
\]

An arithmetic progression with step `M`, where `v=nu_2(M)`, occupies exactly

\[
2^{19n-\min(v,19n)}
\]

classes modulo `Q^n`. For large `n`, this exceeds `6^n` because `2^19>6`.

Therefore the complete survivor set contains no infinite semilinear subset. Since `F(x)>x` for every positive `x`, it contains no nonempty semilinear/Presburger forward-invariant sanctuary.

This closes another exhaustive finite-description certificate class without claiming the survivor set is empty.

## Global assessment

The repository has made genuine progress where it quantifies an entire strict class:

- the frozen corrected phase-34 class is excluded;
- several cycle and pulse families are eliminated;
- false completion/stack/PDR bridges are explicitly refuted;
- exact physical machines and acceptance gates are now available.

The positive infinite-orbit branches still stop at ordinary extraction. Their increasingly strong growth, refund, fresh-prime, stack-capacity, and routing theorems do not imply a finite root.

The explicit supercritical ghost constructions in PR #56 / PR #57 prove that finite compatibility plus arbitrary conditional expansion cannot supply the missing inference.

The present packet now additionally rules out:

```text
direct quotient descent;
finite affine section nuclei;
finite polynomial/rational section nuclei;
semilinear value-space sanctuaries.
```

## Files

1. `claims/D-7401-six-branch-minimal-word-system.md`
2. `claims/L-7401-high-quotient-section.md`
3. `claims/T-7401-affine-section-rigidity.md`
4. `claims/T-7402-finite-affine-nucleus-rigidity.md`
5. `claims/T-7403-finite-rational-nucleus-rigidity.md`
6. `claims/T-7404-no-semilinear-sanctuary.md`
7. `Q-7401-least-root-decision.md`
8. `GLOBAL_BLOCKER_ASSESSMENT.md`
9. `CLAIM_INVENTORY.md`

## Scope boundary

This packet does not decide the least-root sequence and does not produce a Collatz counterexample. Its contribution is to:

1. freeze one exact strict global decision;
2. state honestly which side is a true reduction;
3. prove that direct quotient descent fails;
4. prove that every finite rational recursive extraction collapses to the forward map;
5. exclude every semilinear value-space sanctuary;
6. prevent further local machinery from being mistaken for ordinary existence.

The next valid theorem must either write the stabilizing root, prove the least roots escape, or introduce a genuinely unbounded nonlinear section variable and prove that it bounds the same initial ordinary root.