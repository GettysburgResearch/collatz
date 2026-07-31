# Session report — least-counterexample global proof attack

**Agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Issue:** #78  
**Branch:** `agent/gpt56-positive-02/least-counterexample-global`  
**Date:** 2026-07-31

## Starting instruction

The task was to combine the newest repository work with the latest literature and attempt a proof of the Collatz conjecture, while avoiding another finite-prefix amplifier, counterexample encoding, or conditional growth packet.

## Sources inspected

### Repository

- migrated repository `GettysburgResearch/collatz`;
- issue #75;
- draft PR #76, especially `T-6707` and `T-6708`;
- draft PR #77, especially the independent review of `T-6708` and new `T-6709`;
- the earlier ordinary-extraction, quotient-refund, cycle, and global-cartography work through the current accessible heads.

### Current primary literature

- Rozier--Terracol, arXiv:2502.00948v5 / *Discrete Mathematics* 349 (2026), 115167;
- Angeltveit, arXiv:2602.10466;
- Chang, arXiv:2603.25753;
- Barina, *Journal of Supercomputing* 81 (2025), article 810;
- Ansari, *Notes on Number Theory and Discrete Mathematics* 31 (2025), 471--480;
- Tao and the classical Terras--Everett interfaces as contextual inputs.

The Niu note arXiv:2605.13886 is withdrawn and is not treated as an independent theorem.

## Frozen exhaustive target

For a least positive counterexample, write

\[
D_k=q_k-{\log2\over\log3}k.
\]

The branch-qualified current frontier is:

```text
Lane A:
  D_k >= 0 for every k;
  the actual orbit tends to +infinity;

Lane B:
  a finite first crossing;
  current proposed threshold at least 217,976,794,617.
```

A positive cycle belongs to Lane B after rotation to its minimum.

## Approaches attempted

1. Tried to turn map-level residue balance into pointwise balance; rejected because Chang explicitly leaves the orbit-level one-bit mixing statement open.
2. Tried to combine almost-all descent with one least counterexample; rejected because density-zero exceptional sets may contain one orbit.
3. Tried to infer ordinary realization from the existing completed parity cylinders; rejected by the repository's ordinary-extraction countermodels.
4. Rewrote the exact multiplicative correction along one assumed ordinary Lane-A orbit and used ordinary distinctness and prime-to-six arithmetic rather than symbolic counting.
5. Re-expressed every first-crossing word as one exact residue cylinder with a complete finite no-descent list.

## New theorem chain

### `L-6501` — polynomial odd correction

An all-prefix-supercritical positive ordinary orbit cannot repeat a value. Apart from its initial source, all odd source values are distinct and coprime to six. Hence

\[
P_k
=\prod_{x_i\text{ odd}}
\left(1+{1\over3x_i}\right)
\le e^{7/9}k^{1/9}.
\]

### `T-6501` — polynomial coefficient records

The exact affine surplus gives

\[
\max_{m\le k}C_m
\ge
\left({\alpha\over2ne^{7/9}}\right)^{1/2}k^{4/9}.
\]

At a coefficient-record time `r`,

\[
C_r\ge{\alpha\over2ne^{7/9}}r^{8/9}.
\]

Therefore bounded coefficient surplus is impossible for a positive ordinary Lane-A orbit.

### `T-6503` — quantitative low-band sparsity

The correction product has the exact additive identity

\[
P_k
=1+{1\over3n}
\sum_{\substack{i<k\\x_i\text{ odd}}}3^{-D_i}.
\]

Consequently, for every fixed `H`,

\[
\#\{i<k:D_i\le H\}=O_{n,H}(k^{1/9}),
\]

so `D_i` tends to infinity in natural density one.

This excludes every bounded-discrepancy or positive-frequency critical-return model from Lane A.

### `T-6502` — cofinal harmonic window

Every acyclic no-descent crossing satisfies

\[
j\log2-q\log3
\le
\min\left\{
{q\over3n},
{1\over3n}+{1\over6}\log\left(1+{2(q-1)\over n}\right),
{7\over9}+{1\over9}\log q
\right\}.
\]

### `L-6502` — exact finite list for every crossing word

For a first-crossing word,

\[
x=r_w+2^jt,
\qquad
T^j(x)=y_w+3^qt,
\]

and no descent occurs exactly for

\[
0\le t\le
\left\lfloor{y_w-r_w\over2^j-3^q}\right\rfloor.
\]

Thus every individual Lane-B word is completely decided over ordinary integers. The remaining theorem must be uniform over all words.

## Breakthrough assessment

The pass did **not** prove Collatz.

It did remove a genuine infinite sublane:

```text
an ordinary all-time-supercritical orbit
cannot have bounded surplus,
cannot be recurrent in any fixed surplus band with positive density,
and must have polynomially growing coefficient records.
```

This is stronger than the existing conclusion that the assumed orbit diverges. It imposes a new exact arithmetic profile on every remaining Lane-A witness.

## Exact remaining blockers

### Lane A

Exclude an ordinary orbit with:

```text
unbounded coefficient records;
record law at least r^(8/9);
only O(k^(1/9)) visits to each fixed low-surplus band;
actual pointwise Collatz integrality at every step.
```

### Lane B

Prove a cofinal theorem over every first-crossing word, using its canonical residue `r_w` and exact finite candidate list. Another denominator threshold without cofinal exclusion is not enough.

### Cycles

Force whole-denominator cycle equality and replay, or exclude every periodic member of the Lane-B lists.

## Candidate objects

None. No proof of Collatz, no positive cycle, and no divergent seed is claimed.

## Files added

```text
research/least-counterexample-global/README.md
research/least-counterexample-global/CLAIM_INVENTORY.md
research/least-counterexample-global/LITERATURE_AUDIT.md
research/least-counterexample-global/Q-6501-close-two-coefficient-lanes.md
research/least-counterexample-global/claims/D-6501-least-counterexample-two-lane-framework.md
research/least-counterexample-global/claims/L-6501-distinct-odd-source-product-bound.md
research/least-counterexample-global/claims/L-6502-first-crossing-cylinder-decision.md
research/least-counterexample-global/claims/T-6501-supercritical-coefficient-record-growth.md
research/least-counterexample-global/claims/T-6502-paradoxical-harmonic-window.md
research/least-counterexample-global/claims/T-6503-low-surplus-density-zero.md
```

## Recommended next offense

Do not improve the conditional growth conclusion again. Attack one of:

1. a pointwise orbit-mixing theorem strong enough to contradict the sparse-return Lane-A profile;
2. an inverse-tree/minimality theorem forcing a smaller counterexample from every such sparse-return orbit;
3. a cofinal lower bound on first-crossing canonical residues `r_w`;
4. a full-denominator theorem eliminating every positive cycle.
