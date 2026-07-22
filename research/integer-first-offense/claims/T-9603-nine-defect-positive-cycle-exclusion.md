# T-9603 — Nine non-neutral accelerated valuations cannot support a positive cycle

**Claim ID:** `T-9603`  
**Status:** `PROPOSED / EXACT FINITE CERTIFICATE`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** `T-9601`, `T-9602`; elementary accelerated affine algebra; independently extends PR #34 `L-9910`--`L-9913`  
**Scope:** positive accelerated `3n+1` cycles  
**Related counterexample candidates:** none

## 1. The centered certificate

For an accelerated valuation word

\[
w=(a_0,\ldots,a_{k-1}),\qquad a_j\ge1,
\]

put

\[
A_j=\sum_{i<j}a_i,
\qquad A=A_k,
\]

\[
C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
\qquad D_w=2^A-3^k,
\]

and center at the trivial fixed point:

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

A valuation `2` contributes exactly zero.

If `w` is a nontrivial positive accelerated cycle with initial state `n_0`, then

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
\text{No positive exact accelerated cycle word has exactly nine letters different from }2.
}
\]

Consequently, combining `T-9601`, `T-9602`, and the independently recorded exclusions through six defects,

\[
\boxed{
\text{every nontrivial positive accelerated Collatz cycle would require at least ten non-}2\text{ valuations.}
}
\]

This theorem excludes one complete finite-support layer. It does not construct a positive cycle or a divergent orbit.

## 3. Nine-defect compression and terminal neutral-gap removal

Assume a nine-defect cycle exists. Rotate it into the form

\[
\boxed{
w=(b_0)(2)^{r_0}(b_1)(2)^{r_1}\cdots
(b_8)(2)^{r_8},}
\tag{3}
\]

with

\[
b_i\ne2,
\qquad r_i\ge0.
\]

Every exceptional letter is `1` or at least `3`. Put

\[
B=\sum_{i=0}^{8}b_i,
\qquad
R=\sum_{i=0}^{8}r_i.
\]

Rotate a largest neutral gap to the end:

\[
t=r_8=\max_i r_i,
\qquad
m=R-t,
\qquad
t\ge\left\lceil{R\over9}\right\rceil.
\tag{4}
\]

Let `u` be `(3)` with the terminal `(2)^t` deleted. The full denominator is

\[
\boxed{
D_R=2^B4^R-3^9 3^R
=2^B4^R-19683\,3^R.
}
\tag{5}
\]

Appending a neutral `2` multiplies the centered defect by `3`, so

\[
E_w=3^tE_u.
\tag{6}
\]

Since `gcd(D_R,3)=1`, the cycle conditions `(2)` force

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

For `y=n-1>0`, one valuation branch is

\[
g_a(y)={3y+4-2^a\over2^a}.
\tag{8}
\]

Deleting a neutral `2` or lowering a high valuation to a smaller value at least `3` increases the replay. Every branch has positive slope. Therefore, if such a modified core is a strict contraction, its fixed point must be at least the original centered cycle state and hence at least `2`. In centered data this requires `E>=2D`.

### Four or more high letters

Delete all neutral letters and lower every high letter to `3`. The slope is

\[
{3^9\over2^{9+2h}}<1
\qquad(h\ge4).
\]

The exact maximum of `E-2D` over every cyclic `{1,3}` class is negative:

| high count `h` | cyclic classes | maximizing representative | `D` | `E` | max `E-2D` |
|---:|---:|:---|---:|---:|---:|
| 4 | 14 | `111333113` | 111389 | 1238 | -221540 |
| 5 | 14 | `113331313` | 504605 | -206242 | -1215452 |
| 6 | 10 | `113333313` | 2077469 | -1176994 | -5331932 |
| 7 | 4 | `133313333` | 8368925 | -6587734 | -23325584 |
| 8 | 1 | `133333333` | 33534749 | -26819926 | -93889424 |
| 9 | 1 | `333333333` | 134198045 | -107358436 | -375754526 |

