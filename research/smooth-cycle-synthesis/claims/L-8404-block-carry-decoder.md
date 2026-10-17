# L-8404 — Exact valuation-block decoder and carry graph

Claim ID: `L-8404`  
Title: A fixed accelerated block shape has at most one word at each dyadic residue, and concatenated positive-drift blocks reduce to finite carry reachability  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: exact accelerated affine formula; elementary power-of-two arithmetic  
Scope: finite alphabets of positive accelerated valuation blocks  
Related counterexample candidates: issue #41 and issue #9; no `K-84xx` candidate

## 1. Accelerated block constants

For a positive valuation word

```text
w=(a_0,...,a_(k-1)),
a_i>=1,
A=sum_i a_i,
```

write

```text
x_w=2^A,
y_w=3^k,
C_w=sum_(j=0)^(k-1) 3^(k-1-j) 2^(A_j),
A_j=sum_(i<j)a_i.
```

Then the block affine identity is

```text
x_w S_w(N)=y_w N+C_w.                                 (1)
```

The constants satisfy the exact first-letter recursion

```text
boxed:
C_(a_0 v)=3^(k-1)+2^(a_0) C_v.                       (2)
```

Every tail constant `C_v` is odd.

## 2. Exact residue decoder

Fix `k` and `A`. Given a residue

```text
R=C_w mod 2^A,                                        (3)
```

there is at most one positive valuation word of length `k` and total `A` that realizes it.

More precisely, put `R_0=R`, `A_0=A`. At position `j`, with `ell=k-j`, define

```text
delta_j=[R_j-3^(ell-1)]_(2^(A_j)).                    (4)
```

For a valid word with `ell>1`, `delta_j` is nonzero and

```text
boxed:
a_j=v_2(delta_j),                                     (5)
```

followed by

```text
R_(j+1)=delta_j/2^(a_j),
A_(j+1)=A_j-a_j.                                      (6)
```

The necessary checks are

```text
1<=a_j<=A_j-(ell-1).                                  (7)
```

At the final letter one must have

```text
R_(k-1)=1,
a_(k-1)=A_(k-1)>=1.                                  (8)
```

If all checks pass, equations `(4)`–`(8)` reconstruct the unique word and its exact ordinary constant `C_w`.

### Proof

Equation `(2)` gives

```text
C_w-3^(k-1)=2^(a_0) C_v.                              (9)
```

Because `C_v` is odd and `a_0<A` when more than one letter remains, the exact valuation of the left side modulo `2^A` is `a_0`. Division gives the tail residue modulo `2^(A-a_0)`. Induction proves `(4)`–`(8)` and uniqueness. **QED**

This is the accelerated-valuation specialization of the parity-cylinder inversion principle, but the explicit form `(4)`–`(8)` is the useful interface for the cycle search below.

## 3. Boundary carries for one proposed cycle state

Let a block `w` have positive drift

```text
D_w=x_w-y_w>0.                                       (10)
```

Fix an odd integer `n>=3` and express block-boundary states as

```text
N_j=n+c_j.                                           (11)
```

A transition through `w` is exactly

```text
boxed:
x_w c_(j+1)=y_w c_j+C_w-D_w n.                       (12)
```

Thus a finite block alphabet defines an exact directed graph on integer carries.

For a proposed edge from `c` at `n`, integrality of `(12)` requires

```text
C_w congruent D_w n-y_w c mod x_w.                   (13)
```

The decoder of Section 2 shows that, for each fixed shape `(k,A)`, condition `(13)` selects at most one valuation word. No enumeration of the

```text
binomial(A-1,k-1)
```

positive compositions is required.

## 4. Closed paths and positive cycles

Suppose a word is partitioned into blocks

```text
w_0 w_1 ... w_(g-1).
```

If it is an exact positive cycle based at `n`, its actual boundary states supply a closed carry path

```text
c_0=0 -> c_1 -> ... -> c_g=0                         (14)
```

through `(12)`.

Conversely, a closed path whose decoded blocks replay with all prescribed exact valuations gives an explicit positive cycle. Any computational hit must therefore expand the decoded block words and independently replay every valuation before receiving a candidate identifier.

For a negative result it is safe to enlarge the graph by retaining every integral carry edge from `(12)` even before checking intermediate block valuations. If this over-graph has no nonempty return to zero, the exact block grammar has no positive cycle.

## 5. Finite ordinary-state interval

For one positive-drift block put

```text
q_w=C_w/D_w.                                         (15)
```

Its affine map can be written

```text
F_w(N)=(y_w/x_w)N+(1-y_w/x_w)q_w.                    (16)
```

Every slope lies strictly between zero and one. The fixed point of a finite composition of such maps is a positive weighted convex combination of the individual `q_w`. Consequently every cycle tiled by a positive-drift block alphabet satisfies

```text
boxed:
min_w q_w <= n <= max_w q_w.                         (17)
```

It is therefore sufficient to search the finite odd interval

```text
ceil(min q_w) <= n <= floor(max q_w).                 (18)
```

### Extremes at fixed `(k,A)`

Moving one unit of valuation from a later letter to an earlier letter increases every intervening positive prefix term in `C_w`. Hence

```text
C_min=3^k-2^k                                        (19)
```

is attained by

```text
(1,...,1,A-k+1),
```

while

```text
C_max
 =3^(k-1)+2^(A-k+1)(3^(k-1)-2^(k-1))                 (20)
```

is attained by

```text
(A-k+1,1,...,1).
```

Equations `(17)`–`(20)` give an exact finite search interval without enumerating block words.

## Strategic meaning

This lemma changes the cost of a block-cycle search from

```text
enumerate every positive composition
```

to

```text
one exact residue inversion per carry, block shape, and candidate n.
```

At the period-37 critical shape the declared alphabet already contains

```text
5,621,728,217,559,090
```

individual valuation blocks, yet one residue query still has at most one decoded edge.

## Gap audit

- The finite carry theorem requires every block in the frozen alphabet to have `D_w>0`. A general cycle may use subcritical blocks whose losses are repaid later.
- Absence of a zero return in one block grammar is not a proof that no Collatz cycle exists.
- A carry edge is an over-approximation until the decoded word is replayed; every positive hit must pass the full exact verifier.
- Candidate-state finiteness in `(18)` uses positive drift for every block.
- No positive cycle or divergent orbit is constructed here.