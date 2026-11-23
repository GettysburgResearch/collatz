# Integer cycles force a power-sized residual polynomial degree

Date: 2026-11-23. **Status: new written deductions for unrestricted
primitive positive integer cycles, with an explicitly source-qualified
two-logarithm input. No unrestricted cycle exclusion.**

The all-word theorem in the preceding risk24 packet gave residual degree
`d >> (log p)^2/log log p`. The argument here uses the actual integer
cycle to obtain a substantially different scale:

\[
\boxed{d\ge c p^{\varepsilon}}
\tag{IR1}
\]

for absolute effective positive constants `c,epsilon`. Consequently the
source-qualified factor-gap theorem forces a hypothetical integer cycle
to absorb a residual polynomial denominator at least
`exp(c' p^epsilon)`. This is a necessary condition on a cycle, not a proof
that this absorption cannot happen.

The new mechanism is a root-location inequality for the *actual orbit
numerator*, followed by a logarithm estimate at the **reduced** clock
`A/p=a/b`. An elementary distinct-state argument already gives a positive
power degree bound up to a logarithm. The sharper count from PR182 improves
the exponent and removes that logarithmic loss. Neither argument makes
the polynomial denominator equal to the reduced rational denominator.

## 1. Complete normalization and dependencies

Use the odd map

