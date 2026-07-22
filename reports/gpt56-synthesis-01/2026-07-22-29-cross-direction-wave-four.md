# Cross-direction lemma forge: wave four

Date: 2026-07-22  
Authoring lane: `gpt56-synthesis-01`  
Status: theorem-level claims remain `PROPOSED` pending external repository review

## Scope

This wave attacked one live obstruction in each of five independent parts of
the project:

1. ordinary cyclic order inside survivor translation fibers;
2. actual power-of-two Padé residuals;
3. unbounded-width roots in the automatic-component kernel;
4. ordinary realization of the closed `{30,60,70}` raw H return; and
5. the physical interface between the collision bulk compiler and its
   residual padding tail.

The resulting claims are `L-9847`--`L-9852`. They are deliberately local:
each result states the exact boundary at which the next argument must begin,
and none is promoted to a global Collatz conclusion.

## Executive summary

- `L-9847` turns every multiplicity class of a signed survivor difference
  into a literal common-translation fiber. A successor representative must be
  isolated from every other translate on both sides, and repeated equal arcs
  satisfy an exact circle-packing bound.
- `L-9848` converts actual dyadic Padé residual zeros into one
  characteristic-two augmentation-slack problem. It proves an exact doubling
  convolution, counts every already-forced collapsed factor, and unconditionally
  excludes target zeros for the first two nonzero remainders `s=4,8`. The
  attractive all-layer order formula remains explicitly conjectural.
- `L-9849` proves a finite-core dichotomy for automatic component colorings.
  Every horizontal root cycle is wholly absorbed or wholly outside the core;
  outside it, the staying word makes width intrinsic. Full ternary-kernel
  finiteness is exactly eventual absorption of all widths.
- `L-9850` closes the exact raw `{30,60,70}` H architecture negatively. Its
  2-adic decoder forces distinct macro endpoints, while real drift and
  triangular phase equidistribution demand more small positive endpoints than
  the ordinary integers can contain.
- `L-9851` abstracts that contradiction: normalized growth over a compact
  uniquely ergodic base, together with endpoint multiplicity at most `M`,
  forces the sharp necessary inequality

  \[
  \frac1m\int_X R^{-1}\,d\nu\le M.
  \]

- `L-9852` identifies the first missing physical state in the collision
  compiler. The next padding bit is the bulk quotient bit XOR one residual
  quotient bit; two compatible zipper lifts force opposite answers, so a
  bulk-only rule cannot be physical on the whole cylinder.

## Survivor order: exact translation isolation

For a signed survivor word `eta`, every zero coordinate is a common bit of
the realizing endpoint pair. `L-9847` proves that changing those bits gives
all representations and only those representations:

\[
(a_c,b_c)=(a_0+h_\eta(c),b_0+h_\eta(c))\pmod {64^n}.
\]

The map `c -> h_eta(c)` is injective, so the known multiplicity `2^z` is an
actual `2^z`-point translation set. If one representation is a cyclic
successor arc of length `g`, every nonzero relative translation `delta` must
satisfy

\[
g\le\delta\le64^n-g.
\]

The two forbidden open intervals are both essential: translating the lower
endpoint forward or the upper endpoint backward can put a survivor point
inside the proposed arc. If the same signed word occurs on `s_n(eta)` actual
successor arcs, disjoint arc interiors give

\[
s_n(\eta)g(\eta)\le64^n.
\]

This is the first exact bridge from a settled common carry block to ordinary
cyclic isolation. It does not control the largest pointed gap of the special
translation set and therefore does not yet bound the minimum's successor.

## Padé: augmentation descent and two unconditional layers

For `s=4t`, `L-9848` rewrites the reduced mod-two residual as

\[
F_{n,c}(q)
=\sum_{E\subseteq\{0,\ldots,n-1\}}
q^{c|E|+\sum_{i\in E}i-4\binom{|E|}{2}}
\]

and proves the exact doubling convolution

\[
F_{2n,c}(q)
=\sum_{j=0}^n
q^{cj-3\binom j2}{n\brack j}_q
F_{n,c+n-4j}(q).
\]

