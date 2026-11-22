# Whole-repository synthesis and a faster mandatory-band clock

**Latest continuation:** [Checkpoint 8](parallel/README.md) combines three
parallel attacks into a quantitative inverse-contact question and an exact
source-envelope merger condition, with 44 new audited Lean theorems.
[Checkpoint 7](literature/README.md) connects PR180's
canonical envelope to the entire critical Abel family, adds 94 audited
Lean theorems for ordinary traces, finite anchors, and complete carry
families, and reconciles those results with the latest PR177/180 heads.
The present page preserves the checkpoint-6 statements and evidence.

**Checkpoint 6. Full Collatz remains OPEN.** This pass combines a broader
source review with three new proof developments: a substantially faster
entrance theorem for the existing shrinking band, an all-word lower bound
on the odd-step cost of smaller mergers, and a terminating carry reduction
for arbitrary complete certificate prefixes.

All maps below use the ordinary shortcut convention: an even input is
halved, and an odd input is sent to `(3n+1)/2`. Every merger and every
transport theorem concludes something about an ordinary integer.

## 1. The quantitative advance

Let `d(n)=floor(log_2 n)` and `alpha=log_2 3`. A supplied coprime rational
grid with

\[
q>0,\qquad |q\alpha-a|\le1/q,\qquad d(n)\le q
\]

forces an actual marked visit at a clock

\[
\boxed{t<8q+d(n).}
\]

The mark is exactly PR173's existing condition: the input is odd and
`(d+1)(n-2^d)<=70*2^d`. At every existing admissible scale `Q`, this yields
the uniform range theorem

\[
1\le n\le2^Q\quad\Longrightarrow\quad
\exists t<9Q:\ \operatorname{Mark}(T^t n),\quad T^t n<2^{10Q}.
\]

The proof chooses the actual floor `q^2`. If the odd orbit stays above it,
the accumulated phase error fits inside the rational grid. If it crosses
below it, the older square-root theorem is applied at that smaller state.
All initial and intermediate halvings are counted. The finite statement
has no irrationality-measure or orbit-injectivity assumption.

[FastForward.lean](../section/lean/FastForward.lean) contains the finite
proof and its exact smaller-marked-partner consequence.
[Integer306.lean](../section/lean/Integer306.lean) gives a small exact
integer certificate for the grid `485/306`; consequently every positive
`n<=2^306` reaches a mark in fewer than **2,754** shortcut steps. This is
a band-entrance certificate, not a convergence certificate for that range.

The published exponent `4.117` for the irrationality measure of the ratio
of logarithms then gives the written analytic corollary

\[
\tau_{\rm mark}(n)=O((1+\log n)^{4.117}).
\]

The same bound holds for the first positive marked return. The published
number-theory input and the continued-fraction argument are written in
[POLYLOG_BAND_ENTRANCE.md](POLYLOG_BAND_ENTRANCE.md); that external theorem
is not installed as a Lean axiom. The Lean theorem
`bounded_visit_of_separation` exposes the precise finite denominator
exclusion required for this passage.

## 2. All inverse words, with no halving-clock bound

If `2^j` divides `n+1` and `3^L` divides `n-1`, then every strictly smaller
ordinary partner satisfying `T^q(x)=T^j(n)` must use more than `j+L` odd
inputs. The inverse clock `q` and every run of even inputs are unrestricted.
This is a universal inverse-word theorem, not a search over a finite rule
dictionary.

The result sharpens the comparison-center argument of PR146 by using the
center one. An explicit Mersenne family requires arbitrarily large surplus
odd budgets throughout its whole initial ascent. A written CRT corollary
places any prescribed pair of ascent and surplus budgets inside the exact
marked band in every sufficiently large octave.

[INVERSE_ODD_BUDGET.md](INVERSE_ODD_BUDGET.md) gives the proof and precise
provenance; [InverseOddBudget.lean](lean/InverseOddBudget.lean) proves the
all-word inequality, actual-orbit bridge, and explicit Mersenne family.

This result helps specify a complete merger search: it must sometimes go
beyond the initial ascent or allow an unbounded surplus of odd steps.

## 3. One carry reduction for every complete prefix

An arbitrary complete exponent word, with its terminal gap separated,
gives the exact companion identity

\[
3^s n=2^L+p,\qquad 3\nmid p.
\]

For every signed numerator `p` and denominator exponent `s`, one finite
carry program produces a clock `t` and integer `d`, with

\[
t+|d|+1\le |p|+3^s,\qquad
T^t(n)=2^{L-t}+d\quad\text{when }L\ge t.
\]

The program terminates by a lexicographic order on `(s,|p|)`. It applies
to every dyadic affine companion of the supplied source, including the
existing psi and Hplus queries. Its termination does not assert convergence
of the residual shifted power.

An arbitrary finite signed continuation of length `u`, odd count `a`, and
endpoint `e` gives the exact original-source descent criterion

\[
T^{t+u}(n)<n\quad\Longleftrightarrow\quad
(2^{t+u}-3^{s+a})2^{L-t-u}>3^s e-p,
\qquad t+u\le L.
\]

Zero carries close outright. A carry of minus one has a certified handoff
into a psi query; explicit terminal-grade inequalities allow the whole
accepted prefix language to use PR177's existing multiset replacement
principle. All-state coverage of those handoffs remains unproved.

[TERMINAL_CARRY.md](TERMINAL_CARRY.md) explains the compiler, exact budget,
handoff, and the unbounded family for which descent fails throughout the
entire available binary horizon.
[TerminalCarry.lean](../lean/Collatz/TerminalCarry.lean) is core Lean.

The [final carry closure pass](CARRY_CLOSURE_PASS.md) checks an actual
complete source certificate for which the simple one-step handoff increases
the certificate grade. It then proves the general repair: a clock deficit
`D` can be transferred to the known-source query `3^(D+1)*2^(h-1)` whenever
a supplied ordinary certificate for `3^(D+1)` has every gap below `h`.
The exhibited deficit of two is repaired with the explicit certificate for
27. Universal qualifying certificates and arbitrary signed-carry coverage
remain open.

## 4. Where the full proof is now concentrated

The broader synthesis is in [GLOBAL_SYNTHESIS.md](GLOBAL_SYNTHESIS.md).
It separates three precise global completion targets:

1. A source-preserving compiler supplying a smaller ordinary component
   partner for every unresolved marked source, or complete decreasing
   rules for every certified comparison state.
2. An upper bound on actual marked survivors at unbounded scales, in the
   finite criterion already composed in checkpoint 5.
3. Decay of the complete primitive-source moment, which already includes
   all valuation words and detects cycles as well as divergent orbits.

The new band clock strengthens the quantitative interfaces for these
attacks. The inverse-word theorem and carry normal form expose constraints
the first attack must satisfy. None supplies the still-missing universal
existence or survivor upper estimate.

## Evidence and replay

The [execution report](../../../reports/2026-11-21-lean-global-resolvent/README.md)
keeps compiler logs, source hashes, axiom audits, and the PR source snapshot.
The source survey covers all 143 available PR descriptions and selected
relevant source trees; it is not a claim to have independently verified
every historical proof in the repository.

Use the pinned Lean and Mathlib versions stated in the parent packet. Run
`python3 check.py --help` for the new-module replay. The optional exact
integer replay is `python3 terminal_carry.py --output /tmp/carry-replay.json`.
The unrestricted mathematical claims rest on Lean proofs, not on the finite
Python catalogue.