\[
 U(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
\]

Let `x_0,...,x_(p-1)` be one primitive positive integer odd cycle. Thus
the states are distinct positive odd integers and, cyclically,

\[
 2^{a_i}x_{i+1}=3x_i+1,\quad a_i\ge1,
 \qquad A=\sum_{i<p}a_i,\quad s_j=\sum_{i<j}a_i.
\]

Write

\[
 m=\min_i x_i,\quad M=\max_i x_i,\quad
 \Lambda=A\log2-p\log3>0,\quad \tau=\Lambda/p,
 \qquad r=2^{A/p}=3e^\tau.
\]

The complete polynomials and monic gcd are

\[
 F=X^p-2^A,\quad Q=\sum_{j=0}^{p-1}2^{s_j}X^{p-1-j},
 \quad G=\gcd_{\mathbb Q[X]}(F,Q),
 \quad F_0=F/G,\quad Q_0=Q/G,\quad d=\deg F_0.
\tag{IR2}
\]

All are integer polynomials; `F_0` is monic, and `deg Q_0=d-1`.
The same `G` and `d` occur after every odd rotation. Indeed

\[
 2^{a_0}Q_{\mathrm{next}}=XQ-F,
\]

and `X` is coprime to `F`. The minus sign follows directly by comparing
the constant terms: the constant term of `XQ-F` is `2^A`.

The inherited sources used below are narrowly identified:

| Source | Exact role |
|---|---|
| PR185 `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`, `research/central-closure-20261123/PRIMITIVE_RESIDUAL_DEGREE.md`, Section 1 | Monic integer factors, common root radius, and `b divides d` for `A=ga,p=gb` |
| Same PR185 head, `research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md` | Written factor-gap consequence `|F_0(3)|>(3/2)^(d-1)` outside the trivial primitive word; its logarithmic-form/certificate qualification is retained |
| PR182 `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, Sections 1--5 | Elementary written count for every injective forward-invariant ordinary odd set, used only for the sharper version of IR1 |
| E. M. Matveev, primary Corollary 2.3, printed p. 1219 | Fixed two-logarithm lower bound, explicitly specialized in Section 4 |

The root-location argument is proved below. It needs no unproved
variable-degree gcd theorem and does not sum valuations at unrelated
conjugates.

## 2. Root location for the actual integer numerator

Put `v_j=2^(s_j)x_j` for `0<=j<=p`. The actual edge equations give

\[
 v_0=x_0,\qquad v_{j+1}=3v_j+2^{s_j},\qquad
 v_p=2^A x_0.
\]

Define

\[
 H(X)=\sum_{j=0}^{p-1}v_j X^{p-1-j}.
\]

Direct coefficient comparison gives

\[
 (X-3)H=Q+x_0F.
\tag{IR3}
\]

Since `G(3)` is nonzero, `G` divides `H`; write

\[
 J=H/G=\frac{Q_0+x_0F_0}{X-3}\in\mathbb Z[X].
\tag{IR4}
\]

Here `deg J=d-1` and its leading coefficient is `x_0`. For `p>=2`,
`H` is primitive: its leading two coefficients are `x_0` and `3x_0+1`,
which are coprime. Gauss's lemma then makes `J` primitive as well. This
retains an integral polynomial of degree `d-1` and small leading
coefficient when the starting state is the minimum. Primitivity alone
will not provide the missing degree upper bound.

### Elementary positive-coefficient root lemma

If `P(X)=c_0 X^N+c_1 X^(N-1)+...+c_N`, with `N>=1` and every `c_j>0`, then
every root `z` obeys

\[
 \min_{0\le j<N}\frac{c_{j+1}}{c_j}
 \le |z|\le
 \max_{0\le j<N}\frac{c_{j+1}}{c_j}.
\tag{IR5}
\]

For the lower bound, scale the variable by the minimum ratio. The
resulting polynomial has its coefficients nonincreasing when read from
the constant term upward. For `f(z)=a_0+a_1z+...+a_N z^N`, with
`a_0>=...>=a_N>0`,

\[
 (1-z)f(z)=a_0-
 \sum_{j=1}^N(a_{j-1}-a_j)z^j-a_Nz^{N+1}.
\]

When `|z|<1`, the absolute value of the terms subtracted is strictly
smaller than `a_0`, so there is no zero. Apply the same argument to
the reciprocal polynomial for the upper bound. This is the standard
Enestrom--Kakeya root bound, included with its proof so that no
additional analytic theorem is a dependency.

For the actual coefficients,

\[
 \frac{v_{j+1}}{v_j}=3+\frac1{x_j}.
\]

Every root of `H`, and hence every root of `J`, therefore lies in

\[
 \boxed{3+1/M\le |z|\le3+1/m.}
\tag{IR6}
\]

The last edge need not occur among these adjacent coefficient ratios;
using the full-cycle extrema in (IR6) remains valid.

### Removing every structural factor gives a concentration inequality

All `p-d` roots of `G` have modulus `r`, so `|G(0)|=r^(p-d)`.
The last edge gives

\[
 \frac{|J(0)|}{x_0}
 =\frac{2^{A-a_{p-1}}x_{p-1}}{x_0r^{p-d}}
 =\frac{r^d}{3+1/x_{p-1}}.
\tag{IR7}
\]

Let `e(x)=log(1+1/(3x))`. Comparing the product of the `d-1` root
moduli in (IR6) with (IR7) gives

\[
 \boxed{
 e(x_{p-1})+(d-1)e(M)
 \le d\tau
 \le e(x_{p-1})+(d-1)e(m).
 }
\tag{IR8}
\]

Rotation leaves `d` unchanged, so this holds with every cycle state in
the predecessor position. In particular

\[
 \boxed{e(m)\le d\Lambda/p.}
\tag{IR9}
\]

The inequality is strict if `d>1`, since `e(M)>0`. If `d=1`, the
empty root product gives equality for every predecessor, forcing all
states equal; a primitive integer cycle is then the known one-state
odd cycle at 1.

Equation (IR9) already holds for positive rational cycles. Its
integer-specific force comes next: the ordinary states form a set of
distinct integers. No rational-cycle spacing is silently substituted.

## 3. First integer consequence without a global counting theorem

Distinct positive integer states satisfy

\[
 \Lambda=\sum_{i<p}e(x_i)
 \le\frac13\sum_{i<p}\frac1{x_i}
 \le\frac13 H_p\le\frac{1+\log p}{3}.
\tag{IR10}
\]

Also `e(m)>=1/(3m+1)>=1/(4m)`, because `m>=1` and
`log(1+t)>=t/(1+t)` for `t>=0`. Thus (IR9) implies

\[
 \boxed{p\le\frac43 d m(1+\log p).}
\tag{IR11}
\]

This deduction concerns every primitive positive integer cycle, with no
gap-alphabet, number-of-runs, or word-schema restriction.

## 4. Apply the two-logarithm theorem at the reduced clock

Put

\[
 g=\gcd(A,p),\qquad A=ga,\quad p=gb,\quad\gcd(a,b)=1.
\]

The cycle product gives

\[
 2^A=\prod_{i<p}(3+1/x_i)\le4^p,
 \qquad a\le2b.
\tag{IR12}
\]

Every root of the monic integer polynomial `F_0` has modulus
`2^(a/b)`, hence `|F_0(0)|=2^(ad/b)` is an integer. Unique
factorization and `gcd(a,b)=1` give

\[
 \boxed{b\mid d,\qquad b\le d.}
\tag{IR13}
\]

The fixed logarithmic form to estimate is

\[
 L=a\log2-b\log3>0,\qquad \tau=L/b.
\tag{IR14}
\]

For clarity, an explicit safe specialization can be read directly from
Matveev's Corollary 2.3. Take the number field `Q`, its degree `D=1`,
two arguments `2,3`, coefficient maximum `B*=max(a,b)=a<=2b`,
and height parameters `log 2,log 3`. The corollary allows
`C_1(2)<=2^32`. Therefore, with

\[
 K_0=2^{32}(\log2)(\log3),\qquad
 c_0=(2e)^{-K_0},\qquad K=K_0+1,
\]

one obtains

\[
 \boxed{L>c_0 b^{-K_0}.}
\tag{IR15}
\]

This deliberately crude constant is sufficient. The theorem is used in
fixed dimension two; `p` or `d` does not enter its dimension, degree, or
argument heights. The primary PDF statement and its constants were
opened and visually checked in this pass. Its proof was not reconstructed
or formalized here.

On the other hand `tau=Lambda/p<=1/(3m)`. Dividing (IR15) by `b`
therefore gives

\[
 \boxed{m<C_m b^K\le C_m d^K,\qquad C_m=(3c_0)^{-1}.}
\tag{IR16}
\]

Using the unreduced pair `(A,p)` would lose this connection with the
residual degree. This reduced-clock use is the decisive bootstrap step.

Combining (IR11) and (IR16) yields the first completely written form
that does not depend on the newer global count:

\[
 \boxed{
 d\ge
 \left(\frac{3p}{4C_m(1+\log p)}\right)^{1/(K+1)}.
 }
\tag{IR17}
\]

Thus even the elementary distinct-state bound forces a positive-power
residual degree, up to the displayed logarithm. It already strengthens
the preceding all-word `log^2 p/log log p` bound for hypothetical
integer cycles. The constants and exponent are extremely weak; no
useful finite numerical exclusion is claimed.

## 5. Sharpening from the actual ordinary-state count

The PR182 theorem pinned in Section 1 states that every forward-invariant
positive odd set `S` on which `U` is injective satisfies

\[
 F_S(X)\le C\frac{X^\theta}{\sqrt{1+\log X}},\qquad
 \theta=H_2(\log_3 2)<1,
\tag{IR18}
\]

with an absolute effective constant. A primitive cycle's finite state
set satisfies these hypotheses: `U` is a permutation. The argument
counts distinct states, not repeated traversals of the cycle.

Since the state set has floor `m`, Tonelli gives

\[
 \sum_i\frac1{x_i}
 =\int_m^\infty F_S(t)t^{-2}\,dt
 \le\frac{C}{1-\theta}
 \frac{m^{\theta-1}}{\sqrt{1+\log m}}.
\]

Consequently, putting `C_Lambda=C/[3(1-theta)]`,

\[
 \Lambda\le C_\Lambda
 \frac{m^{\theta-1}}{\sqrt{1+\log m}}.
\tag{IR19}
\]

Equations (IR9) and (IR19) yield the new minimum-degree-period tradeoff

\[
 \boxed{
 p\le4C_\Lambda\,
 \frac{d m^\theta}{\sqrt{1+\log m}}.
 }
\tag{IR20}
\]

Substitute (IR16) and discard only the denominator, which is at least
one. With

\[
 C_* =4C_\Lambda C_m^\theta,\qquad
 \varepsilon=\frac1{1+K\theta}>0,
\]

we obtain

\[
 \boxed{p\le C_*d^{1+K\theta},\qquad
 d\ge C_*^{-\varepsilon}p^\varepsilon.}
\tag{IR21}
\]

This is (IR1). The exact symbolic exponent is the asserted constant;
floating-point approximations are not part of the proof. More efficient
fixed-base logarithm estimates could improve it substantially. No
stronger uninspected Rhin estimate is used in the theorem above.

## 6. What this forces at the complete distinguished fiber

The PR185 factor-gap theorem gives

\[
 D_{\rm pol}:=|F_0(3)|>(3/2)^{d-1}
\tag{IR22}
\]

outside the trivial primitive word. Together with (IR21), this gives

\[
 \boxed{
 \log D_{\rm pol}>
 \log(3/2)\big(C_*^{-\varepsilon}p^\varepsilon-1\big).
 }
\tag{IR23}
\]

In particular `D_pol>=exp(c' p^epsilon)` for all sufficiently large
primitive integer cycles, with adjusted absolute effective `c'>0`.
Even the stand-alone (IR17) gives the corresponding
`exp(c[p/(1+log p)]^(1/(K+1)))` necessity.

The minimum, by contrast, obeys `log m<=log C_m+K log d`. It is only
polynomial in `d`, while `D_pol` is exponential in `d`. The complete
ordinary divisibility condition nevertheless remains

\[
 \boxed{D_{\rm pol}\mid Q_0(3),\qquad
 Q_0(3)=-mF_0(3)
 \text{ after rotation to the minimum}.}
\tag{IR24}
\]

A small integer quotient can absorb a large denominator. None of
(IR8), (IR16), or (IR21) proves that this absorption fails. They sharpen
what a hypothetical integral solution must satisfy and do not replace
the final gcd by a resultant or by a product over other conjugates.

The first unsupported closing step remains a new arithmetic consequence
of the actual integer polynomial `J`, strong enough to force
`log m` to grow faster than `log d` (for example `log m>=c d`), or a
strict bound on `gcd(F_0(3),Q_0(3))`. The companion lattice note proves
an exact degree-dependent normalization bound, but that cost is still
linear in `d`, not sublinear.

Even an effective inequality such as `log m>=c d` would first bound
`d`, and hence `p` by (IR21). Excluding every remaining finite candidate
would still be needed for a complete positive-cycle theorem. No such
finite exhaustion is supplied here.

## 7. Verification and primary-source scope

The companion `check_integer_residual_degree.py` checks exact polynomial
identities, cyclic gcd invariance, the constant-term product identity,
the integral trivial-cycle controls, and rational controls with both
nontrivial polynomial cancellation and no cancellation. It checks the
root-location consequences by exact powered rational inequalities, not
floating root calculations. These finite controls do not validate the
unbounded theorem by enumeration.

Matveev's primary source is *An explicit lower bound for a homogeneous
rational linear form in the logarithms of algebraic numbers. II*,
Izvestiya: Mathematics 64:6 (2000), 1217--1269, Corollary 2.3:
<https://www.mathnet.ru/eng/im314>;
stable full-text endpoint
<https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng>.

For possible future improvement, the primary Simons--de Weger paper,
*Theoretical and computational bounds for m-cycles of the 3n+1-problem*,
Acta Arithmetica 117 (2005), Lemma 12, was also inspected:
<https://www.impan.pl/shop/en/publication/transaction/download/product/82263>.
Its proof uses Rhin's proposition on printed p.160 of the 1987 source.
The original Rhin proposition was not inspected in this pass, so its
smaller exponent is not inserted into (IR15) or (IR21).

No Lean theorem for the analytic root lemma, global count, or Matveev
input is claimed. No finite cycle search, historical certificate replay,
or unrestricted positive-cycle exclusion is claimed.
