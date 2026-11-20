# Review of the ordinary basin-closure proof attempt

**Result:** the scoped identities and finite affine certificates survived
independent reconstruction. The universal basin implication, a successful
all-source selector, and the analytic head bound remain unproved. This is
agent-level mathematical review, not external acceptance or formal verification.

## What was attempted

The primary target was PR146's one-sided basin implication. Work proceeded
through three independent routes: transfer a supplied ordinary certificate,
prove an adaptive first-return descent, and establish a source-weighted
arithmetic upper bound. The source revisions and concurrent later comparisons
are listed in the packet's SOURCES.md.

The first attempted closing step failed at an exact terminal carry, already
present for an antecedent with two accelerated odd steps. The second failed
on an entire positive ordinary affine cylinder, then on a second cylinder
which replenishes the first return's valuation resource. The third removed
all nonminimal endpoint lifts with an exact exponentially small remainder,
but did not bound the remaining least-endpoint mass. None of these failures
was replaced by an assumption of fresh digits, an independently uniform
ternary endpoint, or an arbitrary accepting terminal state.

## Certificate transfer

The root independently substituted the legal inverse edge
`x=(2^a z−1)/3` into the universal carry formula and reconstructed the
two-state rules, including both asymmetric merger clocks. It checked the
unhandled `(1,2)` denominator, the exhaustive two-step classification,
the forced Mersenne excursion, and the necessary total-valuation increase.

A separate agent independently reconstructed these calculations and supplied
`check_certificate_carry_review.py`, which imports none of the compiler.
Its detailed algebra review is in REVIEW_CERTIFICATE_CARRY.md. A further
cross-review by the adaptive-pair agent found no additional error in the
refined compiler.

The published compiler validates a supplied finite source word before using
it. Every emitted merger edge has positive odd endpoints and nonnegative
integer clocks. For an edge with clocks L,R and a certified right hitting
clock D, the compiled left hitting clock is `L+max(D−R,0)`, using `U(1)=1`.
The resulting target word is independently replayed. Corrupted source gaps,
meeting clocks, endpoints, and declared meeting values are rejected. These
checks prove that accepted outputs are literal finite certificates; they do
not prove that the compiler accepts every source certificate.

The later PR146 head contains the same depth-two family and stronger
bounded-rank and three-step results. That overlap is explicitly credited;
the partial compiler is not reported as a replacement for the stronger
current source theorem.

## Expanding physical returns

The root reconstructed the role of the source stride `2^39`, the exact
positive affine floor margins, and the endpoint parity needed to certify
every odd part. It checked why the unequal-clock slope comparison excludes
identically equal cross-block endpoint functions, and why every fixed
eventually periodic macro schedule has a positive integer affine resource
whose binary valuation decreases by the period's full clock length.

The independent reviewer rebuilt the entire physical affine trajectories
without importing the author verifier, checked all 1,521 cross-arm equations
and 74 intermediate section equations for each macro, and constructed finite
schedules by a separate modular-inverse algorithm. It verified the exact
`(47,9) → (9,47) → (47,9)` valuation cycle, the supplied concrete convergent
orbits, and the first subsequent descent and meeting clocks. The detailed
review is in REVIEW_EXPANDING_RETURNS.md.

Two wording corrections were required and incorporated before publication:
the obstruction refutes a **guard-only unconditional numerical lemma**, not
an arbitrary theorem that additionally assumes a genuine least nonconverger;
and the general repetition theorem explicitly assumes a positive clock
length. A finite family of changing positive witnesses is not an all-time
positive orbit. This distinction remains explicit throughout the packet.

## Finite endpoint head

The root independently checked the following items in PRIMITIVE_TRACE.md:

- The least positive odd endpoint and its binary source are paired by the
  same affine congruence, as already established in PR156 SM4.
- Summing the positive lifts gives the two-sided geometric error with
  coefficient `(3/5)^q`.
- The complete inverse-gap recurrence is periodic because increasing a
  gap by `2·3^(q−1)` changes the previous odd endpoint by a multiple of
  `2·3^(q−1)`; geometric summation retains every such gap.
- The partial-summation identity keeps its lower endpoint and its
  exponentially small upper-end contribution.
- Both deliberately independent replacement models grow exponentially;
  they are not asserted distributions of actual ordinary orbits.
- The subquartic power-supersolution obstruction uses actual integral
  inverse chains, with the stated comparability constants and domain.

The exact finite-head checker separately reconstructs word representatives,
literal forward lifts, complete infinite-gap columns through q=5, and the
known total period mass. The modest finite range verifies the implementation
of the identities, not the unproved bound at all q.

## Further attack on arbitrary switching

The two return constants differ by `2^9·3^14`. The root checked the common
binary/ternary congruence, the exact affine normalization in
TWO_MACRO_NORMALIZATION.md, and its converse recovery of the safe cylinders.
The normalized recurrence is precisely a ceiling-map orbit restricted to two
consecutive remainder values. Its narrow real shadow is necessary only; the
real and 2-adic limits are not identified. The external primary source cited
there labels the broader equidistribution statement a conjecture, which was
checked directly. No unavailable theorem is imported.

This additional attack did not provide an all-source exclusion. Its relevance
is limited: in the intended least-counterexample argument, the already
convergent physical X arm already prevents infinitely many unchanged returns.
The original problem still includes permanent avoidance of useful sections.

## Execution boundary

The initial five checkers passed in ordinary and optimized Python locally,
with byte-identical output between those modes. Publication validation will
run the final six-checker packet, including the normalization, and the
repository regression bundle in a clean complete
checkout of the actual GitHub scientific commit. Its exact SHA, tree, commands,
and receipts are recorded in VALIDATION.md in a later documentation commit.

Repository integrity, algebra inspection, independent code reconstruction,
and a complete clean-checkout execution are separate forms of evidence. No
one of them is described here as a proof of Collatz.
