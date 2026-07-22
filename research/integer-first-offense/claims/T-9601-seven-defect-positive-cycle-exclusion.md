# T-9601 — Seven non-neutral accelerated valuations cannot support a positive cycle

**Claim ID:** `T-9601`  
**Status:** `PROPOSED / EXACT FINITE CERTIFICATE`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-22  
**Dependencies:** elementary accelerated affine algebra; independently reconstructs and extends PR #34 `L-9910`, `L-9912`, and `L-9913`  
**Scope:** positive accelerated `3n+1` cycles  
**Related counterexample candidates:** none

## 1. Theorem

Let

\[
w=(a_0,\ldots,a_{k-1}),\qquad a_j\ge1,
\]

be an accelerated valuation word. Put

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

and center at the trivial fixed point `1`:

\[
E_w=C_w-D_w.
\]

Then

\[
\boxed{
E_w=
\sum_{j=0}^{k-1}
3^{k-1-j}2^{A_j}(4-2^{a_j}).
}
\tag{1}
\]

A valuation `2` contributes zero to `(1)`.

### Theorem

\[
\boxed{
\text{No positive exact accelerated cycle word has exactly seven letters different from }2.
}
\]

Consequently, combining this result with PR #34's proposed exclusions through six defects,

\[
\boxed{
\text{every nontrivial positive accelerated Collatz cycle would require at least eight non-}2\text{ valuations.}
}
\]

The conclusion is an exclusion theorem, not a counterexample construction.

## 2. Centered necessities

The branch represented by `w` sends

\[
1+y
\longmapsto
1+{3^k y+E_w\over2^A}.
\]

If `w` is a positive cycle with initial odd state `n_0`, then

\[
D_w n_0=C_w,
\]

and therefore

\[
\boxed{
E_w=(n_0-1)D_w.
}
\tag{2}
\]

For a nontrivial positive cycle, `n_0` is an odd integer at least `3`. Hence

\[
\boxed{
D_w>0,
\qquad
D_w\mid E_w,
\qquad
E_w\ge2D_w>0.
}
\tag{3}
\]

Only these necessary conditions are used below.

## 3. Seven-defect compression and the largest neutral gap

Assume a seven-defect cycle exists. Rotate it to write

\[
\boxed{
w=(b_0)(2)^{r_0}(b_1)(2)^{r_1}\cdots
(b_6)(2)^{r_6},}
\tag{4}
\]

where

\[
b_i\ne2,
\qquad
r_i\ge0.
\]

Every exceptional letter `b_i` is either `1` or at least `3`. Put

\[
B=\sum_{i=0}^6 b_i,
\qquad
R=\sum_{i=0}^6 r_i.
\]

Rotate a largest neutral gap to the terminal position:

\[
t=r_6=\max_i r_i,
\qquad
m=R-t,
\qquad
t\ge\left\lceil {R\over7}\right\rceil.
\tag{5}
\]

Let `u` be `(4)` with the terminal `(2)^t` removed. The full denominator is

\[
\boxed{
D_R=2^B4^R-3^7 3^R
=2^B4^R-2187\,3^R.
}
\tag{6}
\]

Appending one neutral `2` multiplies the centered defect by `3`, so

\[
E_w=3^tE_u.
\tag{7}
\]

As `gcd(D_R,3)=1`, conditions `(3)` imply the sharper core requirements

\[
\boxed{
D_R>0,
\qquad
D_R\mid E_u,
\qquad
E_u\ge2D_R.
}
\tag{8}
\]

The parity in the last condition is exact: `E_u` is even and `D_R` is odd, so a positive integer quotient `E_u/D_R` is at least `2`.

## 4. Centered contraction leaves only five exceptional types

For a centered state `y=n-1>0`, one advertised valuation acts by

\[
g_a(y)={3y+4-2^a\over2^a}.
\tag{9}
\]

Two monotone operations increase the replay:

1. delete a neutral branch `g_2(y)=3y/4<y`;
2. replace a high valuation `a` by `c` with `3\le c<a`, since
   \[
   g_c(y)-g_a(y)
   =(3y+4)(2^{-c}-2^{-a})>0.
   \]

All centered branches have positive slope. Therefore a modified core sends the original positive cycle state to at least itself. If that modified core is a strict contraction, its fixed point must be at least `2`; equivalently its centered numerator must satisfy `E\ge2D`.

The following exact finite classifications contradict that requirement.

### At least three high exceptional letters

Lower every high letter to `3` and delete all neutral letters. The slope is

\[
{3^7\over2^{7+2h}}<1
\qquad(h\ge3).
\]

The table records, over every cyclic `{1,3}` class, the **largest** possible value of `E-2D`. Every maximum is still negative.

| high count `h` | cyclic classes | maximizing representative | `D` | `E` | max `E-2D` |
|---:|---:|:---|---:|---:|---:|
| 3 | 5 | `1131313` | 6005 | -466 | -12476 |
| 4 | 5 | `1133313` | 30581 | -15634 | -76796 |
| 5 | 3 | `1331333` | 128885 | -98086 | -355856 |
| 6 | 1 | `1333333` | 522101 | -416806 | -1461008 |
| 7 | 1 | `3333333` | 2094965 | -1675972 | -5865902 |

Thus at most two exceptional letters are high.

### Two high exceptional letters

If one high letter is at least `4`, lower the high pair to `(3,4)`; if both are at least `4`, lower them to `(4,4)`. Both modified families contract. Exact cyclic enumeration gives:

| lowered pair | cyclic classes | maximizing representative | `D` | `E` | max `E-2D` |
|:---|---:|:---|---:|---:|---:|
| `(3,4)` | 6 | `1114113` | 1909 | 2278 | -1540 |
| `(4,4)` | 3 | `1114114` | 6005 | -1818 | -13828 |

