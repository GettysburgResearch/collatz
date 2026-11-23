# High rational cycles with ordinary finite-Fourier lifts

Date: 2026-11-23.

**Status: source-qualified written consequence.** The generic lifting argument
below is elementary. Its infinite quadratic-height family is conditional on
the proposed written theorem in
[PR182, `CYCLE_IDEAL.md`, Sections 1–5a](https://github.com/GettysburgResearch/collatz/blob/aa12c13601cacec2c8496f1349b4947457dc1b45/research/high-variance-20261123/CYCLE_IDEAL.md),
at exact head `aa12c13601cacec2c8496f1349b4947457dc1b45`. That source reports
completed internal reconstruction reviews; its full existence and infinite
height theorem are not claimed Lean-formalized here. This consequence does
not construct an integer cycle or exclude all such cycles.

## 1. Input and conclusion

Fix \(M\ge1\) coprime to six, a prime \(\ell\ge5\) not dividing \(M\),
and **\(Q=2^r3^s\), with \(r,s\ge0\)**. Put \(K=6Q\).

The cited source supplies infinitely many primitive positive rational
shortcut cycles \((x_i)_{i\bmod L}\), with parity word \(w\), weight \(P\),
complete denominator \(D=2^L-3^P>0\), and complete numerator \(C=C(w)\),
such that

\[
4L<7P,\qquad M\mid C,D,\qquad\ell\mid D,\quad\ell\nmid C,
\]

and

\[
m_*:=\min_i x_i>cL^2,\qquad
c=\frac1{3888M^2t^2},\quad t=\operatorname{lcm}(\varphi(M),\ell-1).
\tag{1}
\]

For every sufficiently large member, there are distinct positive integers
\(n_0,\ldots,n_{L-1}\) with the same ordered parities, avoiding multiples
of three, whose polynomial \(G(z)=\sum_i z^{n_i}\) satisfies

\[
\mathcal TG-G\equiv0\pmod{z^{3Q}-1},\qquad
\|\mathcal TG-G\|_{\ell^2(\mathrm{coeff})}^2=2L. \tag{2}
\]

Their minimum exceeds \(cL^2/2-1\) and satisfies

\[
D\bigl(3\min_i n_i+1\bigr)\le P2^L. \tag{3}
\]

Thus the finite Fourier tests, high ordinary inputs, primitive ordered
parities, prescribed word congruences and the cycle-minimum inequality
coexist with a nonzero full polynomial residual. The ordered lifts are
**not an actual integer orbit**: every image lies outside their source set.
The preserved \(C,D\) are those of the original parity word, not a claim
that the lifts follow its edges exactly.

## 2. Generic lifting proof

Write \(x_i=A_i/D\) using the complete common denominator. Since
\(\gcd(D,6)=1\), the restriction on \(Q\) ensures \(\gcd(D,K)=1\).
Every \(A_i\) is nonzero modulo three: in the complete carry of a rotated
word, only its final odd contribution survives modulo three.

Put \(h=\lfloor m_*/2\rfloor\). For each \(i\), choose the unique integer
in the half-open block

\[
[h+Ki,h+K(i+1))
\]

that satisfies \(n_i\equiv A_iD^{-1}\pmod K\). These integers are distinct,
have the prescribed parity, and avoid multiples of three. By (1), eventually
\(h>2KL\). In particular they are all greater than one and lie below
\(h+KL<m_*\).

If \(\epsilon_i\) is their prescribed parity, the actual rational edge gives

\[
2A_{i+1}=3^{\epsilon_i}A_i+\epsilon_iD.
\]

Reduction modulo \(K\), followed by division of the resulting integer
congruence by two, yields

\[
T(n_i)\equiv n_{i+1}\pmod{K/2}=\pmod{3Q}.
\]

Summing proves the polynomial congruence in (2), hence vanishing of its
residual at every root of unity whose order divides \(3Q\).

The residual nevertheless has disjoint positive and negative supports.
An even source has image

\[
T(n_i)<(h+KL)/2<h,
\]

whereas an odd source has image

\[
T(n_i)\ge(3h+1)/2>h+KL.
\]

Images are injective within each parity class, and the two image ranges are
disjoint. Thus the \(L\) distinct images are disjoint from the \(L\)
distinct sources. The residual has exactly \(L\) coefficients \(+1\) and
\(L\) coefficients \(-1\), proving its squared coefficient norm in (2).

## 3. The minimum inequality requires no integrality

Let \(y_1,\ldots,y_P\) be the odd states of the rational cycle. Multiplying
its accelerated edge equations gives

\[
\frac{3^P}{2^L}
=\prod_{j=1}^P\left(1-\frac1{3y_j+1}\right).
\]

The elementary product-deficit inequality therefore gives

\[
\frac D{2^L}
\le\sum_{j=1}^P\frac1{3y_j+1}
\le\frac P{3m_*+1}.
\]

Since every lift is below \(m_*\), (3) follows. Also
\(\min_i n_i\ge h>cL^2/2-1\), proving the claimed height.

The construction retains the cited word's full \(M\)-divisibility and bad
prime \(\ell\). It does not assert cancellation of the full valuations at
primes dividing \(M\). For a general Fourier modulus, lifting instead
requires invertibility of the reduced rational denominator at that modulus;
\(M\mid C,D\) alone does not supply it. No adaptive-frequency or
full-denominator method is ruled out.

This generic proof was checked in-session independently by the root agent.
No new infinite-dimensional theorem, Lean formalization, or numerical
verification is claimed for this late consequence.
