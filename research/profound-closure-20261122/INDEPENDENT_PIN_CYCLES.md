# Complete exclusion with two independent repetition counts

## Result

Let `T(n)=n/2` for even n and `T(n)=(3n+1)/2` for odd n. An odd gap g
denotes the shortcut parity word `1 0^(g-1)`. Put

\[
P=(1,1,4,1,1,1,2),\qquad Q=(2).
\]

**Theorem.** There is no positive ordinary cycle with odd-gap word
`P^m Q^n`, for any independently chosen integers m,n>=1. This includes
every cyclic rotation. In the whole bounded language `P* Q*`, the only
positive cycles are the trivial repetitions `Q^n`, n>=1; the empty word
does not assert a cycle.

This extends the previous diagonal result `P^k Q^k` to every point in the
positive two-dimensional exponent quadrant. The proof uses Matveev's
published logarithm theorem, a finite exact continued-fraction certificate,
and a Lean-checked physical arithmetic interface. Matveev and the full
continued-fraction closure have not been formalized in this Lean packet.
No finite numerical search over m,n is used as a replacement for a cutoff.

## 1. Actual paths force a complete integer equation

Suppose the P-run starts at x and ends at y. Its exact affine equation is

\[
2048^m(y+41)=2187^m(x+41).
\tag{1}
\]

The Q-run returns from y to x exactly when

\[
4^n x+3^n=3^n y+4^n.
\tag{2}
\]

Every actual ordinary gap cycle satisfies these equations, as proved by
the imported `BlockPath` lemmas. Coprimality in (1) gives a positive integer t
such that

\[
x+41=2048^m t,\qquad y+41=2187^m t.
\tag{3}
\]

Substitution into (2) yields

\[
\boxed{
\bigl(2^{11m+2n}-3^{7m+n}\bigr)t
=42(4^n-3^n),\qquad t\ge1.
}
\tag{4}
\]

Both the whole denominator and its required integer cofactor remain
present. In particular, the denominator is strictly positive.
`independent_integer_quotient` and `independent_gap_cycle_necessary`
check this inference in Lean, including the connection to the actual gap
equations. The latter arithmetic relation allows even more natural-number
paths than ordinary odd trajectories, so its necessary conditions apply
to every ordinary cycle in the stated language.

## 2. The entire cone n>=m is impossible

If n>=m, then

\[
\frac{2187^m3^n}{2048^m4^n}
\le\left(\frac{6561}{8192}\right)^m
\le\frac{6561}{8192}.
\]

The complete cross equation is

\[
2048^m4^n x+42\,2048^m3^n
=2187^m3^n x+2048^m4^n+41\,2187^m3^n.
\]

If x>=170, nonnegativity and the ratio bound would imply
`169*8192 <= 211*6561`; the left side exceeds the right side by 77.
Thus x<170. But (3) gives x>=2048^m-41>=2007. Contradiction.

The Lean theorem `no_independent_cycle_of_twos_ge_pins` proves this whole
cone exclusion without a logarithm theorem or finite parameter census.
Hence any remaining candidate has

\[
1\le n<m,\qquad m\ge2.
\tag{5}
\]

## 3. Physical divisibility forces an exponentially small logarithm

Set

\[
p=11m+2n,\qquad q=7m+n,\qquad
\Lambda=p\log2-q\log3.
\]

By (4), Lambda>0. Dividing (4) by `2^(11m+2n)*t` gives

\[
0<1-e^{-\Lambda}
=\frac{42(1-(3/4)^n)}{2048^m t}
<\frac{42}{2048^m}<\frac12.
\]

For 0<z<1/2, `-log(1-z) < 2z`. Therefore

\[
\boxed{0<\Lambda<84\,2^{-11m}.}
\tag{6}
\]

This is the essential ordinary-integer information: repetitions of P
require an exponentially large dyadic factor in x+41. A real affine
candidate without that factor would not give (6).

## 4. The external logarithm theorem supplies a global cutoff

Matveev, *An explicit lower bound for a homogeneous rational linear form
in the logarithms of algebraic numbers. II* (2000), Corollary 2.3,
printed p.1219, gives

\[
\log|\Lambda|>-C_1(2)D^2\Omega\log(eD)\log(eB^*).
\]

Use the real field Q (D=1), alpha_1=2, alpha_2=3, A_1=1, A_2=2.
The height and logarithm conditions hold. The displayed minimum in the
primary theorem gives C_1(2)<=2^32, and Omega=2. Unique factorization
ensures Lambda is nonzero. Thus

\[
\log|p\log2-q\log3|
>-2^{33}(1+\log\max(p,q)).
\tag{7}
\]

The primary statement was read directly and its formula visually checked;
the full proof of Matveev's theorem was not re-audited. A stable source is
<https://www.mathnet.ru/eng/im314> (DOI 10.4213/im314).

For a deliberately coarse application, replace 2^33 by C=10^12. From
(5), q<8m and p<16m. Equations (6)--(7) imply

\[
11m\log2<\log84+C(1+\log(16m)).
\tag{8}
\]

