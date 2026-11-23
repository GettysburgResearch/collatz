# Full-fiber attack through the actual integer numerator

23 November 2026. **Status: exact algebraic deductions and a written
countermodel to a proposed closing implication; unrestricted positive
integer cycle exclusion remains OPEN.**

This is an attempt at the complete numerical gcd, not an exclusion of a
bounded word family. Its useful outcome is to isolate which of the known
integer-numerator facts actually adds information. Primitivity of the
integer quotient polynomial turns out to follow automatically from full
integer cancellation. Even positivity, monicity, the root annulus, the
two-adic root restriction, a polynomial-size leading coefficient, and the
exponential denominator/height separation admit full cancellation in an
explicit all-degree polynomial model. That model fails the positive-gap
condition at a specific repeated exponent. The exact Collatz coefficient
law therefore cannot be omitted in the next arithmetic step.

## 1. Actual normalization and frozen inputs

For one primitive positive odd integer cycle, use

\[
2^{a_i}x_{i+1}=3x_i+1,\qquad a_i\ge1,\qquad
A=\sum_{i<p}a_i,\quad s_j=\sum_{i<j}a_i,
\]

and put

\[
F=X^p-2^A,\quad Q=\sum_{j=0}^{p-1}2^{s_j}X^{p-1-j},\quad
G=\gcd_{\mathbb Q[X]}(F,Q),\quad F_0=F/G,\quad Q_0=Q/G.
\]

All gcds are monic. Write `d=deg F0`, `m=min xi`, `M=max xi`, and
`Dpol=|F0(3)|`. The cycle is rotated to `x0=m`. The supplied risk25
packet at PR175 local head
`bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17` supplies, at written-proof
scope and with its stated fixed-logarithm input,

\[
d\ge c p^\epsilon,\quad m\le C d^K,\quad
M\le e^\Lambda\big((3/2)^{d-1}(m+1)-1\big),
\]

\[
D_{\rm pol}\ge c_0\beta^d d^{-K_0},\quad
\beta=3/\sqrt{1+\sqrt2}>3/2,\quad
J=\frac{Q_0+mF_0}{X-3}\in\mathbb Z[X].
\]

The roots of `J` lie in `[3+1/M,3+1/m]` in modulus. The complete
ordinary cancellation is `Q0(3)=-mF0(3)`.

New peer sources inspected in this pass:

| Source | Frozen head | Exact path and consequence checked |
|---|---|---|
| PR182 | `afe6f4d1a661b377c9daa4623bdd732ba478386b` | `research/closure-round5-20261123/CYCLE_EXCLUSION.md`: large rational minima and first-crossing geometry do not force a proper rotated gap below the original complete denominator. |
| PR178 | `a9b23dcee61a4b65a63aa4e7ca653d875a405037` | `research/reassessment-20261123/cycles/PRIME_POTENTIAL_AND_FULL_CLOSURE.md`: prime-potential and companion-product attempts retain their stated failure to control original cancellation. |
| PR177 | `2fbc5706d2caff5d1485247e5291374ff4885041` | `research/lean-exact-witness-global-20261121/universal-step-20261123/commutator/UNEQUAL_BLOCK_COMMUTATOR.md`: the common-residue argument requires the strict cross-carry bound for a contracting dictionary. |
| PR176 | `81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a` | `research/lean-global-resolvent-20261121/overview/global-closing/PAIRED_TENSOR_CLOSURE_ATTEMPT.md`: every fixed polynomial product-closure equation lies in the ideal of the two scalar closures; the third apparent denominator supplies no independent equation. |
| PR180 | `7cfd911d35382d9d3bc988060ba88ade78a4267e` | `research/closing-step-20261123/POSITIVE_CYCLE.md`: all-lap ordinary return lattices pay a full ternary separation; the simultaneous defect budget does not by itself exclude one cycle. |

These are source comparisons, not blanket reviews of the branches.

## 2. The exact Smith module has only the original evaluation condition

Let `f` be any monic integer polynomial of degree `d>=1`, with
`f(3)!=0`, and let

