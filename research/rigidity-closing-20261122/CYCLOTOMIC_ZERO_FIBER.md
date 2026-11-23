# A full-denominator algebraic lift and a repaired zero-fiber argument

Date: 2026-11-22. Baseline: PR185 at
`980d40fc4afeaaf8f2a9256f322acf3e4568e013`.

**Status: an unrestricted cycle-closing attempt, with a proved explicit
two-parameter consumer. No unrestricted positive-cycle exclusion.**
The aim was to control the actual zero atom modulo the complete cycle
denominator using algebraic norms, rather than demand impossible uniform
mixing. A primitive-word hypothesis does not prevent cyclotomic
degeneracy of that norm. The example below retains the degenerate factor,
cancels it exactly, and then excludes the entire resulting family by an
integer Bezout identity. The family is structurally restricted; this is
not a claim to improve the strongest known general small-m-cycle bounds.

## 1. The zero atom being attacked

For a shortcut parity word with length A, p ones, and one positions
0<=d_0<...<d_(p-1)<A, put

\[
D=2^A-3^p>0,\qquad
C=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i}.
\]

An integral positive fixed point exists exactly when D divides C. Its
word is an actual parity itinerary. A primitive cycle gives A distinct
zero-residue rotations. The unrestricted goal remains a proof that the
number of such words is less than A, or a direct exclusion of divisibility.

## 2. The coprime number-field lift

Suppose gcd(A,p)=1. Let alpha=2^(1/p), K=Q(alpha), and
S=Z[1/6,alpha]. The polynomial X^p-2 is Eisenstein, so [K:Q]=p.
For integers r,s with pr+As=1, the complete quotient is

\[
S/(\alpha^A-3)\simeq\mathbb Z/D\mathbb Z,\qquad
\alpha\longmapsto 2^r3^s\pmod D.
\tag{N1}
\]

Indeed the image has p-th power 2 and A-th power 3 because 2^A=3^p
modulo D. Conversely alpha is the displayed monomial in the quotient.
Both 2 and 3 are units modulo D; negative exponents cause no omitted
denominator. The maps are inverse on the generators.

Set m_i=p d_i-Ai and P_w(alpha)=sum_i alpha^(m_i). Then

\[
D\mid C\quad\Longleftrightarrow\quad
P_w(\alpha)\in(\alpha^A-3)S.
\tag{N2}
\]

Modulo the ideal, P_w is C/3^(p-1). Its exponents represent each
residue class modulo p exactly once. Shifting all exponents makes them
nonnegative and only multiplies by an S-unit. The ideal norm is D up to
sign. Thus a nonzero numerator norm supplies a genuine whole-denominator
necessary divisibility condition.

The balanced interval case reduces to an S-unit: if the m_i are one
complete interval of p consecutive integers, then

\[
P_w(\alpha)=\alpha^h(1+\alpha+\cdots+\alpha^{p-1})
=\alpha^h/(\alpha-1),
\]

whose norm has no odd factor. This forces D=1. It does not classify
arbitrary ordered exponent walks. For an arbitrary spread R, the generic
triangle/Hadamard estimates allow factors on the scale p^p*2^R (or an
L2 refinement). They do not supply the exclusion needed at D~2^A.

## 3. Retain every component when gcd(A,p)>1

For g=gcd(A,p), the naive same field has

\[
\left|N_{K/\mathbb Q}(\alpha^A-3)\right|
=\left|2^{A/g}-3^{p/g}\right|^g,
\tag{N3}
\]

which is generally **not** the whole D. A norm argument using (N3) as
though it were D discards cyclotomic factors.

One uniform alternative is the finite rational algebra

\[
E=\mathbb Q[X]/(F_w),\qquad F_w(X)=X^p-2^A,
\qquad Q_w(X)=\sum_i2^{d_i}X^{p-1-i}.
\tag{N4}
\]

In the corresponding ring localized at 2, quotienting by X-3 gives
Z[1/2]/(D). Thus the exact test is still Q_w(3)=C modulo the full D.
The algebra norm of X-3 is the full D up to sign. The algebra can be a
product of fields, and a nonzero Q_w can have zero norm. Primitivity of
the parity word does not prevent this, as the next family demonstrates.

For comparison, a toric normalization retains the same components. Write
A=g a,p=g b and choose br+as=1. In the cycle quotient set

\[
v=2^a3^{-b},\quad u=2^r3^s,\quad
v^g=1,\quad u^b=2v^{-s},\quad u^a=3v^r.
\]

