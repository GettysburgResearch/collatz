# L-9910 -- Centered-defect and neutral-tail collapse for accelerated cycles

Claim ID: `L-9910`
Title: Centering at the trivial fixed point makes every non-2 valuation sparse, and a variable all-2 tail reduces to finitely many exact divisor tests
Status: `PROPOSED / EXACT SEARCH REDUCTION`
Authoring agent: `gpt56-synthesis-01-wave22-h-sunit-transfer`
Reviewing agents: `gpt56-synthesis-01` (independent algebra, inequality, and finite-table reconstruction); `gpt56-synthesis-01-wave24-divergent-orbit` (cold reconstruction through the four-defect theorem)
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9904` (complete divisibility-to-replay theorem, power collapse, and rotation invariance)
Scope: nonempty finite accelerated `3n+1` valuation words over the positive integers
Related counterexample candidates: none; the result excludes words with at most four non-2 letters and reduces neutral-tail families, but constructs no nontrivial cycle

## 1. Setup and result

Let

\[
 w=(a_0,\ldots,a_{k-1}),\qquad a_j\ge 1,
\tag{1}
\]

and put

\[
 A_0=0,\qquad A_j=\sum_{i<j}a_i,\qquad A=A_k,
\tag{2}
\]

\[
 C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
 \qquad D_w=2^A-3^k.
\tag{3}
\]

The exact branch represented by `w` is

\[
 x\longmapsto {3^kx+C_w\over 2^A}.
\tag{4}
\]

Define the **centered defect numerator**

\[
 \boxed{E_w=C_w-D_w.}
\tag{5}
\]

The center is the trivial accelerated fixed point `x=1`.  Indeed,

\[
 {3^k(1+y)+C_w\over2^A}-1
 ={3^ky+E_w\over2^A}.
\tag{6}
\]

The main facts proved below are:

1. `E_w` is supported only at letters different from `2`;
2. its exact 2-adic valuation is read from the first such letter, with no
   possible cancellation;
3. `D_w | E_w` is exactly the usual positive-cycle divisibility test;
4. appending any number of neutral letters `2` reduces to divisibility of
   one fixed integer `E_u`; and
5. a word with exactly one letter different from `2` cannot be a nontrivial
   positive cycle; and
6. even two letters different from `2` are still impossible; and
7. three letters different from `2` are also impossible, by centered
   deletion and one exact largest-gap estimate; and
8. four letters different from `2` reduce to three explicit contraction or
   largest-gap tables, none of which passes exact divisibility.

## 2. Sparse centered identity

### Theorem 1 -- telescoping defect formula

For every nonempty word (1),

\[
 \boxed{
 E_w=\sum_{j=0}^{k-1}
 3^{k-1-j}2^{A_j}\bigl(4-2^{a_j}\bigr).}
\tag{7}
\]

Thus every letter `a_j=2` contributes exactly zero.

### Proof

Write

\[
 W_j=3^{k-1-j}2^{A_j}.
\tag{8}
\]

Then `C_w=sum_j W_j`, while

\[
 \begin{aligned}
 \sum_{j=0}^{k-1}W_j2^{a_j}
 &=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_{j+1}}\\
 &=\sum_{\ell=1}^{k}3^{k-\ell}2^{A_\ell}\\
 &=3C_w+2^A-3^k\\
 &=3C_w+D_w.
 \end{aligned}
\tag{9}
\]

Consequently

\[
 \sum_jW_j(4-2^{a_j})
 =4C_w-(3C_w+D_w)=C_w-D_w=E_w.
\tag{10}
\]

This also checks the chronology: `A_j` is the valuation accumulated
*before* the letter `a_j`, exactly as in (3). **QED**

## 3. The first non-2 letter controls the exact 2-adic order

For `a != 2`, define

\[
 \epsilon(a)=
 \begin{cases}
 1,&a=1,\\
 2,&a\ge3.
 \end{cases}
\tag{11}
\]

Indeed,

\[
 v_2(4-2^a)=
 \begin{cases}
 1,&a=1,\\
 2,&a\ge3,
 \end{cases}
\tag{12}
\]

because `4-2=2`, while
`4-2^a=4(1-2^(a-2))` has an odd parenthesis for `a>=3`.

### Theorem 2 -- no-cancellation valuation

Suppose that `w` is not an all-2 word, and let `j` be its first index with
`a_j != 2`. Then

\[
 \boxed{v_2(E_w)=A_j+\epsilon(a_j).}
\tag{13}
\]

In particular, if `w` begins with exactly `r` letters `2`, then

\[
 \boxed{
 v_2(E_w)=
 \begin{cases}
 2r+1,&a_r=1,\\
 2r+2,&a_r\ge3.
 \end{cases}}
\tag{14}
\]

### Proof

The `j`th nonzero summand in (7) has 2-adic valuation

\[
 A_j+\epsilon(a_j).
\tag{15}
\]

Every power of `3` in (7) is a 2-adic unit.  It remains only to rule out a
second summand at the same order.

If `a_j=1`, then for every later non-2 index `ell`,

\[
 A_\ell\ge A_j+1,
 \qquad
 A_\ell+\epsilon(a_\ell)\ge A_j+2>A_j+1.
\tag{16}
\]

If `a_j>=3`, then

\[
 A_\ell\ge A_j+a_j\ge A_j+3,
 \qquad
 A_\ell+\epsilon(a_\ell)\ge A_j+4>A_j+2.
\tag{17}
\]

Intervening letters only increase `A_ell`; letters `2` contribute zero.
Hence the first nonzero summand has uniquely least 2-adic order.  It cannot
cancel, proving (13).  Formula (14) uses `A_j=2r`. **QED**

## 4. Exact positive-cycle equivalence after centering

### Theorem 3 -- centered certificate criterion

The word `w` is the exact accelerated itinerary of a positive closed orbit
if and only if

\[
 \boxed{D_w>0\quad\hbox{and}\quad D_w\mid E_w.}
\tag{18}
\]

When (18) holds, its initial odd integer is

\[
 \boxed{n_0=1+{E_w\over D_w}.}
\tag{19}
\]

There are exactly two cases:

1. `E_w=0`, in which case `w=(2)^k` and `n_0=1`;
2. `w` is nontrivial, in which case

   \[
   \boxed{E_w=(n_0-1)D_w\ge2D_w>0.}
   \tag{20}
   \]

### Proof

Since `E_w=C_w-D_w`,

\[
 D_w\mid E_w\quad\Longleftrightarrow\quad D_w\mid C_w.
\tag{21}
\]

The complete certificate theorem `L-9904` says that `D_w>0` together with
the right side of (21) is equivalent to positive integral replay with every
advertised valuation exact.  Its fixed integer is

\[
 {C_w\over D_w}=1+{E_w\over D_w},
\tag{22}
\]

which proves (18)--(19).

If `E_w=0`, then the replay starts at `1`.  Its unique accelerated valuation
is `v_2(3*1+1)=2`, and the next odd state is again `1`; induction forces
every letter of `w` to be `2`.  Conversely, `(2)^k` replays `1`, so its
centered defect is zero.

In every other positive certificate, `n_0` is an odd integer different from
`1`, hence `n_0>=3`.  Equation (19) now gives (20). **QED**

### Immediate rejection sieve

For any proposed nontrivial word with `D_w>0`, either of

\[
 E_w\le0,
 \qquad
 0<E_w<2D_w
\tag{23}
\]

is an exact rejection certificate.  Passing the height test is not
sufficient: the odd divisibility `D_w | E_w` remains indispensable.

## 5. Appending the neutral all-2 tail

Let `u` be a fixed nonempty word with summary

\[
 (k,A,C_u),
 \qquad
 E_u=C_u-(2^A-3^k).
\tag{24}
\]

For `r>=0`, let

\[
 w_r=u(2)^r
\tag{25}
\]

in chronological order.  The empty tail is allowed at `r=0`.

The all-2 word of length `r` has summary

\[
 (r,2r,4^r-3^r).
\tag{26}
\]

### Theorem 4 -- neutral-tail divisor collapse

Put

\[
 \boxed{D_r=2^A4^r-3^k3^r.}
\tag{27}
\]

Then

\[
 \boxed{
 C_{w_r}=3^rC_u+2^A(4^r-3^r),
 \qquad
 E_{w_r}=3^rE_u.}
\tag{28}
\]

Moreover,

\[
 \boxed{
 w_r\text{ is a positive exact cycle certificate}
 \quad\Longleftrightarrow\quad
 D_r>0\text{ and }D_r\mid E_u.}
\tag{29}
\]

If `u` is not an all-2 word, every possible hit in (29) must satisfy

\[
 \boxed{0<2D_r\le E_u.}
\tag{30}
\]

Once `D_r` is positive, the denominators grow by

\[
 \boxed{D_{r+1}=4D_r+3^{k+r}>4D_r.}
\tag{31}
\]

Consequently a fixed core `u` admits only finitely many tail lengths that
can certify, and they are exhausted exactly by:

1. advance to the first `r` with `D_r>0`;
2. while `2D_r<=E_u`, test the single exact divisibility `D_r | E_u`;
3. stop permanently after `2D_r>E_u`.

### Proof

For chronological concatenation, `L-9904` gives

\[
 C_{uv}=3^{k_v}C_u+2^{A_u}C_v.
\tag{32}
\]

Substituting (26) proves the first formula in (28).  Subtracting (27) gives

\[
 \begin{aligned}
 E_{w_r}
 &=3^rC_u+2^A(4^r-3^r)
   -(2^A4^r-3^k3^r)\\
 &=3^r(C_u-2^A+3^k)=3^rE_u,
 \end{aligned}
\tag{33}
\]

so no reversal of `u` and the tail is hidden.

The denominator is not divisible by `3`, because

\[
 D_r\equiv2^{A+2r}\not\equiv0\pmod3.
\tag{34}
\]

Therefore

\[
 D_r\mid E_{w_r}=3^rE_u
 \quad\Longleftrightarrow\quad D_r\mid E_u.
\tag{35}
\]

Theorem 3 proves (29).  If `u` is not all `2`, then neither is `w_r`.
Equations (19), (28), and (35) give

\[
 n_0-1=3^r{E_u\over D_r}.
\tag{36}
\]

Both `E_u=C_u-(2^A-3^k)` and `D_r` are respectively even and odd.  Thus, at
a divisor hit, `E_u/D_r` is even.  It is positive by (36), so it is at least
`2`, proving (30).  Finally, direct calculation gives (31).  Positivity is
eventual because `(4/3)^r` tends to infinity; after the first positive term,
(31) and (30) make the candidate list finite. **QED**

### Rotation consequence

`L-9904` proves that cycle divisibility is invariant under cyclic rotation.
Thus Theorem 4 applies unchanged to a variable run of `2`s inserted at any
fixed cut: rotate the word so that the run is the terminal tail, and regard
the remaining cyclic block as `u`.

It follows in particular that padding a fixed CRT, covering, morphic, or
grammar core by an arbitrarily long neutral run cannot create an infinite
unexamined cycle family.  Only the finite divisor list (29)--(31) remains.
This says nothing about families in which the core itself changes with `r`.

## 6. One exceptional valuation is impossible

### Corollary 5 -- exact one-defect exclusion

If a nonempty valuation word has exactly one letter different from `2`, it
is not a positive exact cycle certificate.

### Proof

By cyclic rotation, write the word as

\[
 w=(b)(2)^r,
 \qquad b\ne2,\qquad r\ge0.
\tag{37}
\]

For the one-letter core `(b)`,

\[
 C_u=1,
 \qquad
 E_u=1-(2^b-3)=4-2^b.
\tag{38}
\]

If `b>=3`, then `E_u<0`, contradicting the necessary inequality (30).

If `b=1`, then `E_u=2`, while

\[
 D_r=2\cdot4^r-3^{r+1}.
\tag{39}
\]

Here `D_0=D_1=-1` and `D_2=5`.  Equation (31) makes every later positive
denominator still larger.  Hence every `r` with `D_r>0` has `2D_r>=10>2`,
again contradicting (30).

The omitted value `b=2` gives the all-2 word and only the trivial fixed
point `1`. **QED**

## 7. Two exceptional valuations are also impossible

### Theorem 6 -- exact two-defect exclusion

If a nonempty valuation word has exactly two letters different from `2`, it
is not a positive exact cycle certificate.

### Proof

Rotate the cyclic word and write it, with the indicated chronology, as

\[
 \boxed{w=(b)(2)^r(c)(2)^s,}
 \qquad b,c\ne2,\qquad r,s\ge0.
\tag{40}
\]

Take

\[
 u=(b)(2)^r(c)
\tag{41}
\]

as the fixed core and `(2)^s` as the terminal neutral tail.  Formula (7), or
two direct applications of (28), gives

\[
 \boxed{
 E_u=(4-2^b)3^{r+1}+(4-2^c)2^{b+2r}.}
\tag{42}
\]

The complete word has

\[
 \boxed{
 D_s=2^{b+c+2(r+s)}-3^{r+s+2}.}
\tag{43}
\]

By Theorem 4, a nontrivial positive certificate would require

\[
 D_s>0,\qquad D_s\mid E_u,\qquad E_u\ge2D_s.
\tag{44}
\]

We exclude all possible types of the two exceptional letters.

#### Case 1: both exceptional letters are at least three

If `b,c>=3`, both summands in (42) are negative.  Thus `E_u<0`, contradicting
(44).

#### Case 2: exactly one exceptional letter is one

Rotate once more if necessary so that

\[
 b\ge3,\qquad c=1.
\tag{45}
\]

This rotation changes which gap is called `r` or `s`, but preserves cycle
divisibility and retains the chronological form (40).  Put

\[
 q=2^{b+1}4^r.
\tag{46}
\]

Equations (42)--(43) become

\[
 E_u=q-(2^b-4)3^{r+1},
\tag{47}
\]

\[
 D_s=q4^s-9\,3^{r+s}.
\tag{48}
\]

If `D_s>0`, then

\[
 q>9\,3^r(3/4)^s.
\tag{49}
\]

Because `2*4^s-1>0`, equations (47)--(49) give

\[
 \begin{aligned}
 2D_s-E_u
 &=q(2\cdot4^s-1)-18\,3^{r+s}
   +(2^b-4)3^{r+1}\\
 &>3^{r+1}\left((2^b-4)-3(3/4)^s\right)\\
 &>0.
 \end{aligned}
\tag{50}
\]

The final inequality is strict because `2^b-4>=4`, whereas
`3(3/4)^s<=3`.  Thus `E_u<2D_s`, contradicting (44).

#### Case 3: both exceptional letters are one

It remains to take

\[
 b=c=1,
 \qquad t=r+s.
\tag{51}
\]

Now (42)--(43) reduce to

\[
 \boxed{
 E_r=2\,3^{r+1}+4\,4^r,
 \qquad
 D_t=4^{t+1}-9\,3^t.}
\tag{52}
\]

The values `D_0,D_1,D_2,D_3` are respectively `-5,-11,-17,13`, and

\[
 D_{t+1}=4D_t+3^{t+2}.
\tag{53}
\]

Hence positive drift is equivalent to `t>=3`.  Since `r<=t` and `E_r` is
strictly increasing, the height condition in (44) implies

\[
 \begin{aligned}
 2(4^{t+1}-9\,3^t)
 &\le 2\,3^{t+1}+4\,4^t,\\
 (4/3)^t&\le6.
 \end{aligned}
\tag{54}
\]

But `4^7>6*3^7`, and `(4/3)^t` is increasing.  Therefore only

\[
 t\in\{3,4,5,6\}
\tag{55}
\]

can pass the height bound.  The following exact integer table exhausts
every `0<=r<=t`.  Rows omitted from the `r` column already have
`E_r<2D_t`; the displayed nonzero remainders reject all remaining rows.

| `t` | `D_t` | `2D_t` | `r` surviving height | `E_r` | `E_r mod D_t` |
|---:|---:|---:|:---|:---|:---|
| 3 | 13 | 26 | 1, 2, 3 | 34, 118, 418 | 8, 1, 2 |
| 4 | 295 | 590 | 4 | 1510 | 35 |
| 5 | 1909 | 3818 | 5 | 5554 | 1736 |
| 6 | 9823 | 19646 | 6 | 20758 | 1112 |

No row satisfies `D_t | E_r`.  This contradicts (44) in the last possible
case and proves the theorem. **QED**

## 8. Three exceptional valuations are impossible

The centered one-letter branch is

\[
 \boxed{
 g_a(y)={3y+4-2^a\over2^a},
 \qquad g_2(y)={3y\over4}.}
\tag{56}
\]

Thus `g_a` is strictly increasing, while a neutral letter `2` strictly
decreases every positive centered state.

### Theorem 7 -- exact three-defect exclusion

If a nonempty valuation word has exactly three letters different from `2`,
it is not a positive exact cycle certificate.

### Proof

Assume for contradiction that such a certificate exists.  It is nontrivial,
so none of its odd states is `1`: once the orbit reaches `1`, determinism
forces the all-2 itinerary forever.  Therefore at every cyclic cut

\[
 \boxed{y=n-1\text{ is a positive even integer}.}
\tag{57}
\]

We separate the cases according to the three exceptional letters.

#### Case 1: at least one exceptional letter is at least three

Rotate to an exceptional letter and write

\[
 w=(b_1)(2)^r(b_2)(2)^s(b_3)(2)^t,
 \qquad b_i\ne2,
\tag{58}
\]

and let

\[
 v=(b_1,b_2,b_3)
\tag{59}
\]

be the word obtained by deleting every neutral `2`.  Let `G_w,G_v` denote
the corresponding compositions of the centered maps (56), in chronological
order.

Start both formal replays at the cycle value `y_0>0` for `w`.  Scan the two
words together.  At a retained letter, strict monotonicity of `g_a` preserves
the comparison.  At a deleted `2`, the shortened replay skips
`z -> 3z/4`; the original value `z` is positive, and the shortened value is
already at least `z`.  It therefore becomes strictly larger.  Induction
through the word gives

\[
 \boxed{G_v(y_0)\ge G_w(y_0)=y_0,}
\tag{60}
\]

with strict inequality if and only if at least one `2` was deleted.

Put `B=b_1+b_2+b_3`.  Since at least one `b_i>=3` and the other two are at
least one,

\[
 {3^3\over2^B}\le{27\over32}<1.
\tag{61}
\]

Hence `G_v` is an affine contraction.  Its unique fixed point is

\[
 y_v={E_v\over D_v},
 \qquad D_v=2^B-27>0,
\tag{62}
\]

and (60) is equivalent to

\[
 \boxed{y_0\le y_v,}
\tag{63}
\]

again with strict inequality exactly when a neutral `2` was deleted.

If all three `b_i` are at least three, every summand in (7) for `E_v` is
negative, contradicting `y_v>=y_0>0`.

If exactly one of the letters is `1`, write the other two as `p,q>=3`.
The three possible cyclic positions give

\[
 \begin{array}{rcl}
 E_{(1,p,q)}&=&42-2^{p+1}(2^q-1)<0,\\
 E_{(p,1,q)}&=&36+2^p(5-2^{q+1})<0,\\
 E_{(p,q,1)}&=&36+2^p(3-2^q)<0.
 \end{array}
\tag{64}
\]

The inequalities already hold at `p=q=3` and only strengthen thereafter.
This again contradicts (63).

Suppose exactly two exceptional letters are `1`, and call the remaining
letter `b>=3`.  All rotations have denominator

\[
 D_v=2^{b+2}-27,
\tag{65}
\]

while their centered numerators are

\[
 \begin{array}{rcl}
 E_{(1,1,b)}&=&46-2^{b+2},\\
 E_{(1,b,1)}&=&42-2^{b+1},\\
 E_{(b,1,1)}&=&36+2^b.
 \end{array}
\tag{66}
\]

For `b>=4`, direct subtraction gives

\[
 \begin{array}{rcl}
 2D_v-E_{(1,1,b)}&=&3\,2^{b+2}-100>0,\\
 2D_v-E_{(1,b,1)}&=&5\,2^{b+1}-96>0,\\
 2D_v-E_{(b,1,1)}&=&7\,2^b-90>0.
 \end{array}
\tag{67}
\]

Thus every base fixed point in (66) is less than `2`, contradicting
`2<=y_0<=y_v`.

Only `b=3` remains.  Rotate the exceptional sequence to `(1,1,3)`.  Its
base fixed point is

\[
 y_v={14\over5}.
\tag{68}
\]

If no neutral `2` occurs, (63) is equality and the purported integer state
would be `14/5`, impossible.  If at least one `2` occurs, strictness in (63)
and (57) force

\[
 y_0=2,
 \qquad n_0=3.
\tag{69}
\]

But the first exceptional valuation `1` sends `3` to `5`, and

\[
 v_2(3\cdot5+1)=v_2(16)=4.
\tag{70}
\]

The next advertised letter in the rotated word is `2` if the gap after the
first `1` is nonempty, and is the second exceptional `1` if that gap is
empty.  Either value contradicts (70).  This finishes every case containing
a letter at least three.

#### Case 2: all three exceptional letters are one

Rotate a largest neutral gap to the end and write

\[
 w=(1)(2)^r(1)(2)^s(1)(2)^t,
 \qquad t\ge r,s,
 \qquad R=r+s+t.
\tag{71}
\]

The full denominator is

\[
 D_R=8\,4^R-27\,3^R.
\tag{72}
\]

Because `(4/3)^R` is increasing, the exact comparisons

\[
 8\,4^4<27\,3^4,
 \qquad
 8\,4^5>27\,3^5
\tag{73}
\]

show that positive drift requires `R>=5`.  In particular, the largest gap
satisfies `t>=2`.

Remove the terminal tail `(2)^t` and call the remaining word `u`; it has
`m=R-t` neutral letters.  For a word containing only letters `1` and `2`,
swap an adjacent `(1,2)` to `(2,1)`.  In (7), the moved `1` gains a factor
`4` from its prefix and loses a factor `3` from its suffix, while every other
nonzero summand is unchanged.  The centered numerator is therefore
multiplied by `4/3` at that summand and strictly increases.  Repeated swaps
show that, among all arrangements of three `1`s and `m` letters `2`, the
largest numerator has all the `2`s first.  Its value is

\[
 \boxed{
 E_u\le2\,4^m(3^2+3\cdot2+2^2)
      =38\,4^m
      \le38\,4^{R-2}.}
\tag{74}
\]

For `R>=5`,

\[
 {27\,3^R\over8\,4^R}
 \le {6561\over8192}.
\tag{75}
\]

Consequently

\[
 D_R\ge {1631\over1024}4^R,
 \qquad
 2D_R\ge {3262\over1024}4^R
       > {2432\over1024}4^R
       =38\,4^{R-2}\ge E_u.
\tag{76}
\]

This contradicts the neutral-tail necessity `E_u>=2D_R` in (30).  The
all-one case is impossible as well, completing the proof. **QED**

## 9. Four exceptional valuations are impossible

### Theorem 8 -- exact four-defect exclusion

If a nonempty valuation word has exactly four letters different from `2`, it
is not a positive exact cycle certificate.

### Proof

Assume again that a nontrivial positive cycle exists, so every centered state
on its exact replay is a positive even integer.  Two monotone modifications
will be used below:

1. delete a neutral branch `g_2(z)=3z/4<z`;
2. replace a high branch `a` by a smaller `c>=3`, for which

   \[
   g_c(z)-g_a(z)
   =(3z+4)\left({1\over2^c}-{1\over2^a}\right)>0
   \qquad(z>0).
   \tag{77}
   \]

As in the proof of Theorem 7, scan the original and modified replays in
parallel.  Every branch has positive slope.  After the first strict
modification, the modified state is larger; before then it is equal.  In
particular, every modified intermediate state remains positive because it
dominates the corresponding state on the original positive cycle.  Thus the
inequalities used in both modifications remain valid all the way around the
word.

If the final modified core map `H(y)=alpha y+beta` has `alpha<1`, its terminal
value at the original `y_0` satisfies

\[
 H(y_0)\ge y_0
 \quad\Longrightarrow\quad
 y_H={\beta\over1-\alpha}\ge y_0\ge2.
\tag{78}
\]

We now classify by the number of exceptional letters at least three.

#### Case 1: at least two exceptional letters are high

Delete every neutral `2` and replace every high exceptional letter by `3`.
The result is a word `v` in `{1,3}^4` containing `h>=2` letters `3`.  Its slope
is

\[
 {3^4\over2^{4+2h}}\le {81\over256}<1.
\tag{79}
\]

The following table gives its denominator and every possible centered
numerator as the `h` positions vary.  Direct substitution in (7) produces
each finite row.

| `h` | `D_v=2^(4+2h)-81` | all possible `E_v` |
|---:|---:|:---|
| 2 | 175 | -86, -50, 46, 4, 100, 244 |
| 3 | 943 | -722, -668, -524, -140 |
| 4 | 4015 | -3212 |

Every entry satisfies `E_v<2D_v`, so the modified fixed point is less than
`2`.  This contradicts (78).

#### Case 2: exactly one high letter `b>=4`

Rotate the exceptional sequence to `(1,1,1,b)`, delete every neutral `2`,
and replace `b` by `4`.  The modified core is `(1,1,1,4)`, with

\[
 \boxed{E_v=18,\qquad D_v=47,qquad y_v={18\over47}<2.}
\tag{80}
\]

Its slope is `81/128<1`, so (78) gives the same contradiction.

#### Case 3: exactly one high letter, equal to three

Rotate a largest neutral gap to the terminal position.  Write

\[
 w=(b_0)(2)^{r_0}(b_1)(2)^{r_1}
   (b_2)(2)^{r_2}(b_3)(2)^t,
\tag{81}
\]

where `(b_0,b_1,b_2,b_3)` is a permutation of `(3,1,1,1)` and

\[
 t\ge r_0,r_1,r_2,
 \qquad R=r_0+r_1+r_2+t.
\tag{82}
\]

If a largest gap is tied, choose any tied gap.  Allowing the `3` in all four
positions below includes every cyclic rotation arising from every such
choice, so ties remove no case.

Remove the terminal tail and call the remaining core `u`.  For independent
checking, put

\[
 P_i=\sum_{j<i}b_j+2\sum_{j<i}r_j,
 \qquad
 Q_i=3-i+\sum_{j=i}^{2}r_j
 \quad(0\le i\le3),
\tag{83}
\]

where empty sums vanish.  Then

\[
 \boxed{E_u=\sum_{i=0}^3(4-2^{b_i})2^{P_i}3^{Q_i}.}
\tag{84}
\]

Let `m=R-t` be the number of neutral letters retained in `u`.  Drop the one
negative contribution belonging to `3`.  Moving every letter of valuation
at least two before the three positive letters `1` only increases their
positive contributions: each adjacent move of a `1` to the right across a
letter `a>=2` multiplies its term by `2^a/3>1` and leaves the other positive
terms unchanged.  Hence

\[
 \boxed{
 E_u\le 2\,2^{2m+3}(3^2+3\cdot2+2^2)
     =304\,4^m
     \le304\,4^{R-\lceil R/4\rceil}.}
\tag{85}
\]

The full denominator is

\[
 \boxed{D_R=64\,4^R-81\,3^R.}
\tag{86}
\]

It is negative at `R=0` and positive for every `R>=1`.  For `R>=4`,

\[
 {81\,3^R\over64\,4^R}\le{6561\over16384},
\tag{87}
\]

so, using `ceil(R/4)>=1`,

\[
 2D_R\ge{9823\over128}4^R
       >76\,4^R
       \ge E_u.
\tag{88}
\]

This contradicts (30).  It remains only to check `R=1,2,3`.  The following
table lists every canonical largest-gap arrangement that survives the height
test `E_u>=2D_R`; all omitted arrangements fail that test.  In the gap
column, the semicolon separates the terminal largest gap `t`.

| `R` | `(b_0,b_1,b_2,b_3)` | `(r_0,r_1,r_2;t)` | `D_R` | `E_u` | `E_u mod D_R` |
|---:|:---|:---|---:|---:|---:|
| 1 | `(3,1,1,1)` | `(0,0,0;1)` | 13 | 196 | 1 |
| 1 | `(1,3,1,1)` | `(0,0,0;1)` | 13 | 142 | 12 |
| 1 | `(1,1,3,1)` | `(0,0,0;1)` | 13 | 106 | 2 |
| 1 | `(1,1,1,3)` | `(0,0,0;1)` | 13 | 82 | 4 |
| 2 | `(3,1,1,1)` | `(0,0,1;1)` | 295 | 652 | 62 |
| 2 | `(3,1,1,1)` | `(0,1,0;1)` | 295 | 748 | 158 |
| 2 | `(3,1,1,1)` | `(1,0,0;1)` | 295 | 892 | 7 |
| 3 | none | none | 1909 | none | none |

Every displayed remainder is nonzero.  Therefore no divisor hit occurs.

#### Case 4: all four exceptional letters are one

Again rotate a largest neutral gap to the terminal position.  With `R` total
neutral letters, the full denominator is

\[
 \boxed{D_R=16\,4^R-81\,3^R.}
\tag{89}
\]

The exact comparisons at `R=5,6` show that positive drift is equivalent to
`R>=6`.  The largest gap then has length at least two.  If the core obtained
by deleting that tail retains `m` neutral letters, the same adjacent-swap
maximization gives

\[
 \boxed{
 E_u\le2\,4^m(3^3+3^2\cdot2+3\cdot2^2+2^3)
     =130\,4^m
     \le130\,4^{R-\lceil R/4\rceil}.}
\tag{90}
\]

For `R>=7`,

\[
 {81\,3^R\over16\,4^R}\le{177147\over262144},
\tag{91}
\]

and therefore

\[
 2D_R\ge{84997\over8192}4^R
       >{65\over8}4^R
       \ge E_u.
\tag{92}
\]

Only `R=6` remains.  The six canonical largest-gap arrangements surviving
height are listed below; every terminal gap is `2`, and every other
arrangement has `E_u<2D_R`.

| `(r_0,r_1,r_2;t)` | `D_R` | `E_u` | `E_u mod D_R` |
|:---|---:|---:|---:|
| `(0,2,2;2)` | 6487 | 14842 | 1868 |
| `(1,1,2;2)` | 6487 | 15814 | 2840 |
| `(1,2,1;2)` | 6487 | 16966 | 3992 |
| `(2,0,2;2)` | 6487 | 17110 | 4136 |
| `(2,1,1;2)` | 6487 | 18262 | 5288 |
| `(2,2,0;2)` | 6487 | 19798 | 337 |

No remainder vanishes.  This rejects the last case and completes the proof.
**QED**

## 10. Adversarial and boundary audit

1. **The center is `1`, not `0`.**  Formula (6) is why the neutral letter is
   exactly `2`: `(3*1+1)/4=1`.
2. **Sign.**  `E=C-D`, not `D-C`.  The test word `(1,2,2)` has
   `(C,D,E)=(23,5,18)`, agreeing with
   `E_(1)3^2=2*9`.
3. **Chronology.**  In `u(2)^r`, the tail acts last, so its odd multiplier
   `3^r` multiplies `C_u` in (28).  Reversing the word would change the
   displayed numerator, although rotation preserves final divisibility.
4. **No-cancellation claim.**  Theorem 2 uses a uniquely least 2-adic
   summand.  It does not infer a valuation from a triangle inequality with
   two terms of equal order.
5. **Trivial powers.**  For `w=(2)^k`, `C_w=D_w=4^k-3^k` and `E_w=0`.
   These words must be retained as the explicit exception to (20), (23),
   and (30).
6. **Negative or zero drift.**  Centered divisibility alone is not a
   positive certificate; `D>0` remains mandatory.
7. **Height is only a sieve.**  `E>=2D` does not imply divisibility.  For
   `(1,2,2)`, `18>=10`, but `5` does not divide `18`.
8. **Fixed core.**  The finiteness in Theorem 4 freezes `u`.  It does not
   bound a diagonal family in which both the core and tail vary.
9. **Two-defect rotation.**  In Case 2, the high exceptional letter is put
   first and the exceptional `1` second.  The two intervening cyclic gaps
   are then exactly `r` and `s`; no reflection or reversal is used.
10. **Finite table.**  The table in Theorem 6 follows only after the exact
    Archimedean bound reduces `t` to four values.  It is a proof-completing
    finite calculation, not evidence extrapolated beyond a search range.
11. **Centered deletion.**  The comparison in (60) uses positivity of every
    state on the assumed nontrivial cycle.  Strictness holds exactly when at
    least one neutral `2` is actually deleted.  The contraction estimate is
    applied only after a letter at least three makes the three-letter core
    slope at most `27/32`.
12. **All-one maximization.**  The adjacent swap in Theorem 7 changes only
    the moved `1` contribution: later prefixes see the same total valuation,
    and earlier suffix lengths are unchanged.  Thus (74) is a genuine global
    maximum, not a guessed ordering.
13. **Modified replay positivity.**  The high-to-3 comparison in Theorem 8
    is not applied to arbitrary negative formal states.  The modified replay
    dominates the assumed positive cycle at every prefix, so all inputs in
    (77) remain positive.
14. **Largest-gap ties.**  Rotating any chosen maximal gap to the terminal
    position gives (81)--(84).  The finite one-high table allows the `3` in
    every position, so choosing a different tied maximum only duplicates an
    included cyclic arrangement.
15. **Positive-part bounds.**  Equations (85) and (90) first discard every
    negative high contribution, then maximize the remaining positive terms.
    They are upper bounds even though the discarded term itself changes
    under adjacent swaps.
16. **No counterexample.**  Every theorem is a reformulation, finite search
    reduction, or exact exclusion.  No nontrivial positive integer or cycle
    word is produced.

## Strongest conclusion

> Centering an accelerated word at the trivial fixed point deletes every
> valuation `2` from its numerator and leaves an exact sparse signed sum over
> the exceptional letters.  The first exceptional letter determines the
> entire 2-adic order without cancellation.  For a fixed core followed by an
> arbitrary all-2 tail, the cycle condition reduces to divisibility of the
> fixed centered numerator by a denominator that grows by a factor greater
> than four after becoming positive.  Hence neutral padding supplies only a
> finite, exact divisor list.  A complete sign, height, and four-row divisor
> analysis excludes one and two exceptional valuations; centered deletion
> and sharp largest-gap estimates exclude three and four.  No word with at
> most four exceptional valuations can supply a nontrivial positive cycle.

## Suggested next attack

Represent a compressed candidate by its cyclic list of non-2 letters and the
runs of `2`s between them.  Use (7) as the sparse numerator, rotate the
largest or variable neutral run to the end, and apply (29)--(31) before any
general factor or CRT search.  The first genuinely open sparse frontier has
at least five exceptional letters whose core changes with the run
parameters.
