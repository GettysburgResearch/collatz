# First-jet q-Lucas descent at a residual cyclotomic order

Date: 2026-07-22

Status: **all-order lemma**, scratch-only.  The shared repository was not
edited.  This lifts the exact value descent by one local jet.  In particular,
after peeling an odd prime `p`, divisibility by `Phi_m^2` is reduced to a
finite set of residual Rogers--Szego value/derivative states.  Higher jets,
which are needed when `phi(p^k)>2`, remain open.

## 1. A normalized factorial with an explicit first jet

Fix `m>=2` and a primitive `m`-th root `zeta`.  For `a>=0` and
`0<=s<m`, define

\[
 \mathcal H_{a,s}(q)=
 \frac{(q;q)_{am+s}}{(1-q^m)^a}.                    \tag{1}
\]

The quotient is a polynomial: one copy of `1-q^m` is removed from every
factor `1-q^(jm)`.  Put `P_s=(zeta;zeta)_s`.  Splitting the nonmultiples of
`m` into complete blocks gives

\[
 \boxed{\mathcal H_{a,s}(\zeta)=m^a a!P_s.}         \tag{2}
\]

Its logarithmic derivative in characteristic zero is

\[
\begin{aligned}
 \mathcal L_{a,s}:={\mathcal H'_{a,s}(\zeta)
                         \over\mathcal H_{a,s}(\zeta)}
 ={}&{m\zeta^{-1}a(a-1)\over4}\\
 &-\sum_{j=0}^{a-1}\sum_{i=1}^{m-1}
 { (jm+i)\zeta^{i-1}\over1-\zeta^i}
 -\sum_{i=1}^{s}{(am+i)\zeta^{i-1}\over1-\zeta^i}.
                                                               \tag{3}
\end{aligned}
\]

Indeed, the normalized multiple factor is

\[
 {1-q^{jm}\over1-q^m}=1+q^m+\cdots+q^{m(j-1)},
\]

whose logarithmic derivative at `zeta` is
`m zeta^(-1)(j-1)/2`; summing `j` gives the first term of (3).  The other
terms are ordinary logarithmic derivatives of `1-q^(jm+i)`.

For fixed `(m,s,zeta)`, expression (3) is a quadratic polynomial in `a`.
Every denominator `1-zeta^i`, `0<i<m`, is a unit after reduction modulo an
odd prime not dividing `m`.

## 2. Exact first-jet q-Lucas formula

Write `N=Am+R`, `c=Cm+d`, with `0<=R,d<m`.  Let

\[
 G_{N,c}(q)={N\brack c}_q.
\]

When `d<=R`, its `Phi_m`-order is zero.  Equations (1)--(3) give

\[
\boxed{\begin{aligned}
G_{N,c}(\zeta)
 &=\binom AC{R\brack d}_{\zeta},\\
G'_{N,c}(\zeta)
 &=G_{N,c}(\zeta)
   \{\mathcal L_{A,R}-\mathcal L_{C,d}
                         -\mathcal L_{A-C,R-d}\}.
\end{aligned}}                                                   \tag{4}
\]

When `d>R`, necessarily `C<=A-1`; the Gaussian polynomial has one simple
`Phi_m` zero.  Removing its single factor `1-q^m` gives

\[
\boxed{\begin{aligned}
G_{N,c}(\zeta)&=0,\\
G'_{N,c}(\zeta)
 &=-m^2\zeta^{-1}(A-C)\binom AC
   {P_R\over P_dP_{m+R-d}}.
\end{aligned}}                                                   \tag{5}
\]

The extra factor `m` in (5) comes from the complete nonmultiple block in
(2), while `(1-q^m)'|_(q=zeta)=-m zeta^(-1)` supplies the other one.

Although (4) was written using logarithmic derivatives, the products on its
right are division-free algebraic identities after the displayed
cyclotomic units are inverted.  They therefore reduce in every odd
characteristic `p` with `p` not dividing `m`, including cases in which an
ordinary binomial coefficient vanishes modulo `p`.

## 3. Finite first-jet state for the Rogers--Szego block

Recall

\[
 F_{N,b}(q)=\sum_{c=0}^{N}
 q^{E_b(c)}{N\brack c}_q,
 \qquad E_b(c)=(b+c)(b+c+1)+b(b+1).                \tag{6}
\]

Insert (4)--(5) into the derivative of (6).  For `d<=R`, the summand with
`c=Cm+d` is

\[
 \zeta^{E_b(d)}\binom AC{R\brack d}_{\zeta}
 \{E_b(Cm+d)\zeta^{-1}
   +\mathcal L_{A,R}-\mathcal L_{C,d}
                         -\mathcal L_{A-C,R-d}\}.                \tag{7}
\]

For `d>R`, it is

\[
 -\zeta^{E_b(d)}m^2\zeta^{-1}(A-C)\binom AC
 {P_R\over P_dP_{m+R-d}}.                                      \tag{8}
\]

