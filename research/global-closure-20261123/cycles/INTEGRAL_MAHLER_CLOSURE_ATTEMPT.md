# The complete word, Mahler rigidity, and the degree-one obstruction

Date: 23 November 2026.

**Status: attempted unrestricted positive-cycle proof; no closure obtained.**
The elementary propositions below are written proofs. The independent-base
Mahler consequence is **SOURCE-QUALIFIED** by the cited primary theorem.
There is no new Lean claim. The purpose is to test a deep rigidity route
against the complete arithmetic condition, with all word lengths and all
denominator factors retained.

## 1. Exact target and what the latest work supplies

Use the shortcut Collatz map
\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a binary word of length \(A\) with \(p>0\) ones at
\(0\le d_0<\cdots<d_{p-1}<A\), put
\[
\alpha=3^p,\qquad \beta=2^A,\qquad
C=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i},\qquad D=\beta-\alpha.
\tag{1}
\]
The formal branch composition is \((\alpha x+C)/\beta\). We restrict to
\(D>0\), so its fixed point \(C/D\) is positive. Its prescribed word is a
genuine rational itinerary with odd reduced denominator. If \(D\mid C\),
it is an actual positive ordinary cycle. One way to check the latter
assertion is that the first incorrect prescribed parity creates a reduced
even denominator, and all subsequent formal branches increase its
2-primary denominator; it cannot return to the integral fixed point.

Thus the all-word target is \(D\nmid C\) for every primitive positive word
other than the two length-two words \(10,01\). An exclusion of cycles would
still leave possible unbounded positive ordinary orbits as a separate part
of full Collatz.

The latest inputs were read at these exact heads:

- **PR185, `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`:** its
  `PRIMITIVE_DENOMINATOR_GROWTH.md` proves a polynomial lower bound for
  \(|F_0(3)|\), after cancelling a polynomial gcd. This does not lower-bound
  \(|F_0(3)|/\gcd(|F_0(3)|,Q_0(3))\). Its
  `PRINCIPAL_FIBER_CONTROL.md` gives primitive rational words whose
  complete surviving principal 5-primary component is absorbed at the
  correct evaluation \(X=3\).
- **PR176, `ff3e068fa44eb85bb918580b2e10e18c027a18e6`:** its
  `IDENTITY_ATOM_ATTEMPT.md` retains the exact zero residue through
  \[
  [z^p]\operatorname{tr}(P_0+zP_1)^A=D\,N_0(A,p).
  \tag{2}
  \]
  The unproved strict bound \(N_0<A\) would exclude nontrivial cycles.
  Its comparable unit-fiber example already defeats the proposed
  coordinatewise antichain argument.
- **PR175, `8870528daa6a13cc941d602e578e35c8bfa4bf4f`:** its
  `ALL_WORD_POLYNOMIAL_ATTACK.md` keeps the full positive state
  polynomial, gives its exact dyadic-tail elimination, and distinguishes
  full support matching from prime-product balance.
- **PR182, `aa12c13601cacec2c8496f1349b4947457dc1b45`:** its
  `CYCLE_IDEAL.md` supplies high primitive rational controls passing any
  prescribed fixed congruence precision. This does not rule out an
  adaptive test using all of the actual denominator.

These are source inspections, not a new verification of every argument
or a replay of their Lean modules. The present attempt changes the route
to the remaining *simultaneous* numerical cancellation.

## 2. The polynomial route and the precise Mahler question

Let \(S\) be a hypothetical finite positive shortcut cycle and
\[
P(z)=\sum_{n\in S}z^n.
\]
Writing \(P(z)=E(z^2)+zO(z^2)\), its exact invariance is
\[
E(z^2)-E(z)=z^2O(z^3)-zO(z^2).
\tag{3}
\]
This is the formulation and dyadic elimination already supplied in PR175,
Section 2. It is not counted as a new result here.

