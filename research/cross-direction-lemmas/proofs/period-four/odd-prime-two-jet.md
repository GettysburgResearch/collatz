# Odd-prime Taylor cancellation dies within two jets

Date: 2026-07-22

Status: scratch-only theorem checkpoint.  The shared repository was not
edited.  This note uses the already proved two-level block decomposition and
its exact local valuation formula.  It proves the previously open odd-prime
cancellation estimate.

## 1. Statement

Fix an odd prime `p`, put `x=q-1`, and define

\[
 W(n)=\sum_{j=1}^n p^{v_p(j)},\qquad
 V_b=W(2u+1)-W(u)-W(u-b)-W(2b+1)+2W(b).
\]

The exact block decomposition is

\[
 Q_u^{(5)}=\sum_{b=0}^uD_{u,b}F_{u-b,b},
\]

where the `b`-block has exact `x`-order `V_b` over `F_p`, because
`F_{u-b,b}(1)=2^(u-b)` is a unit.  Put

\[
 m=\min_{0\le b\le u}V_b,
 \qquad
 M=\operatorname{ord}_{x=0}Q_u^{(5)}(1+x)\pmod p.
\]

Then

\[
 \boxed{M\le m+2.}                                            \tag{1}
\]

For

\[
 V_0=W(2u+1)-2W(u)-1,
\]

this implies the required structural estimate

\[
 \boxed{M\le 2V_0+1.}                                        \tag{2}
\]

Indeed `m<=V_0`.  If `V_0>0`, its carry formula makes it a
positive multiple of `p-1`, hence `V_0>=2`, and (1) gives
`M<=V_0+2<=2V_0`.  If `V_0=0`, the carry-free evaluation

\[
 Q_u^{(5)}(1)=(2u+1)2^u{2u\choose u}
\]

is a `p`-adic unit, so `M=0`.

Combined with the already proved inequality

\[
 2V_0+1<\varphi(p^k)\qquad(p^k>2u+1),
\]

equation (2) excludes every odd prime-power cyclotomic order above the
cutoff.

## 2. Tropical minimizers are three central indices

Set

\[
 C(b)=W(2b+1)-2W(b)-1,
 \qquad
 I(u,b)=W(u)-W(u-b).
\]

Then

\[
 V_b=V_0+I(u,b)-C(b).                                  \tag{3}
\]

Let

\[
 h_e={p^e-1\over2}\qquad(e\ge0).
\]

In the addition `b+b+1`, let `c_i` be the carry into digit `i`.  The
standard digit formula for `W` gives

\[
 C(b)=(p-1)\sum_{i\ge1}c_i p^{i-1}.                    \tag{4}
\]

Choose the unique `e` with `h_e<=b<h_(e+1)`.  There is no carry beyond
digit `e`, so

\[
 C(b)\le p^e-1=C(h_e).
\]

Every summand in the interval weight is at least one, hence

\[
 I(u,b)-I(u,h_e)\ge b-h_e.
\]

Substitution in (3) proves

\[
 \boxed{V_b\ge V_{h_e}+b-h_e}.                         \tag{5}
\]

Thus every global minimizer is central.

Only the first three central indices can minimize.  Indeed, with

\[
 \Delta_e=h_{e+1}-h_e={(p-1)p^e\over2},
\]

we have

\[
 V_{h_{e+1}}-V_{h_e}
 =\sum_{n=u-h_{e+1}+1}^{u-h_e}p^{v_p(n)}-2\Delta_e.     \tag{6}
\]

For `e>=2`, the interval length `Delta_e` is divisible by `p^2`.  It
contains exactly `Delta_e/p` multiples of `p` and `Delta_e/p^2` multiples
of `p^2`.  Therefore its weight is at least

\[
 \Delta_e+(p-1){\Delta_e\over p}
 +(p^2-p){\Delta_e\over p^2}
 =\left(3-{2\over p}\right)\Delta_e>2\Delta_e.          \tag{7}
\]

So the central values increase strictly after `h_2`.

