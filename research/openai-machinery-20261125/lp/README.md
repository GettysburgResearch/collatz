# Linear programming: exact certificates, common scales, and a failed finite ansatz

**Status.** The five declarations in [PotentialBridge.lean](../formal/PotentialBridge.lean) are compiled mathematical interfaces to the byte-identical OpenAI Farkas implementation. The general strongly polynomial algorithm is **source-qualified**, not implemented or rebuilt here. No potential for every ordinary Collatz source has been found.

## What the new result says

Family 380 contains *Strongly polynomial linear programming* and *Superpolynomial graph diameter of simple polytopes*. The release is pinned at `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`. The LP manuscript claims a deterministic algorithm with an arithmetic-operation count polynomial in the numbers of variables and constraints, independently of the magnitudes of the coefficients. For rational input it additionally bounds intermediate bit lengths polynomially in the input bit length. The accompanying Lean scope covers rational feasibility and optimization with an actual fixed RAM-program model, including feasible, infeasible, optimal and unbounded outputs. Its existence theorem is `OAI.Optimization.LinearProgramming.strongly_polynomial_optimization`; the Comparator file is a challenge and is not an implementation.

The manuscript extends its method to monotone complementarity, convex quadratic optimization and games. A deterministic mean-payoff game can encode the search for a policy and a potential. These are finite explicitly given systems. The paper explicitly distinguishes a polyhedron supplied by a separation oracle; its main bound is not automatically a bound for an infinite family of source-dependent Collatz inequalities.

[LP manuscript](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Strongly-polynomial-linear-programming-November-24-2026/paper.pdf) · [formalization scope](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/380.md) · [actual solution entrypoint](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Optimization/LinearProgramming/Optimization.lean)

## The interesting proof mechanisms

**Certificates before numerical solutions.** For feasibility of `Ax ≤ b`, form the subspace of homogenized slacks `(αb−Ax, α)`. A nonnegative vector with positive last coordinate supplies a feasible point. In its orthogonal complement, the corresponding vector supplies a Farkas certificate. Each coordinate has one of these two sides. The algorithm learns the side and a minimal support; ordinary linear algebra recovers the exact witness on that support. A very small but indispensable coordinate is the principal numerical obstacle.

**Extremal information can suffice.** Reciprocal coordinate prices scale the primal and dual spaces while preserving orthogonality. A label oracle need only be correct on a coordinate where a hidden circuit's scaled entry is largest. The extremal-price theorem learns consistent demands from such labels. The proof first uses a conceptual wealth-weighted population of experts, then implements it with small groups of slots and recursive threshold feedback. A child whose surpluses have all fallen below a threshold gives useful feedback simultaneously on every parent slot above that threshold. The return of unused wealth pays for recursive calls. This is much more specific than assuming a uniformly correct label oracle.

**One common calibration, including unseen constraints.** Pivot selection and minimal-support circuits are governed by the same matrix minors. Short proxies for their logarithms preserve signs of bounded integer affine forms. Projection through Farkas multipliers proves that all comparisons at a query can be lifted to **one** reciprocal scaling of the original matrix. An unrelated good scaling for each pivot would not suffice. The demand assignment is also common throughout an uninterrupted query history.

**A double-exponential counting argument bounds restarts.** If `D` minor logarithms have subset sums separated by more than two, their `2^D` subset products are separated by a factor greater than two. Every subset sum of those products is therefore distinct, giving `2^(2^D)` different polynomial values at the input matrix. But the products have bounded degree and integer coefficient size in only finitely many matrix entries. Counting those polynomials bounds `D` in terms of the dimension. Failed compression requests enlarge such a separated set, so they cannot occur indefinitely. This resembles a possible amortized resource argument; it does not provide one for Collatz until a fixed finite algebra of retained-source observables and degree/coefficient bounds are supplied.

**Strict signs must survive compression.** The projection lemma deals with weak and strict inequalities by introducing a common positive margin. Its multipliers have bounded support and controlled integer size. An approximate numerical solution that loses a zero or a strict margin can select the wrong certificate. That is why this packet checks exact integer certificates after search.

[Proof overview](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Strongly-polynomial-linear-programming-November-24-2026/build/overview.tex) · [common calibration](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Strongly-polynomial-linear-programming-November-24-2026/build/calibration.tex) · [compression and dissociation](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Strongly-polynomial-linear-programming-November-24-2026/build/compression.tex)

## A connected certificate harness

Take a finite directed graph, with source `s(e)`, target `t(e)` and rational cost `c(e)`. We seek a correction `p` satisfying

