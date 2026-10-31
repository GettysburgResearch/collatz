# Bounded exact replay for the second swarm pass

These programs support the [research packet](../../research/beeping-density-swarm-20261031/README.md).
They use the Python standard library and exact integers or rational numbers
for acceptance checks. They do not solve Collatz, compute an infinite
spectrum numerically, or replay external formal developments.

## One reproducible command

From the repository root:

```bash
python -X utf8 -B experiments/beeping-density-swarm-20261031/replay_packet.py --output /tmp/collatz_second_swarm_replay.json
```

The driver runs all five suites in normal mode and again with `-O`. Each
run writes to a temporary directory and compares its **complete parsed JSON**
against the corresponding saved evidence file. Explicit exceptions keep
acceptance checks active under optimization. The driver never overwrites
the saved suite evidence. Its aggregate receipt records exact program hashes.

## Coverage and limits

| Program and saved output | Exact finite coverage | What the computation does not establish |
|---|---|---|
| [check_contact_transport.py](check_contact_transport.py), [contact_transport_checks.json](contact_transport_checks.json) | Template inequalities; 71 odd expanding-family instances; 58 unbounded-return instances; 47 occupation targets compared forward and backward with a proved complete source cutoff containing 2,779 contacts; finite-population flow residual and clock-mass identity. | The all-k theorem and all-target termination of the evaluator follow from the written proof, not sample extrapolation. No inverse supersolution is manufactured by the lift. |
| [check_contact_review.py](check_contact_review.py), [contact_review_checks.json](contact_review_checks.json) | Independently derived two templates, six witness polynomials, eight envelope inequalities, complete long-prefix cutoff certificates, and 24 family indices k=12,...,32,40,60,100. | Independence concerns the implementation and reconstruction within this session, not outside peer review or formal certification. |
| [check_inverse_green.py](check_inverse_green.py), [inverse_green_checks.json](inverse_green_checks.json) | 1,340 legal inverse words, 1,291 first-hit words, 156 packing comparisons, 2,730 graded renewal comparisons; exact infinite-geometric residue laws at 251 positive odd targets through depth six; 126 harmonic identities; 144 comparisons on 36 actual prefix-free frontiers. | No external fast-density premise is proved. The explicit non-prefix-free control fails in the predicted direction, 7/4>11/7. |
| [check_harmonic_spectrum.py](check_harmonic_spectrum.py), [harmonic_spectrum_checks.json](harmonic_spectrum_checks.json) | 12 transport cases; 120 unit-circle residuals; 240 truncated interior eigenvectors; six disjoint inverse rays; 26,461 first-hit product checks; 64 periodic-mass checks. | Infinite-dimensional spectrum and computability equivalence rely on the analytic proofs. No reachability oracle is implemented or assumed. |
| [check_critical_energy.py](check_critical_energy.py), [critical_energy_checks.json](critical_energy_checks.json) | Two independent exact constructions of the infinite-geometric residue law through ternary level six; 1,092 residue equations, 364 projective equations, normalization, and both energy-identity expressions. | No exponent distribution is truncated. Unbounded second moment and the clipping obstruction follow from the written argument, not the six levels. |

For an individual suite, use its script with `--output /tmp/name.json`; all
have deterministic default parameters. The energy suite additionally accepts
`--max-level`, with default six. Altered parameters produce a different
experiment and should not be compared to the saved default receipt.

The inverse and energy programs independently generate the reference law.
The contact programs independently implement Gamma/Phi evaluators rather
than importing the first packet's implementation. They remain corroborating
checks of stated finite certificates, not independent proofs of every
universal mathematical assertion.
