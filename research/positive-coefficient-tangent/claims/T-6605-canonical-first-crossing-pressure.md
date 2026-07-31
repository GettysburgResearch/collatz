# T-6605 — Canonical first crossings obey a joint residue–remainder pressure law

**Claim ID:** `T-6605`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary shortcut-Collatz affine algebra; the dyadic factor-separation argument of PR #81 `L-6801`; the distinct odd-source product estimate of PR #80 `L-6501`  
**Scope:** canonical positive representatives of finite first coefficient-crossing words  

## 1. Setup

Let

\[
w=(v_0,\ldots,v_{j-1})\in\{0,1\}^j
\]

be a first coefficient-crossing word for the shortcut map. Put

\[
q_m=\sum_{i<m}v_i,
\qquad
\alpha={\log2\over\log3},
\qquad
D_m=q_m-\alpha m.
\]

Thus

\[
D_m\ge0\quad(0\le m<j),
\qquad
D_j<0.
\tag{1}
\]

Write

\[
q=q_j,
\qquad
T_w(x)={3^qx+A_w\over2^j},
\qquad
\Delta_w=2^j-3^q>0,
\]

and define

\[
\boxed{x_*(w)={A_w\over\Delta_w}.}
\tag{2}
\]

Let `r=r^+(w)` be the least positive parity-cylinder representative and put

\[
y=T_w(r).
\]

Finally set

\[
B=B(w)=\max_{m<j}D_m,
\qquad
G_j(B)=3^B e^{7/9}j^{1/9}.
\tag{3}
\]

For `1<=L<=j`, let `p_w(L)` be the number of distinct length-`L` factors among the `j-L+1` factors of `w`.

## 2. Canonical descent is exactly the Box-2 inequality

The canonical start and endpoint satisfy

\[
3^qr+A_w=2^jy.
\]

Hence

\[
\boxed{
\Delta_wr-A_w=2^j(r-y).}
\tag{4}
\]

Therefore

\[
\boxed{
 r>{A_w\over2^j-3^q}
 \iff
 y<r.}
\tag{5}
\]

Every positive lift is

\[
x=r+2^jt,
\qquad t\ge0,
\]

with endpoint

\[
T_w(x)=y+3^qt.
\]

Consequently

\[
\boxed{
T_w(x)-x=(y-r)-\Delta_wt.}
\tag{6}
\]

Thus canonical descent forces descent for every lift. Equality in `(5)` is a positive cycle.

## 3. Height confinement under canonical non-descent

Assume

\[
y\ge r.
\tag{7}
\]

Then `(5)` gives

\[
r\le x_*(w).
\tag{8}
\]

Let `x_m=T^m(r)`. Every proper prefix is coefficient-supercritical, so

\[
x_m\ge r
\qquad(0\le m<j).
\tag{9}
\]

If two of `x_0,...,x_(j-1)` coincide, the orbit has entered a positive cycle. Take the acyclic alternative.

For every proper prefix,

\[
{x_m\over r}
=3^{D_m}
\prod_{\substack{i<m\\x_i\text{ odd}}}
\left(1+{1\over3x_i}\right).
\tag{10}
\]

The odd source states are distinct. Except possibly for the first source, they are coprime to six. Ordering them and using that the `s`th positive integer coprime to six is at least `3s-2` gives

\[
\prod_{\substack{i<m\\x_i\text{ odd}}}
\left(1+{1\over3x_i}\right)
\le e^{7/9}m^{1/9}
\le e^{7/9}j^{1/9}.
\tag{11}
\]

Since `D_m<=B`, equations `(9)--(11)` yield

\[
\boxed{
 r\le x_m\le G_j(B)r
 \qquad(0\le m<j).}
\tag{12}
\]

## 4. Exact factor-complexity pressure

If the same length-`L` parity factor occurs at positions `a<b`, applying its common affine map at both starts gives

\[
2^L\mid x_a-x_b.
\tag{13}
\]

Thus `M` occurrences of one factor begin at `M` distinct states spaced by at least `2^L`. By `(12)` and `(8)`,

