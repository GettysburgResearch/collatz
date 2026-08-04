# LIT-KTHM-0050 — Linear-height phase-34 stages refund the next quotient

**Type:** exact native cross-branch theorem with a complete proof.  
**Maps to:** `PR3/L-0031`, `PR33/T-9705`, `SYN/T-9831`, `SYN/T-9834`, PR #38 `ACL-P014`, and the proposed linear-height regeneration program.

## 1. Setup

Use the stabilized phase-34 scaled-tail recurrence of `PR3/L-0031`:

```text
2^[11(t_(j+1)+1)] W_(j+1)
 = 3^[7(t_j+1)] W_j + b_(i_j),                           (1)
```

where every height is divisible by `16`, the type belongs to `{0,1,2,3}`, and

```text
b=(9,54,36,24).
```

Instead of the doubling-scale schedule in the frozen corrected architecture, fix a multiple of `16`, denoted `B`, and take the linear grid

```text
t_j=B+16j,
0<=j<=256.                                               (2)
```

Let one 256-transition stage run from `B` to `B+4096`.

## 2. Exact stage exponents

Composing `(1)` gives

```text
2^[E(B)] W_out
 =3^[A(B)] W_in + tau_B(w),                              (3)
```

for a positive `{2,3}`-unit toll sum `tau_B(w)`, with

```text
A(B)=7*sum_(j=0)^255(B+16j+1)
    =1792B+3657472,                                      (4)

E(B)=11*sum_(j=1)^256(B+16j+1)
    =2816B+5792512.                                      (5)
```

The next complete linear stage begins at `B+4096` and has radix exponent

```text
E(B+4096)=2816B+17326848.                                (6)
```

## 3. Quotient-refund inequality

### Theorem 1

For every multiple of `16` satisfying

```text
B>=477424,                                               (7)
```

one has

```text
boxed:
3^[A(B)] > 2^[E(B+4096)].                                (8)
```

### Proof

The elementary exact inequality

```text
3^53>2^84                                                (9)
```

is the lower logarithm bound already used in the phase-34 packet. It is enough to prove

```text
84A(B)>53E(B+4096).
```

Substitution from `(4)` and `(6)` gives

```text
84A(B)-53E(B+4096)
 =1280B-611095296.                                       (10)
```

At `B=477424` the right side is `7424>0`, and it increases with `B`. Equations `(9)`–`(10)` prove `(8)`. QED.

Thus a unit of free quotient entering one stage contains more than one complete radix of the following stage. This is the opposite inequality from the frozen doubling schedule used by `PR33/T-9705`.

## 4. Every finite word pair has infinitely many positive quotient transitions

Fix a current stage word `w` and a next stage word `v`. Put

```text
Q=2^[E(B+4096)].                                        (11)
```

Write the current canonical input/output form as

```text
W_in = R_B(w)+2^[E(B)]Y,
W_out=S_B(w)+3^[A(B)]Y.                                 (12)
```

Let `R_(B+4096)(v)` be the canonical input residue of the next stage.

### Theorem 2

There is one residue `y_0 mod Q` such that every

```text
Y=y_0+kQ                                                  (13)
```

gives an integral transition from `w` to the next-stage cylinder of `v`. The resulting next quotient is

```text
Y_next=c_(w,v)+3^[A(B)]k                                 (14)
```

for one integer `c_(w,v)`. For all sufficiently large `k`, both quotients are positive, and

```text
lim_(k->infinity) Y_next/Y
 =3^[A(B)]/Q>1.                                          (15)
```

### Proof

The next cylinder condition is

```text
S_B(w)+3^[A(B)]Y
 congruent to R_(B+4096)(v) mod Q.                       (16)
```

The coefficient `3^[A(B)]` is odd, hence invertible modulo the power of two `Q`; therefore `(16)` has one solution `y_0 mod Q`. Substitute `(13)` and divide the exact difference in `(16)` by `Q`. The term involving `k` becomes `3^[A(B)]k`, proving `(14)`. Positivity follows for large `k`, and `(15)` follows from `(8)`. QED.

## 5. What this changes

The proposed exclusion in `PR33/T-9705` relies first on paying the **next** complete doubling-stage radix, which traps a signed ordinary quotient in `{0,-1}`. The linear schedule violates that load-bearing inequality. It therefore supplies an exact example of the `signed quotient refund` escape listed by PR #38 and the maximal Evertse boundary in `SYN/T-9831`.

It also changes the endpoint budget. Along a genuinely growing linear-height quotient path, endpoint words can dominate the primitive projective height rather than occupy a subunit exponent. Thus Evertse's endpoint gate is not inherited automatically from the frozen class.

## 6. The unresolved ordinary-integer theorem

Theorems 1–2 are finite transition results. They do **not** choose one finite `Y_0` whose future belongs to the required residue class at every stage. An arbitrary infinite word sequence still selects an inverse-limit quotient.

The decisive positive target is now:

```text
construct an integer-first invariant K_B of positive quotients such that
for every (B,Y) in K_B,
one explicitly chosen word v and one ordinary k in (13)
produce (B+4096,Y_next) in K_(B+4096),
with Y_next>Y.                                           (17)
```

A proof of `(17)`, together with the existing physical tower replay, would produce a positive ordinary unbounded Collatz orbit.

## 7. Gap and scope audit

- The theorem changes the padding schedule; it does not refute `PR33/T-9705` in its frozen doubling-scale scope.
- Pairwise finite transitions do not imply a coherent infinite integer path.
- The stage word has not been chosen by a finite ordinary rule.
- The endpoints may introduce a changing prime alphabet; no finite-rank theorem is invoked.
- No counterexample or `K-####` object is claimed.