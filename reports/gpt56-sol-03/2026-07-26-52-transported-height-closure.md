# Session report — bounded transported-height closure

**Agent:** `gpt56-sol-03`
**Issue:** #52
**Branch:** `cursor/transported-height-closure-8f0f`
**Date:** 2026-07-26
**Starting hypothesis:** transporting the initial-height parameter through the
exact `L-8252` affine branches should permit an exhaustive search over all
`X_0<2^512` without enumerating the seeds individually.

## Repository and source state read

I read the root operating rules and the complete PR #53 outlier-bridges packet
at head

```text
8b63eb7dda864430ad64c46ae6f8f58d399ef7b8
```

including `L-8251`--`L-8254`, `X-8251`, the `X-8252` README, and
`T-8255/X-8255`. I also reconstructed the physical formulas from PR #51 head

```text
bf00552e5054fd8e5d1692648911b377c5624e56
```

especially `O-8001`, `L-8004`, `T-8003`, and the independent `X-8005`
verifier.

`T-8255` is a separate, source-dependent exclusion for two-pulse lifts of
repeated negative cycles. It is not a logical input to this synchronized
bounded computation.

## Approaches attempted

### 1. Direct transported branch tree

At a branch-prefix node I represented the complete family by

```text
X_0=theta+K*q,
X_d=C+P*q,
0<=q<=q_max.
```

For each label, the unique quotient residue is

```text
rho=(xi_s-C)*P^(-1) mod R_s.
```

Substitution gives the exact update requested in the task:

```text
theta'=theta+K*rho
K'=K*R_s
C'=[M_s(C+P*rho)+T_s]/R_s
P'=M_s*P
q_max'=floor((q_max-rho)/R_s).
```

This representation succeeded. It reduced the full 512-bit interval to 1,936
nonempty branch-prefix nodes.

### 2. Finite intrinsic-label bound

For

```text
Y(q)=9^9(C+P*q)+a,
```

the canonical search has `Y(q)>0`. An intrinsic branch has
`v2(Y)=3s`, hence

```text
2^(3s)<=Y(q)<=Y_max=9^9(C+P*q_max)+a.
```

Therefore

```text
s<=(Y_max.bit_length()-1)//3.
```

The bound is `180` at the root and at most `186` anywhere in the retained
tree. No floating logarithm or unrecorded label cutoff is used.

### 3. Initial leaf-only certificate

The first prototype treated only branch nodes with no children as exits. That
was insufficient as a seed partition: an internal branch cylinder contains
both continuing residue subclasses and seeds that exit at the current prefix.
The generated count check exposed the error.

I corrected the certificate by recording an `EXIT` terminal and exact exit
seed count at every node. Branch words followed by this distinct terminal
symbol are prefix-free and their counts telescope to all `2^512` seeds.

**Status:** corrected before freezing artifacts.

## New exact result

`O-8256/X-8256` establishes the following bounded statement:

> No centered integer `0<=X_0<2^512` executes four consecutive synchronized
> branches with every intrinsic label at least `44`.

Frozen totals:

```text
nodes including root:                1,936
retained edges:                      1,935
candidate labels tested:           269,000
dead-end branch nodes:               1,866
exit terminals:                      1,936
survivors:                                0

depth histogram:
  0:                                     1
  1:                                   116
  2:                                 1,801
  3:                                    18
```

The root labels are exactly `44..159`. The maximum high-prefix depth is
exactly three. The eighteen depth-three words are frozen in both the claim and
canonical result; every one exits before a fourth branch.

Exit-trie SHA-256:

```text
5ea73d22ae33eaba8b154ace55c6fdca9c485eb871e3cd268089ef1ff8743f89
```

## Verification

The author implementation checks all imported constants from their defining
formulas. For each of 1,935 retained edges it checks:

1. the exact branch residue;
2. `s=v2(9^9*X+a)/3`;
3. the centered affine formula;
4. the raw `W` source formula;
5. nine physical `B` edges and `s` physical `A` edges.

The independent `verify.py` imports neither `run.py` nor project code. It uses:

