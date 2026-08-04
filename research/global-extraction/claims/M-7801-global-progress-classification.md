# M-7801 — Global progress classification and stopping rules

**Claim ID:** `M-7801`  
**Type:** methodological / organizational proposal  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-global-01`  
**Created:** 2026-07-25  
**Dependencies:** `T-7801`, `R-7801`  
**Scope:** project-level classification against the ordinary positive-integer counterexample objective

## 1. Five levels of mathematical progress

Every repository result should be classified by its strongest proved implication, not by the complexity of its formalism or computation.

### Level I — complete finite witness

A finite object is written down and independently replayed to prove one of:

```text
positive divergent Collatz orbit;
positive nontrivial Collatz cycle;
finite certificate for another rigorously equivalent disproof.
```

This is a `K-####` candidate.

### Level II — global decision of a prescribed exhaustive class

A theorem proves either:

```text
one ordinary root exists in the whole prescribed class;
```

or

```text
no ordinary root exists in the whole prescribed class.
```

Examples of valid Level-II outcomes include:

- bounded least roots, producing one explicit seed;
- least roots tending to infinity, eliminating the class;
- a universal Diophantine obstruction for every word in the class;
- a full finite enumeration whose coverage is mathematically exhaustive.

This is genuine progress even when the class is a strict subsystem of Collatz.

### Level III — exact reduction to one unresolved global scalar or sequence

The result proves an equivalence such as

```text
architecture inhabited
  <=> least-root sequence bounded;

fixed word is a cycle
  <=> full denominator divides the numerator;

ordinary realization
  <=> appended cylinder blocks eventually vanish.
```

This is legitimate structural progress if the reduced object is simpler, canonical, and reusable. It is not yet a decision of the class.

### Level IV — conditional dynamics after existence

The result proves:

```text
if a forever-defined ordinary orbit exists,
then it grows / refunds / introduces fresh primes / has high complexity.
```

This can be important infrastructure. It is not evidence that the ordinary orbit exists.

### Level V — bounded evidence or local language control

This includes finite prefix searches, bounded support exclusions, proper-factor divisibility, near-integrality, modular lassos, SCCs, entropy estimates, and dimension or measure calculations without an extraction or full-denominator theorem.

These results may guide discovery or verify interfaces. They must not be summarized as global progress without their exact bounded scope.

## 2. Blunt assessment of the current program

The repository is **not** merely circular in every direction.

Genuine accomplishments include:

- independent reconstruction and correction of nontrivial theorem chains;
- universal exclusion of at least one complete frozen stage architecture;
- exact exclusion of several periodic, affine, fixed-support, or fixed-pulse families;
- proof-producing finite arithmetic and mixed-place closure interfaces;
- identification and repair of false compactness, completion, sign, indexing, and source-transfer inferences.

Those are real mathematical results.

However, the positive ordinary-orbit program has not crossed its decisive existence boundary. The leading constructions now give exact induced maps for which one forever-defined positive integer would be a counterexample, but the remaining statement is still

```text
there exists one positive integer whose exact decoder is defined forever.
```

Inside a strict subsystem this is narrower than arbitrary Collatz counterexample existence, but it is still the entire positive-existence question for that subsystem. Conditional growth, permanent refund, prime renewal, and generated capacity do not reduce the least-root problem by themselves.

The repeated reformulations are therefore best described as follows:

```text
local and conditional structure: genuinely improved;
ordinary positive existence: not yet advanced past the least-root dichotomy;
```

## 3. Ordinary-orbit acceptance gate

For every live induced architecture `A`, define

\[
m_N(A)=\min\{x>0:x\text{ realizes }N\text{ exact architecture blocks}\}.
\]

A new positive-orbit contribution counts as global progress only if it proves one of:

1. `m_N(A)` is bounded;
2. `m_N(A)` eventually stabilizes;
3. one explicit integer belongs to every depth set;
4. `m_N(A)->infinity`;
5. every root exits by a global ranking or Diophantine contradiction.

Items 1–3 produce an ordinary infinite seed. Items 4–5 eliminate the architecture.

A finite-depth lower bound, an unbounded family of different long-lived roots, or an inverse-limit point does not pass this gate.

## 4. Cycle acceptance gate

For an accelerated valuation word `w`, put

\[
D_w=2^{A(w)}-3^{k(w)},
\qquad
C_w=\sum_j3^{k-1-j}2^{A_j}.
\]

A positive cycle requires

\[
D_w>0,
\qquad
C_w=nD_w
\]

for a positive integer `n`, followed by exact valuation replay.

The following are global cycle progress:

- direct proof of `D_w|C_w` and replay;
- a mixed-place height theorem whose combined dyadic, odd-prime, and real bounds force `C_w-nD_w=0`;
- universal exclusion of an infinite word class;
- a complete finite enumeration of an explicitly bounded class.

The following do not close the cycle implication:

- divisibility by a proper factor of `D_w`;
- a real near-integer without a sufficient exact height budget;
- many local Hensel levels far below the global forcing threshold;
- a compressed grammar without complete physical replay.

## 5. Why the targets are genuinely weaker than Collatz

Each induced refund, centered, H, or fixed-chart architecture recognizes a proper prescribed subset of Collatz trajectories. Deciding its least-root sequence does not decide all positive integers.

Likewise, a theorem excluding one valuation grammar, support class, pulse cone, or length range leaves all other cycle words open.

Therefore both permitted global targets are genuinely narrower:

```text
ordinary target:
  decide one exact strict subsystem;

cycle target:
  force or exclude one exact word class.
```

A positive subsystem result gives a counterexample because the subsystem embeds into Collatz. A negative result only removes that subsystem.

## 6. Recommended project stopping rules

Before opening another positive-orbit formalism or experiment, require a written answer to:

```text
What new statement about m_N does this prove?
```

Before opening another cycle factor or near-integer experiment, require:

```text
What fraction of the exact full-denominator height gate does this certify,
and how can the remaining gap close uniformly?
```

If the answer is “none,” classify the work as interface validation, bounded evidence, or discovery infrastructure rather than a new counterexample route.

## 7. Recommended portfolio

The highest-value work is now concentrated in two tasks.

### Ordinary extraction

Prove boundedness or divergence of the least-root sequence for one of the live strict architectures, preferably beginning with the smallest fixed chart and then the common finite union.

### Full-denominator cycle closure

Either cross a mixed-place height threshold for one chart-compatible compressed word or prove a uniform obstruction for the complete grammar being searched.

Additional conditional growth or finite-prefix depth is lower priority unless it enters one of these two implications directly.

## 8. Status discipline

The words below should be used consistently:

- `EXTRACTED ORDINARY ROOT` — one finite integer realizes all depths;
- `ARCHITECTURE ELIMINATED` — every positive integer exits;
- `INVERSE-LIMIT COMPATIBLE` — a completion exists, with no ordinary conclusion;
- `CONDITIONALLY EXPANDING` — growth holds after ordinary existence;
- `FULL-DENOMINATOR CLOSED` — exact cycle equality is forced;
- `PROPER-FACTOR HIT` — no cycle conclusion;
- `FINITE PREFIX` — no infinite conclusion.

This vocabulary prevents the same unresolved ordinary-integer step from being hidden under successive encodings.