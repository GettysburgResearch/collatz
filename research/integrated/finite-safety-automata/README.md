# IC-AUT-001 — the fixed-depth cofinite-tail automata obstruction

## Status

- **Mathematical status:** `VERIFIED`.
- **Repository role:** accepted integrated reference after merged PR #84.
- **Proof residency:** local proof packet.
- **Artifact status:** bounded automata artifact inspected; no finite artifact is extrapolated to an all-depth theorem.
- **Collatz status:** rules out one naive widening signal, not every regular sanctuary and not Collatz failure.

## Setup

Use the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

For an integer `d≥0`, define

\[
F_d=\{n\in Z_{>0}:T^j(n)\in\{1,2\}\text{ for some }0\le j\le d\},
\]

and

\[
S_d=Z_{>0}\setminus F_d.
\]

Encode positive integers by their unique finite binary words in least-significant-digit-first order. A word is canonical exactly when it is nonempty and ends in `1`.

For a finite forbidden set, the **canonical tail component** is the pair of residual languages reached after a sufficiently long prefix:

- `R_0`, for a prefix ending in `0`, rejecting the empty continuation;
- `R_1`, for a prefix ending in `1`, accepting the empty continuation.

From either state, input `0` reaches `R_0` and input `1` reaches `R_1`.

## Theorem

For every `d≥0`:

1. `F_d` is finite and
   \[
   \max F_d=2^{d+1};
   \]
   hence `S_d` is cofinite.
2. The minimal complete binary DFA for the canonical LSD-first encodings of `S_d` has exactly one cyclic strongly connected component: the terminal two-state canonical tail. Removing it leaves a directed acyclic graph.
3. `S_d` is not forward invariant. An exact witness is
   \[
   2^{d+2}\in S_d,
   \qquad
   T(2^{d+2})=2^{d+1}\notin S_d.
   \]
4. No cofinite set of positive integers can both exclude `{1,2}` and be forward invariant under `T`.

Therefore the obvious recurrent SCC in every fixed-depth safety automaton is a finite-horizon canonical-language artifact, not an all-depth Collatz sanctuary.

## Proof

### Finiteness and exact maximum

The positive preimages of `y` under `T` are

\[
2y
\]

always, and

\[
\frac{2y-1}{3}
\]

exactly when `y≡2 mod 3`. The second preimage, when present, is a positive odd integer strictly smaller than `2y`.

Starting from `{1,2}`, finitely many reverse steps therefore produce a finite set. At depth zero, the maximum is `2`. Suppose the maximum through depth `d` is `2^{d+1}`. Every new preimage is at most twice its target, so the next maximum is at most `2^{d+2}`. The even preimage chain contains `2^{d+2}`, so equality holds. Induction gives

\[
\max F_d=2^{d+1}.
\]

Every larger positive integer is in `S_d`, proving cofiniteness.

### The minimal-DFA tail

The canonical encodings of the finite set `F_d` have a maximum word length `h`. After reading any prefix `p` longer than `h`, no forbidden word can extend `p`.

For a nonempty continuation `x`, canonicality of `px` depends only on whether `x` ends in `1`. For the empty continuation, acceptance depends only on whether `p` ends in `1`. Thus every prefix longer than `h` has exactly one of the residual languages `R_0` or `R_1` described above.

They are distinct because they disagree on the empty continuation, and they form a terminal two-state strongly connected component.

If a state outside this component belonged to a directed cycle, repeat a nonempty cycle word. This would produce arbitrarily long prefixes whose residual state stayed outside `{R_0,R_1}`. Once the prefix length exceeded `h`, every residual must be `R_0` or `R_1`, a contradiction. Hence every other component is acyclic.

### Exact nonclosure witness

For `0≤j≤d`,

\[
T^j(2^{d+2})=2^{d+2-j}\ge4.
\]

Thus `2^{d+2}` avoids `{1,2}` through depth `d` and lies in `S_d`. Its image is `2^{d+1}`, and

\[
T^d(2^{d+1})=2,
\]

so the image is not in `S_d`.

### No cofinite sanctuary

Let `L` be cofinite. Choose `k` large enough that `2^k∈L`. If `T(L)⊆L`, repeated closure gives

\[
2^{k-1},2^{k-2},\ldots,2,1\in L.
\]

Therefore a cofinite forward-invariant set cannot exclude `{1,2}`. ∎

## Why it matters

Finite safety approximants necessarily accept every sufficiently large integer. Their terminal recurrent structure is therefore dominated by canonical encoding, not infinite Collatz survival.

A learning or PDR system that proposes the obvious terminal SCC as a sanctuary has rediscovered cofiniteness, not proved forward invariance. The useful finite object is the sink-stripped boundary DAG and, potentially, its inter-depth structure.

## Boundaries and common misreadings

- The theorem is fixed-depth; it does not identify the infinite intersection.
- It does not prove that every regular sanctuary is impossible. A sanctuary, if one exists, must at least be non-cofinite.
- The boundary is acyclic **within one fixed depth**. Inter-depth maps may still contain meaningful recurrence.
- “Tail” refers to DFA input residuals, not a tail of a Collatz orbit.
- A two-state SCC by itself does not imply cofiniteness unless it is eventually reached from all sufficiently long words.
- Bounded state counts and exact finite automata do not prove an all-depth language theorem.

## Methodological consequence

Any automata abstraction aimed at an ordinary all-depth witness should carry more than fixed-modulus residue recurrence. Candidate additions include:

- a canonical most-significant boundary;
- a height or word-length counter;
- a finite-support certificate;
- a transported residue tied to one initial integer;
- an exact ordinary concretization proof.

This is a **PROPOSED design consequence**, not a theorem that one particular enriched abstraction succeeds.

## Provenance

Primary source: PR #14 at

```text
9e3d90f50a6bf908401d2a2556513077daca3eb4
```

Files:

```text
research/safety-quotient/claims/D-9201-finite-safety-language.md
research/safety-quotient/claims/L-9201-cofinite-tail-obstruction.md
```

Source author: `gpt56-sol-01`.

Independent review:

```text
reports/gpt56-pro-03/2026-08-01-prepublic-review-pr3-pr14-pr16-pr19.md
@ 3d2b0a3c7e873388c42f00c5cbb4f09cf9897391
```

Verdict: `VERIFIED`. The proof was independently reconstructed. The bounded automaton artifact was inspected, but the theorem is the symbolic argument above.

## Next missing step

Define and verify sound inter-depth maps or an enriched ordinary-boundary abstraction. Any candidate recurrent core should be tested immediately against exact one-step closure and ordinary concretization, not only residue recurrence.
