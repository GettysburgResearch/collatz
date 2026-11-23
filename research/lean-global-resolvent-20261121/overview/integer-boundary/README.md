# Ordinary integer fibres and direct closing attacks

**Checkpoint 15 — 23 November 2026. Full Collatz remains OPEN.**
This pass builds on the latest ordinary atomic-pressure, finite-witness,
residual-denominator, and same-source collision results. It produces a
corrected theorem about simultaneous real and 3-adic values, with a Lean
proof of its quantitative real bridge, and an infinite-dimensional theorem
about positive approximate fixed vectors. Neither theorem excludes an
escaping component or a nontrivial positive cycle.

The current repository inventory covers **145 unique PR metadata records**.
The scientific reading was targeted at six newly advanced branches, with
16 exact source files pinned in [SOURCES.json](SOURCES.json). This is not a
new proof audit of every historical branch. The parent of this checkpoint
is `ff3e068fa44eb85bb918580b2e10e18c027a18e6`.

## 1. A corrected two-place theorem, with the real gap retained

For an infinite binary code with one-digits at positions
`d_1 < d_2 < ...`, consider the same rational partial sums in two
completions:

\[
 S_k=\sum_{i=1}^k\frac{3^{i-1}}{2^{d_i+1}}.
\]

Suppose the 3-adic limit is a positive odd ordinary integer `q`. The tails
of the series then determine actual positive odd unit inverse states
`q_i`, with exact valuations, rather than freely chosen residue witnesses.
The real limit `B` exists and satisfies `0 < B <= q`. The complete
[written classification](TWO_PLACE_NUMEN_CLASSIFICATION.md) proves

\[
 \boxed{B=q\quad\Longleftrightarrow\quad
 \text{the supplied inverse itinerary stays on the actual cycle of }q.}
\]

In the equality case the binary code is purely periodic. If `q` is
nonperiodic, every such code instead has the uniform gap

\[
 \boxed{q-B\ge q\exp(-200/3)>0.}
\]

Here *nonperiodic* includes an integer that later enters the known cycle;
it does not mean that the integer escapes. If the root is periodic but
the inverse path eventually leaves its cycle, the strict gap retains the
finite initial cycle product. It is not uniform over all exit times.

The argument extends PR177's elementary cylinder count to a simple
inverse ray by removing its first `r=floor((3/5)log_2 X)` vertices before
using injectivity of `U^r`. This gives

\[
 \#\{i:q_i\le X\}\le5X^{39/40},\qquad
 \sum_iq_i^{-1}\le200.
\]

The exact real remainder is

\[
 q-S_k=q\prod_{i=1}^k\frac{3q_i}{3q_i+1}.
\]

Thus this result uses elementary actual-integer counting and a retained
real tail. It requires no canonical-envelope, population, stationary-law,
or mixing input. The written proof received an independent reconstruction.
The count is credited to PR177 and its earlier source lineage; the
two-place deduction is not accompanied by a global priority claim.

### What Lean proves

[InverseRealSeparation.lean](lean/InverseRealSeparation.lean) proves
**10 theorems and 3 definitions**, all covered by
[the axiom audit](lean/AuditInverseRealSeparation.lean). Its final theorem
uses positive natural-number states and the literal edges

\[
 2^{e_i}q_i=3q_{i+1}+1.
\]

From the explicitly stated finite reciprocal budget at every depth, it
constructs the real limit of the literal series and proves the displayed
gap. The earlier statements prove affine telescoping, product
telescoping, the exponential estimate, and the dyadic series identity.

The ordinary cylinder count, 3-adic tail reconstruction, and full periodic
classification are written proofs. They are **not** hidden in Lean as
axioms or represented as having been formalized. The module's only axiom
dependencies are `propext`, `Classical.choice`, and `Quot.sound`.

### Why an unrestricted 3-adic root criterion fails

The [inverse-fibre construction](NUMEN_INVERSE_FIBER.md) proves that every
positive odd 3-unit has continuum many irrational binary preimages under
this 3-adic series. At each inverse step choose either of two legal gaps
between 3 and 8. The resulting ordinary states increase strictly. At
root 1 one such ray begins

\[
 1,5,13,277,1477,7877,21005,\ldots.
\]

Its 3-adic sum is 1; its real sum is at most `1/5`. Consequently an
irrational preimage alone does not imply a forward escaping trajectory.
This directly contradicts that converse in Theorem 2.7 of Siegel's
arXiv:2412.02902v1. The inspected proof infers rationality of a particular
preimage from the existence of some rational preimage. The note gives
the exact normalization, source pages, and counterexample. It makes no
claim to review or reject the dissertation's other analytic machinery.

The corrected two-place theorem leaves the periodic equality alternative
intact. A hypothetical nontrivial positive integer cycle would satisfy
that alternative. The full-denominator arithmetic has therefore not been
eliminated by changing completions.

## 2. Positive pressure quasimodes in the known basin

PR177's new classification makes escape equivalent to a nonzero positive
ordinary fixed vector of

\[
 (A_sh)(n)=\left(\frac3{2^{v_2(3n+1)}}\right)^s h(U(n)),
 \qquad s>1,
\]

with the actual component coefficients bounded by `n^(-s)`. The attempted
closing argument used their extra real-circle Fourier regularity.

