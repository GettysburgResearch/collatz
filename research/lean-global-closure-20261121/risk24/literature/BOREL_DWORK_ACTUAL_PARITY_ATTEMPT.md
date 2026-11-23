# Actual parity series against arithmetic rationality

Date: 2026-11-23. This is a new literature-driven closing attempt after the
frozen triadic certificate packet. The frozen files are unchanged.

**Status.** The actual ordinary source supplies an arithmetic formal germ
and an exact rational 2-adic specialization. I tested the Borel–Dwork and
Bost–Chambert-Loir rationality hypotheses directly on that germ. The
arithmetic condition holds. A positive capacitary degree, or a meromorphic
extension producing it, has not been established. No universal triadic
recovery or Collatz proof is claimed.

## 1. The specific primary theorem

Bost and Chambert-Loir, *Analytic curves in algebraic varieties over number
fields*, [arXiv:math/0702593v3](https://arxiv.org/pdf/math/0702593),
Theorem 7.9 and Example 7.10, pp. 47–48 of the PDF, give a rationality
criterion for an arithmetic formal function on a smooth projective curve.
One needs meromorphic continuation on an adelic collection of analytic
domains and **positive capacitary degree**. Their sufficient condition
2′ is a formal function over a model with finitely many primes inverted.
For discs on the projective line, positivity becomes a strict product of
local radii greater than one.

The disc case is Dwork's Theorem 3, *On the rationality of the zeta function
of an algebraic variety*, Amer. J. Math. 82 (1960), 631–648. The primary
paper was consulted through its published Russian translation by Manin,
Theorem 3 on p. 69:
[MathNet record and full text](https://www.mathnet.ru/eng/mat201).

The equality case in Bost–Chambert-Loir Theorem 7.8 is different: it
already assumes algebraicity and has an additional archimedean
complement condition. It does not supply algebraicity for an arbitrary
formal series whose known disc product is one.

This attempt does not replace the shaped-domain criterion by its disc
specialization. Failure to obtain a radius product greater than one is
not a theorem excluding every possible adelic tube.

## 2. One fixed positive ordinary source, not independent parity

Let

\[
x_k=T^k(n),\quad n>0,\quad e_k=x_k\bmod2,\quad
p_k=\sum_{i<k}e_i.
\]

Define two formal series with rational coefficients:

\[
B_n(z)=\sum_{k\ge0}\frac{e_k}{3^{p_{k+1}}}z^k,
\qquad
A_n(z)=\sum_{k\ge0}\frac{x_k}{3^{p_k}}z^k.                 \tag{1}
\]

Every coefficient belongs to \(\mathbb Z[1/3]\). The coefficients of
\(B_n\) are nonnegative in the real embedding. Both series have positive
convergence radius at every place: the elementary bounds
\(x_k\le2^kn\) and \(p_k\le k\) suffice. Their formal graphs therefore
satisfy the arithmetic model condition 2′ of the cited theorem, taking
the model over \(\mathbb Z[1/3]\).

The literal shortcut recurrence gives

\[
2\frac{x_{k+1}}{3^{p_{k+1}}}
=\frac{x_k}{3^{p_k}}+\frac{e_k}{3^{p_{k+1}}},
\]

and hence the exact formal identity

\[
\boxed{(2-z)A_n(z)=2n+zB_n(z).}                            \tag{2}
\]

Bernstein's inverse parity formula gives the exact 2-adic value

\[
\boxed{B_n(2)=-n\quad\text{in }\mathbb Q_2.}              \tag{3}
\]

This is the actual original integer, not a completion-point replacement.
The series converges at 2 in \(\mathbb Q_2\) since its nonzero
coefficients are 2-adic units and \(|2|_2<1\).
For the parity construction and inverse formula, see Monks–Yazinski,
[*The Autoconjugacy of the 3x+1 Function*](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
Section 1 and Theorem 2.1.

## 3. Exact directly available radii

Write

\[
\rho_- =\liminf_{k\to\infty}\frac{p_k}{k},\qquad
\rho_+ =\limsup_{k\to\infty}\frac{p_k}{k}.
\]

A positive ordinary trajectory has infinitely many odd inputs and
infinitely many even inputs. An eventually all-even positive trajectory
cannot remain integral under repeated halving, and an all-odd tail is
excluded by \(\nu_2(x+1)\).

The nonzero coefficients of \(B_n\) therefore give, by the root test,

\[
R_\infty(B_n)=3^{\rho_-},\qquad
R_3(B_n)=3^{-\rho_+},\qquad
R_q(B_n)=1\quad(q\ne3\text{ prime}).                     \tag{4}
\]

For completeness, restricting the density extrema to indices with
\(e_k=1\) does not change them: density decreases along each zero run,
and its value just before the next 1 differs from that next starting
index by a vanishing error. The maxima are likewise obtained at odd
indices up to a vanishing error.

The known disc product is consequently

\[
\boxed{\prod_v R_v(B_n)=3^{\rho_- -\rho_+}\le1.}           \tag{5}
\]

It equals one when the parity density exists. The actual rational value
(3) has not improved any of these radii. Rational rescaling of the
variable cannot improve their product, by the product formula.

These are exact **power-series convergence radii**. They are not asserted
to be maximal meromorphic continuation radii.

## 4. What the same source says at the real specialization

Assume now that this ordinary source escapes. The repository's elementary
orbit count proves convergence of the reciprocal sum on its distinct odd
orbit. Consequently

\[
\Lambda_k=\prod_{\substack{i<k\\e_i=1}}
\frac{3x_i}{3x_i+1}\ \downarrow\ \Lambda_\infty>0.
\]

The input is PR177 at
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`,
(HE2), (HE18)–(HE24a); its orbit-count proof was independently reconstructed
in the present packet's `RECURRENT_ARITHMETIC_NETWORK.md`, Section 8.

The exact multiplicative ledger is

\[
x_k=\frac{n3^{p_k}}{2^k\Lambda_k},\qquad
\frac{x_k}{3^{p_k}}=\frac{n}{2^k\Lambda_k}.                 \tag{6}
\]

Evaluating finite sums before taking any limit gives

\[
\sum_{i<k}\frac{e_i2^i}{3^{p_{i+1}}}
=\frac{2^kx_k}{3^{p_k}}-n
=n(\Lambda_k^{-1}-1).
\]

Therefore the very same rational-coefficient series converges at 2 in
both relevant completions, but to the different values

\[
\boxed{
B_n(2)=
\begin{cases}
-n,&\mathbb Q_2,\\
n(\Lambda_\infty^{-1}-1)>0,&\mathbb R.
\end{cases}}                                                \tag{7}
\]

There is no contradiction in (7). It is an exact consequence of a
hypothetical escaping ordinary trajectory, and its exclusion requires a
theorem connecting the two specializations with hypotheses beyond
convergence and rationality of one value.

Equation (6) gives \(R_\infty(A_n)=2\), and, for real \(z\uparrow2\),

\[
(2-z)A_n(z)\longrightarrow\frac{2n}{\Lambda_\infty}>0.       \tag{8}
\]

When \(B_n\) is analytic in a neighborhood of 2, this is a genuine simple
pole of \(A_n\). At the critical radius \(R_\infty(B_n)=2\), equation
(8) proves pole-type boundary growth only. It does not prove a
meromorphic continuation through the boundary point.

After the first odd step the integers \(x_k\) are units modulo 3, so

\[
R_3(A_n)=3^{-\rho_+},\qquad R_2(A_n)=1.
\]

The rational 2-adic zero of the numerator in (2) is removable on the
already available 2-adic disc. This does not extend that disc. In
particular the quotient still has radius exactly one at 2, since
infinitely many \(x_k\) are odd.

## 5. The attempted denominator cancellation

The ordinary \(1\leftrightarrow2\) cycle gives the weighted-series
denominator \(3-z^2\). I tested this actual candidate, rather than
assuming an arbitrary meromorphic extension.

Put \(C_n(z)=(3-z^2)B_n(z)\). For \(k\ge2\), write
\(u=e_{k-2},v=e_{k-1},w=e_k\). Its coefficient is exactly

\[
[z^k]C_n
=3^{-p_{k-1}}
\left(w3^{1-v-w}-u\right).                                \tag{9}
\]

The bracket in (9) vanishes precisely for

\[
(u,v,w)\in\{000,010,101\}.
\]

Otherwise it belongs to the fixed set \(\{-1,1,1/3,-2/3\}\).
Thus cancellation only deletes these three exact local configurations;
it gives no growing 3-adic divisibility on a remaining coefficient.

For an escaping ordinary orbit,
\(\rho_-\ge\log_3 2>1/2\), as also follows from (6) and
\(x_k\to\infty\). Both density extrema are attained along indices
where (9) is nonzero. Indeed, between two such indices the allowed
triples force an alternating or zero word, with at most one boundary
error. Such an interval contributes at most half as many 1's as its
length, plus a fixed constant. For maxima use the preceding nonzero
index, and for minima use the following one. Since the limiting lower
density exceeds one half, these comparisons preserve both extrema.

There must be infinitely many nonzero indices: otherwise the tail is
all zero or alternating. The former is impossible for a positive
ordinary trajectory, and an alternating positive integer trajectory
enters the \(1,2\) cycle.

Consequently the attempted cancellation leaves both relevant radii
unchanged on an escape:

\[
R_\infty(C_n)=3^{\rho_-},\qquad
R_3(C_n)=3^{-\rho_+}.                                      \tag{10}
\]

The target denominator did not create the strict arithmetic excess.
This calculation does not rule out a different denominator, a
nonpolynomial analytic factor, or a shaped-domain construction.

## 6. Why the isolated value does not provide the missing capacity

For the known discs, (3) places an algebraic point at \(z=2\), already
strictly inside the 2-adic unit disc. Removing its zero in (2), or
translating the 2-adic base point from 0 to 2, does not enlarge that
known disc. Translation by 2 preserves it.

The actual later ordinary values are not independent specializations at
new abscissae. They obey

\[
B_{x_k}(z)=3^{p_k}z^{-k}
\left(B_n(z)-\sum_{i<k}\frac{e_i}{3^{p_{i+1}}}z^i\right).   \tag{11}
\]

All identities \(B_{x_k}(2)=-x_k\) follow from the same original value
(3) by (11). They do not supply additional analytic continuation
domains or infinitely many distinct base points for an algebraization
criterion. Moving the common formal expansion to 2 would additionally
require arithmetic control of its derivatives there; only its constant
value is currently known to be rational.

A positive capacitary degree could still come from actual meromorphic
continuation on better domains, as allowed by the primary theorem. No
such continuation was constructed here. The precise missing input is
that continuation, with enough capacity, not the already verified
arithmetic formal-germ condition.

## 7. What rationality alone would and would not close

Even rationality of \(B_n\) would initially establish eventual
periodicity, leaving the classification of positive cycles. This can be
seen without importing a zero-set theorem for linear recurrences.

If its coefficients satisfy a fixed finite rational linear recurrence,
multiply a recurrence block by \(3^{p_k}\). Each normalized entry is
determined by the finite parity block, since

\[
3^{p_k}[z^{k+j}]B_n
=e_{k+j}3^{-\sum_{t=0}^j e_{k+t}}.
\]

The recurrence then determines its next bit uniquely: the two possible
normalized next entries are 0 and a specified nonzero power of \(1/3\).
A finite parity window therefore has a unique successor after the
recurrence begins, forcing an eventually periodic parity sequence.

Full triadic recovery would require more, for example that the core
denominator \(3-z^2\) actually leaves a polynomial. No such conclusion
has been obtained from the analytic criteria. The source remains fixed
throughout; no generic completion measure, independent parity model, or
unproved finite-state property has been substituted for it.
