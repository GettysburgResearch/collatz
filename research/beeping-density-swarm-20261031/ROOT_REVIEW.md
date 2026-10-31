# Root reconstruction of the second swarm pass

**Status: internal mathematical review of the named claims below; no external
peer review, proof-assistant certification, or Collatz solution is claimed.**
The source baseline is PR142 at
`d0f48c472d45a336e9083b37b45e1a8d39a2cf16`. Final relocated file identities
are recorded in the adjacent report's source manifest. This review does not
extend to later revisions, neighboring historical statements, or external
claims beyond the portions explicitly reconstructed.

## Contact geometry: CT-001--005

**Verdict: VERIFIED WITH FIXES, within the stated exploratory scope.**
The reviewer independently reconstructed the following steps, in addition
to the separate inverse-track review:

* The power-of-three spike forces the first contact on the pure doubling
  ancestry to occur at depths tending to infinity. Bellman growth along
  the resulting noncontact segment gives unbounded contact-return rank
  amplification. Every intermediate state escapes a prescribed finite
  core, by properness and the envelope's quadratic upper bound. This is
  stronger than merely sending the two endpoints outside the core.
* For `243*4^k+115` and its odd successor, the template parity lengths are
  respectively 2k and 2k-1. Their perturbations have 3-adic valuations five
  and six, exceeding the templates' displacement valuations three and four.
  Hence all template displacement valuations remain exact over those lengths.
  The winning candidates are the claimed squares divided by three.
* The short-prefix gap, eventual 1--2 template tail, and the exact common
  state `3^(k+4)+2` cover the complete growing Gamma cutoff. The post-template
  gap is at most seven for the first source and nine for its successor; the
  latter's extra factor 3/2 in its height denominator makes the common bound
  valid. At k=12 that bound is already below one half and decreases thereafter.
* The first six explicit Gamma majorants and the geometric envelope tail
  prove that both sources are contacts. Integral Gamma values handle the
  ceilings. The one-edge obstruction then has the correct a<2s versus
  a>=2s split, with no inference to arbitrary residue corrections.
* The inverse search for the occupation extension terminates because the
  rank divides by three, up to ceiling, at each noncontact predecessor.
  Determinism and strict noncontact rank growth prevent duplicate source
  visits. A doubling ancestor proves positivity; finite backward induction
  proves uniqueness. Arc telescoping gives the pointwise residual, and
  nonnegative Tonelli gives the exact clock-mass identity.
* The return clock yields `theta=log2/log(4/3)`. Extra height moments pay
  for actual endpoint movement, with the explicit source-domain loss stated
  in CT-005. Pairing the lift with the cumulative inverse bound requires a
  second height moment and therefore the stronger s threshold. It is a
  depth-average result, not a prescribed-depth or termination result.

Two final wording repairs were requested and incorporated: the return cannot
silently be absorbed at one before reaching its claimed contact endpoint,
and the computability assertion for the lift requires a **computable** real
exponent s. No code change was needed for these qualifications.

## Harmonic spectrum and effective evaluation: HS-001--004

**Verdict: VERIFIED WITH FIXES, on the specified harmonic Banach space.**
In normalized coordinates `e_x=x*1_x`, L maps e_x to c(x)e_Ux with
`c(x)=3x/(3x+1)`. This proves strict norm loss for each nonzero vector;
it does not give uniform loss over the unit sphere. The ordinary all-one
valuation segments prove the norm of every positive power remains one.

For an interior spectral parameter, the coefficients on an inverse ray are
`lambda^j/C_j`, where C_j includes the outgoing c factor at the ray's first
node. Multiplying the next coefficient by its outgoing factor gives exactly
lambda times the preceding coefficient. Pairing two rays cancels their
flux at one; if one is killed, each flux is separately discarded. Positive
lower bounds on C_j give absolute summability. Distinct rays give infinitely
many independent eigenvectors. Infinite kernel and closedness of the
non-Fredholm set prove the essential-spectrum assertion, including the
circle. There is no invalid claim that compact operators send the ell^1
basis to zero.

The reciprocal estimate T-A3-651 was reconstructed with the low-valuation
cylinder count, distinct high-valuation endpoints, and explicit tail
integration. It applies to simple orbit segments, not to an entire basin or
repeated cycle with multiplicity. Its use in the survival product is valid
on an injective escaping orbit. Dominated convergence gives the residual
mass formula. This establishes equivalence with universal eventual
periodicity, while leaving cycle exclusion separate.

For the computability equivalence, the unseen-first-hit lower bound is
uniform in its clock. At rejection stage N, the queried source is explicitly
simulated through the same N used in the partial sum, with any detected hit
accepted first. That synchronization was clarified during review. Otherwise
a source whose hit was already included in the partial sum could be
incorrectly treated as unseen. The converse uses a reachability decider to
resolve periodic renewal and a computable source-height tail, rather than an
unjustified stopping-time cutoff. No noncomputability conclusion follows.

## Inverse Green bounds: IFT-001--006

**Verdict: VERIFIED for the elementary upper bounds; SOURCE-QUALIFIED for
the positive lower bound that invokes the external fast-density theorem.**
The harmonic identity is sourcewise and survives actual transport. Its
input domain excludes the constant function one. First-hit paths have unique
sources across depths; a periodic target requires precisely the geometric
renewal factor. The common cutoff over all depths gives the claimed integral
`t(1+Q log96)` and geometric tail. An exact first-hit-at-zero source also
attains the stated Green evaluation norm.

Prefix-free concatenation is injective in full inverse histories, not just
endpoints. This validates the transported depth average even for countably
many words; the retained counterexample shows why the prefix-free guard
cannot be dropped. Finite-tree induction and monotone convergence validate
the arbitrary-depth budget for the source-penalized Green potential. That
potential is finite pointwise but is not asserted effectively computable or
summable in ordinary counting measure.

The normalized Abel subsequence produces only a superharmonic limit by
Fatou. Equality needs control of inverse-exponent tail mass. Neither this
review nor the proof supplies it. Qualitative linear cumulative growth and
cycle renewal were located in prior literature during the pass and explicitly
reclassified as reconstructions, not new discoveries.

## Critical energy: CE-001--003

The root authored this local reconstruction and consequence; its separate
[independent review](CRITICAL_ENERGY_REVIEW.md) is by the concentration
agent. The short non-L2 proof is credited to Valbuena. Finite second-moment
boundedness would yield an L2 martingale limit; equal-measure positive
supports force nonzero branch overlap, contradicting the exact critical
norm identity. No density-floor or doubling-ergodicity premise is hidden.

Layer cake excludes an integrable clipping envelope. It does not prove a
pointwise lower tail, a linear energy-growth rate, or failure of a weak C/U
bound. The exponent-two consequence applies only to the explicitly stated
global clipping census. It cannot be cited as a limitation on actual
predecessor density or source-conditioned counting methods.

## Failed concentration target and evidence ceiling

The attempt to extract sufficiently early repeated blocks from PR140's
collision concentration did not close. The limits are in the wrong order
for that inference, and late sources can have exponentially grown heights.
Computability of an orbit alone is not a zero-entropy principle. The failed
step remains visible in the harmonic manuscript.

The exact finite programs check algebraic interfaces, full bounded residue
laws, complete bounded inverse enumerations, and concrete spectral-vector
residuals. They do not compute an infinite spectrum, decide Collatz
reachability, replay external Lean dependencies, or replace the universal
arguments. The final complete-checkout gate checks repository integrity only.
