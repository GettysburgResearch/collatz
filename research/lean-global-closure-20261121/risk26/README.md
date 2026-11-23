# Unconditional cycle boundaries and fixed-source arithmetic

23 November 2026. **Collatz remains OPEN.** This checkpoint attacks the
complete cycle denominator, the actual critical stationary branch, and
universal triadic construction. It contains six new finite Lean theorems,
written all-parameter deductions, and explicit countermodels to proposed
closing implications. It does not contain a proof of universal stopping
or exclusion of all nontrivial positive cycles.

The strongest positive deductions are an unconditional simultaneous
cycle-defect budget and an exact gcd restriction for every prefix of one
unchanged ordinary source. The strongest representation result is a
proof that the autoconjugacy's whole-sequence generating function cannot
be algebraic over Q_2(z). The failed closing attempts are retained at
the exact arithmetic step where their required gain disappears.

## 1. All positive cycles share one unconditional budget

The existing PR182 global count applies to any forward-invariant set
of positive odd integers on which the accelerated odd map U is injective.
It explicitly applies to the union of all positive odd periodic points.
Applying its reciprocal moment to that union gives

\[
 \sum_{\text{primitive positive cycles }c}\delta_c<\infty,
 \qquad
 \delta_c=A_c\log2-p_c\log3
 =\sum_{x\in c}\log\left(1+\frac1{3x}\right).
\]

More precisely, for one absolute constant C and
theta=H_2(log_3 2)<1,

\[
 \sum_{\min c\ge M}\delta_c
 \le\frac{C}{3(1-\theta)}
       \frac{M^{\theta-1}}{\sqrt{1+\log M}}.
\]

This removes the predecessor-density hypothesis P from PR180's grouped
Blaschke construction. With a_c=3^(p_c)/2^(A_c), the product

\[
 \mathcal B(w)=\prod_c\frac{a_c-w^{A_c}}{1-a_cw^{A_c}}
\]

is a bounded nonzero holomorphic function on the unit disk. Its tail,
after retaining all cycles with minimum below M, is uniformly at most
((1+r)/(1-r)) times the displayed defect tail on |w|<=r<1.
Combined with PR180's separately pinned simple-cycle-pole theorem,
it makes B(z/2)(I-zK)^(-1) holomorphic on |z|<2 for the actual operator.

The same count gives the finite real normalization of every hypothetical
escaping ordinary ray without a predecessor-density assumption. This
is an application of an existing count and its moment consequence;
no priority for that counting theorem is claimed. Pole cancellation
does not establish the absence of the cycles producing those poles.

**Proof:** [Unconditional cycle and escape boundary](root/UNCONDITIONAL_CYCLE_BOUNDARY.md).

## 2. Every prefix retains an exact original-source gcd

For the actual odd orbit q_0=p, q_1, ..., define its positive gap sum
A_N and complete carry C_N by

\[
 2^{A_N}q_N=3^Np+C_N,
 \qquad D_N=2^{A_N}-3^N.
\]

The new finite formalization proves

\[
 \boxed{\gcd(C_N,D_N)=\gcd(q_N-p,D_N).}
\]

When q_N differs from p, the full numerical gcd is therefore at most
|q_N-p|. The Lean proof derives the prefix affine identity by induction
from every original edge; it does not assume an unrelated carry or
change the source at each horizon. It permits arbitrary integer affine
data with coprime multipliers before specializing to powers of two and
three. The distinctness premise in the size bound is necessary.

Under escape and the finite reciprocal correction, the exact
normalization E_N=2^(A_N)q_N/3^N increases to E_infinity>p. Therefore
D_N/3^N tends to -1 and C_N/3^N tends to E_infinity-p. If the additional
critical clock A_N log2=N log3+o(N) holds, the reduced periodic shadow
z_N=C_N/D_N satisfies

\[
 \log\operatorname{den}(z_N)=N\log3+o(N),\qquad
 \log H(z_N)=N\log3+o(N),\qquad
 \frac{-\log|z_N-p|_2}{\log H(z_N)}\longrightarrow1.
\]

