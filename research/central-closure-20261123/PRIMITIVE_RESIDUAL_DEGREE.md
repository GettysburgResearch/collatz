# Primitive parity words require growing residual polynomial degree

Date: 2026-11-23. Written theorem; not an end-to-end Lean development.

## Statement

Let a binary parity word of length $A\ge1$ have $p\ge1$ odd positions

\[
0\le d_0<d_1<\cdots<d_{p-1}<A.
\]

Define

\[
F(X)=X^p-2^A,\qquad
Q(X)=\sum_{i=0}^{p-1}2^{d_i}X^{p-1-i},
\]

and take the monic rational polynomial gcd $G=\gcd(F,Q)$. Put
$F_0=F/G$, $n=\deg F_0$, $g=\gcd(A,p)$, $A=ga$, and $p=gb$.
Thus $\gcd(a,b)=1$. The word is **primitive** when it has no positive
cyclic shift smaller than $A$ that leaves its odd-position set invariant.

**Theorem.** If the parity word is primitive, then

\[
\boxed{g\le3^{n-b},\qquad
       p\le b3^{n-b}\le3^{n-1}.}
\tag{1}
\]

In particular, bounded residual polynomial degree cannot occur along
primitive words with an unbounded number of odd positions. Explicitly,

\[
\boxed{n\ge1+\log_3 p.}
\tag{2}
\]

Thus $n=\Omega(\log p)$ as $p\to\infty$.

There is no positivity-cone hypothesis $2^A>3^p$ in this theorem.
It applies in particular to the positive-cycle cone. It gives a degree
bound, not a lower bound of the same form for $|F_0(3)|$, and does not
exclude the remaining integer divisibility at $X=3$.

## 1. The monic factor and its degree

The monic polynomial $G$ has integer coefficients, by Gauss's lemma,
and exact division by a monic polynomial gives $F_0\in\mathbb Z[X]$.
Since $\deg Q=p-1$, one has $n\ge1$.

Let $r=2^{A/p}=2^{a/b}>0$. Every root of $F_0$ has modulus $r$.
The absolute value of the nonzero constant coefficient of $F_0$ is

\[
r^n=2^{an/b}\in\mathbb Z_{>0}.
\]

Raising to the $b$th power and using prime factorization shows that
$b\mid an$. Since $\gcd(a,b)=1$, this gives

\[
b\mid n,\qquad b\le n.
\tag{3}
\]

The same argument proves $M=X^b-2^a$ irreducible: a nonconstant monic
integer factor of $M$ has positive degree divisible by $b$, hence full
degree. Since $Q(r)>0$, the common factor $G$ cannot vanish at $r$.
The identity $F=GF_0$ then gives $F_0(r)=0$, so the minimal polynomial
$M$ divides $F_0$. Thus

\[
M\mid F_0.
\tag{3a}
\]

This is the principal-binomial survival argument from the companion
note. Its proof uses only $r>0$, so it remains valid without the
positive-cycle cone. No classification of the other irreducible factors
of $F$ is required.

## 2. Normalize the coefficient word

Put

\[
c_i=2^{d_i}r^{-i}>0,\qquad
C(Y)=\sum_{i=0}^{p-1}c_iY^i.
\]

For every $p$th root of unity $\zeta$,

\[
Q(r\zeta^{-1})
 =r^{p-1}\zeta^{-(p-1)}C(\zeta).
\tag{4}
\]

Let

\[
\mathcal S=\{\zeta:\zeta^p=1,\ C(\zeta)\ne0\}.
\]

The polynomial $F$ has simple roots. Its gcd with $Q$ cancels exactly
those roots where $Q$ vanishes. Hence (4) gives a bijection

\[
\mathcal S\longrightarrow\{\alpha:F_0(\alpha)=0\},
\qquad \zeta\longmapsto r\zeta^{-1}.
\tag{5}
\]

In particular $|\mathcal S|=n$. Since $C(1)=\sum c_i>0$, the root
of unity $1$ belongs to $\mathcal S$.

## 3. Primitivity makes the support orders generate the full clock

Let

\[
L=\operatorname{lcm}\{\operatorname{ord}(\zeta):\zeta\in\mathcal S\}.
\]

All these orders divide $p$, so $L\mid p$ and $1\le L\le p$.
I claim that a primitive word has

\[
L=p.
\tag{6}
\]

Assume instead $L<p$. At any $p$th root of unity $\zeta$, either
$C(\zeta)=0$ or $\zeta^L=1$. Therefore

\[
Y^p-1\mid (Y^L-1)C(Y)
\quad\text{over }\mathbb C[Y].
\tag{7}
\]

The use of all the distinct roots justifies this divisibility. Reducing
the right side modulo $Y^p-1$ cyclically shifts the coefficient vector
by $L$. Its remainder is zero, so

\[
c_{i+L\bmod p}=c_i\qquad(0\le i<p).
\tag{8}
\]

Here is the ordinary-word, including wraparound, implication. Extend the
odd-position sequence to all nonnegative indices by

\[
D_j=d_{j\bmod p}+A\lfloor j/p\rfloor.
\]

Because $r^p=2^A$, the sequence $2^{D_j}r^{-j}$ is exactly the
$p$-periodic extension of $(c_i)$. Equation (8) gives

\[
2^{D_{j+L}-D_j}=r^L\qquad(j\ge0).
\tag{9}
\]

At $j=0$, set $\ell=d_L-d_0$. This is a positive integer because
$0<L<p$. Raising (9) to the $p$th power yields
$2^{p\ell}=2^{AL}$, so

\[
p\ell=AL,\qquad 0<\ell<A.
\tag{10}
\]