\[
\mathcal A=\mathbb Z[X]/(f).
\]

As a free abelian group, `A` has basis `1,X,...,X^(d-1)`. Multiplication
by `X-3` has cokernel

\[
\boxed{\quad
\mathcal A/(X-3)\mathcal A
\cong\mathbb Z[X]/(f,X-3)
\cong\mathbb Z/(f(3)).\quad}                         \tag{SN1}
\]

The last isomorphism is evaluation at three. For completeness, every
integer polynomial satisfies `h(X)-h(3)=(X-3)k(X)` with `k` integral.
Thus the image of the ideal `(f,X-3)` under evaluation is exactly
`f(3) Z`, establishing both directions of the kernel assertion.

Consequently the integer matrix of this multiplication has Smith form

\[
\boxed{\operatorname{diag}(1,\ldots,1,|f(3)|).}       \tag{SN2}
\]

Its determinant has absolute value `|f(3)|`; the cokernel is cyclic,
so all but its last invariant factor are one. In particular

\[
q\in(X-3)\mathcal A
\quad\Longleftrightarrow\quad f(3)\mid q(3).          \tag{SN3}
\]

Applying this with `f=F0,q=Q0` preserves **every prime power of the
original residual numerical denominator**. It neither replaces that
denominator by a complementary cycle denominator nor multiplies
valuations at distinct conjugates. It also shows why Smith reduction
alone does not create an additional obstruction: it is exactly the
full evaluation condition in another basis.

The still more general quotient

\[
\mathbb Z[X]/(F_0,Q_0,X-3)
\cong\mathbb Z/\gcd(F_0(3),Q_0(3))                   \tag{SN4}
\]

identifies the numerical gcd itself, without a factorwise substitution.

## 3. Primitivity of J is automatic after integral cancellation

**Proposition IN1.** Let `f,q` be monic integer polynomials of degrees
`d` and `d-1`, respectively. Suppose `m` is an integer and

\[
J=(q+mf)/(X-3)\in\mathbb Z[X].
\]

If `d>=2`, then `J` is primitive. In fact, write

\[
f=X^d+f_1X^{d-1}+\cdots,\qquad
J=mX^{d-1}+j_1X^{d-2}+\cdots.
\]

The coefficient of `X^(d-1)` in `(X-3)J=q+mf` is

\[
j_1-3m=1+mf_1,
\qquad\boxed{j_1-m(f_1+3)=1.}                       \tag{IN1}
\]

Any common divisor of the coefficients of `J` divides the two displayed
leading coefficients and hence divides one. This is an explicit Bezout
certificate; positivity or any root estimate is unnecessary.

For `d=1`, comparison of the constant term gives
`-3m=1+mf1`, so `m` itself divides one. Thus the same primitive
conclusion holds in the degree-zero case.

For actual cycles, `F0,Q0` are both monic because `F,Q,G` are monic.
Therefore IN1 shows that the primitive-J statement is not a second
integer-specific hypothesis after one has assumed full integer
cancellation. This does not invalidate the risk25 proof of primitivity;
it identifies the precise logical strength of the conclusion.

## 4. Resultant divisibility is the same condition with an extra factor

The polynomial identity gives, at every root `lambda` of `F0`,

\[
Q_0(\lambda)=(\lambda-3)J(\lambda).
\]

Since `F0` is monic, multiplication over its `d` roots yields

\[
\boxed{\operatorname{Res}(F_0,Q_0)
=(-1)^dF_0(3)\operatorname{Res}(F_0,J).}              \tag{RE1}
\]

The second resultant is an integer. Thus a large factor `F0(3)` in the
first resultant is required by full integer cancellation. Primitivity
of `J` does not make `Res(F0,J)` a unit. Replacing the numerical gcd
by a divisor of this resultant cannot exclude cancellation unless an
additional, genuinely strict estimate on that same resultant factor is
proved. No such estimate is supplied by the root annulus alone; the
next section gives an explicit obstruction.

## 5. Positive integral polynomial models with full cancellation

