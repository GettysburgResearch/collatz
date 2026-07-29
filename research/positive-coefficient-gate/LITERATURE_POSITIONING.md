# Literature positioning and nearest-neighbor audit

**Agent:** `gpt56-positive-01`  
**Issue:** #75  
**PR:** #76  
**Date:** 2026-07-29  
**Status:** source-positioning note; no external novelty claim

## Purpose

This note records the closest recent literature found after the mathematical packet was drafted. It narrows the contribution boundary and prevents the Farey language from being presented as if it arose without antecedents.

The load-bearing theorem in `PROOF.md` does not depend on any novelty assertion. It remains valid or invalid solely according to its explicit mathematical dependencies.

## 1. Rozier--Terracol: coefficient stopping and paradoxical sequences

Rozier and Terracol define

```text
C_j(n)=3^q/2^j,
tau(n)=min{j:C_j(n)<1},
t(n)=min{j:T^j(n)<n},
```

and call a finite segment paradoxical when its coefficient contracts but its endpoint does not fall below its start. Their work supplies the natural language for this packet, exact affine-remainder identities, and a remainder-order principle under parity-word rearrangement.

They also prove that an infinite stopping-time orbit would create infinitely many paradoxical sequences, so finiteness of nontrivial paradoxical sequences would imply Collatz. Their computational evidence and conjecture concern the nonexistence of paradoxical starts above `4,614`; they do not prove that conjecture.

### Relationship to this packet

The present packet specializes to the start of a **least counterexample**, for which every intermediate iterate is automatically no smaller than the start. It then adds a current verified floor, a microscopic Diophantine interval, an exact Farey candidate, a first-crossing mechanical extremizer, and a Denjoy--Koksma exclusion.

## 2. Tong Niu 2026: the nearest external neighbor

Tong Niu's May 2026 preprint, *Parity vectors and paradoxical sequences in the accelerated Collatz map* (`arXiv:2605.13886`), is the closest source found.

It proves:

1. a sharp finite parity-cylinder count: each length-`k` word occurs in one residue class modulo `2^k`, with count within one of `N/2^k` on `[1,N]`;
2. an exact fixed-length formula for the number of paradoxical starts attached to each parity word;
3. density zero for paradoxical sequences of any fixed bounded length.

It also observes, for the finitely enumerated small paradoxical examples, that their reduced `(j,q)` ratios are lower convergents, lower semiconvergents, or a Stern--Brocot mediant near `log(2)/log(3)`, and formulates an unproved approximation-structure conjecture. The paper explicitly states that it makes no progress toward Collatz, Terras's coefficient-stopping-time conjecture, or the global nonexistence of large paradoxical sequences.

### Exact overlap

- both programs use parity cylinders and the affine inequality
  ```text
  n <= E_w/(1-C_w);
  ```
- both recognize that paradoxical ratios sit close to `log(2)/log(3)`;
- both use continued-fraction or Stern--Brocot language.

### Exact distinction

The `67xx` packet does **not** assume Niu's approximation-structure conjecture. For a least counterexample above the imported verification floor, the product over odd iterates proves the explicit interval

```text
0 < log(2)/log(3)-q/j < 4.86e-23.
```

Elementary Farey separation then forces the first candidate rigorously. The packet additionally proves a constrained upper-mechanical remainder extremizer and excludes that candidate analytically with Denjoy--Koksma and an exact rational margin. Niu's fixed-length enumerator and worst-weight bound do not contain this exclusion or the resulting `217,976,794,617` gate.

Therefore Niu is a clear conceptual predecessor and mandatory citation, but the exact theorem packet is not a restatement of the results visible in that preprint. This is still **not** a priority claim: another source may contain the same synthesis.

## 3. Angeltveit 2026: descent sieve

Angeltveit's Theorem 4.1 gives a deterministic sufficient condition for descent:

```text
485 q <= 306 k
```

plus a lower bound `99,781` on the intermediate iterates implies that the endpoint is below the start.

For a least counterexample above the much larger verified floor, contraposition gives the all-prefix ballot constraint

```text
485 q_k > 306 k.
```

This constraint is auxiliary to the first Farey gate but is likely important for the remaining uniform-supercritical cylinder tree.

## 4. Barina 2025 and Ansari 2025: verification floor

Barina reports exhaustive convergence through `2^71`. Ansari's recursively sufficient interval argument extends a verified range through

```text
A=2*3^r+1
```

to twice that endpoint. Taking `r=44` yields the imported floor

```text
N_*=4*3^44+2.
```

This composition is load-bearing because the first Farey candidate is excluded only when the no-descent lower bound is strong enough. It is therefore marked `PROPOSED` pending independent source reconstruction rather than silently treated as a repository-proved fact.

## 5. Kramer 2026: non-load-bearing experimental context

Kramer's July 2026 preprint experiments with exponent/parity codes near mechanical critical slope and emphasizes the difference between symbolic drift and ordinary integer residue compatibility. This aligns with the repository's ordinary-extraction diagnosis but contributes no theorem used in `T-6701`--`T-6707`.

## 6. Contribution boundary after the audit

The defensible statement is:

> The current repository did not contain a lane combining least-counterexample no-descent, the Barina--Ansari floor, an explicit first-crossing Farey interval, a constrained mechanical remainder extremizer, and a Denjoy--Koksma exclusion. Recent external work already connects paradoxical ratios with continued fractions and Stern--Brocot structure, so no broad novelty is claimed for that motif.

The packet's review question is mathematical, not bibliographic:

```text
Does the explicit dependency chain really prove

tau=infinity
or
tau>=217,976,794,617

for a least counterexample?
```

## Sources to inspect first

1. O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349 (2026), 115167; arXiv `2502.00948`.
2. T. Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv `2605.13886` (May 2026).
3. V. Angeltveit, *An improved algorithm for checking the Collatz conjecture for all n<2^N*, arXiv `2602.10466` (February 2026).
4. D. Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81 (2025), article 810.
5. M. Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, NNTDM 31(3) (2025), 471--480.
6. O. Kramer, *Adaptive Search in Collatz Exponent-Code Space via 2-adic and 3-adic Constraints*, arXiv `2607.10041` (July 2026).