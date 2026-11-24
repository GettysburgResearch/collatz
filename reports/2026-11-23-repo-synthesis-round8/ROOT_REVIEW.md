# Root reconstruction and integration review

23 November 2026. Published parent:
`3954c775ba74e1f40776ff38cb4282698d4a334a`.

**VERIFIED at the written claim level: R8-G1--G4, R8-S1, R8-P1--P4,
and R8-O1--O5. R8-P5 is VERIFIED conditional on its explicitly pinned
actual escaping-product input. R8-L1 REFUTES the specified external
uniform-descent lemma. No universal Collatz conclusion is established.**

The root independently reconstructed the three agent lanes, inspected
their exact controls, freshly compiled their two Lean modules, audited
all public declarations, and executed the combined controls normally
and under optimization. The root authored R8-S1 and the literature
counterexample note; those have independent sibling review in
PRESSURE_REVIEW.md, rather than being described as independently
reviewed by their author.

## Exact science versions

All paths in this table are under
`research/repo-synthesis-round8-20261123/`.

| File | Git blob |
| --- | --- |
| `GERM_BRIDGE.md` | `540110f09cf68e3309fd83fea9c7ae497536ded4` |
| `SCALAR_SEPARATION.md` | `5aa20b1793534d2e7a5bf8891b64cfcb4633c455` |
| `PRESSURE_CONSTRUCTION.md` | `7ef222d23f59a2dffd936dbfa93765df064db166` |
| `ORDINARY_SELECTOR.md` | `27ac47ee345d3197bcd85d5128419c601da6ebe3` |
| `LITERATURE_BOUNDARY.md` | `a46644df1ef545616f2ebd5958d161ab4d8d64bc` |
| `GermBridge.lean` | `d6a9d41f6fc348ab6ed636645e2711ae7f95615d` |
| `OrdinarySelector.lean` | `0296d5bc7faab46351bad7351a4be854050285f6` |
| `germ_bridge_controls.py` | `5d4d09073d4ad088807d77543de5f5e437111403` |
| `scalar_controls.py` | `51533c527655d7ae365ad5a4efad8e653dd56e51` |
| `pressure_controls.py` | `ff6936ae3bc57daa8ebe10bdfa07f92aeb2af592` |
| `selector_controls.py` | `7093c020392ed3193fcc14f54018d060ab726136` |
| `exact_replay.py` | `b48fd01b89f7aef6478032bb965eb0b4bac02ef1` |

## Substantive reconstruction

For the scalar construction I checked the complete odd-step equation,
the bound `A_m<=2m+log_2(q)`, both geometric constants, and the strict
half endpoint. The analytic derivative is taken at the interior real
point one, not inferred from a different completion. The initial-even
normalization adds exactly the number of initial binary divisions.

Triadic denominator clearing makes the actual tail scalar integral.
This supplies the threshold needed for contraction. The stronger
integer potential keeps the full powers `2^g`, `2^h`, and `2^h'`,
including the complete affine `+1`. I independently expanded the
polynomial inequality and its a=2 versus a>=3 cases. The finite budget
uses the nonterminal bit-length lower bound and handles q=1 before
applying it. The guard proof is valid at r=0, with unreduced candidates,
and after subtracting an initial-even scalar contribution. Rejection
is a decision about one candidate, never a decision that its source
fails to converge.

For R8-S1, the discrepancy scales by exactly `3^k`. The unreduced
candidate denominator at the decision step is `3^max(r-k,0)`. The
three possible rejection margins have the correct integer-lattice
constants, giving the common bound `3^(-K-1)`. The strict approximation
criterion is sufficient for equality; generic real computability is
not a supply of successful approximants.

The phase proof keeps the actual positive ordinary orbit. Its strict
minimum lift assigns three halves to the fraction one half. Canonical
phase charges are integers between one and three, so the block test
is an exact rational comparison. The verified odd floor 31 gives
`q>=33` on a hypothetical nonconvergent path, including any nonstandard
positive cycle. Both powers-of-two cosets, the d=8 exception, and the
odd-prime-power full fibers were reconstructed. The theorem for a
complete prime-power denominator is not a theorem about each factor
of a general denominator. The p=11 valuation-two exception is retained.

The pressure deduction uses the same attained maximum throughout.
The component-uniform positive product bound makes its logarithmic
boundary term vanish. Independently of that logarithmic identity,
every actual prefix satisfies the clock bound. Escape then makes the
clock deficit tend to minus infinity, proving a strict scalar ceiling.
The forty-term enclosure is exact. Clearing powers of three need not
preserve the pressure-maximizing source, and the note does not reuse
that maximum at the later state. The underlying product remains
source-qualified at its frozen upstream input; I did not present it
as a new proof or as a product on periodic components.

For the ordinary construction, the modular inverse exists modulo the
complete odd D, and exactly one of its two representatives modulo 2D
is odd. This makes u positive and odd. I checked all L-prefix source
classes and the final P class, the actual intermediate quotients, and
the full affine remainder `-29/16`. The endpoint's initial gap-one
prefix and the unconditional scalar upper bound give its low actual
scalar without any termination assumption. Backward transport gives
exactly one high scalar among the whole constructed segment. The
unbounded endpoint/source ratio and the two strict phase-approximation
bounds follow with a source of only linearly growing bit length.
The high-state `35/36` estimate is valid, but the construction shows
why it is not a bound for low-to-low returns. Changing m changes the
source; no ordinary infinite realization is extracted.

The literature counterexample includes the complete standard tail.
Its logarithmic sign is certified by an exact positive rational lower
bound, not a plotted countdown or floating point. The separate
Monks--Yazinski comparison keeps the different coordinate and the
cycle/divergence distinction explicit. No literature-wide novelty
claim is made.

## Formal and execution evidence

LEAN_RECEIPT.json records a fresh empty output directory, both source
compiles and the audit compile with `-j1`, warnings as errors, and
auto-implicit variables disabled. Seventeen theorems and three
definitions were audited. Only `propext`, `Classical.choice`, and
`Quot.sound` occur. Neither module imports an older repository module;
the pinned official Lean distribution and Mathlib cache were used.

This formal scope consists of finite polynomial, complete gap, power,
affine, and scalar interval arithmetic. The real series, its analytic
attachment, the complete recognizer theorem, and the all-exponent phase
families remain written mathematics. There is no claimed full Lean
formalization of those statements or of Collatz.

EXACT_RECEIPT.json records both successful combined executions. The
outputs are byte-identical, all fifteen scientific inputs are hashed,
and the five Python sources contain no `assert` statements. The four
lanes perform 183,622 explicit checks in total. Their domains overlap;
that number is not a count of distinct ordinary sources or theorems.
The largest actual constructed example reaches one in 1,901 odd
transitions in the bounded replay. Its 258-step expanding prefix is
therefore not an alleged Collatz counterexample.

Independent reviews are GERM_REVIEW.md, PRESSURE_REVIEW.md,
ORDINARY_PRESSURE_REVIEW.md, and ORDINARY_REVIEW.md. Each pins its
reviewed science blobs and specifies its inherited dependencies.
Repository-integrity checks and preservation bindings are separate
from these mathematical reviews.

## First unsupported global inference

No arbitrary fixed ordinary source has been proved to have a triadic
scalar. The remaining low rational phases and all irrational values
are not excluded. The same-source pressure restriction, finite
recognizer, explicit approximation threshold, and actual ordinary
obstruction are useful new inputs, but none supplies that construction.
The earlier full moving-root mass comparison and universal paid
ordinary selector also remain open.
