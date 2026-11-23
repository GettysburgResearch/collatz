# The principal binomial survives, and the unit case is exactly trivial

Date: 2026-11-23. Continuation of PR185 at
`39ba48e6a8af781193e28c679ea8ab64663c3aa6`.

## Main result

Let `A,p` be positive integers with `2^A>3^p`, and let a binary parity
word have odd positions

\[
0\le d_0<\cdots<d_{p-1}<A.
\]

Set

\[
F=X^p-2^A,\quad
Q=\sum_{i=0}^{p-1}2^{d_i}X^{p-1-i},\quad
G=\gcd_{\mathbb Q[X]}(F,Q)\text{ monic},\quad F_0=F/G,\quad Q_0=Q/G.
\]

Write `g=gcd(A,p)`, `A=ga`, `p=gb`, and `gcd(a,b)=1`. All of
`G,F_0,Q_0` have integer coefficients: `G` is a monic rational divisor
of the monic integer polynomial `F`, and division by a monic integer
polynomial preserves integer coefficients when exact.

**Theorem 1 (principal-binomial survival).**

\[
M(X):=X^b-2^a\quad\text{divides }F_0(X)\text{ in }\mathbb Z[X].
\tag{1}
\]

Consequently, for `D_pol=|F_0(3)|`,

\[
2^a-3^b\mid D_{\rm pol},\qquad D_{\rm pol}\ge2^a-3^b>0.
\tag{2}
\]

**Theorem 2 (complete unit classification for parity words).**

\[
D_{\rm pol}=1
\quad\Longleftrightarrow\quad
A=2p\text{ and }d_i=2i+\epsilon\ (0\le i<p)
\text{ for some }\epsilon\in\{0,1\}.
\tag{3}
\]

These are exactly repetitions of `10` and `01`, the two phases of
the shortcut cycle `1 -> 2 -> 1`. The corresponding rational fixed
point is `2^epsilon`. Every other positive word has odd
`D_pol>=3`.

Both theorems have elementary proofs below. They require no GRH,
logarithmic-form theorem, factorization classification, finite search,
or unproved Collatz assertion. The quantitative all-factor theorem in
`PRIMITIVE_DENOMINATOR_GROWTH.md` is a separate strengthening and
is not needed for either result here.

This closes the `D_pol=1` exception explicitly left in PR185's
distinguished-ideal criterion. It does not exclude
`D_pol | Q_0(3)` for a nonunit residual denominator.

## Proof of principal-binomial survival

Let `r=2^(a/b)>3`, the positive root of `M`.

First, `M` is irreducible over `Q`. To prove this directly, any
nonconstant monic integer factor `P` of `M` has all its roots on the
circle of radius `r`. If `h=deg P`, its constant coefficient has
absolute value

\[
r^h=2^{ah/b}.
\]

This is a positive integer. Its `b`-th power is `2^(ah)`, so prime
factorization implies it is a power `2^k` with `bk=ah`. Coprimality
of `a,b` gives `b|h`. Since `0<h<=b`, necessarily `h=b`.
Gauss's lemma now proves irreducibility. This reasoning works also
when `b=1`.

Every coefficient of `Q` is positive, so `Q(r)>0`. Thus `M` cannot
divide `Q`. In particular `G(r)!=0`: otherwise `G|Q` would force
`Q(r)=0`. Because `F=GF_0` and `F(r)=0`, it follows that `F_0(r)=0`.
The minimal polynomial `M` therefore divides `F_0` over `Q`; since
both are monic integer polynomials, it divides it over `Z` too.
Evaluation at 3 proves (2). QED.

The same argument applies to any nonzero polynomial with nonnegative
coefficients in place of the special numerator `Q`. In that sense
the survival statement is a general positivity theorem.

## Proof of the complete unit classification

Suppose first that `D_pol=1`. Equation (2) forces `2^a-3^b=1`.
If `a>=3`, this positive difference is `5` or `7 mod 8`, according
as `b` is odd or even. Thus `a<3`. The inequalities `2^a>3^b`
and `a,b>=1` then force `a=2,b=1`. Hence `A=2p`.

Every root `alpha` of the monic polynomial `F_0` has modulus four.
The reverse triangle inequality gives

\[
|3-\alpha|\ge1,
\]

with equality only when `alpha=4`. For example, its square is
`25-6 Re(alpha)>=1`, and equality forces `Re(alpha)=4` and
`Im(alpha)=0`.

The degree of `Q` is `p-1`, so `F_0` is nonconstant. The product of
the distances `|3-alpha|`, counted with multiplicity, is `|F_0(3)|=1`.
Every factor must equal one, hence every root is four. The binomial
`X^p-4^p` has simple roots in characteristic zero. Therefore

\[
F_0=X-4,\qquad
G=\frac{X^p-4^p}{X-4}
=\sum_{i=0}^{p-1}4^iX^{p-1-i}.
\tag{4}
\]

The polynomials `Q` and `G` both have degree `p-1`, so `Q/G` is
constant. Its value is the leading coefficient `2^(d_0)` of `Q`.
Comparing coefficients in (4) yields

\[
2^{d_i}=2^{d_0}4^i=2^{d_0+2i},\qquad d_i=d_0+2i.
\]

The final position `d_(p-1)<2p` forces `d_0<=1`. This gives (3).

