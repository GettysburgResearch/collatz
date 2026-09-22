# T-9602 — Eight non-neutral accelerated valuations cannot support a positive cycle

**Claim ID:** `T-9602`  
**Status:** `PROPOSED / EXACT FINITE CERTIFICATE`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-22  
**Dependencies:** `T-9601`; elementary accelerated affine algebra; independently extends PR #34 `L-9910`, `L-9912`, and `L-9913`  
**Scope:** positive accelerated `3n+1` cycles  
**Related counterexample candidates:** none

## 1. Theorem

Let

\[
w=(a_0,\ldots,a_{k-1}),\qquad a_j\ge1,
\]

be an accelerated valuation word, and put

\[
A_j=\sum_{i<j}a_i,
\qquad
A=A_k,
\]

\[
C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
\qquad
D_w=2^A-3^k,
\]

\[
E_w=C_w-D_w.
\]

Centering at the trivial fixed point gives

\[
\boxed{
E_w=
\sum_{j=0}^{k-1}
3^{k-1-j}2^{A_j}(4-2^{a_j}).
}
\tag{1}
\]

Thus a valuation `2` is centered-neutral.

### Theorem

\[
\boxed{
\text{No positive exact accelerated cycle word has exactly eight letters different from }2.
}
\]

Together with the independently documented exclusions through seven defects,

\[
\boxed{
\text{every nontrivial positive accelerated Collatz cycle would require at least nine non-}2\text{ valuations.}
}
\]

This is an exclusion theorem. It does not construct a cycle or a divergent orbit.

## 2. Exact centered necessities

For a positive cycle with initial odd state `n_0`,

\[
D_wn_0=C_w,
\]

hence

\[
\boxed{E_w=(n_0-1)D_w.}
\tag{2}
\]

If the cycle is nontrivial, then `n_0>=3`, so

\[
\boxed{
D_w>0,
\qquad D_w\mid E_w,
\qquad E_w\ge2D_w>0.
}
\tag{3}
\]

These necessary conditions are the final certificate interface below.

## 3. Eight-defect compression

Assume for contradiction that there is an eight-defect cycle. Rotate it to write

\[
\boxed{
w=(b_0)(2)^{r_0}(b_1)(2)^{r_1}\cdots
(b_7)(2)^{r_7},}
\tag{4}
\]

where

\[
b_i\ne2,
\qquad r_i\ge0.
\]

Every exceptional letter `b_i` is `1` or at least `3`. Put

\[
B=\sum_{i=0}^7b_i,
\qquad
R=\sum_{i=0}^7r_i.
\]

Rotate a largest neutral gap to the terminal position:

\[
t=r_7=\max_i r_i,
\qquad
m=R-t,
\qquad
t\ge\left\lceil{R\over8}\right\rceil.
\tag{5}
\]

Let `u` be `(4)` with the terminal `(2)^t` deleted. The full denominator is

\[
\boxed{
D_R=2^B4^R-3^8 3^R
=2^B4^R-6561\,3^R.
}
\tag{6}
\]

A terminal neutral letter multiplies the centered defect by `3`, so

\[
E_w=3^tE_u.
\tag{7}
\]

Since `gcd(D_R,3)=1`, the conditions `(3)` imply

\[
\boxed{
D_R>0,
\qquad D_R\mid E_u,
\qquad E_u\ge2D_R.
}
\tag{8}
\]

The last inequality is exact: `E_u` is even and `D_R` is odd.

## 4. Centered contraction classification

For `y=n-1>0`, one accelerated branch is

\[
g_a(y)={3y+4-2^a\over2^a}.
\tag{9}
\]

Deleting `g_2(y)=3y/4<y` increases the replay. Replacing a high valuation `a` by a smaller `c>=3` also increases it, because

\[
g_c(y)-g_a(y)
=(3y+4)(2^{-c}-2^{-a})>0.
\tag{10}
\]

All branches have positive slope. Therefore any modified strict contraction maps the original cycle state to at least itself, so its fixed point must be at least `2`; equivalently its centered data must satisfy `E>=2D`.

### Three or more high letters

Delete all neutral letters and lower every high letter to `3`. For `h>=3` high letters, the slope is

\[
{3^8\over2^{8+2h}}<1.
\]

The table gives the maximum of `E-2D` over every cyclic `{1,3}` class. Each maximum is negative.

| high count `h` | cyclic classes | maximizing representative | `D` | `E` | max `E-2D` |
|---:|---:|:---|---:|---:|---:|
| 3 | 7 | `11133113` | 9823 | 6898 | -12748 |
| 4 | 10 | `13131313` | 58975 | -16850 | -134800 |
| 5 | 7 | `11333313` | 255583 | -141110 | -652276 |
| 6 | 4 | `13331333` | 1042015 | -797810 | -2881840 |
| 7 | 1 | `13333333` | 4187743 | -3347570 | -11723056 |
| 8 | 1 | `33333333` | 16770655 | -13416524 | -46957834 |

Hence at most two exceptional letters are high.

### Two high letters

If both high letters are at least `4`, lower them to `(4,4)`. If one high letter is `3` and the other is at least `5`, lower the pair to `(3,5)`. Both families contract, and exact cyclic enumeration gives:

| lowered pair | cyclic classes | maximizing representative | `D` | `E` | max `E-2D` |
|:---|---:|:---|---:|---:|---:|
| `(4,4)` | 4 | `11141114` | 9823 | 3762 | -15884 |
| `(3,5)` | 7 | `11115113` | 9823 | 5602 | -14044 |

Thus the only two-high residual pairs are `(3,3)` and `(3,4)`.

