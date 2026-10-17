# L-9407 — Sparse stack partial-theta normal form

Claim ID: L-9407  
Title: Every prescribed stack directive is one sparse `2`-adic series and its finite cylinders  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9401; direct stack algebra; compatible with L-9406 and T-9409  
Scope: every infinite sequence of nonnegative stack heights  
Related counterexample candidates: issue #4 stack frontier and M1; no `K-####` candidate

## Setup

Fix stack heights

```text
m_0,m_1,m_2,...,
```

and put

```text
ell_t = 9*m_t+1,
h_0   = 0,
h_t   = sum_(0<=i<t) ell_i       for t>=1.
```

Define the binary support word `eps` by

```text
eps_n=1  iff  n=h_t for some t,
eps_n=0  otherwise.
```

Thus its stage blocks are exactly

```text
1 0^(ell_0-1), 1 0^(ell_1-1), 1 0^(ell_2-1), ... .
```

Let

```text
A_*(m)
 =Phi(eps)
 =(17/81)*sum_(t>=0) (64/81)^h_t
 in Z_2.                                             (1)
```

## Statement 1 — formal stack orbit

Let `A_t=Phi(sigma^(h_t) eps)` be the code tail beginning at stage `t`. Then

```text
H^(ell_t)(A_t)=A_(t+1).                              (2)
```

Moreover there is a unique `x_t in Z_2` with

```text
A_t=S_(m_t)(x_t)
   =64^(ell_t)*x_t+(64^(ell_t)+17)/81.               (3)
```

Hence every height directive determines one exact formal stack chain in `Z_2`.
No CRT choice remains at infinite depth.

## Statement 2 — context partial-theta series

Put

```text
H_0=0,
H_j=sum_(1<=i<=j) ell_i       for j>=1.
```

For the initial context define

```text
Z_0=81*x_0+1.
```

Then

```text
Z_0
 =17/81^(ell_0) * sum_(j>=0) (64/81)^H_j
 in Z_2.                                             (4)
```

Equivalently,

```text
x_0
 =-1/81
  +17/81^(ell_0+1)*sum_(j>=0)(64/81)^H_j.            (5)
```

This is the **sparse stack partial-theta normal form**.

## Statement 3 — equality with the active cylinders

For a finite directive

```text
m_0,...,m_K,
```

let `R_K mod Q_K` be the unique context cylinder of T-9409, where

```text
Q_K=product_(i=1)^K 64^(ell_i).
```

Let

```text
A_K^(fin)
 =(17/81)*sum_(t=0)^K (64/81)^h_t.                  (6)
```

Then, in exact `2`-adic congruence notation,

```text
S_(m_0)(R_K)
 =A_K^(fin)
   mod 64^(sum_(i=0)^K ell_i),                      (7)
```

and

```text
81*R_K+1
 =17/81^(ell_0)*sum_(j=0)^(K-1)(64/81)^H_j
   mod Q_K.                                         (8)
```

Thus the backward one-cylinder construction and the forward sparse-code
construction are the same inverse system.

## Statement 4 — ordinary-section equivalence

The selected formal chain has an ordinary initial context `x_0 in Z` iff
`A_*(m)` is an ordinary integer. Indeed,

```text
x_0=[A_*(m)-(64^(ell_0)+17)/81]/64^(ell_0).         (9)
```

The stage-prefix congruence makes the numerator divisible by the displayed
power of `64` in `Z_2`; if `A_*(m)` is ordinary, that is ordinary integer
divisibility. Conversely an ordinary `x_0` makes (3) ordinary.

Positivity and the chart class modulo `17` remain separate checks before any
candidate can be assigned a `K-####` identifier.

## Proof

The code map satisfies the exact shift identity

```text
Phi(eps)
 =(17/81)*eps_0+(64/81)*Phi(sigma eps).              (10)
```

At stage `t`, the code begins with one `1` and `ell_t-1` zeros. Iterating (10)
through this block proves (2). The first `ell_t` digits are the exact stage
word, so subtracting the stage constant and dividing by `64^(ell_t)` gives the
unique `x_t` in (3).

Equation (1) is the definition of `Phi` on the support positions `h_t`.
Multiplying (1) by `81`, subtracting the first term `17`, and dividing by
`64^(ell_0)` gives

```text
(81*A_*-17)/64^(ell_0)
 =17/81^(ell_0)*sum_(j>=0)(64/81)^H_j.
```

The left side is `81*x_0+1` by (3), proving (4) and (5).

For a finite prefix, the first omitted code term starts at

```text
h_(K+1)=sum_(i=0)^K ell_i,
```

so it vanishes modulo the modulus in (7). After removing the first stage, the
first omitted context term starts at

```text
H_K=sum_(i=1)^K ell_i,
```

which is exactly the exponent of `Q_K`; this proves (8). Uniqueness in T-9409
then identifies the two cylinder constructions. Statement 4 follows from (3).
**QED**

## Dependency audit

- D-9401 supplies `Phi` and the code indexing.
- The proof otherwise uses only the displayed geometric series and the exact
  stage word `1 0^(9m)`.
- T-9409 is used only to name and identify its already-unique finite cylinder;
  the congruences can be checked directly from the series.

## Gap audit

- The same rational partial sums are interpreted `2`-adically. Their real
  limits are not silently identified with an ordinary integer.
- Formal existence in `Z_2` is automatic for every directive and is not an
  ordinary-integer existence theorem.
- A nonrational coefficient power series can still take an algebraic value at
  a particular `2`-adic argument; function transcendence alone would not close
  M1.
- Equation (9) proves integrality equivalence, not positivity.

## Adversarial tests

`X-9405` independently computes the backward cylinders and the sparse partial
sums for every one-through-three-edge schedule over heights `{0,1,2,3}`, and
for a bounded `17/18` directive prefix. It verifies (7) and (8) exactly.

## Remaining uncertainty

The exact remaining value problem is whether the series in (4), for an
admissible balanced directive, can be an ordinary integer context. No such
value is claimed.

## Suggested next attack

Use the exponent structure in T-9410 to seek a `2`-adic irrationality or
transcendence theorem for

```text
sum_(j>=0)(64/81)^H_j,
```

where `H_j` has quadratic growth and Sturmian first differences.