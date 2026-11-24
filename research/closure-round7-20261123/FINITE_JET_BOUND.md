# A finite, prefix-independent detector for every cycle denominator prime

23 November 2026. Parent: `e4367dd2c4406c1041e66d82dfba822908747fa3`.

**Status: PROPOSED written theorem, submitted for independent review.**
This sharpens the previous asymptotic Taylor-denominator obstruction to
an explicit finite certificate. Once a positive eventual cycle is given,
each prime of its reduced clock is detected within a bounded Taylor
order, independently of the length or content of the actual preperiod.
It does not construct the actual germ or a universal stopping procedure.
Full Collatz remains open.

## 1. Fixed source and complete denominator

Use the shortcut map `T(x)=x/2` for even `x`, `(3x+1)/2` for odd `x`.
For an actual ordinary source, use its literal parities `e_k`, odd counts
`p_k`, and binary analytic functions

\[
B_n(z)=\sum_{k\ge0}e_k3^{-p_{k+1}}z^k,
\qquad J_n(t)=B_n(2+t)=\sum_{j\ge0}c_j(n)t^j.
\]

The same definitions apply to a positive rational source with odd
denominator and an actually replayed periodic itinerary. Ordinary and
rational sources are distinguished below. No fitted finite germ replaces
the actual binary Taylor expansion.

For a chronological periodic word `w` of length `A>0` and odd count
`p>0`, put

\[
C_w(z)=\sum_{i=0}^{A-1}w_i3^{p-p_{i+1}}z^i,
\quad Q_w(z)=3^p-z^A,
\quad B_w(z)=C_w(z)/Q_w(z).
\]

Assume the full positive-cycle denominator `2^A-3^p` is positive.
Set

\[
g=\gcd(A,p),\quad u=A/g,\quad v=p/g,
\quad F(z)=z^u-3^v,\quad D_{\rm red}=F(2)>0.
\]

The preceding packet proves that `F` is irreducible and cannot cancel
from `B_w`. Its positive real root `r=3^(p/A)` satisfies
`1<r<2` and `C_w(r)>0`. Thus the integer

\[
\mathcal R_w=\operatorname{Res}(F,C_w)
=\prod_{F(\alpha)=0}C_w(\alpha)
\tag{1}
\]

is nonzero. The resultant convention in (1) uses monic `F`; its sign is
irrelevant to valuations. Integrality also follows directly: the product
is a rational symmetric expression in algebraic integers, hence is an
ordinary integer. Irreducibility and positivity ensure that none of its
factors is zero.

The exact earlier dependency is PR182 at
`e4367dd2c4406c1041e66d82dfba822908747fa3`,
`research/profound-round6-20261123/RATIONAL_SELECTION.md`, claims
R6-SEL-1--4, Git blob `54d7949ac80ec6b8286f0d03d579f9f6e0efe95f`.
Its finite polynomial and cycle arithmetic were Lean checked; the
irreducibility and analytic arguments had separately scoped written
reviews. This note uses the stated noncancellation, not a claim that the
full earlier analytic route was formalized.

## 2. Finite prime-detection theorem

For a prime `ell` dividing `D_red`, write

\[
d_\ell=v_\ell(D_{\rm red})>0,
\qquad b_\ell=v_\ell(\mathcal R_w)\ge0.
\]

Such a prime differs from two and three. Normalize `v_ell(ell)=1`.
For the rational Taylor coefficients of the periodic series, let

\[
\delta_\ell(w)=\min\{j\ge0:v_\ell(c_j(w))<0\}.
\]

**R7-DET-1 (finite resultant certificate).** This minimum exists and

\[
\boxed{\delta_\ell(w)
\le \left\lfloor\frac{u b_\ell}{d_\ell}\right\rfloor.}
\tag{2}
\]

Equivalently, if `N d_ell > u b_ell`, at least one of the first `N`
coefficients, indexed `0,...,N-1`, is not `ell`-integral. The entire
prime-power valuation in `D_red` occurs in this bound.

**Proof.** Work in a complete algebraic extension of `Q_ell` containing
all roots `alpha_i` of `F`. They are integral units. The translated roots
`beta_i=alpha_i-2` satisfy

\[
v_\ell(\beta_i)\ge0,\qquad
\sum_{i=1}^u v_\ell(\beta_i)=d_\ell.
\]

Choose one with `v_ell(beta)>=d_ell/u>0`, and write `alpha=2+beta`.
Each `C_w(alpha_i)` is integral, so the complete product (1) gives

\[
v_\ell(C_w(\alpha))\le b_\ell.
\tag{3}
\]

Suppose the first `N` actual Taylor coefficients are integral at `ell`,
and let `P_N(t)=sum_(j<N)c_j t^j`. The polynomial

\[
E_N(t)=C_w(2+t)-Q_w(2+t)P_N(t)
\]

has integral coefficients at `ell`. The defining Taylor identity shows
its first `N` coefficients vanish, so `E_N=t^N H_N`, where `H_N` is
also an integral polynomial at `ell`. At the genuine pole,

\[
C_w(\alpha)=\beta^N H_N(\beta),
\qquad
v_\ell(C_w(\alpha))\ge N v_\ell(\beta)
\ge N d_\ell/u.
\tag{4}
\]

Combining (3)--(4) gives `N d_ell<=u b_ell`. Choosing the least integer
`N>u b_ell/d_ell` proves that a nonintegral coefficient occurs before
`N`, giving (2). This is a finite polynomial evaluation argument. It
does not infer a finite detection order from a limsup without an
additional height estimate. No infinite-series evaluation at the pole
is used. Square.

