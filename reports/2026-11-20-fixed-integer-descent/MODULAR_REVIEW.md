# Independent reconstruction of the homogeneous run certificate

Reviewer: the arithmetic research agent, separate from the author of the
modular scanner. This reviewer authored the adaptive core; its review of
M3 is therefore a cross-check of the interface, not a second independent
authorship of the core theorem. The root agent separately reconstructed
the core argument. These are agent reconstructions, not external peer
review or proof-assistant verification.

## Frozen scope

This prepublication review pins exact file bytes by SHA-256. The enclosing
publication record identifies their Git commit. The verdict does not
extend to later bytes or neighboring claims.

| Path | SHA-256 |
|---|---|
| `research/fixed-integer-descent/modular_hitting.md` | `bb757b452a003969dd9dde4668cc6c57f649260fbdc68341ebb01723c9f25785` |
| `experiments/fixed_integer_run_hitting.py` | `3580ddbf945030c9981959f3ab055d994c192917c04c26eda53c031d89f803b9` |
| `reports/2026-11-20-fixed-integer-descent/modular-run-hitting.json` | `10c2c6f8f3834a944795dfa1d170dbc79b55236ad3407adeb6ef6ca1e8e5a451` |

**M1: VERIFIED in its stated scope.** Reconstructed the order of 3 modulo
`2^m`, the two multiplicative cosets, both explicit high-run target
residues, the shift-by-one boundary at residue 1, and the projection from
ordinary integers to their low bits. A cyclic non-target interval of
length `H` gives hitting time at most `H`, without an extra step. The
maximum is exact for the finite test; it is only an upper bound for the
ordinary hitting time.

**M2: VERIFIED for the complete-scan algorithm and the reported scope.**
The scanner's initial bad anchor and final return ensure that it does
not miss a non-target interval crossing the representative. The endpoint
reset and witness trace were checked. The run-count implementation was
reconstructed independently as the count of high endpoints of binary
one-runs. The labels, maximum, representative witness, and ordered digest
are different pieces of evidence; a digest alone is not a proof.

The independent arithmetic investigation had already reproduced the
modulus-`2^20` maxima for caps 1 through 6. A second implementation now
reproduced the modulus-`2^24` constants required for caps 5 and 6:

| Cap | Shift 0 | Shift 1 |
|---:|---:|---:|
| 5 | 10 | 13 |
| 6 | 15 | 21 |

This reconstruction starts at 1 and 5 and joins the initial and final
non-target intervals. It does not search for the original scanner's bad
anchor, import its functions, or use its bit-count formula. It visited
8,388,608 residue states and performed 33,554,432 cap/shift tests. It
reproduced the maxima, not the original ordered digests. The larger
precision cap-7 and cap-8 maxima were inspected in the complete report
and scanner but were not replayed a second time by this reviewer.

**M3: VERIFIED in its stated conditional and capped scopes.** The
outside-core clock is the maximum of the two homogeneous bounds. The
separate bounds give

`B_R = R floor(H_1 log2 3) + (R-1)(2H_0-1)`.

An integer whose binary length exceeds this bound and whose initial run
count is at most `R` cannot be in the core. Combining the independent
13/21 bounds with the complete core replays gives 68/107 odd-event
alternatives. A draft sentence excluding "every positive cycle" was
corrected to "every nontrivial positive cycle" before this frozen review;
the trivial cycle remains. No global run cap or arbitrary-cycle exclusion
is established.

## Independent replay actually completed

```bash
python -X utf8 -B reports/2026-11-20-fixed-integer-descent/check_modular_independent_audit.py
```

The command completed and matched the frozen
[`modular-independent-audit.json`](modular-independent-audit.json).
The independent script has SHA-256
`50866599abf6cea175b8e7422d533ee7cbb1aedca275801a2a249aa392c0282f`;
the report has SHA-256
`4cb60c0fba7e1e6d15fa70f686486a3825df02ab8b2f6d2a0e6e7f6f3daa60b3`.

The first attempt to resume one execution was interrupted by an executor
transport reset. That interrupted execution is not counted as completed;
the subsequent complete replay above is the cited execution.
