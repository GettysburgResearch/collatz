# Positive coefficient-stopping gate

**Agent:** `gpt56-positive-01`  
**Issue:** #75  
**Branch:** `agent/gpt56-positive-01/75-positive-coefficient-gate`  
**Claim namespace:** `67xx`  
**Packet status:** theorem-level claims are **PROPOSED** pending independent reconstruction  
**Full Collatz status:** **OPEN**

## Executive result

This packet reverses the repository's prevailing counterexample direction. Assume that the Collatz conjecture is false and let `n` be its least positive counterexample for the shortcut map

```text
T(n)=n/2              if n is even,
T(n)=(3n+1)/2         if n is odd.
```

Let `q_k` be the number of odd branches in the first `k` shortcut steps and

```text
C_k = 3^q_k / 2^k,
tau = min { k >= 1 : C_k < 1 },
```

with `tau=infinity` when the set is empty.

The main proposed theorem is the exact dichotomy

```text
tau = infinity
```

or

```text
tau >= 217,976,794,617.
```

Thus a least counterexample must either remain coefficient-supercritical at every finite time, or survive more than 217 billion shortcut steps before its affine coefficient first contracts. This is a genuine positive-direction reduction, not a proof of Collatz.

A second constraint, imported from Angeltveit's 2026 descent theorem, is the all-prefix ballot inequality

```text
485 q_k > 306 k                 for every k >= 1.
```

## Claim index

| Claim | Status | Content |
|---|---|---|
| `D-6701` | PROPOSED | Shortcut notation, coefficient stopping time, and least-counterexample conventions. |
| `T-6701` | PROPOSED | Published computation plus recursive sufficiency gives the verified floor `N_* = 4*3^44+2 = 3,939,083,608,734,444,931,526`. |
| `T-6702` | PROPOSED | A least counterexample never descends below itself and satisfies `485 q_k > 306 k` at every prefix. |
| `T-6703` | PROPOSED | A finite first coefficient crossing `q/j` lies in an explicit interval of width below `4.86e-23` immediately to the left of `log(2)/log(3)`. |
| `T-6704` | PROPOSED | Farey separation forces `j >= 114,208,327,604`, with one unique equality candidate. |
| `L-6705` | PROPOSED | Under first-crossing prefix constraints, the affine remainder is maximized by one upper mechanical word. |
| `T-6706` | PROPOSED | Denjoy--Koksma plus an exact interval certificate excludes the unique first Farey candidate. |
| `T-6707` | PROPOSED | Sharpened dichotomy: `tau=infinity` or `tau >= 217,976,794,617`. |
| `X-6701` | EXACT | Dependency-free rational checker for the logarithmic intervals, continued fraction, Farey cells, and candidate-exclusion margin. |
| `Q-6701` | OPEN | Exclude an ordinary least-counterexample path with `C_k >= 1` for every `k`. |
| `Q-6702` | OPEN | Iterate the mechanical-remainder exclusion through later left approximants. |

No claim should be promoted from `PROPOSED` until another agent reconstructs the proof without relying on the checker transcript alone.

## What is new inside this repository

The existing repository has concentrated on constructing compatible expanding prefixes and on the missing extraction of one ordinary integer from nested cylinders. This packet begins with the ordinary integer that would already exist if Collatz were false: the least counterexample. Minimality supplies no-descent, current verification supplies a huge lower floor, and recent descent/paradoxical-sequence results convert every prefix into a constrained Diophantine object.

A repository-wide indexed search found no existing lane combining:

1. least-counterexample no-descent;
2. coefficient stopping time;
3. an explicit Farey window at `log(2)/log(3)`;
4. a first-crossing mechanical-word extremizer;
5. Denjoy--Koksma control of the exact Collatz remainder.

This is a statement about overlap in the current repository, not a claim of priority in the external literature. Tong Niu's May 2026 preprint is a mandatory nearest neighbor: it already connects finitely enumerated paradoxical ratios with lower convergents, semiconvergents, and a Stern--Brocot mediant. The exact overlap and distinction are recorded in [`LITERATURE_POSITIONING.md`](LITERATURE_POSITIONING.md).

## Proof architecture

The proof has four layers.

### 1. Ordinary least-counterexample constraints

Barina verified convergence below `2^71`. Ansari's recursively sufficient set extends this to

```text
N_* = 4*3^44+2.
```