Let
\[
f(z)=\sum_{j\ge0}z^{2^j},
\qquad
S_{\rm odd}=\{n\in S:n\text{ odd}\},
\qquad
K_S(z)=\sum_{n\in S_{\rm odd}}f(z^n).
\tag{4}
\]
These are formal power series over \(\mathbb Q\), and are analytic for
\(|z|<1\). If \(a(n)=v_2(3n+1)\) and
\(U(n)=(3n+1)/2^{a(n)}\), then
\[
f(z^{3n+1})
=f(z^{U(n)})-\sum_{j=0}^{a(n)-1}z^{2^jU(n)}.
\tag{5}
\]
The map \(U\) permutes \(S_{\rm odd}\). The finite states on the odd-to-odd
edge from \(n\) are precisely \(2^jU(n)\), \(0\le j<a(n)\).
Summing (5) therefore gives the full-state identity
\[
P(z)=K_S(z)-\sum_{n\in S_{\rm odd}}f(z^{3n+1}).
\tag{6}
\]

The proposed next step was to turn this mixed \(2/3\) identity into two
independent Mahler equations for \(K_S\), then apply an independent-base
rigidity theorem. The next proposition determines what that route would
actually require.

### Proposition 1: every nonzero finite odd-support lift is nonrational

Let \(M\) be a finite set of distinct positive odd integers, and let
\(c_m\) be coefficients in a characteristic-zero field, not all zero. Then
\[
K(z)=\sum_{m\in M}c_m f(z^m)
\tag{7}
\]
is not a rational function.

**Proof.** Distinct positive odd \(m\) give disjoint sets
\(\{m2^j:j\ge0\}\). Thus the coefficient at \(m2^j\) is exactly \(c_m\).
For any \(m\) with \(c_m\ne0\), there are infinitely many nonzero
coefficients. The support up to \(X\) has at most
\[
|M|\bigl(1+\lfloor\log_2 X\rfloor\bigr)
\tag{8}
\]
elements. Consequently there are arbitrarily long consecutive blocks of
zero coefficients arbitrarily far out: a uniform upper bound on the gaps
would give a positive linear lower bound on the support count, contradicting
(8).

If \(K=P_0/Q_0\) were rational, take \(Q_0(0)\ne0\) and
\(d=\deg Q_0\). For all sufficiently large indices, the coefficients of
\(K\) satisfy the order-\(d\) homogeneous recurrence obtained from
\(Q_0K=P_0\). If \(d=0\), \(K\) is a polynomial, already impossible.
For \(d>0\), a block of \(d\) zero coefficients beyond the recurrence's
starting index forces every subsequent coefficient to be zero, by forward
induction. This contradicts the infinitely many coefficients \(c_m\).
\(\square\)

The same argument proves linear independence of the dyadic rays
\(f(z^m)\), for distinct positive odd \(m\), **modulo rational functions**.
It does not prevent the exact same ray from occurring on both sides of
(6). That matching is precisely the actual odd-state permutation.

### Corollary 2: the needed independent equation is absent, even at the core

From \(f(z)-f(z^2)=z\), every series (7) satisfies
\[
K(z)-K(z^2)=\sum_{m\in M}c_m z^m.
\tag{9}
\]
It is therefore 2-Mahler. Adamczewski--Bell, *A problem about Mahler
functions*, Theorem 1.3, says that a formal power series over a
characteristic-zero field that is both \(k\)-Mahler and \(\ell\)-Mahler
for multiplicatively independent integers \(k,\ell>1\) is rational.

Apply that theorem with \(k=2,\ell=3\). Proposition 1 proves that every
nonzero series (7) is **not 3-Mahler**. The statement holds for arbitrary
finite odd support, so in particular for the support of any positive
ordinary cycle, if one exists.

The trivial cycle already shows the issue concretely:
\[
S=\{1,2\},\qquad K_S=f,\qquad
f(z)-f(z^4)=z+z^2.
\tag{10}
\]
It supplies a second power-of-two relation, not an independent base-three
relation. The conclusion does not assume the absence of other cycles.

