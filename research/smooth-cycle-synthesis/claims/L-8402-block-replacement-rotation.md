# L-8402 — Exact block-replacement and rotation laws

Claim ID: `L-8402`  
Title: Fixed-boundary word replacements localize the cycle numerator, and divisibility is rotation invariant  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: elementary affine-word algebra  
Scope: finite positive accelerated valuation words

## Definitions

For a word

```text
w=(a_0,...,a_(k-1)),
a_i>=1,
```

put

```text
A_j=sum_(i<j)a_i,
A=A_k,
C(w)=sum_(j=0)^(k-1)3^(k-1-j)2^A_j,
D(w)=2^A-3^k.
```

The affine action is

```text
S_w(n)=[3^k n+C(w)]/2^A.                              (1)
```

For concatenated words `uv`, write their summaries as `(k_u,A_u,C_u)` and
`(k_v,A_v,C_v)`.

## Statement 1 — concatenation law

```text
boxed:
C(uv)=3^k_v C(u)+2^A_u C(v).                          (2)
```

### Proof

The terms whose starting positions lie in `u` acquire all `k_v` later odd
multipliers.  The terms starting in `v` acquire the complete earlier dyadic
prefix `2^A_u`.  Splitting the defining sum gives (2). **QED**

## Statement 2 — fixed-boundary block replacement

Fix positions

```text
0<=u<v<=k
```

and replace the block

```text
(a_u,...,a_(v-1))
```

by a positive block of the same length and the same total valuation.  Let

```text
s_t=sum_(h=0)^(t-1)a_(u+h),
s'_t=sum_(h=0)^(t-1)a'_(u+h),
1<=t<v-u.
```

Then the full length, total valuation, and denominator are unchanged, while

```text
boxed:
C(w')-C(w)
 =sum_(t=1)^(v-u-1)
   3^(k-1-u-t) 2^A_u (2^s'_t-2^s_t).                 (3)
```

### Proof

Every prefix before `u` is unchanged.  Equal block totals make every prefix at
or after `v` unchanged.  Only the internal prefix exponents

```text
A_(u+t)=A_u+s_t
```

change.  Subtract their contributions to the defining sum for `C`. **QED**

## Statement 3 — adjacent swap

For an adjacent replacement

```text
(x,y)->(y,x)
```

at positions `u,u+1`,

```text
boxed:
Delta C
 =3^(k-u-2) 2^A_u (2^y-2^x).                         (4)
```

Disjoint adjacent swaps have additive numerator changes.

### Proof

There is exactly one internal prefix, so (3) has one term.  Disjoint fixed-sum
blocks modify disjoint prefix indices, hence their contributions add. **QED**

For the binary valuation alphabet `a_i=1+epsilon_i`, this specializes to

```text
01 -> 10 : Delta C=+3^(k-u-2)2^A_(u+1),
10 -> 01 : Delta C=-3^(k-u-2)2^(A_(u+1)-1).          (5)
```

## Statement 4 — cyclic rotation preserves divisibility

Let `w=uv` and let `rot(w)=vu`.  Then

```text
boxed:
2^A_u C(vu)-3^k_u C(uv)=D(w)C(u).                    (6)
```

Because `D(w)` is odd, both `2` and `3` are units modulo `D(w)`.  Consequently

```text
boxed:
D(w)|C(w)
 iff D(w)|C(rot(w)).                                  (7)
```

### Proof

Apply (2) to both concatenation orders:

```text
C(uv)=3^k_v C(u)+2^A_u C(v),
C(vu)=3^k_u C(v)+2^A_v C(u).
```

Multiply the second identity by `2^A_u`, the first by `3^k_u`, and subtract.
The terms containing `C(v)` cancel and the remainder is

```text
(2^(A_u+A_v)-3^(k_u+k_v))C(u).
```

This is (6), and unit cancellation gives (7). **QED**

## Constructive use

Equation (3) permits a proof-carrying search:

1. compile one large base word;
2. list disjoint local replacements;
3. compute their exact residue deltas;
4. solve a finite modular subset problem;
5. replay the chosen replacements independently.

The same identity also exposes the limitation: passing a divisor component of
`D` is only a necessary condition.  Full cycle closure requires the complete
ordinary identity `C=nD`.

## Dependency audit

No experiment or external theorem is used.

## Gap audit

- The lemma does not assert that the local deltas span the full denominator.
- A modular solution for a proper divisor of `D` is not a cycle.
- Real proximity of `C/D` to an integer is not exact equality.

## Adversarial tests

`X-8401` checks the general formula on finite controls and replays 43 disjoint
binary adjacent swaps at a trillion-step compressed target.