# Validation and publication record

The source originals, written proofs, independent bounded checker and
review records have separate evidence scopes. No finite run is substituted
for the probability proof or the all-parameter algebra.

## Reproduce the new finite checker

From the repository root:

```sh
python -B research/certificate-transfer-intake-20261120/check_certificates.py
python -OO -B research/certificate-transfer-intake-20261120/check_certificates.py
```

The checker imports none of the supplied scripts. Its explicit acceptance
checks remain enabled under optimized Python. It validates actual finite
source/output certificates, symbolic affine identities, phase controls,
fixed-clock corrections, rank-four single/double target paths, and bounded
residue partitions. Search exhaustion is UNRESOLVED.

Both commands were executed by the root publisher. They passed with
byte-identical JSON output, pinned in [science-replay.json](science-replay.json)
and [science-executions.json](science-executions.json). The checker SHA-256
is `02f014b321a93794747ff22a4d7c899b38cf593ac579490f03c48cfe0adc62e3`;
the shared receipt SHA-256 is
`2421379cacf795a7127dbbaf1adae935a1f231c0e46abbc0159e8f40908016a2`.
The [code review](code-review.md) lists exact finite coverage and the
parameter-depth conversion. The root separately confirmed all 25 preserved
source hashes and all retained original stdout hashes.

The full original supplied runs and their exact output hashes are recorded
in [original-runs/execution-record.json](original-runs/execution-record.json).
The source programs are archived unchanged. Original successful exit
codes are not interpreted as proof that every printed failure count is
zero.

## Repository gate

The required command is:

```sh
python -X utf8 -B tools/validate.py --regressions --receipt /tmp/collatz-intake-validation.json
```

The actual GitHub scientific commit was fetched into a complete clean
checkout and the command above was executed with regressions enabled:

- Commit: `b7fffad6e5513859d2878c922fccd166754787f0`.
- Tree: `0fdb4058139e422202f9ce0a9f35afd2e1b57e44`.
- Tracked files: 368.
- All 11 child commands exited successfully.
- The checkout remained clean at the same commit and tree after execution.
- [Actual receipt](repository-checkout.json), SHA-256
  `272d1f78c1179b526024502081a7d3041c31485523b493baaad3a1ea7c4905ec`.

The remote tree is byte-for-byte identical to the locally prepared tree
on which the new scientific checker was executed in both interpreter
modes. The publication follow-up adds this receipt and updates this note;
it does not change scientific files or the preserved uploads. This receipt
covers the named parent and does not claim to self-certify its own later
documentation commit. The pull request records the final remote-head check.

All new Markdown, Python, C and JSON files passed the scoped whitespace
check. The untouched historical question files and source stdout retain
their original terminal blank lines or trailing spaces; preserving those
bytes is intentional, and a blanket whitespace-clean claim is not made.

## What these checks do not claim

The new checker has bounded arithmetic scope. The repository gate checks
integrity and the existing bounded regression bundle. Neither is a Lean
build, external referee acceptance, a proof of every original experimental
claim, remote CI success, or a proof of Collatz.