Conversely, if either alternating profile in (3) holds, then
`Q=2^epsilon G` with the geometric polynomial `G` in (4).
The monic gcd of `F` and `Q` is exactly this `G`, so
`F_0=X-4` and `D_pol=1`. At 3 the geometric polynomial equals
`4^p-3^p`, giving the fixed point `Q(3)/(2^A-3^p)=2^epsilon`.

Finally, `F(3)=G(3)F_0(3)` is an odd nonzero integer, so `F_0(3)`
is odd. Every nonunit absolute value is at least three. QED.

## Exact repetition interface

The same polynomial argument identifies precisely when no additional
factor survives beside `M`.

**Proposition 3.** The following are equivalent:

1. `F_0=M`.
2. The parity word consists of `g` copies of one length-`a` word
   with `b` odd positions; equivalently there are
   `0<=e_0<...<e_(b-1)<a` such that
   `d_(jb+r)=aj+e_r` for `0<=j<g`, `0<=r<b`.

**Proof.** If `F_0=M`, then

\[
G=S:=\frac{X^{gb}-2^{ga}}{X^b-2^a}
=\sum_{j=0}^{g-1}2^{aj}X^{b(g-1-j)}.
\]

Since `Q=SR` and `deg R=b-1`, write
`R=sum_(r=0)^(b-1) c_r X^(b-1-r)`. The separated exponent blocks
do not overlap. Coefficient comparison gives
`2^(d_(jb+r))=2^(aj)c_r`. Setting `j=0` gives `c_r=2^(d_r)`;
therefore `d_(jb+r)=aj+d_r`. The final block bounds imply `d_r<a`.

Conversely, the stated repeated profile gives `Q=SQ_base` with
`deg Q_base=b-1`. The irreducible degree-`b` polynomial `M` is
coprime to `Q_base`. Hence
`gcd(SM,SQ_base)=S`, and `F_0=M`. QED.

Also, any nonconstant monic divisor of `F` has degree divisible by
`b`, by the constant-term argument in the proof of Theorem 1.
Thus, if `g>1` and the word is primitive,

\[
\deg F_0\ge2b.
\tag{5}
\]

This is a structural constraint, not an exclusion of high-degree
residual factors.

## The distinguished-ideal question after this result

PR185's exact remaining integrality test is

\[
D_{\rm pol}\mid Q_0(3).
\tag{6}
\]

The main theorem proves that a nontrivial word always has a genuine
nonunit denominator in this test, and that its entire principal
binomial factor survives polynomial cancellation. The remaining
numerator is evaluated at the particular residue class `X=3`.
An integer gcd at that point can be larger than the polynomial gcd.
The theorem supplies no inequality between its valuation and that
of `F_0(3)`.

In particular, the argument `Q(r)>0` excludes a characteristic-zero
root, not the finite-prime evaluation ideal `(ell^v,X-3)`. Transporting
that positivity to nonvanishing in a finite quotient would be an
unsupported step. The explicit unbounded control family in
`PRINCIPAL_FIBER_CONTROL.md` shows this obstruction directly:
primitive positive rational cycles, all phases above `19/10`, have
the principal factor completely absorbed by the actual integer
gcd while the polynomial gcd remains one.

## Refreshed sources, mathematical dependencies, and formal status

The following latest source attempts were read before this extension:

- PR175 at `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`,
  `ZERO_ATOM_CLOSING_ATTEMPT.md`: the actual zero fibre has a polynomial
  minimum-based upper bound, which still permits one primitive cycle.
- PR177 at `0444986571f09f302cb3687b4bba3552600e4119`,
  `ARITHMETIC_CYCLE_CONTINUATION.md`: sparse-return occupation forces
  complexity growth without supplying a universal complexity ceiling.
- PR178 at `7e4569476e152f6b8537bdc1711df595ec1ffd89`,
  `WHOLE_WORD_MERGER_ATTEMPT.md`: the actual smaller-ancestor reservoir
  has an exact residue formulation but no universal existence proof.

The present theorem addresses a distinct explicitly open branch of
PR185 and makes no claim to close those other inequalities.

No external analytic theorem enters the elementary main proof. It
uses factorization over the complex numbers, Gauss's lemma, prime
factorization, and coefficient comparison. A quantitative strengthening
for arbitrary monic factors, without numerator positivity, uses
Matveev and an exact continued-fraction certificate; its full
dependency boundary is in `PRIMITIVE_DENOMINATOR_GROWTH.md`.

The primary analytic source inspected for that quantitative strengthening
was Bugeaud--Mignotte--Siksek, *Classical and modular approaches to
exponential Diophantine equations I. Fibonacci and Lucas perfect
powers*, Annals of Mathematics 163 (2006), 969--1018, Section 9.1,
Theorem 9.4, printed page 989. Only its real two-logarithm specialization
is used there.
https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf

The source-qualified manuscript *Sparse block-sum and ordered-state
complexity in positive Collatz cycles*, rStation Paper 22 version 3,
was inspected for its half-word factors and power-gap certificate.
The elementary principal-survival proof above requires neither result.
https://rstation.ai/problems/collatz/papers/22/v3

This note itself is a written proof. The polynomial-to-word coefficient bridge is
formalized in `lean/ResidualWord.lean`; no end-to-end
Lean coverage of the complex-root irreducibility or survival argument
is claimed here. Every formal theorem should retain its exact proved
hypotheses. No full Collatz theorem is claimed.
