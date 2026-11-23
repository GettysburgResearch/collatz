# Independent review: all-exponent finite-profile obstruction

Date: 2026-11-22. Reviewer: global_analytic22.

**Verdict: VERIFIED as a written deduction with the stated published
arithmetic-progression input.** The conclusion is an obstruction to
nonzero fixed finite-period asymptotic profiles of excessive functions.
It is not a Collatz convergence proof and is not fully Lean formalized.

## Frozen review target and inputs

* ADDENDUM_ALL_EXPONENTS.md, SHA-256
  **856b86ce24a4bcd345d83bf5dce267690a21bd9adcbc09d1a2cbe1bce22d2ad3**.
* Its sublinear input FIXED_RESOLUTION_ENVELOPE_OBSTRUCTION.md, SHA-256
  **898337c461d9a9c23ac38e99a98800a02a500d51d3660bbdbac8b73fb90509e3**,
  is retained unchanged. This reviewer authored that earlier packet; the
  independent review here concerns the new p≥1 extension.
* The positive finite lift was compared with EndpointSteering.lean,
  SHA-256
  **b4f87c7b9eb38cd015f31a9f7ae60b0eaef6aeba77d496c5d586090e2da65416**,
  at PR175 **2bc2ad37b490a5aea63658eaf657bc048da4532e**,
  specifically orbit_shift and odds_shift.
* Monks, *The Sufficiency of Arithmetic Progressions for the 3x+1
  Conjecture*, Proceedings of the AMS 134 (2006), 2861–2872,
  Theorem 1.1, was read in the primary author text:
  <https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf>.

This is a semantic and mathematical review. No new Lean execution was
performed in this review.

## 1. Published input and its exact consequence

The positive arithmetic-progression theorem says that every positive
arithmetic progression meets every ordinary merger component. Applying
it to the component of one supplies a finite hit of one, since that
component's known terminal shortcut cycle is {1,2}. It does not assert
that every member of the progression converges.

The proof selects odd progressions by using step 2M. For the critical
case, the progression starts at 1+2M, so the chosen source is strictly
greater than one. This exclusion is essential and is present.

The new p≥1 proof uses only the positive version of Monks's theorem.
Its logic does not depend on the negative extension used for p<1, the
uniform predecessor-density input, or the canonical-envelope results.

## 2. Exact physical lift and propagation of a zero

For a fixed actual odd source z with a gap word of odd depth ell,
shortcut clock B, and endpoint one, the lifted source
\[
x_t=z+2^{B+1}Mt
\]
is an ordinary binary translation by a multiple of 2^B. The entire
finite parity prefix is preserved; its endpoint is
\[
q_t=1+2M3^\ell t.
\]
The original and lifted sources and endpoints are odd. Preservation of
the prefix therefore gives the exact accelerated gap word, not only a
terminal affine equality.

This follows directly from the published ordinary shift identities,
or by their parity induction. All intermediate states are positive.
Both clocks and the word are fixed before t tends to infinity.

Nonnegative excessivity implies \(P^\ell F\le F\) by induction.
Its single retained physical word has coefficient \(3^\ell/2^B\).
The source-to-target slope is \(2^B/3^\ell\), so normalization by
\(q_t^pL(q_t)\) gives exactly
\[
a(1)\ge(3^\ell/2^B)^{1-p}a(z).
\]
The coefficient is positive for every real p. Thus a zero at residue
one propagates to every odd-bearing residue through the particular
finite basin witnesses supplied by Monks. No infinite parent-series
limit or uniform depth estimate is needed.

## 3. The p>1 self-return

The targets \(q_t=1+6Mt\) and parents \(x_t=1+8Mt\) satisfy
\(3x_t+1=4q_t\), with exact gap two. Both lie in residue one.
The normalized coefficient is
\[
(3/4)(4/3)^p=(3/4)^{1-p}>1.
\]
Consequently excessivity forces \(a(1)=0\). The coefficient's sign
and the threshold p>1 are correct.

## 4. The p=1 two-history argument

The source \(z>1\) in residue one has an actual complete word W of
length ell≥1. It cannot equal the all-two word E of the same length:
backtracing E from one gives one at every letter, so its unique source
is one.

Both W and E lift to the same \(q_t=1+2M3^\ell t\). Their sources
\[
x_t=z+2^{B+1}Mt,\qquad
y_t=1+2^{2\ell+1}Mt
\]
are positive odd integers in residue one. Their shortcut clocks B and
2ell can differ, but their accelerated odd depth is the same ell.
They are therefore two terms in the same iterate \(P^\ell\).

The distinctness argument is valid. Were the lifted sources equal,
the deterministic accelerated map would assign the same first ell
exact gaps to that one ordinary source. That would force W=E. The
argument consequently does not double-count one ancestor, invoke
independence, or compare different-depth parent sums.

At p=1 each weight times its source-to-target slope is one. The two
retained terms give
\[
a(1)\ge2a(1).
\]
Together with nonnegativity this proves a(1)=0, after which Section 2's
propagation applies. This closes the critical exponent within the
profile architecture.

## 5. Exact scope

The all-real-exponent conclusion is valid under the displayed limits.
The profile can still be identically zero, even if the function has the
corresponding upper bound. An excessive function can also lack a
finite-period leading profile. The result does not prove that the
canonical envelope has the assumed regularity, nor that its moving
ordinary trace is sublinear.

No semantic correction is required. The addendum accurately separates
the published AP input, exact finite ordinary arithmetic, and written
asymptotic step from the available Lean finite cores.
