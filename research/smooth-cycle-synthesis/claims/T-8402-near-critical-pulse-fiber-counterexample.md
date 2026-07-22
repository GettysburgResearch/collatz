# T-8402 — Arbitrarily near-critical pulse fibers with exponential branching

Claim ID: `T-8402`  
Title: The negative three-cycle pulse chart contains arbitrarily near-critical supercritical fibers with exponentially many exact branches  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-8405`  
Scope: fixed-weight macro charts in the ordinary coordinate `n=-5+2h`  
Related counterexample candidates: issue #41, issue #46, PR #51; no `K-84xx` candidate

## 1. Supercritical criterion

Use the fixed-weight chart of `L-8405`:

```text
M_(L,b)=2^(3L+b),
N_L=9^L,
|D_(L,b)|=binomial(L,b).
```

Put

```text
theta=log_2(9/8)=log_2(9)-3.                           (1)
```

Then

```text
boxed:
N_L/M_(L,b)=2^(theta L-b).                             (2)
```

Hence the chart is supercritical exactly when

```text
b/L<theta.                                             (3)
```

For every `L>=6`, choose

```text
b_L=floor(theta L).                                    (4)
```

The number `theta` is irrational, so

```text
0<theta L-b_L<1.
```

Therefore every such chart satisfies

```text
boxed:
1<N_L/M_(L,b_L)<2.                                    (5)
```

## 2. Arbitrarily near-critical subsequence

There are infinitely many pairs of integers `(L,b)` with

```text
0<theta L-b<1/L.                                       (6)
```

An elementary pigeonhole proof applies to the fractional parts of

```text
0,theta,2theta,...,L theta.
```

Taking an infinite sequence of improving denominators gives `(6)`. Along that
sequence,

```text
boxed:
N_L/M_(L,b)=2^(theta L-b) -> 1 from above.             (7)
```

Thus the pulse architecture supplies exact supercritical Collatz charts whose
multiplier can be made arbitrarily close to one.

## 3. Exponential branch supply

Along the same sequence,

```text
b/L -> theta in (0,1).
```

Consequently the branch count

```text
binomial(L,b)
```

grows exponentially in `L`. More explicitly, for every closed interval

```text
0<alpha<=b/L<=beta<1,
```

the largest binomial coefficient identity

```text
sum_(j=0)^L binomial(L,j)=2^L
```

and standard ratio comparison around `b` give

```text
binomial(L,b)>=2^(cL)/(L+1)                            (8)
```

for some `c=c(alpha,beta)>0`. Since `b/L -> theta`, one fixed positive `c`
works eventually.

The near-critical limit therefore does not collapse to a single branch: it
retains an exponentially growing exact collision fiber.

## 4. Explicit certified shapes

The first three frozen lower approximants used by `X-8403` are:

| `L` | `b` | input radix | branches | conclusion |
|---:|---:|---:|---:|:---|
| 6 | 1 | `2^19` | 6 | `2^19 < 9^6 < 2^20` |
| 53 | 9 | `2^168` | 4,431,613,550 | `2^168 < 9^53 < 2^169` |
| 665 | 113 | `2^2108` | `17483960556008270027789260935692849310945078464608626002918548755009061518797627539210884186649776932937953715574037393534756563500` | `2^2108 < 9^665 < 2^2109` |

For the last row the multiplier differs from one by less than `0.000088` in the
real embedding, while the exact fiber has `433` binary bits of branch count.
These decimals are explanatory only; the proof and verifier use the displayed
integer power comparisons.

## 5. Counterexample criterion

Every branch of `H_(L,b)` is an exact finite positive Collatz block in the
coordinate

```text
n=-5+2h.
```

Assume `N_L>M_(L,b)` and one ordinary integer `h_0>3` remains in the chart for
all forward macro-steps. For its selected branch word `w_r`, equation `(5)` of
`L-8405` gives

```text
h_(r+1)=(N_L h_r+C_(w_r))/M_(L,b)
       >=(N_L/M_(L,b)) h_r
       >h_r.                                           (9)
```

Thus `h_r` and the physical states

```text
n_r=-5+2h_r
```

are strictly increasing and unbounded. The concatenated exact branch replays
therefore give a positive ordinary shortcut-Collatz trajectory avoiding the
trivial cycle forever.

Hence

```text
boxed:
One nontrivial ordinary infinite path in any supercritical
fixed-weight pulse chart is an unconditional Collatz counterexample. (10)
```

No separate growth theorem would remain.

## 6. What this changes

The constructive state is no longer restricted to one padded negative-cycle
edge. A single two-letter physical system yields:

```text
- arbitrary macro length;
- an exact prescribed pulse density;
- exponentially many collision branches;
- multiplier arbitrarily close to one from above;
- and a deterministic residue decoder for implicit branches.
```

This provides a direct interface between the negative-cycle offense, the
collision-fiber program, and the ordinary-section/carry methods of PR #20 and
PR #49.

## Gap audit

- The theorem constructs chart families, not an ordinary infinite path.
- Exponential branch count and supercriticality do not prove that one finite
  ordinary marker survives every cylinder.
- The exact finite minima in `X-8403` grow through the audited depths; this is
  bounded evidence, not nonexistence.
- No modular lasso or `2`-adic completion is promoted to an ordinary witness.
- No positive cycle, divergent seed, or complete Collatz counterexample is
  claimed without the ordinary path required by `(10)`.

## Next constructive target

Use the implicit branch decoder from `L-8405` to build a proof-carrying
one-counter or stack invariant for one near-critical shape. The smallest exact
laboratory is `(L,b)=(6,1)`; the first very large fiber is `(53,9)`. A positive
certificate must give one explicit finite `h_0`, preserve the canonical
most-significant boundary, and prove all-time branch legality.
