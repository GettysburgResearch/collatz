# Arithmetic lane execution

Executed from the repository root with Lean 4.34.1, mathlib at d13f23b723b8a846827a245b89c10fc7d3f11612 on the supplied LEAN_PATH, and Python 3.

| Source under research/astra-joint-closure-20261124/arithmetic | SHA-256 |
|---|---|
| FiniteCycleTests.lean | 6d59babca177a85ead06fcfcd732b4e9715296d0521284b3b9f71d858e0ee0bc |
| check_cycle.py | aaa42f47aea83dce0e12cf1b1a6e277b1bfe8c2ead0dba58be79d0feb53dcd41 |

`lean -j1 research/astra-joint-closure-20261124/arithmetic/FiniteCycleTests.lean` exited 0. The four axiom audit outputs were:

```text
'FiniteCycleTests.branch_swap' depends on axioms: [propext, Quot.sound]
'FiniteCycleTests.translation_generator' depends on axioms: [propext]
'FiniteCycleTests.outside_divides_denominator' depends on axioms: [propext]
'FiniteCycleTests.saturated_residue' depends on axioms: [propext, Quot.sound]
```

`python -X utf8 -B research/astra-joint-closure-20261124/arithmetic/check_cycle.py` exited 0 and printed:

```text
primitive period 184, odd steps 116, residue 157 modulo 180
cancelled gcd 5, reduced denominator 466923261846322839553673870807890524045457468671845219
cycle minimum 22488132255881977213793957567500181099017372753319593853/466923261846322839553673870807890524045457468671845219
```

The example checks every literal parity, positivity at every phase, first return, the full cancelled gcd, the reduced denominator, and the simultaneous input congruence. It does not establish the general construction or the entropy asymptotic.
