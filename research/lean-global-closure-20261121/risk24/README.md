# Triadic certificates, primitive denominators, and actual-component flows

**23 November 2026. Collatz remains OPEN.** This continuation targets the
universal arithmetic witness, the complete cycle denominator, and the
same-source branching estimate. It builds on the newly advanced PR177 and
PR185, the existing PR178/180/182 work, and the literature map in PR186.
The full pull-request metadata refresh and exact source pins are in the
[report](../../../reports/lean-global-closure-20261121/nov23/risk24/README.md).

The main additions are a total Lean-checked verifier for signed triadic
complementary certificates and an all-word improvement from polynomial
to superpolynomial growth of the residual polynomial denominator.
The final integer-gcd exclusion and the universal certificate construction
are not proved.

A late refresh found concurrent triadic work in PR178 at
`4e204f54136c79cf8c9393b34e3330594f99ae0a`. Its
`research/global-closure-20261123/duality/TRIADIC_RANK.md` gives the same
triadic criterion and signed energy below, with a Mathlib formalization
of the all-time consumer. Our core/Std module additionally implements an
unconditionally total stopping clock and its finite-check consumer.
The overlap is credited explicitly; the earlier pins in the frozen notes
remain their actual read-time dependencies.

## 1. A complete rank for a full-convergence certificate

Let \(\Omega\) be the 2-adic parity-complement autoconjugacy of the shortcut
map. The [written criterion](TRIADIC_AUTOCONJUGACY_ATTACK.md) proves

\[
\boxed{\Omega(n)\in\mathbb Z[1/3]
\iff \exists k\ge0,\ T^k(n)=1\quad(n>0).}
\]

This specializes the literature's general rational-dual interface: a
denominator consisting only of powers of three also settles the cycle
outcome. No novelty claim is made for the equivalence itself.

The new [Lean core/Std file](TriadicDual.lean) implements a proposed dual
as a signed numerator \(a\) and a nonnegative exponent \(r\). Every
valid complementary step strictly decreases a lexicographic rank. While
\(r>0\), an ordinary even step lowers \(r\); an odd step lowers
\(v_2(x+1)\). At \(r=0\), the signed integer energy

\[
2x|a|+\mathbf1_{a=1}
\]

strictly decreases, with the zero numerator handled by the odd-run rank.
This gives a total executable stopping clock for every candidate: it either
reaches the actual value 1 or encounters a parity mismatch. Checking parity
only through that finite computed clock is sufficient for the formal
convergence theorem. Negative numerators are included.

The missing universal assertion is still
\(\Omega(\mathbb N_{>0})\subseteq\mathbb Z[1/3]\).
An explicit control at \(n=1\) shows why raw finite triadic approximations
cannot establish it: their exact denominators are \(3^r\), although their
2-adic limit is the integer 2. The file does not assume a universal witness,
and the construction of \(\Omega\) itself remains a written literature
interface rather than part of this Lean module.

## 2. Every primitive word pays a superpolynomial denominator

For a binary word of length \(A\), with \(p\) odd positions \(d_i\), set

\[
F(X)=X^p-2^A,\qquad Q(X)=\sum_{i<p}2^{d_i}X^{p-1-i},
\quad F_0=F/\gcd(F,Q),\quad n=\deg F_0.
\]

The [new degree proof](SUPERPOLYNOMIAL_RESIDUAL_DENOMINATOR.md) strengthens
PR185's full Fourier-clock argument by charging each maximal prime power
of the order lcm to its totient cost. A central-binomial estimate then gives,
for **every primitive parity word** with \(p\ge10\),

\[
\boxed{n>\frac{(\log p)^2}{72\log(2\log p)}.}
\]

This degree result uses elementary finite Fourier and prime-power arguments;
it has no positivity-cone hypothesis and no fixed word schema. In particular
\(n/\log p\to\infty\) uniformly over primitive words.

For positive words, PR185's separately qualified written factor-gap theorem
gives \(D_{\rm pol}:=|F_0(3)|>(3/2)^{n-1}\). Combining the results yields

\[
\boxed{\forall K>0\ \exists p_K\ \forall\text{ primitive positive words},
\quad p\ge p_K\Longrightarrow D_{\rm pol}>p^K.}
\]

The threshold is uniform in the word and its length \(A\). This is growth
after all common polynomial factors have been removed. It is **before**
the remaining integer evaluation gcd:

\[
q=\frac{D_{\rm pol}}{\gcd(D_{\rm pol},Q_0(3))}.
\]

An integer cycle would still have to cancel the whole \(D_{\rm pol}\).
The [companion closing attempt](DISTINGUISHED_GCD_CONTINUATION.md) tests whether the height gap makes a
moving-target gcd theorem applicable; it does not claim that the required
nondivisibility has been proved.

## 3. An ordinary-component recurrence theorem without population assumptions

The [network construction](RECURRENT_ARITHMETIC_NETWORK.md) starts with any
hypothetical actual escaping component. A countable mixture of binary
inverse-tree path laws gives an atomless law with positive mass at every
ordinary vertex. Its level mass is exactly one. The elementary actual-path
count gives a uniform reciprocal moment, so it supplies a positive critical
harmonic function \(G\) with