\[
(M-1)2^L
\le
\bigl(G_j(B)-1\bigr)r
\le
\bigl(G_j(B)-1\bigr)x_*(w).
\tag{14}
\]

Some factor occurs at least

\[
\left\lceil{j-L+1\over p_w(L)}\right\rceil
\]

times. Therefore every acyclic canonical non-descent satisfies

\[
\boxed{
 p_w(L)
 \ge
 \left\lceil
 {j-L+1\over
  1+\left\lfloor
  {(G_j(B)-1)x_*(w)\over2^L}
  \right\rfloor}
 \right\rceil.}
\tag{15}
\]

Equivalently, the canonical representative must descend whenever, for some `L`,

\[
\boxed{
\left(
\left\lceil{j-L+1\over p_w(L)}\right\rceil-1
\right)2^L
>
\bigl(G_j(B)-1\bigr)x_*(w).}
\tag{16}
\]

This is a direct finite certificate for Box 2:

```text
factor repetition
+ exact dyadic separation
+ proper-prefix coefficient-bank control
+ the exact real fixed-point threshold
    -> canonical ordinary descent.
```

No free infinite directive or completion is used.

## 5. Global bank-gap corollary

The `j` proper states are distinct integers in `[r,G_j(B)r]`. Hence

\[
r+j-1\le G_j(B)r.
\]

Using `(8)`, every acyclic canonical non-descent must satisfy

\[
\boxed{
 x_*(w)
 \ge
 {j-1\over G_j(B)-1}.}
\tag{17}
\]

For bounded `B`, this is

\[
x_*(w)
\ge
\bigl(e^{-7/9}3^{-B}-o(1)\bigr)j^{8/9}.
\tag{18}
\]

Thus a Box-2 counterexample must pay either a growing proper-prefix surplus bank or a correspondingly large fixed-point threshold.

## 6. Source-qualified linear-scale recurrence exclusion

At a first crossing,

\[
{A_w\over2^j}<{j\over2},
\tag{19}
\]

because each odd additive contribution is less than `1/2`.

Let

\[
\lambda=j\log2-q\log3>0.
\]

A standard two-logarithm Baker bound supplies effective constants `c_0,mu>0` with

\[
\lambda\ge c_0j^{-\mu}.
\tag{20}
\]

Since `1-e^{-lambda}>=lambda/2` for `0<lambda<log2`, equations `(19)--(20)` give

\[
\boxed{x_*(w)<c_0^{-1}j^{\mu+1}.}
\tag{21}
\]

Fix `B_0` and `theta in (0,1)`. If `B(w)<=B_0` and a length

\[
L=\lfloor\theta j\rfloor
\]

factor repeats, `(14)` requires an exponentially large left side `2^L`, while `(3)` and `(21)` make the right side polynomial. Hence:

\[
\boxed{
\begin{minipage}{0.86\linewidth}
For fixed `B_0` and `theta>0`, every sufficiently long acyclic non-descending first-crossing word with `B(w)<=B_0` has all length-`floor(theta j)` factors distinct.
\end{minipage}}
\tag{22}
\]

The source theorem in `(20)` must be frozen and independently reconstructed before `(21)--(22)` are promoted. Equations `(4)--(18)` are elementary.

## 7. Strategic meaning

A late failure of Box 2 must simultaneously satisfy:

```text
one canonical positive root at or below x_*(w);
no earlier positive cycle;
all proper states confined to [r,G_j(B)r];
the exact factor-complexity floor (15);
the bank-gap inequality (17);
and, at bounded bank, linear-scale factor uniqueness (22).
```

The remaining offense is now precise: prove that every admissible first-crossing corridor forces enough repeated structure—or enough canonical residue growth—to violate `(15)`.

## 8. Gap audit

- Growing-bank words remain open.
- A finite word may have all long factors distinct; `(22)` is a recurrence obstruction, not a contradiction by itself.
- The positive-cycle alternative remains a separate full-denominator problem.
- The exponent `1/9` is safe rather than asserted optimal.
- Box 2, universal CST, and Collatz remain unproved.