### One high letter

If the high valuation is at least `7`, lower it to `7`. The core

\[
(1,1,1,1,1,1,1,7)
\]

has

\[
D=9823,
\qquad E=-3518,
\qquad E-2D=-23164.
\]

Therefore a lone high valuation can only be `3`, `4`, `5`, or `6`.

The complete surviving type list is

\[
\boxed{
1^8,
\quad1^7 3,
\quad1^7 4,
\quad1^7 5,
\quad1^7 6,
\quad1^6 3^2,
\quad1^6 3\,4.
}
\tag{11}
\]

All cyclic placements of the high letters are retained.

## 5. Infinite neutral-gap ranges collapse

In `(1)`, letters `1` contribute positively and high letters contribute negatively. Discard the negative contributions, then move every neutral or high letter before all the `1`s. Each adjacent move `(1,a)->(a,1)`, `a>=2`, multiplies the moved positive term by `2^a/3>1` and leaves the other positive terms unchanged.

If a residual type has `o` ones and total high valuation `H`, this gives

\[
\boxed{
E_u\le2^{H+1}(3^o-2^o)4^m.
}
\tag{12}
\]

Together with `m<=R-ceil(R/8)`, the exact cutoffs are:

| type | `B` | coefficient in `(12)` | first `R` with `D_R>0` | first `R` excluded by `2D_R>E_u` |
|:---|---:|---:|---:|---:|
| `1^8` | 8 | 12610 | 12 | 17 |
| `1^7,3` | 10 | 32944 | 7 | 17 |
| `1^7,4` | 11 | 65888 | 5 | 17 |
| `1^7,5` | 12 | 131776 | 2 | 17 |
| `1^7,6` | 13 | 263552 | 0 | 17 |
| `1^6,3,3` | 12 | 85120 | 2 | 9 |
| `1^6,3,4` | 13 | 170240 | 0 | 9 |

The first excluded rows are:

| type | first excluded `R` | upper bound for `E_u` | `2D_R` |
|:---|---:|---:|---:|
| `1^8` | 17 | 3384971100160 | 7101515803322 |
| `1^7,3` | 17 | 8843337662464 | 33489794869946 |
| `1^7,4` | 17 | 17686675324928 | 68674166958778 |
| `1^7,5` | 17 | 35373350649856 | 139042911136442 |
| `1^7,6` | 17 | 70746701299712 | 279780399491770 |
| `1^6,3,3` | 9 | 1394606080 | 1889203322 |
| `1^6,3,4` | 9 | 2789212160 | 4036686970 |

They remain excluded for every later `R`: `2D_R/4^R=2^(B+1)-2*6561(3/4)^R` increases strictly, while the normalized upper bound decreases weakly.

## 6. Complete exact divisor certificate

Only 75 finite `(type,R)` rows remain. `X-9606` performs the following complete enumeration:

1. enumerate every weak composition `(r_0,...,r_7)` of `R` satisfying `r_7=max_i r_i`;
2. enumerate all eight positions of a lone high letter, all 28 positions of `(3,3)`, or all 56 ordered positions of `(3,4)`;
3. omit the terminal largest neutral gap and construct the core `u`;
4. compute `E_u` independently as `C_u-D_u` and from `(1)`;
5. test `D_R|E_u` before applying the height filter;
6. record all height survivors and their least circular nonzero remainder.

Ties among largest gaps can duplicate a word but cannot omit one. The frozen aggregates are:

| type | finite rows | largest-gap-normalized candidates | height survivors | least nonzero circular remainder |
|:---|---:|---:|---:|---:|
| `1^8` | 5 | 100006 | 158 | 1497644 |
| `1^7,3` | 10 | 894480 | 1911 | 726 |
| `1^7,4` | 12 | 898080 | 656 | 236 |
| `1^7,5` | 15 | 898944 | 514 | 102 |
| `1^7,6` | 17 | 898960 | 307 | 83 |
| `1^6,3,3` | 7 | 63140 | 1252 | 38 |
| `1^6,3,4` | 9 | 126392 | 756 | 10 |
| **total** | **75** | **3880002** | **5554** | -- |

There are zero formal divisor hits, even before the height filter. This contradicts `(8)` in every remaining case and proves the theorem. ∎

## 7. Exact replay

Authoring computation:

```bash
python3 -B experiments/X-9606-eight-defect-cycle/run.py \
  --check-results \
  experiments/X-9606-eight-defect-cycle/results/canonical.json
```

Independent enumeration:

```bash
python3 -B experiments/X-9606-eight-defect-cycle/verify.py \
  experiments/X-9606-eight-defect-cycle/results/canonical.json
```

The authoring payload records

```text
semantic audit SHA-256
658584e6034f43867a932b3fbbe3c9d13c5b0bc179299cda1d8aaf99461d89d9

canonical results payload SHA-256
bc9d50184da495c5ca6643ea47fecb68986fe5b0382e8243275004fbeff5bcd8
```

## 8. Boundary and next offense

- This theorem covers exactly eight non-`2` valuations, with arbitrary neutral gaps and unbounded original high valuations through the monotone reductions.
- Nine or more non-`2` valuations remain open.
- The result says nothing about divergent nonperiodic orbits.
- No positive cycle, divergent seed, sanctuary, or unconditional Collatz counterexample is claimed.

At nine defects the centered contraction boundary changes only modestly: exact triples `(3,3,3)`, pairs `(3,4)` and one cyclic `(3,5)` class survive, alongside the one-high families. The same finite-certificate architecture remains applicable, but the residual table is substantially larger.
