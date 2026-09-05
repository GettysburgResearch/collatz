# Session report — cross-direction lemma forge

Agent: `gpt56-synthesis-01`  
Issue: #29  
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`  
Date: 2026-07-21

## Starting hypothesis

Several active directions were independently reaching the same boundary:
finite congruence cylinders and completion points are abundant, while a
counterexample requires one ordinary positive integer compatible at every
depth. The working hypothesis was that a small number of exact arithmetic
lemmas could expose this shared bottleneck and create useful interfaces between
otherwise separate programs.

## Approaches attempted

1. Read the repository protocol and mapped the active collision/Hensel,
   adelic-carry, active-cylinder, H-frontier, regular-sanctuary, Schottky,
   termination, foundry, and solution-cone branches.
2. Reconstructed the collision branch's dyadic bulk algebra in a general odd
   base rather than importing its claim status.
3. Assigned three independent mathematical lanes: adelic completion height,
   active survivor cylinders, and H carry geometry.
4. Gave the successful adelic and active-cylinder lanes harder follow-ups:
   finite CRT transference, simultaneous cylinders, and zero-tail rigidity.
5. Cross-checked the returned formulas against the source branches and
   packaged them in a separate provisional namespace.
6. Tested two tempting bridges adversarially: local carry sparsity to itinerary
   repetition, and coarse H carry rectangles to mixed-sign displacement.

## New results

### General arithmetic interfaces

- `L-9801`: compatible canonical cylinders contain an ordinary nonnegative
  integer exactly when their representatives eventually stabilize.
- `L-9802`: odd-base inverse powers obey an exact quadratic Hensel recurrence,
  have exact odometer difference valuations, and converge after normalization
  to an explicit 2-adic logarithm.
- `L-9803`: one product-formula wedge gives both the completion-height
  zero-carry slope and the reciprocal ordinary-code repetition slope.

### Active survivor cylinders

- `L-9804`: every finite active height directive has an exact forward
  mixed-radix digit recurrence and automatic nonnegative propagation. The
  extension digit vanishes exactly at one target-modulus congruence.
- `L-9805`: an eventually zero digit tail must follow a deterministic partial
  valuation map. Its normalized state has an exact real/2-adic series formula,
  and its terminal height grows with logarithm `Theta(K^2)`. Any fixed
  polynomial-in-stage-modulus height bound would exclude stabilization.

### Adelic/itinerary diagonal

- `R-9801`: finite reciprocal-carry sparsity cannot force a repeated survivor
  block. CRT combines a zero-carry phase prefix with an arbitrary de Bruijn
  itinerary prefix, even while taking one positive primitive integer as both
  frequency and survivor. The integer necessarily depends on the depth.
- `L-9806`: the correct global bridge is one simultaneous cylinder modulo
  `5184^K`, with an exact base-`5184` digit recurrence. For every stabilized
  positive integer, the reciprocal lift digits are eventually nonzero and
  4-periodic; only the combined CRT digit should eventually vanish.

### H carry geometry

- `L-9807`: the unresolved first expanding-to-contracting crossing is exactly
  the sharp inequality `c+he <= delta+jd`, equivalently one rational endpoint
  comparison. This is a reduction, not a proof of `PR19/C-9501`.
- `R-9802`: a fully integral abstract affine tuple satisfies the canonical
  endpoint ranges, both input sign inequalities, and the interface carry
  rectangle but reverses the composite sign. Therefore a proof must use the
  actual ordered H offset or ghost digits.

## Candidate counterexamples

None. No ordinary nontrivial infinite trajectory and no `K-####` candidate is
claimed. The countermodels `R-9801` and `R-9802` refute proof strategies, not
the Collatz conjecture or an established theorem.

## Failed approaches and negative information

- A local carry-to-repetition bridge is impossible at finite depth because the
  relevant conditions live on coprime `81`-adic and `64`-adic axes.
- Vanishing reciprocal lift digits are the wrong stabilization target: for a
  fixed positive integer they become nonzero periodic digits.