All forced lower dyadic factors, after collapsing modulo two, consume exactly

\[
A(4t)=t+2\sum_{m=1}^t2^{\nu_2(m)}
\]

augmentation degrees in addition to the diagonal order `s/2`. Hence a new
target `L=2^k>s` can divide only if the remaining augmentation slack is at
least `L/2`.

Complete group-ring identities prove uniformly in the odd chart parameter

\[
\lambda_4=6,
\qquad
\lambda_8=14.
\]

Their slacks are respectively `1` and `2`, below every eligible target cost,
so all dyadic targets are nonexceptional in these first two actual remainder
layers. The formula

\[
\lambda_{4t}=4t+2\sum_{m\le t}2^{\nu_2(m)}
\]

fits the exact data and would exclude every actual dyadic target, but it is an
open algebraic target. No full Padé gcd bound is inferred from it.

## Automatic components: width is intrinsic outside one finite core

`L-9849` enlarges the finite binary kernel by the finite family of central
ternary-dilate states and calls the result `F`. This core is closed under both
binary sections. Every positive-valuation horizontal cycle has one staying
child and one escape child at each state, with every escape already in `F`.

It follows that a horizontal cycle is either entirely in `F` or entirely
outside it. In the second case, the staying bit is the unique binary section
that remains outside `F`, so the root sequence itself reconstructs its entire
periodic staying tail. Exact least period `2*3^(k-1)` then makes the width `k`
an intrinsic equality invariant.

The resulting equality classification shows that unabsorbed cycles at
different widths are disjoint and that each width-`k` cycle contributes its
full `2*3^(k-1)` states. Conversely, at any one fixed width the central-depth
parameter ranges through only a finite family. Therefore

\[
|\mathcal K_3(s)|<\infty
\quad\Longleftrightarrow\quad
\text{all sufficiently large widths are absorbed into }\mathcal F.
\]

Combined with Cobham and the earlier component rigidity, a nonconstant
2-automatic coloring would have to create new unabsorbed cycles at infinitely
many widths. The theorem does not decide whether absorption occurs.

## H: the raw-return graph has no ordinary point

The raw `{30,60,70}` return had survived all earlier local tests: it closes
the multiplier phase, violates the finite zero-descent no-go, has positive
real normalized-fiber drift, and selects a unique inverse-compatible 2-adic
endpoint graph.

`L-9850` combines those ingredients. If one graph point were ordinary, graph
invariance would propagate an integral macro orbit. Equality of two macro
endpoints would feed back through the modulo-`2^32` branch decoder, force an
eventually periodic branch tail, and contradict the irrational Sturmian
frequency. The endpoints would therefore be distinct.

The exact normalized growth and triangular phase distribution imply that,
for every sufficiently small fixed `y>0`,

\[
\frac1T\#\{n\le T:N_n\le yT\}
\longrightarrow
\frac{16}{7(1+\mu_3^{-1})},y.
\]

The coefficient is strictly larger than one because
`3^10=59049>57344=7*2^13`. Distinct positive integers can occupy at most
`yT+O(1)` places below `yT`, a contradiction. Thus the invariant graph has no
ordinary signed integer point. This excludes the exact raw architecture, not
all H returns.

`L-9851` separates the mechanism from those constants. If
`N_n/(nR(P^nx_0))->m` over a compact uniquely ergodic base and every positive
endpoint has multiplicity at most `M`, triangular product equidistribution
gives the exact small-value density

\[
\frac ym\int_XR^{-1}\,d\nu.
\]

Integer capacity then forces `m^(-1) integral R^(-1)dnu<=M`. This is a
screening theorem for future architectures, not a construction when the
inequality happens to hold.

## Collision/padding: the first residual-aware interface bit

Let the bulk compiler choose a padding address with
`Omega(a)=-V modulo 2^H`, while `h` is the actual outgoing physical tail.
`L-9852` proves that the address routes the physical prefix exactly when

\[
h\equiv V\pmod {2^H}.
\]

