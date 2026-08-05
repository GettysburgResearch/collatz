# T-9604 — Ten non-neutral accelerated valuations cannot support a positive cycle

**Claim ID:** `T-9604`  
**Status:** `PROPOSED / EXACT MITM CERTIFICATE`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** `L-9605`, `T-9601`--`T-9603`; elementary centered affine algebra  
**Scope:** positive accelerated `3n+1` cycles  
**Related counterexample candidates:** none

## 1. Centered certificate

For an accelerated valuation word

\[
w=(a_0,\ldots,a_{k-1}),
\qquad a_j\ge1,
\]

put

\[
A_j=\sum_{i<j}a_i,
\quad A=A_k,
\quad
C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
\quad
D_w=2^A-3^k.
\]

Center at the trivial fixed point `1`:

\[
E_w=C_w-D_w.
\]

Then

\[
\boxed{
E_w=
\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}(4-2^{a_j}).
}
\tag{1}
\]

A valuation `2` contributes zero. If `w` is a nontrivial positive exact cycle with initial odd state `n_0`, then

\[
\boxed{
E_w=(n_0-1)D_w,
\qquad
D_w>0,
\qquad
D_w\mid E_w,
\qquad
E_w\ge2D_w.
}
\tag{2}
\]

## 2. Theorem

\[
\boxed{
\text{No positive exact accelerated cycle word has exactly ten letters different from }2.
}
\]

Together with the proposed exact-certificate exclusions through nine defects,

\[
\boxed{
\text{every nontrivial positive accelerated Collatz cycle would require at least eleven non-}2\text{ valuations.}
}
\]

This is a complete exclusion of one support layer. It is not a construction of a cycle or divergent orbit.

## 3. Largest neutral gap

Assume a ten-defect cycle exists and rotate it as

\[
\boxed{
w=(b_0)(2)^{r_0}\cdots(b_9)(2)^{r_9},}
\tag{3}
\]

where

\[
b_i\ne2,
\qquad r_i\ge0.
\]

Every `b_i` is `1` or at least `3`. Put

\[
B=\sum_{i=0}^{9}b_i,
\qquad
R=\sum_{i=0}^{9}r_i.
\]

Rotate a largest neutral gap to the terminal position:

\[
t=r_9=\max_i r_i,
\qquad
m=R-t,
\qquad
t\ge\left\lceil{R\over10}\right\rceil.
\tag{4}
\]

Let `u` be `(3)` with the terminal `(2)^t` removed. The full denominator is

\[
\boxed{
D_R=2^B4^R-3^{10}3^R
=2^B4^R-59049\,3^R.
}
\tag{5}
\]

A terminal neutral letter multiplies the centered defect by `3`, so

\[
E_w=3^tE_u.
\tag{6}
\]

Since `gcd(D_R,3)=1`, every positive cycle must satisfy

\[
\boxed{
D_R>0,
\qquad
D_R\mid E_u,
\qquad
E_u\ge2D_R.
}
\tag{7}
\]

## 4. Centered contraction classification

On a centered state `y=n-1>0`, one valuation acts by

\[
g_a(y)={3y+4-2^a\over2^a}.
\tag{8}
\]

Deleting a neutral `2` increases the replay, because `g_2(y)=3y/4<y`. Lowering a high valuation `a` to `c`, with `3<=c<a`, also increases it:

\[
g_c(y)-g_a(y)
=(3y+4)(2^{-c}-2^{-a})>0.
\tag{9}
\]

Every branch has positive slope. Therefore a modified strict contraction must have centered fixed point at least the original cycle state and hence at least `2`; in centered data it must satisfy `E>=2D`.

### Four or more high letters

Delete all neutral letters and lower every high letter to `3`. For `h>=4`, the slope

\[
{3^{10}\over2^{10+2h}}
\]

is less than one. Exact cyclic classification gives:

