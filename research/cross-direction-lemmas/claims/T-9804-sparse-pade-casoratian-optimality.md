# T-9804 -- Sparse scalar Pade orders have an exact consecutive-order accuracy deficit

Claim ID: `T-9804`
Title: Every sparse equal-allocation Pade Casoratian is nonzero, and skipped orders strictly lose normalized 2-adic accuracy at fixed width and largest order
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave13-adelic-bridge`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR20/L-9408`, `PR20/L-9410`, local `L-9884`, `L-9891`, and `L-9895`; compared with `PR20/R-9407` at `ed1ee9d9d6c8fa6c79f63267a296c2e0df17b6d8`
Scope: monomial-aligned scalar combinations of arbitrary distinct equal-allocation periodic block-Pade orders
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Fix the positive word `W` and the notation of `L-9891`:

\[
T={64\over81},\qquad r=|W|,\qquad S=S(W)>0,
\qquad Z=T^\zeta.
\tag{1}
\]

For the equal-allocation Pade error of order `t>=1`, write

\[
E_t(Y)
=B_t(Y)F(Y)-A_t(Y)
=Y^{(r+1)t}\sum_{\ell\ge0}g_{t,\ell}Y^\ell.
\tag{2}
\]

Every `g_(t,ell)` is nonzero.  Put

\[
V(t,\ell):=v_2(g_{t,\ell}).
\tag{3}
\]

The completed-window valuation formula of `L-9891/(7)--(8)` is

\[
\boxed{
V(t,\ell)=U(t)+W(\ell)+54Sr\,t\ell,
}
\tag{4}
\]

where

\[
U(t)=6\{\zeta(r+1)t+9S L_{r,t}\},
\tag{5}
\]

\[
W(\ell)=6\left\{\zeta\ell
+9S{r\ell(\ell-1)\over2}\right\}.
\tag{6}
\]

In particular,

\[
\boxed{
V(t,\ell+1)-V(t,\ell)
=6\{\zeta+9Sr(t+\ell)\}>0.
}
\tag{7}
\]

At the prime `3`, `L-9895` gives

\[
v_3(g_{t,\ell})=-4P(t,\ell),
\tag{8}
\]

where `P` has the separated form

\[
P(t,\ell)=\widetilde U(t)+\widetilde W(\ell)
+9Sr(r+1)t\ell.
\tag{9}
\]

Only the positive mixed coefficients in (4) and (9) will matter.

## Theorem 1 -- arbitrary sparse minors have opposite unique tropical terms

Let

\[
1\le t_0<t_1<\cdots<t_{q-1},
\qquad
0\le c_0<c_1<\cdots<c_{q-1},
\qquad q\ge2,
\tag{10}
\]

and define the sparse coefficient minor

\[
\Delta_{\mathbf t}(\mathbf c)
:=\det(g_{t_i,c_j})_{0\le i,j<q}.
\tag{11}
\]

Then this determinant is nonzero.  Its exact `2`-adic valuation is selected
by the reverse permutation:

\[
\boxed{
v_2(\Delta_{\mathbf t}(\mathbf c))
=\sum_{i=0}^{q-1}V(t_i,c_{q-1-i}).
}
\tag{12}
\]

Its exact `3`-adic valuation is selected by the identity permutation:

\[
\boxed{
v_3(\Delta_{\mathbf t}(\mathbf c))
=-4\sum_{i=0}^{q-1}P(t_i,c_i).
}
\tag{13}
\]

Both selecting permutations are unique.

### Proof

For a permutation `pi`, (4) gives the valuation of its determinant term as

\[
\sum_iU(t_i)+\sum_jW(c_j)
+54Sr\sum_i t_i c_{\pi(i)}.
\tag{14}
\]

The first two sums are independent of `pi`.  Since the `t_i` and `c_j` are
strictly increasing, the strict rearrangement inequality makes the reverse
permutation the unique minimizer of the last sum.  One determinant term is
therefore uniquely least at `2`, proving both nonvanishing and (12).

Equations (8)--(9) similarly reduce the `3`-adic comparison to

