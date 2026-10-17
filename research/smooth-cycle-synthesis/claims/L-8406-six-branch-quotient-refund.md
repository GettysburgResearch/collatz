# L-8406 — Exact quotient-refund normal form for the six-branch pulse chart

Claim ID: `L-8406`  
Title: The `(6,1)` pulse fiber is a deterministic six-state multiplicative one-counter map  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-8405`  
Scope: the supercritical `(L,b)=(6,1)` negative-three-cycle chart  
Related counterexample candidates: `Q-8402`; PR #51 run-core quotient; PR #49 complement quotient; no `K-84xx` candidate

## 1. Chart data

Put

```text
M=2^19=524,288,
N=9^6=531,441,
Delta=N-M=7,153.                                      (1)
```

Index the six branches of `L-8405` by their domain and output digits:

| `i` | word | `d_i` | `e_i` |
|---:|:---|---:|---:|
| 0 | `AAAAAB` | 360448 | 365367 |
| 1 | `AAAABA` | 471040 | 477468 |
| 2 | `AAABAA` | 267776 | 271431 |
| 3 | `AABAAA` | 366784 | 371790 |
| 4 | `ABAAAA` | 19416 | 19683 |
| 5 | `BAAAAA` | 349523 | 354294 |

The physical macro map is

```text
H(Mq+d_i)=Nq+e_i.                                     (2)
```

## 2. One quotient residue for every ordered branch pair

To continue from branch `i` into branch `j`, equation `(2)` must have the form

```text
Nq+e_i=Mq'+d_j.                                       (3)
```

Equivalently,

```text
Delta q+e_i congruent d_j mod M.                      (4)
```

Since `Delta` is odd, it is invertible modulo `M`. Define

```text
boxed:
rho_(i,j)=[(d_j-e_i)Delta^(-1)]_M.                   (5)
```

Then branch `j` follows branch `i` exactly when

```text
boxed:
q congruent rho_(i,j) mod M.                          (6)
```

Write

```text
q=rho_(i,j)+M ell,
ell>=0.                                                  (7)
```

Put

```text
boxed:
sigma_(i,j)=(N rho_(i,j)+e_i-d_j)/M.                 (8)
```

Substitution in `(3)` gives the exact refunded successor

```text
boxed:
q'=sigma_(i,j)+N ell.                                 (9)
```

Thus one `19`-bit cylinder is consumed and the unused ordinary lift is
transported by the odd multiplier `N=531,441`.

## 3. Deterministic form

No future branch symbol is required. From a finite state `(i,q)`, compute

```text
r=[Delta q+e_i]_M.                                    (10)
```

If `r` is not one of the six domain digits, the map is undefined. If

```text
r=d_j,
```

the distinctness of the digit table makes `j` unique, and

```text
boxed:
q'=q+(Delta q+e_i-d_j)/M.                             (11)
```

Equations `(5)`--`(9)` and `(10)`--`(11)` are the same partial map in cylinder
and causal forms.

## 4. Every legal quotient transition grows

For all `36` ordered pairs,

```text
boxed:
sigma_(i,j)>rho_(i,j).                                (12)
```

The exact difference matrix, with rows `i` and columns `j`, is

```text
6784 3822 4961  877  754 5979
3441  479 1618 4687 4564 2636
3256  294 1433 4502 4379 2451
6625 3663 4802  718  595 5820
1473 5664 6803 2719 2596  668
 149 4340 5479 1395 1272 6497.                        (13)
```

Hence, from `(7)` and `(9)`,

```text
q'-q
 =(sigma-rho)+(N-M)ell
 >0.                                                    (14)
```

The quotient itself—not merely the physical state—strictly increases at every
legal macro transition.

Statement `(12)` is a finite exact integer check over the displayed canonical
digits. `X-8404` reconstructs every residue, quotient, and difference directly
from `(1)`--`(8)`.

## 5. Physical reconstruction

A state `(i,q)` represents

```text
h=Mq+d_i,
n=-5+2h.                                               (15)
```

One legal transition is exactly the six two-odd-step Collatz blocks encoded by
the word in row `i`. Equation `(3)` identifies the next physical branch state
with `(j,q')`. Thus the quotient map loses no physical information.

## 6. Relation to the live quotient-refund programs

The update

```text
q=rho+M ell -> q'=sigma+N ell,
N>M,                                                    (16)
```

is a constant-modulus sibling of:

```text
PR #51:
  k=rho+2^E ell -> k+=sigma+9^(r+1)ell;

PR #49:
  k=rho+M_t ell -> k+=sigma+N_t ell.
```

All three systems have:

```text
- finitely many physical types;
- one exact moving cylinder;
- one finite ordinary quotient;
- multiplicative odd refund;
- and infinite definedness as the sole positive existence gap.
```

The present chart is the smallest fixed-scale instance and has the additional
strict quotient growth `(14)` with no threshold.

## Gap audit

- Strict growth does not imply that the partial map is defined forever.
- Every finite type word has an exact quotient cylinder, but its inverse-limit
  completion need not be an ordinary integer.
- A cycle in a fixed residue projection omits the most-significant boundary and
  is not a counterexample certificate.
- No finite state satisfying all-time definedness is supplied here.

## Suggested next attack

Seek a proof-carrying top-boundary invariant for `(10)`--`(11)`. Because every
legal quotient step already grows, a positive result needs only all-time
legality. The exact finite state should carry:

```text
(current branch,
 low quotient block,
 canonical most-significant boundary,
 one unbounded lift counter).
```

Any such invariant immediately closes `Q-8402`.