| high count `h` | cyclic classes | maximizing representative | `D` | `E` | max `E-2D` |
|---:|---:|:---|---:|---:|---:|
| 4 | 22 | `1113313113` | 203095 | 84610 | -321580 |
| 5 | 26 | `1113333113` | 989527 | -151934 | -2130988 |
| 6 | 22 | `1133331313` | 4135255 | -1794278 | -10064788 |
| 7 | 12 | `1133333313` | 16718167 | -9560294 | -42996628 |
| 8 | 5 | `1333313333` | 67049815 | -52819970 | -186919600 |
| 9 | 1 | `1333333333` | 268376407 | -214677506 | -751430320 |
| 10 | 1 | `3333333333` | 1073682775 | -858946220 | -3006311770 |

Every maximum is negative. Hence at most three exceptional letters are high.

### Three high letters

The all-`3` multiset has twelve cyclic classes and is retained. If at least one high valuation is at least `4`, lower to `(3,3,4)`. Its 36 cyclic classes are strict contractions, with maximum

\[
E-2D=-10940
\]

at representative `1111431113`, where `(D,E)=(72023,133106)`. Thus the only three-high residual type is

\[
1^7 3^3.
\]

### Two high letters

If one high is `3` and the other is at least `6`, lower to `(3,6)`. Its nine cyclic classes have maximum

\[
E-2D=-29084.
\]

If both highs are at least `4` and one is at least `5`, lower to `(4,5)`. Its nine cyclic classes have maximum

\[
E-2D=-95644.
\]

The residual pair types are therefore

\[
(3,3),
\quad(3,4),
\quad(3,5),
\quad(4,4).
\]

### One high letter

If the high valuation is at least `8`, lower it to `8` and rotate it last. The modified core `1^9 8` has

\[
(D,E,E-2D)=(72023,-13998,-158044).
\]

Hence a lone high valuation can only be `3,4,5,6,7`.

The complete residual list is

\[
\boxed{
\begin{gathered}
1^{10},\\
1^9 3,
1^9 4,
1^9 5,
1^9 6,
1^9 7,\\
1^8 3^2,
1^8 3\,4,
1^8 3\,5,
1^8 4^2,\\
1^7 3^3.
\end{gathered}}
\tag{10}
\]

All cyclic placements are retained.

## 5. Infinite neutral-gap cutoff

In `(1)`, letters `1` contribute positively and high letters negatively. Discard every negative high contribution, then move every neutral or high letter before all `1`s. Each adjacent move `(1,a)->(a,1)`, `a>=2`, multiplies the moved positive term by `2^a/3>1`.

If a residual type has `o` ones and total high valuation `H`, then

\[
\boxed{
E_u\le2^{H+1}(3^o-2^o)4^m.
}
\tag{11}
\]

Using `m<=R-ceil(R/10)`, the exact ranges are:

| type | `B` | coefficient in `(11)` | first `R` with `D_R>0` | first `R` excluded by `2D_R>E_u` |
|:---|---:|---:|---:|---:|
| `1^10` | 10 | 116050 | 15 | 22 |
| `1^9,3` | 12 | 306736 | 10 | 21 |
| `1^9,4` | 13 | 613472 | 7 | 21 |
| `1^9,5` | 14 | 1226944 | 5 | 21 |
| `1^9,6` | 15 | 2453888 | 3 | 21 |
| `1^9,7` | 16 | 4907776 | 0 | 21 |
| `1^8,3,3` | 14 | 807040 | 5 | 21 |
| `1^8,3,4` | 15 | 1614080 | 3 | 21 |
| `1^8,3,5` | 16 | 3228160 | 0 | 21 |
| `1^8,4,4` | 16 | 3228160 | 0 | 21 |
| `1^7,3,3,3` | 16 | 2108416 | 0 | 21 |

The first excluded rows satisfy:

| type | cutoff `R` | upper bound for `E_u` | `2D_R` |
|:---|---:|---:|---:|
| `1^10` | 22 | 31899581100851200 | 32322756641260286 |
| `1^9,3` | 21 | 21078737416093696 | 34793450226396074 |
| `1^9,4` | 21 | 42157474832187392 | 70822247245360042 |
| `1^9,5` | 21 | 84314949664374784 | 142879841283287978 |
| `1^9,6` | 21 | 168629899328749568 | 286995029359143850 |
| `1^9,7` | 21 | 337259798657499136 | 575225405510855594 |
| `1^8,3,3` | 21 | 55459366505021440 | 142879841283287978 |
| `1^8,3,4` | 21 | 110918733010042880 | 286995029359143850 |
| `1^8,3,5` | 21 | 221837466020085760 | 575225405510855594 |
| `1^8,4,4` | 21 | 221837466020085760 | 575225405510855594 |
| `1^7,3,3,3` | 21 | 144889244261810176 | 575225405510855594 |

