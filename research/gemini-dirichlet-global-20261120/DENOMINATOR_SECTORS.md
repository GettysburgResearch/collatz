# Denominator sectors and the proposed spectral penalty

**Scope.** This note audits Route 4 of the supplied `collatz_routes_bundle`.
It proves an exact obstruction to one proposed norm change, not an
obstruction to adaptive proofs about positive integers. Collatz is not
resolved here. The operator and its domain are specified in each statement.

Let the shortcut map on rational numbers with odd reduced denominator be

\[
T(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(3x+1)/2,&x\equiv1\pmod2.\end{cases}
\]

For a reduced fraction with odd denominator, parity means its image in
\(\mathbb Z_2/2\mathbb Z_2\).

## DS1. Reduced denominator is exactly conserved away from 2 and 3

Put

\[
S=\{a/q>0:\gcd(a,q)=1,\ q\ge1,\ \gcd(q,6)=1\}.
\]

Then \(T(S)\subseteq S\), and

\[
\operatorname{den}(T(x))=\operatorname{den}(x)\qquad(x\in S). \tag{1}
\]

**Proof.** Write \(x=a/q\) in lowest terms. Since \(q\) is odd, the
parity of \(x\) is that of \(a\). If \(a\) is even, the reduced output
is \((a/2)/q\), and \(\gcd(a/2,q)=1\). If \(a\) is odd, the output is
\(((3a+q)/2)/q\). The numerator is integral. Any common divisor of this
numerator and \(q\) divides \(3a\); it is one since \(\gcd(q,3a)=1\).
This proves (1). Positivity is preserved. \(\square\)

More generally, for every prime \(p\ge5\), a negative valuation is
conserved: if \(v_p(x)<0\), then \(v_p(T(x))=v_p(x)\). In the odd
branch, \(v_p(3x)<0=v_p(1)\), so the unequal-valuation rule gives
\(v_p(3x+1)=v_p(x)\); division by two changes nothing. This also shows
why a height made only from prime-to-six denominator exponents has no
strict drift along these rational orbits.

## DS2. Any finite sector reweighting is an isometric conjugacy

Let \(v:S\to(0,\infty)\) be a finite positive weight. Let
\(a:\{q\ge1:\gcd(q,6)=1\}\to(0,\infty)\) be any finite positive
function. On atomic signed or complex masses use the norms

\[
\|f\|_v=\sum_{x\in S}v(x)|f(x)|,\qquad
\|f\|_{av}=\sum_{x\in S}a(\operatorname{den}x)v(x)|f(x)|.
\]

Suppose a fixed forward weighted pushforward

\[
(Kf)(y)=\sum_{T(x)=y}w(x)f(x) \tag{2}
\]

is bounded on \(\ell^1(v)\). The same formula is bounded on
\(\ell^1(av)\), with the same norm and spectrum. Indeed

\[
(Jf)(x)=a(\operatorname{den}x)f(x)
\]

is an onto isometry from \(\ell^1(av)\) to \(\ell^1(v)\), with
inverse division by the same finite factor, and (1) gives
\(JK=KJ\). These facts prove isometric conjugacy. They also preserve
essential spectra and essential norms, since conjugating a compact
operator by bounded isomorphisms preserves compactness.

In particular, changing the norm by
\(a(q)=\operatorname{rad}(q)^{-\beta}\) has no spectral effect on a
fixed operator (2). With \(\beta>0\), this particular weight makes
large-denominator atoms cheaper. Replacing the minus sign by a plus
sign still has no spectral effect of the proposed kind.

For the **unweighted actual forward pushforward** \(w=1\), every finite
cycle \(x_0,\ldots,x_{p-1}\) supplies the nonzero finite-norm vector

\[
\mu=\sum_{i=0}^{p-1}\delta_{x_i},\qquad K\mu=\mu.
\]

Every finite denominator penalty retains this eigenvector. For a
weighted operator, its cycle multiplier is the product of the weights
around that cycle; denominator reweighting leaves that product unchanged.
In particular, a coboundary weight \(w(x)=b(Tx)/b(x)\) has cycle product
one. A coefficient tilt that is not such a coboundary may change cycle
eigenvalues, but that change comes from the operator, not from the
denominator norm factor.

**Boundary.** This proves nothing against a space that excludes the
atomic cycle measures, imposes additional regularity, or assigns an
infinite cost to nonintegral support. Such a proposal must separately
show that its space contains the objects needed to infer the desired
pointwise statement for every positive integer. On integer support,
\(q=1\) and this entire denominator factor is constant. The statement
does not rule out well-founded integer arguments or precision that grows
with a fixed ordinary source.

## DS3. Forward pushforward and Haar transfer are different operators

On \(C(\mathbb Z_2)\), let

\[
(Uf)(x)=f(Tx),\qquad
(Lf)(y)=\tfrac12\left[f(2y)+f((2y-1)/3)\right]. \tag{3}
\]

These are the Koopman and Haar Perron--Frobenius operators, respectively.
Both inverse branches in (3) exist for every \(y\in\mathbb Z_2\), since
three is invertible there. Each has one half of Haar mass. In particular,
\(LU=I\), \(\|U\|=\|L\|=1\), and \(L^jU^j=I\).

For every compact \(C\) and integer \(j\ge1\),

\[
\|L^j-C\|\ge\|(L^j-C)U^j\|
=\|I-CU^j\|\ge1.
\]

The last inequality is the usual distance-one property of the identity
from compact operators on an infinite-dimensional Banach space.
Taking \(C=0\) supplies the opposite bound. Hence

\[
\|L^j\|_{\rm ess}=1,\qquad r_{\rm ess}(L)=1. \tag{4}
\]

Thus the supplied proposal's essential-radius value on this particular
space is correct. Its explanation using rational-cycle distributions
conflates two dual operators. Actual forward pushforward on measures is
\(U^*\), not \(L^*\). Already the ordinary cycle measure
\(\mu=(\delta_1+\delta_2)/2\) gives

\[
U^*\mu=\mu,\qquad
L^*\mu=\tfrac14(\delta_2+\delta_{1/3}+\delta_4+\delta_1)\ne\mu.
\]

The displayed operator in Route 4, containing a guard
\(y\equiv2\pmod3\), is neither (3) nor the finite Markov matrix in its
code. Such a guard is meaningful on integers or \(\mathbb Z_3\), but
does not define a continuous residue condition on \(\mathbb Z_2\).
Its displayed normalization also lacks the factors one half: at tilt
zero, applying that formula to the constant one yields one or two,
rather than one. A product-space proposal must first define its state
space, reference measure, branch weights, and relation to actual integer
trajectories before a spectral conclusion can be transferred.

## DS4. What the finite Galerkin calculation really proves

The supplied code chooses each of the two lifts of the next residue
modulo \(2^{M-1}\) with probability one half. Under the bijection
between a residue modulo \(2^M\) and its first \(M\) parity bits, this
deletes the first bit and appends an independent fair bit. Therefore its
matrix satisfies exactly

\[
P_M^M=2^{-M}\mathbf 1\mathbf 1^\mathsf T.
\]

The stationary eigenvalue is one and every other eigenvalue is zero.
The apparent nonzero second eigenvalue in floating-point output is
numerical perturbation of a nilpotent part. It is not an exact spectral
value and is not evidence for contraction of actual integer mass.
This finite averaging issue was already proved in PR152,
`research/gemini-global-closure-20261120/AVERAGED_CHAIN_AUDIT.md`; it is
credited here as an existing boundary, not a new result.

The accompanying independent checker verifies finite controls for these
operator identities using exact integers and fractions. The proofs above,
not the checked finite ranges, establish their universal quantifiers.
