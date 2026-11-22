# Source reconciliation for checkpoint 8

**Scope:** named statements at frozen heads, not approval of entire PRs.
The source heads below were read again before this checkpoint's push.
The complete theorem is still open.

## PR180: the new energy, return and witness syntheses

Frozen head: `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`.
This advances checkpoint 7's source pin
`d0349de2108abb7c8fb8393c086610e3372df116`.

The inspected files under `research/lean-wide-pass-20261122/` are
`ENERGY_SYNTHESIS.md`, `RETURN_SYNTHESIS.md`, `WITNESS_SYNTHESIS.md`, and
the named witness interface in `lean/WitnessSynthesis.lean`.
The canonical-envelope construction remains in
`research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`.

Credit and boundaries are as follows.

- **E11 already proves the finite-depth sandwich.** With its constant
  `mu`, it gives `mu V <= liminf D_k <= limsup D_k <= 2G <= 2V` at each
  ordinary target. This is stronger in its lower constant than the
  independently derived finite-depth version in our checkpoint 7.
  The priority belongs to PR180. Our critical-Abel parent-tail argument
  remains a separate written integration result.
- PR180 gives `V=kappa D` almost everywhere, component covariance,
  component infimum one, and `V/(2kappa)<=G<=V`. Its finite-cylinder
  comparison `V_k(q)<=kappa D_s(q)` uses actual finite cylinder values;
  it does not evaluate an arbitrary almost-everywhere representative
  at an ordinary integer.
- The new all-prefix-clock bound is
  `|P_F^d H(q)| <= [q(L-d+1)+2M*Omega+M*9^d*(2/3)^L] ||H||_(1,M)`
  for a periodic function of period `M=3^t`, with the stated cylinder
  occupancy factor `Omega`. The resolution and clock factors are part
  of the bound. They do not give a uniform contact probability by
  themselves.
- The return synthesis gives a finite-segment marked occupation bound
  `C N/log(N+2)` for injective odd prefixes and a fourth logarithmic
  moment for its actual reference distribution, with cycles retained.
  Aggregate critical return domination remains an open step there.
- The witness synthesis already permits all-length asynchronous
  prefix erasure inside the complete interval induction. Our addition
  computes the exact attained source maximum over every paid literal
  cut, including retention of the original even exponent.

This checkpoint uses the finite least excessive majorant as an explicit
analytic input. Its existence and the upstream atom/mixing inputs are
written, source-qualified mathematics, not new Lean axioms or a replay
of all upstream analytic claims. The abstract subtraction theorem and
its countable-kernel summability interfaces are independently formalized.

## PR177: complete low-word source induction

Frozen head: `a0a0d76f91b4e3846c1b1f0706cad56cb6098317`, unchanged.
The source path is `research/lean-exact-witness-global-20261121/lean/Collatz/`.

The fourteen-module transitive closure of the new source-envelope module
is copied byte for byte or reused from identical existing local sources.
[DEPENDENCIES.json](DEPENDENCIES.json) records the original path, commit,
local path and SHA256 of every file. These dependencies and the new module
were compiled in a fresh output directory.

The existing high-gap and large-initial-run rules remain credited to
PR177. Its bounded-gap cofinal construction covers every complete source
containing a gap at least five, or an initial even exponent at least four,
under its common induction hypothesis. The low source language is still
unbounded in length. Our source-envelope maximum pays for arbitrary
literal prefix deletion and exposes a smaller target domain for the
remaining selector; it does not prove that selector.

## A scoped correction to checkpoint 7

The old synchronized budget in
`../literature/CYCLE_DEFICIT_FAMILIES.md`, section 7.1, is sufficient but
not necessary for all literal cuts. A nonempty removed prefix can retain
the existing even exponent. The exact bound is
`f<=max(e,max_{a in W}(a-1))`, not `f<=max(e,max W)-1`.

The note now preserves the failed synchronized example and states the
correct scope. The new source-26/target-31 example proves that another
paid literal cut succeeds. This correction does not alter the older
complete carry-family Lean proofs or their published receipt.

## Primary literature and novelty boundary

The primary manuscript *Ternary Syracuse laws: real localization, clock
stability, and critical regularity*,
[paper 9](https://rstation.ai/problems/collatz/papers/9), Theorem 9 and
Appendix B.2, already states the maximum-density exponential rate
`log(3/2)` and derives an `O(k)(3/2)^k` upper bound. It attributes the
fixed-length/fixed-clock numerator injectivity to Tao's Lemma 6.2.
This checkpoint claims no new exponent. It rebuilds the needed estimate
with the explicit constant `4k+2`, formalizes its finite arithmetic core,
and combines it with the actual contact expansion. The rest of that
manuscript is not accepted wholesale as an input.

The least-majorant and approximate-contact interpretation is classical
optimal stopping. A primary author exposition is Yury Polyanskiy's
[Notes on optimal stopping of Markov processes](https://people.lids.mit.edu/yp/homepage/data/opt_stop.pdf),
especially Sections 1.2--1.6 and Theorem 6. Our direct ordinary-kernel
subtraction argument proves the precise version used here. No stochastic
independence premise is imposed on a prescribed forward integer orbit.

## Remaining global statements

1. **Analytic:** an effective finite-time contact lower bound with
   `p_{L(q)}(q) log(q+2)^2 -> infinity` through the actual marked units,
   followed by the required finite basin certificate below its cutoff.
2. **Arithmetic:** `LowEnvelopeMerger` or `LowEnvelopeEntry` on every
   remaining supplied low-word state above the exact paid interval.

Pointwise inverse contact, finite-word density bounds and exact source
maximization are proved at their stated levels. Neither global assertion
is inferred from them without its missing hypothesis.
