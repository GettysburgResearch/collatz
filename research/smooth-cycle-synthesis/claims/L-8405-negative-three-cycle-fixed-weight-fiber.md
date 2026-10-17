# L-8405 — Fixed-weight pulse words form exact collision fibers

Claim ID: `L-8405`  
Title: Equal pulse-count words over the negative three-cycle chart share one radix and give distinct exact Collatz branches  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: elementary accelerated Collatz algebra; branch-qualified `PR51/O-8001` as an independent comparison  
Scope: the ordinary negative-three-cycle coordinate `n=-5+2h`  
Related counterexample candidates: issue #41, issue #46, PR #51; no `K-84xx` candidate

## 1. Two exact ordinary letters

Put

```text
n=-5+2h.
```

There are two exact two-odd-step Collatz blocks.

### Unpulsed letter `A`

If

```text
h=8q,
```

then the advertised accelerated valuations are `(1,2)` and

```text
boxed:
h -> 9q.                                               (1)
```

Indeed,

```text
n=16q-5
 ->[a=1] 24q-7
 ->[a=2] 18q-5=-5+2(9q).
```

### First-pulse letter `B`

If

```text
h=3+16q,
```

then the advertised valuations are `(2,2)` and

```text
boxed:
h -> 3+9q.                                             (2)
```

Indeed,

```text
n=32q+1
 ->[a=2] 24q+1
 ->[a=2] 18q+1=-5+2(3+9q).
```

The domains are disjoint. In affine form,

```text
A(h)=9h/8,
B(h)=(9h+21)/16.                                      (3)
```

## 2. Composite word formula

Let

```text
w=w_0...w_(L-1) in {A,B}^L,
b=number of B letters in w,
B_j=number of B letters before position j.
```

Put

```text
M_(L,b)=2^(3L+b),
N_L=9^L.                                               (4)
```

The exact composite is

```text
boxed:
M_(L,b) F_w(h)=N_L h+C_w,                              (5)
```

where

```text
boxed:
C_w=21 sum_(j:w_j=B) 9^(L-1-j) 2^(3j+B_j).            (6)
```

### Proof

After a prefix using binary exponent `E`, appending `A` sends

```text
(C,E) -> (9C,E+3),
```

while appending `B` sends

```text
(C,E) -> (9C+21*2^E,E+4).
```

Starting from `(0,0)` gives `(4)`--`(6)` by induction. **QED**

## 3. One exact digit per word

Since `N_L` is odd, define

```text
boxed:
d_w=[-C_w N_L^(-1)]_(M_(L,b)),                         (7)
```

and

```text
boxed:
e_w=(N_L d_w+C_w)/M_(L,b).                            (8)
```

Then every integer in the branch cylinder has the exact macro transition

```text
boxed:
F_w(M_(L,b)q+d_w)=N_L q+e_w.                           (9)
```

Moreover, the final divisibility condition in `(7)` is equivalent to every
intermediate branch divisibility in the word. Thus the chronological word is
replayed exactly, including all `2L` accelerated valuations.

### Path-domain proof

The first letter requires divisibility by `8` for `A` or by `16` after adding
`21` for `B`. Reducing the composite numerator modulo that first radix recovers
exactly this first condition because all later radices are powers of two and all
intervening multipliers are odd. Divide by the first radix and repeat. Induction
proves equivalence with every local condition.

The digits `d_w` are distinct for distinct words having the same `(L,b)`. If two
words shared one digit, the same ordinary input would have to enter two different
first branch domains at their first disagreement. The domains in `(1)`--`(2)`
are disjoint, a contradiction.

## 4. Exact fixed-weight collision chart

For every pair `(L,b)`, the `binomial(L,b)` words of weight `b` therefore form
one partial radix chart

```text
boxed:
H_(L,b)(M_(L,b)q+d_w)=N_L q+e_w,
|D_(L,b)|=binomial(L,b).                               (10)
```

Every branch is an actual finite positive Collatz block in the coordinate
`n=-5+2h`; no symbolic branch is added by completion or interpolation.

## 5. Constructive decoder

A residue `d modulo M_(L,b)` can be checked without listing the whole fiber.
Starting from its least representative, repeatedly apply the unique legal
letter among `(1)` and `(2)`. Reject if neither letter is legal, if more than `L`
letters are needed, or if the final pulse count differs from `b`. Hence each
residue query returns at most one branch word.

This is the pulse-chart analogue of `L-8404`: exponentially many implicit
branches can be accessed by one exact deterministic residue replay.

## Exact six-branch example

For

```text
(L,b)=(6,1),
M=2^19=524,288,
N=9^6=531,441,
```

one obtains:

| word | `d_w` | `e_w` |
|---|---:|---:|
| `AAAAAB` | 360448 | 365367 |
| `AAAABA` | 471040 | 477468 |
| `AAABAA` | 267776 | 271431 |
| `AABAAA` | 366784 | 371790 |
| `ABAAAA` | 19416 | 19683 |
| `BAAAAA` | 349523 | 354294 |

Every row satisfies `(9)` exactly, and

```text
N-M=7,153>0.                                           (11)
```

## Gap audit

- A finite branch word or finite cylinder is not an infinite ordinary path.
- The exact digit set is sparse; branch multiplicity does not imply ordinary
  realization.
- A periodic symbolic directive selects a rational completion but does not by
  itself supply a positive ordinary initialization.
- No infinite survivor, divergent seed, positive cycle, or Collatz
  counterexample is constructed here.

## Verification

`X-8403` reconstructs all branches and direct physical replays for `(6,1)`,
`(12,2)`, and `(18,3)`, freezes the complete six-branch table, and computes the
first eight exact least cylinders of the six-branch chart.
