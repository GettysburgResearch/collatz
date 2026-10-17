# Session report — intrinsic primitive-core decoder

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Branch:** `agent/gpt56-cylinder-01/43-linear-quotient-refund`  
**Date:** 2026-07-23

## Starting hypothesis

The complement-counter theorem `T-8504` still carried large connector inverse data in its derivation. The goal was to determine whether the physical state could be normalized so that the all-time target became one familiar ordinary arithmetic recurrence rather than a mixed-radix connector system.

## Main derivation

The exact binary and ternary signatures of consecutive boundary words are

```text
v_2(W_n)=i_n,
v_3(W_n)=beta_(i_(n-1)),
beta=(2,3,2,1).
```

Removing these signatures gives the prime-to-six core

```text
C_n=W_n/[2^(i_n)3^(beta_(i_(n-1)))].
```

Substitution into the physical connector equation collapses every stage to

```text
2^(L_n) C_(n+1)=3^(G_n) C_n+1,
```

with

```text
L_n=11(t_n+17)+i_(n+1)-i_n,
G_n=7(t_n+1)+beta_(i_(n-1))-beta_(i_n).
```

This is `L-8505`.

## `T-8506` — automatic core growth

The exact lower logarithm bound `3^53>2^84` gives

```text
3^[7(t+1)]/2^[11(t+17)] > 2^177
```

for every `t>=3744`. Bounded type corrections cost less than seven bits, hence

```text
C_(n+1)>2^170 C_n.
```

The prime-to-six part of the physical shifted boundary grows at every connector.

## `T-8507` — inverse-free runtime map

An intrinsic state is now only

```text
(t,gamma,i,C),
gamma in {1,2,3},
i in {0,1,2,3},
gcd(C,6)=1.
```

Compute

```text
G=7(t+1)+gamma-beta_i,
D=11(t+17)-i,
X=3^G C+1.
```

The step is defined iff

```text
2^D | X
```

and, for `Y=X/2^D`,

```text
3^(beta_i)Y mod64 in {5,30,20,56}.
```

The latter residue gives the unique next type `j`, and `C'=Y/2^j`. The state updates to `(t+16,beta_i,j,C')`.

The high divisibility itself forces the current source cell, so no separate low-cell condition or connector inverse is needed. The physical integer is

```text
n=2^(11t+5+i)3^gamma C-34.
```

Every defined core step is exactly one phase-34 tower block of the shortcut map.

## `L-8506` — finite ordinary block compiler

For fixed `(t,gamma,i)`, the high inverse and six-bit target gate compile into four binary blocks. Enforcing `gcd(C,3)=1` splits each into two ternary lifts, yielding exactly eight ordinary source blocks modulo

```text
3*2^(D+6).
```

Each has an exact high-tail replacement with multiplier greater than `2^170`. Local existence and growth are complete; only next-scale block compatibility remains.

A draft statement initially omitted the input condition `3 does not divide C`; it was corrected before publication to the exact eight-block form. The proof history is visible in the branch commits.

## Exact experiments

### X-8504

```text
two-step chains:             256
binary signatures:           512
ternary signatures:          512
coprime core checks:         256
semantic digest:
9610e5be23c04c02a1a1ee3a95c40ce7a96939c103cc67558862c3e3c1de0e09
```

### X-8505

```text
intrinsic core transitions:       256
automatic source-cell checks:     256
high-block divisibility checks:   256
six-bit output decodes:           256
170-bit growth checks:            256
semantic digest:
195d29ef16bb7038ac9b3da9080344dfcc450f6663a973a757e475503afcf10e
```

Both have separately written independent checkers.

## Candidate counterexamples

None. No `K-85xx` identifier was created.

## Exact remaining target

Find one finite core state whose intrinsic decoder is defined forever. The required inductive invariant has been reduced to recurrence of:

```text
one exact high binary zero block,
one six-bit output cell,
one rapidly growing prime-to-six core.
```

Every other counterexample obligation is already part of the theorem chain.

## Failed or closed approaches

- fixed-modulus and low-type lassos omit the high binary block;
- bounded additive-counter controllers become ultimately periodic;
- fixed-prime libraries contradict `T-8505`;
- local branch abundance is irrelevant because next-scale compatibility is the sole missing condition;
- a first four-block formulation that ignored input ternary primitivity was rejected and repaired.

## Files changed

- `L-8505-primitive-core-syracuse.md`
- `T-8506-primitive-core-growth.md`
- `T-8507-intrinsic-core-decoder.md`
- `L-8506-core-block-replacement.md`
- `X-8504-primitive-core-turnover/`
- `X-8505-intrinsic-core-decoder/`
- packet README, inventory, gap audit, and `Q-8501`.

## Recommended next attack

1. Treat the eight block replacements of `L-8506` as a top-boundary transducer and search for a symbolic section identity, not a low-depth lasso.
2. Compare the canonical high inverse `[-3^(-G)]_(2^D)` with PR #3's ordinary quadratic bulk generator at the exact top block, not only in low prefixes.
3. Adapt the independently verified completion-height/carry machinery of PR #16 to the nonstationary core equation.
4. Use the negative-three-cycle chart as a minimal regression example for any proposed intrinsic-core invariant.