In (6), the second term is
\[
\sum_{j\ge0}z^{2^j}\sum_{n\in S_{\rm odd}}z^{3n2^j},
\tag{11}
\]
whereas
\[
K_S(z^3)=\sum_{j\ge0}\sum_{n\in S_{\rm odd}}z^{3n2^j}.
\]
The factor \(z^{2^j}\) depends on the dyadic clock. Replacing it by an
outside factor \(z\), or dropping it, would change the exact equation.
The additive \(+1\) has not disappeared into an independent dilation.

**Result of this attack.** The primary rigidity theorem applies if the
independent equation is proved, but that equation is impossible for the
natural nonzero finite-support lift, including the known core. A new
auxiliary construction could still be useful. No such construction
satisfying the necessary independent hypotheses was obtained here.

## 3. A full-denominator torus normalization

The additive term can be kept exactly by moving to two variables.
For the complete word data (1), consider the torus map
\[
\Phi_w(x,y)=\bigl(x^\alpha,x^C y^\beta\bigr)
\quad\text{on }(\mathbb C^\times)^2.
\tag{12}
\]
All the following algebra is over the integer character lattice; there is
no passage to one denominator factor or to a field norm.

Put
\[
g=\gcd(C,D),\qquad r=C/g,\qquad s=D/g.
\tag{13}
\]
Then \(r,s>0\), \(\gcd(r,s)=1\), and \(Dr=Cs\). Define
\[
H_w(x,y)=\bigl(x,x^r y^s\bigr),\qquad
\Delta_w(u,v)=\bigl(u^\alpha,v^\beta\bigr).
\tag{14}
\]

### Proposition 3: the diagonalizing degree is the actual denominator

The exact semiconjugacy identity is
\[
H_w\circ\Phi_w=\Delta_w\circ H_w.
\tag{15}
\]
The kernel of \(H_w\) is
\[
\{(1,\zeta):\zeta^s=1\},
\tag{16}
\]
so its degree is \(s=D/\gcd(C,D)\).

**Proof.** The second coordinate of \(H_w\Phi_w\) is
\[
x^{\alpha r+Cs}y^{\beta s}
=x^{\beta r}y^{\beta s},
\]
since \(Cs=Dr=(\beta-\alpha)r\). This is the second coordinate
of \(\Delta_wH_w\); the first coordinates agree directly. The kernel
calculation is immediate, with exactly \(s\) roots of unity over
\(\mathbb C\). \(\square\)