Thus at most three exceptional letters are high.

### Three high letters

If any of the three high letters is at least `4`, lower the multiset to `(3,3,4)`. Its 28 cyclic classes contract; the largest centered margin is still

\[
E-2D=-65572
\]

at representative `111413113`, with `(D,E)=(45853,26134)`. Therefore all three highs must equal `3`.

For the ten cyclic classes of `1^6 3^3`, exactly three pass the contraction height test:

```text
111133113
111313113
113113113
```

Their respective values of `E-2D` are

```text
748, 4636, 10468.
```

All other triple classes are excluded. The finite table retains every rotation of these three classes.

### Two high letters

If both highs are at least `4`, lower to `(4,4)`. The four cyclic classes have maximum `E-2D=-5524`.

If one high is `3` and the other is at least `6`, lower to `(3,6)`. The eight cyclic classes have maximum `E-2D=-53908`.

Hence only `(3,3)`, `(3,4)`, and `(3,5)` remain. The `(3,5)` core is a contraction; among its eight cyclic classes only

```text
111151113
```

survives, with

\[
(D,E,E-2D)=(13085,37286,11116).
\]

All rotations of that sole surviving class are retained.

### One high letter

If the high valuation is at least `7`, lower it to `7`. The core `111111117` has

\[
(D,E,E-2D)=(13085,6086,-20084),
\]

so the high valuation can only be `3`, `4`, `5`, or `6`.

The complete residual type list is

\[
\boxed{
\begin{gathered}
1^9,
\quad1^8 3,
\quad1^8 4,
\quad1^8 5,
\quad1^8 6,\\
1^7 3^2,
\quad1^7 3\,4,
\quad1^7 3\,5\text{ in one cyclic class},\\
1^6 3^3\text{ in three cyclic classes}.
\end{gathered}}
\tag{9}
\]

## 5. Infinite neutral-gap ranges collapse

Letters `1` contribute positively to `(1)` and high letters contribute negatively. Discard every negative contribution and move all neutral or high letters before all `1`s. An adjacent move `(1,a)->(a,1)`, `a>=2`, multiplies the moved positive term by `2^a/3>1`.

If a residual type has `o` ones and total high valuation `H`, then

\[
\boxed{
E_u\le2^{H+1}(3^o-2^o)4^m.
}
\tag{10}
\]

Using `m<=R-ceil(R/9)`, the exact positivity and cutoff data are:

| type | `B` | coefficient in `(10)` | first `R` with `D_R>0` | first `R` excluded by `2D_R>E_u` |
|:---|---:|---:|---:|---:|
| `1^9` | 9 | 38342 | 13 | 19 |
| `1^8,3` | 11 | 100880 | 8 | 19 |
| `1^8,4` | 12 | 201760 | 6 | 19 |
| `1^8,5` | 13 | 403520 | 4 | 19 |
| `1^8,6` | 14 | 807040 | 1 | 19 |
| `1^7,3,3` | 13 | 263552 | 4 | 19 |
| `1^7,3,4` | 14 | 527104 | 1 | 19 |
| `1^7,3,5` | 15 | 1054208 | 0 | 19 |
| `1^6,3,3,3` | 15 | 680960 | 0 | 10 |

The first excluded rows are certified by:

| type | cutoff `R` | upper bound for `E_u` | `2D_R` |
|:---|---:|---:|---:|
| `1^9` | 19 | 164677636063232 | 235721391800734 |
| `1^8,3` | 19 | 433276300820480 | 1080146321932702 |
| `1^8,4` | 19 | 866552601640960 | 2206046228775326 |
| `1^8,5` | 19 | 1733105203281920 | 4457846042460574 |
| `1^8,6` | 19 | 3466210406563840 | 8961445669831070 |
| `1^7,3,3` | 19 | 1131947220795392 | 4457846042460574 |
| `1^7,3,4` | 19 | 2263894441590784 | 8961445669831070 |
| `1^7,3,5` | 19 | 4527788883181568 | 17968644924572062 |
| `1^6,3,3,3` | 10 | 44627394560 | 66394953802 |