The following construction is deliberately **not a Collatz cycle**.
It tests the strongest attempted implication based only on the known
polynomial geometry and elementary integrality properties. In contrast
with a rational-cycle control, its distinguished quotient is an integer
and its full numerical gcd equals the entire denominator.

### 5.1 Parameters and the exact auxiliary recurrence

Choose coprime positive integers `A,d`, with `d>=16`, such that

\[
\eta=\frac{2^A-3^d}{3^d}\in(0,1/192].
\tag{PC1}
\]

There are infinitely many such pairs, for example a sufficiently late
sequence of upper continued-fraction convergents of `log_2 3`.
Put `D=2^A-3^d`, and choose the least integer

\[
m\equiv7\pmod {192},\qquad m\ge4/\eta.
\]

Then

\[
\boxed{4\le m\eta<4+192\eta\le5.}                  \tag{PC2}
\]

Define positive integers

\[
y_0=m,\qquad y_j=\lfloor3y_{j-1}/2\rfloor+1,
\qquad v_j=2^j y_j\quad(0\le j\le d-1),
\]

and the polynomial

\[
J=\sum_{j=0}^{d-1}v_jX^{d-1-j}.
\tag{PC3}
\]

Set `c_j=v_j-3v_(j-1)` for `1<=j<=d-1`. Directly from the two
parities of `y_(j-1)`,

\[
c_j=\begin{cases}
2^{j-1},&y_{j-1}\text{ odd},\\
2^j,&y_{j-1}\text{ even}.
\end{cases}                                         \tag{PC4}
\]

Thus every `c_j` is a positive power of two. Since `m=7 mod192`,
`v1=3m+1`, and `J` is primitive. Also `3` divides no `v_j`: this
holds for `v0=m`, and follows for each later coefficient from
`v_j=3v_(j-1)+c_j`.

### 5.2 Monicity, positivity, irreducibility and the full integer gcd

Define

\[
F_0=X^d-2^A,\qquad Q_0=(X-3)J-mF_0.
\tag{PC5}
\]

The leading terms of degree `d` cancel. The leading coefficient of
`Q0` is `v1-3m=1`. Its remaining nonconstant coefficients are the
positive powers of two `c2,...,c_(d-1)`. Its constant term is

\[
q_{\rm last}=m2^A-3v_{d-1}.
\]

The recurrence gives

\[
y_j\le(3/2)^j(m+2)-2,
\quad v_j\le3^j(m+2)-2^{j+1}.
\tag{PC6}
\]

Consequently

\[
q_{\rm last}\ge mD-2\,3^d+3\,2^d
\ge2\,3^d+3\,2^d>0.                                \tag{PC7}
\]

Both `J` and `Q0` therefore have strictly positive integer coefficients.
Every nonconstant coefficient of `Q0` is a power of two.

All roots of `F0` have modulus `2^(A/d)`. A monic integer factor of
degree `k>0` has constant-term modulus `2^(Ak/d)`. Integrality and
`gcd(A,d)=1` force `d|k`; hence `F0` is irreducible over the rationals.
Since `Q0` has smaller degree, its full polynomial gcd with `F0` is one.

Evaluation at three nevertheless gives

\[
\boxed{Q_0(3)=mD,\qquad
\gcd(F_0(3),Q_0(3))=D.}                            \tag{PC8}
\]

This is complete cancellation in the same distinguished fiber.

### 5.3 The same archimedean annulus and height scale

Put

\[
M=(3/2)^{d-1}(m+1)-1.
\tag{PC9}
\]

For every adjacent coefficient pair of `J`,

\[
\frac{v_j}{v_{j-1}}
=3+\frac{c_j}{v_{j-1}}
=3+\frac{1\text{ or }2}{y_{j-1}}.
\]

At `j=1`, the correction equals `1/m`. At `j=2`, `y1` is odd
because `m=3 mod4`, and the correction is `1/y1<=1/m`. For `j>=3`,
`y_(j-1)>=(3/2)^(j-1)m>=9m/4`, so the correction is at most
`2/y_(j-1)<1/m`. On the other side, PC6 gives

