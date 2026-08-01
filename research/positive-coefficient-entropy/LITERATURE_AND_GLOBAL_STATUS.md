# Literature and global-status audit

**Snapshot date:** 2026-07-31  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Purpose:** identify what the newest literature genuinely contributes to a proof of Collatz, what remains pointwise, and where `T-6802` fits

## 1. Primary rigorous neighbors

### Vigleik Angeltveit — exact finite verification and descent sieves

```text
An improved algorithm for checking the Collatz conjecture for all n < 2^N
arXiv:2602.10466, submitted 2026-02-11
```

The paper gives an improved exhaustive verification algorithm and exact finite-prefix sieves, including descent, path merging, preimage restrictions, and the quantitative odd-density criterion imported by PR #76.

The relevant strength is deterministic and pointwise **at a fixed finite verification scale**. It does not prove that one arbitrary infinite orbit samples residues generically or must enter a finite verified range.

Repository use:

- PR #76 imports the `485/306` ballot barrier for a least counterexample;
- the delayed-crossing lane should incorporate the path-merging and preimage losses into the mechanical remainder maximization;
- no finite verification extension alone closes the infinite problem.

Primary source:

```text
https://arxiv.org/abs/2602.10466
```

### Olivier Rozier and Claude Terracol — paradoxical finite sequences

```text
Paradoxical behavior in Collatz sequences
Discrete Mathematics 349 (2026), 115167
arXiv:2502.00948v5, revised 2026-05-17
```

This is the closest established source for the first-coefficient-crossing lane. It analyzes finite prefixes whose multiplicative coefficient predicts contraction while the endpoint still exceeds the start, and explains why such paradoxical behavior is closely connected to Collatz.

The work is finite and structural, not a global proof. PR #76's Farey-window argument is a least-counterexample specialization using a much larger verified floor, a mechanical extremizer, and Denjoy--Koksma.

Primary sources:

```text
https://arxiv.org/abs/2502.00948
https://doi.org/10.1016/j.disc.2026.115167
```

### Edward Y. Chang — map balance versus orbit balance

```text
A Structural Reduction of the Collatz Conjecture to One-Bit Orbit Mixing
arXiv:2603.25753, submitted 2026-03-24
```

The paper proves exact low-depth block decompositions and a map-balance theorem: the map itself is essentially unbiased between two short-gap outcomes. It then isolates the remaining statement as pointwise balance of two residue classes modulo `32` along a sparse orbit subsequence.

This separation is directly relevant:

```text
map-level balance is proved;
orbit-level balance remains open.
```

`T-6802` adds a deterministic individual-orbit pressure theorem. It says that an all-time-supercritical ordinary path must realize enough distinct parity factors to force polynomial physical records. It does **not** turn factor complexity into the required residue-frequency balance.

Primary source:

```text
https://arxiv.org/abs/2603.25753
```

### Jonathan S. Gilbert — exact pruned-graph conjugacy

```text
A Collatz-Equivalent Map on the Nonzero Integers
Preprints.org 202607.0575, posted 2026-07-08
```

The paper constructs an exact conjugacy from the conjecture-relevant part of the Collatz graph to a map on the nonzero integers and explicitly makes no proof claim. Its value is coordinate simplification; the universal orbit question survives unchanged.

Primary source:

```text
https://www.preprints.org/manuscript/202607.0575
```

## 2. Withdrawn overlap

Tong Niu's

```text
Parity vectors and paradoxical sequences in the accelerated Collatz map
arXiv:2605.13886
```

was withdrawn on 2026-05-20 because Rozier--Terracol already contained the relevant enumeration and ratio observations. It made no claim toward Collatz or the coefficient-stopping-time conjecture.

The repository should cite Rozier--Terracol rather than treating the Niu note as an independent active advance.

Primary source:

```text
https://arxiv.org/abs/2605.13886
```

## 3. Audit of recent claimed complete proofs

### Funnel-density / ergodic proof

```text
David D. Zelenka,
The Collatz Conjecture Resolved: Funnel Density and the Impossibility of Divergence,
Zenodo 10.5281/zenodo.18626114, 2026-02-13
```

The public proof chain moves from a geometric valuation law across integers, through ergodic genericity, to probability-zero divergence, and then states that probability zero in a deterministic system means impossibility.

That final inference is invalid:

```text
measure zero != empty.
```

