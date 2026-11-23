# Formal scope of the amortized triadic certificate

The final source `lean/TriadicAmortizedBudget.lean` proves the entire
finite paired-state horizon, including signed numerators, zero entry,
the ensuing finite odd tail, and the literal binary-height choice.
There are **22 new theorem declarations and four definitions**; these
are an audit inventory, not a novelty count. Every declaration is listed
in `THEOREMS.json` and audited by `lean/TriadicAmortizedAudit.lean`.

The main theorem is

```text
CollatzTriadicBudget.finite_triadic_height_certificate
```

For any one positive integer `n`, signed integer `a`, and natural `r`,
define

```text
F(r) = product_(j<r) (1+3^j)
B = n * max(1,abs(a)) * F(r)
E = Nat.log 2 B.toNat + 1
H = 9*E+1.
```

If the actual deterministic paired trajectory from `(n,a,r)` passes
opposite-parity tests at every clock `k<H`, the theorem concludes that
the literal original shortcut orbit satisfies `T^k(n)=1` for some
`k<=H`. Positivity of that original orbit is derived from its actual map.
The theorem has no infinite compatibility, all-time positivity of a
candidate, drift, absence-of-cycles, or candidate-existence premise.

The displayed complete-carry congruence in `TRIADIC_AMORTIZED_BUDGET.md`
implies this finite parity premise by the written inverse-word argument
already used in PR178. **That congruence-to-prefix bridge is not newly
formalized in this module.** The asymptotic estimate for `log F(r)`,
literature analysis, and universal construction discussion also remain
written mathematics. No universal candidate is supplied.

The imported `lean/TriadicDualClosure.lean` is an exact unchanged copy
from PR178 commit `4e204f54136c79cf8c9393b34e3330594f99ae0a`; it supplies
the actual paired step, deterministic trajectory, and ordinary orbit.
Its source pin is in `SOURCES.json`. The new capstone proves a finite
horizon directly; it does not invoke the imported infinite rank theorem
to stand in for finite parity checking.

Fresh compilation and the complete declaration audit use Lean 4.34.1
and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`, with
warnings treated as errors. Only `propext`, `Classical.choice`, and
`Quot.sound` occur in the union of audited axioms. The execution receipt
records the exact source hashes, fresh objects, and actual commands.
