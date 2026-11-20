# Actual publication validation

## Executed scientific content

- Commit: `3aa75073e5d000b3ccf6ac29cbfbda1b14445c6c`.
- Tree: `5e79c89edd930adc6ff7fc2021e872c7c021a0bd`.
- Complete tracked checkout: 343 files; clean before and after.
- Scientific manifest:25 entries, SHA-256
  `92fac502920d0f83f69d581d818fe92ff2c676358023f77f73528bfbdd770fb4`.

The scientific driver executed each of the arithmetic, certificate and
energy programs normally and with `-OO`. All six returned zero,
reported success in their own declared schemas, and reproduced their
entire frozen JSON output byte for byte. This is bounded execution
evidence, separate from the written all-parameter proofs.

The repository validator executed its complete `--regressions` bundle
on the same actual commit. All eleven commands passed. The receipt's
before/after commit, tree and tracked-file count agree.

| Receipt | SHA-256 |
|---|---|
| [scientific-execution.json](scientific-execution.json) | `03fa5d5a2fb2dcfae41b98e48fc1e24bdd2eb309484469bf42b0a30972926243` |
| [repository-validation.json](repository-validation.json) | `921b19b84feaaac1036e29c2e0bd244ebc6af31a92451ec6ec15dc53f48ee87f` |

## Preserved initial failure

The first published content commit was
`5c266c164c9109292de5d478b774e5b4e718e4b9`, tree
`37e53edb74143c2635e8713a372fbe9fc91158d8`. Its first science-driver
attempt stopped after the two arithmetic executions and normal carry
execution had returned zero and matched their complete frozen reports.
The driver then incorrectly required a field named `status` from the
carry report, whose actual success field is Boolean `success`.

The next commit fixed that orchestration assumption and preserved the
failed receipt. It changed no mathematical proof, scientific program,
or frozen scientific output. The complete six-execution success above
is a fresh run on the actual corrected commit, not a reinterpretation
of the earlier incomplete execution. The earlier repository bundle
also passed; its receipt remains labeled with its earlier head.

## Publication child and exact final-head boundary

The publication child adds this document, the two successful receipts,
and the updated report README. Every manifest-listed file and the
manifest itself must be identical to the executed content commit.
The final checkout check verifies that parent relationship, the
restricted changed-path list, all 25 hashes and the complete manifest
identity. The mandatory repository bundle is then rerun on that actual
final head and its receipt is included in the PR description.

The six scientific executions recorded here belong to the content
commit. Their inputs are preserved exactly in the publication child;
this document does not mislabel them as executions on a future SHA.
Neither the repository checks nor the finite mathematical examples
prove Collatz, eliminate all cycles, validate the external theorems,
or show finite energy on the uncovered sources.
