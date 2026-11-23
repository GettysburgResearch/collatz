# High-variance attacks: complete cycle divisibility and actual source routing

The later [closing-attempt continuation](../closure-round2-20261123/README.md)
adds a common ordinary pressure maximum, full numerical cancellation transport,
and exact original-source pressure-loss accounting. This page preserves the
earlier checkpoint and its original verification scope.

**23 November 2026. Full Collatz remains open.** This checkpoint pursued three
closing mechanisms directly: distinguished-ideal cycle exclusion, unbounded
cheap source surgery, and arithmetic regularity of the actual inverse law.
None yielded universal convergence. The strongest new result is an explicit
all-modulus construction showing that fixed congruence precision, primitivity
and even a quadratic cycle-height threshold can coexist without integrality.
The source attack gives a second all-depth theorem about actual integers.

This continues PR182 at `9dacd610ba7735e89e2e29e4ab01795983317980` after reading
the advanced PR175/176/177/178/180/185 heads. The [source ledger](SOURCES.json)
distinguishes the metadata refresh and targeted proof reading from a full
repository audit. Existing results and their original evidence are retained.

## 1. A full-word construction at every prescribed congruence precision

For a chronological binary shortcut word w of length L and weight P, put

\[
C(w)=\sum_{i=0}^{P-1}2^{d_i}3^{P-1-i},\qquad D(w)=2^L-3^P.
\]

**Constructive written theorem.** For every integer M>=1 coprime to six,
every H>=0, and every prime ell>=5 not dividing M, there is a primitive word
with D>0 and 4L<7P whose positive rational Collatz cycle has every state >H,
while

\[
M\mid C,\quad M\mid D,\qquad \ell\mid D,\quad \ell\nmid C.
\]

The last prime certifies nonintegrality. All chosen tests occur at the correct
evaluation C(w), rather than a norm that mixes conjugates. The theorem concerns
the **specified finite precisions** in M: it does not claim that the complete
valuation v_p(D) passes at primes p dividing M if that valuation is larger than
the prescribed precision.

There is also an infinite height strengthening. For fixed M and ell, let
t=lcm(phi(M),ell-1), with phi(1)=1. Infinitely many of these primitive rational
cycles have

\[
\boxed{\min_i x_i>\frac{L^2}{3888M^2t^2}.}
\]

Their minimum/period ratio is therefore unbounded with the modulus fixed.
This leaves adaptive prime selection or word-dependent precision available;
it refutes the attempted completion using a fixed finite set of precision
tests together with primitivity and a large linear minimum/period ratio.

### The mechanism

Take a balanced word U, close to the critical density log_3(2), and rotate
one occurrence of `10101` to its start. Swap its middle `01` to obtain V.
The complete carry changes by exactly

\[
C(U)-C(V)=2\,3^{p-2}.
\]

Euler/Fermat parameter choices make both block multipliers equal one at the
selected moduli. One of k=1 or k=2 retains a nonzero carry modulo ell. The
whole word U^(kM)V^M then pays M and fails ell. A unique longest spacing
between `00` markers proves primitivity. Cyclic discrepancy below three and
absence of `000` give a lower bound for every rational cycle member. Upper
continued-fraction convergents to log_2(3) amplify the bound quadratically.

[Complete construction and proof](CYCLE_IDEAL.md) ·
[Independent reconstruction and contribution disclosure](../../reports/2026-11-23-high-variance/CYCLE_REVIEW.md).

### Exact controls and their meaning

The checker replays every parity step on the rational cycle, and also on an
explicit positive **ordinary integer realizing the finite word**. The latter
is a finite-prefix witness, not an integer cycle.

| Prescribed M | q | Extra amplification B | Least period L | Rational minimum, floored |
|---:|---:|---:|---:|---:|
| 1 | 306 | 306 | 3,880 | 72,043 |
| 5 | 41 | 41 | 7,800 | 866 |
| 25 | 12 | 1 | 60,000 | 4 |
| 35 | 12 | 1 | 168,000 | 4 |