Finally `W(n)=n mod (p-1)`, and direct substitution gives

\[
 V_b\equiv b\pmod{p-1}.                                \tag{8}
\]

Now `h_0` and `h_2` are zero modulo `p-1`, whereas
`h_1=(p-1)/2` is not.  Consequently

\[
 \boxed{\text{the minimum is unique, or its minimizer set is exactly }
 \{0,h_2\}.}                                            \tag{9}
\]

## 3. Exact description of the tied state

Write

\[
 a={p-1\over2},\qquad h=h_2={p^2-1\over2},
 \qquad u\equiv pR+s\pmod{p^2},\quad0\le R,s<p.
\]

Since `C(h)=p^2-1=2h`, equality `V_h=V_0` says that the last `h`
integers ending at `u` have total weight `2h`.  Such an interval must
contain no multiple of `p^2` and exactly `(p+1)/2` multiples of `p`.
Equivalently,

\[
 \boxed{R\ge a+1,\qquad s<a.}                          \tag{10}
\]

Under (10), the last `a` integers ending at `u` contain one multiple of
`p`, of exact valuation one.  Hence

\[
 V_{h_1}-V_0=a>0,                                       \tag{11}
\]

so (10) is also the exact condition for the global tie in (9).

## 4. Leading units and the leading-cancellation equation

Put

\[
 \Gamma(n)=\prod_{j=1}^n {j\over p^{v_p(j)}}\pmod p.
\]

If the normalized `b`-block is written

\[
 x^{-V_b}D_{u,b}F_{u-b,b}
 =L_b(1+\gamma_bx+\delta_bx^2+O(x^3)),                 \tag{12}
\]

then

\[
 L_b=(-1)^b2^{u-b}
 {\Gamma(2u+1)\Gamma(b)^2
  \over\Gamma(u)\Gamma(u-b)\Gamma(2b+1)}.             \tag{13}
\]

The elementary recurrence

\[
 \Gamma(pN+r)=(-1)^N\Gamma(N)r!\pmod p                 \tag{14}
\]

and Wilson's theorem give, under (10), with `t=R-a-1`,

\[
 {L_h\over L_0}
 =(-1)^{a+1}{(t+a+1)!s!\over t!(s+a+1)!}.              \tag{15}
\]

Thus the two leaders either do not cancel, in which case `M=m`, or
`L_h=-L_0`.  No classification of the solutions of (15) is needed for the
next step.

## 5. The first jet

For `p>=5`, normalize Pochhammer factors and the `F` block logarithmically.
The first logarithmic coefficients are

\[
 \alpha(n)=\sum_{\substack{1\le j\le n\\p\nmid j}}{j-1\over2},
\]

and

\[
 \beta(N,b)={16b^2+16b+8bN+5N+3N^2\over8}.            \tag{16}
\]

Therefore

\[
 \gamma_b=\alpha(2u+1)+2\alpha(b)-\alpha(u)
 -\alpha(u-b)-\alpha(2b+1)+\beta(u-b,b).               \tag{17}
\]

Formula (5) shows that only `b=0,1,h,h+1` can affect the first jet.
Under the tropical tie, direct use of (16)--(17) gives

\[
 \gamma_0-\gamma_h={12s+5\over32},                    \tag{18}
\]

and the effective leading contributions of the order-one blocks are

\[
 {L_1\over L_0}=-{s\over12},
 \qquad
 {L_{h+1}\over L_0}={2s+1\over32}.                    \tag{19}
\]

Here the first expression is interpreted as zero when `s=0`: in that
case the `b=1` block has order jump `p`, not one.  If the leaders cancel,
the coefficient of `x^(m+1)`, divided by `L_0`, is consequently

\[
 \boxed{{17s+9\over48}.}                               \tag{20}
\]

For `p=3`, (10) forces `(R,s)=(2,0)` and (15) gives `L_h/L_0=1`, so the
leaders do not cancel.  For `p=5` or `7`, the allowed values `0<=s<a`
make `17s+9` nonzero.  The same is automatic for `p=17`.