Hence the only two-high possibility is exactly `(3,3)`.

### One high exceptional letter

If the high valuation is at least `6`, lower it to `6`. Up to rotation the modified core is

\[
(1,1,1,1,1,1,6),
\]

with

\[
D=1909,
\qquad
E=150,
\qquad
E-2D=-3668.
\]

Thus a lone high valuation can only be `3`, `4`, or `5`.

The complete surviving list is therefore

\[
\boxed{
1^7,
\quad1^6 3,
\quad1^6 4,
\quad1^6 5,
\quad1^5 3^2.
}
\tag{10}
\]

All cyclic positions of the high letters remain included.

## 5. Infinite neutral-gap ranges collapse

In `(1)`, letters `1` contribute positively and high letters contribute negatively. Discard every negative high contribution. Then move every retained neutral or high letter before every `1`.

An adjacent move `(1,a)\mapsto(a,1)` with `a\ge2` multiplies the moved positive term by `2^a/3>1`; all other positive terms are unchanged. Therefore, if a residual type has `o` letters `1` and total high valuation `H`,

\[
\boxed{
E_u\le2^{H+1}(3^o-2^o)4^m.
}
\tag{11}
\]

Using `m\le R-\lceil R/7\rceil`, the five types have the bounds below.

| type | `B` | positive coefficient in `(11)` | first `R` with `D_R>0` | first `R` excluded by `2D_R>E_u` |
|:---|---:|---:|---:|---:|
| `1^7` | 7 | 4118 | 10 | 15 |
| `1^6,3` | 9 | 10640 | 6 | 9 |
| `1^6,4` | 10 | 21280 | 3 | 8 |
| `1^6,5` | 11 | 42560 | 1 | 8 |
| `1^5,3,3` | 11 | 27008 | 1 | 8 |

The first excluded rows are certified exactly:

| type | first excluded `R` | upper bound for `E_u` | `2D_R` |
|:---|---:|---:|---:|
| `1^7` | 15 | 69088575488 | 212115787726 |
| `1^6,3` | 9 | 174325760 | 182342014 |
| `1^6,4` | 8 | 87162880 | 105519914 |
| `1^6,5` | 8 | 174325760 | 239737642 |
| `1^5,3,3` | 8 | 110624768 | 239737642 |

These inequalities persist at every later `R`, because

\[
{2D_R\over4^R}=2^{B+1}-4374(3/4)^R
\]

is strictly increasing, whereas the normalized right side of `(11)` is nonincreasing.

Only 27 finite `(type,R)` rows remain.

## 6. Complete exact divisor certificate

For each remaining row, `X-9605` performs the following finite enumeration:

1. enumerate every weak composition `(r_0,\ldots,r_6)` of `R` satisfying `r_6=max_i r_i`;
2. enumerate all seven positions of a lone high letter, or all 21 positions of the pair `(3,3)`;
3. form the core `u` by omitting the terminal largest gap;
4. compute `E_u` independently as both `C_u-D_u` and the sparse sum `(1)`;
5. test the exact divisor condition `D_R\mid E_u`, before applying the height sieve;
6. record the height survivors `E_u\ge2D_R` and their least circular nonzero remainder.

Tied largest gaps can duplicate a word but cannot omit one. The frozen packet contains:

| type | finite rows | largest-gap-normalized candidates | height survivors | least nonzero circular remainder |
|:---|---:|---:|---:|---:|
| `1^7` | 5 | 18111 | 547 | 30 |
| `1^6,3` | 3 | 7546 | 169 | 2837 |
| `1^6,4` | 5 | 4718 | 302 | 4 |
| `1^6,5` | 7 | 4774 | 124 | 72 |
| `1^5,3,3` | 7 | 14322 | 148 | 6 |
| **total** | **27** | **49471** | **1290** | -- |

There are

\[
\boxed{0}
\]

formal divisor hits, even before the height filter. This contradicts `(8)` in every remaining case and proves the theorem. ∎

## 7. Exact replay artifacts

Authoring computation:

```bash
python3 -B experiments/X-9605-seven-defect-cycle/run.py \
  --check-results \
  experiments/X-9605-seven-defect-cycle/results/canonical.json
```

Independent enumeration:

```bash
python3 -B experiments/X-9605-seven-defect-cycle/verify.py \
  experiments/X-9605-seven-defect-cycle/results/canonical.json
```

The two programs use different stars-and-bars generators and independent direct word construction. The authoring payload records

```text
semantic audit SHA-256:
9545aa4c7677d13f1ff47374f93bb3fc6dd3e01b9ca89312521466d556beebba

results payload SHA-256:
db9fdf0647d5111ee1dd2fb83fdcb41dbd03a29d9a4bd013493e9c803cdfc607
```

Source-file SHA-256 values from the authoring environment are recorded in the experiment README.

## 8. Boundary and next offense

- This theorem excludes exactly seven non-`2` valuations; it does not bound their neutral gaps by assumption.
- Valuation magnitudes are unbounded in the theorem; contraction reduces them to the five residual types.
- Eight or more non-`2` valuations remain open.
- The result does not exclude divergent orbits.
- No positive cycle, divergent seed, sanctuary, or unconditional Collatz counterexample is claimed.

The next finite-cycle target is the eight-defect frontier. The same centered architecture still applies, but the contraction boundary changes: two high valuations `(3,3)` already form a contraction at length eight, while one high valuation up to `6` and the all-one type survive. This may make the eight-defect classification no harder than the seven-defect case despite the larger gap simplex.