This is the *minimal* positive degree among triangular monomial maps
\((x,y)\mapsto(x,x^{r'}y^{s'})\), \(r'\in\mathbb Z,s'>0\), that preserve
the first coordinate and give (15). Comparing exponents forces
\(Dr'=Cs'\). Since \(r/s=C/D\) is reduced, \(s\mid s'\).
In particular,
\[
\begin{aligned}
D\mid C
&\iff s=1\\
&\iff H_w\text{ is an automorphism of the torus}\\
&\iff \Phi_w\text{ is diagonalized by an integral triangular torus automorphism}.
\end{aligned}
\tag{17}
\]
For \(s=1\), the inverse of \(H_w\) is \((u,v)\mapsto(u,u^{-r}v)\).
Conversely, \(s>1\) gives a nontrivial kernel, so \(H_w\) is not invertible.

Equation (17) preserves exactly the sought ordinary integrality.
It does **not** prove that a nontrivial primitive word has \(s>1\).

### Why the two-variable Mahler direction does not remove the degree

The character
\[
\chi_w(x,y)=x^r y^s
\]
satisfies
\[
\chi_w\circ\Phi_w=\chi_w^{2^A}.
\tag{18}
\]
Also let \(\Psi(x,y)=(x^2,y^2)\). Then
\(\chi_w\circ\Psi=\chi_w^2\). Consequently
\(f(\chi_w(x,y))\), interpreted as its convergent series near the origin,
satisfies exact Mahler identities under both maps. But along this character
the two dilation factors are \(2\) and \(2^A\); they are dependent.

This character exists for **every** positive rational word, at every
denominator degree \(s\). The apparently independent multiplier \(3^p\)
in the first coordinate does not act as an independent multiplier on
this series. Independent-base rigidity cannot be applied merely because
both 2 and 3 occur somewhere in (12).

For example, the word \(11010\) has
\[
(A,p,C,D)=(5,3,23,5),\qquad (r,s)=(23,5).
\]
The same exact normalization and Mahler character exist, with degree five.
For \(10\), they exist with \((r,s)=(1,1)\).
These two arithmetic checks illustrate the degree distinction; they are
not a bounded cycle search.

The intrinsic reduced degree here is also different from PR185's
polynomial residual denominator. Its lower bound for \(D_{\rm pol}\)
does not bound \(s\) unless the additional numerical gcd is controlled.
The principal-fiber family shows why one component's survival before
evaluation cannot supply that comparison by itself.

## 4. Further closing attempts and their first unsupported step

The affine trace (2) was retained as the direct alternative. The needed
bound is still \(N_0<A\), equivalently a bound below \(AD\) for the
unnormalized trace coefficient. Positivity, the ordinary operator norm,
and conservation under cyclic rotation did not provide this bound.
No all-residue antichain assumption was reused after the explicit PR176
counterexample.

Primitive-divisor reasoning was considered at the complete denominator.
For \(A=ga,p=gb\), a new prime divisor of
\((2^a)^g-(3^b)^g\) would be useful only if it also failed to divide the
*ordered* numerator \(C\) at its full required valuation. A primitive
divisor of the denominator alone does not establish that second claim.
For coprime \(A,p\), there is no increasing common exponent \(g\) on which
that argument alone could operate.

The S-unit gcd route was also checked against the primary literature.
Corvaja's 2010 account states the relevant gcd and quotient theorems for
fixed multiplicative groups and fixed power sums. Those results can
control specified finite dictionaries or sparse supports. They do not,
as stated, give a single effective bound for the numerator in (1) as its
support size, exponents and polynomial all vary with the unrestricted
word. Merely writing each summand as a \(\{2,3\}\)-unit does not supply
such a uniform theorem. The full growing-support estimate needed here
was not proved.

The torus route makes the final arithmetic step especially explicit:
\[
\boxed{
s_w=\frac{2^A-3^p}{\gcd\!\left(2^A-3^p,\,
\sum_i2^{d_i}3^{p-1-i}\right)}>1
}
\tag{19}
\]
for every nontrivial primitive positive word. It is exactly the statement
that the full denominator supplies a nontrivial kernel in (16).
A proof must distinguish this from the case \(s_w=1\); the written
semiconjugacy and the available Mahler identities permit both.

No statement in this packet bounds all primitive periods, establishes
(19), or resolves the escape half of Collatz. The new primary-theorem
application check and integral-lattice normalization identify where this
particular ambitious route must acquire additional arithmetic content.

## 5. Primary literature and exact scope

1. B. Adamczewski and J. P. Bell, *A problem about Mahler functions*,
   Ann. Sc. Norm. Super. Pisa Cl. Sci. (5), XVII (2017), 1301--1355.
   [Primary journal PDF](https://journals.sns.it/index.php/annaliscienze/article/download/574/560/792).
   Definition 1.1 and Theorem 1.3, printed pp. 1303 and 1306, were read
   directly. The theorem is imported as stated; its 55-page proof is not
   claimed independently verified or Lean-formalized.
2. P. Corvaja, *Upper bound for the gcd(u-1,v-1), u,v S-units,
   generalisations and applications*, RIMS Kokyuroku 1710 (2010), 1--6.
   [Primary author lecture PDF](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1710-01.pdf).
   The statements of Theorems 2--4 and their fixed-data hypotheses were
   inspected. No new gcd estimate is claimed here.
3. PR175's exact polynomial encoding and dyadic elimination are reused as
   explicitly credited above. Its references to Neklyudov are retained as
   source attribution, not counted as a separate primary-paper review
   in this lane.

All new arguments in Sections 2--3 are written derivations. No empirical
sample is extrapolated to a universal theorem, and no absence of a new
proof is disguised as a machine-checked closure.
