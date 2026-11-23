# A uniform polynomial lower bound for the residual denominator

Date: 2026-11-23. Written theorem with an exact finite arithmetic
certificate. This is not an end-to-end Lean proof.

## Main theorem and its exact meaning

For a binary parity word with positive length `A` and `p>=1` odd
positions `0<=d_0<...<d_(p-1)<A`, put

\[
F(X)=X^p-2^A,\qquad
Q(X)=\sum_{i=0}^{p-1}2^{d_i}X^{p-1-i},
\]

and let `G` be their monic rational polynomial gcd. Write

\[
F_0=F/G,\qquad Q_0=Q/G,\qquad
n=\deg F_0,\qquad D_{\rm pol}=|F_0(3)|.
\]

**Theorem.** Suppose `2^A>3^p`, and the parity word is primitive and
is neither of the two length-two words `10,01`. Then

\[
\boxed{
D_{\rm pol}>
\left(\frac32\right)^{n-1}
\ge p^{\log_3(3/2)}.
}
\tag{1}
\]

For `A!=2p`, the stronger first inequality

\[
D_{\rm pol}>\left(\frac32\right)^n
\tag{2}
\]

holds. The exponent `log_3(3/2)` is a fixed positive constant. Thus
the polynomial denominator left after *every* common polynomial
factor is removed grows at least as a positive power of the odd clock
along primitive positive words.

The degree theorem in `PRIMITIVE_RESIDUAL_DEGREE.md` supplies
`p<=3^(n-1)`. This note proves the value bound that converts that
degree restriction into (1). The exceptional integer slope `A=2p`
is included explicitly, rather than omitted as a limiting case.

This is not a lower bound for the actual reduced rational denominator

\[
\frac{D_{\rm pol}}{\gcd(D_{\rm pol},Q_0(3))}.
\]

The same integer evaluation gcd can still absorb all of `D_pol`.
Proving that it does not is the remaining cycle-closing problem.
In particular, (1) does not assert a complete Collatz proof.

## 1. Coefficient support of every monic binomial factor

Write `g=gcd(A,p)`, `A=ga`, `p=gb`, `gcd(a,b)=1`, and

\[
r=2^{a/b}>3,\qquad e=\gcd(b,2),\qquad t=b/e.
\]

Let `P` be any nonconstant monic integer divisor of `F`, of degree
`d`. Its roots all have modulus `r`. The absolute value of its
constant coefficient is `r^d=2^(ad/b)`, a positive integer. Prime
factorization gives `b|d`.

Writing `P(X)=sum c_i X^i`, closure of its roots under conjugation
and `r^2/alpha=conjugate(alpha)` give the polynomial identity

\[
X^dP(r^2/X)=c_0P(X).
\]

If `c_i!=0`, comparison of coefficients gives

\[
\frac{c_i}{c_{d-i}}
=\frac{r^{2(d-i)}}{c_0}
=\pm2^{a(d-2i)/b}\in\mathbb Q.
\]

A rational power of two with rational exponent has integral exponent
when it is rational. Together with `gcd(a,b)=1` and `b|d`, this gives
`b|2i`, equivalently `t|i`. Consequently

\[
P(X)=H(X^t)
\]

for a monic integer polynomial `H` of degree `d/t`, whose roots have
modulus `2^(a/e)`. The reverse triangle inequality yields

\[
|P(3)|\ge
\left(2^{a/e}-3^{b/e}\right)^{ed/b}.
\tag{3}
\]

This concerns arbitrary factors, including reducible ones and partially
split homogeneous cyclotomic factors. It does not assume that
`Phi_h(X^b,2^a)` is irreducible.

## 2. A uniform gap for the reduced pair

**Gap lemma.** For coprime positive `a,b` with `2^a>3^b`, put
`e=gcd(b,2)`. Except for `(a,b)=(2,1)`,

\[
\boxed{2^{a/e}-3^{b/e}>\left(\frac32\right)^{b/e}.}
\tag{4}
\]

The complete finite arithmetic component is reproduced by
`check_factor_growth_gap.py`. Its calculations use integers and exact
rational fractions, with explicit failure checks that also run under
Python's `-O` flag. The code does not replace the analytic coverage
argument below.

### 2.1 The effective infinite tail

Suppose that (4) fails and `b>=14`. Set `q=b/e>=7`. Then

\[
2^{a/e}\le3^q+(3/2)^q<4^q.
\]

The last inequality holds for all integer `q>=2`: it holds at 2,
and each summand grows by a factor at most 3 while the right side
grows by 4. Thus `a<2b`.

Let

\[
\varepsilon=2^a3^{-b}-1>0,
\qquad C=10^{10},\quad K=10^{12}.
\]

The real-field Matveev bound, in Bugeaud--Mignotte--Siksek,
Theorem 9.4, gives