This is impossible when m>=M=10^14. Here is an explicit all-tail check.
Write m=M*s, s>=1. Since `16M<2^51`, `log2<7/10`, and `84<2^7`,

\[
\log84+C(1+\log(16m))
<5+37C+C(s-1),
\]

where `log s<=s-1`. On the other hand,
`11m log2 > (11M/2)s`. At s=1 the latter exceeds `5+37C`, and its
linear coefficient exceeds C. All comparisons are explicit integer
inequalities. Consequently

\[
\boxed{m<10^{14},\qquad q<8\cdot10^{14}.}
\tag{9}
\]

The checker verifies a slightly sharper version of these margins using
its rational logarithm enclosure. This finite bound comes from (7), not
from extrapolating an experimental enumeration.

## 5. Legendre reduces every remaining pair to a short exact list

Put alpha=log3/log2. By (6) and log2>1/2,

\[
0<\frac pq-\alpha<\frac{168}{q\,2^{11m}}.
\]

For m>=2, `2^(11m)>2688m>336q`: the first inequality holds at two and
is preserved on multiplying by 2048. Hence

\[
\left|\frac pq-\alpha\right|<\frac1{2q^2}.
\tag{10}
\]

Reduce p/q to a/b. Since b<=q, Legendre's theorem implies that a/b is a
continued-fraction convergent of alpha. The standard theorem is also
formalized in the pinned Mathlib as `Real.exists_rat_eq_convergent`
in `Mathlib/NumberTheory/DiophantineApproximation/Basic.lean`.

The signs in (6) require an upper convergent. Its possible integer scales
are completely controlled. Write p=d*a,q=d*b. Then

\[
m=\frac{d(2b-a)}3,\qquad
n=\frac{d(7a-11b)}3.
\tag{11}
\]

The least positive admissible scale is
`d0=3/gcd(3,2b-a)`; every admissible d is a positive multiple of d0.
If the corresponding m0,n0 are outside (5), no scale works. If m0>=M,
the global cutoff excludes every scale. Otherwise it suffices to prove

\[
d_0(a\log2-b\log3)>84\,2^{-11m_0},
\tag{12}
\]

because the left side increases and the required right side decreases
under all larger scales. Thus no unbounded scale search is hidden in
the finite list.

## 6. Exact rational certificate and complete coverage

For r=1/3 and r=1/2 respectively, use

\[
\log\frac{1+r}{1-r}
=2\sum_{j=0}^{95}\frac{r^{2j+1}}{2j+1}+R,
\qquad
0<R\le\frac{2r^{193}}{193(1-r^2)}.
\tag{13}
\]

These give rational enclosures for log2 and log3. Common continued-fraction
digits of the resulting alpha interval certify every consecutive
convergent, not a selected subset. The certificate contains **32** such
convergents, ending with denominator

\[
5\,750\,934\,602\,875\,680>8\cdot10^{14}.
\]

Before that terminal denominator, 16 are lower convergents, one has
m0=0, one already has m0>=M, and all 13 remaining upper convergents
violate (6) by the exact test (12). For speed the test uses
`2^min(11*m0,66)`, a weaker comparison that avoids constructing enormous
integers. The first admissible upper convergent is 8/5, with d0=3,
m0=2,n0=1; it is already separated by a wide rational margin.

The generator is `independent_pin_certify.py`. The separate verifier
`independent_pin_verify.py` does not import the generator. It recomputes
the logarithm series by a separate recurrence, checks the complete omitted
tail, validates every consecutive continued-fraction digit, checks both
cutoffs and the minimum integer scaling, and proves every required
separation by rational arithmetic. Acceptance contains no floating-point
decision and does not depend on Python assertions.

Both ordinary and optimized Python runs accept the certificate and reject
eight damaged versions: an omitted convergent, an incomplete terminal
cover, a wrong digit, wrong scaling, an omitted logarithm tail, an
unsupported Matveev constant, an insufficient denominator cutoff, and an
invalid dyadic comparison. The published replay records exact bytes and
fresh execution separately.

## 7. Zero exponents, literature relationship, and full-theorem scope

If m=0,n>0, the Q-run fixes exactly x=1 and gives the trivial odd cycle.
If n=0,m>0, the P-run fixes exactly -41, so it has no positive cycle.
If both counts vanish, the word is empty. Rotating a realized cycle merely
changes its starting state, so all cyclic rotations have the same exclusion.

The architecture follows the cycle methods of Steiner and
Simons--de Weger: an exponentially small linear form from actual cycle
arithmetic, an effective transcendence lower bound, then exact Diophantine
reduction. See Simons and de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1 problem*, Acta Arithmetica 117 (2005), 51--70,
and the authors' version 1.43 (2007), sections 1.4 and 3:
<https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf>.
Here the repetition count m is not their number of local minima; the
repeated internal block can contain an unbounded number of such minima.
No external finite computational verification of Collatz is used.

This is a complete result for the displayed bounded language, not an
assertion that all positive cycles have that form. The companion general
bounded-language theorem handles arbitrary fixed block lists and
independent exponent vectors; universal complexity control and escaping
aperiodic trajectories remain separate.