\[
y_{j-1}\le(3/2)^{d-2}(m+2)-2<M
\]

for `m>=1`. Thus every correction is at least `1/M`. The elementary
positive-coefficient root lemma used in risk25 now proves

\[
\boxed{3+1/M\le |z|\le3+1/m
\quad\text{for every root }z\text{ of }J.}          \tag{PC10}
\]

Even the roots of `F0` lie in this annulus. Concavity gives

\[
m\big(2^{A/d}-3\big)
=3m\big((1+\eta)^{1/d}-1\big)
\le3m\eta/d\le15/d<1.
\]

For the lower bound, the mean-value theorem gives
`(1+eta)^(1/d)-1>=eta/[d(1+eta)]`. As
`M>=m(3/2)^(d-1)`, PC2 implies

\[
M\big(2^{A/d}-3\big)
\ge\frac{12}{d(1+\eta)}(3/2)^{d-1}>1
\quad(d\ge16).
\tag{PC11}
\]

### 5.4 Local root integrality also survives

The polynomial

\[
2^{-(d-1)}J(2Y)=\sum_{j=0}^{d-1}y_jY^{d-1-j}
\]

has integer coefficients and odd leading coefficient `m`. Dividing by
that leading coefficient makes it monic over `Z_2`, so every root of
`J` has two-adic valuation at least one. Since the leading and constant
coefficients of `J` are both units at three and all coefficients are
three-adically integral, all its roots are three-adic units as well.
These statements hold in an algebraic closure with the usual normalized
valuations. They do not merely inspect one selected conjugate.

### 5.5 The denominator/height separation still grows exponentially

PC2 and `eta<=1` imply `m+1<=6/eta`. Therefore

\[
\boxed{\frac D M\ge\frac{\eta^2 2^d}{4}.}           \tag{PC12}
\]

The same fixed two-logarithm input already used in risk25 gives
`eta>=c d^(-K0)` at these reduced coprime clocks. It follows that

\[
m\le5c^{-1}d^{K_0},\qquad
\frac D M\ge\frac{c^2 2^d}{4d^{2K_0}}\longrightarrow\infty.
\tag{PC13}
\]

The examples can also have defect `Lambda=log(1+eta)` tending to zero.
Because `m eta` stays in `[4,5]`, the scale
`Lambda=O(1/m)` is compatible with the weaker upper bound
`O(m^(theta-1)/sqrt(log m))` in the ordinary counting argument for
any fixed `theta` in `(0,1)`. This is only a comparison of numerical
scales, not an assertion that the auxiliary states form an ordinary
forward-invariant set.

### 5.6 Exact failure of the positive-gap law

Write `m=7+192k`. The first auxiliary values are

\[
\begin{aligned}
y_0&=7+192k,& y_1&=11+288k,& y_2&=17+432k,\\
y_3&=26+648k,& y_4&=40+972k,& y_5&=61+1458k.
\end{aligned}
\]

Thus the first six nonconstant carry coefficients have exponents

\[
\boxed{0,1,2,4,5,5.}                                \tag{PC14}
\]

Actual positive odd gaps require every partial-sum exponent to increase
strictly. The repeated exponent `5,5` is a zero gap. Hence these are
not positive-gap Collatz words. In addition, no claim is made that the
last coefficient in PC7 is a power of two. These exact failures are
preserved, rather than disguising the model as an ordinary cycle.

**Consequence.** Any argument that derives the missing numerical gcd
bound using only the properties proved in PC5--PC13 is false. It must
use additional information from the original positive-gap power-of-two
carry law, including its terminal coefficient and full closure. The
countermodel does not refute an argument that actually uses that law.

## 6. Primary S-unit theorem audit and attempted application

The original sources were opened, not inferred from abstracts alone.

1. Corvaja--Zannier, *A lower bound for the height of a rational function
   at S-unit points*, arXiv:math/0311030v2, Theorem 1 and Corollary 1,
   printed pp.1--2, <https://arxiv.org/pdf/math/0311030>. Theorem 1 fixes
   the finitely generated group and two coprime polynomials; excessive
   gcd/height loss is confined to finitely many translated subtori and
   a finite set. This is not a bound uniform over all degrees and
   coefficient arrays.

