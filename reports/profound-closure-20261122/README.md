# Evidence for the independent-block and finite-ancestor continuation

The mathematical statements and proof-level boundaries are in
[`research/profound-closure-20261122`](../../research/profound-closure-20261122/README.md).
This directory records development checks, independent semantic reviews,
and published-checkout replay evidence as it is produced.

The new source contains four Lean modules with 39 public theorem audits:
eight finite power-budget declarations, six physical two-exponent cycle
declarations, 21 complement/carry declarations, and four finite-telescope
declarations. Development logs report strict Lean 4.34.1 compilation with
only `propext`, `Classical.choice`, and `Quot.sound` in the audited lists.
The exact commands and hashes are recorded in the associated receipts;
the telescope source ledger is under the research packet's `sources/`.

The semantic reviews distinguish the proved written deductions, external
published inputs, repository analytic inputs, exact arithmetic certificate
checks, and Lean formalization. The independent two-exponent review
includes a separate replay of the 32-convergent cover and its eight damaged
certificate controls. The carry checker hardening receipt records both
normal and optimized Python, four semantic corruption controls, and three
invalid-input controls. The bounded-language verifier independently
recomputes six block-list bounds and four uniform bounds.

The continuation does not rerun the previous 23-module/140-audit packet
or the previous five-module/23-audit packet as a substitute for new work.
The new replay driver compiles only the actual dependency closure of the
four new modules and preserves the older recorded sources byte for byte.
