# Integral all-order composite jet descent

Date: 2026-07-22

Status: **all-order theorem**, scratch-only. The shared repository was not
edited. This note answers the proposed local-product question: the naive
product is false beyond the value jet, but every finite jet has an exact
integral finite-channel descent.

## 1. The normalized jet theorem

Write

\[
 S_A=2^A{2A\choose A},\qquad u=Am+r,\quad 0\le r<m,
\]

and let `zeta` be a primitive `m`-th root. For `j>=0` define

\[
 \mathcal J_j(A)={1\over S_A}[X^j]
 Q_{Am+r}^{(5)}(\zeta(1+X)).                         \tag{1}
\]

Then, for every fixed `m,r,j,zeta`,

\[
 \boxed{\mathcal J_j(A)\text{ is a polynomial in }A
        \text{ of degree at most }2j+1.}             \tag{2}
\]

This includes `m=1`, with `r=0,zeta=1`. Thus it also controls the
normalized Taylor jets of `Q_A^(5)` at 1.

## 2. Integral interpolation and the all-order lift

Fix `J>=0` and put `N=2J+1`. For `0<=t<=s<=A`, set

\[
 K_{A,s,t}={S_A\over S_t}{A\choose s}{s\choose t}.   \tag{3}
\]

Despite its displayed quotient, `K_(A,s,t)` is an integer. Newton
interpolation applied separately to (1) for `0<=j<=J` gives

\[
 \boxed{
 Q_{Am+r}^{(5)}(q)\equiv
 \sum_{s=0}^{N}\sum_{t=0}^{s}(-1)^{s-t}K_{A,s,t}
 Q_{tm+r}^{(5)}(q)
 \pmod{\Phi_m(q)^{J+1}}.}                           \tag{4}
\]

Here a binomial coefficient with `s>A` is zero. Formula (4) is in
`Z[q]`, so it may be reduced modulo every prime without introducing a
denominator.

When `A>N`, the double sum collapses to `N+1` channels:

\[
 Q_{Am+r}\equiv\sum_{t=0}^{N}M_{A,N,t}Q_{tm+r}
 \pmod{\Phi_m^{J+1}},                                \tag{5}
\]

\[
 \boxed{M_{A,N,t}=(-1)^{N-t}{S_A\over S_t}{A\choose t}
 {A-t-1\choose N-t}\in\mathbb Z.}                   \tag{6}
\]

For `A<=N`, (4) simply interpolates the node `A` and is tautological.

At `J=0`, (5) is the exact two-channel value descent

\[
 Q_{Am+r}\equiv S_A(1-A)Q_r+{AS_A\over4}Q_{m+r}
 \pmod{\Phi_m}.                                      \tag{7}
\]

Since `AS_A/4=Q_(A-1)(1)`, this is exactly the previously proved lower
formula. In the upper channel `Q_(m+r)(zeta)=12Q_r(zeta)`, and (7)
becomes

\[
 Q_{Am+r}(\zeta)=S_A(2A+1)Q_r(\zeta)
                 =Q_A(1)Q_r(\zeta).
\]

At `J=1`, `N=3`, so four fixed residual indices determine the complete
first jet. Explicitly, for `A>=4`, the coefficients of
`Q_r,Q_(m+r),Q_(2m+r),Q_(3m+r)` are

\[
 -{S_A(A-1)(A-2)(A-3)\over6},\quad
 {S_AA(A-2)(A-3)\over8},
\]

\[
 -{S_AA(A-1)(A-3)\over48},\quad
 {S_AA(A-1)(A-2)\over960}.                           \tag{8}
\]

## 3. A particularly clean two-channel defect recurrence

Define the value-level two-channel lift

\[
 B_A(q)=S_A(1-A)Q_r(q)+{AS_A\over4}Q_{m+r}(q),
 \qquad H_A(q)=Q_{Am+r}(q)-B_A(q).                   \tag{9}
\]

Then `H_0=H_1=0` identically and `Phi_m|H_A` for every `A`. Subtracting
the degree-one normalized family `B_A/S_A` from (4) shows that the same
all-order interpolation holds for `H_A`. In particular,

\[
 \boxed{
 H_A\equiv
 -{S_AA(A-1)(A-3)\over48}H_2
 +{S_AA(A-1)(A-2)\over960}H_3
 \pmod{\Phi_m^2}.}                                  \tag{10}
\]

This explains the empirically observed cubic first-defect dependence and
is the requested lower-channel lift using only `Q_(m+r)` and `Q_r`.

## 4. Product-defect lift in the upper channel

Put

\[
 E_A(q)=Q_{Am+r}(q)-Q_A(q^m)Q_r(q).                  \tag{11}
\]

The `m=1` case of (2), followed by the substitution
`q^m=(1+X)^m`, shows that every normalized jet of the product term also
has degree at most `2j+1` in `A`. Hence (4)--(6) remain valid with every
`Q_(tm+r)` replaced by `E_t`:

\[
 \boxed{E_A\equiv\sum_{t=0}^{2J+1}M_{A,2J+1,t}E_t
 \pmod{\Phi_m^{J+1}}\quad(A>2J+1).}                 \tag{12}
\]