\[
\log\varepsilon>-C(1+\log(2b)).
\tag{5}
\]

The specialization uses the field `Q`, the numbers `2,3`, exponents
`a,-b`, and height bounds `1,2`. Unique factorization supplies
nonvanishing. The maximum exponent is at most `2b`. Its numerical
prefactor is less than
`(7/5)*30^5*32*2=2177280000<C`.

The assumed failure of (4) gives

\[
\varepsilon\le(1+2^{-b/e})^e-1<3\,2^{-b/2}.
\]

Using `log 3<2` and `log 2>2/3`, this implies

\[
\log\varepsilon<2-b/3.
\tag{6}
\]

For `b>=K`,

\[
b/3-2>C(1+\log(2b)).
\]

At `K`, use `log(2K)<30` and `K/3-2>31C`; thereafter the difference
has derivative `1/3-C/b>0`. The logarithm bound follows from
`exp(1)>8/3` and `(8/3)^30>2K`. All numerical comparisons are checked
as exact rational inequalities in the certificate. Equations (5) and
(6) contradict one another. Therefore an exception must have `b<K`.

### 2.2 Complete continued-fraction coverage of the finite interval

Put `tau=a log 2-b log 3`. The failed gap implies

\[
0<\tau
\le e\log(1+2^{-b/e})
<e2^{-b/e}\le2\,2^{-b/2}.
\]

For `b>=14`,

\[
0<\frac ab-\log_2 3
<\frac3{b2^{b/2}}<\frac1{2b^2}.
\tag{7}
\]

The last inequality is `2^(b/2)>6b`. It holds at `b=14,15` by
squaring and exact comparison, and persists under `b -> b+2`.
Since `a/b` is reduced, Legendre's criterion makes it an upper
continued-fraction convergent of the irrational number `log_2 3`.
Its irrationality follows from unique factorization of powers of
2 and 3.

For `y=2,3` use `z=(y-1)/(y+1)` and the strict rational bounds

\[
L_y=2\sum_{j=0}^{127}\frac{z^{2j+1}}{2j+1}
<\log y<
U_y=L_y+\frac{2z^{257}}{257(1-z^2)}.
\tag{8}
\]

The geometric tail comparison proves these bounds. Applying the
continued-fraction algorithm simultaneously to `L_3/U_2` and
`U_3/L_2` certifies 26 common partial quotients through the first
denominator above `K`, which is `5409303924479`. This certifies all
convergents of denominator at most `K`.

There are exactly twelve upper convergents in that range. Of those
with denominator at least 14, one is `65/41` and the other nine have
denominator at least 306. The first is excluded by the exact integer
comparison

\[
2^{41}(2^{65}-3^{41})>3^{41},
\]

which is exactly (4) in this odd-`b` case. For every remaining
candidate the rational enclosure proves

\[
aL_2-bU_3>2^{-100}.
\]

But a failed gap would give

\[
\tau<2\,2^{-b/2}\le2^{-152}<2^{-100}.
\]

This excludes every `14<=b<K`. The script regenerates the full
convergent list; candidate completeness is not assumed from a list
of plausible approximants.

For each `1<=b<=13`, the script finds the least positive `a` satisfying
coprimality, `2^a>3^b`, and the exclusion of `(2,1)`. It verifies
(4) at that least exponent using rational arithmetic. Larger `a`
increase the left side. When `e=2`, the exact comparison is

\[
2^a>\left(3^{b/2}+(3/2)^{b/2}\right)^2,
\]

so no square-root approximation is used. These cases complete the
gap lemma.

## 3. All factors away from the integer slope

If `A!=2p`, its reduced pair is not `(2,1)`. Combining (3) and (4)
for every nonconstant monic integer factor `P` gives

\[
|P(3)|>\left(\frac32\right)^{\deg P}.
\tag{9}
\]

In particular this applies directly to `F_0`, proving (2).

This strengthens the earlier optional unit-factor argument; a separate
proof of merely `|P(3)|>1` is not needed for the present theorem.

## 4. The complete integer-slope case A=2p

The binomial now factors over the rationals as

\[
X^p-4^p=\prod_{h\mid p}P_h(X),\qquad
P_h(X)=4^{\varphi(h)}\Phi_h(X/4).
\]

Each `P_h` is monic with integer coefficients and irreducible over
`Q`, by irreducibility of the ordinary cyclotomic polynomial and
invertibility of linear scaling over `Q`. These factors are distinct.
Principal survival places `P_1=X-4` in `F_0`.

For `h>1`, the value `P_h(3)` is positive: when `h>2`, its nonreal
roots occur in conjugate pairs and each pair contributes a positive
squared distance from 3; for `h=2`, the factor is `X+4`. Thus the
absolute-value estimate below is also an estimate for `P_h(3)` itself.