2. Grieve--Wang, *Greatest common divisors with moving targets and
   consequences for linear recurrence sequences*, arXiv:1902.09109v2,
   Theorem 1.2, printed p.2, <https://arxiv.org/pdf/1902.09109>;
   published in Transactions of the AMS 373 (2020), 8095--8126,
   DOI <https://doi.org/10.1090/tran/8220>. This moving-target theorem
   still fixes the number field, finite set of places, number of
   variables, and positive degrees. Coefficient heights must be
   little-oh of the largest argument height. Its conclusion includes
   a possible small-height translated subgroup alternative, and its
   small-gcd conclusion is on an infinite subset.

Here are the actual substitutions attempted, retaining the original carry.

| Encoding | Data that stay fixed | First failed hypothesis |
|---|---|---|
| `F(3),Q(3)` as values at `(2,3)` | Number field and `S={2,3,infinity}` | The evaluation point has bounded height while the polynomials and their degrees vary with the word. |
| The individual terms `2^(s_j)3^(p-1-j)` as torus coordinates | Each coordinate is an S-unit | The number of coordinates grows with `p`; after residual compression, it still grows with `d`. |
| A fixed number of long blocks | Number of block variables | The internal block carries have heights on the same scale as the block powers. The required little-oh coefficient hypothesis has not been proved. |
| Split into short blocks so each carry is small | Coefficient cost per short block | The number of variables grows with the word. |
| Replace the carry by `m(2^A-3^p)` under integral closure | A two-variable expression with small `m` | The two torus polynomials now have the common factor `X-Y`; the coprimality hypothesis has been lost. |

The degree lower bound `d>=c p^epsilon` strengthens the desired
denominator estimate, but does not make a variable-degree application
of either theorem legitimate. The bound `log m=O(log d)` controls one
leading coefficient, not the heights of the entire variable carry
polynomial or the dimension of the torus encoding. No application of
either theorem to the unrestricted cycle family has been obtained.

## 7. Positive-gap route still under attack

The exact positive-gap data have not been discarded as irrelevant.
They force all actual cyclic edges and local oddness, but the prime
obstruction to integer closure lies at the odd primes dividing the
complete `D=2^A-3^p`, rather than at two or three. Every legal positive
rational word already has odd denominator coprime to three and has its
exact prescribed two-adic gaps. A local argument restricted to those two
primes therefore needs an additional global height input to separate
ordinary closure from rational closure.

The companion `POSITIVE_GAP_FULL_FIBER.md` records the direct attempt
to extract that missing condition from the exact coefficient law.

## 8. Evidence and boundary

`check_positive_numerator_models.py` is a new exact check of PC1--PC14;
it does not rerun the risk25 rational controls or enumerate Collatz
cycles. It verifies complete integer cancellation, positive polynomial
coefficients, content one, each adjacent coefficient-ratio inequality,
the local coefficient conditions, and the repeated exponent. The root
annulus is certified through the exact coefficient inequalities rather
than floating-point root plots.

Executed command: `python -X utf8 -B check_positive_numerator_models.py`.
It exited zero. The three controls `(A,d)=(401,253),(485,306),(886,559)`
gave `m=1351,4039,967`, respectively, and exact lower bounds
`D/M>=2^234,2^284,2^541`. All 1,115 adjacent coefficient-ratio
certificates passed; every full numerical gcd was the complete `D`.
The deliberate repeated exponent was detected in all three. No
floating-point root test or Collatz-cycle search was performed.

No Lean theorem for the infinite construction, the root lemma, or the
S-unit literature is asserted. A tiny formal restatement of SN3 or IN1
would not supply the missing arithmetic; none is presented as progress
toward closure. The unproved step remains a strict full-fiber arithmetic
inequality that uses the actual increasing power-of-two exponents and
the terminal carry law. No unrestricted cycle exclusion is claimed.