## 6. The second jet cannot also cancel

It remains to treat primes `p>=11`, `p!=17`, under

\[
 L_h=-L_0,\qquad17s+9=0\pmod p.                        \tag{21}
\]

In particular `s!=0`.  Only

\[
 b=0,1,2,h,h+1,h+2                                    \tag{22}
\]

can contribute through order `m+2`; (5) excludes every other block.  If
`s=1`, the `b=2` block has a jump of `p` and its displayed effective
coefficient below is zero automatically.

For auditability, here is the complete two-jet ledger.  The second
logarithmic coefficient of a normalized Pochhammer is

\[
 \eta(n)=\sum_{\substack{1\le j\le n\\p\nmid j}}
 {(j-1)(j-5)\over24}.                                  \tag{23}
\]

For the normalized `F` block, put

\[
 d=2b+1+{N\over2},\qquad e=2b(b+1),
\]

and

\[
 \theta(N,b)=
 {N(8N^2-9N-17+24d^2+24dN-48d)-96e\over192}.          \tag{24}
\]

Thus the second logarithmic block coefficient is the same factorial
combination of `eta` plus `theta`.  Formula (24) follows by viewing
`{N choose c}_q` at `q=e^z` as the inversion enumerator of a uniformly
chosen binary word.  Its conditional mean and variance are

\[
 {c(N-c)\over2},\qquad {c(N-c)(N+1)\over12},
\]

and averaging over `c~Bin(N,1/2)` gives (24), after
`z=log(1+x)`.

Let `lambda_b` denote the total second logarithmic block coefficient and
put

\[
 G=\gamma_0-\gamma_h,\qquad
 \Lambda=\lambda_0-\lambda_h.
\]

Straight substitution into (17), (23), and (24) gives

\[
\begin{aligned}
 G&={12s+5\over32},
 &\Lambda&={26s^2-57s-45\over384},\\
 \gamma_1-\gamma_0&={3(s+1)\over4},
 &\gamma_{h+1}-\gamma_h&={6s+1\over8},\\
 r_1&=-{s\over12},
 &r'_1&={2s+1\over32},\\
 r_2&={s(s-1)\over120},
 &r'_2&=-{3(4s^2-1)\over2048},
\end{aligned}                                          \tag{25}
\]

where `r_i` and `r'_i` are the effective leading contributions from the
blocks at distance `i` from `0` and `h`, divided by `L_0`.

Since an ordinary second coefficient is `lambda+gamma^2/2`, the normalized
coefficient `C_2` at `x^(m+2)` is

\[
\begin{aligned}
 {C_2\over L_0}={}&\Lambda-{G^2\over2}-r'_1G
 +r_1(\gamma_1-\gamma_0)
 +r'_1(\gamma_{h+1}-\gamma_h)+r_2+r'_2\\
 ={}&-{301s^2+2059s+990\over7680}.                     \tag{26}
\end{aligned}
\]

Using `17s+9=0` in the last line reduces it to

\[
 \boxed{{C_2\over L_0}={189\over320\cdot17^2}\ne0\pmod p.} \tag{27}
\]

The numerator has prime divisors only `3` and `7`; those primes were
already disposed of before (21).  The denominator is a unit for
`p>=11`, `p!=17`.  Hence simultaneous cancellation beyond two jets is
impossible.  This proves (1), and therefore (2).

## 7. Reproducibility

The standard-library checker

`check_q5_odd_taylor_two_jet.py`

independently audits:

1. the three-central-minimizer theorem and exact tie digit condition over a
   finite exhaustive box;
2. the leading-unit ratio (15);
3. the `F`-block formulas (16) and (24) directly from the Rogers--Szego
   recurrence;
4. every rational simplification in (18)--(27); and
5. exact normalized block jets for the known single- and double-cancellation
   witnesses, without constructing the degree-`2u(u+1)` polynomial.

The finite checks audit the algebra.  The arguments above prove the result
for all `u` and every odd prime.