The resultant can be computed after reducing `C_w` modulo `F`. That
changes neither (1) nor its prime valuations and avoids a Sylvester
matrix whose size depends on a long unreduced numerator degree.

## 3. A period-only bound, with no unknown height constant

**R7-DET-2 (explicit uniform bound for a specified period).** For every
prime `ell|D_red`, one of the first

\[
\boxed{M=u^2(2p-1)}
\tag{5}
\]

Taylor coefficients is not `ell`-integral.

To prove this, every complex root of `F` has modulus `r`, so

\[
|\mathcal R_w|\le C_w(r)^u.
\]

There are `p` nonzero summands in `C_w`. Each has coefficient at most
`3^(p-1)`, and its power of `r` is strictly below `r^A=3^p`. Thus

\[
C_w(r)<p3^{2p-1}<5^{2p-1}.
\tag{6}
\]

The last inequality holds for every integer `p>=1`: the ratio
`p(3/5)^(2p-1)` starts at `3/5` and its successive ratio is at most
`18/25<1`. Consequently

\[
5^{b_\ell}\le\ell^{b_\ell}\le|\mathcal R_w|
<5^{u(2p-1)},
\qquad b_\ell<u(2p-1).
\]

Now (2) and `d_ell>=1` give `delta_ell<M`.
This deliberately simple bound is not claimed optimal. The exact
resultant certificate (2) is typically much smaller.

Since `u<=A` and `p<=A`, a coarser bound depending only on a known
period bound `A<=L` is `L^2(2L-1)` coefficients. This does not provide
a universal period bound.

## 4. The first forbidden order cannot be hidden by a preperiod

**R7-DET-3 (prefix invariance).** Fix a prime `ell` other than two and
three. For every finite actual prefix `a` of length `h` and odd count
`s`, and every finite order `K`,

\[
c_0(n),\ldots,c_K(n)\in\mathbb Z_{(\ell)}
\quad\Longleftrightarrow\quad
c_0(T^hn),\ldots,c_K(T^hn)\in\mathbb Z_{(\ell)}.
\tag{7}
\]

Here `Z_(ell)` denotes the rational numbers with denominator prime to
`ell`. The statement applies whenever the displayed coefficients are
rational; eventual periodicity ensures this for the present application.

The exact actual-prefix identity is

\[
J_n(t)=\frac{C_a(2+t)}{3^s}
+\frac{(2+t)^h}{3^s}J_{T^hn}(t).
\tag{8}
\]

Its additive polynomial is integral at `ell`. Its multiplier is a
formal power-series unit over `Z_(ell)`, because its constant coefficient
`2^h/3^s` is a unit there. Its inverse `3^s(2+t)^(-h)` has integral
coefficients at `ell` as well. Reduce (8) modulo `t^(K+1)` and solve in
both directions. This proves (7), hence exact equality of the earliest
forbidden order along every finite actual prefix or tail.

The equivalent one-step proof uses the triangular equations

\[
3^e c_j(x)=2c_j(Tx)+
\begin{cases}e,&j=0,\\c_{j-1}(Tx),&j>0.\end{cases}
\]

The companion `GermConstruction.lean` checks the finite subring
equivalence for these equations when `1/2` and `1/3` belong to the
subring. The analytic definition of the actual coefficients remains the
written attachment, as in the preceding packet.

The full prefixed numerator also gives a direct norm check:
at a root of `F`, it is `alpha^h C_w(alpha)`. Since the norm of `alpha`
is a signed power of three, the prefixed resultant has the same
`ell`-valuation as (1). There is no hidden dependence on preperiod
length in (2) or (5).

## 5. A finite conditional test for an ordinary eventual cycle

**R7-DET-4.** Suppose one positive ordinary source is known to be
eventually periodic with cycle parameters `A,p`. If its first
`u^2(2p-1)` actual Taylor coefficients all lie in `Z[1/3]`, it reaches one.

Indeed, a nonstandard positive ordinary cycle has `D_red>1` coprime to
six, by the preceding packet's actual cycle-product and modulo-eight
argument. Choose a prime divisor. Equations (5) and (7) force a
forbidden coefficient in the stated range, a contradiction.

No limiting parity density, complex radius, or ternary radius is needed
for this statement after eventual periodicity is known. A certificate
that excludes nonstandard cycles through a supplied period bound still
does not establish eventual periodicity or construct the actual Taylor
coefficients for an arbitrary source. The exact resultant test likewise
depends on a supplied literal cycle word.

## 6. What the parallel construction does and does not show

The companion [ORDINARY_DESCENT.md](ORDINARY_DESCENT.md) constructs
positive rational cycles for which the first occurrence of a specified
denominator prime, five, is arbitrarily late, while the entire rational
cycle can lie above an arbitrarily prescribed positive floor. It
complements the period-dependent upper bound; there is no period-free
bound for this specified-prime problem over positive rational cycles.

That family may have other primes in its constant denominator. It is
not a family whose initial coefficients all lie in `Z[1/3]`, and it
does not refute an unproved uniform bound restricted to hypothetical
nonstandard ordinary integer cycles. Its ordinary finite shadows use
different, genuinely convergent sources for different finite horizons.
Those quantifiers are essential.

The new finite theorem is written algebra and valuation theory. This
file does not claim a Lean formalization of algebraic norms, the
resultant valuation, or the root-distance estimate. Exact finite
controls check the certificate and prefix invariance on selected words;
the general proof is Sections 2--4. The all-source germ construction and
full Collatz remain open.
