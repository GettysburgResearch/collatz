# T-8001 — No nontrivial positive accelerated cycle has exactly five non-2 valuations

**Claim ID:** `T-8001`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Scope:** positive accelerated `3n+1` valuation words containing exactly five letters different from `2`

## 1. Centered certificate

Let

\[
w=(a_0,\ldots,a_{k-1}),\qquad a_i\ge1,
\]

and put

\[
A_j=\sum_{i<j}a_i,
\qquad
A=A_k,
\]

\[
C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
\qquad
D_w=2^A-3^k.
\]

Center at the trivial fixed point `1`:

\[
E_w=C_w-D_w
   =\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}(4-2^{a_j}).
\tag{1}
\]

Every valuation `2` disappears from (1).

The word is a positive exact cycle certificate if and only if

\[
D_w>0,
\qquad
D_w\mid E_w.
\tag{2}
\]

Indeed `D|E` is equivalent to `D|C`.  If `n=C/D`, then `C` and `D` are odd,
so `n` is odd.  The rotated numerator identity

\[
C_{\operatorname{rot}(w)}={3C_w+D_w\over2^{a_0}}
\tag{3}
\]

shows inductively that every cyclic state is a positive odd integer and

\[
3n_j+1=2^{a_j}n_{j+1}.
\]

Hence every advertised valuation is exact.  Conversely an exact cycle gives
(2).

For a nontrivial positive certificate, every cyclic centered state

\[
y_j=n_j-1
\]

is a positive even integer.  In particular

\[
\boxed{y_j\ge2,
\qquad E_w\ge2D_w.}
\tag{4}
\]

The centered one-letter branch is

\[
g_a(y)={3y+4-2^a\over2^a},
\qquad g_2(y)={3y\over4}.
\tag{5}
\]

On positive states, deleting a neutral `2` strictly increases the replay, and
replacing any `a>=3` by a smaller `c>=3` also strictly increases it:

\[
g_c(y)-g_a(y)
=(3y+4)\left(2^{-c}-2^{-a}\right)>0.
\tag{6}
\]

## 2. Five exceptional letters

Assume for contradiction that a nontrivial positive cycle has exactly five
letters different from `2`.  Write those exceptional letters cyclically and
call a letter **high** when it is at least `3`.

### Case A — at least two high letters

Delete every neutral `2` and replace every high letter by `3`.  The modified
five-letter word `v` lies in `{1,3}^5` and contains `h>=2` high letters.  Its
slope is

\[
{3^5\over2^{5+2h}}
\le {243\over512}<1.
\tag{7}
\]

Choose a cyclic rotation of the exceptional sequence that minimizes the
modified fixed point.  The complete cyclic table is:

| high letters `h` | `D_v` | cyclic necklaces | largest, over necklaces, of the minimum rotated `E_v` | `2D_v` |
|---:|---:|---:|---:|---:|
| 2 | 269 | 2 | 62 | 538 |
| 3 | 1,805 | 2 | -1,174 | 3,610 |
| 4 | 7,949 | 1 | -6,262 | 15,898 |
| 5 | 32,525 | 1 | -26,020 | 65,050 |

`X-8003` independently reconstructs every rotation in this table.  In every
necklace one may choose a cut with

\[
{E_v\over D_v}<2.
\tag{8}
\]

At that same cut, the modified replay dominates the assumed positive cycle.
Since the modified affine map is a contraction, dominance after one full
turn implies

\[
y_0\le {E_v\over D_v}<2,
\]

contradicting (4).

### Case B — exactly one high letter

Let the high valuation be `b>=3`, and let the other four exceptional letters
be `1`.  Rotate a largest neutral gap to the terminal position and write

\[
w=(b_0)(2)^{r_0}(b_1)(2)^{r_1}(b_2)(2)^{r_2}
   (b_3)(2)^{r_3}(b_4)(2)^t,
\tag{9}
\]

where `(b_0,...,b_4)` is a permutation of `(b,1,1,1,1)`.  Put

\[
R=r_0+r_1+r_2+r_3+t,
\qquad
t\ge\lceil R/5\rceil,
\]

and let `u` be the word obtained by deleting the terminal `(2)^t`.
Neutral-tail centering gives

\[
E_w=3^tE_u,
\qquad
D_w\mid E_w\iff D_w\mid E_u,
\tag{10}
\]

because `gcd(D_w,3)=1`.

Drop the one negative high-letter contribution from (1).  Moving every
remaining valuation at least `2` before the four positive letters `1` can
only increase those positive terms.  If `m=R-t`, this gives

