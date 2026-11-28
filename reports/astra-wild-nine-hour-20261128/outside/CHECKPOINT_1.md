# Forward-time congruences and rational atoms

**PROPOSED research.** The elementary finite block estimate gives a simultaneous bound for the complete set of centers that reach one within a supplied number of shortcut ticks. The time-density consequences use only this estimate and the ordinary product formula for an escaping orbit. The stationary-law theorem uses Poincaré recurrence, the exact affine word and elementary orders of units at odd prime powers. At an uncanceled cycle-denominator prime it determines the conditional distribution of the deep digits. The separate unrestricted affine approximation rate is from Javaheri's written Theorem 3.8. Its contribution stops short of the required integer denominator precision.

- [Short ordinary predecessors and the simultaneous cofactor bounds](../../../research/astra-wild-nine-hour-20261128/outside/CONGRUENCES_TO_SHORT_PREDECESSORS.md)
- [Atoms, rational cycles and exact denominator-prime distributions](../../../research/astra-wild-nine-hour-20261128/outside/ATOMS_OF_ORDINARY_TIME_AVERAGES.md)
- [The real approximation theorem and strict integer threshold](../../../research/astra-wild-nine-hour-20261128/outside/AFFINE_APPROXIMATION_AT_THE_DENOMINATOR.md)

## Local evidence

Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`, checked the two finite integer alignment declarations using `Std` alone:

~~~
lean -j1 -DElab.async=false -DwarningAsError=true -DautoImplicit=false \
  research/astra-wild-nine-hour-20261128/outside/CommonPrimeAlignment.lean
~~~

The command exited zero with no diagnostics. It covers common-modulus divisibility and the strict-size implication only. The orbit counting and measure-theoretic theorems have written proofs.

`python -B research/astra-wild-nine-hour-20261128/outside/check_congruence_clocks.py` and its `python -O -B` version both exited zero and printed identical counts:

~~~
blocks: 1535
integral outputs: 287
nonvacuous single-prime bounds: 44
partially canceled clocks: 16
prefixes: 10414
rational phases: 480
same-prime transports: 7288
sharp mixed errors: 196
simultaneous prime clocks: 153
~~~

The auxiliary clocks are exact modular walks from ordinary residue 5 at rational phases. The finite tests do not assert that an ordinary seed shadows those phases forever. The standard `python -X utf8 -B tools/validate.py` also exited zero at the pre-commit base worktree, with the repository's explicit integrity-only scope.

## Open inference

The cofactor application would exclude escape if a positive proportion of actual times were forced near a short transient predecessor at the requisite growing prime power. Those neighborhoods have vanishing spatial density in the sublogarithmic-horizon version. The atomic classification allows nonatomic invariant distributions and negative rational local limits. Neither argument supplies an ordinary infinite counterexample or excludes all positive orbits. The next question is whether arithmetic information on transitions between rational phases forbids concentration even when the controlling primes or return lengths vary.
