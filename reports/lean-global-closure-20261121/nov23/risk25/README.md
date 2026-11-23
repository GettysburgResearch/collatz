# Evidence for the parallel residual, endpoint and triadic attacks

23 November 2026. Scientific packet:
[risk25](../../../../research/lean-global-closure-20261121/risk25/README.md).
Baseline PR175 head: `53ba1e1ffc46bf022433c2124a62682ad8dd4739`.
The previous public PR description is preserved in
[`previous-pr-description.json`](previous-pr-description.json), including
its preceding exact-head gate receipt.

## New written-proof reviews

| Claim scope | Independent reconstruction |
|---|---|
| Actual numerator root bound, reduced-clock minimum bound, power residual degree | [Root cycle review](ROOT_CYCLE_REVIEW.md); [endpoint-lane review](REVIEW_INTEGER_RESIDUAL_DEGREE.md) |
| Complete cyclotomic residual value, including every quadratic half packet; maximum-state comparison | [Root cyclotomic review](ROOT_CYCLOTOMIC_REVIEW.md); [endpoint-lane review](REVIEW_CYCLOTOMIC_VALUE_SEPARATION.md) |
| Complete-carry reference estimate, unnormalized actual-word transfer and stationary distortion alternative | [Root endpoint review](ROOT_ENDPOINT_TRIADIC_REVIEW.md); [cycle-lane review](REVIEW_ENDPOINT.md) |
| Source-aware anchor identities, all-run reset interpretation, finite Mahler equations and higher-digit interpolation | [Root triadic review](ROOT_ENDPOINT_TRIADIC_REVIEW.md) |

Every review binds its exact scientific source bytes by SHA256 and limits
its verdict to named claims. Matveev's original Corollary 2.3 was opened
and its parameter specialization checked independently by the root and
endpoint reviewer. Its proof remains a published input. The newer
ordinary-state counting argument was independently reconstructed on its
actual injective forward-invariant domain, including finite cycles.

The original cyclotomic continuation retains its PROPOSED header; the
two later pinned reviews establish its written-proof verdict. It is not
an unreviewed premise silently added to a Lean declaration. The older
factor-gap certificate remains qualified where the core paper cites it;
the new cyclotomic asymptotic bound has a separate derivation.

## Executions actually performed

| Execution | Observed result | Receipt |
|---|---|---|
| Author's new core/Std Lean module | Exit 0; 26 theorem declarations; 12 printed key axiom inventories contain only propext and Quot.sound | [Author Lean receipt](source-aware-lean-receipt.json) |
| Root execution of the copied final Lean source | Exit 0; empty stderr; same 12 axiom inventories and exact source hash | [Root Lean receipt](root-lean-receipt.json) |
| Exact cycle controls, normal and optimized Python | Both exit 0; identical output; six controls, all 76 rotations | [Receipt](cycle-validation-receipt.json), [results](cycle-control-results.json) |
| Exact carry/endpoint controls, normal and optimized Python | Both exit 0; identical output; m<=12, 3902 ordinary replays, 24 strip cases, 873 occurrence cases | [Receipt](critical-carry-receipt.json), [results](critical-carry-checks.json) |

The cycle script uses Python 3.12.14 and SymPy 1.14.0. The Lean binary
is version 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`; its exact binary hash is in
the root receipt. The author and root executions are distinct events.
The finite controls are not claimed to prove the infinite theorems by
enumeration. Older Lean modules and historical computational certificates
were not rebuilt for this continuation.

The required complete clean-checkout repository gate is performed on
the final unreferenced commit before advancing PR175's branch. Its exact
commit/tree, command results and receipt hash are published in the PR
description after execution. This report does not predeclare that result
or pretend a receipt can contain the hash of its own enclosing commit.
Repository integrity validation is separate from mathematical proof.

## Sources and late updates

[`source-refresh.json`](source-refresh.json) records the initial refresh,
including older PRs sorted by their newest updates and the unchanged main
head. [`prepublication-refresh.json`](prepublication-refresh.json) records
the later observed heads. New peer files were read narrowly for closing
implications; the published proof dependencies keep their earlier exact
pins. No later commit is implicitly covered by an earlier review.

The precise source paths, Git blob identities, SHA256 values and roles
are listed in `source-bindings.json`. The final `manifest.json` binds
the new scientific files, reviews and receipts. Neither file counts as
mathematical verification.

The late comparison is in `PREPUBLICATION_COMPARISON.md`. In particular,
PR178's new flow change supplies a fast inverse-endpoint comparison;
it does not supply the actual word-energy bound used in the endpoint
consumer. The newest cycle notes do not turn denominator size into a
numerical gcd bound, and the triadic finite tests remain recognition
tests until a successful candidate is constructed.

## Exact unresolved obligations

The cycle result requires a new restriction on the complete numerical
gcd at X=3 or the associated primitive integer numerator polynomial.
The escape result requires actual word-energy and omitted-mass bounds,
or another same-source critical collision upper. The construction route
requires every ordinary source to have a triadic candidate passing its
own finite horizon. None of those assertions is proved in this packet;
no full Collatz theorem or global successful selector is claimed.
