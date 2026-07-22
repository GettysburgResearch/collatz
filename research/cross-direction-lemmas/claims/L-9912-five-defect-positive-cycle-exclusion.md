# L-9912 -- Exact exclusion at the five-defect positive-cycle frontier

Claim ID: `L-9912`
Title: Five non-neutral accelerated valuations cannot support a positive cycle
Status: `PROPOSED / EXACT FINITE CERTIFICATE`
Authoring agent: `gpt56-synthesis-01-wave22-h-sunit-transfer`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9904` (complete divisibility-to-replay theorem) and
local `L-9910` (centered defect, neutral-tail collapse, and four-defect
exclusion)
Verification artifact:
`../proofs/L-9912-five-defect-certificate.py`

## 1. Result

For an accelerated valuation word

\[
 w=(a_0,\ldots,a_{k-1}),\qquad a_j\ge1,
\tag{1}
\]

put

\[
 A_j=\sum_{i<j}a_i,\quad A=A_k,\quad
 C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
\tag{2}
\]

\[
 D_w=2^A-3^k,\qquad E_w=C_w-D_w.
\tag{3}
\]

The letter `2` is centered-neutral: with `y=n-1`, its branch is

\[
 g_2(y)={3y\over4}<y\qquad(y>0),
\tag{4}
\]

and its contribution to the sparse identity

\[
 E_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}(4-2^{a_j})
\tag{5}
\]

vanishes.

### Theorem -- five-defect exclusion

No positive exact accelerated cycle word has exactly five letters different
from `2`.

Combined with `L-9910`, every nontrivial positive accelerated cycle would
therefore have at least six non-`2` valuations.

The proof is a complete classification.  Most cases die by centered
contraction.  The remaining three letter types reduce, after rotating a
largest neutral gap to the end, to ten finite rows of exact integer
arithmetic.  None has a divisor hit.

## 2. Compressed form and two inherited necessities

Assume for contradiction that a five-defect cycle exists.  Rotate it to an
exceptional letter and write

\[
 \boxed{
 w=(b_0)(2)^{r_0}(b_1)(2)^{r_1}(b_2)(2)^{r_2}
   (b_3)(2)^{r_3}(b_4)(2)^{r_4},}
\tag{6}
\]

where

\[
 b_i\ne2,\qquad r_i\ge0.
\tag{7}
\]

Every `b_i` is either `1` or at least `3`.  Put

\[
 B=\sum_{i=0}^4b_i,\qquad R=\sum_{i=0}^4r_i.
\tag{8}
\]

Because the cycle is nontrivial, every centered state on every cyclic cut is
a positive even integer:

\[
 y=n-1\ge2.
\tag{9}
\]

For `a>=3`, lowering a high letter increases its centered branch:

\[
 g_c(y)-g_a(y)
 =(3y+4)\left(2^{-c}-2^{-a}\right)>0
 \quad(3\le c<a,\ y>0).
\tag{10}
\]

Deleting a neutral `2` also increases the replay, by (4).  Since every
centered branch has positive slope, any word obtained through these two
modifications maps the original positive cycle state to a value at least as
large as that state.

There is a second reduction that will handle the low cases.  Rotate a
largest neutral gap to the terminal position and put

\[
 t=r_4=\max_i r_i,\qquad m=R-t,
\tag{11}
\]

so in particular

\[
 t\ge\left\lceil {R\over5}\right\rceil.
\tag{12}
\]

Let `u` be (6) with its terminal `(2)^t` removed.  Its full denominator is

\[
 \boxed{D_R=2^B4^R-243\,3^R.}
\tag{13}
\]

The neutral-tail identity of `L-9910` gives

\[
 E_w=3^tE_u,\qquad \gcd(D_R,3)=1.
\tag{14}
\]

Thus a positive exact certificate requires

\[
 \boxed{D_R>0,\qquad D_R\mid E_u,\qquad E_u\ge2D_R.}
\tag{15}
\]

The last inequality is exact, not merely Archimedean: `D_R` is odd and
`E_u` is even, so a positive integer quotient `E_u/D_R` is at least two.

## 3. Two sharp positive-part bounds

We need only two elementary maximizations.

### Lemma 1 -- all five exceptional letters are one

If every `b_i=1`, then

\[
 \boxed{E_u\le422\,4^m.}
\tag{16}
\]

### Lemma 2 -- one high letter and four ones

If one exceptional letter is `b>=3` and the other four are `1`, then

\[
 \boxed{E_u\le130\,2^b4^m.}
\tag{17}
\]

### Proof

In (5), a letter `1` contributes positively and every high letter
contributes negatively.  Swap an adjacent pair `(1,a)` to `(a,1)`, where
`a>=2`.  The moved positive contribution gains `2^a` from its prefix and
loses `3` from its suffix, so it is multiplied by `2^a/3>1`; every other
positive contribution is unchanged.

For Lemma 1, move all `m` neutral letters before all five ones.  The resulting
positive sum is

\[
 2\,4^m(3^4+2\cdot3^3+2^2\cdot3^2+2^3\cdot3+2^4)
 =422\,4^m.
\tag{18}
\]

For Lemma 2, first discard the one negative high contribution, then move the
high letter and all neutral letters before the four ones.  Their positive sum
is

\[
 2\,2^b4^m(3^3+2\cdot3^2+2^2\cdot3+2^3)
 =130\,2^b4^m.
\tag{19}
\]

Discarding the negative term only enlarges the numerator, so both are valid
upper bounds. **QED**

## 4. At least two high letters: centered contraction

Let `h` be the number of exceptional letters at least three.  Suppose first
that `h>=2`.  Delete every neutral `2` and replace every high letter by `3`.
The resulting five-letter word `v` lies in `{1,3}^5`, has slope

\[
 {3^5\over2^{5+2h}}<1,
\tag{20}
\]

and maps the original state `y_0` to at least `y_0`.  Therefore its fixed
point must satisfy

\[
 {E_v\over D_v}\ge y_0\ge2.
\tag{21}
\]

Up to cyclic rotation, the positions of the high letters give only the six
rows below.  The displayed representative is a permitted cyclic rotation
chosen to make the contradiction immediate.  Direct substitution in (5)
gives every integer.

| `h` | cyclic class representative `v` | `D_v` | `E_v` | `E_v-2D_v` |
|---:|:---|---:|---:|---:|
| 2 | `(1,1,1,3,3)` | 269 | -10 | -548 |
| 2 | `(1,1,3,1,3)` | 269 | 62 | -476 |
| 3 | `(1,1,3,3,3)` | 1805 | -1282 | -4892 |
| 3 | `(1,3,1,3,3)` | 1805 | -1174 | -4784 |
| 4 | `(1,3,3,3,3)` | 7949 | -6262 | -22160 |
| 5 | `(3,3,3,3,3)` | 32525 | -26020 | -91070 |

Every row has `E_v/D_v<2`, contradicting (21).  Hence

\[
 \boxed{h\le1.}
\tag{22}
\]

## 5. One high letter at least five

Suppose `h=1`, and call the high letter `b`.  If `b>=5`, rotate the
exceptional sequence to

\[
 v=(1,1,1,1,b)
\tag{23}
\]

and delete every neutral `2`.  The core is a contraction, and (5) gives

\[
 D_v=2^{b+4}-243>0,
 \qquad
 E_v=454-2^{b+4}<0.
\tag{24}
\]

As before its fixed point would have to dominate the original positive
state, whereas (24) makes that fixed point negative.  Thus the only
one-high cases left are

\[
 \boxed{b=3\quad\hbox{or}\quad b=4.}
\tag{25}
\]

## 6. Largest-gap cutoff in the three residual types

There are now only three types:

1. five ones, with `B=5`;
2. four ones and one `3`, with `B=7`;
3. four ones and one `4`, with `B=8`.

The sign test

\[
 D_R>0\quad\Longleftrightarrow\quad
 (4/3)^R>{243\over2^B}
\tag{26}
\]

is monotone in `R`, while the recurrence

\[
 D_{R+1}=4D_R+243\,3^R
\tag{27}
\]

shows that `D_R` stays positive once it becomes positive.  Exact evaluation
gives the respective positivity ranges

\[
 R\ge8,\qquad R\ge3,\qquad R\ge0.
\tag{28}
\]

For fixed `B`, the normalized height

\[
 {2D_R\over4^R}=2^{B+1}-486(3/4)^R
\tag{29}
\]

is strictly increasing.  Meanwhile (12), (16), and (17) make the normalized
upper bound for `E_u` nonincreasing.  It is therefore enough to check the
first row of each infinite range below:

| type | first eliminated `R` | upper bound for `E_u` | `2D_R` | strict margin |
|:---|---:|---:|---:|---:|
| five `1`s | 9 | `422*4^7 = 6914048` | 7211278 | 297230 |
| one `3` | 6 | `1040*4^4 = 266240` | 694282 | 428042 |
| one `4` | 6 | `2080*4^4 = 532480` | 1742858 | 1210378 |

Thus (15) fails for all `R>=9` in the all-one case and for all `R>=6` in
both one-high cases.

## 7. Complete exact finite table

Only ten values of `(type,R)` remain.  Their enumeration is canonical and
small:

1. list all five-tuples `(r_0,...,r_4)` of nonnegative integers summing to
   `R` with `r_4=max_i r_i`;
2. in a one-high row, put the high letter in each of the five exceptional
   positions;
3. form the core `u` by omitting the terminal `r_4` copies of `2`;
4. test the exact conditions `E_u>=2D_R` and `E_u mod D_R=0`.

Every cyclic gap pattern is covered because at least one largest gap can be
rotated to the terminal position.  Ties merely duplicate a word and cannot
omit one.

In the table, `N` is the number of canonical candidates, `M` is the largest
core numerator, `H` is the number surviving height, and `rho` is the least
nonnegative circular remainder

\[
 \rho=\min\{r,D_R-r:E_u\equiv r\pmod{D_R},\ 0\le r<D_R\}
\tag{30}
\]

over the `H` height survivors.  A dash means `H=0`.

| type | `R` | `D_R` | `N` | `M=max E_u` | `H` | `rho` |
|:---|---:|---:|---:|---:|---:|---:|
| five `1`s | 8 | 502829 | 120 | 751634 | 0 | -- |
| one `3` | 3 | 1631 | 55 | 11996 | 26 | 65 |
| one `3` | 4 | 13085 | 95 | 41108 | 7 | 148 |
| one `3` | 5 | 72023 | 160 | 131516 | 0 | -- |
| one `4` | 0 | 13 | 5 | 1108 | 5 | 2 |
| one `4` | 1 | 295 | 5 | 1108 | 2 | 72 |
| one `4` | 2 | 1909 | 25 | 5404 | 3 | 146 |
| one `4` | 3 | 9823 | 55 | 21076 | 1 | 1430 |
| one `4` | 4 | 45853 | 95 | 73468 | 0 | -- |
| one `4` | 5 | 203095 | 160 | 236788 | 0 | -- |

Every displayed `rho` is positive.  Consequently no height survivor has
`D_R|E_u`; every remaining candidate violates (15).  This completes the
five-defect exclusion. **QED**

## 8. Exact certificate and hit policy

Run

```text
python research/cross-direction-lemmas/proofs/L-9912-five-defect-certificate.py
```

The certificate uses integer arithmetic only.  It independently:

- recomputes the contraction table from the word definition;
- checks the three positivity thresholds and all large-range margins;
- generates every largest-gap composition rather than reading a stored
  candidate list;
- reconstructs `E_u`, the full word, `D_w`, and `E_w`, checking
  `E_w=3^tE_u` for every row;
- recomputes every entry of the finite table; and
- asserts that the divisor-hit list is empty.

The hit path is deliberately retained in the checker.  If a future edit
creates a divisor hit, it computes

\[
 n_0=1+{E_w\over D_w},
\tag{31}
\]

replays every accelerated branch, checks each advertised valuation exactly,
checks positivity and return, and records the first return time.  Thus a
negative, formal, inexact, trivial, or powered hit cannot silently be
reported as a primitive positive cycle.

## 9. Boundary audit

1. **No search bound is extrapolated.**  Section 6 proves the infinite
   tails impossible before Section 7 enumerates the finite remainder.
2. **Largest-gap coverage is cyclic, not reflective.**  Only rotations are
   used; the high letter is allowed in all five chronological positions.
3. **The tail is omitted from `E_u`.**  Its only effect is the coprime factor
   `3^t` in (14).  Including it in the divisor test would obscure the exact
   collapse.
4. **Positive-part maximization is safe.**  The high summand is discarded
   before adjacent swaps, so moving the high letter cannot accidentally be
   claimed to increase its negative contribution.
5. **Contraction is used only when strict.**  At `h>=2` the slope is at most
   `243/512`; for the lone-high core (23), `b>=5` gives slope at most
   `243/512`.
6. **No counterexample is hidden.**  The exact hit list is empty.  Hence
   there is no integer to promote to a positive cycle certificate, primitive
   or otherwise.

## Strongest conclusion

> Centering at the trivial fixed point resolves the entire five-exception
> frontier.  Two or more high exceptional letters contract, after monotone
> lowering, to one of six cores whose fixed point lies below the least
> positive centered integer.  A lone high letter at least five contracts to
> a negative fixed point.  Largest-gap bounds reduce the remaining all-one,
> lone-three, and lone-four families to ten exact rows, none divisible.
> Therefore any nontrivial positive accelerated Collatz cycle must contain
> at least six valuations different from two.