For an upper-channel residual, every `E_t` is divisible by `Phi_m`, but
it is generally not divisible by `Phi_m^2`. The smallest clean exact
counterexample is

\[
 (m,A,r)=(5,1,2),
\]

for which

\[
 {Q_7(q)-Q_1(q^5)Q_2(q)\over\Phi_5(q)}
 \equiv-244+98q-134q^2+250q^3\pmod{\Phi_5(q)}.       \tag{13}
\]

Thus the tempting direct congruence modulo `Phi_m^2` is false. Formula
(12), not a one-channel factorization, is the correct all-order statement.

## 5. Proof of the degree bound

Use the exact block decomposition

\[
 Q_u=\sum_{b=0}^uD_{u,b}F_{u-b,b}.
\]

Write `b=Bm+t`, `0<=t<m`, and put

\[
 \delta=\lfloor(2r+1)/m\rfloor,
 \quad e={\bf1}_{t>r},\quad f=\lfloor(2t+1)/m\rfloor.
\]

The ordinary local order of `D` is

\[
 v=B+\delta+e-f.                                     \tag{14}
\]

We use one elementary period-product fact. For fixed `m,s`, after putting
`q=zeta(1+X)` and extracting the leading zero and factorial from
`(q;q)_(am+s)`, its normalized `X^ell` coefficient is a polynomial in
`a` of degree at most `2ell`. Indeed, the `ell`-th logarithmic coefficient
of each normalized factor is a polynomial of degree at most `ell` in its
period number. Summing over periods raises the degree by at most one;
exponentiating a partition of total weight `ell` gives degree at most
`ell + number_of_parts <= 2ell`. Ratios have the same bound.

Applying this to `D`, its leading factorial ratio is

\[
 { (2A+\delta)!(B!)^2\over
    A!(A-B-e)!(2B+f)!}.
\]

After division by `S_A`, it is `2^(-A)` times a polynomial in `A` of
degree `B+delta+e`. Therefore the coefficient `ell` steps above local
order in `D/S_A` is `2^(-A)` times a polynomial of degree at most

\[
 B+\delta+e+2\ell.                                   \tag{15}
\]

For `F`, write `u-b=(A-B-e)m+R`. Split its summation index as `Cm+d`.
The same period-product lemma gives a Gaussian-binomial jet equal to
`binom(A-B-e,C)` times a polynomial of degree at most twice the jet order
in `A,C`. The phase exponent is quadratic in `C`, so it obeys the same
bound. Binomial moments then give

\[
 [X^\ell]F_{u-b,b}(\zeta(1+X))
 =2^{A-B-e}\times\{
 \text{polynomial in }A\text{ of degree }\le2\ell\}. \tag{16}
\]

The borrowed states `d>R` start at order one with a factor `A-B-e-C`;
this still lies within the bound `2ell`.

For a block contributing to total jet `j`, combine (15)--(16) with
`ell_1+ell_2=j-v`. Its normalized degree is at most

\[
 B+\delta+e+2(j-v)
 =2j-B-\delta-e+2f\le2j+1.                           \tag{17}
\]

The last inequality uses `v>=0`: if `f=1`, then
`B+delta+e>=1`; if `f=0` it is immediate. Also `v<=j` forces
`B<=j+1`, so only finitely many blocks, independent of `A`, occur.
Falling factorials make the same polynomial formulas vanish automatically
when a nominal block lies beyond `b=u`. Summing proves (2).

## 6. Why the interpolation coefficients are integral

It is enough to prove

\[
 { {2A\choose A}{A\choose t}\over {2t\choose t}}
 \in\mathbb Z\qquad(0\le t\le A).                   \tag{18}
\]

For a prime-power denominator `d`, the corresponding Legendre summand is

\[
 \lfloor2A/d\rfloor-\lfloor A/d\rfloor
 -\lfloor(A-t)/d\rfloor+\lfloor t/d\rfloor
 -\lfloor2t/d\rfloor.
\]

Writing `a=A mod d`, `b=t mod d`, this equals

\[
 {\bf1}_{2a\ge d}+{\bf1}_{a<b}-{\bf1}_{2b\ge d}\ge0:
\]

if the last indicator is one, either `a>=b` makes the first one, or
`a<b` makes the second one. This proves (18), hence (3). The alternating
partial-binomial identity gives (6). Finally, divisibility at every
primitive root to order `J+1` is equivalent in characteristic zero to
divisibility by `Phi_m^(J+1)`; monicity and Gauss's lemma upgrade the
rational divisibility to `Z[q]`.

## 7. Exact audit

`experiments/X-9876-period-four-quotient-audits/check_composite_all_order_jet_descent.js`
checks with exact
`BigInt` polynomial arithmetic:

1. the integral coefficient lemma over a large finite box;
2. (4)--(8) through zero, first, and second local jets in independent
   composite states;
3. the two-defect first-jet recurrence (10);
4. the product-defect recurrence (12); and
5. the exact nonzero quotient (13).

The audit is finite; the period-product argument proves the theorem for
all indices and every jet order.