I claim that every other factor satisfies

\[
P_h(3)>\left(\frac32\right)^{\varphi(h)}
\qquad(h>1).
\tag{10}
\]

Here is a uniform bound, retaining all conjugates. Let

\[
c_h(k)=\sum_{\zeta\text{ primitive }h}\zeta^k
\]

be the Ramanujan sum. Its elementary prime-power formula is

\[
c_{\ell^v}(k)=\ell^v\mathbf1_{\ell^v\mid k}
-\ell^{v-1}\mathbf1_{\ell^{v-1}\mid k}.
\]

Using multiplicativity over coprime moduli gives
`|c_h(k)|<=gcd(h,k)<=k`. For real `0<z<1`, the absolutely convergent
logarithm series, summed over all primitive roots, gives

\[
\log|\Phi_h(z)|
=-\sum_{k\ge1}\frac{c_h(k)z^k}{k}
\ge-\sum_{k\ge1}z^k.
\]

At `z=3/4` this is at least `-3`. Therefore

\[
P_h(3)\ge4^{\varphi(h)}e^{-3}.
\]

For `phi(h)>=4`, this is strictly greater than
`(3/2)^phi(h)`: indeed `(8/3)^4>27>e^3`, using `e<3`, and the
ratio increases with `phi(h)`. The elementary estimate `e<3`
follows by bounding `1/j!<=1/2^(j-1)` for `j>=2`, with strict
inequality at some terms.

The only `h>1` with `phi(h)<4` are `2,3,4,6`, and their values at
3 are respectively `7,37,25,13`, all satisfying (10). To check the
small list directly, every prime divisor `ell` of such an `h` has
`ell-1<=phi(h)<=2`, so only 2 and 3 can occur; their prime-power
totients then give exactly that list.

The product `F_0` contains `P_1`, whose absolute value at 3 is one.
If it contained no other factor, the exact repetition theorem in
`RESIDUAL_UNIT_EXCLUSION.md` would make the parity word a repetition
of `10` or `01`. Primitivity would force one of the two excluded
length-two words. Otherwise at least one factor in (10) occurs, and
multiplying their strict bounds gives

\[
|F_0(3)|>\left(\frac32\right)^{n-1}.
\tag{11}
\]

This completes the remaining slope without assuming that the positive
integer cycle problem has already excluded `A=2p`.

## 5. Combine value growth with primitive degree growth

The independent structural theorem in
`PRIMITIVE_RESIDUAL_DEGREE.md` proves

\[
p\le3^{n-1}
\]

for every primitive binary word. Its proof uses the finite Fourier
support of `2^(d_i)r^(-i)`, the actual cyclic word-period implication,
and the full Galois orbits of `alpha^b/2^a` for residual roots. The
principal binomial accounts for `b` roots with image one. There is
no growth assumption on its gcd, its word blocks, or its valuations.

Raising the displayed bound to the positive power `log_3(3/2)` and
using (9) or (11) proves (1).

## Inputs, validation, and limitations

The only imported deep analytic theorem is the real two-logarithm
case of Bugeaud--Mignotte--Siksek, *Classical and modular approaches
to exponential Diophantine equations I. Fibonacci and Lucas perfect
powers*, Annals of Mathematics 163 (2006), Theorem 9.4, printed page
989, a consequence of Matveev's theorem. Its hypotheses and constants
are instantiated in section 2.1. The primary journal PDF was inspected:
https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf

Legendre's continued-fraction criterion and elementary cyclotomic
irreducibility are also used as standard theorems. The rational-log
tail, root-modulus argument, Ramanujan-sum estimate, and all coverage
steps are supplied explicitly above. No GRH assumption is used.

The exact certificate has a finite role: rational logarithm enclosures,
complete convergent coverage below the proved cutoff, exact exclusion
of every candidate, small-pair comparisons, and tail constants. It
does not claim to formalize Matveev, Legendre, or this full proof in
Lean. Its normal and optimized executions must produce identical JSON;
malformed input checks run in both modes.

PR185's primitive family with `D_pol=exp(O(sqrt(A)))` is compatible
with the polynomial lower bound (1). No exponential-in-`A` estimate
is restored. More importantly, the actual reduced numerical denominator
also divides `D_pol` and may be much smaller. A lower bound for
`D_pol` is not a lower bound for that quotient. The principal-fibre
control family in `PRINCIPAL_FIBER_CONTROL.md` demonstrates exactly
how a surviving polynomial factor can be absorbed at `X=3`.

The unrestricted statement still needed for full positive-cycle
exclusion is `D_pol` not dividing `Q_0(3)` for every nontrivial
primitive candidate. Neither this note nor its executable certificate
asserts that statement.
