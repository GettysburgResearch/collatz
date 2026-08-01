# Integration practice

This is a gentle default for major integration passes. It is not a gate on exploratory research.

## 1. Freeze a snapshot

Record UTC and local time, main SHA, every open PR head, and a cutoff statement. Assume agents will continue pushing.

## 2. Locate exact-SHA evidence

For each PR, record:

- reviewed SHA;
- verdict;
- report and reviewer;
- claim-level exceptions;
- source-qualified inputs;
- artifact/replay state.

No verdict moves automatically with a branch.

## 3. Audit later deltas

Classify the delta from reviewed SHA to current head:

- editorial;
- review record only;
- proposed connection;
- computation/artifact only;
- theorem-bearing;
- dependency change.

Only the first two normally inherit the old mathematical scope without new theorem review.

## 4. Integrate claims, not branch numbers

A PR may contain verified, proposed, empirical, refuted, and blocked material. Extract coherent packets. Do not maximize merge count.

Prefer one canonical statement when several branches prove the same result. Preserve every alternative proof and reviewer as provenance.

## 5. Allocate canonical IDs

Source IDs stay unchanged and are cited as `PR<number>:<claim-id>`. Allocate a repository-owned canonical ID and update the alias/collision ledger. Never silently rename a source theorem.

## 6. Keep repairs separate

A refuted original remains refuted. A repair receives a new source claim/SHA and a new review. Record the relation explicitly.

## 7. Record computation honestly

Use separate fields for proof reconstruction, artifact inspection, regeneration, checker execution, and independent large-run replay. A stored digest produced by the same program is not an independent verifier.

## 8. Keep the README stable

The README explains mission, boundaries, navigation, and status semantics. Put live heads, current blockers, and short-term priorities in an immutable timestamped state linked by `docs/integration/CURRENT.md`.

## 9. Preserve exploratory freedom

Exploratory contributors may use broad PRs and informal notes. The canonicalization contract applies only when material seeks the integrated layer.

## 10. Leave a handoff

A fresh integrator should be able to reconstruct the cutoff, identify new deltas, locate pending reviews, run normal checks, and update the registry without private chat history.