The exclusion persists at every later `R`, because `2D_R/4^R` increases and the normalized upper bound is nonincreasing.

## 6. Exact normalized half-join certificate

Only 184 finite `(type,R)` rows remain. A direct expansion would contain

\[
\boxed{1,623,353,430}
\]

largest-gap-normalized words.

`X-9608` applies `L-9605`. For every terminal largest gap, it splits the ten exceptional blocks `5+5`, stores

\[
E_L2^{-A_L}\pmod D,
\]

and joins against

\[
-E_R3^{-k_R}\pmod D
\]

with complementary exceptional multiset and neutral-gap sum.

The exact aggregate coverage is:

| type | rows | covered candidates | left states | right states |
|:---|---:|---:|---:|---:|
| `1^10` | 7 | 5130175 | 203369 | 57575 |
| `1^9,3` | 11 | 36647600 | 1012836 | 305652 |
| `1^9,4` | 14 | 36768470 | 1025484 | 311784 |
| `1^9,5` | 16 | 36779440 | 1027416 | 312924 |
| `1^9,6` | 18 | 36781290 | 1027878 | 313242 |
| `1^9,7` | 21 | 36781410 | 1027932 | 313290 |
| `1^8,3,3` | 16 | 165507480 | 2739776 | 834464 |
| `1^8,3,4` | 18 | 331031610 | 5310703 | 1618417 |
| `1^8,3,5` | 21 | 331032690 | 5310982 | 1618665 |
| `1^8,4,4` | 21 | 165516345 | 2741152 | 835440 |
| `1^7,3,3,3` | 21 | 441376920 | 4454372 | 1357590 |
| **total** | **184** | **1623353430** | **25881900** | **7879043** |

There are zero normalized joins and therefore zero divisor hits.

A separately written verifier uses a `4+6` split, different half-pattern collections, and a different gap decomposition. It independently obtains the same row candidate counts and zero hits. This contradicts `(7)` in every remaining row and proves the theorem. ∎

## 7. Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9608-ten-defect-mitm/run.cpp \
  -o /tmp/x9608

/tmp/x9608 > /tmp/x9608.json

diff -u \
  experiments/X-9608-ten-defect-mitm/results/canonical.json \
  /tmp/x9608.json

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9608-ten-defect-mitm/verify.cpp \
  -o /tmp/x9608-verify

/tmp/x9608-verify
```

Frozen digests:

```text
run.cpp SHA-256
2f07ed7ae0467f89b844087d893df79ec2cd6dba4e71e5429c5dfcd8545f1d07

verify.cpp SHA-256
7fbe8b49ce45eaf66f3867597e38b9bb88a47438438bf28dc4a206f1b5994a3a

canonical.json SHA-256
7daad798a10f6c68db81064a5014f0214392be3d422b58771ab5b6a7b8d82545

5+5 row FNV-1a-64
776c0a3b4ace3abc

split-independent candidate FNV-1a-64
8b0ed2d5d2377bda
```

In the authoring environment, the `5+5` run completed in approximately `5.1` seconds and the independent `4+6` verifier in approximately `5.4` seconds. Timings are informational only.

## 8. Boundary

- This theorem covers exactly ten valuations different from `2`, with arbitrary neutral gaps and unbounded original high valuations through monotone reduction.
- Eleven or more non-neutral valuations remain open.
- It says nothing about divergent nonperiodic trajectories.
- No positive cycle, divergent seed, sanctuary, or unconditional Collatz counterexample is claimed.

At eleven defects the raw finite family is larger, but `L-9605` changes the asymptotic computation from full-word enumeration to a join of two bounded-gap half-state sets. The next attack should combine that exact join with modular factor sieves before increasing the residual exceptional-language width.
