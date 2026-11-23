# Independent review: complete carry entropy and collision transport

Reviewer: global-construction lane. Date: 23 November 2026.

**Verdict: VERIFIED at the stated written-proof scope.** I independently
reconstructed the carry injection, stationary entropy budget, weighted
collision estimate, geometric squared-law change of measure, and both
geometric moment regimes. I found no missing arithmetic channel, reversal
assumption, moment hypothesis, or endpoint-limit error in the frozen note.
This verdict does not supply the still-missing original-source upper
collision exponent or certify Collatz.

## Frozen target

`research/closing-step-20261123/COLLISION_CLOSURE.md`

SHA-256:
`5a08dc30b5f7d4a7ff8d47c6797c46011ec1b3cb05a27cbcc88557b09a4ea927`

No source edits were made during this review. The verdict applies to
this exact file and its own statements. It does not constitute a new
full review of its inherited stationary-lift or peer-source premises.
No Lean execution or formalization of its infinite probability arguments
is claimed by this review.

## 1. Exact arithmetic and orientation

For a chronological word, I checked the finite affine relation and
reversed endpoint expansion directly:

\[
2^{-A}C
=\sum_{j=1}^{m}3^{j-1}
  2^{-(g_{m-j+1}+\cdots+g_m)}.
\]

Thus the window ending at time zero produces precisely the first
\(m\) terms of the stated past ternary factor. Extending farther into
the past changes this value by a multiple of \(3^m\). Translating the
chronological window to \((G_1,\ldots,G_m)\) uses stationarity only;
it does not require reversal invariance.

Given \(A,K,r\), the residue of the full carry is \(2^A r\) modulo
\(3^m\) and its quotient is \(K\), so the complete positive integer
carry is determined. For \(m>1\), subtracting \(3^{m-1}\) leaves
\(2^{g_1}\) times the odd suffix carry. Its exact binary valuation
therefore recovers \(g_1\). Repetition recovers the first \(m-1\)
gaps, and \(A\) recovers the last. At \(m=1\), \(A\) itself is the
gap. Consequently the chain-rule identity in (7) is exact, including
the full probability of repeated empirical words.

## 2. The Shannon loss uses the correct conditional drift

I reconstructed
\[
C/3^m=\tfrac13\sum_{i=0}^{m-1}e^{S_i}
\]
with the forward chronological increments
\(G_i\log2-\log3\). The term \(S_0=0\) makes the running maximum
nonnegative. The two inequalities in (10) follow from the largest
summand and the bound on the number of summands; the floor introduces
no sign or one-step error.

Birkhoff gives the conditional, rather than merely global, drift.
The maximum divided by \(m\) tends to its positive part. To check the
expectation limit, I independently used the truncation
\(G_i\le L+G_i\mathbf1_{G_i>L}\): above a threshold \(2L\), the
tail expectation of its sample average is at most
\(2\mathbb E[G_0\mathbf1_{G_0>L}]\). This proves uniform
integrability of the averages and their dominated running maxima.
No second moment or independence has entered that argument.

The maximum-entropy bound for the total gap is logarithmic in \(m\).
Cross entropy against the normalized law \((k+1)^{-t}\), for fixed
\(t>1\), bounds carry entropy by its finite logarithmic moment.
First taking \(m\to\infty\), then \(t\downarrow1\), gives exactly
the loss budget in (13). On an invariant restriction with conditional
mean at most \(\log_2 3\), this budget is zero. The note correctly
keeps a global mean bound separate from that stronger condition.

## 3. Weighted collisions retain cross-channel terms

For each endpoint residue, weighted Cauchy gives one reciprocal-penalty
sum and one penalized square sum. Injection ensures that a box occurs
at most once in the first sum. Bounding it by the full reciprocal sum
and then summing the second factors over residues proves (15).
Monotone finite-subset approximation gives the countable extension.

The resulting bound (17) is on the full endpoint collision energy.
It includes collisions between different total-gap and carry-quotient
boxes. It does not replace those terms by the sum of within-box
energies. The law proportional to \(P_m(w)^2\) is the necessary and
exact change of measure; no stationarity of this family is inferred.
The lower bound follows independently by dropping positive cross
terms when words are grouped into residues.

## 4. The geometric range below two

Squaring and normalizing the geometric law gives precisely
\[
Z_m=(2b-1)^{-m},\qquad
\beta=b^2/(2b-1).
\]
For \(1<b<2\), one has \(1<\beta<4/3\). I checked the moment
formula
\[
\mathbb E(2^G/3)^u
=\frac{(2/3)^u}{\beta-(\beta-1)2^u}.
\]
At \(u=1\) it is strictly below one, so continuity supplies the fixed
moment \(u>1\) used in the proof. Minkowski and independence bound the
entire normalized carry uniformly in that moment, including all gap
sizes.

The reciprocal total-gap penalty sums to \(O(\sqrt m)\) by an integral
comparison on both sides of the center. The normalized centered iid sum
has every fixed finite moment uniformly bounded: in an even-moment
expansion, every surviving index appears at least twice. Hölder then
controls its product with the carry penalty, without assuming these
two quantities independent. This proves both sides of (25) and the
exact exponent in (26).

At \(b=\log_2 3\), the chronological Shannon budget is zero and the
two displayed endpoint rates in (27) follow. The collision rate is the
smaller geometric exponent. This supplies no contradiction to the
previous lower bound, and the note states that limitation explicitly.

## 5. The endpoint at geometric mean two

Here \(\beta=4/3\), the first carry-product moment equals one, and the
expected normalized carry is \(m/3\). The proof does not reuse the
strict uniform-moment argument from the preceding section.

For \(u=1+1/m\), the logarithm of the moment multiplier has a bounded
derivative on \([1,3/2]\). Hence each of its first \(m\) product norms
is bounded by an absolute constant, yielding
\(\|K_m+1\|_u=O(m)\). I checked all moving Hölder exponents:
\(t=1+1/(2m)\), \(p=2m+2\), \(u/t\) is its conjugate, and
\(r=2p=4m+4\).

The tilted exponential moment is exactly
\(\mathbb E2^{A_m}=3^m\). Maximizing \(x^r2^{-x}\) gives the stated
bound and thus \(\|A_m+1\|_r=O(m)\), with a constant uniform in
\(m\). Hölder costs \(O(m^3)\); the moving zeta factor costs
\(O(m)\). The extra factor \(m^{1/(2m)}\) is bounded. This establishes
the \(Cm^4 3^{-m}\) upper bound with the lower bound from word grouping.
The finitely exceptional case \(m=1\) is harmless.

The final dimension-one assertions follow. Polynomial growth of the
finite-level \(L^2\) norms is not a bounded \(L^2\) density or a
pointwise theorem at an ordinary ternary fibre; the note does not make
either inference.

## 6. Retained closing boundary

The finite periodic-shadow height payment excludes arbitrarily long
tracking of one fixed template by one fixed source. It does not turn
a residue collision into a repeated word or a long consecutive period.
The note retains both restrictions.

For general actual word laws, the new weighted estimate leaves the
moment under the squared-word law to be bounded. The un-tilted
stationary first-moment calculation does not establish that bound.
The geometric mean-two model remains separate from an ordinary
escaping stationary limit whose mean is at most \(\log_2 3\).
These are explicit unresolved interfaces rather than hidden theorem
premises or an asserted solution.
