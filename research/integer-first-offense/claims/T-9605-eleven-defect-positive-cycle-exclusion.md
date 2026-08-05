# T-9605 — Eleven non-neutral accelerated valuations cannot support a positive cycle

**Claim ID:** `T-9605`  
**Status:** `PROPOSED / EXACT FINITE CERTIFICATE`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** `L-9605`, `T-9604`; elementary accelerated affine algebra  
**Verification artifact:** `experiments/X-9609-eleven-defect-mitm/`

## 1. Statement

For an accelerated valuation word

\[
w=(a_0,\ldots,a_{k-1}),\qquad a_j\ge1,
\]

put

\[
D_w=2^A-3^k,
\qquad
E_w=C_w-D_w.
\]

The centered identity is

\[
\boxed{
E_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}(4-2^{a_j}).
}
\tag{1}
\]

Thus valuation `2` is exactly neutral. A nontrivial positive exact cycle requires

\[
\boxed{
D_w>0,\qquad D_w\mid E_w,\qquad E_w=(n_0-1)D_w\ge2D_w.
}
\tag{2}
\]

The proposed theorem is

\[
\boxed{
\text{No positive exact accelerated cycle word has exactly eleven letters different from }2.
}
\tag{3}
\]

Combined with `T-9601`--`T-9604`, every nontrivial positive accelerated Collatz cycle would therefore require at least twelve valuations different from `2`.

## 2. Largest-gap form

Rotate a hypothetical eleven-defect word as

\[
w=(b_0)(2)^{r_0}\cdots(b_{10})(2)^{r_{10}},
\qquad b_i\ne2.
\tag{4}
\]

Put

\[
B=\sum_i b_i,
\qquad
R=\sum_i r_i.
\]

Rotate a largest neutral gap to the terminal position:

\[
t=r_{10}=\max_i r_i,
\qquad
m=R-t,
\qquad
t\ge\lceil R/11\rceil.
\tag{5}
\]

Let `u` be the word with the terminal `(2)^t` deleted. Then

\[
D_R=2^B4^R-3^{11}3^R,
\qquad
E_w=3^tE_u.
\tag{6}
\]

Since `gcd(D_R,3)=1`, the cycle conditions force

\[
\boxed{D_R>0,\qquad D_R\mid E_u,\qquad E_u\ge2D_R.}
\tag{7}
\]

## 3. Complete contraction reduction

For `y=n-1>0`, one centered branch is

\[
g_a(y)=\frac{3y+4-2^a}{2^a}.
\tag{8}
\]

Deleting a neutral `2` or lowering a high valuation to a smaller value at least `3` increases every subsequent centered state. If the modified exceptional core is a strict contraction with fixed point below `2`, the original positive cycle is impossible.

The exact cyclic checks give the following complete residual list.

- Four or more high letters are impossible. Lowering all highs to `3`, the maximum of `E-2D` over every cyclic `{1,3}^{11}` class is already `-241076` at high count four and is smaller for every larger high count.
- With three highs, `(3,3,5)` has maximum cyclic margin `-147764`, while `(3,4,4)` has maximum `-251444`. Hence only the multisets `(3,3,3)` and `(3,3,4)` remain.
- With two highs, `(3,7)`, `(4,6)`, and `(5,5)` have maximum cyclic margins `-15572`, `-447700`, and `-663764`. Hence only
  \[
  (3,3),(3,4),(3,5),(3,6),(4,4),(4,5)
  \]
  remain.
- With one high, lowering every value at least `8` to `8` gives maximum margin `-79892`. Hence the lone high is one of `3,4,5,6,7`.

Together with the all-one case, the exact residual multisets are

```text
1^11;
1^10,3 through 1^10,7;
1^9,3,3; 1^9,3,4; 1^9,3,5; 1^9,3,6;
1^9,4,4; 1^9,4,5;
1^8,3,3,3; 1^8,3,3,4.
```

The finite certificate conservatively retains **all** arrangements of each residual multiset, including cyclic classes already removable by the sharper contraction test. This enlarges the searched set and cannot create a false exclusion.

## 4. Uniform infinite-gap cutoff

Suppose a residual type has `o` letters equal to `1` and total high valuation `H`. Discard every negative high contribution in `(1)` and move all neutral or high letters before the positive `1` letters. The adjacent move `(1,a)->(a,1)`, `a>=2`, multiplies the moved positive contribution by `2^a/3>1`. Therefore

\[
\boxed{
E_u\le 2^{H+1}(3^o-2^o)4^m.
}
\tag{9}
\]

Using `m<=R-ceil(R/11)`, direct exact substitution at `R=23` gives

\[
2^{H+1}(3^o-2^o)4^{R-\lceil R/11\rceil}<2D_R
\tag{10}
\]

for every residual type. The left side divided by `4^R` is nonincreasing, while `2D_R/4^R` is strictly increasing. Thus every `R>=23` is excluded at once.

No modulus above the finite range `0<=R<23` remains.

## 5. Exact normalized half-join

`L-9605` gives, for every split `w=uv`,

\[
E_w=3^{k_v}E_u+2^{A_u}E_v
\]

and hence

\[
\boxed{
D_w\mid E_w
\iff
E_u2^{-A_u}+E_v3^{-k_v}\equiv0\pmod{D_w}.
}
\tag{11}
\]

`X-9609` uses a `5+6` split. Its key also records the high-letter multiset used by the left half and the neutral-gap sum, so a modular match is possible only between genuinely complementary halves.

The exact packet covers all residual types and every finite row before `R=23`:

```text
finite rows                         258
full candidates represented          27,283,361,062
left normalized states                   84,513,178
right normalized states                 122,629,329
formal divisor hits                                0
nontrivial cycle hits                              0
```

The row digest is

```text
d1b2a4105d0f4bcf67d9e49584c202f77b022f67d0945079ebb04bb3735c62d8
```

A separately written reduced verifier uses a `6+5` split on every row that can pass the exact height test. It represents `188,604,494` full candidates and again obtains zero divisor hits. The omitted rows are certified impossible by the exact height program and the uniform bound `(10)`.

This contradicts `(7)` in every possible eleven-defect case and proves `(3)`. ∎

## 6. Scope boundary

- This is a finite positive-cycle exclusion, not a convergence theorem.
- Twelve or more non-neutral valuations remain open.
- The result does not exclude divergent nonperiodic trajectories.
- No positive cycle, divergent seed, sanctuary, or unconditional Collatz counterexample is claimed.

The next cycle offense should use the same normalized half-join at twelve defects rather than return to raw word enumeration.