# Unconventional ordinary-source attacks

**PROPOSED research, 26 November 2026. Collatz remains open.** This packet starts from the owned PR192 head `0e313e2cd42cfce1275dbef6129ac13e9a49abd5`. It tests three different ways of retaining one fixed ordinary source: arithmetic squareclasses, constructive inverse control, and signed transport. The infinite arguments are written mathematics; the named finite and local results have Lean kernels. A verification report records the exact checked revision and scope.

Throughout, the shortcut map is `T(2n)=n`, `T(2n+1)=3n+2`. The accelerated odd map is `U(x)=(3x+1)/2^a`, where `a=v₂(3x+1)`. A shortcut clock and an odd departure are different resources.

## Results and their boundaries

| Direction | Result | What remains unproved |
|---|---|---|
| [Squareclasses](adelic/README.md), [actual descent](adelic/GROWTH.md) | An explicit bound on an orbit's record height in terms of its odd-state squareclass rank; an actual convergence theorem from a dependence condition at every growth triple; a mixed real/ternary argument for rank at most seven using the separately published verification below `2^71`. | No bound on the squareclass rank of every fixed source. The rank-seven corollary uses an external range computation, which this packet does not rerun. |
| [Fixed-source inverse control](descent/README.md) | For every fixed positive ternary-unit endpoint and every prescribed residue modulo `3^L`, a positive odd ancestor in that class reaches that same endpoint with `L^α+O(1)` odd departures and `exp(Oα(L/log L))` shortcut clocks, for each fixed `0<α≤1`. | The resulting height can be enormous. The construction does not transport the second orbit label needed by the existing paired closing target. |
| [Signed ordinary transport](operator/README.md) | The residual norm of a summable signed charge is exactly its mass on escaping components. Vanishing finite charges have explicit finite transport witnesses. Arbitrary unitary weights on genuine physical edges do not remove that obstruction. | No construction places a charge positive at every ordinary source in the closure of the transport boundaries. This operator also damps any hypothetical positive cycle, so escape control alone would not identify the cycle. |
| [Quadratic characters](adelic/CHARACTERS.md) | Almost every multiplicative quadratic sign character codes every fixed injective ordinary orbit normally; three specific dyadic characters must exhibit a quantitative bias on any such orbit. | A Haar-generic character theorem says nothing about those three specified characters. The fixed-character transfer has not been proved. |

The positive inverse theorem has an elementary finite-distribution proof and an independently executable radix construction. Its large-clock examples are modular certificates unless an actual ordinary walk is explicitly reported. The elementary arithmetic descent theorem is checked on the actual factorization-defined odd map, rather than on an unspecified transition system.

## The central interaction

An entrance into a residue class for one orbit is insufficient for the canonical paired target. The later parts of this pass investigate actual common-clock returns of `(Y,3Y−1)` to `(X,3X−1)`, transporting both physical labels. Their resource accounting must include both odd counts, their changing difference, and the shared shortcut clock. An unbounded return grammar is a different object from a fixed bank used a bounded number of times.

Neither a changing finite ordinary witness, a generic character, nor a vanishing scalar average is promoted to a pointwise assertion about the original source. The first unsupported step remains stated with each argument. No theorem in this packet establishes that every positive integer reaches one.

## Reading and replay

Read the three lane documents for statements and complete written proofs, then their Lean modules for the precise formalized scope. The root review and replay receipt under `reports/astra-unconventional-20261126/` distinguish independent proof reconstruction, finite computation, Lean checking, and whole-repository integrity validation. A source-qualified use of an external theorem is not a formalization of that theorem.
