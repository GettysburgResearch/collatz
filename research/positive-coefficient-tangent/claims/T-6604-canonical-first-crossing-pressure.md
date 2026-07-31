# T-6604 — Canonical first crossings obey a joint residue–remainder pressure law

**Claim ID:** `T-6604`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary shortcut-Collatz affine algebra; the dyadic factor-separation argument of PR #81 `L-6801`; the distinct odd-source product estimate of PR #80 `L-6501`  
**Scope:** canonical positive representatives of finite first coefficient-crossing words  

## 1. Setup

Use the shortcut map

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

Let

\[
w=(v_0,\ldots,v_{j-1})\in\{0,1\}^j
\]

be a first coefficient-crossing word. Put

\[
q_m=\sum_{i=0}^{m-1}v_i,
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
T_w(x)={3^q x+A_w\over2^j},
\qquad
\Delta_w=2^j-3^q>0,
\tag{2}
\]

and define the positive real fixed-point threshold

\[
\boxed{x_*(w)={A_w\over\Delta_w}.}
\tag{3}
\]

Let `r=r^+(w)` be the least positive representative of the parity cylinder of `w`, and put

\[
y=T_w(r).
\tag{4}
\]

Finally, let

\[
B=B(w)=\max_{0\le m<j}D_m
\tag{5}
\]

and define

\[
\boxed{
G_j(B)=3^B e^{7/9}j^{1/9}.}
\tag{6}
\]

For `1<=L<=j`, let `p_w(L)` be the number of distinct length-`L` factors of `w` among its `j-L+1` starting positions.

## 2. Exact canonical crossing identity

The canonical start and endpoint satisfy

\[
3^q r+A_w=2^j y.
\]

Therefore

\[
\boxed{
\Delta_w r-A_w=2^j(r-y).}
\tag{7}
\]

Since `Delta_w>0`, the following are equivalent:

\[
\boxed{
 r>x_*(w)
 \iff
 y<r.}
\tag{8}
\]

Equality is equivalent to `y=r`, hence to a positive cycle with word `w`.

Every positive integer in the same parity cylinder is

\[
x=r+2^j t,
\qquad t\in\mathbf Z_{\ge0},
\]

and its endpoint is

\[
T_w(x)=y+3^q t.
\]

Consequently

\[
\boxed{
T_w(x)-x=(y-r)-\Delta_w t.}
\tag{9}
\]

Thus:

- if the canonical representative descends, every positive lift descends;
- if it does not descend, the complete finite list of non-descending lifts is determined by `(9)`.

In particular, the Box-2 target

\[
r^+(w)>{A_w\over2^j-3^q}
\]

is exactly the statement that the canonical representative descends at its first coefficient crossing.

## 3. Ordinary height bound inside a non-descending crossing

Assume from now on that

\[
y\ge r.
\tag{10}
\]

Then `(8)` gives

\[
r\le x_*(w).
\tag{11}
\]

Let

\[
x_m=T^m(r)
\qquad(0\le m\le j).
\]

For every proper prefix, the exact multiplicative identity is

\[
{x_m\over r}
=3^{D_m}P_m,
\qquad
P_m=
\prod_{\substack{0\le i<m\\x_i\text{ odd}}}
\left(1+{1\over3x_i}\right).
\tag{12}
\]

Condition `(1)` and the nonnegative affine remainder give

\[
x_m\ge r
\qquad(0\le m<j).
\tag{13}
\]

If two states among `x_0,...,x_(j-1)` coincide, the orbit has entered a positive cycle. We henceforth take the acyclic alternative, so these states—and in particular all odd source states—are distinct.

After the first odd step, every orbit state is nonzero modulo three. Thus all later odd sources are coprime to six. Ordering the distinct odd sources and using that the `s`th positive integer coprime to six is at least `3s-2` gives the elementary bound

\[
P_m\le e^{7/9}m^{1/9}
\le e^{7/9}j^{1/9}.
\tag{14}
\]

Together with `D_m<=B`, equations `(12)--(14)` give

\[
\boxed{
 r\le x_m\le G_j(B)r
 \qquad(0\le m<j).}
\tag{15}
\]

This uses the same ordinary orbit throughout; no free symbolic completion is introduced.

## 4. Joint factor-complexity pressure

Suppose one length-`L` factor occurs `M` times in `w`. The corresponding `M` starting states lie among `x_0,...,x_(j-1)`.

For two occurrences at positions `a<b`, applying the same length-`L` affine map and subtracting gives

\[
2^L\bigl(x_{a+L}-x_{b+L}\bigr)
=3^s(x_a-x_b),
\]

where `s` is the factor weight. Hence

\[
2^L\mid x_a-x_b.
\tag{16}
\]

The states are distinct, so the `M` starting values are spaced by at least `2^L`. By `(15)`, they all lie in the interval

\[
[r,G_j(B)r].
\]

Therefore