The injectivity of the real exponential $2^x$ in (9) now gives
$D_{j+L}=D_j+\ell$ for every $j$. Taking residues modulo $A$, the
original odd-position set is unchanged by adding $\ell$: adding $L$
permutes its indices modulo $p$. Thus the original binary word is fixed
by the proper cyclic shift $\ell$, contrary to primitivity.
Moreover $L\mid p$ and (10) imply $A=\ell(p/L)$, so this is also a
literal repeated block of length $\ell$. This proves (6).

This step is essential: primitivity of the binary parity word is not
silently replaced by primitivity of an unrelated polynomial or of a
symbolic approximation.

## 4. Use the rational image and retain its full Galois orbits

For each root $\alpha$ of $F_0$, form

\[
\eta=\frac{\alpha^b}{2^a}.
\]

Since $\alpha^{gb}=2^{ga}$, each $\eta$ is a $g$th root of unity.
Let $\mathcal T$ be their set of distinct values, and let $\mathcal H$
be the set of orders that occur in $\mathcal T$.

The polynomial $F_0$ is rational and the map $\alpha\mapsto\alpha^b/2^a$
is rational. Therefore $\mathcal T$ is stable under the absolute Galois
group. If one primitive $h$th root occurs, all its $\varphi(h)$
cyclotomic conjugates occur. Different orders give disjoint conjugacy
classes. Consequently

\[
|\mathcal T\setminus\{1\}|
 =\sum_{\substack{h\in\mathcal H\\h>1}}\varphi(h).
\tag{11}
\]

Principal survival (3a) matters here: all $b$ distinct roots of $M$
occur among the $n$ roots of $F_0$, and they all map to $\eta=1$.
There are at most $n-b$ remaining distinct images. Thus

\[
\boxed{\sum_{\substack{h\in\mathcal H\\h>1}}\varphi(h)\le n-b.}
\tag{12}
\]

For the correspondence (5), the image is $\eta=\zeta^{-b}$. Taking
$b$th powers of a collection of roots of unity whose order lcm is $p$
changes that lcm to $p/\gcd(p,b)=p/b=g$. This follows directly from
$\operatorname{ord}(\zeta^b)=\operatorname{ord}(\zeta)/\gcd(\operatorname{ord}(\zeta),b)$, by taking the maximum valuation
at each prime. Equation (6) therefore gives

\[
\operatorname{lcm}\{h:h\in\mathcal H\}=g.
\tag{13}
\]

These are full Galois orbits of the rational image. The proof does not
assert that a homogenized cyclotomic substitution in the original
variable is irreducible, nor count just one selected conjugate.

## 5. An elementary bound for each image order

Every integer $m\ge1$ satisfies

\[
m\le2\varphi(m)^2.
\tag{14}
\]

Indeed, for a prime power $q^e\Vert m$,

\[
\frac{q^e}{\varphi(q^e)^2}
 =\frac{q^{2-e}}{(q-1)^2}
 \le\frac q{(q-1)^2}.
\]

The last quantity is at most one for every odd prime and at most two
for the prime two. Multiplication proves (14); the case $m=1$ is
immediate.

For every integer $u\ge1$, one also has $2u^2\le3^u$. Check $u=1,2$
directly; for $u\ge2$ the ratio of the next left-hand side to the
current one is $(1+1/u)^2\le9/4<3$, proving the rest by induction.
Taking $u=\varphi(m)$ in (14) yields

\[
\boxed{m\le3^{\varphi(m)}.}
\tag{15}
\]

## 6. Assemble the bound

By (13), $g$ is the least common multiple of the image orders. The
order one contributes nothing to this least common multiple or its
product bound. Equations (12) and (15) give

\[
g\le\prod_{\substack{h\in\mathcal H\\h>1}}h
 \le3^{\sum_{h\in\mathcal H,\ h>1}\varphi(h)}
 \le3^{n-b}.
\]

An empty product is one, so this also covers $g=1$. Finally,
$b\le3^{b-1}$ for every positive integer $b$, by the base case $b=1$
and the induction inequality $b+1\le3b$. Hence

\[
p=bg\le b3^{n-b}\le3^{n-1},
\]

as claimed. The exact argument covers $n=b=1$, without a logarithmic
exception or a lower size threshold.

## Relation to the repository and exact boundary

PR185 at `39ba48e6a8af781193e28c679ea8ab64663c3aa6`,
`research/rigidity-closing-20261122/CYCLOTOMIC_ZERO_FIBER.md`, Section 8,
constructs primitive words whose residual denominator has subexponential
growth in the word length. The present theorem concerns the degree of
the polynomial factor that remains; it does not contradict that family
or restore the disproved exponential-in-$A$ denominator estimate.

The proof above grew out of an independent review of the principal
survival and repetition results in `nov23_cycle/RESIDUAL_UNIT_EXCLUSION.md`,
SHA256 `3d6619371246f4918e0c5a57eee2ef1c2f08b76c0794fddcaba869baab498eaf`.
It extends the degree restriction $n\ge2b$ for primitive words with
$g>1$ to a bound that grows with the full odd clock $p$, including when
$b$ stays fixed. The normalization and parity-period argument came from
this lane; the cycle lane supplied the rational-image/Galois-orbit
sharpening, and retaining the repeated image of the principal factor
gives (12). No global priority claim is made for finite Fourier support
or cyclotomic degree; this is a proved application to the repository's
exact residual polynomial.

The remaining cycle-closing line is still

\[
|F_0(3)|\nmid Q_0(3)
\]

for every nontrivial primitive candidate. Residual degree growth alone
does not compare the prime-power valuations of those two evaluations.
This note contains no GRH assumption, no finite search extrapolation,
and no assertion that the displayed unrestricted nondivisibility has
been proved.
