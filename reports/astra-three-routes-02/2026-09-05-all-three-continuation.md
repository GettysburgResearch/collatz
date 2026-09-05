# All-three continuation of PR #92 — 2026-09-05

Agent: `astra-three-routes-02` (GPT-6 Pro).
Parent: `879343c33a7dca29128891cf6e10d9c7be1ba482`.
Branch: `agent/astra-three-routes-01/three-route-offense`.

The owner requested another ambitious pass on **all three routes**, on top of
the published PR. The portfolio is not narrowed. All new theorem-level claims
remain PROPOSED pending independent review; no complete Collatz proof was found.

## Attempt and concrete result

Route 1 initially revisited the original survivor-bias ceiling. A finite
extension did not yield an all-time argument. The more productive step was to
separate many-to-one basin transport from equal-depth-injective orbit transport.
Exact cylinders yield a uniform 4X^(39/40) count and reciprocal bound; forward
invariance permits a fiber-free recurrence giving O(X^(19/20)). Known related
Garcia–Tal sparsity and an earlier public summability/escape derivation are
credited explicitly. A cofinal-time bias target replaces the unnecessarily
strong eventual-all-times requirement, but remains open.

Route 2 uses the bounded correction product to extract an actual SC-infinite
source on every infinite orbit. This proves the local SC* iff eventual
periodicity bridge, plus a quantitative proximity bound without a time bound.
The continuation compiler uses one interval and one CRT class modulo the
complete D*2^t, and improves the old finite rational prefilter from 6,431 to
9,381 rejections. An exact 61/295 no-descent rational tail explains why deleting
the whole-denominator gate would be invalid even with arbitrarily many echoes.

Route 3 tests a genuine enlargement of the failed rank class: arbitrary separate
nonlinear valuation profiles. Precision transport eliminates that enlargement
for fixed shortcut blocks and, by a separate proof, the adaptive whole-run
macro. The proof allows arbitrary finite profile values, with no degree or
regularity assumption. It does not eliminate cross-feature interaction,
infinite dictionaries, vector/tree ranks, or other adaptive groupings.

## Checks actually performed

The new generator and independent verifier both pass, including six resealed
corruption tests. The verifier has no generator imports. Coverage is 1,023
valuation cylinders, 3,069 ordinary lifts, 64 tail inequalities, six integer
certificates, 10,416 correction-product positions, the full core 1..64,
12,449 first-crossing words, 35,666 continuation constraints, the rational
period certificate, and 36 nonlinear rank witnesses above 10^6.

Semantic digest:

    541017f8a517ee731791224129150e68543bd06c434de48e5ffa07e447aa2b68

Both implementations have the same author; this is not external mathematical
review. Universal claims rest on the accompanying proofs, not extrapolation.
The parent large inverse-cone experiment was not rerun. No external Lean or
predecessor payload, full-repository validator, or GitHub workflow was run.

## Publication and handoff boundaries

This continuation is additive under `research/astra-three-routes/pass2/` and
`experiments/X-ASTRA3-002-three-routes/`, plus this report and an append-only
parent README pointer. Parent proof/experiment bodies are preserved. Main,
canonical statuses, PR #91, settings, and workflows are not changed.

The decisive missing assertions remain: a real basin survivor-bias mechanism;
SC* and complete ordinary cycle exclusion; and a total constructive rank
mechanism outside the proved separable-profile obstructions. The useful
cross-route connection is the new fixed-source correction bound, not an
unsupported identification of orbit sparsity with basin sparsity.
