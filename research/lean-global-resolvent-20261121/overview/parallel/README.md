# Checkpoint 8: contact probabilities and exact source envelopes

**2026-11-22. Full Collatz remains OPEN.** Three parallel attacks now meet
at two concrete universal questions. The analytic attacks give an exact
first-contact representation of the canonical envelope and an explicit
bound for its finite contact contribution. Their combination reduces
marked sublinearity to a quantitative contact probability. The arithmetic
attack computes the exact largest interval payable by any literal cut
of a supplied source certificate, and exposes the remaining merger
selector. This checkpoint adds **44 audited Lean theorems**.

The work continues checkpoint 7 at
`41dc0ff039c13eeaf7f130c56a290212c00bcdef`. Named source inputs, their
proof status, and overlap with the latest work are recorded in
[SOURCE_RECONCILIATION.md](SOURCE_RECONCILIATION.md) and
[SOURCES_AND_STATUS.json](SOURCES_AND_STATUS.json).

## 1. The combined analytic step

Use the actual positive-integer inverse operator

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
3\,2^{-e}f((2^e q-1)/3),\qquad D_k=P^k1.
\]

Let `V` be PR180's finite least excessive majorant of the ternary-unit
indicator. Fix `epsilon>0`, and stop inverse paths when they first enter
`C={q:3 does not divide q, V(q)<=1+epsilon}`. If `Q` is the inverse
kernel killed at that contact set, minimality proves

\[
Q^L V(q)\downarrow0,\qquad
\boxed{V(q)=\sum_{j\ge0}Q^j(1_CV)(q).}
\]

This removes the **whole surviving inverse boundary**, not just the mass
of one prescribed infinite ray. It is a written countable-kernel proof
with an abstract Lean core. It retains the source-qualified existence
and finiteness of `V`. The statement concerns each fixed ordinary root;
it does not supply a rate uniform in changing roots.

The arithmetic density attack gives

\[
\boxed{D_k(q)\le(4k+2)(3/2)^k}
\]

for every residue and depth, including every positive inverse exponent.
The finite counting core is in Lean; the remaining infinite geometric
tail is proved in the written note. The exponential rate already appears
in the primary manuscript cited below. The contributions here are the
explicit constant, self-contained proof, checked finite core, and its
use in the contact representation.

For the stopped `V`-Doob chain, write `tau` for its first contact time
and `p_L(q)=Prob_q(tau<L)`. The exact telescoping identity and finite
sum bound give

\[
V(q)p_L(q)=\sum_{j<L}Q^j(1_CV)(q)
\le8(1+\varepsilon)L(3/2)^L.
\]

Here `j` and `L` count inverse odd steps. A word's total shortcut clock
is a separate, unrestricted sum of its exponents; its exact weight
retains that sum.

Set `ell(q)=log(q+2)` and, for all sufficiently large `q`,

\[
L(q)=\left\lfloor
\frac{\log q-3\log\ell(q)}{\log(3/2)}
\right\rfloor.
\]

Then

\[
\boxed{\frac{V(q)}q\le
\frac{8(1+\varepsilon)}{\log(3/2)}
\frac1{\ell(q)^2p_{L(q)}(q)}.}
\]

Thus it is enough to prove `p_{L(q)}(q) ell(q)^2 -> infinity` through
the actual constant-70 marked odd units. In particular, an effective
lower bound `p_{L(q)}(q)>=c/ell(q)` would suffice. This needs only a
small capture probability, not a uniform probability tending to one.

**The capture lower bound is OPEN.** An effective proof would give the
marked-height cutoff required by PR180's closing theorem. The corresponding
finite basin certificates below that cutoff remain a separate obligation.
Neither an inverse first-contact theorem nor a conditional implication
is asserted as forward convergence.

Read the full [contact synthesis](CONTACT_CAPTURE_SYNTHESIS.md),
[obstacle proof](OBSTACLE_ENTRANCE_RENEWAL.md), and
[word-density proof](WORD_DENSITY_ENVELOPE.md).

## 2. The exact arithmetic alternative

For a complete supplied source word
`q=q_0 -> q_1 -> ... -> q_r=1` with positive gaps `a_1,...,a_r`, and
initial even exponent `e>=1`, let `S=2^e q`. If a nonempty literal prefix
`W` is removed, the largest initial exponent payable by PR177's strict
multiset rank drop is exactly

\[
F_e(W)=\max(e,\max_{a\in W}(a-1)).
\]

The empty-prefix option separately requires an exponent at most `e-1`.
Consequently the largest powered source obtainable by **any** such cut is

\[
\boxed{E(e,q,A)=\max\left(2^{e-1}q,
\{2^{F_e(A_{\le k})}q_k:1\le k\le r\}\right).}
\]

