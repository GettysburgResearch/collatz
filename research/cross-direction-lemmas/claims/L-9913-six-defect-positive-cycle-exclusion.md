# L-9913 -- Exact exclusion at the six-defect positive-cycle frontier

Claim ID: `L-9913`
Title: Six non-neutral accelerated valuations cannot support a positive cycle
Status: `PROPOSED / EXACT FINITE CERTIFICATE`
Authoring agent: `gpt56-synthesis-01-wave22-h-sunit-transfer`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9904`, `L-9910`, and `L-9912`
Verification artifact: `../proofs/L-9913-six-defect-certificate.py`

## 1. Theorem

Use the standard accelerated-word quantities

\[
 C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
 \qquad D_w=2^A-3^k,
 \qquad E_w=C_w-D_w.
\tag{1}
\]

Then

\[
 E_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}(4-2^{a_j}),
\tag{2}
\]

so a valuation `2` contributes zero after centering at the fixed point `1`.

### Theorem -- six-defect exclusion

No positive exact accelerated cycle word has exactly six valuations different
from `2`.

Together with `L-9910` and `L-9912`, any nontrivial positive cycle would have
at least seven non-`2` valuations.

## 2. Compressed word and largest-gap test

Write a putative word cyclically as

\[
 w=(b_0)(2)^{r_0}\cdots(b_5)(2)^{r_5},
 \qquad b_i\ne2,
 \qquad r_i\ge0.
\tag{3}
\]

Put

\[
 B=\sum_i b_i,\qquad R=\sum_i r_i.
\tag{4}
\]

Every `b_i` is `1` or at least `3`.  Rotate a largest gap to the end and set

\[
 t=r_5=\max_i r_i,\qquad m=R-t,\qquad
 t\ge\left\lceil {R\over6}\right\rceil.
\tag{5}
\]

Let `u` be the word with the terminal `(2)^t` omitted.  The neutral-tail
identity gives

\[
 D_R=2^B4^R-729\,3^R,\qquad E_w=3^tE_u.
\tag{6}
\]

As `gcd(D_R,3)=1`, every positive exact certificate must satisfy

\[
 \boxed{D_R>0,\qquad D_R\mid E_u,\qquad E_u\ge2D_R.}
\tag{7}
\]

The last bound follows because `E_u` is even and `D_R` is odd.

We also use the centered branches

\[
 g_a(y)={3y+4-2^a\over2^a}.
\tag{8}
\]

For positive `y`, deleting `g_2(y)=3y/4` or lowering a high letter from `a`
to `c>=3` increases the replay.  Therefore, if the modified core is a strict
contraction and maps a cycle state `y_0>=2` to at least itself, its fixed
point must be at least `2`.

## 3. Contraction classification

Let `h` count the high exceptional letters `b_i>=3`.

### Three or more high letters

For `h>=3`, delete all neutral letters and lower every high letter to `3`.
The slope is

\[
 {3^6\over2^{6+2h}}<1.
\tag{9}
\]

The cyclic `{1,3}^6` cores are exhausted below.  Each displayed cyclic
representative has `E_v<2D_v`, contradicting the fixed-point necessity.

| `h` | representative `v` | `D_v` | `E_v` |
|---:|:---|---:|---:|
| 3 | `(1,1,1,3,3,3)` | 3367 | -2078 |
| 3 | `(1,1,3,1,3,3)` | 3367 | -1862 |
| 3 | `(1,1,3,3,1,3)` | 3367 | -1286 |
| 3 | `(1,3,1,3,1,3)` | 3367 | -962 |
| 4 | `(1,1,3,3,3,3)` | 15655 | -12038 |
| 4 | `(1,3,1,3,3,3)` | 15655 | -11714 |
| 4 | `(1,3,3,1,3,3)` | 15655 | -10850 |
| 5 | `(1,3,3,3,3,3)` | 64807 | -51554 |
| 6 | `(3,3,3,3,3,3)` | 261415 | -209132 |

### Exactly two high letters

If at least one of the two high letters is at least `4`, lower the pair to
`(3,4)` or `(4,4)`.  Up to cyclic rotation there are respectively five and
three placements.  Their selected representatives have the following
centered numerators:

| lowered pair | selected cyclic representatives | common `D_v` | all `E_v` |
|:---|:---|---:|:---|
| `(3,4)` | `111134, 111143, 111314, 111413, 113114` | 1319 | `-558, -430, -414, -94, -198` |
| `(4,4)` | `111144, 111414, 114114` | 3367 | `-2478, -2142, -1638` |

All modified cores contract and have fixed point below `2`.  Thus both high
letters must be `3`.  For the three cyclic placements of `(3,3)`, the
adjacent class has representative

\[
 v=(1,1,1,1,3,3),\qquad (D_v,E_v)=(295,466),
\tag{10}
\]

and is also excluded because `466<590`.  Only the two nonadjacent `(3,3)`
classes survive this contraction test.

### Exactly one high letter

If the high letter is `b>=5`, rotate it last and delete the neutral letters.
For `v=(1,1,1,1,1,b)`, direct evaluation gives

\[
 D_v=2^{b+5}-729,\qquad E_v=1394-2^{b+5},
\tag{11}
\]

and

\[
 E_v-2D_v=2852-3\,2^{b+5}\le-220.
\tag{12}
\]

The core contracts and its fixed point is below `2`.  Hence a lone high
letter can only be `3` or `4`.

The entire surviving classification is therefore

\[
 \boxed{
 (1^6),\quad (1^5,3),\quad(1^5,4),\quad
 (1^4,3,3)\text{ with nonadjacent threes}.}
\tag{13}
\]

## 4. Infinite gap ranges collapse

Move every neutral or high letter before all positive letters `1`, discarding
negative high contributions first.  The adjacent-swap calculation from
`L-9910` and `L-9912` gives the following upper bounds:

\[
\begin{array}{c|c|c}
\text{type}&B&E_u\text{ upper bound}\\ \hline
1^6&6&1330\,4^m\\
1^5,3&8&3376\,4^m\\
1^5,4&9&6752\,4^m\\
1^4,3,3&10&8320\,4^m.
\end{array}
\tag{14}
\]

For example, the first coefficient is

\[
 2(3^6-2^6)=1330.
\tag{15}
\]

The other three are obtained by moving the high valuation mass before the
remaining five or four ones.

The sign test

\[
 D_R>0\quad\Longleftrightarrow\quad
 (4/3)^R>{729\over2^B}
\tag{16}
\]

gives positivity from `R=9,4,2,0`, respectively.  Moreover

\[
 {2D_R\over4^R}=2^{B+1}-1458(3/4)^R
\tag{17}
\]

is strictly increasing, whereas the normalized bounds in (14), using
`t>=ceil(R/6)`, are nonincreasing.  The first strictly excluded rows are:

| type | first excluded `R` | upper bound `E_u` | `2D_R` | margin |
|:---|---:|---:|---:|---:|
| `1^6` | 13 | 1394606080 | 6265411658 | 4870805578 |
| `1^5,3` | 7 | 3457024 | 5199962 | 1742938 |
| `1^5,4` | 7 | 6914048 | 13588570 | 6674522 |
| `1^4,3,3` | 7 | 8519680 | 30365786 | 21846106 |

Thus only the finite rows in the next section remain.

## 5. Complete exact divisor table

For each residual `R`, enumerate all weak compositions
`(r_0,...,r_5)` with `r_5=max_i r_i`.  Enumerate all six positions of a lone
high letter and, conservatively, all fifteen positions of the pair `(3,3)`.
This includes the already excluded adjacent pair and avoids any hidden
orientation convention.

In the table, `N` is the number of canonical candidates, `M=max E_u`, `H`
counts candidates with `E_u>=2D_R`, and `rho` is the least circular nonzero
remainder among the height survivors.  A dash means `H=0`.

| type | `R` | `D_R` | `N` | `M` | `H` | `rho` |
|:---|---:|---:|---:|---:|---:|---:|
| `1^6` | 9 | 2428309 | 412 | 8206498 | 30 | 85987 |
| `1^6` | 10 | 24062143 | 607 | 27240934 | 0 | -- |
| `1^6` | 11 | 139295293 | 872 | 85917106 | 0 | -- |
| `1^6` | 12 | 686321335 | 1223 | 274528534 | 0 | -- |
| `1^5,3` | 4 | 6487 | 186 | 139708 | 130 | 2 |
| `1^5,3` | 5 | 84997 | 336 | 460084 | 20 | 1776 |
| `1^5,3` | 6 | 517135 | 612 | 1445788 | 2 | 105617 |
| `1^5,4` | 2 | 1631 | 36 | 18260 | 25 | 55 |
| `1^5,4` | 3 | 13085 | 96 | 71420 | 26 | 216 |
| `1^5,4` | 4 | 72023 | 186 | 253172 | 15 | 2065 |
| `1^5,4` | 5 | 347141 | 336 | 841436 | 3 | 42706 |
| `1^5,4` | 6 | 1565711 | 612 | 2655380 | 0 | -- |
| `1^4,3,3` | 0 | 295 | 15 | 4756 | 14 | 16 |
| `1^4,3,3` | 1 | 1909 | 15 | 4756 | 1 | 938 |
| `1^4,3,3` | 2 | 9823 | 90 | 22588 | 2 | 350 |
| `1^4,3,3` | 3 | 45853 | 240 | 93268 | 1 | 1562 |
| `1^4,3,3` | 4 | 203095 | 465 | 357628 | 0 | -- |
| `1^4,3,3` | 5 | 871429 | 840 | 1236724 | 0 | -- |
| `1^4,3,3` | 6 | 3662863 | 1530 | 3972316 | 0 | -- |

Every `rho` is positive.  In fact the checker also tests divisibility before
the height sieve and finds no formal divisor hit at all.  This contradicts
(7) in every surviving case and proves the theorem. **QED**

## 6. Exact certificate and adversarial audit

Run

```text
python research/cross-direction-lemmas/proofs/L-9913-six-defect-certificate.py
```

The checker uses integer arithmetic only.  It independently evaluates both
`E=C-D` and the sparse sum (2), generates every largest-gap composition,
recomputes the contraction and cutoff tables, and asserts that the complete
divisor-hit list is empty.

Its dormant hit path reconstructs

\[
 n_0=1+{E_w\over D_w},
\tag{18}
\]

then checks every exact valuation, positivity, return, and first return time.
By `L-9910`, any six-defect positive hit would automatically be primitive:
a proper first-return block would have at most three defects.  The replay
audit is retained anyway, so a powered or formal hit cannot pass silently.

## Strongest conclusion

> Monotone centered contraction reduces every six-exception word to four
> low-high types.  Largest-gap height bounds make all four finite, and exact
> divisibility rejects every remaining candidate.  Any nontrivial positive
> accelerated Collatz cycle therefore requires at least seven valuations
> different from two.
