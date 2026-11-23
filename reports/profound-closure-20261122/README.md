# Published execution evidence

The new packet passed a fresh replay on the actual published science commit
`868530d258a947bd54888511f21834cc59660761`, tree
`a9ecef96247af3e6da03a6e5554b89a904f8627e`. The checkout was complete and
clean, with 500 tracked files. Compilation artifacts, generated certificates,
and logs were written outside it. The replay ran from 05:33:36 to 05:34:37
UTC on 2026-11-22, and the checkout remained unchanged.

The complete machine receipt is [published1-complete-replay.json](published1-complete-replay.json).
The [module header port](published1-module-port.patch) and
[all command logs](published1-logs) are attached. Compiler versions,
source and generated-source hashes, artifact hashes, individual commands,
exit codes, times, and every audited declaration are recorded there.

## Results actually executed

| Check | Outcome |
|---|---|
| Lean 4.34.1, pinned Mathlib, fresh source dependency closure | PASS: nine modules; four new modules and five required inherited modules |
| Public theorem audit | PASS: all 39 new declarations (8 power budget, 6 independent cycle, 21 carry, 4 finite telescope) |
| Allowed proof axioms | Only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or native-reduction trust |
| Two-exponent exact certificate, normal and optimized Python | PASS: all 32 consecutive convergents; all eight damaged certificates rejected in each mode |
| Bounded-language exact certificates, normal and optimized Python | PASS: six block lists and four uniform bounds; all four damaged certificates rejected in each mode |
| Negative-budget certificates, normal and optimized Python | PASS: three valid examples, four damaged certificates rejected, three invalid-input controls rejected in each mode |
| Exact regeneration | PASS: all three certificate files reproduced byte for byte |
| Default repository validation | PASS: all five commands on the same complete published checkout |
| Source continuity and cleanliness | PASS: all 32 recorded replay inputs unchanged; HEAD/tree unchanged and checkout clean after replay |

There were 32 recorded command invocations, all with exit code zero.
The default repository gate includes its own finite integrity controls;
it is not a proof of the mathematical statements. The optional regression
bundle was not needed or run for this independent research packet.

## Preserved preceding work

[Source continuity](published-source-continuity.json) checks the older
23-module/140-audit receipt's 39 inputs and the preceding five-module/23-audit
receipt's 19 inputs, as well as this replay's 32 inputs. Every hash matches.
The follow-up attaching these reports changes only this report directory.
No mathematical source was rewritten to attach execution evidence.

The older complete packets were not rebuilt wholesale. Inherited modules
were compiled only when required by one of the four new sources.

## Written proofs, formal proofs, and reviews

The [research entrypoint](../../research/profound-closure-20261122/README.md)
separates all evidence levels. Matveev's logarithm theorem is a published
external input to the written cycle proof. The whole continued-fraction
closure is checked with exact rational arithmetic but is not fully
formalized in Lean. The generic bounded-language cutoff is proved; an
astronomical naive enumeration to that cutoff was not executed.

The analytic estimates are written deductions from Tao's marginal theorem
and pinned repository finite counting/comparison results. Lean verifies
the finite telescope under its explicit hypotheses. No infinite-horizon
bound or universal certificate-depth coverage is asserted.

[SEMANTIC_REVIEW.md](SEMANTIC_REVIEW.md) records the coordinating review,
with exact hashes in [root-review-pins.json](root-review-pins.json).
Independent reviews cover the
[two-exponent closure](REVIEW_INDEPENDENT_PIN_CLOSURE.md),
[inverse horizon theorem](REVIEW_POLYLOG_INVERSE_FLOORS.md), and
[finite small-ancestor theorem](REVIEW_FINITE_SPIKE_ANCESTORS.md).
Development receipts and the carry-checker hardening receipt are retained
separately from the authoritative published-checkout replay.

Imported Markdown retains its SHA-pinned two-space hard line breaks.
The assembly receipt therefore records the whitespace check with
`core.whitespace=-blank-at-eol`; this formatting choice does not modify
any proof source or certificate.