- Zero active-cylinder digits do not imply literal terminal equality or a
  bounded quotient carry; the quotient instead escapes quadratically in log
  scale.
- Canonical H endpoint ranges and carry rectangles do not settle a mixed-sign
  crossing. An exploratory bounded word search found no actual-word failure,
  but this is empirical and was not used in any claim.
- Precision growth by itself is not an ordinary-section obstruction.

## Potential errors to audit

1. Recheck the signs and inverses in `L-9806/(11)`--`(14)` and the positive
   representative convention in its late normal form.
2. Audit both directions of the 2-adic series membership criterion in
   `L-9805/(12)`, especially preservation of `u_K congruent to 1 mod 1296`.
3. Recheck that every modulus in `L-9804` is the target height modulus and that
   positivity is propagated through the quotient coordinate.
4. Keep the depth-dependent CRT integer in `R-9801` separate from a single
   stabilized ordinary integer.
5. Keep `R-9802` labeled as an abstract affine countermodel, never as an H-word
   counterexample.
6. Do not promote `PR19/C-9501`; `L-9807/(6)` is precisely the missing step.

## Files changed

- `research/cross-direction-lemmas/README.md`
- `research/cross-direction-lemmas/CLAIMS.md`
- `research/cross-direction-lemmas/VERIFICATION.md`
- `research/cross-direction-lemmas/claims/L-9801-nested-cylinder-stabilization.md`
- `research/cross-direction-lemmas/claims/L-9802-dyadic-logarithmic-bulk.md`
- `research/cross-direction-lemmas/claims/L-9803-completion-height-wedge.md`
- `research/cross-direction-lemmas/claims/L-9804-active-cylinder-digit-recurrence.md`
- `research/cross-direction-lemmas/claims/L-9805-zero-tail-escape.md`
- `research/cross-direction-lemmas/claims/R-9801-finite-crt-orthogonality.md`
- `research/cross-direction-lemmas/claims/L-9806-simultaneous-cylinder-recurrence.md`
- `research/cross-direction-lemmas/claims/L-9807-h-first-crossing-reduction.md`
- `research/cross-direction-lemmas/claims/R-9802-h-carry-rectangle-insufficiency.md`
- this report

## Claims affected

New provisional IDs: `L-9801` through `L-9807`, `R-9801`, and `R-9802`.
No root ledger or source-branch status was changed.

## Recommended next actions

1. Seek a terminal-context height bound from the room/carry-energy programs and
   feed it into `L-9805`.
2. Combine the late 4-periodic reciprocal restriction in `L-9806` with a
   theorem about the itinerary of one fixed ordinary survivor.
3. Rewrite `L-9807/(7)` using the ordered H offset sum and identify the exact
   residue or monotonicity property missing from `R-9802`.
4. Connect the next non-stabilized logarithmic bit in `L-9802` to the finite
   residual router in PR #3.
5. Obtain external repository review before promoting any packet claim.

## Organizational improvement ideas

Every completion-based direction should expose the same three objects in its
claim packet: canonical representatives, extension digits, and an explicit
ordinary-section criterion. Cross-direction proposals should also include a
finite CRT independence test before symbolic patterns on coprime axes are
treated as causally linked.

## Adversarial review addendum

Before publication, all three proof lanes reread the integrated files.

- The adelic lane passed `L-9803` and `L-9806`, and narrowed `R-9801` to its
  exact finite conclusion: sparse carries do not force a repeat of length at
  least `ceil(log_2 K)`.
- The active-cylinder lane passed `L-9801` and `L-9804`, and caught a genuine
  scope distinction in `L-9805`: membership of `U_s^(2)` constructs an
  ordinary suffix context, while stabilization of the already selected prefix
  requires the stronger equality `U_s^(2)=81t_s+1`.
- The H lane verified every integer in `R-9802` and every identity in `L-9807`.
  It also identified the strict version of the carry inequality needed to
  exclude zero displacement for a non-all-zero word.

These corrections were integrated while every claim remained `PROPOSED`.
