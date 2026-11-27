# Actual ordinary sources, complete denominators, and prescribed clocks

**Collatz remains OPEN.** This branch contains a formal completion of an
existing equivalence, unconditional ordinary first-hit constructions,
written sparse inverse counts, and complete-denominator results and
counterexamples. It does not prove universal convergence or
exclude all nontrivial cycles.

The working map is the shortcut Collatz map, halving even inputs and
taking odd inputs to \((3n+1)/2\). An odd departure count and a shortcut
clock are kept separate throughout. Source inputs are positive ordinary
integers whenever an ordinary conclusion is stated.

## Read the mathematical results

| Packet | Main contribution | Evidence and remaining boundary |
| --- | --- | --- |
| [Finite reciprocal mass](root/README.md) | Completes PR201's written converse in Lean. The full Collatz statement is equivalent to arbitrarily small explicit finite reciprocal-prefix sums. Supplies a finite hit-budget transfer, a sharper post-hit clock, a monotone actual potential, and a formal obstruction to bootstrapping solely from the birth reserve. | All displayed finite identities, bounds, and the equivalence are in Lean. The universal small-mass estimate is open. |
| [Prescribed merger clocks](merger/README.md) | Positive first-hit pairs with any fixed gap and ternary source class in every sufficiently large relative interval, uniformly over all ternary-unit targets, with a fixed additive clock overhead. Also provides every sufficiently large prescribed exact clock. | `FastPairs.fast_pairs` is unconditional Lean mathematics. Finite-pattern, arbitrary-progression and sharp sparse-counting extensions are written proofs with separate status. Sources vary with the window. |
| [Complete cycle denominators](cycles/README.md) | Full-denominator restrictions in sparse and powered families, moving-reference arc bounds, and explicit primitive positive rational cycles with subexponential complete denominators and odd amplitude arbitrarily close to one octave. | Finite carry, Fourier, pulse, arc-height and clock-floor kernels are in Lean. Infinite Diophantine conclusions and the counterfamily are written. The counterfamily has denominator greater than one; it is not an integer Collatz cycle. |
| [Source-cone meetings and sparse inverse counts](escape/README.md) | Finite dyadic-boundary budgets and asynchronous guards; unconditional ordinary window visitors; exact fixed-grade clock polynomials plus periodic corrections; a sparse pointwise inverse local limit with first-hit and physical-location consequences. | Finite ordinary kernels and window visitors are in Lean. Analytic local limits have independent written reviews and a restricted sparse parameter range. No fair-law or universal forward-source estimate is inferred. |

These packets are intended to be read with their failed strengthenings.
In particular, residue coverage, dense inverse families, many coalescing
pairs, a complete denominator theorem on a restricted word family, and a
small average each have different quantifiers from descent at every
supplied source.

## The unconditional first-hit pair theorem

Fix a nonnegative gap \(d\), a ternary precision \(s\), and a relative
width \(\delta>0\). There are constants \(C,K>0\) and an integer \(G\)
such that, for every positive target \(y\) prime to three, every
\(X\ge Cy\), and every source class \(c\bmod3^s\), one positive
ordinary integer \(x\) satisfies all of the following:

- \(x\equiv c\pmod{3^s}\), and both \(x,x+d\) lie in
  \([X,(1+\delta)X]\).
- Both starts first reach \(y\) at the same shortcut clock \(D\),
  with the same odd-departure count, at most \(G\).
- \(2^D y\le KX\), equivalently
  \(D\le\log_2(X/y)+\log_2 K\).

The lower clock bound \(D\ge\log_2(X/y)\) follows from
\(T(n)\ge n/2\). The upper bound thus gives a fixed additive overhead
above the absolute halving bound. The proof combines the actual integer
two-gap router, an off-orbit first-arrival leg, a positive inverse ladder,
and an unconditional finite phase cover. The complete theorem is
[FastPairs.lean](merger/FastPairs.lean); its constructive route and
quantifier boundary are explained in
[FAST_FIRST_HIT_PAIRS.md](merger/FAST_FIRST_HIT_PAIRS.md).

The [independent integer certificates](root/README.md#a-separate-constructive-phase-theorem-and-exact-examples)
literally replay four large pairs. The source choice is existential in
every window, so the theorem does not settle an arbitrary supplied source.

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