\[
-36Sr(r+1)\sum_i t_i c_{\pi(i)}.
\tag{15}
\]

The identity permutation uniquely maximizes the unsigned sum and hence
uniquely minimizes (15).  This proves (13). **QED**

## Theorem 2 -- exact sparse coupling and evaluated error

Put

\[
t_*:=t_{q-1},
\qquad
\widetilde E_i(Y)
:=Y^{(r+1)(t_*-t_i)}E_{t_i}(Y).
\tag{16}
\]

Thus all errors begin at the same degree:

\[
\widetilde E_i(Y)
=Y^{(r+1)t_*}\sum_{\ell\ge0}g_{t_i,\ell}Y^\ell.
\tag{17}
\]

For `0<=i<q`, let `d_i` be the signed cofactor obtained from the first
`q-1` coefficient columns `0,...,q-2` after deleting row `i`.  Define

\[
\mathcal E_{\mathbf t}(Y)
:=\sum_{i=0}^{q-1}d_i\widetilde E_i(Y).
\tag{18}
\]

For `ell>=q-1`, abbreviate

\[
\Delta_{\mathbf t}(\ell)
:=\Delta_{\mathbf t}(0,1,\ldots,q-2,\ell).
\tag{19}
\]

Then

\[
\boxed{
\mathcal E_{\mathbf t}(Y)
=Y^{(r+1)t_*}
 \sum_{\ell\ge q-1}\Delta_{\mathbf t}(\ell)Y^\ell.
}
\tag{20}
\]

In particular the sparse coupling cancels exactly `q-1` further blocks and
not `q`.  Moreover,

\[
\boxed{
v_2(\Delta_{\mathbf t}(\ell))
=V(t_0,\ell)
 +\sum_{i=1}^{q-1}V(t_i,q-1-i)
\qquad(\ell\ge q-1),
}
\tag{21}
\]

and these valuations strictly increase with `ell`.  Hence

\[
\boxed{
v_2(\mathcal E_{\mathbf t}(1))
=v_2(\Delta_{\mathbf t}(q-1)).
}
\tag{22}
\]

The coupling is an actual rational approximant.  Put

\[
\mathcal B_{\mathbf t}
:=\sum_{i=0}^{q-1}d_iB_{t_i}(1),
\qquad
\mathcal A_{\mathbf t}
:=\sum_{i=0}^{q-1}d_iA_{t_i}(1).
\tag{23}
\]

Then

\[
\boxed{
\mathcal B_{\mathbf t}\ne0,
\qquad
v_2(\mathcal B_{\mathbf t})=v_2(d_{q-1}),
}
\tag{24}
\]

and the normalized evaluated error has the exact valuation

\[
\boxed{
\begin{aligned}
v_2\left(
F(1)-{\mathcal A_{\mathbf t}\over\mathcal B_{\mathbf t}}
\right)
={}&V(t_*,0)\\
&+6\sum_{i=0}^{q-2}
 \{\zeta+9Sr(t_i+q-2-i)\}.
\end{aligned}
}
\tag{25}
\]

### Proof

Laplace expansion in the last column gives

\[
\sum_i d_i g_{t_i,\ell}
=\det(g_{t_i,c_j}),
\tag{26}
\]

where the columns are `0,...,q-2,ell`.  This determinant is zero for
`ell<q-1` because its last column repeats an earlier column.  At
`ell=q-1` it is nonzero by Theorem 1.  This proves (20) and exact
cancellation order.

For `ell>=q-1`, the reverse permutation sends row `t_0` to the last column
and row `t_i`, `i>=1`, to column `q-1-i`.  Equation (12) gives (21).
Only `V(t_0,ell)` changes with `ell`, so (7) makes the valuations strictly
increase.  The first term therefore controls the convergent value at `Y=1`,
proving (22).

The reverse matching in `d_i` uses the ordered row set with `t_i` omitted.
Comparing consecutive omissions changes only the row assigned to column
`q-2-i`, and gives

\[
\boxed{
v_2(d_i)-v_2(d_{i+1})
=V(t_{i+1},q-2-i)-V(t_i,q-2-i)>0.
}
\tag{27}
\]

