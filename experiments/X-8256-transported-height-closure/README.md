# X-8256 — Exact bounded transported-height closure

**Experiment ID:** `X-8256`
**Associated claim:** `O-8256`
**Issue:** #52
**Agent:** `gpt56-sol-03`
**Status:** exact finite computation on the declared bounded synchronized
sublanguage

## Question

Can any ordinary centered state

```text
0 <= X_0 < 2^512
```

execute four consecutive synchronized branches whose intrinsic labels all
satisfy `s>=44`?

This is a bounded question about the `L-8251`--`L-8253` synchronized
sublanguage. It is not a search over all Collatz trajectories and cannot
exclude a Collatz counterexample outside this coordinate, above the cap, or
outside the all-high synchronized language.

## Exact machine

The source constants are reconstructed from

```text
D9    = 16^9-9^9 = 68,332,056,247
omega = -9^(-9) mod D9 = 37,933,813,917
a     = (9^9*omega+1)/D9 = 215,072,362
b     = (16^9*omega+1)/D9 = 38,148,886,279
W     = omega+D9*X.
```

The scripts also check

```text
b-a=omega,
2^36*a-9^9*b=1.
```

For each proposed intrinsic label `s>=44`, put

```text
h_s = 3s+36,
R_s = 2^h_s,
M_s = 9^(s+9),
T_s = 9^s*a-8^s*b,
xi_s = -T_s*M_s^(-1) mod R_s.
```

The centered branch is

```text
F_s(X)=(M_s*X+T_s)/R_s
```

on `X=xi_s mod R_s`. Every retained edge is checked against the intrinsic
label

```text
s=v2(9^9*X+a)/3
```

and against both the raw source formula

```text
W'=[9^s*(1+9^9*W)-2^(3s)]/2^(3s+36)
```

and a direct replay of nine physical `B` chart edges followed by `s` physical
`A` chart edges.

## Transported search

At a branch-prefix node, the complete represented family is

```text
X_0 = theta+K*q,
X_d = C+P*q,
0 <= q <= q_max.
```

Here `P` is odd. Pulling back branch `s` gives the unique residue

```text
rho = (xi_s-C)*P^(-1) mod R_s.
```

The child is nonempty exactly when `rho<=q_max`, and its exact state is

```text
theta' = theta+K*rho,
K'     = K*R_s,
C'     = [M_s*(C+P*rho)+T_s]/R_s,
P'     = M_s*P,
q_max' = floor((q_max-rho)/R_s).
```

The root is `(theta,K,C,P)=(0,1,0,1)` with `q_max=2^512-1`.

## Complete finite label bound

At every node,

```text
Y(q)=9^9*(C+P*q)+a > 0
```

on the canonical corpus. If `s` is intrinsic, then

```text
2^(3s) <= Y(q) <= Y_max,
Y_max=9^9*(C+P*q_max)+a.
```

Let `beta=Y_max.bit_length()-1`, equivalently the unique integer satisfying
`2^beta<=Y_max<2^(beta+1)`. Then every possible label satisfies

```text
s <= beta//3.
```

The root upper bound is `180`; the largest bound at any retained node is
`186`. The complete run tests 269,000 candidate labels. No floating-point
logarithm or heuristic truncation is used.

## Frozen result

```text
nodes including root:                1,936
retained branch edges:               1,935
candidate labels tested:           269,000
dead-end branch nodes:               1,866
terminal exit records:               1,936
survivor records:                        0

node depth histogram:
  depth 0:                               1
  depth 1:                             116
  depth 2:                           1,801
  depth 3:                              18
```

The root retains exactly labels `44..159`. Exactly eighteen length-three
branch cylinders are nonempty; all eighteen have no fourth high child.
Therefore the maximum number of consecutive defined `s>=44` synchronized
branches below the initial cap is exactly three.

`results/exit-trie.json` records all 1,936 exact transported states. A node
also records the number of represented seeds that exit at that prefix, even
when the node has continuing children. Appending the terminal symbol `EXIT`
to those branch words makes the terminal set prefix-free and partitions all
`2^512` initial integers exactly. This distinction is necessary: dead-end
branch nodes alone do not partition seeds that exit from an internal prefix.

Exit-trie SHA-256:

```text
5ea73d22ae33eaba8b154ace55c6fdca9c485eb871e3cd268089ef1ff8743f89
```

## Independent verification and tests

`verify.py` imports neither `run.py` nor any project module. It independently:

1. derives all constants with an extended-Euclidean inverse;
2. derives `xi_s` from the distinct `L-8253` reset-coordinate formula;
3. uses a Newton--Hensel dyadic inverse;
4. derives every finite label bound by integer shifts;
5. reconstructs every node, terminal count, source formula, and physical
   replay;
6. checks prefix-freeness, exact seed partition, and both frozen artifacts.

`test_run.py` includes seven tests, including regression against the frozen
`X-8251` constants and branch rows, the 132-bit `L-8253` common prefix, and
brute-force differential checks over every quotient in three actual 12-bit
tail windows.

No randomness or external package is used. Replay with:

```bash
python3 -B -m py_compile \
  experiments/X-8256-transported-height-closure/run.py \
  experiments/X-8256-transported-height-closure/verify.py \
  experiments/X-8256-transported-height-closure/test_run.py

python3 -B experiments/X-8256-transported-height-closure/run.py \
  --check-results \
  experiments/X-8256-transported-height-closure/results/canonical.json

python3 -B experiments/X-8256-transported-height-closure/verify.py \
  experiments/X-8256-transported-height-closure/results/canonical.json

python3 -B experiments/X-8256-transported-height-closure/test_run.py -v
```

The frozen artifacts were generated on Linux with CPython 3.12.3 using only
the standard library and arbitrary-precision integers.

## Source boundary and correction

The frozen source snapshots are PR #53 head
`8b63eb7dda864430ad64c46ae6f8f58d399ef7b8` and PR #51 head
`bf00552e5054fd8e5d1692648911b377c5624e56`.

At the PR #53 head, `experiments/X-8252-bezout-reset/README.md` describes
`run.py`, `verify.py`, and `results/canonical.json`, but those three files are
absent from the PR and branch; only its README is present. Consequently
X-8256 does not claim regression against a nonexistent X-8252 artifact. It
rederives the reset identities directly and regresses shared branch data
against the present X-8251 artifact.

`T-8255/X-8255` concerns two-pulse lifts of repeated negative cycles. It is a
separate source-dependent exclusion and is not a dependency of this bounded
synchronized computation.

## Interpretation

The exact result is only:

> No `X_0` in `[0,2^512)` has four consecutive defined synchronized branches
> with every intrinsic label at least `44`.

It says nothing universal about larger `X_0`, nonsynchronized chart words,
general positive Collatz trajectories, or the existence of a Collatz
counterexample.
