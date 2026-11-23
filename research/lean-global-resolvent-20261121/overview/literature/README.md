# Checkpoint 7: critical Abel limits and the remaining marked-height bound

**Continuation:** [Checkpoint 8](../parallel/README.md) gives an exact
contact-entrance representation, an explicit finite-depth density bound,
and the maximal paid literal-cut source interval. It adds 44 audited Lean
theorems and a more concrete finite-time capture target.
Its [source reconciliation](../parallel/SOURCE_RECONCILIATION.md) credits
PR180's intervening finite-depth sandwich and corrects the scope of the
older synchronized even-run budget.

**2026-11-22. Full Collatz remains OPEN.** This continuation combines
rational-affine renewal, ordinary hitting potentials, and signed-cycle
transport. It adds 94 audited Lean theorems and a written analytic bridge.
It builds on checkpoint 6 at `486b0421f34f332645c46a723033eda480718d69`.

The late updates to PR177 and PR180 materially changed the frontier. Read
the [source reconciliation](LATEST_REPO_RECONCILIATION.md) alongside this
page. PR180 already supplies the canonical envelope and a stronger
marked-only closing theorem. PR177's new high-gap rule covers our entire
large-terminal-gap family under its common induction hypothesis.

## 1. The new analytic integration result

Let `P` be the actual critical inverse operator, `D_k=P^k 1`, and

\[
H_r=(1-r)\sum_{k\ge0}r^kD_k,\qquad 0<r<1.
\]

PR180 constructs the finite least excessive majorant `V` of the unit
indicator `g`, and its harmonic part `G=lim_k P^k V`. Given that construction
and its uniform atom floor `D_k>=alpha g` at all sufficiently large depths,
we prove

\[
D_k\le2P^{k-1}V\le2V\quad(k\ge1),\qquad
H_r\le1+2V.
\]

Since `P(1+2V)` is finite at every ordinary target, this majorant makes the
actual Abel parent tails uniformly integrable at each fixed target. Every
common pointwise critical Abel limit `h` is therefore **harmonic**, and

\[
\boxed{
\alpha V\le\liminf_{r\uparrow1}H_r
\le\limsup_{r\uparrow1}H_r\le2G\le2V.
}
\]

This discharges the parent-tail limit interchange left open in the earlier
Abel construction. It also transfers inverse-ray atom removal and
fixed-basin sublinearity to every actual critical Abel limit. The proof,
quantifiers, and imported hypotheses are in
[ABEL_CANONICAL_COMPARISON.md](ABEL_CANONICAL_COMPARISON.md).
This is a written conditional analytic theorem, not a Lean declaration.
It proves neither uniqueness of the critical limit nor uniform decay as
the ordinary target moves.

The same comparison holds for ordinary depth liminf and limsup. Moreover,
`D_n(q)>=(alpha/2)D_j(q)` once `n>=j-1+k_0`. Thus a deep finite-level spike
persists at a fixed fraction at all sufficiently later depths. The desired
marked-height estimate can equivalently be posed for `sup_k D_k(q)` under
the same imported inputs; the new note proves this comparison as well.

## 2. The best remaining analytic target

For a positive odd ternary unit `q`, put `d=floor(log_2 q)`. The exact
constant-70 marked section is

\[
(d+1)(q-2^d)\le70\,2^d.
\]

Every ordinary orbit reaches this section. PR180's Lean theorem
`universal_of_marked_inverse_envelope_and_base` needs the upper estimate
only there. The remaining height question is

\[
\boxed{
\frac{G(q)}q\longrightarrow0
\quad\text{as marked ordinary units }q\longrightarrow\infty.
}
\]

By the new comparison, the same question can be asked of `V`, any one
common critical Abel limit, `limsup H_r`, or `sup_{k>=1} D_k`. These are equivalent height
obligations up to absolute constants. An effective estimate also supplies
a finite cutoff; convergence certificates below that cutoff are still
required by the full closing theorem. No such effective marked-height
estimate is proved here.

The [standalone arithmetic question](question_critical_trace.txt) states
this target using only word sums, congruences, Abel means, and the integer
window. It includes a more ambitious power-bound version. Its closing
significance is disclosed here; the question itself is self-contained.
The earlier [primitive-source moment question](../../question_primitive_source_moment.txt)
remains a separate complete arithmetic criterion that includes escape and
cycles without the present analytic inputs.

Fixed-discount bounds and fixed-root predecessor-basin decay do not yet
give the displayed estimate. The former lose their gain as `r` approaches
one; the latter allow the cutoff to depend on the root. The missing control
is uniformity as the marked ordinary target changes.

## 3. New finite and arithmetic theorems

