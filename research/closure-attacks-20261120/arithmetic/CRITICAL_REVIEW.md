# Independent review of the critical singularity derivations

**Reviewer:** arithmetic closure route, independently reconstructing the
analytic consequences. **Verdict: VERIFIED CONDITIONAL DERIVATIONS at the
frozen bytes below.** The named external/source inputs remain
SOURCE-QUALIFIED; this review does not promote them into the repository's
accepted baseline and does not prove Collatz.

## Frozen boundary

Reviewed file:
`research/closure-attacks-20261120/critical/CRITICAL_SINGULARITY.md`

SHA256:
`027e694d8c6223fe305073318043caba28b0eb00a314926620d6475db40233fa`.

This review covers CS-001--003 and the elementary full five-ray comparison
in that file. It does not extend to later revisions or to neighboring
single-slice propagation claims. The following exact source bodies were
also read for their stated interfaces:

- PR155 `92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
  `research/gemini-dirichlet-global-20261120/ENDPOINT_BOUNDARY.md`, E1--E3.
- PR146 `6863d298187af8b2619efbf78cc4b0aa8e627393`,
  `research/upper-bit-mergers/DIRECTED_TRIPLING.md`, the bounded return
  path and finite affine source-list interface.
- Lech Mazur's primary
  [ProofAtlas predecessor-density record](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/),
  inspected on 20 November 2026, for the exact PD statement and its
  ordinary unaccelerated-map convention. Its supplied Lean development
  was not rebuilt in this review. The site's verification assertions are
  source claims, not a local execution receipt.

The UP estimate remains the separately named source input from PR146,
`THREE_RAY_UPPER.md`, at the same head. The conditional derivations below
use precisely its unconditional ordinary failure count, without assuming
independence after conditioning on a putative component.

## 1. Component mass and map compatibility

The reduction from PD to positive lower natural density of every nonempty
ordinary invariant set is correct. Such a set contains a positive ternary
unit after ordinary forward steps. Every predecessor of that fixed unit
retains its invariant label. Although the PD record uses the unaccelerated
map, shortcut invariance also identifies an odd \(n\) with \(3n+1\):
both have shortcut successor \((3n+1)/2\). The final note now explicitly
states this convention bridge.

For a nonempty proper invariant set, both it and its complement therefore
have a positive lower-density constant, with constants permitted to
depend on the respective fixed targets. Nonnegative partial summation
then gives a lower bound of order \((s-1)^{-1}\) for each Dirichlet
mass, while the zeta-function comparison gives the matching upper order.
No uniform lower-density constant, natural-density limit, or residue of
the Dirichlet series is inferred.

## 2. CS-001: boundary size, divergence, and abscissa

An actual merger of \(n\) and \(3n\) preserves every invariant label.
Thus the separating boundary is contained in UP's ordinary failure set.
Partial summation against its count bound gives

\[
 B_K(1+\epsilon)
 \le C(1+\epsilon)\int_0^\infty e^{-\epsilon t}t^{-1/2}\,dt
 =C(1+\epsilon)\sqrt\pi\,\epsilon^{-1/2}.
\]

The singularity at \(t=0\) is integrable, so replacing
\(\log(2x)\) by \(\log x\) is a valid upper estimate. This calculation
uses the full source count and never resamples or conditions a pair
process on \(K\).

If the boundary's harmonic series were finite, EP would give a binary
constant dyadic-profile limit. Summing the dyadic shell bounds implies
that either \(K\) or its complement has natural density zero. Both sets
are nonempty and have positive lower density under PD, a contradiction.
Therefore \(B_K(1)=\infty\). Monotone convergence as
\(\epsilon\downarrow0\) proves divergence from the convergent side.

For each nonnegative series, convergence for all \(s>1\) together with
divergence at one establishes abscissa exactly one. The two-sided
component-mass order and the boundary upper bound give the stated
\(O_K(\sqrt\epsilon)\) normalized boundary. The truncated harmonic
upper bound \(O(\sqrt{\log(2X)})\) follows from the same partial
summation. Nothing in the argument supplies a positive lower divergence
rate, and the note correctly refrains from claiming one.

## 3. CS-002: the precise loss under normalization

The probability measure is supported on genuine ordinary integers.
For a fixed finite interval its unnormalized numerator stays bounded,
whereas its denominator is of order \(\epsilon^{-1}\); its mass
therefore tends to zero. Its numerator on the boundary is at most
\(B_K(1+\epsilon)\), giving the second vanishing limit.

These are properties of the specified critical measures. They do not
show that the unnormalized boundary is empty or that a proper invariant
set exists. The note correctly treats a hypothetical endpoint coercive
inequality as a sufficient unresolved closing statement, rather than
claiming to refute such an inequality using a counterexample not known
to exist.

## 4. CS-003: metric and oriented energy statements

The metric extension is valid without completeness, boundedness or
separability of the metric target. If two labels have distance \(L>0\),
the real function
\(h(n)=\min\{d(f(n),f(a)),L\}\) is bounded, invariant, and 1-Lipschitz
as a function of the original label. It inherits finite harmonic
tripling energy and hence EP's scalar profile limit. The two chosen
ordinary components carry values zero and \(L\), respectively; at least
one stays at distance at least \(L/2\) from the putative limiting
constant. Positive lower density gives the contradiction. No
metric-valued \(L^1\) limit is required.

For bounded labels, the pointwise defect is bounded by the diameter times
the ordinary tripling-failure indicator. This gives the same convergent-
side upper bound and, for nonconstant labels, the exact critical abscissa.

For the separately directed real energies, the additional directed-return
input is used in the correct orientation. Along a path from \(3x\) to
\(x\), ordinary changes vanish and positive total decrease is bounded
by the sum of the negative parts of the queried forward-tripling changes.
Every query comes from a fixed finite list of injective rational affine
functions, with heights comparable to \(x\). Consequently each queried
odd source has bounded multiplicity and comparable harmonic weight.
This gives \(E_+(1)\le C E_-(1)\); replacing the label by its negative
gives the reverse inequality. Extended nonnegative sums are legitimate.
Exact doubling contributes only a finite geometric factor at exponent
one. Thus the total critical divergence forces both oriented divergences.
The full directed path source theorem is retained as an explicit input;
this review is not acceptance by association of neighboring PR146 claims.

## 5. Full five-ray comparison

The identities \(T^2(20x+1)=15x+1\) and \(f(4x)=f(x)\) give the
displayed two-query triangle inequality. On odd \(x\), the query sets
\(3x\) and \(4x\) are disjoint. Their respective weight conversions
are \(3^s\) and \(4^s\), bounded by the advertised common \(4^s\).
This proves the full five-ray harmonic consequence under the already
named critical-rigidity inputs. It does not imply the single-slice
finite-energy theorem, which is still explicitly open.

## Corrections and evidence boundary

The reviewed revision incorporates two requested source clarifications:
the primary record's author is **Lech** Mazur, and its unaccelerated map
is explicitly reconciled with shortcut invariance. These changes affect
attribution and the visible convention bridge; the conditional estimates
above required no mathematical repair.

This review reconstructed the proofs and inspected exact named source
interfaces. It did not execute a Lean build, infer an analytic theorem
from numerical evidence, verify all external dependency stacks, or prove
a summable ordinary separating-boundary estimate. The remaining closure
gap is preserved: the upper bound has precisely a nonintegrable harmonic
scale, and no theorem supplies the finite critical energy that would
contradict a second component.
