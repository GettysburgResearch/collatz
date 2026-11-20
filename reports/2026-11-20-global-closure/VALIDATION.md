# Validation and publication boundary

The manuscripts, certificates, deterministic reports, and separate reviews
are listed in `CONTENT_SHA256.json`. Their agent reconstruction verdicts
are recorded in the four review files. No verdict asserts a full Collatz
proof, external acceptance, or proof-assistant verification.

## Executed GitHub content commit

Both required commands were actually executed in a clean, complete
checkout of the exact GitHub commit
[`3cd47dbdeaddf6e4f4446d795271e75a52d68c99`](https://github.com/GettysburgResearch/collatz/commit/3cd47dbdeaddf6e4f4446d795271e75a52d68c99),
tree `9af44ea668ae3afc1431625fc8d6a093b664ba9e`, containing **344 tracked
files**. The GitHub tree matched the locally assembled tree exactly. The
complete Git commit object was reconstructed and its SHA-1 matched the
GitHub commit before its detached checkout was executed. This was not a
claim based only on an API tree listing or a locally different commit.

Execution used Python 3.12.14 on Linux on 2026-11-20, from
19:58:57 through 19:59:02 UTC. Both receipts record identical before/after
checkout identities and `success: true`.

| Executed bundle | Result | Attached exact receipt | Receipt SHA256 |
|---|---|---|---|
| New scientific bundle | All 26 manifest files matched; all 8 checks passed | [execution-content-science.json](execution-content-science.json) | `3c16aeae964c1774b446a54161296c3185c14cb021fc4045ee52d88161533650` |
| Existing `tools/validate.py --regressions` | All 11 commands exited 0 | [execution-content-repository.json](execution-content-repository.json) | `5f284a5ded7fb4c1ed35fdb8adbb4bb6544def81181c65b34956881186fac6b2` |

The eight new checks are three production report comparisons, the four
separate review computations, and the arithmetic production checker's
**expected optimized-mode refusal**. The last check passed because the
checker exited 1 with its exact safeguard message. It is not described as
a successful optimized execution of the arithmetic mathematics.

The content manifest SHA256 is
`75f68c6906d5ab5e4a34accd3a4566e90962b38fe5ba3966f5fd020d154997d4`.
The independent physical-return comparison regenerated its complete JSON
report exactly; the other six positive programs regenerated or compared
their own frozen reports successfully. The receipts retain each actual
exit code and output, including the expected refusal.

## Relationship to the publication head

The publication child of the executed content commit adds the two attached
receipts and updates only this validation narrative and the report index.
It preserves every file in `CONTENT_SHA256.json` byte for byte. These
receipts therefore identify the exact executed content commit, not a later
commit that did not exist when the commands ran.

The PR description records the exact final publication head and any
additional completed execution on it. A receipt for that head cannot be
inserted into the same immutable Git commit without changing its identity.
The commands below can also be run directly against that head; the
manifest and checkout identity checks remain active.

## Required commands

```sh
python -X utf8 -B reports/2026-11-20-global-closure/run_bundle.py --receipt /absolute/path/outside-checkout/science.json
python -X utf8 -B tools/validate.py --regressions --receipt /absolute/path/outside-checkout/repository.json
```

The new bundle's manifest comparison, exact deterministic outputs,
independent calculations, and expected optimized-mode rejection are
distinct from the existing repository validator. Both require a clean,
complete checkout and record its actual commit and tree before and after
execution. The receipts preserve actual exit codes and output.

## Interpretation

The all-lift affine legality and coverage checks support the conditional
descent proof. Bounded orbit replays support only their recorded domains.
The transport's infinite omitted-source tail is a proved analytic bound,
not a computation of infinitely many orbits. Passing repository validation
establishes the stated integrity and regression checks, not the mathematical
truth of an unproved global premise.