Birkhoff gives genericity almost everywhere, not for every orbit. More sharply, the ordinary positive integers form a countable Haar-null subset of `Z_2`, so an almost-everywhere theorem can leave every ordinary starting integer logically unresolved.

The presentation also assumes uniqueness of the positive cycle on the basis of a bounded search and an irrationality heuristic. Excluding all nontrivial positive cycles is itself an open global obligation.

Disposition: **not a proof of Collatz**. See `claims/R-6801-almost-everywhere-is-not-pointwise.md`.

Primary source:

```text
https://doi.org/10.5281/zenodo.18626114
```

### Hut induction manuscript

```text
Dylan Motimba,
All orbits of the collatz map attain the trivial cycle 4 2 1:
A proof via the theory of huts and 2-adic classification classes,
Cambridge Open Engage, 2026-07-20,
DOI 10.33774/coe-2026-zw9t8
```

The abstract claims a well-founded induction on classes of odd multiples of three. The hosting page labels the manuscript an unreviewed working paper.

The abstract alone is not enough to audit the load-bearing points:

1. every physical orbit step must map to the stated hut transition;
2. the rank used by induction must strictly decrease after a uniformly finite physical segment;
3. the classification must cover every relevant integer without identifying distinct orbit states improperly;
4. the claimed smaller hut must preserve the same convergence implication needed by the induction.

Disposition in this packet: **unverified, not imported**. A separate line-by-line reconstruction of the full manuscript is required before any theorem is used.

Primary source:

```text
https://doi.org/10.33774/coe-2026-zw9t8
```

## 4. The repository's current positive theorem chain

The new positive-direction branches now isolate a clean least-counterexample split.

### Finite first coefficient crossing

PR #76 proposes:

\[
\tau(n)=\infty
\quad\text{or}\quad
\tau(n)\ge217{,}976{,}794{,}617
\]

for the least positive counterexample.

The proof combines:

```text
verified floor
+ least-counterexample no descent
+ microscopic Diophantine window
+ Farey denominator gate
+ mechanical remainder extremizer
+ Denjoy--Koksma.
```

### Infinite coefficient stopping time

PR #77 proposes:

\[
D_k\ge0\ \forall k
\quad\Longrightarrow\quad
T^k(n)\to+\infty.
\]

The present packet adds:

\[
\liminf_{N\to\infty}
\frac{B_N}{\log_2N}
\ge\kappa_*>0,
\]

and

\[
X_N\ge nN^{\delta_*-o(1)}.
\]

Thus the infinite-stopping-time lane is no longer an amorphous exceptional orbit. It is a quantitatively constrained divergent ordinary orbit with polynomial record growth forced by exact parity-factor arithmetic.

## 5. What still blocks a proof of Collatz

There are two exhaustive remaining obligations.

### A. Exclude the all-time-supercritical ordinary path

It is not enough to prove:

- map-level balance;
- almost-everywhere mixing;
- high factor complexity;
- or polynomial record growth.

One needs a pointwise arithmetic theorem that makes the required residue visitation incompatible with one ordinary orbit.

The sharp target is:

```text
prove that the least ordinary representative
among all depth-N coefficient-supercritical cylinders
tends to infinity.
```

Equivalently, prove every ordinary integer has a coefficient-subcritical prefix.

### B. Exclude every delayed first crossing

For every later rational approximant in the microscopic window, show

\[
E_{\max}(j,q)
<
N_*\left(1-\frac{3^q}{2^j}\right),
\]

where `E_max` is maximized over parity words satisfying all genuine least-counterexample constraints.

The current upper mechanical word uses only the coefficient prefix barrier. The next attack should impose simultaneously:

```text
485/306 ballot barrier;
every intermediate no-descent inequality;
mod-9 preimage restrictions;
path merging;
odd-even-even exclusions;
Ostrowski block decomposition.
```

## 6. Blunt status

The latest rigorous literature and the newest repository work do **not** currently yield a complete proof of Collatz.

They do produce a coherent global program:

```text
finite crossing:
    Diophantine approximation + constrained remainder pressure;

infinite crossing time:
    exact parity-cylinder separation + entropy/height pressure
    + a still-missing pointwise residue theorem.
```

The remaining statements are genuinely global and pointwise. Replacing them by another average, density, finite prefix, or free symbolic completion would not close the conjecture.