The positivity follows from (4)--(6) and the strict increase of `U`, already
computed in `L-9891/(29b)`.  Thus `d_(q-1)` is the unique cofactor of least
`2`-adic valuation.  Every `B_t(1)` is a `2`-adic unit, so it uniquely
controls the sum in (23), proving (24).

The reverse term of `Delta_t(q-1)` has valuation

\[
V(t_*,0)+\sum_{i=0}^{q-2}V(t_i,q-1-i),
\tag{28}
\]

whereas the reverse term of `d_(q-1)` has valuation

\[
\sum_{i=0}^{q-2}V(t_i,q-2-i).
\tag{29}
\]

Subtract (29) from (28), apply (7), and use
`mathcal E_t(1)=mathcal B_t F(1)-mathcal A_t`.  This proves (25). **QED**

## Theorem 3 -- skipped orders have an exact accuracy deficit

For `0<=i<=q-2`, define the nonnegative order deficits

\[
\delta_i
:=t_*-(q-1-i)-t_i\ge0.
\tag{30}
\]

Then (25) is exactly

\[
\boxed{
\begin{aligned}
v_2\left(
F(1)-{\mathcal A_{\mathbf t}\over\mathcal B_{\mathbf t}}
\right)
={}&V(t_*,0)
+6(q-1)\{\zeta+9Sr(t_*-1)\}\\
&-54Sr\sum_{i=0}^{q-2}\delta_i.
\end{aligned}
}
\tag{31}
\]

Therefore, among every `q`-element order set with fixed largest order `t_*`,
the normalized `2`-adic error valuation is uniquely maximized by

\[
\boxed{
(t_0,t_1,\ldots,t_{q-1})
=(t_*-q+1,t_*-q+2,\ldots,t_*).
}
\tag{32}
\]

Every omitted intermediate order loses at least `54Sr` valuation units, and
the total loss is exactly `54Sr sum delta_i`.

### Proof

Strict increase of the integer orders gives

\[
t_i\le t_*-(q-1-i),
\tag{33}
\]

which proves `delta_i>=0`.  Substitute

\[
t_i+q-2-i=t_*-1-\delta_i
\tag{34}
\]

in (25).  This gives (31).  Equality with the consecutive-order value holds
only when every `delta_i=0`, which is exactly (32).  If the set is not
consecutive, at least one integral deficit is positive. **QED**

## Theorem 4 -- arbitrary sparse cofactors retain the two-place obstruction

The cofactor valuations run in opposite directions.  Equation (27) shows
that they strictly decrease with `i` at `2`, while Theorem 1's identity
matching gives

\[
\boxed{
v_3(d_{i+1})-v_3(d_i)
=4\{P(t_{i+1},i)-P(t_i,i)\}>0.
}
\tag{35}
\]

Consequently `d_(q-1)` is uniquely smallest at `2`, while `d_0` is uniquely
smallest at `3`.  If

\[
S_2:=v_2(d_0)-v_2(d_{q-1}),
\qquad
S_3:=v_3(d_{q-1})-v_3(d_0),
\tag{36}
\]

then

\[
\boxed{
S_2=\sum_{i=0}^{q-2}
 \{V(t_{i+1},q-2-i)-V(t_i,q-2-i)\}>0,
}
\tag{37}
\]

\[
\boxed{
S_3=4\sum_{i=0}^{q-2}
 \{P(t_{i+1},i)-P(t_i,i)\}>0.
}
\tag{38}
\]

After clearing the rational cofactor vector and dividing by its common
integer gcd, its primitive projective height satisfies

\[
\boxed{
H_{\rm proj}(d_0:\cdots:d_{q-1})
\ge\max\{2^{S_2},3^{S_3}\}.
}
\tag{39}
\]

### Proof

For the `3`-adic identity matching, comparing the minors omitting `t_i` and
`t_(i+1)` changes only the row paired with column `i`.  Since `P(t,i)`
strictly increases with `t`, this proves (35).  Telescoping (27) and (35)
gives (37)--(38).  Finally,