Lean proves this maximum is attained by an actual suffix certificate,
strictly decreases the original rank, and bounds every other paid literal
cut. The union of all these paid intervals reaches exactly `2E+1`.
The word length and intermediate source sizes are unrestricted. This
maximality claim concerns literal cuts; it does not forbid additional
inverse-prefix rewrites.

For example, source `26=2*13` with complete word `[3,4]` has cut sources
`13,20,8`, hence `E=20`. Target `31` is covered by the interval ending at
`41`, through the actual child certificate `(e=2;[4])`. The previously
failed synchronized calculation for this pair was not a failure of all
source cuts. The older note now carries the precise correction.

The final theorem chain is

\[
\texttt{LowEnvelopeEntry}\Longrightarrow
\texttt{LowEnvelopeMerger}\Longrightarrow
\texttt{LowIntervalStep}\Longrightarrow\texttt{FullCollatz}.
\]

The selector only asks about complete low-gap words, `e` in `{1,2,3}`,
and remaining odd interval targets above `2E+1`. It accepts a positive
partner at most `2E+1` that meets the target at independent ordinary
clocks. **The universal selector is OPEN.**

See [SOURCE_ENVELOPE.md](SOURCE_ENVELOPE.md) and
[SourceEnvelope.lean](lean/Collatz/SourceEnvelope.lean).

## 3. What Lean checks, and what remains written mathematics

| Module | Audited theorems | Exact formal scope |
|---|---:|---|
| [ClockSliceBound](lean/ClockSliceBound.lean) | 7 | Fixed-clock numerator injectivity, numerator range, counting and normalized slice bounds |
| [MinimalObstacle](lean/MinimalObstacle.lean) | 7 | Minimal-majorant subtraction, relative slack, killed fixed points, and summable countable-kernel interfaces |
| [ContactCapture](lean/ContactCapture.lean) | 5 | Exact finite weighted sum, its bound, capture-ratio inequality, and sublinearity under explicit capture hypotheses |
| [SourceEnvelope](lean/Collatz/SourceEnvelope.lean) | 25 | Attained literal-cut maximum, exact coverage, ordinary merger transfer and conditional full closing chain |

The fresh build compiled 20 jobs: the 14 exact PR177 dependency modules,
the four new proof modules, and two audits. All exited zero with
`-j1 -DwarningAsError=true`. All 44 audited theorem outputs use only
`propext`, `Classical.choice`, and `Quot.sound`, or no axioms.

The infinite parent-limit argument, contact probability law, all-clock
tail summation, logarithmic depth specialization and sharp marked spikes
are written proofs. They are not silently installed as Lean axioms.
The Collatz-specific analytic input retains its upstream qualification.

The [portable driver](check_parallel.py) checks the exact Lean and Mathlib
pins, frozen dependency hashes, source hashes before and after compilation,
and the expected axiom-audit count. From the repository root:

```sh
python -X utf8 -B research/lean-global-resolvent-20261121/overview/parallel/check_parallel.py \
  --mathlib /path/to/mathlib4 \
  --lean /path/to/lean-4.34.1/bin/lean \
  --out /path/to/new-empty-output \
  --receipt /path/to/checkpoint8-lean.json
```

Use Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612` and Lean
commit `5045d0056413266e57c625dcd7c365b10e377c52`. A dependency cache is
optional and must match the pinned compiled artifacts. The committed
[execution receipt](../../../../reports/2026-11-22-parallel-global/checkpoint8-lean.json)
records the actual commands, outputs, source hashes and audit results.

## 4. Standalone handoff and useful limits

[question_inverse_contact.txt](question_inverse_contact.txt) states the
quantitative probability question using only its integer kernel,
canonical envelope, stopping law and dyadic window. It does not name
Collatz in the problem statement. Its full-proof significance, analytic
inputs and finite-base obligation are disclosed above.

The density exponent cannot simply be reduced: the note gives infinitely
many actual marked targets with a matching `(3/2)^k` spike. The potential
argument also shows that every unit ternary cylinder contains arbitrarily
high envelope values. A finite residue class cannot certify membership
in the actual low-envelope contact set. These are scoped obstructions;
they leave weighted capture and ordinary real-offset estimates open.

The primary literature connection is the least-excessive-majorant
interpretation of optimal stopping. The finite-density exponent is
credited to [Ternary Syracuse laws, Theorem 9 and Appendix B.2](https://rstation.ai/problems/collatz/papers/9),
with the fixed-clock injectivity attributed there to Tao's Lemma 6.2.
The direct proofs here specify the ordinary domain, countable sums and
actual clocks needed by this repository.