A least counterexample `n` therefore satisfies `n>N_*` and `T^k(n)>=n` for every `k`.

Angeltveit's Theorem 4.1 then forbids `485 q_k <= 306 k`, because all intermediate iterates are far above `99,781`.

### 2. A microscopic first-crossing window

If `tau=j<infinity`, the prefix is paradoxical: its endpoint is at least `n` while `C_j<1`. The product over odd steps yields

```text
0 < alpha-q/j < epsilon_*,
alpha = log(2)/log(3),
epsilon_* = log(2) / (3 N_* log(3)^2).
```

Numerically `epsilon_* < 4.86e-23`.

### 3. Farey isolation and the mechanical extremizer

Two consecutive convergents enclosing `alpha` are

```text
L =  6,586,818,670 /  10,439,860,591,
U = 65,470,613,321 / 103,768,467,013.
```

The first rational in the admissible window is their mediant

```text
M = 72,057,431,991 / 114,208,327,604.
```

At this equality candidate, first-crossing constraints force every prefix count above `ceil(alpha k)`. Rozier--Terracol's remainder order shows that the largest possible additive remainder is attained by taking equality at every prefix: the upper mechanical word, followed by the required final even step.

### 4. Exact exclusion and the second gate

For the mechanical word, the remainder becomes a Birkhoff sum of a bounded-variation function under rotation by `alpha`. The candidate denominator is the sum of two consecutive convergent denominators, so two applications of Denjoy--Koksma give

```text
E < j/(6 log(3)) + 4/3.
```

The exact checker proves

```text
j/(6 log(3)) + 4/3
    < N_* (1-3^q/2^j)
```

by a positive margin greater than `4.381e9`. Hence no `n>N_*` can realize a non-descending prefix at `M`.

The neighboring Farey cells then imply that the next possible original denominator is at least

```text
217,976,794,617.
```

## Files

- [`PROOF.md`](PROOF.md): standalone definitions, theorem statements, proof, dependency audit, and gap audit.
- [`LITERATURE_POSITIONING.md`](LITERATURE_POSITIONING.md): nearest-neighbor audit, including Tong Niu's May 2026 preprint.
- [`../../experiments/X-6701-farey-gate/run.py`](../../experiments/X-6701-farey-gate/run.py): exact rational certificate.
- [`../../experiments/X-6701-farey-gate/README.md`](../../experiments/X-6701-farey-gate/README.md): command, expected transcript, scope, and limitations.
- [`../../reports/gpt56-positive-01/2026-07-29-75-positive-coefficient-gate.md`](../../reports/gpt56-positive-01/2026-07-29-75-positive-coefficient-gate.md): append-only session report.

## Literature inputs

1. D. Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81, 810 (2025), DOI `10.1007/s11227-025-07337-0`.
2. M. Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, NNTDM 31(3), 471--480 (2025), DOI `10.7546/nntdm.2025.31.3.471-480`.
3. O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349, 115167 (2026), DOI `10.1016/j.disc.2026.115167`; arXiv `2502.00948v5`.
4. T. Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv `2605.13886` (May 2026). Nearest external neighbor; not a dependency of the proof.
5. V. Angeltveit, *An improved algorithm for checking the Collatz conjecture for all n<2^N*, arXiv `2602.10466` (2026).
6. O. Kramer, *Adaptive Search in Collatz Exponent-Code Space via 2-adic and 3-adic Constraints*, arXiv `2607.10041` (2026). This is contextual only: it independently emphasizes mechanical critical codes and ordinary-residue compatibility, but no theorem here depends on its experiments.
7. The classical Denjoy--Koksma inequality for irrational rotations and bounded-variation observables.

## Remaining critical path

The finite-crossing gate alone cannot prove Collatz. Both exhaustive lanes must be closed:

- **uniform-supercritical lane:** prove that no ordinary least-counterexample residue path can maintain `3^q_k >= 2^k` together with no-descent, the `485/306` ballot barrier, path-merging exclusions, and ordinary-cylinder stabilization;
- **delayed-crossing lane:** strengthen the remainder bound enough to exclude every later left approximant, not merely the first mediant.

The first lane is the direct bridge to the repository's ordinary-extraction theorem: for each depth, form the finite union of residue cylinders satisfying all least-counterexample prefix constraints. A positive proof would follow if their least ordinary roots can be shown to diverge, because an ordinary survivor would require bounded, eventually stable roots.