On that compatibility cylinder, the physical next bit is

\[
\varepsilon_h
=\varepsilon_V\mathbin{\mathrm{XOR}}
\operatorname{qbit}_H(h-V).
\]

The same identity is recovered from ordinary chart numerators after exact
division; no completed 2-adic address is invoked. For an odd-affine zipper
tail `h=psi+Ny`, compatibility chooses one residue cylinder in `y`. Its two
lifts differing by `2^H` have the same lower physical prefix and opposite
next bits. This both refutes a bulk-only next-bit rule and proves that one
residual quotient bit is sufficient for this single interface.

The remaining `K-H` connector block is not compiled. Later address bits must
be recomputed after a correction and are not asserted to be raw digits of the
initial residual defect.

## Explicit non-results

- No nontrivial infinite ordinary Collatz orbit, divergent seed, cycle,
  sanctuary, or `K-####` candidate is claimed.
- Translation-fiber multiplicity does not by itself control a pointed largest
  gap or certify successor adjacency against points outside that fiber.
- The Padé all-layer augmentation order is conjectural, and the result does
  not bound odd-prime composite or noncyclotomic specialization gcd sectors.
- Eventual absorption of automatic horizontal roots is not proved. Finite
  local compilation is compatible with infinitely many genuinely new widths.
- The H contradiction applies only to the exact raw return graph. Passing the
  abstract packing inequality is necessary, not sufficient, for a replacement
  architecture.
- One corrected collision/padding bit is not the full residual grammar and
  does not force the physical tail into the compatibility cylinder.

## Internal audit record

- Every translation representation, both forbidden intervals, and the equal-
  arc packing estimate in `L-9847` were independently reconstructed.
- The Padé subset exponent, q-Vandermonde shear, lower-factor degree, and
  target-slack implication were independently re-derived. Complete support
  recurrences checked all parameter residues in the `s=4,8` group rings.
- The automatic core closure, absorbed/disjoint dichotomy, intrinsic staying
  word, least-period width rigidity, padded-input equality proof, and full
  ternary-state exhaustion were independently checked.
- The H signed-integrality propagation, decoder distinctness, triangular
  indicator limit, exact coefficient, and integer capacity contradiction were
  independently checked. The abstract multiplicity-`M` theorem received a
  separate proof audit.
- The collision compatibility congruence, XOR sign, ordinary numerator
  division, odd-affine two-lift obstruction, and multi-bit scope were
  independently checked.
- Claim files were checked for required audit sections, balanced display
  delimiters, unique equation tags, and control characters.

## Highest-leverage next actions

1. Couple the survivor translation set to the actual pointed
   minimum/successor selector; multiplicity alone is now known to be
   insufficient.
2. Extract a unit-preserving binary transition from the exact Padé doubling
   convolution. Even a proof of the next two actual layers would test the
   all-layer order formula sharply.
3. Build finite ordinary test inputs that separate an automatic horizontal
   root from the fixed core; this would make absorption a finite word
   condition at each width.
4. Screen new H return architectures first by the abstract packing
   inequality, then derive their smallest arithmetic endpoint multiplicity.
5. Adjoin the residual quotient parity to the collision zipper state and
   derive its update through one complete scale transition.

## Files added in wave four

- `research/cross-direction-lemmas/claims/L-9847-successor-translation-isolation.md`
- `research/cross-direction-lemmas/claims/L-9848-pade-dyadic-augmentation-descent.md`
- `research/cross-direction-lemmas/claims/L-9849-finite-core-width-rigidity.md`
- `research/cross-direction-lemmas/claims/L-9850-ordinary-raw-return-packing-obstruction.md`
- `research/cross-direction-lemmas/claims/L-9851-unique-ergodic-integer-packing.md`
- `research/cross-direction-lemmas/claims/L-9852-residual-bulk-padding-xor.md`
- this report

The packet `research/cross-direction-lemmas/README.md`, `CLAIMS.md`, and
`VERIFICATION.md` index the theorem statements and preserve their dependency
and counterexample boundaries.