No logarithmic-form lower bound is needed for these conclusions.
Selected-horizon hypotheses give only selected-horizon conclusions.
The real limit of these same shadows is negative, p-E_infinity, while
their binary limit is p; these are different completions.

The canonical fixed-source Subspace forms have a local product exactly
q_N>=1. Even using alpha=E_infinity-p in the real form gives

\[
 \mathcal P_N
 =\frac{3^N}{2^{A_N}}(E_\infty-E_N)
 =\sum_{j\ge0}\frac{2^{A_{N+j}-A_N}}{3^{j+1}}
 \ge\frac13.
\]

Subtracting K future corrections still leaves an unrenormalized scalar
tail at least 2^K/3^(K+1). Sublinear K cannot supply a fixed negative
power of the shadow height. These are exact tests of the stated forms;
they do not exclude different forms, new encodings, or every use of the
Subspace Theorem.

**Proof and formalization:**
[Fixed-source prefix shadows](endpoint/FIXED_SOURCE_PREFIX_SHADOWS.md),
[FixedSourcePrefixGcd.lean](endpoint/FixedSourcePrefixGcd.lean).

## 3. The full cycle gcd needs the complete positive-gap law

The preceding checkpoint showed exponential separation between the
residual polynomial denominator and the largest cycle state. This pass
attacks the numerical cancellation directly.

For monic f,q of consecutive degrees, integral cancellation gives
(X-3)J=q+mf. Its leading coefficients obey

\[
 j_1-m(f_1+3)=1.
\]

Thus J is automatically primitive. Its primitivity is not a second
restriction after full integer cancellation has been assumed. The exact
Smith quotient is Z/f(3)Z, with invariant factors 1,...,1,|f(3)|;
changing basis retains the original evaluation condition.

An infinite family of positive integral polynomial models retains
monicity, primitive J, the known root annulus, local root integrality,
polynomially bounded leading coefficient, and exponential D/M growth,
while still having complete numerical cancellation. Its nonconstant
carry coefficients are powers of two, but begin with exponents
0,1,2,4,5,5. The zero gap and the uncontrolled terminal power are
explicitly retained. These are not Collatz cycles: they refute a
closing implication using only the listed polynomial facts.

Restoring the exact positive-gap law gives further exact statements:
all rotated prime-power valuation conditions are equivalent; the actual
Hankel determinant ratio is the original full residual denominator;
and the cross-carry of arbitrary complementary cycle cuts is the full
denominator times their state displacement. Adding complete laps scales
both sides by the same new denominator. None supplies the missing
strict inequality.

**Proofs:** [Integer numerator and full fiber](cycles/FULL_FIBER_INTEGER_NUMERATOR_ATTACK.md),
[Direct positive-gap attack](cycles/POSITIVE_GAP_FULL_FIBER.md).

## 4. The complete repetition budget has an exact critical scale

The maximum-Shannon branch identified in the latest source work is the
critical geometric iid gap law of mean ell=log_2 3. For a repeated gap
template w^k, PR178's ordinary-source inequality demands height at least

\[
 D(w,k)=\frac{2^{(k-1)A(w)+1}}{(3/2)^{|w|}}.
\]

For the maximum demand over starts before N, allowing all period lengths,
all positive gaps, all powers and overlaps, this packet proves the
almost-sure exponent

\[
 \boxed{\kappa_*=
 \frac1{\log_2(\log_2 3)}=1.5050070664\ldots.}
\]

A full geometric moment sum gives the upper bound; disjoint all-one
runs give the matching lower bound. Thus all those numerical demands
are simultaneously compatible with a polynomial envelope. This does
not make a selected ordinary generic ray a typical random sample, and
it does not construct an ordinary realization of that law.

