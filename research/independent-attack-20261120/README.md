# Four powered factors: finiteness when the minimum lies in a descending cube

**Status: PROPOSED, source-qualified, ineffective.** The Collatz conjecture
remains open. This packet gives a new written finiteness argument for a
specified class of primitive positive cycles. It does not eliminate an
individual member of that class or provide a period cutoff.

## Claim CUBE-4

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

There are only finitely many primitive positive ordinary cycles whose
cyclic parity word admits a complete factorization into **four** nonempty
word powers, each of exponent at least two, such that the global least
phase lies in a factor of exponent **three**.

The roots, their lengths, and the three other exponents are unrestricted.
The factors cover exactly one primitive tour; no uncovered gaps are
allowed in the statement proved here. A minimum in an increasing power
already gives an effective length inequality. The substantial case is a
minimum in the last copy of a decreasing cube.

The proof has two finite components:

* With two increasing factors, both must be squares in any unbounded
  family. The other decreasing factor has total homogeneous logarithmic
  drop less than `0.327` times the cube's exit height. A transported
  two-coordinate comparison has a strict margin greater than `1/5`.
* With three increasing factors, seven rational three-dimensional
  polytopes are covered by comparisons of two or three coordinates.
  Exponents above two are handled by an upper gain bound at exponent
  three; their integer multipliers never become comparison coordinates.

The arithmetic certificate checks those seven regions exactly, retains
an explicit **square-descent** cone point that the method does not
exclude, and independently replays 378 ordinary powered-word segments.

## Relation to the preceding work

The frozen input is PR #145 at
`dd245a712f985909f541590e3f6c179b7ba011e4`:

* [Four-factor conclusions in THREE_POWER_COVERAGE.md](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/synchronized-cycle-blocks/THREE_POWER_COVERAGE.md)
  leave a minimum-containing descending square or cube in an unbounded
  family of four-power covers. They exclude quartic and quintic descents
  using transported comparisons.
* [THREE_POWER_FINITENESS.md](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/synchronized-cycle-blocks/THREE_POWER_FINITENESS.md)
  treats three factors and develops the fixed-form transport method.
* [PRIOR_WORK.md](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/synchronized-cycle-blocks/PRIOR_WORK.md)
  credits the powered-block brackets and height argument to Fourier
  Wren's paper 57 and distinguishes other notions of block complexity.

The new ingredient here is transport to the **leading monomial of the
descending cube**, combined with comparisons between rising squares.
This supplies the missing cubic case for exact four-factor covers.
Combining CUBE-4 with the separately source-qualified earlier four-factor
classification leaves a descending **square** at the minimum in every
sufficiently long exact four-factor cover. That combination inherits the
earlier proof's review boundary. We do not extend its sparse-gap version
in this packet.

## Proof, evidence, and remaining obstacle

Read [PROOF.md](PROOF.md) for all normalizations, the fixed-form comparison
lemma, the two-rise estimate, and the seven-cone reduction. Its only
external analytic inputs are a polynomial bound for the least phase
from a logarithmic-form estimate, and the rational p-adic Subspace
Theorem. Both are identified there. The latter makes the conclusion
ineffective. No stationary-policy theorem or unproved Collatz bridge is
used.

Run:

```sh
python -X utf8 -B research/independent-attack-20261120/check_cubic_descent.py
```

The exact checker covers seven cones in 308 recursion nodes. The
all-nonsquare domain is empty. These are certificates of elementary
rational inequalities, not a formal verification of the analytic proof.
See [CHECKS.md](CHECKS.md) for the recorded output and scope.

The first unproved strengthening is finiteness, or an effective
exclusion, of arbitrary exact four-factor covers whose least phase lies
in a descending **square**. The checker preserves the feasible abstract
point `g=(1/2,1/2,1)` for three rising squares and a descending square;
every comparison used here fails there. It is a counterexample to
coverage by these inequalities, not an ordinary Collatz cycle. Cycles
requiring more factors and nonperiodic divergent trajectories remain
outside the result.