Here `zeta^(E_b(Cm+d))=zeta^(E_b(d))`.  The remaining dependence on `C`
in (7) is quadratic, and in (8) is linear.  Consequently the complete sum
over `C` uses only

\[
 \sum_C\binom AC=2^A,
 \quad\sum_CC\binom AC=A2^{A-1},
 \quad\sum_CC^2\binom AC=A(A+1)2^{A-2}.             \tag{9}
\]

Thus both `F_(Am+R,b)(zeta)` and its first derivative reduce to finitely
many states indexed by

\[
 (R,\ b\bmod m,\ d),\qquad 0\le R,d<m,             \tag{10}
\]

with explicit coefficients polynomial in `A` times powers of two.  This is
the promised first-jet strengthening of value q-Lucas; it does not merely
assert that a finite algorithm exists.

## 4. Only two quotient layers can affect the first jet of `Q`

Write

\[
 u=Am+r,\quad b=Bm+t,
\]

and set

\[
 \delta=\left\lfloor{2r+1\over m}\right\rfloor,
 \quad e={\bf1}_{t>r},
 \quad f=\left\lfloor{2t+1\over m}\right\rfloor.
\]

For the factorial block in

\[
 Q_u^{(5)}=\sum_bD_{u,b}F_{u-b,b},
\]

the ordinary local order is

\[
 v_m(D_{u,b})=B+\delta+e-f.                         \tag{11}
\]

If `B>=2`, then the right side is at least one.  Equality could occur only
at `B=2`, `delta=e=0`, `f=1`; but `delta=e=0` implies
`t<=r<(m-1)/2`, contradicting `f=1`.  Hence

\[
 \boxed{v_m(D_{u,b})\le1\quad\Longrightarrow\quad B\le1.}       \tag{12}
\]

Blocks with order at least two have zero value and zero derivative.  Every
first jet of `Q_u` therefore comes only from `b=t` and `b=m+t`, with
`0<=t<m`.

For completeness, these block jets are explicit from (1)--(3).  If
`v=v_m(D_(u,b))`, write each factorial in `D` as
`(1-q^m)^(floor(n/m)) H_(floor(n/m),n mod m)`.  The remaining ratio is a
unit `K_(u,b)`.  Then

\[
\begin{array}{c|cc}
v&D_{u,b}(\zeta)&D'_{u,b}(\zeta)\\ \hline
0&K_{u,b}(\zeta)&K_{u,b}(\zeta)\,\Delta\mathcal L_{u,b}\\
1&0&-m\zeta^{-1}K_{u,b}(\zeta),
\end{array}                                                       \tag{13}
\]

where `Delta L` is the numerator-minus-denominator combination of (3).
The value `K(zeta)` is the exact integer factorial ratio times the residual
`P_s` ratio supplied by (2); it is evaluated over the integers before any
finite-field reduction.

Combining (7)--(8) and (13) yields the finite formula

\[
\boxed{\begin{aligned}
Q_u(\zeta)&=\sum_{B=0,\ v=0}K_{u,b}(\zeta)F_{u-b,b}(\zeta),\\
Q'_u(\zeta)&=
 \sum_{B=0,\ v=0}K_{u,b}(\zeta)
   \{\Delta\mathcal L_{u,b}F_{u-b,b}(\zeta)
                         +F'_{u-b,b}(\zeta)\}\\
&\quad-
 \sum_{B\in\{0,1\},\ v=1}
 m\zeta^{-1}K_{u,b}(\zeta)F_{u-b,b}(\zeta).
\end{aligned}}                                                   \tag{14}
\]

All sums in (14) have fewer than `2m` block indices, regardless of `u`.

## 5. Exact multiplicity-two consequence

Let `p` be odd and `p` not divide `m`.  Since `Phi_m` is squarefree modulo
`p`, for every polynomial `P`

\[
 \Phi_m^2\mid P\pmod p
 \quad\Longleftrightarrow\quad
 P\equiv0\pmod{\Phi_m},\quad P'\equiv0\pmod{\Phi_m}.             \tag{15}
\]

Equations (7)--(14) therefore turn the first nontrivial peeled threshold
into two explicit finite residual identities.  In particular, for a peeled
factor `p^1` with `p=3`, proving the second identity nonzero immediately
gives the required strict deficit below `phi(3)=2`.

This does not claim that the residual derivative is always nonzero.  For
example, zero-order prime selection already fails at `(u,L)=(4,12)`:
both peeled residual values vanish, although their multiplicities are only
one.  Formula (14), rather than a value-only argument, is the correct next
state for that family.

## 6. Exact audit

`experiments/X-9876-period-four-quotient-audits/check_composite_first_jet_descent.js`
uses exact q-polynomials
and modular evaluations at certified primitive roots.  It verifies:

* (4)--(5) in 666 Gaussian states;
* the finite reconstruction (7)--(8) in 270 Rogers--Szego states; and
* the `B<=1` truncation (12)--(14) in 40 complete `Q` states.

The checker uses primes larger than 200 solely as exact finite-field audit
rings; the proof above is algebraic and holds for all permitted
characteristics.


