# High-variance checkpoint: execution and review scope

Date: 23 November 2026. Own branch baseline:
`8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`.

The scientific entry point is
[the new research packet](../../../../research/lean-global-closure-20261121/risk23/README.md).
The full Collatz theorem remains open. This report separates actual
compiler execution, finite controls, written proofs, inherited inputs,
and complete-checkout integrity.

## Fresh execution only

The [source execution receipt](new-source-checks.json) has SHA-256
`458e93c30a6581e86046a67db8ca41b6307d736c22dc755925dc8a55ebbae2f0`.
It records actual commands, source hashes, outputs, exit codes, and the
complete public-theorem axiom audit. The verifier copies each new source
to an external temporary directory and appends exhaustive axiom-printing
queries; it does not modify or rebuild earlier project sources.

| Execution | Scope and result |
|---|---|
| `InverseBranching.lean` | Fresh core/Std compilation; its one public theorem proves two strictly larger positive odd unit predecessors for every positive odd unit root, with exact exponents in 3--8. |
| `PrimeBalanceObstruction.lean` | Fresh core/Std compilation; all 20 public theorems audited, including the integer-valued completely additive strict-descent obstruction and its exact arithmetic witnesses. |
| `check_hardy_flows.py` | Exact rational controls for 18 root/eigenvalue/depth cases, plus four antichain truncations. Checks shared even tails, exact leaf defects, norm bounds, and cancellation of the common root defect. |
| `check_cycle_obstructions.py` | Exact five-edge product balance, distinctness, actual shortcut residual, complete word numerator and denominator, and the rational-cycle finite Fourier lifts. |
| `check_fourier_interface.py` | Exact modular formulas over the specified finite range and exact rational fifth-root weights. Its explicitly labeled floating values are sanity checks; they do not prove the analytic limits. |

All five commands exited zero. Both Lean modules use only core/Std, with
no Mathlib dependency. Across all **21 public theorems**, the only axiom
dependencies reported are `propext`, `Classical.choice`, and `Quot.sound`.
No admission or custom theorem axiom is used. The compiler is Lean 4.34.1,
commit `5045d0056413266e57c625dcd7c365b10e377c52`; its executable SHA-256 is
`e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550`.

The Hardy finite truncations are deliberately **not** described as
eigenvectors: their recorded nonzero leaf defects tend to zero by the
separate infinite written proof. The universal Hardy theorem, the TV
measure theorem, the Fourier norm limits and the late rational-cycle
corollary are not claimed Lean-formalized.

## Written proof reconstruction

The [exact review bindings](review-scope.json) identify final proof hashes,
reviewed drafts and later changes. Reviews here are independent
collaborating-agent reconstructions within this session, not external peer
review or mathematical acceptance by the repository.

The primary agent checked the complete Hardy coefficient construction,
including complex `lambda`, all shared-tail balances, the precise root
defect, channel telescoping, norm convergence, antichain supports, the
positive fixed cone, and the coefficient `ell^1` nonclosed-range endpoint.
Two other agents separately reconstructed the main Hardy proof. One
[retained review](HARDY_REVIEW_PRIOR_DRAFT.md) binds its earlier draft
explicitly; the final additions are covered by the primary-agent binding.
Neklyudov's exact operator and index formulation and Béhani's displayed
dyadic-ray comparison were checked in their primary papers. No exhaustive
novelty claim is made.

The primary agent and another agent separately checked the exact radial
TV comparison, common-source submeasure, solenoid character scale,
root-retaining product limit, and finite entropy subtraction. The final
note adds an explicit credit for PR180's concurrently stronger common-path
formulation; its proof is not presented as a unique priority result.

The Fourier argument was checked through its actual positive-integer
pullback, exact logarithmic coefficient, accelerated fifth-root residue,
dominated-convergence step and real-measure contradiction. The pole
argument was checked at ordinary positive approximants as well as at its
separately stated Haar integral. The two domains are not interchanged.

The late lifting corollary was reconstructed algebraically by the primary
agent. Its infinite high-cycle input remains the proposed, internally
reviewed PR182 theorem at its pinned head. The source's full existence,
primitivity and infinite height theorem were not newly formalized here.

## Latest-source scope

[repo-refresh.json](repo-refresh.json) contains the initial 145-PR metadata
snapshot. [late-frontier.json](late-frontier.json) pins the five peer heads
that advanced during the work. The
[scientific synthesis](../../../../research/lean-global-closure-20261121/risk23/LATE_FRONTIER_SYNTHESIS.md)
records exact paths, overlapping results, improved closing targets, and
the claims still missing. PR descriptions that lagged their current heads
were not used as substitutes for the actual new files.

The canonical analytic laws and recent external manuscripts keep their
source qualifications. Peer compiler logs and large enumerations were
read only where relevant and are not counted as new executions.

## Publication and the separate integrity receipt

The [manifest](FILES.json) binds the new packet and this report to their
source bytes, including the unchanged source execution receipt. The final
publication commit is fetched into a clean complete checkout and checked
with `python -X utf8 -B tools/validate.py` before moving our branch ref.
Its exact receipt is attached to PR175 with the actual commit and tree;
this avoids embedding a self-referential commit receipt into its own tree.

That gate checks repository structure, frozen identities and declared
scope. It is not a proof of any new mathematical theorem. The earlier PR
description, including historical results and receipts, is preserved
verbatim as the `body` field of
[previous-pr-description.json](previous-pr-description.json).