These complete finite controls passed both normally and under Python -O.
Four damaged controls were rejected in each run. A separate small case
exercised k=2, and an independent reviewer used Fraction arithmetic on
separate controls. None of these executions substitutes for the all-M,
all-H written proof.

## 2. Every fixed inverse-routing clock has actual ordinary obstructions

The source attack sought an unbounded inverse family using only cheaper
gaps, then a route into the literal endpoint cylinder required by the
existing sharp source-ceiling theorem. A uniform bounded routing step fails.

For every natural B, let

\[
q_B=2\,3^{B+2}-1,\qquad
x_i=2^{i+1}3^{B+2-i}-1\quad(0\le i\le B).
\]

Among inverse exponents 1,2,3,4 with positive odd ternary-unit outputs, every
route from q_B through depth B is forced to be this sequence, using exponent
one throughout. Each x_i is 8 mod9 and hence is never 7 mod729. The module
also constructs every such prefix, including one of full depth B.

The initial integer varies with B. This does not construct one infinite
avoiding ordinary orbit, and it does not exclude a root-dependent logarithmic
clock or a route on a suitable restricted family of certified sources.

[Attempt and exact theorem](SOURCE_SURGERY.md) · [Lean proof](ForcedRoute.lean).

## 3. The direct escape attempt and an entropy control

The exact harmonic inverse law retains a summable amount of sibling leakage
along a hypothetical escaping forward ray. The new all-root arithmetic
routing estimates still lose the depth-dependent weight of a specified
ordinary spike. I did not derive the opposing entropy lower bound or
approximation of the canonical escape label that would close this route.

A second attempted shortcut was to infer shift regularity from finite descent
and exact doubling invariance. The standalone control in
[ESCAPE_RIGIDITY.md](ESCAPE_RIGIDITY.md) proves that some sequences satisfying
b(2n)=b(n) exactly have the fair Bernoulli consecutive-word frequencies.
It assigns independent bits to odd parts and proves the required variance
bound and almost-sure normality. These sequences are not claimed to satisfy
the odd Collatz equation. The control prevents that specific entropy
inference without resolving the actual arithmetic regularity problem.

## 4. Formalization and reproduction

There are **24 new public Lean statements in two modules**, including their
supporting lemmas. These are not 24 independent discoveries.

| Module | Kernel-checked scope |
|---|---|
| [CycleWordAlgebra.lean](CycleWordAlgebra.lean), 12 statements | Chronological complete carries; arbitrary-context adjacent swap; repeated and mixed-block quotient identities; complete denominator payment; the two-choice surviving carry. |
| [ForcedRoute.lean](ForcedRoute.lean), 12 statements | Exact unit-edge classification, actual ordinary state formulas, prefix existence, uniqueness of any supplied route, and the all-B avoidance theorem. |

The full balanced-word cycle construction, primitivity, real height bounds,
continued-fraction subsequence and normal-label control remain written
mathematics with scoped internal reconstruction reviews. No convergence,
analytic or Diophantine premise is installed as a Lean axiom.

```sh
python -X utf8 -B research/high-variance-20261123/replay.py \
  --mathlib /path/to/mathlib-at-d13f23b723b8a846827a245b89c10fc7d3f11612 \
  --lean-bin /path/to/lean-4.34.1/bin --out /empty/external/output
python -X utf8 -B research/high-variance-20261123/cycle_ideal_control.py
python -X utf8 -B -O research/high-variance-20261123/cycle_ideal_control.py
python -X utf8 -B tools/validate.py --receipt /external/repository-receipt.json
```

Fresh proof outputs and all-declaration axiom audits, exact controls, reviews,
source bindings and actual checkout evidence are in the
[execution report](../../reports/2026-11-23-high-variance/README.md).
The repository validator checks integrity separately from mathematical proof.

The missing steps remain successful original-target source descent, a
same-source arithmetic estimate eliminating escape, or an adaptive
complete-denominator obstruction for every nontrivial integer cycle word.
No one of those conclusions was obtained in this pass.
