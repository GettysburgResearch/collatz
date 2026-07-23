# Wave 8 topic note — restricted minimal words in base `3^12/2^19`

## Exact object

The PR #45/PR #50 six-branch chart is the deterministic ceiling map

\[
 x^+=\left\lceil {3^{12}x\over2^{19}}\right\rceil
\]

restricted by the minimal digit

\[
 a(x)=2^{19}x^+-3^{12}x
\]

to

\[
 \mathcal A=
 \{229376,258048,290304,326592,367416,413343\}.
\]

The set is a finite geometric window:

\[
 a_i=7\,2^{15}(9/8)^i,
 \qquad0\le i\le5.
\]

A positive root that remains in this digit set forever is already an unconditional divergent Collatz seed through the native physical conjugacy.

## Why this formulation is superior

- It is deterministic: the next digit is produced by the current ordinary integer.
- It is integer-first: there is no final completion-to-integer promotion.
- It retains one unbounded root, matching rational-base tree theory.
- It has exact external complexity and nonperiodicity theorems.
- It gives a direct target for proof-producing search and inductive invariants.

## Proof-producing solver design

State:

```text
current positive integer x
current residue x mod 2^19
current minimal digit a(x)
optional pulled-back cylinder Theta_s
controller/invariant certificate state
```

Transition:

```text
y=ceil(3^12*x/2^19)
a=2^19*y-3^12*x
accept iff a in A
x:=y
```

A candidate invariant must prove:

```text
x>0,
a(x) in A,
y in the invariant,
y>x.
```

The last inequality is automatic because `3^12>2^19` and `x>0`; only digit confinement and inductive closure remain.

## Recommended filters

1. **Complexity:** reject any controller family with proved factor-complexity coefficient below
   `log(2^19)/log(3^12/2^19)=971.866577...`.
2. **Periodicity:** eventually periodic type words are impossible.
3. **Finite-state caution:** the exact rooted future generally requires an infinite transducer/root state.
4. **Ordinary-marker:** a prescribed infinite digit word is valid only when its pulled-back residues stabilize at one ordinary integer.
5. **Conjectural normality:** use only as a heuristic prioritizer, never as a proof.

## High-value experiments

- Compute bottom words for many roots and measure first exit from `A`.
- Search roots by pulled-back cylinders rather than scanning consecutive integers.
- Learn nonlinear residue features of unusually long survivors.
- Test whether the six geometric digits produce an invariant in a mixed `2`/`3`/`7` coordinate.
- Compare survivor words with the Dubickas complexity lower bound at finite scales.

## Failure modes

- A long prefix is not an infinite root.
- A symbolic word with all digits in `A` may select a nonordinary `Q`-adic point.
- A modular SCC does not preserve the exact root.
- A conjectural normality statement cannot close the branch.
