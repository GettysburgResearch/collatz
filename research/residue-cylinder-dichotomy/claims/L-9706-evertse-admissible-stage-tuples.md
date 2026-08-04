# L-9706 — Evertse-admissible connector-free stage tuples

**Claim ID:** `L-9706`  
**Title:** Every hypothetical cap or co-cap tail produces infinitely many distinct nondegenerate `(1,1/50,{2,3})`-admissible projective zero sums  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9704`, `L-9705`; J.-H. Evertse, *On sums of S-units and linear recurrences*, Compositio Math. 53 (1984), Corollary 1  
**Scope:** every eventual cap or co-cap chain in the corrected 256-transition stage class

## External theorem

For a nonzero integer `x` and finite prime set `S_0`, define

```text
out_(S_0)(x)=|x|*product_(p in S_0)|x|_p.
```

This is the part of `|x|` supported outside `S_0`.

Evertse's 1984 Corollary 1 says: fix `n>=1`, `c>0`, `0<=d<1`, and a finite prime set `S_0`. There are only finitely many primitive integer tuples

```text
(x_0,...,x_n),
gcd(x_0,...,x_n)=1,
```

such that

```text
x_0+...+x_n=0,
```

no nonempty proper subsum vanishes, and

```text
product_(k=0)^n out_(S_0)(x_k)
 <= c*||x||^d,
||x||=max_k |x_k|.                                (1)
```

The source theorem is used as an external black box. We verify its native hypotheses with

```text
S_0={2,3},
n=257,
c=1,
d=1/50.                                           (2)
```

## Cap tuple

On a cap chain, let `U_m=Z_m>0`. `L-9704` gives

```text
2^(E_m)*U_(m+1)
 =3^(A_m)*U_m
  +sum_(j=0)^255 b_(i_(m,j))*2^(U_(m,j))*3^(V_(m,j)).   (3)
```

Define 258 integer coordinates

```text
a_(m,0)= 2^(E_m)*U_(m+1),
a_(m,1)=-3^(A_m)*U_m,
a_(m,j+2)=-b_(i_(m,j))*2^(U_(m,j))*3^(V_(m,j)).   (4)
```

Their sum is zero. Exactly one coordinate is positive.

## Co-cap tuple

On a co-cap chain, put `U_m=-Z_m>0`. Then

```text
3^(A_m)*U_m
 =2^(E_m)*U_(m+1)
  +sum_(j=0)^255 b_(i_(m,j))*2^(U_(m,j))*3^(V_(m,j)).   (5)
```

Use the positive coordinate `3^(A_m)U_m`, the negative coordinate `-2^(E_m)U_(m+1)`, and the same 256 negative internal coordinates. Again the sum is zero and exactly one coordinate is positive.

In either case, a proper subset excluding the positive coordinate has negative sum. A proper subset containing it omits at least one negative coordinate and has positive sum. Thus no nonempty proper subsum vanishes.

## Primitive gcd

Let

```text
g_m=gcd(|a_(m,0)|,...,|a_(m,257)|),
x_(m,k)=a_(m,k)/g_m.
```

Every internal coordinate is supported only on `{2,3}`. Hence `g_m` has no prime divisor above three.

The `j=0` internal term has zero binary prefix exponent, so

```text
v_2(g_m)<=max_i v_2(b_i)=3.
```

The `j=255` term has zero ternary suffix exponent, so

```text
v_3(g_m)<=max_i v_3(b_i)=3.
```

Therefore

```text
g_m divides 2^3*3^3,
g_m<=216.                                          (6)
```

## Outside-prime content

Primitive normalization removes only powers of two and three. Every internal primitive coordinate has outside content one. The two endpoint coordinates have outside content at most `U_m` and `U_(m+1)`. Hence

```text
product_(k=0)^257 out_{2,3}(x_(m,k))
 <=U_m*U_(m+1).                                    (7)
```

The cap estimate in `L-9704` and the co-cap estimate in `L-9705` give, in both cases,

```text
limsup log_2(U_m)/E_m <=2166/346819,
limsup log_2(U_(m+1))/E_m <=4332/346819.
```

Thus

```text
limsup log_2(U_m*U_(m+1))/E_m
 <=6498/346819
 <1/50.                                             (8)
```

One raw coordinate contains `2^(E_m)U_(m+1)`, and (6) gives

```text
||x_m||>=2^(E_m)/216.                              (9)
```

The strict gap in (8) implies that for all sufficiently large `m`,

```text
U_m*U_(m+1)<=||x_m||^(1/50).                       (10)
```

Combining (7) and (10) proves Evertse admissibility (1) with the fixed data (2).

## Projective distinctness

The connector-free congruence gives

```text
U_(m+1)= +/- p_(i_(m+1,0)) (mod 64),
p in {5,30,20,56},
```

so `v_2(U_(m+1))` lies in `{0,1,2,3}`.

Compare the projective coordinate containing `2^(E_m)U_(m+1)` with the fixed `j=0` internal coordinate. Their ratio has 2-adic valuation

```text
E_m+v_2(U_(m+1))-v_2(b_(i_(m,0))),                (11)
```

which lies in `[E_m-3,E_m+3]`. But

```text
E_(m+1)-E_m=(8459/2)*2^m>6.                       (12)
```

The invariant (11) strictly increases with `m`. The admissible projective points are pairwise distinct.

## Conclusion

Every hypothetical cap or co-cap tail yields infinitely many distinct primitive, nondegenerate, `(1,1/50,{2,3})`-admissible projective zero sums. Evertse's theorem permits only finitely many. This contradiction is used in `T-9705`.

## Applicability audit

- There are 258 coordinates, hence `n=257`.
- Primitive normalization costs at most 216 and cannot add outside-`{2,3}` content.
- The load-bearing numerical gate is the **combined** endpoint exponent `6498/346819<1/50`.
- Proper subsums are ruled out by signs, not by sampled computation.
- Distinctness uses a projective ratio, so division by `g_m` is harmless.
- `X-9704` independently checks every elementary arithmetic gate. It does not prove Evertse's theorem.