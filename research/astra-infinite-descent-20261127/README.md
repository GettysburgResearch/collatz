# Actual ordinary sources, complete denominators, and prescribed clocks

**Collatz remains OPEN.** This branch contains formal reciprocal-mass
and bounded-orbit equivalences, unconditional ordinary first-hit
constructions, written sparse inverse counts, and complete-denominator
results and counterexamples. New written results give a uniform
first-arrival source cutoff and a dyadic mean bound for the original
stopped-trace rate statistic. It does not prove universal convergence or
exclude all nontrivial cycles.

The working map is the shortcut Collatz map, halving even inputs and
taking odd inputs to \((3n+1)/2\). An odd departure count and a shortcut
clock are kept separate throughout. Source inputs are positive ordinary
integers whenever an ordinary conclusion is stated.

## Read the mathematical results

| Packet | Main contribution | Evidence and remaining boundary |
| --- | --- | --- |
| [Finite reciprocal mass](root/README.md) | Completes PR201's written converse in Lean. The full Collatz statement is equivalent to arbitrarily small explicit finite reciprocal-prefix sums. Supplies a finite hit-budget transfer, a sharper post-hit clock, a monotone actual potential, and a formal obstruction to bootstrapping solely from the birth reserve. | All displayed finite identities, bounds, and the equivalence are in Lean. The universal small-mass estimate is open. |
| [Prescribed merger clocks](merger/README.md) | Arbitrary finite additive patterns in every sufficiently large relative interval, simultaneously in every class of any prescribed source modulus, with common first-hit clock, equal bounded odd count, independently prescribed residues of both, and fixed additive clock overhead. Also gives every sufficiently large exact clock. | `MarkedProgressions.all_residues` and `AllProgressions.all_clocks` are unconditional Lean theorems. Sparse-counting extensions are written separately. The selected ordinary sources vary with the requested window and pattern. |
| [Complete cycle denominators](cycles/README.md) | Full-denominator restrictions in sparse and powered families, moving-reference arc bounds, and a complete spectral description of denominator growth near one odd octave, including the sharp leading minimum at each clock gcd. Primitive positive rational examples attain the permitted rates. | Finite carry, Fourier, pulse, arc-height, native inversion and clock-floor kernels are in Lean. Infinite Diophantine conclusions and the sharp constructions are written, using the identified two-logarithm input. The constructed cycles have denominator greater than one. |
| [Source-cone meetings and sparse inverse counts](escape/README.md) | Finite dyadic-boundary budgets, exact fixed-grade clock polynomials, and a sparse inverse local limit. An independent written square-root synchronization proof gives a uniform first-row source cutoff and a dyadic mean bound on the original all-visit stopped-trace statistic. | Finite integer flux and first-hit transport are in Lean. The full stochastic and all-visit variation arguments are written proofs. The separate compact correction-set and local-limit arguments retain their identified analytic inputs. The trace estimate remains polynomial, while the convergence criterion asks for exponential decay. |

These packets are intended to be read with their failed strengthenings.
In particular, residue coverage, dense inverse families, many coalescing
pairs, a complete denominator theorem on a restricted word family, and a
small average each have different quantifiers from descent at every
supplied source.

## The unconditional finite-pattern theorem

Fix a finite set of nonnegative offsets \(F\) containing zero, positive
moduli \(m,M,Q\), and a relative width \(\delta>0\). There are constants
\(C,K>0\) and an integer \(G\) such that, for every positive target
\(y\) prime to three, every \(X\ge Cy\), and every pair of requested
residues \(t\bmod M\), \(a_0\bmod Q\), one ordinary certificate has
the following properties:

- For every source residue \(c\bmod m\), there is a positive base
  \(x_c\equiv c\pmod m\) whose entire pattern \(x_c+F\) lies in
  \([X,(1+\delta)X]\). The bases lie in a common block of length \(m\).