All g-th roots in the v coordinate must be retained, including the
nonprimitive roots. The gcd-one parametrization corresponds to g=1.
No componentwise estimate has been promoted here to an estimate on their
complete simultaneous arithmetic intersection.

## 4. A primitive family with a vanishing full algebra norm

Fix

\[
k=(0,0,1,1,0,2,1,0,0,1,1,2).
\tag{N5}
\]

Let b>=1, a-b>=2, and 2^a>3^b. Set A=12a,p=12b and define

\[
d_{bj+r}=aj+r+k_j,
\qquad 0\le j<12,\quad0\le r<b.
\tag{N6}
\]

These are legal increasing one positions in [0,A): d_0=0,
d_(p-1)=11a+b+1<A. Within each block the odd gaps are one. The boundary
gap from block j to j+1 is

\[
a-b+1+k_{j+1}-k_j\ge1,
\tag{N7}
\]

with cyclic subscripts. These are finite legal words, independently of
whether their rational cycle is integral.

**Primitivity.** Every gap different from one occurs at index b-1 modulo
b, and some such gaps exist. Any period of the cyclic gap word must
therefore be a multiple of b. A period of the boundary differences is a
period of k: the difference k_(j+h)-k_j would be constant, and summing
over j forces that constant to zero. The vector k has least period 12.
It has exactly two entries equal to 2, at indices 5 and 11, so the only
possible proper period is 6; k_0!=k_6 excludes that period. Thus the
gap word has least period 12b, and the parity word has least period 12a.
This also covers a-b=2, where one pair of runs merges.

Let

\[
R(Y)=\sum_{j=0}^{11}2^{k_j}Y^j
=(Y^4-Y^2+1)T(Y),
\tag{N8}
\]

where

\[
T(Y)=4Y^7+2Y^6+6Y^5+3Y^4+3Y^3+3Y^2+Y+1.
\]

Writing H_b(X)=sum_(r=0)^(b-1) 2^r X^(b-1-r), direct grouping gives

\[
Q_w(X)=H_b(X)\,2^{11a}R^*(X^b/2^a),
\qquad R^*(Y)=Y^{11}R(1/Y).
\tag{N9}
\]

Consequently both Q_w and F_w have the factor

\[
G_{a,b}(X)=X^{4b}-2^{2a}X^{2b}+2^{4a}.
\tag{N10}
\]

Indeed this is the homogenized Phi_12 factor, and

\[
F_w(X)=G_{a,b}(X)(X^{6b}-2^{6a})(X^{2b}+2^{2a}).
\]

The full algebra norm/resultant of Q_w is therefore zero for this
primitive family. Its cancellation is structural, not an integer cycle.
There are arbitrarily large parameters in the nontrivial-cycle cone:
for example a=5m,b=3m gives 4A<7p, 2^a>3^b, and a-b>=2.

## 5. Exact cancellation repairs the zero-residue argument for this family

Put s=2^a,t=3^b and

\[
G=t^4-s^2t^2+s^4>0,
\qquad D'=(s^6-t^6)(s^2+t^2)>0,
\]

\[
B(t,s)=t^7+t^6s+3t^5s^2+3t^4s^3+3t^3s^4
       +6t^2s^5+2ts^6+4s^7.
\tag{N11}
\]

The complete numerator and denominator are exactly

\[
\boxed{D=GD',\qquad C=(t-2^b)GB(t,s).}
\tag{N12}
\]

Here H_b(3)=3^b-2^b because 3-2=1. Thus full integrality is equivalent
to D' dividing (t-2^b)B. No uncancelled denominator factor is dropped.

Define f(Y)=(Y^6-1)(Y^2+1) and

\[
T^*(Y)=Y^7+Y^6+3Y^5+3Y^4+3Y^3+6Y^2+2Y+4.
\]

The following explicit integer polynomial identity is the useful bound:

\[
U(Y)f(Y)+V(Y)T^*(Y)=805,
\tag{N13}
\]

where coefficients are listed from constant term upward:

```
U = [-1353, -1926, -931, -1365, -971, -600, -392]
V = [-137, -413, -159, -21, 186, -21, 208, 392]
```

Equivalently, for U_h(t,s)=s^6 U(t/s), V_h(t,s)=s^7 V(t/s),

\[
-U_h(t,s)D'+V_h(t,s)B(t,s)=805s^{14}.
\tag{N14}
\]

Since D' is odd and s is a power of two, gcd(D',s)=1. Therefore