The new [Wiener-space theorem](PRESSURE_WIENER_ATTACK.md) shows that, for
every `s>1` and `0<=t<s-1`, there are nonnegative vectors supported wholly
in the known basin of 1 such that

\[
 \|f_k\|_t=1,\qquad
 \|(I-A_s)f_k\|_t\le2^t(2/3)^{(s-t)k}\longrightarrow0,
 \qquad \|h\|_t=\sum n^t|h(n)|.
\]

Every true fixed vector vanishes on that basin, so these vectors have
distance exactly one from the kernel. Hence the range of `I-A_s` is not
closed and the operator is not Fredholm in any of the specified spaces.
Finite-support positive approximants also exist.

This is a statement about the actual weighted ordinary pullback. PR175's
unweighted Hardy pushforward results concern a different operator. Here
positivity and the automatic finite coefficient moments do not restore
norm coercivity. The approximate vectors do not obey a uniform bound
`C n^(-s)`; their mass moves out to larger indices. Exact uniqueness in
the fixed coefficient envelope remains a separate, unresolved question.

At `s=2`, the note derives an equivalent finite mixed dilation equation
with six explicit residue filters modulo 9. The self-contained
[WEIGHTED_FUNCTIONAL_QUESTION.txt](WEIGHTED_FUNCTIONAL_QUESTION.txt)
states that analytic uniqueness question without its dynamical application.
It can be assigned independently. It targets escape only; it is not
claimed easier than the original missing escape argument.

A fourth agent attacked that equation independently, initially without its
application. The [analytic continuation note](INDEPENDENT_KERNEL_ATTACK.md)
derives the exact repetition
`g_(64n+21)=g_n`, where `g_n=(n+1/3)^2 h_n`, and the differentiated mixed
equation. Any nonzero solution consequently fails the critical little-o
coefficient condition and has no Hardy `H^1` second Euler derivative.
The envelope supplies substantial subcritical Sobolev regularity, but the
attempt did not bootstrap it to that endpoint. Its reconstructed maximal
solution and escape equivalence are credited to the existing project input.


## 3. The mandatory band does not pay for the full binary horizon

The unrestricted finite optimizer on PR177 already includes every complete
source eligible to improve its grade. The next attempt therefore used the
actual target's marked visit `q=2^a+r` and its smaller binary remainder.
The [source note](BAND_REMAINDER_CLOSURE_ATTEMPT.md) retains the exact identity

\[
 T^j(q)=T^j(r)+2^{a-j}3^{o_j}\quad(0\le j\le a).
\]

Three resources are missing from a universal use: a remainder below the
original least bad input, a certificate fitting the shared horizon, and
a saving below that unchanged original input rather than merely below
the later marked state.

The new all-parameter diagnostic is

\[
 q=2^{3k}+2^{2k+1}-1,\quad a=3k,\quad k\ge2.
\]

It lies in the narrower band `(a+1)(q-2^a)<=4*2^a`, while every actual
iterate at clocks `1,...,a` is strictly above `q`. The relative band
excess tends exponentially to zero. This refutes descent by the full
shared binary horizon from band geometry alone. It does not refute an
unbounded, target-aware continuation, and no member is asserted divergent.
This is a diagnostic appendix, not a new universal descent estimate.

## 4. What the latest repo changes leave as central targets

| Current input | Actual remaining implication |
|---|---|
| PR177 ordinary pressure cone | Exclude an exact positive fixed vector with its fixed ordinary coefficient envelope. The positive quasimodes above rule out a norm-gap shortcut. |
| PR185 residual polynomial degree and growth | Exclude complete numerical cancellation at the actual evaluation. A positive integer cycle remains the allowed equality case of the two-place theorem. |
| PR185 same-source collision lower bound `c sqrt(m) 3^(-theta m)`, `theta=0.949955527188...` | Prove an upper bound `O(3^(-theta m))` on the same actual source law and admissible moving precision. |
| PR180 actual boundary and entropy identities | Supply regularity of that canonical probability law, rather than only full-dimensional support or an auxiliary inverse law. |
| PR177 complete optimizer and PR180 all-length source cuts | Construct an actual original-target merger or cheaper complete certificate, paying the original floor and full grade. |

The collision/boundary attack was pursued with the original integer and
clock retained. No same-law collision upper bound was obtained. In
particular the full dimension of a support cannot be substituted for the
dimension or collision entropy of the canonical measure carried by it.
These are the missing implications after the current synthesis, not new
theorems asserted by this packet.

## Evidence and reproduction

The [execution report](../../../../reports/2026-11-23-integer-boundary/README.md)
keeps source hashes, internal review scopes, compiler evidence, and the
separate repository-integrity gate. New finite controls cover the six
pressure trajectory families, exact residue filters and operator
coefficients, the numen inverse prefixes, and the band family. They do
not substitute for the written infinite arguments.

```bash
python -X utf8 -B research/lean-global-resolvent-20261121/overview/integer-boundary/verify_integer_boundary.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib \
  --receipt /absolute/path/outside/the/checkout/checks.json
```

Use Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Existing dependency objects
are reused; no historical project Lean corpus or old large census is
rebuilt. [Checkpoint 14](../longshot/README.md) and the earlier positive
[sparse-return results](../returns/README.md) retain their original scope.