```math
p(t(e))-p(s(e))\le -c(e)\quad\text{for every edge }e.
```

The matrix row for an edge is the target unit vector minus the source unit vector. The directly imported Farkas theorem gives exactly two alternatives: a potential, or a nonnegative multiplier `y` with zero net flow at every vertex and positive total cost. A multiplier supported on a cycle is the simplest example. The normalized sparse alternative has `c·y=1` and support at most `rank(A)+1`.

The bridge proves the matrix/edge equivalence, the soundness of an obstruction, and the sparse alternative. The [Python harness](certificates.py) implements the difference-constraint specialization using Bellman–Ford. It does **not** claim to implement the new general LP algorithm. Every returned potential is checked against every supplied row; every obstruction is checked for exact nonnegativity, balance and positive cost. Source annotations are independently replayed under the ordinary odd Collatz map.

The cost used in the controls is `c=8−5g`, where `g=v₂(3n+1)`. The margin `8/5>log₂3` is certified by `2^8>3^5`. If a finite graph faithfully covered an entire orbit and admitted this potential, summing the inequalities would force its cumulative clock above `(8/5)k` up to a bounded endpoint term. That would eventually pass PR206's clock crossing. **The faithful global graph and potential are the missing objects.** A successful certificate on a single convergent path is only a control for the checker.

## A universal obstruction to the residue-only version

For any modulus `m≥1`, take the ordinary positive integers

```math
n=4m-1,\qquad y=6m-1.
```

They are odd, `3n+1=2y`, and both have residue `m−1` modulo `m`. Thus this genuine step has `g=1`, positive cost three, and identical source and target in the residue graph. Any potential depending only on that residue would have to satisfy `0≤−3`. This proof is formalized using the repo's actual shortcut map. When `m` is a multiple of three, both values are also ternary units.

For any finite horizon `H≥1` and modulus `m`,

```math
n_0=2^{H+1}m-1,\qquad
n_i=3^i2^{H+1-i}m-1\quad(0\le i\le H)
```

is an ordinary path of `H` consecutive gap-one steps, all with residue `−1 mod m`, and `n_H>n_0`. Replacing the multiplier `m` in this formula by `3mL` retains that residue modulo the original `m`, makes both arms ternary units, and moves the entire witness above any supplied floor as the positive integer `L` grows. This excludes a fixed-horizon repair that still uses only the residue correction. The witness changes with `H`; it does not produce one infinite positive orbit. An adaptive stopping time, an unbounded arithmetic counter, or inequalities proved specifically on a retained counterexample set are different architectures.

The exact finite runs at moduli 6, 18, 54, 162 and 486 find positive-circulation certificates. Some selected circulations use edges coming from different ordinary sources. They disprove a universally required **potential ansatz**, since that ansatz must obey both inequalities. They do not represent an ordinary Collatz cycle: equating residues does not equate the integers. Three convergent paths supply positive controls; fifteen deliberately corrupted certificates and five inexact-type or misprojected-edge controls are rejected in both ordinary and optimized Python modes. The empty graph returns the vacuous potential.

## Where the new machinery might still matter

The useful near-term application is symbolic certificate synthesis for a specified source family. Retain the full affine source, its congruence conditions and the actual endpoint. Derive inequalities that hold on the entire progression, search for rational weights, and export the exact certificate. The target could be PR197's strict `2^40` contraction or PR192's lower smooth base. A failure certificate then identifies which proposed transitions or cost assignment prevent the proof, rather than merely returning a solver failure.

A more ambitious application would imitate the common-calibration argument: maintain one finite set of retained-source observables whose scales cover all later queried inequalities, and charge every failed compression to an enlargement of a bounded dissociated set. The unresolved requirement is a dimension and degree bound independent of the clock. Arbitrarily many new carry variables or fresh source labels invalidate that bound. A finite constraint solve cannot replace this theorem.

Finally, the companion polytope result is a useful warning about proof architecture. Fast global optimization need not mean that a prescribed local edge-following process takes few steps: the same release claims superpolynomial graph diameters. Likewise, an efficient search for some merger certificate need not force the actual deterministic Collatz orbit to visit its domain. This is an analogy about quantifiers, not an application of the polytope theorem to Collatz.

## Reproduce

From the repository root:

```bash
python -B research/openai-machinery-20261125/lp/certificates.py
python -O -B research/openai-machinery-20261125/lp/certificates.py
```

The unified [formal project](../formal/README.md) builds the directly imported modules and prints axiom dependencies. No custom Collatz axiom or placeholder proves a missing coverage premise.