\[
\gcd(D',B(t,s))\mid805.
\tag{N15}
\]

If D' divided (t-2^b)B, Euclid's lemma would force

\[
D'\le805(t-2^b)<805t.
\tag{N16}
\]

But s and t are distinct integers with s>t>=3, so

\[
D'=(s^6-t^6)(s^2+t^2)\ge12t^7>805t.
\tag{N17}
\]

This contradiction proves: **none of the words (N6), for any parameters
in its stated domain, is an integral positive cycle.** No GRH, Matveev
bound, finite search cutoff, or external S-unit theorem is needed for
this particular consumer.

The unrestricted task remains open. For arbitrary words, one must control
the residual numerator after retaining every structural factor. Neither
a bounded number of residual terms, a uniform small Bezout constant, nor
a norm bound sharp enough to exclude all remaining divisibility has been
proved. These are exactly the inputs that the explicit family supplies
and an arbitrary cycle does not yet supply.

## 6. One ordinary control and scope of execution

For a=5,b=3, the word has A=60,p=36 and least shortcut period 60. Its
full values are

\[
D=1002826869309847855,\qquad C=8287225771885636121,
\]

\[
\gcd(C,D)=5834647=7\cdot833521,
\qquad C/D=1420347412943/171874471465.
\]

The shared Phi_12 factor at 3 is 833521. The rational cycle is positive
and nonintegral. The checker also constructs and replays an ordinary
positive integer source realizing the entire exact odd-gap word, so
finite word legality is not inferred from rational positivity.

`check_cyclotomic_zero_fiber.py` uses integer polynomial arithmetic only.
It verifies (N8), (N13), the symbolic two-variable denominator identity,
the exact A=60,p=36 factorization and ordinary source, and rejected damaged
certificates. These finite controls support the displayed identities;
the all-parameter theorem is the written proof (N6)--(N17).

## 7. Literature and current repository relation

The fixed-dimensional nondegenerate S-unit theorem of Evertse,
Schlickewei and Schmidt is a genuine candidate for a general norm
continuation. Its primary Theorem 1.1 bounds solutions in terms of both
dimension and group rank. It does not give a dimension-free assertion
as the number of word terms grows. This pass inspected the primary
statement and the discussion of necessary dimension dependence, not
its full proof again:
<https://arxiv.org/pdf/math/0409604> and
<https://annals.math.princeton.edu/2002/155-3/p04>.

Lam--Leung's primary indexed abstract on vanishing sums of roots of unity
provided relevant context for cyclotomic components. Direct full-text
retrieval returned HTTP403; no theorem from that paper is a dependency of
the explicit identities above:
<https://doi.org/10.1006/jabr.1999.8089>.

The recent Paper136/v1 uses cyclotomic divisors of a different, nonzero
Hankel determinant for prescribed growing-block schedules. Its source
height estimate is not an arbitrary-word zero-atom bound. Its stated
theorem and factorization mechanism were inspected, with external claims
kept SOURCE-QUALIFIED:
<https://rstation.ai/problems/collatz/papers/136>.

Latest PR175 `08fe1388ad63c758680b3695249aca319515c47d`,
`machinery/FIXED_BLOCK_INTEGRAL_RIGIDITY.md` and
`machinery/REGULAR_CYCLE_LANGUAGE_COROLLARY.md`, constrain fixed repetition
schemas and regular languages whose accepted words are all integral.
Latest PR177 `e4ca639326bac73da8c2a698dec8a749e5efbe68`,
`LITERATURE_ARITHMETIC_RETURN.md`, derives sparse binary-run returns using
the same S-unit finiteness input. Neither supplies the universal bounded
description of an arbitrary cycle needed to apply its conclusion globally.
This note's contribution is the exact full-denominator norm test, its
primitive cyclotomic failure mode, and a complete repaired consumer.

## 8. Primitivity does not force a large residual polynomial denominator

A tempting continuation of the norm route would assert that, after
cancelling the complete polynomial gcd, a primitive word in the cycle
cone retains a denominator of size exp(c*A), for an absolute c>0. The
following family disproves that assertion. This is a statement about
**polynomial gcd cancellation**; the reduced rational denominator can be
smaller still after evaluating at 3.

Let m,n>=2 be distinct coprime integers and L=2mn. On cyclic indices
0<=j<L set

\[
c_j=2^{k_j}
 =1+\mathbf1_{j\equiv0\pmod{2m}}
   +\mathbf1_{j\equiv1\pmod{2n}}.
\tag{N18}
\]

The two indicator supports are disjoint, being respectively even and
odd. Hence c_j is either 1 or 2 and k_j is either 0 or 1. The coefficient
polynomial is

\[
R(Y)=\frac{Y^L-1}{Y-1}
 +\frac{Y^L-1}{Y^{2m}-1}
 +Y\frac{Y^L-1}{Y^{2n}-1}.
\tag{N19}
\]

Define the monic integer polynomials

\[
H(Y)=\operatorname{lcm}(Y^{2m}-1,Y^{2n}-1)
 =\frac{(Y^{2m}-1)(Y^{2n}-1)}{Y^2-1},
\quad
G(Y)=\frac{Y^L-1}{H(Y)}.
\tag{N20}
\]

Then **gcd(R,Y^L-1)=G**, with monic gcd convention. To prove this, test
all L-th roots zeta, which are simple. Outside the roots of H, each sum
in (N19) vanishes. At a root of Y^(2m)-1 that is not a root of
Y^(2n)-1, R(zeta)=n. In the reverse case R(zeta)=m*zeta. The common
roots are 1 and -1, at which the values are L+n+m and n-m. All these
values are nonzero. This proves both the claimed factors and the absence
of any further factors. In particular

\[
\deg H=2m+2n-2.
\tag{N21}
\]

**Primitivity.** The profile has n entries equal to 2 on even indices
and m on odd indices. An odd period would interchange these two counts,
which is impossible because m!=n. An even period 2h preserves each
parity class; its restrictions force m|h and n|h. Coprimality then forces
L|2h. Thus the profile has least cyclic period L.

Embed this into actual parity words by taking a=5,b=3 and

\[
A=5L,\quad p=3L,\qquad d_{3j+r}=5j+r+k_j\quad(0\le r<3).
\]

The positions are increasing and lie in [0,A). Here d_0=1, so the first
parity letter is even; this causes no issue for the full carry formula.
The within-block gaps are 1 and the boundary gaps are
3+k_(j+1)-k_j in {2,3,4}. Consequently every gap different from 1 is
exactly at index 2 modulo 3. A period of the gap word is therefore a
multiple of 3, and then induces a period of the boundary differences.
As in Section 4, a period of those differences is a period of k. Thus
the parity word has least period A. It lies in the strict cone 4A<7p,
and 2^A>3^p follows from 32>27.

Set s=32,t=27 and let H_hom,G_hom denote the homogeneous versions of
H,G. The complete polynomial carry factors as

\[
F(X)=X^{3L}-s^L=G_{\rm hom}(X^3,s)H_{\rm hom}(X^3,s),
\]

\[
Q(X)=(X^2+2X+4)s^{L-1}R^*(X^3/s).
\]

The roots of X^2+2X+4 have modulus 2; all roots of F have modulus
32^(1/3)>2. Hence that factor is coprime to F. The reciprocal R* has
the same common cyclotomic factors as R, since G is a product of
reciprocal cyclotomic polynomials. Substitution introduces no repeated
roots. Therefore the complete monic polynomial gcd of F and Q is
exactly G_hom(X^3,s).

The denominator remaining after this polynomial cancellation is exactly

\[
D_{\rm pol}
=|H_{\rm hom}(t,s)|
=\frac{(s^{2m}-t^{2m})(s^{2n}-t^{2n})}{s^2-t^2}.
\tag{N22}
\]

If G0=gcd(F,Q), the actual reduced denominator of C/D is
D_pol/gcd(D_pol,|(Q/G0)(3)|), so it is at most D_pol. The distinction
matters: (N22) claims exactness only before this additional integer gcd.

For successive parameters n=m+1,

\[
A=10m(m+1),\qquad
1\le D_{\rm pol}<2^{20m+2}.
\tag{N23}
\]

Indeed writing r=27/32 gives D_pol=
32^(4m)*(1-r^(2m))*(1-r^(2m+2))/(1-r^2), and
1/(1-r^2)=1024/295<4. Thus log(D_pol)=O(sqrt(A)) along an unbounded
primitive family in the strict cone. No bound D_pol>=exp(c*A) with a
fixed c>0 can follow from just primitivity and that cone. This is a
structural family calculation, not a search over candidate cycles.

## 9. A residual norm can contain all of D at the wrong conjugates

There is a second loss of information even when the polynomial gcd is
one and A,p are coprime. Consider the single word

\[
A=13,\quad p=8,\quad d=(0,1,2,3,4,6,8,9).
\]

It is primitive because A is prime and the word is nonconstant. It
satisfies 4A=52<56=7p. Its complete polynomials and values are

\[
F=X^8-8192,
\qquad
Q=X^7+2X^6+4X^5+8X^4+16X^3+64X^2+256X+512,
\]

\[
D=1631=7\cdot233,\quad C=Q(3)=7553,\quad\gcd(C,D)=7,
\]

\[
\gcd(F,Q)=1,\qquad
\operatorname{Res}(F,Q)=-2^{71}\cdot7\cdot233^2.
\tag{N24}
\]

In particular the **whole D divides the nonzero resultant**, although
D does not divide C. This is not an accidental sign or localization
issue: removing all powers of 2 and 3 from the resultant still leaves
7*233^2, divisible by D.

The exact mechanism is visible locally. Modulo 7, F and Q share the
root X=3. Modulo 233, they instead share X=-3=230, while
Q(3)=97 mod 233. Thus the norm aggregates different conjugates at the
two prime factors. It forgets which prime ideal lies over the
**distinguished evaluation X=3**. The counterexample applies already
with gcd(A,p)=1, so merely repairing the missing noncoprime components
cannot repair this second loss.

For arbitrary words define G0=gcd(F,Q), F0=F/G0, Q0=Q/G0 and
D_pol=|F0(3)|. The exact unrestricted condition remains

\[
D\mid C\quad\Longleftrightarrow\quad D_{\rm pol}\mid Q_0(3).
\tag{N25}
\]

The norm implication D_pol | Res(F0,Q0) is only necessary. A proposed
universal proof that D_pol does not divide that resultant would be
false by (N24). The missing global arithmetic step must retain the
ideals (ell^v,X-3) for the actual prime powers ell^v dividing D_pol.
One sufficient target, explicitly at the right fiber, is

\[
\sum_{\ell\mid D_{\rm pol}}
 \min\{v_\ell(Q_0(3)),v_\ell(D_{\rm pol})\}\log\ell
 <\log D_{\rm pol}
\tag{N26}
\]

whenever D_pol>1, followed by separate handling of D_pol=1. Equation
(N26) is precisely a strict gcd bound, not a theorem proved here. Its
point is to specify what survives both counterexamples: the valuation
must be at the same evaluation ideal at every prime. ESS does not
currently supply this bound as polynomial degree and word complexity
grow. No hidden assertion of (N26) is used in the family proof of
Section 5.

## 10. Cyclic rotations are exact unit multiples in the norm algebra

Cyclic rotations do not repair the loss. With F=X^p-2^A, a one-letter
left rotation satisfies the exact polynomial identities

\[
2Q_{\rm rot}=Q\quad\text{if the first letter is even},
\qquad
2Q_{\rm rot}=XQ-F\quad\text{if the first letter is odd}.
\]

Consequently in E=Q[X]/(F), after ell letters with p_ell odd letters,

\[
Q_{\rm rot,ell}=X^{p_{\ell}}2^{-\ell}Q,
\quad
\left|N_E(Q_{\rm rot,ell})\right|
=2^{A p_{\ell}-p\ell}|N_E(Q)|.
\tag{N27}
\]

Since X^p=2^A, these multipliers are units away from 2. In the corresponding Z[1/2]-order, every prime
ideal over an odd rational prime sees exactly the same vanishing status;
in each number-field component, the prime-ideal valuation is unchanged. Their nonzero resultant odd parts are
identical. In particular every rotation of (N24) retains the same
wrong-conjugate obstruction. Thus the A rotations are not independent
S-unit equations for this norm route; they are exact unit multiples
inside the same finite algebra.

`check_residual_norm_obstructions.py` independently checks the displayed
identities at two controls for Section 8, and checks (N24) using exact
integer Bareiss elimination on the 15-by-15 Sylvester matrix. It also
checks the two indicated modular roots and rejects a perturbed
resultant certificate. This is a targeted check of failed universal
inequalities, not a finite cycle census.

Tao's 2011 primary exposition discusses precisely the complete-denominator
counting and Littlewood--Offord route. Its Propositions 6--7 and ensuing
discussion distinguish a useful lower bound for 2^A-3^p from the zero
residue exclusion. This pass inspected that argument directly:
<https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/>.
It is relevant prior-art context, not a theorem imported into (N18)--(N26).