The companion arithmetic analysis retains the actual larger-sieve
difference energy, including diagonal correction and all lags. It also
computes the complete three-coordinate S-adic product. Balanced positive
ordinary CRT segments realize the exact m/d saving, which becomes
subpower when collision depth m is small compared with the lag. These
are finite witnesses to the failure of a uniform inference, explicitly
not one infinite ordinary source.

**Proofs:** [Sharp repetition demand](endpoint/REPETITION_ENTROPY_BOUNDARY.md),
[Sieve and Subspace source products](endpoint/SIEVE_AND_SUBSPACE_SOURCE_PRODUCT.md).

## 5. Algebraic sequence constructions are excluded, while pointwise existence remains open

Write g(n)=Omega(n)+1 for the parity-complement autoconjugacy. Its
exact even section satisfies g(2n)=(2/3)g(n), with g(0)=0 and g(1)=3.
If G(z)=sum g(n)z^n were algebraic, its complete finite singularity set
would be permuted by squaring. In particular, opposite singularities
could not cancel in G(z)+G(-z)=(4/3)G(z^2).

Propagation of a first nonholomorphic Puiseux exponent through finitely
many branches then forces three to be a rational power of two. A
finite field-of-definition argument makes this complex contradiction
apply to hypothetical algebraicity over Q_2(z). The ordinary value
series and the Newton-coefficient series are consequently transcendental.
This written theorem has two independent reconstructions. It remains
compatible with every individual ordinary value being in Z[1/3].

The fixed-source continuation attempt also has an explicit control:

\[
 H(z)=(1-4z/9)^{-1/2}-1,
 \quad H(2)=2\text{ in }\mathbb R,
 \quad H(2)=-4\text{ in }\mathbb Q_2.
\]

It has positive triadic coefficients and is real analytic past two.
It is not an actual parity series. The actual single-generator
coefficient rule is stronger: Bell--Smertnig makes algebraicity or
D-finiteness imply rationality for that rule. What is missing is a
proof of that sufficient property for the actual source. The supplied
Taylor discs have adelic product at most one; the checked Bost--
Chambert-Loir and 2026 Bost--Charles criteria retain a strict capacity
or pseudoconcavity premise that these discs do not verify.

**Proofs:** [Algebraic section rigidity](triadic/ALGEBRAIC_SECTION_RIGIDITY.md),
[Fixed-source gluing](triadic/FIXED_SOURCE_GLUING_BOUNDARY.md).

## 6. Literature, verification and remaining obligations

The primary texts checked include Corvaja--Zannier and Grieve--Wang on
S-unit gcd estimates, Adamczewski--Bugeaud on repetition and p-adic
approximation, Flajolet--Sedgewick on algebraic branches, Bell--Smertnig
on restricted-coefficient series, and the arithmetic continuation
criteria above. Each scientific note records the actual substitutions
and the first unsupplied hypothesis. A variable number of carry
coordinates is not passed to a fixed-dimension theorem.

The six new Lean declarations were compiled with Lean 4.34.1, Std only,
warnings as errors, and a fresh object file. Their axiom dependencies
are subsets of {propext, Quot.sound}. The asymptotic, probability,
algebraic-function and operator claims remain written mathematics.

New exact controls cover three positive polynomial countermodels with
1,115 coefficient-ratio certificates, 172 positive ordinary CRT
collisions, 20 finite weighted tensor identities, and six same-source
sieve controls. They verify those finite identities and constructions;
they do not establish any infinite theorem. No older census or old
finite-control bundle was rerun.

The [reports and frozen source ledger](../../../reports/lean-global-closure-20261121/nov23/risk26/README.md)
separate written reviews, fresh executions, source comparisons, and the
final clean-checkout publication gate. A late PR177 update is compared
there at its full SHA; this checkpoint does not silently inherit later
claims.

The central obligations are still a strict full-denominator obstruction
using the entire positive-gap and terminal law; a new arithmetic saving
for one actual escaping source beyond the positive prefix corrections;
or a successful pointwise triadic construction. The new proofs make
those obligations more precise but do not discharge them.