The exclusion persists for every later `R`: `2D_R/4^R` is strictly increasing, whereas the normalized upper bound is nonincreasing.

## 6. Complete exact divisor certificate

Only 125 finite `(type,R)` rows remain. `X-9607` enumerates:

1. every weak composition `(r_0,...,r_8)` of `R` with `r_8=max_i r_i`;
2. every position of a lone high letter;
3. all positions of `(3,3)` and all ordered positions of `(3,4)`;
4. all rotations of the unique surviving `(3,5)` cyclic class;
5. all rotations of the three surviving `(3,3,3)` cyclic classes;
6. the exact core numerator `E_u` and divisibility `D_R|E_u` before the height sieve.

Tied largest gaps can duplicate words but cannot omit them. The exact aggregates are:

| type | rows | largest-gap candidates | height survivors | least nonzero circular remainder |
|:---|---:|---:|---:|---:|
| `1^9` | 6 | 593995 | 3954 | 36472 |
| `1^8,3` | 11 | 5716692 | 16938 | 134 |
| `1^8,4` | 13 | 5730246 | 3734 | 55 |
| `1^8,5` | 15 | 5733198 | 1712 | 748 |
| `1^8,6` | 18 | 5733621 | 1049 | 228 |
| `1^7,3,3` | 15 | 22932792 | 4945 | 195 |
| `1^7,3,4` | 18 | 45868968 | 4431 | 20 |
| `1^7,3,5` | 19 | 5733630 | 138 | 547 |
| `1^6,3,3,3` | 10 | 160041 | 87 | 748 |
| **total** | **125** | **98203183** | **36988** | -- |

There are zero formal divisor hits, even before the height filter. This contradicts `(7)` in every remaining row and proves the theorem. ∎

## 7. Independent exact implementations

The authoring program uses recursive weak compositions and the nine-term sparse centered sum. The independent verifier uses a separate enumeration and block-composition recurrence for the centered affine numerator.

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9607-nine-defect-cycle/run.cpp \
  -o /tmp/x9607

/tmp/x9607 > /tmp/x9607.json

diff -u \
  experiments/X-9607-nine-defect-cycle/results/canonical.json \
  /tmp/x9607.json

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9607-nine-defect-cycle/verify.cpp \
  -o /tmp/x9607-verify

/tmp/x9607-verify \
  experiments/X-9607-nine-defect-cycle/results/canonical.json
```

Frozen SHA-256 values:

```text
run.cpp
9ef1d1507fbe8158a6c2cb8bd7d9ed1f713661296273997c8077283cfa2ae6c8

verify.cpp
fdc10fa677d3f084d514a8f948897c6c4eaad3b9220eb926f8872f355dbd7e5c

canonical.json
e85ba1f4e6e60186764c176561bd3126725136dee278a95fa7239813247b6712
```

The authoring run completed in `3.77` seconds with peak RSS `3,584 KB`; the independent verifier completed in `4.08` seconds with peak RSS `3,956 KB` in the authoring container. These timings are informational only.

## 8. Boundary and next offense

- This theorem covers exactly nine non-`2` valuations with arbitrary neutral gaps and unbounded original high valuations through monotone reduction.
- Ten or more non-neutral valuations remain open.
- It does not exclude divergent nonperiodic trajectories.
- No positive cycle, divergent seed, sanctuary, or unconditional Collatz counterexample is claimed.

The ten-defect frontier is still finite after centered contraction, but its residual cyclic types grow. The correct next optimization is not raw word enumeration: precompute cyclic exceptional types by contraction margin, then use a modular or meet-in-the-middle join over the neutral-gap simplex.
