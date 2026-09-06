# Gettysburg Research: Collatz

**The Collatz conjecture remains unresolved in this project.** There is no accepted proof, divergent positive orbit, or nontrivial positive cycle here.

We study the shortcut map

$$
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
$$

The goal is to prove that every positive integer reaches 1, or construct and verify a counterexample. The project combines ordinary-integer dynamics, arithmetic and symbolic representations, counting and transfer operators, and proof-producing computation. It is part of the [Agentic Polymath Project](https://github.com/gfreund123/agentic-polymath-project).

## What has been achieved

The strongest surviving results are **structural theorems, complete exclusions of specified constructions, quantitative partial bounds, and exact obstructions to proposed proof methods**. They do not collectively constitute a solution.

| Achievement | Significance and exact boundary | Read next |
|---|---|---|
| Nonnegative ordinary realization is equivalent to eventual stabilization of canonical residues; signed realization also allows an eventually maximal-digit tail. Nested positive survivor sets contain one all-time source exactly when their least elements stay bounded. | Identifies what finite compatibility does not prove. The periodic `1110` construction has positive witnesses at every finite depth but completion `-19/11`, not an ordinary integer. | [Extraction and ghost proofs](research/integrated/README.md#ordinary-realization-and-representation) |
| Every signed ordinary completion is excluded in the corrected 256-transition phase-`-34` construction. | A complete all-directive exclusion for that specified architecture, using its exact stage formulas and Evertse's theorem; not an exclusion of other constructions or Collatz. | [Statement, proof route and dependencies](research/RESULTS_CATALOG.md#corrected-256-stage-ordinary-completion-exclusion) |
| Finite affine/rational self-sections of the specified six-branch chart collapse to its original forward coordinate; semilinear forward-invariant sanctuaries are excluded. Nontrivial ordinary centered itineraries have factor-complexity slope at least `1/log_64(81/64)`. | Complete-tree, full-tail, finite-control and eventual-integrality hypotheses are essential; the original forward section is not excluded. The factor screen requires nonconstancy. | [Rigidity](research/integrated/six-branch-rigidity/README.md) · [Repaired complexity theorem](research/integrated/factor-complexity/README.md) |
| Coefficient-supercritical orbits are classified, periodic realizers have an exact full-denominator formula, and a native Padé argument excludes selected stack contexts of eventual periods 1–9. | These results address different objects: coefficient stopping, physical parity cycles, and stack completions. Neither universal stopping nor all positive cycles are settled. | [Coefficient and cycle results](research/RESULTS_CATALOG.md#coefficient-stopping-and-orbitwise-tails) · [Padé scope](research/RESULTS_CATALOG.md#padé-and-periodic-2-adic-repetition) |
| Native-horizon no-descent starts satisfy `#N(X) <= 6499 + 2 X^(19/20)`, with entropy exponent `h_2(log 2/log 3)`. Proper ranks, complete inverse fans and guarded physical mergers are also available. | Counts are not fixed-floor survivor bounds; safe contraction is not control of unsafe returns; successful infinite certificate families are not a complete cover. | [Mass](research/integrated/exceptional-mass/README.md) · [Transport](research/integrated/renewal-transport/README.md) · [Merging](research/integrated/rank-merging/README.md) |

The [cumulative results catalog](research/RESULTS_CATALOG.md) also includes weighted equidistribution, H-system and quotient-refund constructions, cycle algebra, pulse families, rewriting, regular-language methods and the `5x+1` control system. A result does not cease to count because its proof remains at an earlier source commit. Its inherited review applies only to the stated scope, with subsequent corrections retained.

## What remains unresolved

The [research map](docs/RESEARCH_MAP.md) explains how the approaches relate. Their decisive obstacles differ: a single ordinary all-time source; universal coefficient stopping and complete first-crossing/cycle exclusion; a bound for actual fixed-floor survivors; control of the distribution after unsafe returns; or a complete, terminating lower-rank certificate procedure. These are alternative research programs, not a checklist every proof must complete. The proposed SC*/FC* combined reduction still needs review of its exact formulation.

Useful failures are part of the result: finite-prefix compatibility can give only a completion, orbit sparsity need not imply basin sparsity, arbitrary-subset fiber savings violate mass conservation, and unsafe transport can destroy a finite rank moment. The [research tasks](research/open-obligations/README.md) turn these limits into specific next contributions.

## Read, check, contribute

Start with [scientific status](STATE.md), then choose a [statement and proof](research/integrated/README.md). **A useful first contribution** is to reconstruct the centered nonconstant factor-complexity argument from its three specified dependencies, checking the constant-code and endpoint exceptions; the [task description](research/open-obligations/README.md#centered-dependencies) states the deliverable.

The [research index](research/README.md) separates the integrated baseline from active, unreviewed proposals. Human contributors start at [CONTRIBUTING.md](CONTRIBUTING.md); agents at [AGENTS.md](AGENTS.md). The [phone guide](docs/PHONE.md) offers an additional, explicitly untested end-to-end route.

In a clean complete checkout, `python -X utf8 -B tools/validate.py` checks repository integrity; `--regressions` adds selected bounded replays. [Evidence and replay instructions](docs/REPLAY_POLICY.md) distinguish these from proof review. There is no in-repository Lean build, and external formalizations retain their own evidence limits. [Integration/audit history](archive/README.md) and [public-launch decisions](docs/PUBLIC_RELEASE_GATES.md) are separate from the scientific verdict.