- Every member of every selected pattern first reaches \(y\) at the
  same shortcut clock \(D\), with the same odd-departure count \(a\le G\).
- \(D\equiv t\pmod M\) and \(a\equiv a_0\pmod Q\).
- \(2^D y\le KX\), equivalently
  \(D\le\log_2(X/y)+\log_2 K\).

The lower clock bound \(D\ge\log_2(X/y)\) follows from
\(T(n)\ge n/2\). The upper bound gives a fixed additive overhead
above the absolute halving bound. The proof combines a finite
coalescence of affine profiles, the actual integer two-gap router,
an off-orbit first-arrival leg, a positive inverse ladder, and a finite
phase cover retaining both residue constraints. The final theorem is
[MarkedProgressions.lean](merger/MarkedProgressions.lean).
[FastPairs.lean](merger/FastPairs.lean) retains the earlier pair theorem
and its signatures. The constructive route and quantifier boundary are
explained in [FINITE_BLOCKS.md](merger/FINITE_BLOCKS.md).

The [independent integer certificates](root/README.md#a-separate-constructive-phase-theorem-and-exact-examples)
literally replay four large pairs. A separate
[finite block certificate](merger/FINITE_BLOCK_1024.json) replays 1,024
consecutive positive integers, all first reaching 1 after exactly 1,903
shortcut steps with 930 odd departures. None of these existence results
settles an arbitrary supplied source. The profile engine also proves that
no positive integer synchronizes at the same clock with all its additive
translates: its doubled value already prevents that conclusion.

For a separate preassigned family, [FixedMersenneRows.lean](merger/FixedMersenneRows.lean)
completes all **192** canonical-return cases in PR206's table. With
\(m=12\cdot2^{18k}-1\) and \(z=(2^{m+7}-271)/81\), each specified
\(1\le k\le192\) has a smaller positive \(Y\equiv17\pmod{48}\)
that meets \(z\), while \(3Y\) reaches 1 in exactly three odd
departures at a clock at most \(m\). Nine new exact modular certificates
complete the earlier 183 cases. The proof retains the actual ordinary
source and checks the lift in Lean; it does not prove that \(Y\) or
\(z\) itself reaches 1. The
[case table and scope](merger/FIXED_MERSENNE.md) distinguish this finite
result from the still-open statement for every positive parameter.

## The remaining universal step

There is now an unconditional formal criterion specifically for escape.
Let \(A_{m,d}(y)\) be the complete finite set of positive ordinary starts
whose first visit to an odd target \(y\) occurs at shortcut clock \(m\)
with exactly \(d\) odd departures. Then

\[
 \text{every positive ordinary orbit is bounded}
 \quad\Longleftrightarrow\quad
 \lim_{\substack{y\to\infty\\y\text{ odd}}}
 \sup_{m,d}\frac{3^d}{2^m y}\,|A_{m,d}(y)|=0.
\]

The precise epsilon formulation, complete finite row definition, and
both implications are in
[TargetExtinction.lean](escape/TargetExtinction.lean). Elementary parity
counting bounds the number of small vertices on any simple physical
trajectory. Finite reciprocal bands then give a uniform first-arrival
mark floor and show that a heavy high-target row must visit a small
integer. This proof has no external analytic premise. It does not prove
the displayed vanishing limit, and boundedness alone leaves nontrivial
cycles to exclude. [HIGH_TARGET_ROWS.md](escape/HIGH_TARGET_ROWS.md)

The new affine classification in
[AffineClassification.lean](merger/AffineClassification.lean) proves
that finite positive affine families admit the full marked relative-window
placement precisely when their slopes share the same prime-to-six part.
PR146 already contains the basic written classification; this packet
formalizes it and strengthens the placement and first-arrival controls.
Separately, [FiveWindow.lean](merger/FiveWindow.lean) constructs genuine
joint first arrivals from \(x,5x\) to \(y,5y\), with the same bounded odd
count, near-minimum common clock, and independent prescribed clock and
grade residues in every sufficiently large relative window.

There is also a grade-indexed formal boundedness criterion:

\[
 \text{every positive ordinary orbit is bounded}
 \quad\Longleftrightarrow\quad
 \lim_{d\to\infty}\sup_{m,\,y>0}
 \frac{3^d}{2^m y}\sum_{z\in A_{m,d}(y)}\frac1z=0.
\]

[DampedRows.lean](root/DampedRows.lean) proves both directions and the
uniform reciprocal-source tail \(1/(R+1)\). The remaining limit is a
universal assertion about actual first-arrival rows.

The formal reciprocal-mass equivalence still requires its universal
small-mass estimate. The new first-arrival construction provides chosen
sources in every sufficiently large interval; it does not select a
descent certificate for every supplied integer.

The [finite octave flux argument](escape/CLOCK_ANTICONCENTRATION.md)
and [scalar return proof](escape/SCALAR_RETURN_PROOF.md) now give the
uniform source cutoff directly: starts above \(R\) contribute at most
\(C/\sqrt{\log R}\) to every normalized exact first-arrival row,
uniformly in the target, clock, and grade. This removes the previous
external analytic premise for that upper bound. It does not prove
nullity of the global compact correction set in the separate
[fair-clock compactness argument](escape/FAIR_CLOCK_DIFFUSION.md).
The limiting maximum row mass is still positive if an escaping orbit
exists, and a finite synchronized escaping class attains it. Excluding
such a class remains necessary.

The same transport, applied to the exact all-visit law and its original
period-six source selector, gives the written estimate
\(\sum_{D\le j<2D}Q_j^*=O(\sqrt D)\). The
[original-trace argument](escape/ORIGINAL_TRACE_VARIATION.md) retains
recurrent visits, takes targetwise positive parts before summing, and
controls every omitted source and target. It supplies arbitrarily large
grades with \(Q_j^*=O(j^{-1/2})\). PR193's full-convergence criterion
requires a bound of the form \(O(j^A(2/3)^j)\) on an unbounded sequence;
that estimate remains open.

The [spectral cycle theorem](cycles/SPECTRAL_NEAR_OCTAVE.md) treats a
specified physical regime: least odd value at least \(h^{2-o(1)}\) and
odd-value ratio at most \(2+h^{-1+o(1)}\). It identifies the full
denominator rate in that regime, including changing clock gcds. It does
not place every hypothetical integer cycle in that regime or establish
an all-family denominator exclusion.

## Prior work and reproducibility

The intake freezes main at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` and inventories the open and
closed pull requests available at the start of the pass. Its evidence
levels distinguish full argument reconstruction, a selected-file read,
and a PR-description inspection. The new work sits on an isolated branch;
it does not merge or rewrite the existing research PRs.

- [Source intake and review scope](../../reports/astra-infinite-descent-20261127/SOURCE_INTAKE.md)
- [Pinned imported Lean sources](imports/pr201/SOURCES.json)
- [Portable strict Lean rebuild](replay_lean.py)

Use Lean **4.34.1**, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and a built Mathlib checkout at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Run from any working directory:

```bash
python research/astra-infinite-descent-20261127/replay_lean.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib4 \
  --receipt /absolute/path/outside/the/checkout/lean-replay.json
```

The script verifies the dependency revisions and clean tracked source
state, creates a fresh object directory, builds the local import graph
with warnings as errors, and audits every declaration originating in the
packet's Lean modules, including private and generated declarations.
It rejects any transitive axiom outside `propext`, `Classical.choice`, and
`Quot.sound`. It does not rebuild the whole Mathlib library or turn an
explicit hypothesis into a proved theorem.

Repository integrity is a separate check, run in a clean complete
checkout with `python -X utf8 -B tools/validate.py`. Exact validation and
source-review receipts belong in the reports directory. Counts and source
hashes report what was actually run; they are not a proof of the written
infinite arguments.
