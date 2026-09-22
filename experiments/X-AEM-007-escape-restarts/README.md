# X-AEM-007: actual escape restarts

Python standard library only. Run from the repository root:

```sh
python -B -S experiments/X-AEM-007-escape-restarts/run.py --full aer-full.json --check experiments/X-AEM-007-escape-restarts/canonical.json
python -B -S experiments/X-AEM-007-escape-restarts/verify.py aer-full.json --summary experiments/X-AEM-007-escape-restarts/canonical.json --self-test
python -O -B -S experiments/X-AEM-007-escape-restarts/verify.py aer-full.json --summary experiments/X-AEM-007-escape-restarts/canonical.json --self-test
python -O -B -S experiments/X-AEM-007-escape-restarts/contract_check.py
```

Single comparison examples:

```sh
python -B -S experiments/X-AEM-007-escape-restarts/run.py --r-parameter 191
python -B -S experiments/X-AEM-007-escape-restarts/run.py --h-parameter 7759
```

`--h-parameter C` investigates (9C+2,C), not an arbitrary original Collatz
source. `--r-parameter D` investigates (3D-4,D), D>=2. Neither option claims
universal convergence; both accept exact positive integers and reject booleans
at the library boundary. Single-comparison options cannot be combined with
corpus generation/check options.

## Inventory

135,584 rows:

| Kind | Count | Coverage |
|---|---:|---|
| primitive | 4 | One credited and three added whole-cylinder R rules |
| normalization | 65,535 | Every D=2..65536, complete mixed-return execution |
| K_table | 4,095 | Every E=2..4096, including every tested residue |
| family | 386 | Exact successful cylinders for all words through length4, longer repeated/mixed words, and large controls |
| lift | 24 | Original-source CRT lifts, all states and whole progressions |
| grid | 65,536 | Every H parameter C=1..65536, both old/new classifications |
| control | 4 | C=2/17/71 and the expanding eleven-step return |

Each of the 386 word cases is a whole-progression certificate, not just the
least representative. Longer controls include B^128, C^64, D^32, and mixed
(BCAD)^16. Sources change with prescribed finite words; no infinite ordinary
word is inferred.

The same H grid gives 5,082 old successes and 5,255 extended successes, with
173 additions, 54 of them C=2 mod3. Every previous successful word pair,
clock and endpoint in this comparison is identical in the extension. There
are 60,281 remaining OUTSIDE outcomes and no BUDGET cases in this corpus.
The outer procedure has a 1,000-stage budget. The inner R normalizer needs
no stage budget because its common integer rank decreases unconditionally.

The old baseline is reconstructed from the exact read #129 source; it is
not a comparison against every later repository method. When a prospective
new restart fails, the recorded OUTSIDE checkpoint is the last accepted H
state. Failed-trial steps are not silently added to its clock. All source
labels are retained, and the local R trial is directly reconstructible.

## Independence and adversarial scope

`kernel.py` supplies the generator's closed formulas. `verify.py` imports
none of it: it calculates R and H macro endpoints from actual T steps,
constructs return cylinders by forward word numerators, and enforces all
progression identities, positivity, original-source inequalities, clocks,
first meetings, exact inventory and all failed labels. It rejects booleans,
floats and duplicate JSON keys. It does not rely on removable Python asserts.

The self-test rejects 23 directly mutated semantic witness rows, four
inventory alterations, and five JSON/type controls. These are **not** described
as re-sealed full-corpus attacks. The contract harness separately tests the
library/CLI domain, normalizer stage bound and valuation countdown formulas.
Both implementations have the same author; agreement is not independent
mathematical peer review.

`canonical.json` authenticates the deterministic finite rows. A large full
JSON is generated on demand rather than committed. The delivered archive
includes the actually generated full corpus as a convenience.

Read the [mathematical proof](../../research/astra-exit-merging/escape-restarts/PROOF.md)
and [execution receipt](../../reports/astra-exit-merging-07/validation.json).
Repository-wide validation was not run; a clean packet application is not a
complete checkout. All new mathematical statements remain PROPOSED.
