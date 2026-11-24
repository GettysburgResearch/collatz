# A finite negative-integer potential and its missing rational poles

**PROPOSED written construction and refutation of its closing inequality.**
This was a direct attempt to construct the finite ordinary supersolution
required by the biased series. It produces a positive potential, finite
at every positive integer with an explicit linear bound. Its required
forward inequality fails. The failure also excludes every potential of
the stated discrete form with a finite first moment. It does not exclude
diffuse measures or arbitrary ordinary functions.

## A negative ancestor measure with finite first moment

Write a negative ordinary integer as `-h`, with `h>=1`. The two inverse
shortcut branches on magnitudes are

\[
 I_0(h)=2h,\qquad I_1(h)=(2h+1)/3.
\]

Choose them with probabilities `1/3` and `2/3`, respectively, and kill a
path whenever its odd inverse is not an integer. That inverse is legal
exactly when `h=1 mod 3`. The resulting substochastic operator is

\[
 (Kf)(h)=\tfrac13 f(2h)+
 \tfrac23\mathbf1_{h\equiv1\ (3)} f((2h+1)/3).
\]

Start at magnitude one. Let `mu(h)` be the total expected number of
visits to `h` before killing, including clock zero. These weights are
specified by finite inverse words; no positive Collatz convergence
assumption enters their definition.

For `f(h)=h+32/13`, direct enumeration of two branch choices gives

\[
 K^2 f(h)\le \frac{76}{81}f(h),\qquad
 Kf(h)\le\frac{10}{9}f(h),\qquad h\ge1.                 \tag{1}
\]

Here is the whole residue calculation, before the substitution for the
constant `c` in `f(h)=h+c`:

| Initial residue | `K^2 f(h)` |
|---|---|
| `h=0 mod 3` | `4h/9+c/9` |
| `h=2 mod 3` | `20h/27+c/3+2/27` |
| `h=4 or 7 mod 9` | `20h/27+c/3+4/27` |
| `h=1 mod 9` | `76h/81+7c/9+32/81` |

The last row is exactly `(76/81)(h+c)` when `c=32/13`.
The other rows are smaller. Positivity of `K`, finite partial sums and
the geometric series now give

\[
 \sum_{h\ge1}\mu(h)(h+32/13)
 =\sum_{k\ge0}(K^k f)(1)
 \le\frac{1+10/9}{1-76/81}\frac{45}{13}
 =\frac{1539}{13}.                                   \tag{2}
\]

Thus this is a finite positive measure with finite first moment on
negative ordinary centers. In particular `mu(2)>=1/3`, from the single
even inverse of the root.

Its exponential valuation potential is

\[
 V(n)=\sum_{h\ge1}\mu(h)2^{v_2(n+h)},\qquad n\ge1.
\]

Since a power of two dividing the positive integer `n+h` is at most
`n+h`, (2) proves

\[
 0<V(n)\le \frac{1539}{13}(n+1)<\infty.
\]

This meets the automatic-finiteness part of the attempted construction.
It does not meet the supersolution inequality.

## A residue limit forces every missing inverse pole

The following argument applies to **any** nonnegative weights `nu(h)`
with finite `sum h*nu(h)`. Put
`V_nu(n)=sum nu(h)*2^v_2(n+h)`.
For a binary integer `r`, choose positive representatives
`n_k=r mod 2^(k+1)` with `n_k<=2^(k+1)`. If there is no atom at `-r`
among these negative ordinary centers, then

\[
                         2^{-k}V_\nu(n_k)\longrightarrow0.       \tag{3}
\]

For every fixed center with positive weight, `r+h` is nonzero. Once
`k` exceeds its valuation, `v_2(n_k+h)=v_2(r+h)` is fixed. Each normalized
summand therefore tends to zero. It is dominated by

\[
 2^{-k}2^{v_2(n_k+h)}\le 2+h,
\]

whose weighted sum is finite. Splitting into a finite set of centers
and its uniformly small moment tail proves (3); no interchange of an
unbounded unweighted sum is used.

Suppose a nonzero such measure gave the desired inequalities

\[
 V_\nu(n)\ge1+c(n)V_\nu(Tn),\qquad
 c(n)=\begin{cases}2/3&n\text{ even},\\4/3&n\text{ odd}.
 \end{cases}                                                   \tag{4}
\]

First let `t` have positive weight and `t!=1 mod 3`. The odd binary
integer `r=-(2t+1)/3` is not an ordinary integer, so (3) applies to it.
But `T(n_k)+t=0 mod 2^k`, and hence

\[
 2^{-k}V_\nu(Tn_k)\ge\nu(t)>0.
\]

This contradicts (4). Every supported `t` must consequently be `1 mod 3`.
Choose any one of them. Now `2t=2 mod 3`, so its weight has just been
forced to zero. Apply (3) instead to `r=-2t`, using even representatives.
Their halved endpoints again satisfy `T(n_k)+t=0 mod 2^k`, giving the
same contradiction with the even coefficient `2/3` in (4). Thus **no
nonzero measure in this finite-first-moment discrete class works**.

For the explicitly constructed Green measure, the single center `t=2`
already obstructs the odd inequality at the lifts of `r=-5/3`.
Rescaling the measure or adding a constant to the potential cannot fix
this argument: constants disappear in (3). More generally the same is
true of adding a function `b(n)=o(n)` at both sides of (4), since its
normalized values along these representatives and their images vanish.

This identifies the exact loss in the attempted shortcut. Preserving
the pole at a negative integer target forces rational inverse centers
with increasing powers of three in their denominators. Restricting to
negative integer centers made finiteness easy by removing those centers.
The original diffuse biased measure does retain their arithmetic, and
its potential at all positive integers remains unproved.

**Evidence.** The residue formulas and constants are written elementary
proofs. `checks/negative_kernel_control.py` independently evaluates the
two-step operator on all nine residue representatives and a range of
ordinary heights, and checks finite Green sums against (2). No part of
this note is claimed as Lean formalized.