\[
G(n)/n\le C,\qquad \sum_nG(n)/n^2<\infty.
\]

This deliberately constructed function needs no predecessor-density or
canonical-envelope hypothesis. It is not identified with the canonical
function, and no uniform positive floor for \(G\) is asserted.

Mix the deterministic forward step and that actual inverse law with equal
probabilities. The resulting reversible chain is **null recurrent**.
The proof uses finite-mass level tents with Dirichlet energy \(1/M\),
followed by finite-support approximation; it handles infinitely many
inverse neighbors explicitly.

The bounded physical coordinate
\(Y(n)=\prod_{j\ge0}3U^jn/(3U^jn+1)\) has the exact drift

\[
SY(q)-Y(q)=\frac{r(q)}2
\left(\frac13-\mathbb E_{K(q,\cdot)}2^{-a}\right),
\qquad r(q)=Y(q)/q.
\]

Recurrence forces this drift to take both signs. The finite probability
proportional to \(G(q)r(q)^2\) gives its conditional inverse moment exact
mean \(1/3\). This accounts for the failed attempt to compare the strict
unweighted forward-gap surplus with a stationary finite measure.

The same construction makes pointwise inverse Rényi dissipation coexist
with a fixed positive mass on every reversed prefix of the actual moving
spine. Atomlessness, the displayed moments, and recurrence of the
auxiliary chain therefore do not by themselves exclude the original
deterministic escape.

## 4. The arithmetic price of sibling-cone transport

The [same-source transport calculation](SIBLING_CONE_TRANSPORT.md) tests
whether PR177's new atomic measures supply canonical branch comparability.
Their bounded distortion under the actual sibling involution does not
move an entire predecessor cone: it only swaps its root atom.

A genuine equal-depth transport has an exact ordinary cost. From the
sibling of the \(j\)-th actual forward state, choose any legal \(j\)-step
inverse path, with total gap \(A'_j\); let \(A_j\) be the actual prefix
total from the fixed source. The off-spine cones are disjoint, so their
chosen endpoints are distinct. Physical telescoping then forces

\[
\sum_{j=1}^{N}(A'_j-A_j)\ge\log_2(N!)-C_pN
=N\log_2N-O_p(N).
\]

This excludes uniformly bounded equal-depth gap repair along the whole
spine. It does not exclude unequal depths or the correctly weighted
transports sought elsewhere. The note also retains the direction of
relative entropy in the attempted digit comparison; no same-endpoint
collision upper bound is claimed.

[SiblingSourceSeparation.lean](SiblingSourceSeparation.lean) proves the
distinct-source core for every deterministic map with the stated exact
merger clocks. The factorial and probability estimates remain written proofs.

## 5. Evidence and boundaries

The two new Lean modules compiled under Lean 4.34.1. All **26 public theorem
declarations** and the executable stopping clock were audited; the only
axioms reported are propext and Quot.sound. No previous project modules
were rebuilt. The degree proof, infinite network analysis, and 2-adic
autoconjugacy interface are written mathematics, with their internal review
scope recorded separately. The inherited PR185 factor-gap certificate was
not rerun or relabeled as new evidence.

Reproduce only the new formal check with:

~~~bash
python -X utf8 -B research/lean-global-closure-20261121/risk24/verify_risk24.py \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --receipt /absolute/path/outside/checkout/risk24-checks.json
~~~

The [preceding checkpoint](../risk23/README.md), including the infinite
Hardy eigenspace theorem, is preserved. No result here proves that every
ordinary input has a triadic dual, that the full residual denominator fails
to divide its numerator, or that the actual same-source collision upper
bound holds.

## 6. What the late heads add to the closing attempt

PR178's new triadic note also gives a written bit-length horizon for a
candidate and converts the finite complementary checks into one exact
carry congruence. It still requires a source-dependent small triadic
residue; no universal construction of that residue is asserted.

PR180 at `fcdcdbadc6172e414f7282442a8a6b85587d7e70`,
`research/source-clock-20261123/BOUNDARY_OVERLAP.md` and `EXTENSIONS.md`,
strengthens dimension and information estimates for the actual canonical
real boundary. These retain the canonical positive floor and full-event
selection inputs. They do not automatically apply to the deliberately
constructed function in Section 3. The common-boundary entropy also does
not identify the actual integer endpoint or remove its integer-lift term.

PR182 at `b78819e95ee7d39f02022de991b42217821e7590`,
`research/closure-round2-20261123/CYCLE_CANCELLATION.md`, proves new exact
adjacent-swap gcd transport and reconstruction bounds for zero words.
It independently tests the moving-target gcd interface but leaves full
numerical cancellation open. Our new superpolynomial denominator is
compatible with those bounds; it is not an upper bound on the final gcd.

PR176 at `c82e3c1be894f655b40dcb61bf6d309a8f664e67`,
`research/lean-global-resolvent-20261121/overview/integer-boundary/TWO_PLACE_NUMEN_CLASSIFICATION.md`,
classifies when the real and 3-adic values of an actual inverse path agree.
An integer cycle is an allowed equality case, so the classification does
not supply the required exclusion of an additional positive cycle.