\[
(M-1)2^L
\le
\bigl(G_j(B)-1\bigr)r
\le
\bigl(G_j(B)-1\bigr)x_*(w).
\tag{17}
\]

Since the `j-L+1` factor occurrences are distributed among `p_w(L)` distinct factors, some factor occurs at least

\[
M\ge
\left\lceil{j-L+1\over p_w(L)}\right\rceil
\]

times. Combining this with `(17)` proves the exact pressure inequality

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
\tag{18}
\]

Equivalently, the canonical representative must descend whenever, for some `L`,

\[
\boxed{
\left(
\left\lceil{j-L+1\over p_w(L)}\right\rceil-1
\right)2^L
>
\bigl(G_j(B)-1\bigr)x_*(w).}
\tag{19}
\]

Equation `(19)` is a direct sufficient certificate for Box 2 using only the finite word:

```text
factor repetition
+ exact dyadic separation
+ bounded proper-prefix coefficient bank
+ exact real fixed-point threshold
    -> canonical ordinary descent.
```

It couples the two sides of `Q-6801`; it is not another independent encoding.

## 5. Global packing corollary

The `j` states

\[
x_0,\ldots,x_{j-1}
\]

are distinct integers in `[r,G_j(B)r]`. Hence

\[
r+j-1\le G_j(B)r.
\]

Under the non-descent assumption `(10)`, equation `(11)` gives

\[
\boxed{
 x_*(w)
 \ge
 {j-1\over G_j(B)-1}.}
\tag{20}
\]

Thus every acyclic Box-2 counterexample must pay one of two word-level resources:

```text
large proper-prefix surplus bank B,
```

or

```text
large real fixed-point threshold A_w/(2^j-3^q).
```

For bounded `B`, `(20)` has the asymptotic form

\[
x_*(w)
\ge
\bigl(e^{-7/9}3^{-B}-o(1)\bigr)j^{8/9}.
\tag{21}
\]

## 6. Source-qualified recurrence exclusion

The first-crossing remainder satisfies

\[
{A_w\over2^j}<{j\over2}.
\tag{22}
\]

Indeed, every odd additive contribution is

\[
{1\over2}{C_j\over C_m}< {1\over2},
\]

because `C_m>=1` at every proper prefix and `C_j<1`.

Let

\[
\lambda=j\log2-q\log3>0.
\]

A standard two-logarithm Baker bound supplies effectively computable constants `c_0,mu>0` such that

\[
\lambda\ge c_0j^{-\mu}.
\tag{23}
\]

Since `0<lambda<log2`,

\[
1-e^{-\lambda}\ge{\lambda\over2}.
\]

Equations `(22)--(23)` give

\[
\boxed{
 x_*(w)
 ={A_w/2^j\over1-3^q/2^j}
 <c_0^{-1}j^{\mu+1}.}
\tag{24}
\]

Fix `B_0` and `theta in (0,1)`. If `B(w)<=B_0` and a length

\[
L=\lfloor\theta j\rfloor
\]

factor repeats, equation `(17)` requires

\[
2^L
\le
\bigl(G_j(B_0)-1\bigr)x_*(w),
\]

but the left side is exponential in `j` while `(6)` and `(24)` make the right side polynomial. Therefore:

\[
\boxed{
\begin{minipage}{0.86\linewidth}
For fixed `B_0` and `theta>0`, every sufficiently long acyclic non-descending first-crossing word with `B(w)<=B_0` has all length-`floor(theta j)` factors distinct.
\end{minipage}}
\tag{25}
\]

This strengthens the low-complexity exclusion: a bounded-bank CST counterexample cannot contain even one repeated block at any fixed positive fraction of its length once the crossing is sufficiently late.

The quantitative constants in `(23)--(25)` remain source-qualified until the exact logarithmic-form theorem is frozen and independently reconstructed. Equations `(7)--(21)` are elementary and unconditional.

## 7. Strategic meaning

A late failure of Box 2 is no longer merely an arbitrary high-complexity word. It must simultaneously satisfy:

```text
one canonical positive root at or below x_*(w);
no positive cycle before the crossing;
all proper states confined to [r,G_j(B)r];
the exact factor-complexity floor (18);
the bank-gap lower bound (20);
and, at bounded bank, linear-scale factor uniqueness (25).
```

The remaining global task is to show that the first-crossing corridor itself forces enough repeated structure—or enough residue growth—to violate `(18)`.

## 8. Gap audit

- The theorem does not exclude words with a growing surplus bank `B(w)`.
- A finite word may have all long factors distinct; `(25)` is a strong recurrence obstruction, not by itself a contradiction.
- The positive-cycle alternative remains a separate full-denominator problem.
- The harmonic exponent `1/9` is safe rather than claimed optimal.
- No almost-everywhere or entropy-to-pointwise inference is used.
- Box 2, universal CST, and Collatz remain unproved.
