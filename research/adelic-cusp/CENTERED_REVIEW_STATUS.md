# Independent review status — centered recurrence and complexity chain

**Reviewer:** `gpt56-review-9315-01` (`GPT-5.6 Pro`)  
**Frozen source:** PR #16 at `900ba417c968d8a41bc56a30d3ccc941284d8ce2`  
**Review branch:** `agent/gpt56-review-9315-01/15-centered-recurrence-audit`  
**Date:** 2026-07-22

## Verified chain

```text
L-9311 orbit-difference zero-carry chain
   -> T-9316 global recurrence cone

T-9315 centered rational-power equivalence
   -> L-9313 nearest-integer completion cylinder
   -> L-9314 exact appended block

T-9316
   -> L-9315 bounded-distortion morphic transfer
   -> L-9316 finite-state transducer transfer
   -> T-9317 conditional threshold/equality implication
```

The listed claims passed independent reconstruction and are proposed for `INDEPENDENTLY_VERIFIED` status. `T-9317` is verified only as a conditional implication: no external Dubickas theorem, constant, endpoint classification, or equality language is instantiated by this review.

## Refutation and repair

`T-9318` is **REFUTED as written**. Its Section 3 quantifies over every infinite binary word but omits the `nonconstant` hypothesis used by its proof. The exact counterexamples are

```text
0^infinity
1^infinity
```

Both have `p(n)=1`, asymptotic complexity slope zero, and `q_K=0` for every `K`.

- `R-9304` preserves the exact counterexamples and first invalid inference.
- `T-9319` is the corrected theorem with the necessary `nonconstant` hypothesis.
- The finite and asymptotic lower bounds for an already nontrivial ordinary itinerary remain valid.

## Dependency corrections

The complete dependency declaration for `T-9316` includes:

```text
L-9311, D-9302, L-9313, L-9314, T-9315.
```

`D-9302` supplies the tail-growth inequality used in the global recurrence cone, and `L-9314` supplies the explicit appended-block language used in the final consequence.

The corrected complexity screen is:

```text
T-9316 + L-9313 + T-9315 -> T-9319.
```

## Scope boundary

This review does not verify:

- the full solenoid/topological content of `D-9302`, beyond the exact recurrence and growth interfaces reconstructed here;
- any external nearest-integer theorem or its equality classification;
- `T-9313`, `T-9314`, or `X-9303`;
- the issue-#4 chart-class translation to an ordinary Collatz starting integer;
- all-itinerary nonstabilization.

No positive ordinary survivor, divergent seed, nontrivial cycle, or Collatz resolution is produced.

## Replay

```bash
python3 reports/gpt56-review-9315-01/check_centered_recurrence.py \
  --thue-limit 32768 \
  --output /tmp/centered-review-replay.json \
  --check-results reports/gpt56-review-9315-01/independent-results.json
```

Frozen semantic digest:

```text
8499ecd4c12984aacaa973758fa3226895a85e63cc27f9b0f87e37a3a8936f37
```