- extended Euclid for the ordinary inverse;
- Newton--Hensel inversion modulo powers of two;
- the distinct `L-8253` reset expression for `xi_s`;
- integer shifts for binary height;
- an independent full BFS reconstruction.

It matches both frozen artifacts exactly.

Seven tests pass, including frozen `X-8251` regression, the `L-8253` 132-bit
prefix, brute-force valuation bounds, and differential checks over every
quotient in three real 12-bit transported-tail windows.

I also replayed both existing `X-8251` implementations and both existing
`X-8255` implementations. They reproduce their frozen transcript hashes

```text
X-8251: 62a6db9a403326384e207dddd9a7a135a0f9c03eb7a7cb92d6f26c18c0914908
X-8255: b60b6c1e4564ac52a52749af8e19f854fb0f3de0c0a6269037e3f452b91278a8
```

This replay checks the branch-local source packet; it does not remove
`T-8255`'s stated primary-Matveev source dependency.

## Candidate counterexamples

None.

No surviving bounded synchronized prefix, divergent seed, positive cycle, or
`K-####` object is proposed.

## Failed approaches and limitations

1. The initial leaf-only interpretation did not partition exits at internal
   prefixes; it was replaced by explicit terminal edges.
2. A bounded closure does not imply a uniform closure over all initial
   heights.
3. The result says nothing about nonsynchronized chart words or labels below
   `44`.
4. The cap constrains only `X_0`; later orbit values are not capped.
5. The computation cannot be promoted to a full Collatz exclusion.

## Potential errors

1. A reviewer should recheck that different-label child cylinders are
   disjoint because the label is intrinsic, rather than treating the
   terminal-count subtraction as an independent premise.
2. The bit-length bound uses positivity of `9^9*X_d+a` on the canonical
   corpus. Both implementations reconstruct positive retained states; the
   reusable helper uses endpoint absolute values for more general tests.
3. The physical replay begins at the synchronized pre-`B` boundary. It does
   not silently supply an earlier initial-run divisibility condition.
4. Upstream `L-8251`--`L-8253` remain proposed claims even though their exact
   formulas are independently exercised here.

## Corrections and source audit findings

At the frozen PR #53 head,

```text
experiments/X-8252-bezout-reset/README.md
```

describes `run.py`, `verify.py`, and `results/canonical.json`, but those files
are absent from both the PR file list and the checked branch. Only the README
exists. I therefore did not present X-8252 as a replayable artifact. The new
code rederives its reset identities and regresses shared data against the
present frozen X-8251 result.

No arithmetic correction was needed for the supplied constants:

```text
D9=68,332,056,247
omega=37,933,813,917
a=215,072,362
b=38,148,886,279.
```

All defining quotient and Bézout identities hold exactly.

## Files changed

```text
experiments/X-8256-transported-height-closure/README.md
experiments/X-8256-transported-height-closure/run.py
experiments/X-8256-transported-height-closure/verify.py
experiments/X-8256-transported-height-closure/test_run.py
experiments/X-8256-transported-height-closure/results/canonical.json
experiments/X-8256-transported-height-closure/results/exit-trie.json
research/outlier-bridges/claims/O-8256-bounded-transported-closure.md
reports/gpt56-sol-03/2026-07-26-52-transported-height-closure.md
```

## Claims affected

```text
O-8256  new, PROPOSED; supported by exact finite certificate X-8256
X-8256  new, exact finite bounded computation
```

No upstream claim status is changed.

## Recommended next actions

1. Independently review `O-8256`, beginning with the per-node finite label
   bound and terminal-partition semantics.
2. Run the same transported method at larger initial caps and record the
   maximum prefix depth without extrapolation.
3. Seek a symbolic upper bound relating initial binary height to possible
   synchronized high-prefix depth.
4. Keep this bounded language separate from `T-8255` and from any universal
   Collatz statement.

## Organizational improvement idea

Changing-cylinder experiments should standardize a terminal-trie schema with
two distinct objects:

```text
branch child cylinder;
exit complement at the current prefix.
```

Recording only dead-end nodes can silently omit exits from internal
cylinders. Exact terminal counts and a telescoping partition check should be
required for future transported searches.
