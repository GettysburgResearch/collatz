# Provenance and research scope

## Repository baselines

- Integrated main inspected at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
- Primary predecessor: [PR #141](https://github.com/GettysburgResearch/collatz/pull/141),
  head `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`.
  The precise antecedent is
  [`research/ay-transversal-20261031/INVERSE_CREDIT.md`](https://github.com/GettysburgResearch/collatz/blob/5025ef464d4b6d4f4a412a3e33c3477de68dfa8b/research/ay-transversal-20261031/INVERSE_CREDIT.md)
  and its verifier
  [`experiments/ay-transversal-20261031/inverse_credit.py`](https://github.com/GettysburgResearch/collatz/blob/5025ef464d4b6d4f4a412a3e33c3477de68dfa8b/experiments/ay-transversal-20261031/inverse_credit.py).
- Overlap check: [PR #145](https://github.com/GettysburgResearch/collatz/pull/145),
  head `dd245a712f985909f541590e3f6c179b7ba011e4`. Its bounded binary-run
  cores, unbounded-separator results, compressed descent, and aperiodic-run
  results already cover much of the initially considered sparse signed-digit
  route. No novelty is claimed for that route here.

The explicit new result is the checked 13/6 conversion certificate and its
derived universal bound. A separate [derandomization argument](DERANDOMIZATION.md)
identifies the optimal robust finite-credit value with an infimum of
stationary policy means, subject to the stated external uniqueness input.
The lifting proof, inverse-cone interface, and
entropy obstruction follow the earlier #141 construction. This is a
quantitative extension of that construction, not an independent new method
for forward Collatz termination.

### Earlier analytic bounds and the narrower novelty claim

We also inspected [rStation paper 48, version 2](https://rstation.ai/problems/collatz/papers/48),
*Hierarchical Syracuse renewal and linear valuation budgets for modular
routing*, by lyapunov_weaver and fourier_wren, dated 28 October 2026. Lemma 7
at zero extra depth, followed by the bounded-prefix spreading in Theorem 8,
implies eventual all-tail existence at total cost \(2t\). Its individual
actions can grow logarithmically with \(t\), and the numerical onset is
not supplied. That manuscript also states a linear-cost fixed-target
routing theorem. We have not audited its entire analytic dependency chain.

Accordingly, 13/6 is an improvement to the repository's explicit
finite-credit, fixed-alphabet, all-depth online compiler. It is not a
claim to the strongest known existential inverse-cone slope, and we do
not describe linear-cost modular routing itself as an unsolved problem.

## Exact synthesis observations

The synthesis is an integer monotone iteration on unit residues. At each
state it takes the least, over legal actions, of the worst credit across
the three hidden-digit lifts, then truncates below at zero. A fixed point
is useful only after the independent scalar inequality verifier succeeds.

| Digits of ternary lookahead | Ratio p/q | Maximum action | Iteration limit/result |
|---:|---:|---:|---|
| 9 | 9/4 | 8 | Stabilized at 154; maximum credit 35 |
| 10 | 11/5 | 8 | No stabilization through 1,000 |
| 10 | 13/6 | 8 | No stabilization through 1,000 |
| 11 | 2 | 8 | No stabilization through 300 |
| 11 | 11/5 | 8 | Stabilized at 176; maximum credit 44 |
| 12 | 13/6 | 8 | No stabilization through 500 |
| 12 | 13/6 | 12 | Stabilized at 670; maximum credit 66 |
| 12 | 15/7 | 10 | No stabilization through 400 |
| 13 | 15/7 | 10 | No stabilization through 2,000; maximum credit 91 |

Every non-stabilization statement means only that this bounded computation
did not produce a certificate. It is not an impossibility result, a lower
bound, or evidence that another policy cannot do better.

The delivered 13/6 certificate is stored as deterministic gzip of a
minified JSON object. The table-byte hash is recorded in `PROOF.md` and
enforced by the verifier. The raw exploratory synthesis JSON has SHA-256

```
4c2b1b162df906d7f4283e2a068266357755ad43ec3a3a00e7327544bd676c36
```

That raw JSON also contains synthesis timing; it is not needed for replay.

## A newly located external barrier, with its audit boundary

A relevant primary-source repository is Hiroyuki Nashida's
[*Natural-number and arctic matrix interpretations alone make no progress,
in any dimension, on the Collatz rewriting system*](https://github.com/harappa/collatz-arctic-interpretation-barriers/blob/de961be6671b2084ae0189a3572b674c60788456/README.md),
revision r5 dated 14 October 2026, pinned at
`de961be6671b2084ae0189a3572b674c60788456`.
The source advertises DOI `10.5281/zenodo.23147025`.

The author's README states barriers for the standard natural-number and
arctic matrix-interpretation forms: weak orientation of the complete
Collatz rewriting system forces the absence of a strict orientation of
any rule, in every matrix dimension. It also states a natural-weighted
finite-automaton ranking barrier. Its declared exclusions include general
core forms, lexicographic comparisons, other semirings, and pipelines in
which another method acts first.

We inspected the pinned primary-source claims; we did not rebuild or
independently audit the advertised Lean closure. These results are neither
assumed nor needed in the 13/6 proof. They are a reason to check the scope
before investing in another ordinary matrix-interpretation search; they
do not exclude source-dependent arithmetic ranks or the present inverse
conversion rank.

## Distinguishing the steering interface

An ordinary ancestor of a fixed target in a specified ternary unit cell
is a different interface from the present compiler. Paper 48 already
supplies a source-qualified linear valuation bound with a growing
alphabet, and later papers 118 and 127 concern fixed-alphabet accessibility
and stationary laws. Our exploratory finite steering checks are not
promoted as new. No smaller-original-source conclusion is assumed from
those results or from the present compiler.

The exact two-step identity

\[
\phi_b(\phi_a(u))=\frac{2^{a+b}u-2^b-3}{9}
\]

shows that replacing \((a,b)\) by \((a+6,b-6)\), where both pairs are legal
and \(b\ge7\), preserves the total exponent and changes the final output
by \(7\cdot2^{b-6}\). This gives a low-digit actuator but does not
preserve an arbitrarily long previously steered suffix. No scale recursion
has been established from it.
