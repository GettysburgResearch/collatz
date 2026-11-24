# Dyadic descent continuation: executed proof checks

**Full Collatz remains open.** This continuation adds four Lean modules and
53 public theorems to PR182. The new results strengthen selected marked
descents, quantify temporal marked occupation, and restrict an original
source with no forward descent. None asserts universal marked-return descent.

The [scientific entry point](../../../research/lean-dyadic-descent-20261121/README.md)
states the complete quantifiers and remaining obligations.

## Actual Lean replay

The [complete execution receipt](LEAN_RECEIPT.json) records the successful run
from 2026-11-21 22:42:45 UTC through 22:47:48 UTC. All commands used Lean
4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`, with
`-j1 -DwarningAsError=true` and a tracked-clean Mathlib checkout at
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

This run freshly compiled the three exact PR178 vendor modules and all four
new modules, then compiled the combined 53-theorem audit. It reused seven
unchanged baseline modules from the successful fresh build earlier in the
same session. The receipt embeds that actual earlier seven-command receipt,
checks its source and compiler pins, and records the reused artifact hashes.
It does not represent the final eight jobs as a fresh compilation of all
fifteen units in one run.

| New module | Public theorems | Fresh compilation | Checked scope |
|---|---:|---:|---|
| ExponentCoverage | 17 | 21.155 s | Growing certificate budgets, power-saving marked returns, selected exponent blocks and an exact upper-density bound |
| MergerDispatch | 14 | 6.865 s | Ordinary descent identities and the four possible first valuations for an original source with no descent |
| AnalyticCoupling | 15 | 15.629 s | Harmonic and Fourier finite-prefix budgets, finite marked counts, and the exact first-hit offset obstruction |
| TemporalDensity | 7 | 19.338 s | The explicit uniform logarithmic bound on marked visits for a distinct odd prefix |

The [generated audit source](ContinuationAudit.lean) and
[parsed complete audit](AXIOM_AUDIT.json) cover every public theorem declared
in these four modules. All dependency closures contain only subsets of
`propext`, `Classical.choice`, and `Quot.sound`. No `sorry`, custom closure
axiom, or `native_decide` supplies a result. The large exact example uses
kernel reduction through `decide`.

All fourteen source SHA-256 values were checked before and after compilation
and matched again when these receipts were archived. The three vendor files
are byte-identical to PR178 at
`0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`; their Git blob IDs were also
compared with GitHub. Their authorship is credited in the vendor README.

## Semantic review and mathematical limits

[SEMANTIC_REVIEW.md](SEMANTIC_REVIEW.md) records the separate internal agent
reviews of the exact proof sources and the resulting corrections. These
reviews checked mathematical interpretation and quantifiers; the execution
receipt supplies the separate kernel-checking evidence.

The selected exponent intervals do not cover every exponent, and their
growing offset-certificate budget does not cover arbitrary forced-band
offsets. Temporal sparsity does not erase a fixed surviving source or prove
spatial survivor-mass contraction. The four valuation classes constrain an
original no-descent source, not every later state above its floor. The
first-hit example refutes an offset-induction shortcut and says nothing
against convergence of that source.

The MergerDispatch restriction is a finite-prefix sieve: all valuations at
least eight already give descent by clock eight. The four remaining classes
are a necessary cover, not an exact description of all eight-step survivors.
The accompanying note retains the example 39, which lies in that cover but
descends to 38 at clock eight.

## Repository checks and publication

All five required repository checks passed in a clean, complete checkout
of proof commit `95df18ff2680a59b6ab207fccc21f3545e2883f5`, tree
`a220a9f006b6418463ff2092439b549c9808e600`, with 359 tracked files and no
checkout changes. [CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) is
the actual receipt. It is separate from the Lean replay, because structural
checks do not establish mathematical claims.
The pull-request description records the final published head, tree, and
its actual complete-checkout validation receipt. The previous PR182
description and its historical receipts are preserved in
[PR182_BEFORE.json](PR182_BEFORE.json).

## Reproduce

From a complete repository checkout, with the pinned Mathlib source and
Lean runtime available:

```sh
python -B research/lean-dyadic-descent-20261121/replay_continuation.py \
  --mathlib /absolute/path/to/mathlib4 \
  --lean-bin /absolute/path/to/lean-4.34.1-linux/bin \
  --out /absolute/path/to/fresh-output
```

Without `--base-build`, the runner compiles every dependency from source.
The optional baseline mode accepts only an existing successful baseline
receipt with matching source and compiler pins and embeds that evidence.

```sh
python -X utf8 -B tools/validate.py --receipt /absolute/path/to/checkout-validation.json
```

No compiler binary, Mathlib cache, or generated `.olean` file is included in
the repository packet.