\[
v_2(d_0/d_{q-1})=S_2,
\qquad
v_3(d_0/d_{q-1})=-S_3.
\tag{40}
\]

In lowest terms, the numerator of this ratio is divisible by `2^(S_2)` and
its denominator by `3^(S_3)`; both occur among the coordinates of every
primitive integral representative.  This proves (39). **QED**

## What this advances

- `L-9891` treated consecutive orders.  Theorems 1--2 close every finite
  sparse scalar order set: all minors are nonzero and exactly `q-1` further
  blocks can be cancelled.
- Theorem 3 proves a strict optimization statement, not just nonvanishing:
  at fixed largest order and width, consecutive orders uniquely maximize the
  normalized `2`-adic error valuation.  Skipping orders cannot be the missing
  scalar cancellation mechanism.
- At the refreshed PR-20 head, `R-9407` shows that even the optimistic
  adjacent-order scalar benchmark is subcritical at period ten.  Theorem 3
  closes the apparent sparse-order escape from that ceiling: skipped scalar
  orders have a quantified accuracy deficit before any height cost is charged.
- Theorem 4 shows that sparse choices retain the opposite `2`/`3` tropical
  endpoint obstruction of `L-9895`.

## Dependency audit

- `PR20/L-9408` and `PR20/L-9410` supply the rational periodic Pade pairs and
  the fact that every evaluated denominator `B_t(1)` is a `2`-adic unit.
- `L-9884` supplies post-window phase noncancellation.
- `L-9891` supplies the exact `2`-adic coefficient formula (4)--(7) and the
  aligned-error construction in the consecutive special case.
- `L-9895` supplies the exact `3`-adic coefficient formula (8)--(9).
- Refreshed `PR20/R-9407` supplies the period-ten ceiling only as context; it
  is not used in the determinant proof.
- The new proof is strict rearrangement plus determinant/cofactor algebra for
  arbitrary order sets.

## Gap and scope audit

- The theorem concerns scalar combinations of equal-allocation Pade errors
  after their unique monomial alignment.  Unequal allocations inside each
  constituent, polynomial multipliers with several coefficients, and genuine
  Hermite--Pade systems remain outside it.
- Consecutive orders maximize exact `2`-adic accuracy at fixed `t_*` and `q`.
  This does not prove that they optimize the final accuracy-to-height ratio;
  sparse orders may change archimedean or other-prime height.
- The projective coefficient height in (39) can still cancel between the
  evaluated numerator and denominator, exactly as in `R-9805`.
- No irrationality theorem, period-four closure theorem, or Collatz
  conclusion is claimed.

## Adversarial checks

- For `q=2`, Theorem 1 selects
  `V(t_0,c_1)+V(t_1,c_0)` at `2` and
  `-4(P(t_0,c_0)+P(t_1,c_1))` at `3`, recovering the opposite terms in the
  first Casoratian.
- For `q=2`, equation (25) becomes
  `V(t_1,0)+6{zeta+9Sr t_0}`.  If `t_0=t_1-1-delta`, the loss from the
  adjacent pair is exactly `54Sr delta`.
- For `(t_0,t_1,t_2)=(2,4,7)`, the deficits are `(3,2)`, so (31) predicts a
  loss of exactly `270Sr` from the consecutive triple `(5,6,7)`.
- Distinct order and column indices are essential.  Repeated columns make a
  determinant zero, and repeated rows are the same approximant twice.
- The monomial shifts in (16) are formal alignment data; they evaluate to one
  and therefore do not alter the rational pair in (23).

## Remaining uncertainty

Can a genuinely coupled Hermite--Pade system, or a polynomial multiplier
with several independent coefficients, trade a lower scalar valuation for a
larger reduction in global height?  This theorem closes sparse order
selection only inside the scalar aligned family.

## Suggested next attack

Construct the smallest two-function Hermite--Pade matrix whose rows are not
all shifts of one scalar error.  Its coefficient valuation must first be
tested for a strict tropical assignment; only after that should its reduced
height be compared with the exact scalar ceiling above.