\[
\boxed{
E_u\le
2\,2^{b+2m}(3^3+2\cdot3^2+2^2\cdot3+2^3)
=130\,2^b4^m.}
\tag{11}
\]

The full denominator is

\[
D_w=16\,2^b4^R-243\,3^R.
\tag{12}
\]

For `R>=6`, use `b>=3` and `t>=2`:

\[
{2D_w\over2^b4^R}
=32-{486\over2^b}\left({3\over4}\right)^R
\ge 32-{243\over4}\left({3\over4}\right)^6
={347141\over16384}
>{130\over16}.
\tag{13}
\]

Together with (11), this gives `2D_w>E_u`, contradicting (4) and (10).

It remains to treat `0<=R<=5`.  Freeze a largest-tail gap tuple and the
position of the high letter.  For `x=2^b`, direct use of (1) gives

\[
E_u=Px+S,
\qquad
D_w=Lx-Q,
\tag{14}
\]

with

\[
L=16\,4^R,
\qquad Q=3^{R+5}.
\]

The determinant identity

\[
LE_u-PD_w=LS+PQ=:K
\tag{15}
\]

is independent of `b`.  Since `gcd(L,D_w)=1`,

\[
\boxed{D_w\mid E_u\iff D_w\mid K.}
\tag{16}
\]

If `K!=0`, every hit must satisfy

\[
2^b\le {|K|+Q\over L}.
\tag{17}
\]

`X-8003` exhausts all `345` canonical pattern/position pairs.  It finds:

- zero determinant resonances;
- `3,347` powers `2^b` under the exact cap (17);
- `53` rows passing `D>0` and `E_u>=2D`; and
- zero divisor hits.

The per-`R` certificate is:

| `R` | patterns | powers tested | largest `b` | height survivors | divisor hits |
|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 32 | 10 | 14 | 0 |
| 1 | 5 | 32 | 9 | 2 | 0 |
| 2 | 25 | 196 | 11 | 3 | 0 |
| 3 | 55 | 491 | 13 | 27 | 0 |
| 4 | 95 | 919 | 14 | 7 | 0 |
| 5 | 160 | 1,677 | 16 | 0 | 0 |

Thus the one-high case is impossible.

### Case C — all five exceptional letters are `1`

Let `R` again be the total number of neutral `2`s and rotate a largest gap
`t` to the terminal position.  Positive drift is equivalent to `R>=8`, since

\[
D_R=32\,4^R-243\,3^R
\tag{18}
\]

is negative at `R=7` and positive at `R=8`.

Deleting the terminal tail and moving all retained `2`s before the five `1`s
maximizes the centered numerator.  Hence

\[
E_u\le
2(3^5-2^5)4^{R-t}
=422\,4^{R-t}.
\tag{19}
\]

For `R>=10`, `t>=2` and

\[
{2D_R\over4^R}
=64-486\left({3\over4}\right)^R
\ge64-486\left({3\over4}\right)^{10}
>{422\over16}.
\tag{20}
\]

So `2D_R>E_u`, again impossible.

The only remaining totals are `R=8,9`.  `X-8003` checks all canonical
largest-tail arrangements:

| `R` | arrangements | height survivors | minimum `2D_R-E_u` |
|---:|---:|---:|---:|
| 8 | 120 | 0 | 254,024 |
| 9 | 170 | 0 | 4,825,304 |

This excludes the all-one case.

## 3. Conclusion

All possible configurations of five exceptional valuations have been
excluded.  Therefore

\[
\boxed{
\text{No nontrivial positive accelerated Collatz cycle has exactly five
valuations different from }2.}
\]

Combined with the separately proposed four-defect theorem on PR #34, this
moves the centered sparse-cycle frontier from four to five exceptional
valuations.  This claim itself proves only the exactly-five case.

## 4. Verification and boundary

Replay:

```bash
python3 -B experiments/X-8003-five-defect-cycle-exclusion/run.py \
  --check-results \
  experiments/X-8003-five-defect-cycle-exclusion/results/canonical.json

python3 -B experiments/X-8003-five-defect-cycle-exclusion/verify.py \
  experiments/X-8003-five-defect-cycle-exclusion/results/canonical.json
```

The build and verifier use different coefficient constructions for the
one-high determinant table.

The theorem does not address six or more exceptional valuations.  A bounded
six-defect scout in the session report found no candidate but exposed the
first new obstruction: two separated high letters can leave every shortened
`{1,3}` core with fixed point at least `2`, so the five-defect comparison no
longer closes automatically.