| Result | Evidence | Exact limit of the result |
|---|---|---|
| Ordinary hit potentials, killed Green equations, finite exit identities, and predecessor trace inequalities | 41 Lean theorems, with explicit finite count hypotheses | No upper survivor-flux bound is asserted |
| Critical trace propagation, boundedness under a supplied sublinear estimate, and finite-cycle ratio floors | 10 Lean theorems, with explicit edge and side-parent hypotheses | PR180 already has the stronger marked-only global interface |
| Every nonnegative carry deficit has arbitrarily large actual complete ordinary sources; exact continuation and suffix debt law | 43 core Lean theorems | The terminal gap is necessarily large, so PR177's new high-gap interval rule covers this family under its induction hypothesis |
| Pointwise complete inverse Green estimate at nonperiodic targets, with explicit decay as the floor rises | Written proof conditional on the pinned CFJ input | It is a bound for each row, not a sum over all rows; full cycle Green sums diverge |
| Sublinear growth at each fixed Abel discount | Written calculation; PR180 already proves the stronger all-target scope | No uniform critical endpoint estimate follows |

The carry family is exact for every `D>=0`:

\[
B=22D+132,\quad t=21D+132,\quad d_D=244\,2^D-5,
\qquad B-t=D.
\]

All prefix gaps are at most four. Actual complete source legality forces
the terminal gap `h>=B+3`, and supplies arbitrarily large such realizations.
Thus a scalar uniform deficit bound is false, while the complete source
simultaneously supplies a large terminal grade. The latest interval
dispatcher uses that grade. Its remaining arithmetic language has initial
even run in `{1,2,3}`, all odd gaps at most four, and unbounded word length.

The finite-anchor analysis also refutes a tempting broad density Poincare
inequality using actual disjoint predecessor basins. The replacement keeps
singleton defects, upper exits, and trapped internal cycles explicitly.
It does not refute a separately restricted theorem for exactly invariant
ordinary labels.

## 4. Reading order

1. [Latest repository reconciliation](LATEST_REPO_RECONCILIATION.md): source
   pins, priority, and the current remaining obligations.
2. [Canonical Abel comparison](ABEL_CANONICAL_COMPARISON.md): the new
   domination, harmonicity, and comparison proof.
3. [Admissibility-sensitive inverse Green estimate](ANCHORED_INVERSE_GREEN.md):
   the actual inverse words and pointwise Green bound.
4. [Trace-height completion attempt](TRACE_HEIGHT_CLOSURE_ATTEMPT.md) and
   [critical trace interface](CRITICAL_TRACE.md): the attempted global step,
   its failed endpoint passage, and the finite Lean implications.
5. [Ordinary anchors and exit flux](ORDINARY_ANCHORS_AND_EXIT_FLUX.md): exact
   finite-target identities and the surviving boundary terms.
6. [Signed cycles and terminal precision](CYCLE_DEFICIT_FAMILIES.md): the
   all-deficit family, latest high-gap coverage, and the failed automatic
   low-alphabet clock-payment implication.

## 5. Literature and proof boundaries

Brofferio's rational-affine boundary theorem motivates retaining both the
real and ternary coordinates. Tao's renewal estimate is the non-elementary
source behind the pinned PR180 CFJ argument. Mixed binary/ternary rewrite
systems motivate retaining both arithmetic resources in the carry analysis.
The proofs and reductions used here retain actual ordinary integer targets.

The current Valbuena manuscripts suggest a finite-resolution route, but
their canonical-density and integrability claims are not dependencies of
the Green proof or any Lean declaration. Sources and reading scopes are in
[SOURCES_AND_STATUS.json](SOURCES_AND_STATUS.json). The newer PR180 inputs
and their exact scope are recorded in the reconciliation and Abel notes.

No `sorry`, convergence axiom, unproved trace-capture assertion, or discarded
positive-cycle term is used to make a Lean module compile.

## 6. Replay

`python overview/check_literature.py --help` describes the dedicated replay.
It builds the four new core modules and two new Mathlib modules with their
necessary local imports, using Lean 4.34.1 and the pinned Mathlib commit.
All 94 new public theorem audits passed with warnings treated as errors;
their axiom union is `propext`, `Classical.choice`, and `Quot.sound`.

The exact execution receipt is
[checkpoint7-lean.json](../../../../reports/2026-11-21-lean-global-resolvent/checkpoint7-lean.json).
The independent [arithmetic replay](replay_cycle_carry.py) checks 129 compiler
programs, 140 arbitrary-suffix identities, and 13 terminal congruences at
full precision. Its
[receipt](../../../../reports/2026-11-21-lean-global-resolvent/checkpoint7-cycle-replay.json)
distinguishes modular checks from the infinite ordinary-realization theorem
proved in Lean. Checkpoint-6 sources and receipts remain available unchanged.
